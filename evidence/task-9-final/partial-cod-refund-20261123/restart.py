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


base = "http://127.0.0.1:8274/api"
database = "comein_disposable_t9_cod_restart_" + uuid4().hex[:16]
env = dict(os.environ, DB_NAME=database, MONGO_EXPECTED_DB_NAME=database)


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8274"],
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





if __name__ == "__main__":
    mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
    db = mongo[database]
    process = None
    try:
        process = start()
        admin = authenticate()
        account = api("/auth/register", {}, "POST", {"email": "merchant@fixture.example",
            "password": "Fixture-" + uuid4().hex, "name": "COD fixture", "phone": "5550100081"})
        merchant = account["user"]["id"]
        db.users.update_one({"_id": ObjectId(merchant)}, {"$set": {"role": "shopkeeper"}})
        headers = {"Authorization": "Bearer " + account["token"]}
        restaurant = str(db.restaurants.insert_one({"owner_id": merchant, "financial_policy_updated_at": datetime.now(timezone.utc) - timedelta(days=1),
            "commission_rate_percent": 0, "platform_service_fee_inr": 0, "delivery_fee_beneficiary": "platform"}).inserted_id)
        customer = str(ObjectId())
        oid = db.restaurant_orders.insert_one({"restaurant_id": restaurant, "customer_id": customer,
            "fulfillment": "delivery", "delivery_fee": 15, "total": 150, "subtotal": 135, "status": "delivered",
            "payment_method": "cod", "payment_status": "cod_pending", "created_at": datetime.now(timezone.utc)}).inserted_id
        ticket = db.restaurant_support.insert_one({"user_id": customer, "order_id": str(oid), "order_kind": "restaurant",
            "financial_review": {"replacement_id": "fixture", "original": {"delivery_fee": 15}, "reasons": []}}).inserted_id
        path = f"/earnings/orders/restaurant/{oid}/cash-collected"
        confirmation = {"confirmed": True, "note": "Synthetic COD collection"}
        assert api(path, headers, "POST", confirmation)["payment_status"] == "cash_collected"
        process.terminate()
        process.wait(timeout=15)
        process = start()
        admin = authenticate()
        assert api(path, headers, "POST", confirmation)["payment_status"] == "cash_collected"
        query = {"order_id": str(oid), "order_kind": "restaurant"}
        assert db.financial_audit.count_documents({**query, "action": "manual_cash_collection_confirmed"}) == 1
        assert db.financial_ledger.count_documents({**query, "event_type": "order_finalized"}) == 1
        print("PASS post-restart COD replay preserved one audit and one finalized ledger snapshot")
        details = api(f"/admin/restaurant/support/{ticket}/financial-review", admin)["reconciliation"]
        assert details["cod_evidence"] == {"collection_recorded": True, "delivery_recorded": True,
            "collection_audit_matched": True, "payout_status": "pending_authorized_cod_rail"}
        assert not db.restaurant_payments.find_one({"order_id": str(oid)})
        print("PASS persisted COD evidence remains review-only and no provider refund record was created")
    finally:
        if process is not None and process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
        mongo.drop_database(database)
        mongo.close()
