"""Repeatable local seller, Grocery customer and COME-IN Assist smoke test."""

import os
import secrets
from datetime import datetime, timezone

from bson import ObjectId
from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient
import requests


api = "http://127.0.0.1:8099/api"
web = "http://localhost:8081"
suffix = secrets.token_hex(4)
password = "LocalOnly-" + secrets.token_hex(12)
mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = mongo.comein_disposable_task9_final
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
shop = db.shops.insert_one({"owner_id": seller, "name": "Task Nine Grocery", "status": "approved", "online": True}).inserted_id
base_product = {"shop_id": str(shop), "available": True, "category_id": "dairy", "unit": "1 L"}
original = db.products.insert_one({**base_product, "name": "Green Milk", "price": 130, "stock": 0}).inserted_id
db.products.insert_one({**base_product, "name": "Fresh Milk", "price": 160, "stock": 3})
order = db.orders.insert_one({
    "shop_id": str(shop), "customer_id": buyer, "ref": "TASK9-BROWSER",
    "status": "preparing", "payment_method": "cod", "payment_status": "cod_pending", "fulfillment": "delivery",
    "items": [{"product_id": str(original), "name": "Green Milk", "unit": "1 L", "qty": 1, "price": 130, "category_id": "dairy"},
              {"product_id": str(ObjectId()), "name": "Rice", "unit": "1 kg", "qty": 1, "price": 50}],
    "subtotal": 180, "delivery_fee": 29, "total": 209, "created_at": datetime.now(timezone.utc),
}).inserted_id


def login(browser, actor, destination):
    page = browser.new_page(viewport={"width": 425, "height": 950})
    page.route("https://**", lambda route: route.abort())
    page.goto(f"{web}/auth?next={destination}")
    page.get_by_test_id("auth-email").fill(users[actor][0])
    page.get_by_test_id("auth-password").fill(password)
    page.get_by_test_id("auth-submit").click()
    return page


with sync_playwright() as p:
    chromium = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_BIN", "/usr/bin/chromium"), args=["--no-sandbox"])
    seller_page = login(chromium, "seller", "%2Fseller%2Forders")
    seller_page.get_by_role("button", name="Report Green Milk (1 L) unavailable").click()
    expect(seller_page.get_by_text("Awaiting customer decision")).to_be_visible()
    print("PASS Seller reported missing item and saw the pending customer decision.")
    buyer_page = login(chromium, "buyer", "%2Fnotifications")
    buyer_page.get_by_text("An order item is unavailable", exact=True).click()
    expect(buyer_page.get_by_text("New order total ₹210.00 · delivery ₹0.00")).to_be_visible()
    buyer_page.get_by_role("button", name="Contact COME-IN Assist").click()
    expect(buyer_page.get_by_test_id(f"chand-order-{order}")).to_be_visible()
    buyer_page.get_by_text("Wrong / missing item", exact=True).click()
    buyer_page.get_by_test_id("chand-support-message").fill("Please verify the stock before I choose a replacement.")
    buyer_page.get_by_test_id("chand-support-submit").click()
    buyer_page.get_by_test_id("chand-support-confirm").click()
    expect(buyer_page.get_by_text("Your support cases", exact=True)).to_be_visible()
    ticket = db.restaurant_support.find_one({"order_id": str(order), "user_id": buyer})
    assert ticket is not None and ticket["category"] == "wrong_or_missing_item"
    seller_page.goto(f"{web}/seller/support")
    expect(seller_page.get_by_text(ticket["ref"], exact=True)).to_be_visible()
    expect(seller_page.get_by_text("Please verify the stock before I choose a replacement.", exact=True)).to_be_visible()
    print("PASS The customer submitted an order-linked COME-IN Assist ticket from the notification flow, and the seller received it.")
    buyer_page.goto(f"{web}/order-tracking?id={order}&kind=grocery")
    buyer_page.get_by_role("button", name="Accept Fresh Milk · ₹210.00 total").click()
    expect(buyer_page.get_by_text("Replacement confirmed", exact=True)).to_be_visible()
    expect(buyer_page.get_by_text("Confirmed order total ₹210.00 · was ₹209.00")).to_be_visible()
    seller_page.goto(f"{web}/seller/orders")
    expect(seller_page.get_by_text("Replacement confirmed", exact=True)).to_be_visible()
    stored = db.orders.find_one({"_id": order})
    assert stored["payment_status"] == "cod_pending" and stored["total"] == 210
    print("PASS Customer approved the displayed total; the seller saw the decision and the order stayed COD pending.")
    chromium.close()
