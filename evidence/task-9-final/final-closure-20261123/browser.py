"""Local browser verification for payout configuration and fixed commercial terms."""
import json
import os
from datetime import datetime, timedelta, timezone
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient
import requests

web, api = "http://localhost:8089", "http://127.0.0.1:8283/api"
db = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0").comein_disposable_t9_closing_browser
now = datetime.now(timezone.utc)
email, password = f"biz-{uuid4().hex[:10]}@fixture.example", "Fixture-" + uuid4().hex
registered = requests.post(api + "/auth/register", json={"email": email, "password": password,
    "name": "Payout fixture", "phone": "5550100190"}, timeout=10)
registered.raise_for_status()
seller = registered.json()["user"]["id"]
from bson import ObjectId
db.users.update_one({"_id": ObjectId(seller)}, {"$set": {"role": "shopkeeper"}})
shop = db.shops.insert_one({"owner_id": seller, "name": "Campaign fixture", "status": "approved"}).inserted_id
ad = db.advertisements.insert_one({"owner_id": seller, "shop_id": str(shop), "status": "pending_owner_approval",
    "title": "Browser fixed campaign", "placement": "home_banner", "starts_at": now - timedelta(days=1),
    "ends_at": now + timedelta(days=1), "created_at": now}).inserted_id


def login(browser, email, password, destination):
    page = browser.new_page()
    page.route("https://**", lambda route: route.abort())
    page.goto(f"{web}/auth?next={destination}")
    page.get_by_test_id("auth-email").fill(email)
    page.get_by_test_id("auth-password").fill(password)
    page.get_by_test_id("auth-submit").click()
    return page


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    admin = login(browser, os.environ["COMEIN_TEST_ADMIN_EMAIL"], os.environ["COMEIN_TEST_ADMIN_PASSWORD"], "%2Fadmin-earnings")
    admin.get_by_text("Load payout schedule", exact=True).click()
    editor = admin.get_by_label("Payout schedule JSON")
    expect(editor).to_have_value(__import__("re").compile("expected_version"))
    schedule = json.loads(editor.input_value())
    schedule.update(cycle_start=now.isoformat(), reason="Fixture schedule review")
    editor.fill(json.dumps(schedule))
    admin.get_by_text("Save payout schedule", exact=True).click()
    expect(admin.get_by_text("Payout schedule version", exact=False)).to_be_visible()
    print("PASS Admin loads, edits and persists a versioned weekly payout schedule via the UI.")
    admin.get_by_placeholder("Campaign ID").fill(str(ad))
    admin.get_by_label("Campaign commercial terms JSON").fill(json.dumps({
        "model": "fixed_duration", "rate_paise": 1000, "daily_budget_paise": 1000,
        "total_budget_paise": 2000, "funding_reference": "Fixture funding", "objective": "Fixture",
        "target_area": "Fixture City", "reason": "Fixture terms accepted", "delivery_target_impressions": 2,
    }))
    admin.get_by_text("Save commercial terms", exact=True).click()
    expect(admin.get_by_text("Campaign terms saved for advertiser acceptance.", exact=True)).to_be_visible()
    seller_page = login(browser, email, password, "%2Fseller%2Fadvertisements")
    expect(seller_page.get_by_text("fixed duration · ₹10.00 · Fixture City", exact=True)).to_be_visible()
    seller_page.get_by_text("Accept displayed terms", exact=True).click()
    expect(seller_page.get_by_text("Commercial terms accepted", exact=True)).to_be_visible()
    assert db.advertisements.find_one({"_id": ad})["status"] == "pending_owner_approval"
    print("PASS Advertiser sees price and accepts terms while the moderation and owner gate stays pending.")
    seller_page.get_by_text("Load measured delivery", exact=True).click()
    expect(seller_page.get_by_text("0 measured impressions · 0 measured clicks · Reconciliation requires review", exact=True)).to_be_visible()
    print("PASS Seller sees measured delivery without inferred conversions.")
    db.advertisements.update_one({"_id": ad}, {"$set": {
        "poster_sha256": "fixture", "owner_approval": {"poster_sha256": "fixture"},
        "ends_at": datetime.now(timezone.utc),
    }})
    admin.get_by_label("Delivery review reason").fill("Fixture final review")
    admin.get_by_text("Record final delivery review", exact=True).click()
    expect(admin.get_by_text("Delivery review pending compensation policy", exact=False)).to_be_visible()
    seller_page.get_by_text("Load measured delivery", exact=True).click()
    expect(seller_page.get_by_text("0 measured impressions · 0 measured clicks · pending compensation policy", exact=True)).to_be_visible()
    print("PASS Admin records final delivery evidence and seller sees the pending compensation review.")
    admin.goto(f"{web}/admin")
    admin.get_by_text("Food support (", exact=False).click()
    admin.get_by_text("Open promotion drafts", exact=True).click()
    label = "Browser funded coupon " + uuid4().hex[:8]
    draft = {"name": label, "kind": "campaign", "starts_at": now.isoformat(),
             "expires_at": (now + timedelta(days=1)).isoformat(), "budget_paise": 10000,
             "max_benefit_paise": 1000, "customer_budget_paise": 1000, "min_order_paise": 0,
             "max_redemptions": 10, "per_customer_limit": 1, "funding_reference": "Fixture",
             "eligibility": "Signed-in customers", "terms": "Cash only", "cancellation_terms": "Release on unpaid cancellation",
             "refund_terms": "No cash refund", "discount_model": "fixed", "fixed_discount_paise": 100,
             "funding_allocation_basis_points": {"come_in": 10000}}
    admin.get_by_label("Promotion draft JSON").fill(json.dumps(draft))
    admin.get_by_text("Save promotion draft", exact=True).click()
    button = admin.get_by_text(f"Activate Grocery coupon for {label}", exact=True)
    expect(button).to_be_visible()
    code = "TEST" + uuid4().hex[:8].upper()
    admin.get_by_label("Grocery coupon activation JSON").fill(json.dumps({
        "code": code, "customer_scope": "all_signed_in", "release_unpaid_cancellation": True,
    }))
    button.click()
    expect(admin.get_by_text(f"Grocery cash coupon {code} active.", exact=True)).to_be_visible()
    assert db.financial_policy_drafts.find_one({"_id": f"coupon:{code}"})["redemptions"] == 0
    print("PASS Admin activated a Grocery coupon with no budget spent on activation.")
    admin.get_by_text("Load coupon campaigns", exact=True).click()
    admin.get_by_label("Coupon campaign change reason").fill("Fixture audit pause")
    admin.get_by_text(f"Set {code} paused", exact=True).click()
    expect(admin.get_by_text(f"{code} · paused", exact=False)).to_be_visible()
    assert db.financial_policy_drafts.find_one({"_id": f"coupon:{code}"})["status"] == "paused"
    print("PASS Admin pauses an existing coupon and the campaign remains persisted.")
    admin.get_by_text(f"Reconcile {code}", exact=True).click()
    expect(admin.get_by_text(f"{code}: balanced", exact=False)).to_be_visible()
    print("PASS Admin reconciles campaign budget, order receipts and audit totals.")
    browser.close()
