"""Exercise the exported UI against a loopback API and disposable Mongo replica set."""
import os
from datetime import datetime, timezone
from uuid import uuid4
from urllib.parse import quote

import requests
from bson import ObjectId
from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient

web = "http://127.0.0.1:8294"
api = "http://127.0.0.1:8293/api"
assert os.environ["DB_NAME"] == "comein_disposable_t9ops_browser"
db = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")[os.environ["DB_NAME"]]
now = datetime.now(timezone.utc)


def request(method, path, body=None, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    response = requests.request(method, api + path, json=body, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def register(role):
    email, password = f"{role}-{uuid4().hex[:10]}@fixture.example", f"Fixture-{uuid4().hex}"
    registered = request("POST", "/auth/register", {"email": email, "password": password,
        "name": f"Fixture {role}", "phone": "5550100190"})
    user_id = registered["user"]["id"]
    db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"role": role}})
    token = request("POST", "/auth/login", {"email": email, "password": password})["token"]
    return user_id, token, (email, password)


buyer, _, customer_login = register("customer")
seller, seller_token, _ = register("shopkeeper")
admin_login = (os.environ["COMEIN_TEST_ADMIN_EMAIL"], os.environ["COMEIN_TEST_ADMIN_PASSWORD"])
shop = str(db.shops.insert_one({"owner_id": seller, "name": "Fixture Shop", "status": "approved"}).inserted_id)
restaurant = str(db.restaurants.insert_one({"owner_id": seller, "name": "Fixture Kitchen", "tax_rate": 10}).inserted_id)

common = {"customer_id": buyer, "status": "accepted", "fulfillment": "delivery", "payment_method": "cod",
          "payment_status": "cod_pending", "status_history": [{"status": "accepted", "at": now}], "created_at": now}
milk, substitute, rice = [ObjectId() for _ in range(3)]
db.products.insert_many([
    {"_id": oid, "shop_id": shop, "name": name, "price": price, "stock": stock, "available": True,
     "category_id": category, "unit": "pack"}
    for oid, name, price, stock, category in [(milk, "Old Milk", 130, 0, "dairy"),
        (substitute, "Fresh Milk", 160, 10, "dairy"), (rice, "Rice", 50, 10, "grains")]
])
grocery_items = [{"product_id": str(oid), "shop_id": shop, "name": name, "price": price, "qty": 1,
                  "category_id": category, "unit": "pack"}
                 for oid, name, price, category in [(milk, "Old Milk", 130, "dairy"), (rice, "Rice", 50, "grains")]]
grocery_id = db.orders.insert_one({**common, "ref": "BROWSER-GROCERY", "shop_id": shop, "items": grocery_items,
                                  "subtotal": 180, "delivery_fee": 29, "total": 209}).inserted_id
grocery = request("POST", f"/orders/{grocery_id}/replacements", {"line_index": 0, "product_id": str(milk), "qty": 1}, seller_token)

soup, bowl, side = [ObjectId() for _ in range(3)]
db.restaurant_menu.insert_many([
    {"_id": oid, "restaurant_id": restaurant, "name": name, "price": price, "available": True}
    for oid, name, price in [(bowl, "Bowl", 70), (side, "Side", 25)]
])
food_id = db.restaurant_orders.insert_one({**common, "ref": "BROWSER-FOOD", "restaurant_id": restaurant,
    "restaurant_name": "Fixture Kitchen", "restaurant_owner_id": seller,
    "items": [{"menu_item_id": str(soup), "name": "Soup", "unit_price": 50, "quantity": 2, "instructions": ""},
              {"menu_item_id": str(side), "name": "Side", "unit_price": 25, "quantity": 1, "instructions": ""}],
    "subtotal": 125, "tax": 12.5, "delivery_fee": 15, "total": 152.5}).inserted_id
food = request("POST", f"/restaurant/orders/{food_id}/replacements",
    {"line_index": 0, "menu_item_id": str(soup), "alternatives": [{"menu_item_id": str(bowl), "quantity": 2}]}, seller_token)
legacy_id = db.orders.insert_one({**common, "ref": "BROWSER-LEGACY", "shop_id": shop, "items": grocery_items,
                                  "subtotal": 180, "delivery_fee": 29, "total": 209}).inserted_id
legacy = request("POST", f"/orders/{legacy_id}/replacements", {"line_index": 0, "product_id": str(milk), "qty": 1}, seller_token)
db.orders.update_one({"_id": legacy_id}, {"$unset": {"replacements.0.active_offer": "",
                                                    "replacements.0.offer_sequence": "", "replacements.0.offer_history": ""}})


def signed_in_page(browser, credentials, path):
    page = browser.new_page()
    page.route("https://**", lambda route: route.abort())
    page.goto(f"{web}/auth?next={quote(path, safe='')}")
    page.get_by_test_id("auth-email").fill(credentials[0])
    page.get_by_test_id("auth-password").fill(credentials[1])
    page.get_by_test_id("auth-submit").click()
    return page


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    admin = signed_in_page(browser, admin_login, "/admin")
    admin.get_by_test_id("admin-tab-support").click()
    admin.get_by_label("Replacement order ID").fill(str(grocery_id))
    admin.get_by_label("Replacement case ID").fill(grocery["id"])
    admin.get_by_text("Load active offer", exact=True).click()
    admin.get_by_label("Individual expiry duration").fill("20")
    admin.get_by_label("Individual expiry adjustment reason").fill("Browser fixture verifies adjustment")
    admin.get_by_text("Adjust active offer expiry", exact=True).click()
    expect(admin.get_by_text("Expiry updated and the customer was notified.", exact=True)).to_be_visible()
    assert db.orders.find_one({"_id": grocery_id})["replacements"][0]["active_offer"]["duration_minutes"] == 20
    print("PASS Admin adjusts an individual active offer")
    admin.get_by_label("Replacement order ID").fill(str(legacy_id))
    admin.get_by_label("Replacement case ID").fill(legacy["id"])
    admin.get_by_text("Review legacy migration eligibility", exact=True).click()
    expect(admin.get_by_text("Selected offer · Eligible 1 · Excluded 0 · Ambiguous 0 · Already enrolled 0")).to_be_visible()
    expect(admin.get_by_text("The offer keeps its existing terms for 24 hours.", exact=False)).to_be_visible()
    assert "legacy_migration" not in db.orders.find_one({"_id": legacy_id})["replacements"][0]
    print("PASS Admin eligibility preview is read-only and shows the notice and activation policy")
    admin.get_by_text("Confirm enrollment and notify customer", exact=True).click()
    expect(admin.get_by_text("Migration status: grace", exact=True)).to_be_visible()
    assert db.orders.find_one({"_id": legacy_id})["replacements"][0]["legacy_migration"]["status"] == "grace"
    print("PASS Admin enrolls an eligible legacy case and sees grace status")

    for kind, page_path, collection, oid, revised_total in [
        ("Grocery", f"/order-tracking?id={grocery_id}", db.orders, grocery_id, 79),
        ("Restaurant", f"/restaurant/orders/{food_id}", db.restaurant_orders, food_id, 42.5),
    ]:
        customer = signed_in_page(browser, customer_login, page_path)
        customer.get_by_text("Withdraw from replacement", exact=True).click()
        expect(customer.get_by_text("You withdrew from replacement. Your order remains open.")).to_be_visible()
        customer.get_by_text("Review item removal", exact=True).click()
        expect(customer.get_by_text(f"Revised total ₹{revised_total:.2f}", exact=False)).to_be_visible()
        assert len(collection.find_one({"_id": oid})["items"]) == 2
        customer.get_by_text("Confirm item removal", exact=True).click()
        expect(customer.get_by_text("Customer continued without this item", exact=True)).to_be_visible()
        persisted = collection.find_one({"_id": oid})
        assert persisted["total"] == revised_total and len(persisted["items"]) == 1
        print(f"PASS {kind} customer withdraws, reviews the total and confirms removal")
    browser.close()
