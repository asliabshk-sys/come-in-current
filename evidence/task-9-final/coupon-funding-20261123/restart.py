"""Exercise policy persistence across two real FastAPI processes on isolated MongoDB."""
import os
from datetime import datetime, timedelta, timezone
import subprocess
import sys
import time
from uuid import uuid4

from bson import ObjectId
from pymongo import MongoClient
import requests


base = "http://127.0.0.1:8270/api"
database = "comein_disposable_t9_coupon_restart_" + uuid4().hex[:16]
env = dict(os.environ, DB_NAME=database, MONGO_EXPECTED_DB_NAME=database)


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8270"],
        env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(80):
        if process.poll() is not None:
            raise RuntimeError("Restart fixture API exited during startup")
        try:
            if requests.get(base + "/health", timeout=0.5).status_code < 500:
                return process
        except requests.RequestException:
            pass
        time.sleep(0.25)
    process.terminate()
    process.wait(timeout=10)
    raise RuntimeError("Restart fixture API did not become ready")


def authenticate():
    response = requests.post(base + "/auth/login", json={
        "email": os.environ["COMEIN_TEST_ADMIN_EMAIL"], "password": os.environ["COMEIN_TEST_ADMIN_PASSWORD"],
    }, timeout=10)
    response.raise_for_status()
    return {"Authorization": "Bearer " + response.json()["token"]}


def api(path, headers, method="GET", body=None):
    response = requests.request(method, base + path, headers=headers, json=body, timeout=10)
    response.raise_for_status()
    return response.json()


mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = mongo[database]
now = datetime.now(timezone.utc)
campaign = "/admin/financial/grocery-coupons/RESTART"
reconciliation = campaign + "/reconciliation"
process = None
try:
    process = start()
    admin = authenticate()
    buyer = api("/auth/register", {}, "POST", {"email": "coupon@fixture.example",
                "password": "Fixture-" + uuid4().hex, "name": "Coupon restart", "phone": "5550100081"})
    customer = {"Authorization": "Bearer " + buyer["token"]}
    shop = db.shops.insert_one({"status": "approved", "delivery_available": True,
                               "payment_methods": ["cod"]}).inserted_id
    product = str(db.products.insert_one({"shop_id": str(shop), "category_id": "dairy", "name": "Coupon item",
                                          "unit": "pack", "price": 100, "stock": 10, "available": True}).inserted_id)
    draft = api("/admin/financial/promotion-drafts", admin, "POST", {
        "name": "Coupon restart fixture", "kind": "campaign",
        "starts_at": (now - timedelta(hours=1)).isoformat(), "expires_at": (now + timedelta(days=1)).isoformat(),
        "budget_paise": 2000, "max_benefit_paise": 2000, "customer_budget_paise": 2000, "min_order_paise": 5000,
        "max_redemptions": 10, "per_customer_limit": 1, "funding_reference": "Fixture funding",
        "eligibility": "Signed-in customers", "terms": "Cash fixture", "cancellation_terms": "Restore unpaid cancellation",
        "refund_terms": "Review only", "discount_model": "fixed", "fixed_discount_paise": 2000,
        "funding_allocation_basis_points": {"come_in": 10000},
    })
    api(f"/admin/financial/promotion-drafts/{draft['id']}/activate-grocery-coupon", admin, "POST",
        {"code": "RESTART", "customer_scope": "all_signed_in", "release_unpaid_cancellation": True})
    quote = api("/grocery/quotes", customer, "POST", {"items": [{"product_id": product, "qty": 1}], "coupon_code": "RESTART"})
    order = api("/orders", customer, "POST", {
        "items": [{"product_id": product, "qty": 1, "name": "Item", "price": 100, "unit": "pack", "shop_id": str(shop)}],
        "delivery_address": "Fixture address", "payment_method": "cod", "quote_token": quote["quote_token"],
        "idempotency_key": "coupon-restart-order",
    })
    before = api(reconciliation, admin)
    assert before["status"] == "balanced" and before["remaining_paise"] == 0
    api(campaign, admin, "PATCH", {"status": "closed", "expected_status": "active", "reason": "Fixture close"})
    process.terminate()
    process.wait(timeout=15)
    process = start()
    admin = authenticate()
    assert api(reconciliation, admin) == before
    rows = api("/admin/financial/grocery-coupons", admin)
    assert any(row["activation"]["code"] == "RESTART" and row["status"] == "closed" for row in rows)
    print("PASS restarted API preserved terminal status, campaign counters, order receipt and spent audit reconciliation")
    for _ in range(2):
        result = api(f"/orders/{order['id']}/cancel", customer, "POST", {})
        assert result["coupon_redemption"]["state"] == "released"
    after = api(reconciliation, admin)
    assert after["status"] == "balanced" and after["remaining_paise"] == 2000
    assert db.financial_audit.count_documents({"coupon_code": "RESTART", "action": "grocery_coupon_released"}) == 1
    print("PASS after restart an eligible unpaid cancellation restored budget exactly once despite closure and replay")
finally:
    if process is not None and process.poll() is None:
        process.terminate()
        process.wait(timeout=15)
    mongo.drop_database(database)
    mongo.close()
