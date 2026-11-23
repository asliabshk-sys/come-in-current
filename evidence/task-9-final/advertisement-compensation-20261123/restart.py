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


base = "http://127.0.0.1:8271/api"
database = "comein_disposable_t9_ad_restart_" + uuid4().hex[:16]
env = dict(os.environ, DB_NAME=database, MONGO_EXPECTED_DB_NAME=database)


def start():
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8271"],
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
    now = datetime.now(timezone.utc)
    process = None
    try:
        process = start()
        admin = authenticate()
        # Synthetic accepted booking with one measured impression against a two-impression target.
        campaign = db.advertisements.insert_one({
            "status": "approved", "starts_at": now - timedelta(days=2), "ends_at": now - timedelta(days=1),
            "poster_sha256": "fixture-only", "owner_approval": {"poster_sha256": "fixture-only"},
            "commercial_terms": {"model": "fixed_duration", "accepted_at": now - timedelta(days=3),
                                 "delivery_target_impressions": 2, "version": 1, "rate_paise": 1000},
        }).inserted_id
        db.advertisement_events.insert_one({"advertisement_id": str(campaign), "user_id": str(ObjectId()),
            "event_type": "impression", "day": (now - timedelta(days=2)).date().isoformat(), "created_at": now - timedelta(days=2)})
        review_path = f"/admin/advertisements/{campaign}/delivery-review"
        review_request = {"reason": "Fixture final shortfall review"}
        snapshot = api(review_path, admin, "POST", review_request)
        assert snapshot["delivery"]["shortfall_impressions"] == 1
        assert not snapshot["financial_action_confirmed"]
        removal = {"decision": "remove", "reason": "Fixture post-delivery removal"}
        api(f"/admin/advertisements/{campaign}", admin, "PATCH", removal)
        process.terminate()
        process.wait(timeout=15)
        process = start()
        admin = authenticate()
        assert api(review_path, admin, "POST", review_request) == snapshot
        assert api(f"/admin/advertisements/{campaign}", admin, "PATCH", removal)["status"] == "removed"
        assert db.advertisement_audit.count_documents({"advertisement_id": str(campaign), "event": "admin_remove"}) == 1
        assert db.advertisement_audit.count_documents({"advertisement_id": str(campaign), "event": "delivery_review_recorded"}) == 1
        assert db.advertisements.find_one({"_id": campaign}).get("commercial_budget") is None
        print("PASS immutable shortfall review preserved and replayed after process restart")
        print("PASS terminal removal and audit persisted without any duplicate audit or budget mutation")
    finally:
        if process is not None and process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
        mongo.drop_database(database)
        mongo.close()
