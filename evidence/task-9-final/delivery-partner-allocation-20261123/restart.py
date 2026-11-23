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


base = "http://127.0.0.1:8272/api"
database = "comein_disposable_t9_dp_restart_" + uuid4().hex[:16]
env = dict(os.environ, DB_NAME=database, MONGO_EXPECTED_DB_NAME=database)


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8272"],
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
        owner = str(ObjectId())
        order_id = str(db.orders.insert_one({
            "customer_id": owner, "fulfillment": "delivery", "delivery_fee": 29,
            "status": "delivered", "payment_method": "cod", "payment_status": "cash_collected",
        }).inserted_id)
        ticket = db.restaurant_support.insert_one({
            "user_id": owner, "order_id": order_id, "order_kind": "grocery",
            "financial_review": {"replacement_id": "fixture", "original": {"delivery_fee": 29}, "reasons": []},
        }).inserted_id
        db.financial_ledger.insert_one({"order_id": order_id, "order_kind": "grocery", "event_type": "order_finalized",
                                       "source_delivery_fee_inr": 29, "recorded_at": datetime.now(timezone.utc)})
        path = f"/admin/restaurant/support/{ticket}/financial-review"
        evidence = api(path, admin)["reconciliation"]["delivery_fee_evidence"]
        assert evidence["ledger_fee_matches"] is True and evidence["partner_payable_inr"] is None
        process.terminate()
        process.wait(timeout=15)
        process = start()
        admin = authenticate()
        assert api(path, admin)["reconciliation"]["delivery_fee_evidence"] == evidence
        print("PASS original order and finalized fee evidence reconciled unchanged after restart")
        db.orders.update_one({"_id": ObjectId(order_id)}, {"$set": {"delivery_fee": "invalid legacy value"}})
        changed = api(path, admin)["reconciliation"]["delivery_fee_evidence"]
        assert changed["ledger_fee_matches"] is False and changed["partner_payable_inr"] is None
        assert db.financial_ledger.find_one({"order_id": order_id})["source_delivery_fee_inr"] == 29
        print("PASS malformed order fee was flagged without mutating the finalized ledger or creating a payable")
    finally:
        if process is not None and process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
        mongo.drop_database(database)
        mongo.close()
