"""Local Restaurant seller and customer replacement smoke test."""

import json
import os
import secrets
from datetime import datetime, timezone

from bson import ObjectId
from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient
import requests


api = "http://127.0.0.1:8180/api"
web = "http://localhost:8081"
suffix = secrets.token_hex(4)
password = "LocalOnly-" + secrets.token_hex(12)
mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = mongo.comein_disposable_task9_closure
users = {}
for actor in ("buyer", "seller"):
    email = f"task9-{actor}-{suffix}@fixture.example"
    response = requests.post(f"{api}/auth/register", json={
        "name": f"Task Nine {actor}", "email": email, "password": password,
        "phone": "5550100049",
    }, timeout=10)
    response.raise_for_status()
    users[actor] = (email, response.json()["user"]["id"])

buyer, seller = (users[key][1] for key in ("buyer", "seller"))
db.users.update_one({"_id": ObjectId(seller)}, {"$set": {"role": "shopkeeper"}})

restaurant = db.restaurants.insert_one({
    "owner_id": seller, "name": "Task Nine Kitchen", "status": "approved", "available": True, "tax_rate": 10,
}).inserted_id
original = ObjectId()
db.restaurant_menu.insert_one({
    "restaurant_id": str(restaurant), "name": "Fresh Bowl", "category": "Main", "price": 160,
    "available": True, "variants": [], "add_ons": [],
})
order = db.restaurant_orders.insert_one({
    "restaurant_id": str(restaurant), "restaurant_owner_id": seller,
    "restaurant_name": "Task Nine Kitchen", "customer_id": buyer, "ref": "TASK9-FOOD",
    "status": "preparing", "payment_method": "cod", "payment_status": "cod_pending", "fulfillment": "pickup",
    "items": [{"menu_item_id": str(original), "name": "Green Soup", "quantity": 1, "unit_price": 130}],
    "subtotal": 130, "tax": 13, "delivery_fee": 0, "total": 143, "created_at": datetime.now(timezone.utc),
}).inserted_id


def login(browser, actor, destination):
    page = browser.new_page(viewport={"width": 425, "height": 950})
    page.route("https://**", lambda route: route.abort())
    page.goto(f"{web}/auth?next={destination}")
    page.get_by_test_id("auth-email").fill(os.environ["COMEIN_TEST_ADMIN_EMAIL"] if actor == "admin" else users[actor][0])
    page.get_by_test_id("auth-password").fill(os.environ["COMEIN_TEST_ADMIN_PASSWORD"] if actor == "admin" else password)
    page.get_by_test_id("auth-submit").click()
    return page


with sync_playwright() as p:
    chromium = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_BIN", "/usr/bin/chromium"), args=["--no-sandbox"])
    seller_page = login(chromium, "seller", "%2Frestaurant%2Fdashboard")
    seller_page.get_by_role("button", name="Report Green Soup unavailable").click()
    seller_page.get_by_role("button", name="Offer Fresh Bowl", exact=True).click()
    expect(seller_page.get_by_text("Awaiting customer decision")).to_be_visible()
    buyer_page = login(chromium, "buyer", "%2Fnotifications")
    buyer_page.get_by_text("A restaurant order item is unavailable", exact=True).click()
    expect(buyer_page.get_by_text("New order total ₹176.00 · delivery ₹0.00 · tax ₹16.00")).to_be_visible()
    buyer_page.get_by_role("button", name="Accept Fresh Bowl · ₹176.00 total").click()
    expect(buyer_page.get_by_text("Replacement confirmed", exact=True)).to_be_visible()
    saved = db.restaurant_orders.find_one({"_id": order})
    assert saved["total"] == 176 and saved["tax"] == 16 and saved["payment_status"] == "cod_pending"
    print("PASS Restaurant seller proposal, customer notification, tax review, approval and cash-status preservation.")
    paid = db.restaurant_orders.find_one({"_id": order})
    paid.update({
        "_id": ObjectId(), "ref": "TASK9-FIN-BROWSER", "idempotency_key": "fixture-fin-" + suffix, "payment_method": "razorpay",
        "payment_status": "paid", "items": [{"menu_item_id": str(original), "name": "Paid Soup", "quantity": 1, "unit_price": 130}],
        "subtotal": 130, "tax": 13, "total": 143, "invoice_id": "historic-fixture", "coupon_discount": 5,
    })
    paid.pop("replacements", None)
    db.restaurant_orders.insert_one(paid)
    seller_page.reload()
    seller_page.get_by_role("button", name="Report Paid Soup unavailable").click()
    seller_page.get_by_role("button", name="Offer Fresh Bowl", exact=True).click()
    buyer_page.goto(f"{web}/restaurant/orders/{paid['_id']}")
    buyer_page.get_by_role("button", name="Reject these replacements").click()
    buyer_page.get_by_role("button", name="Request item removal").click()
    expect(buyer_page.get_by_text("Your decision was sent to Assist.", exact=False)).to_be_visible()
    admin_page = login(chromium, "admin", "%2Fadmin")
    admin_page.get_by_text("Food support (", exact=False).click()
    ticket = db.restaurant_support.find_one({"order_id": str(paid["_id"])})
    card = admin_page.get_by_text(f"{ticket['ref']} · wrong_or_missing_item", exact=True).locator("..")
    expect(card.get_by_text("Financial review pending · No financial action confirmed", exact=True)).to_be_visible()
    expect(card.get_by_text("reward review · historical tax review · payment review", exact=True)).to_be_visible()
    expect(card.get_by_text("Original total ₹143 · Decision keep_unavailable", exact=True)).to_be_visible()
    assert db.restaurant_orders.find_one({"_id": paid["_id"]})["invoice_id"] == "historic-fixture"
    print("PASS Admin saw combined financial blockers and the recorded removal request with no confirmed financial action.")
    card.get_by_text("Open financial review", exact=True).click()
    card.get_by_label("Financial review reason").fill("Preserve the existing shopping reward ledger")
    card.get_by_text("Reject reward adjustment", exact=True).click()
    expect(card.get_by_text("reward · rejected", exact=False)).to_be_visible()
    updated = db.restaurant_support.find_one({"order_id": str(paid["_id"])})
    assert updated["financial_review"]["reward_status"] == "rejected"
    assert not updated["financial_review"]["financial_action_confirmed"]
    print("PASS Admin recorded a reasoned reward rejection without financial execution.")
    admin_page.get_by_text("Open promotion drafts", exact=True).click()
    draft = {
        "name": "Fixture Welcome " + suffix, "kind": "welcome", "starts_at": "2026-11-01T00:00:00Z",
        "expires_at": "2026-12-01T00:00:00Z", "budget_paise": 10000, "max_benefit_paise": 100,
        "customer_budget_paise": 500, "max_redemptions": 10, "per_customer_limit": 1,
        "min_order_paise": 0, "funding_reference": "fixture", "eligibility": "fixture",
        "terms": "fixture", "cancellation_terms": "fixture", "refund_terms": "fixture",
    }
    admin_page.get_by_label("Promotion draft JSON").fill(json.dumps(draft))
    admin_page.get_by_text("Save promotion draft", exact=True).click()
    expect(admin_page.get_by_text("Draft saved. Redemption remains disabled.", exact=True)).to_be_visible()
    assert db.financial_policy_drafts.find_one({"name": draft["name"]})["redemption_enabled"] is False
    print("PASS Admin saved a budgeted promotion draft with redemption disabled.")
    cheaper = dict(paid, _id=ObjectId(), ref="TASK9-CHEAPER", idempotency_key="fixture-cheaper-" + suffix,
                   items=[{"menu_item_id": str(original), "name": "Cheaper fixture original", "quantity": 1, "unit_price": 130}])
    cheaper.pop("invoice_id")
    cheaper.pop("coupon_discount")
    db.restaurant_orders.insert_one(cheaper)
    db.restaurant_menu.insert_one({"restaurant_id": str(restaurant), "name": "Budget Bowl", "category": "Main",
                                  "price": 80, "available": True, "variants": [], "add_ons": []})
    seller_page.reload()
    seller_page.get_by_role("button", name="Report Cheaper fixture original unavailable").click()
    seller_page.get_by_role("button", name="Offer Budget Bowl", exact=True).click()
    buyer_page.goto(f"{web}/restaurant/orders/{cheaper['_id']}")
    expect(buyer_page.get_by_text("Proposed order total ₹88.00 · Potential refund ₹55.00 pending review", exact=True)).to_be_visible()
    buyer_page.get_by_role("button", name="Approve Budget Bowl for Assist review").click()
    expect(buyer_page.get_by_text("Your decision was sent to Assist.", exact=False)).to_be_visible()
    admin_page.reload()
    admin_page.get_by_text("Food support (", exact=False).click()
    ticket = db.restaurant_support.find_one({"order_id": str(cheaper["_id"])})
    card = admin_page.get_by_text(f"{ticket['ref']} · wrong_or_missing_item", exact=True).locator("..")
    card.get_by_text("Open financial review", exact=True).click()
    card.get_by_label("Financial review reason").fill("Verify the quoted replacement refund")
    card.get_by_text("Approve refund for pending execution", exact=True).click()
    expect(card.get_by_text("Refund review · approved pending execution", exact=True)).to_be_visible()
    assert db.restaurant_orders.find_one({"_id": cheaper["_id"]})["total"] == 143
    assert db.restaurant_payments.count_documents({"order_id": str(cheaper["_id"])}) == 0
    print("PASS cheaper paid replacement quote, customer consent, Admin approval pending execution and unchanged payment.")
    orders = []
    for _ in range(10):
        qualifying = db.orders.insert_one({"customer_id": str(ObjectId()), "total": 100, "status": "delivered",
                                           "payment_status": "paid", "order_kind": "grocery"}).inserted_id
        orders.append({"order_id": str(qualifying), "kind": "grocery"})
    reward = db.referral_rewards.insert_one({"referrer_id": buyer, "status": "pending_verification",
                                          "reward_key": "fixture-" + suffix, "qualifying_orders": orders}).inserted_id
    admin_login = requests.post(api + "/auth/login", json={
        "email": os.environ["COMEIN_TEST_ADMIN_EMAIL"], "password": os.environ["COMEIN_TEST_ADMIN_PASSWORD"],
    }, timeout=10)
    admin_login.raise_for_status()
    result = requests.patch(f"{api}/admin/referral-rewards/{reward}", json={"decision": "approve"},
        headers={"Authorization": "Bearer " + admin_login.json()["token"]}, timeout=10)
    result.raise_for_status()
    buyer_page.goto(f"{web}/notifications")
    buyer_page.get_by_text("Referral reward approved", exact=True).click()
    buyer_page.wait_for_url("**/referral-dashboard")
    print("PASS notification from an actual referral review opens the customer's Referral & Earn screen.")
    chromium.close()
