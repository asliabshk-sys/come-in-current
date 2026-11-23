"""Local Restaurant seller and customer replacement smoke test."""

import os
import secrets
from datetime import datetime, timezone

from bson import ObjectId
from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient
import requests


api = "http://127.0.0.1:8109/api"
web = "http://localhost:8081"
suffix = secrets.token_hex(4)
password = "LocalOnly-" + secrets.token_hex(12)
mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = mongo.comein_disposable_task9_close
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
    page.get_by_test_id("auth-email").fill(users[actor][0])
    page.get_by_test_id("auth-password").fill(password)
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
    chromium.close()
