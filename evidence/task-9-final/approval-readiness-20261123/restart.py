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


base = "http://127.0.0.1:8262/api"
env = dict(os.environ, DB_NAME="comein_disposable_t9_approval_restart", MONGO_EXPECTED_DB_NAME="comein_disposable_t9_approval_restart")


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8262"],
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


promotion = {
    "name": "Restart fixture " + uuid4().hex[:8], "kind": "sponsored",
    "starts_at": "2026-11-01T00:00:00Z", "expires_at": "2026-12-01T00:00:00Z",
    "budget_paise": 10_000, "max_benefit_paise": 100, "customer_budget_paise": 300,
    "max_redemptions": 20, "per_customer_limit": 2, "min_order_paise": 500,
    "funding_reference": "audit fixture", "eligibility": "fixture customer segment",
    "terms": "fixture terms", "cancellation_terms": "fixture cancellation",
    "refund_terms": "fixture refund", "category_ids": ["food", "food", "beverages"],
}
path = "/admin/financial/promotion-drafts"
mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = mongo[env["DB_NAME"]]


def financial_fixture(admin_headers):
    account = requests.post(base + "/auth/register", json={
        "email": f"audit-{uuid4().hex[:10]}@fixture.example", "password": "Fixture-" + uuid4().hex,
        "name": "Restart fixture", "phone": "5550100081",
    }, timeout=10)
    account.raise_for_status()
    buyer = account.json()
    restaurant = db.restaurants.insert_one({"name": "Fixture Kitchen", "tax_rate": 10}).inserted_id
    original, option = ObjectId(), ObjectId()
    db.restaurant_menu.insert_one({"_id": option, "restaurant_id": str(restaurant), "name": "Fixture replacement", "price": 100})
    order = db.restaurant_orders.insert_one({
        "customer_id": buyer["user"]["id"], "restaurant_id": str(restaurant), "status": "preparing",
        "ref": "AUDIT-RESTART", "fulfillment": "pickup", "payment_method": "razorpay", "payment_status": "paid",
        "items": [{"menu_item_id": str(original), "name": "Fixture original", "quantity": 1, "unit_price": 50}],
        "subtotal": 50, "tax": 5, "delivery_fee": 0, "total": 55,
    }).inserted_id
    offer = requests.post(f"{base}/restaurant/orders/{order}/replacements", headers=admin_headers, json={
        "line_index": 0, "menu_item_id": str(original), "alternatives": [{"menu_item_id": str(option), "quantity": 1}],
    }, timeout=10)
    offer.raise_for_status()
    case = offer.json()
    decision = requests.post(f"{base}/restaurant/orders/{order}/replacements/{case['id']}/decision",
        headers={"Authorization": "Bearer " + buyer["token"]},
        json={"action": "accept", "option_id": case["options"][0]["id"]}, timeout=10)
    decision.raise_for_status()
    db.restaurant_payments.insert_one({
        "order_id": str(order), "customer_id": buyer["user"]["id"], "status": "paid", "amount": 55,
        "currency": "INR", "gateway": "razorpay", "gateway_order_id": "order_fixture",
        "gateway_payment_id": "pay_fixture",
    })
    review_path = f"/admin/restaurant/support/{case['support_id']}/financial-review"
    approval = {"replacement_id": case["id"], "stage": "collection", "decision": "approve", "reason": "Isolated review test"}
    result = requests.post(base + review_path, headers=admin_headers, json=approval, timeout=10)
    result.raise_for_status()
    assert result.json() == {"status": "approved_pending_execution", "financial_action_confirmed": False}
    return review_path, approval, order, case["support_id"]
first = start()
try:
    headers = authenticate()
    created = requests.post(base + path, headers=headers, json=promotion, timeout=10)
    created.raise_for_status()
    saved = created.json()
    assert saved["status"] == "draft" and saved["redemption_enabled"] is False
    assert saved["category_ids"] == ["beverages", "food"]
    print("PASS process 1 saved normalized promotion fields; redemption is disabled.")
    review_path, approval, order, ticket_id = financial_fixture(headers)
    evidence_time = datetime.now(timezone.utc)
    ad = db.advertisements.insert_one({
        "starts_at": evidence_time - timedelta(days=2), "ends_at": evidence_time - timedelta(days=1),
        "status": "approved", "poster_sha256": "fixture",
        "owner_approval": {"poster_sha256": "fixture"},
        "commercial_terms": {"model": "fixed_duration", "accepted_at": evidence_time - timedelta(days=3),
                             "delivery_target_impressions": 1, "version": 1, "rate_paise": 1000},
    }).inserted_id
    ad_path = f"/admin/advertisements/{ad}/delivery-review"
    ad_reason = {"reason": "Isolated final delivery review"}
    ad_review = requests.post(base + ad_path, headers=headers, json=ad_reason, timeout=10)
    ad_review.raise_for_status()
    assert ad_review.json()["status"] == "pending_compensation_policy"
finally:
    first.terminate()
    first.wait(timeout=15)

second = start()
try:
    headers = authenticate()
    response = requests.get(base + path, headers=headers, timeout=10)
    response.raise_for_status()
    loaded = next(draft for draft in response.json() if draft["id"] == saved["id"])
    assert loaded == saved
    replay = requests.post(base + path, headers=headers, json=promotion, timeout=10)
    replay.raise_for_status()
    assert replay.json() == loaded
    print("PASS process 2 retrieved the same draft and caps; replay reused the identifier.")
    review = requests.get(base + review_path, headers=headers, timeout=10)
    review.raise_for_status()
    assert [row["status"] for row in review.json()["audit"]] == ["approved_pending_execution"]
    contract = review.json()["audit"][0]["payment_contract"]
    assert contract["status"] == "execution_disabled" and contract["amount_paise"] == 5500
    assert contract["original_payment_evidence"]["status"] == "linked_capture_recorded"
    assert contract["provider_order_preview"]["notes"]["original_payment_id"] == "pay_fixture"
    preflight = requests.get(base + review_path.replace("/financial-review", "/payment-readiness/collection"),
                             headers=headers, timeout=10)
    preflight.raise_for_status()
    assert preflight.json()["reference"] == contract["reference"]
    assert preflight.json()["status"] == "execution_disabled"
    print("PASS process 2 revalidated the persisted provider request preview from the original synthetic capture.")
    ad_reply = requests.post(base + ad_path, headers=headers, json=ad_reason, timeout=10)
    ad_reply.raise_for_status()
    assert ad_reply.json() == ad_review.json()
    assert db.advertisement_audit.count_documents({"advertisement_id": str(ad), "event": "delivery_review_recorded"}) == 1
    print("PASS process 2 replayed the same immutable ended-campaign review without compensation.")
    replay_review = requests.post(base + review_path, headers=headers, json=approval, timeout=10)
    replay_review.raise_for_status()
    assert replay_review.json()["financial_action_confirmed"] is False
    assert db.financial_audit.count_documents({"ticket_id": ticket_id, "stage": "collection"}) == 1
    assert db.restaurant_orders.find_one({"_id": order})["total"] == 55
    assert db.restaurant_payments.count_documents({"order_id": str(order)}) == 1
    print("PASS process 2 reloaded pending collection and its audit; replay created no duplicate or payment.")
finally:
    second.terminate()
    second.wait(timeout=15)
