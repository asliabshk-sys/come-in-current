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


base = "http://127.0.0.1:8273/api"
database = "comein_disposable_t9_ref_restart_" + uuid4().hex[:16]
env = dict(os.environ, DB_NAME=database, MONGO_EXPECTED_DB_NAME=database)


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8273"],
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
        referrals, orders = [], []
        for _ in range(10):
            customer = str(ObjectId())
            order = str(db.orders.insert_one({"customer_id": customer, "status": "delivered",
                                              "payment_status": "paid", "total": 100}).inserted_id)
            referrals.append(str(db.referrals.insert_one({"referrer_id": owner, "referred_user_id": customer,
                "status": "qualified", "qualifying_order_id": order, "qualifying_order_kind": "grocery"}).inserted_id))
            orders.append({"order_id": order, "kind": "grocery"})
        reward = str(db.referral_rewards.insert_one({"reward_key": f"referral-target-10:{owner}", "referrer_id": owner,
            "amount": 500, "status": "pending_verification", "qualifying_referral_ids": referrals, "qualifying_orders": orders}).inserted_id)
        path = f"/admin/referral-rewards/{reward}"
        decision = {"decision": "approve"}
        assert api(path, admin, "PATCH", decision)["status"] == "approved"
        ledger = db.referral_ledger.find_one({"reward_id": reward})
        assert ledger["amount"] == 500 and ledger["status"] == "approved"
        process.terminate()
        process.wait(timeout=15)
        process = start()
        admin = authenticate()
        response = requests.patch(base + path, headers=admin, json=decision, timeout=10)
        assert response.status_code == 409
        assert db.referral_ledger.count_documents({"reward_id": reward}) == 1
        assert db.notifications.count_documents({"data.reward_id": reward}) == 1
        print("PASS approved credit and notification persisted and approval replay did not duplicate either")
        db.orders.update_one({"_id": ObjectId(orders[0]["order_id"])}, {"$set": {"refund_status": "refunded"}})
        for _ in range(2):
            conflict = requests.patch(base + path, headers=admin, json={"decision": "available"}, timeout=10)
            assert conflict.status_code == 422
        assert db.referral_ledger.find_one({"reward_id": reward}) == ledger
        assert db.referral_rewards.find_one({"_id": ObjectId(reward)})["status"] == "approved"
        print("PASS refunded qualifying order blocks release after restart without reversing the original credit")
    finally:
        if process is not None and process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
        mongo.drop_database(database)
        mongo.close()
