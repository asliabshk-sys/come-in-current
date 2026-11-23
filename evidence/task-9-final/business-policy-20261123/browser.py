"""Local browser verification for payout configuration and fixed commercial terms."""
import json
import os
from datetime import datetime, timedelta, timezone
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient
import requests

web, api = "http://localhost:8081", "http://127.0.0.1:8190/api"
db = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0").comein_disposable_task9_biz
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
        "target_area": "Fixture City", "reason": "Fixture terms accepted",
    }))
    admin.get_by_text("Save commercial terms", exact=True).click()
    expect(admin.get_by_text("Campaign terms saved for advertiser acceptance.", exact=True)).to_be_visible()
    seller_page = login(browser, email, password, "%2Fseller%2Fadvertisements")
    expect(seller_page.get_by_text("fixed duration · ₹10.00 · Fixture City", exact=True)).to_be_visible()
    seller_page.get_by_text("Accept displayed terms", exact=True).click()
    expect(seller_page.get_by_text("Commercial terms accepted", exact=True)).to_be_visible()
    assert db.advertisements.find_one({"_id": ad})["status"] == "pending_owner_approval"
    print("PASS Advertiser sees price and accepts terms while the moderation and owner gate stays pending.")
    browser.close()
