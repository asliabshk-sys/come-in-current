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


base = "http://127.0.0.1:8281/api"
database = "comein_disposable_t9_invoice_restart_" + uuid4().hex[:16]
env = dict(os.environ, DB_NAME=database, MONGO_EXPECTED_DB_NAME=database)


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8281"],
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
        buyer = str(ObjectId())
        originals = {"total": 100, "tax": 5, "payment_status": "paid"}
        oid = db.restaurant_orders.insert_one({**originals, "customer_id": buyer,
            "invoice_id": "synthetic-original-reference", "tax_details": {"fixture": "historical"},
            "replacements": [{"id": "fixture", "state": "assist_required"}]}).inserted_id
        ticket = str(db.restaurant_support.insert_one({"user_id": buyer, "order_id": str(oid), "order_kind": "restaurant",
            "financial_review": {"replacement_id": "fixture", "original": originals,
                                 "admin_tax_status": "approved_pending_accounting_procedure"}}).inserted_id)
        snapshot = {"reference": "synthetic-original-reference", "tax_details": {"fixture": "historical"}, "financials": originals}
        db.financial_audit.insert_many([
            {"ticket_id": ticket, "replacement_id": "fixture", "action": "replacement_financial_review",
             "stage": stage, "decision": "approve", "actor_id": str(ObjectId()), "invoice_review_snapshot": snapshot}
            for stage in ("professional_tax", "admin_tax")
        ])
        path = f"/admin/restaurant/support/{ticket}/invoice-correction-draft"
        request = {"replacement_id": "fixture", "reason": "Synthetic correction readiness only"}
        draft = api(path, admin, "POST", request)
        assert draft["status"] == "pending_statutory_issuance"
        process.terminate()
        process.wait(timeout=15)
        process = start()
        assert api(path, authenticate(), "POST", request) == draft
        assert db.financial_audit.count_documents({"action": "replacement_invoice_correction_drafted", "ticket_id": ticket}) == 1
        assert db.restaurant_orders.find_one({"_id": oid})["invoice_id"] == "synthetic-original-reference"
        print("PASS internal draft and original invoice reference persisted across restart without duplicate or statutory issuance")
    finally:
        if process is not None and process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
        mongo.drop_database(database)
        mongo.close()
