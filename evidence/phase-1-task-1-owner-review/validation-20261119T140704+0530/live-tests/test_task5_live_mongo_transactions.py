"""Task 5 LIVE MongoDB transaction scenarios (T5-MONGO-01..07) + measured Repeat Order + measured import apply/rollback.

Runs against a RUNNING backend connected to a transaction-capable MongoDB (replica set). Creates synthetic
test_t5_* users/shops/products only and deletes them at module teardown; never run against production.
Run: cd backend && python -m pytest tests/test_task5_live_mongo_transactions.py -n 0 -q
Env: EXPO_PUBLIC_BACKEND_URL (or frontend/.env), MONGO_URL + DB_NAME (or backend/.env),
     COMEIN_TEST_ADMIN_EMAIL / COMEIN_TEST_ADMIN_PASSWORD (default: ADMIN_EMAIL / ADMIN_PASSWORD from backend/.env).
"""
import os
import re
import secrets
import threading
import time
from pathlib import Path

import pytest
import requests
from bson import ObjectId
from pymongo import MongoClient

ROOT = Path(__file__).resolve().parents[2]


def _env_file(path):
    out = {}
    if path.exists():
        for line in path.read_text().splitlines():
            m = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$", line)
            if m:
                out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


BENV, FENV = _env_file(ROOT / "backend" / ".env"), _env_file(ROOT / "frontend" / ".env")
BASE = (os.environ.get("EXPO_PUBLIC_BACKEND_URL") or FENV["EXPO_PUBLIC_BACKEND_URL"]).rstrip("/") + "/api"
MONGO_URL = os.environ.get("MONGO_URL") or BENV["MONGO_URL"]
DB_NAME = os.environ.get("DB_NAME") or BENV["DB_NAME"]
ADMIN_EMAIL = os.environ.get("COMEIN_TEST_ADMIN_EMAIL") or BENV["ADMIN_EMAIL"]
ADMIN_PASSWORD = os.environ.get("COMEIN_TEST_ADMIN_PASSWORD") or BENV["ADMIN_PASSWORD"]
RUN = secrets.token_hex(4)
T = 60


def hdr(token):
    return {"Authorization": f"Bearer {token}"}


def register(role):
    email = f"test_t5_{role}_{RUN}_{secrets.token_hex(2)}@comein-preview.com"
    r = requests.post(f"{BASE}/auth/register", json={"name": f"TEST T5 {role}", "email": email, "password": secrets.token_urlsafe(14)}, timeout=T)
    assert r.status_code == 200, r.text
    return r.json()["token"]


@pytest.fixture(scope="module")
def mdb():
    c = MongoClient(MONGO_URL, serverSelectionTimeoutMS=8000)
    assert c.admin.command("hello").get("setName"), "MongoDB is not a replica set; transactions unavailable"
    yield c[DB_NAME]
    c.close()


@pytest.fixture(scope="module")
def env(mdb):
    admin = requests.post(f"{BASE}/auth/login", json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD}, timeout=T)
    assert admin.status_code == 200, admin.text
    seller = register("seller")
    shop = requests.post(f"{BASE}/shops", headers=hdr(seller), timeout=T, json={
        "name": f"TEST T5 Shop {RUN}", "phone": "9000000000", "city": "Testpur", "delivery_available": True,
        "pickup_available": True, "payment_methods": ["cod", "cash_shop"], "shop_type": "online", "category_ids": ["fruits-veggies"]})
    assert shop.status_code == 200, shop.text
    shop_id = shop.json()["id"]
    ok = requests.patch(f"{BASE}/admin/shops/{shop_id}/status", json={"status": "approved"}, headers=hdr(admin.json()["token"]), timeout=T)
    assert ok.status_code == 200, ok.text
    yield {"seller": seller, "shop_id": shop_id, "admin": admin.json()["token"]}
    cleanup(mdb, RUN)


def cleanup(mdb, run_pattern):
    """Remove every synthetic record created by this suite (run_pattern: one RUN id or a regex such as '.*')."""
    shops = [str(s["_id"]) for s in mdb.shops.find({"name": {"$regex": f"^TEST T5 Shop {run_pattern}$"}}, {"_id": 1})]
    users = [str(u["_id"]) for u in mdb.users.find({"email": {"$regex": f"^test_t5_[a-z]+_{run_pattern}_"}}, {"_id": 1})]
    for coll in ("products", "orders", "grocery_quotes", "catalog_import_history", "catalog_price_audit", "notifications"):
        mdb[coll].delete_many({"shop_id": {"$in": shops}})
    mdb.notifications.delete_many({"user_id": {"$in": users}})
    mdb.shops.delete_many({"_id": {"$in": [ObjectId(s) for s in shops]}})
    mdb.users.delete_many({"_id": {"$in": [ObjectId(u) for u in users]}})


def measured(env, *, price=120.0, stock=5000, lo=250, step=250, hi=3000, name="Tomato"):
    body = {"name": f"TEST {name} {RUN}", "price": price, "stock": stock, "category_id": "fruits-veggies", "description": "TEST measured",
            "sell_by": "weight", "measure": {"min_qty": lo, "step": step, "max_qty": hi, "presets": [lo]}}
    r = requests.post(f"{BASE}/shops/{env['shop_id']}/products", json=body, headers=hdr(env["seller"]), timeout=T)
    assert r.status_code == 200, r.text
    return r.json()["id"]


def pack(env, *, price=55.0, stock=10, name="Rice 1kg"):
    body = {"name": f"TEST {name} {RUN}", "unit": "1 kg", "price": price, "stock": stock, "category_id": "atta-rice-dal", "description": "TEST pack"}
    r = requests.post(f"{BASE}/shops/{env['shop_id']}/products", json=body, headers=hdr(env["seller"]), timeout=T)
    assert r.status_code == 200, r.text
    return r.json()["id"]


def quote(token, items, fulfillment="delivery"):
    return requests.post(f"{BASE}/grocery/quotes", json={"items": items, "fulfillment": fulfillment}, headers=hdr(token), timeout=T)


def order(token, q, idem=None, name="TEST T5 Customer"):
    body = {"items": [{"product_id": i["product_id"], "qty": i["qty"]} for i in q["items"]], "delivery_address": "1 Test Street",
            "fulfillment": q["fulfillment"], "customer_name": name, "customer_phone": "9000000001", "payment_method": "cod",
            "quote_token": q["quote_token"], "idempotency_key": idem or secrets.token_hex(12)}
    return requests.post(f"{BASE}/orders", json=body, headers=hdr(token), timeout=T)


def stock(mdb, pid):
    return mdb.products.find_one({"_id": ObjectId(pid)})["stock"]


def test_t5_mongo_01_transaction_behavior(env, mdb):
    """Quote claim + stock decrement + order insert commit together; replay is idempotent."""
    pid = measured(env)
    cust = register("customer")
    q = quote(cust, [{"product_id": pid, "qty": 750}]).json()
    idem = secrets.token_hex(12)
    r1 = order(cust, q, idem)
    assert r1.status_code == 200, r1.text
    oid = r1.json()["id"]
    assert mdb.grocery_quotes.find_one({"_id": q["quote_token"]})["status"] == "consumed"
    assert mdb.orders.count_documents({"_id": ObjectId(oid)}) == 1
    assert stock(mdb, pid) == 4250
    r2 = order(cust, q, idem)
    assert r2.status_code == 200 and r2.json()["id"] == oid
    assert stock(mdb, pid) == 4250 and mdb.orders.count_documents({"grocery_idempotency_scope": {"$regex": f"{idem}$"}}) == 1
    r3 = order(cust, q)  # new key, consumed quote
    assert r3.status_code == 409 and stock(mdb, pid) == 4250


def test_t5_mongo_02_measured_stock_deduction(env, mdb):
    pid = measured(env, stock=3000)
    cust = register("customer")
    for qty, left in ((250, 2750), (1000, 1750), (1750, 0)):
        q = quote(cust, [{"product_id": pid, "qty": qty}]).json()
        r = order(cust, q)
        assert r.status_code == 200, r.text
        assert stock(mdb, pid) == left
        assert mdb.orders.find_one({"_id": ObjectId(r.json()["id"])})["items"][0]["qty"] == qty


def test_t5_mongo_03_insufficient_stock_rejection(env, mdb):
    pid = measured(env, stock=400)
    cust = register("customer")
    before_orders = mdb.orders.count_documents({"items.product_id": pid})
    r = quote(cust, [{"product_id": pid, "qty": 500}])
    assert r.status_code == 409 and r.json()["detail"]["code"] == "insufficient_stock" and r.json()["detail"]["available_stock"] == 400
    assert stock(mdb, pid) == 400 and mdb.orders.count_documents({"items.product_id": pid}) == before_orders


def test_t5_mongo_04_concurrent_order_protection(env, mdb):
    pid = measured(env, stock=500, lo=500, step=250, hi=1000)
    customers = [register("customer") for _ in range(4)]
    quotes = [quote(c, [{"product_id": pid, "qty": 500}]).json() for c in customers]
    results = [None] * len(customers)
    barrier = threading.Barrier(len(customers))

    def go(i):
        barrier.wait()
        results[i] = order(customers[i], quotes[i])

    threads = [threading.Thread(target=go, args=(i,)) for i in range(len(customers))]
    [t.start() for t in threads]
    [t.join() for t in threads]
    codes = sorted(r.status_code for r in results)
    assert codes.count(200) == 1, [(r.status_code, r.text[:160]) for r in results]
    assert all(c in (200, 409, 503) for c in codes)
    assert stock(mdb, pid) == 0
    assert mdb.orders.count_documents({"items.product_id": pid}) == 1


def test_t5_mongo_05_failed_order_creation_rolls_back(env, mdb):
    """Inject a server-side insert failure on `orders` after stock decrement + quote claim inside the transaction."""
    pid = measured(env, stock=2000)
    cust = register("customer")
    q = quote(cust, [{"product_id": pid, "qty": 1000}]).json()
    marker = f"TEST_ROLLBACK_INJECT_{RUN}"
    mdb.command({"collMod": "orders", "validator": {"customer_name": {"$ne": marker}}, "validationAction": "error", "validationLevel": "strict"})
    try:
        r = order(cust, q, name=marker)
    finally:
        mdb.command({"collMod": "orders", "validator": {}, "validationLevel": "off"})
    assert r.status_code == 503 and r.json()["detail"]["code"] == "grocery_checkout_unavailable", r.text
    assert stock(mdb, pid) == 2000, "stock decrement was not rolled back"
    assert mdb.grocery_quotes.find_one({"_id": q["quote_token"]})["status"] == "open", "quote claim was not rolled back"
    assert mdb.orders.count_documents({"customer_name": marker}) == 0
    r2 = order(cust, q)  # same quote works after rollback
    assert r2.status_code == 200 and stock(mdb, pid) == 1000


def test_t5_mongo_06_measured_precision_and_pricing(env, mdb):
    pid = measured(env, price=123.45, stock=5000, lo=250, step=50, hi=3000)
    cust = register("customer")
    mp = requests.post(f"{BASE}/grocery/measured-price", json={"product_id": pid, "qty": 1250}, timeout=T).json()
    assert mp["line_total"] == 154.31 and mp["quantity_label"] == "1.25 kg" and mp["unit"] == "kg"
    bad = requests.post(f"{BASE}/grocery/measured-price", json={"product_id": pid, "qty": 260}, timeout=T)
    assert bad.status_code == 422 and bad.json()["detail"]["code"] == "measured_quantity_invalid"
    q = quote(cust, [{"product_id": pid, "qty": 1250}]).json()
    assert q["subtotal"] == 154.31 and q["delivery_fee"] == 29.0 and q["total"] == 183.31
    r = order(cust, q)
    assert r.status_code == 200, r.text
    doc = mdb.orders.find_one({"_id": ObjectId(r.json()["id"])})
    line = doc["items"][0]
    assert (line["qty"], line["line_total"], line["price"], line["quantity_label"], line["sell_by"]) == (1250, 154.31, 123.45, "1.25 kg", "weight")
    assert (doc["subtotal"], doc["delivery_fee"], doc["total"]) == (154.31, 29.0, 183.31)
    assert stock(mdb, pid) == 3750


def test_t5_mongo_07_fixed_pack_compatibility(env, mdb):
    mid, kid = measured(env, price=80.0, stock=5000), pack(env, price=55.0, stock=10)
    cust = register("customer")
    q = quote(cust, [{"product_id": mid, "qty": 500}, {"product_id": kid, "qty": 3}]).json()
    lines = {i["product_id"]: i for i in q["items"]}
    assert lines[mid]["line_total"] == 40.0 and "line_total" not in lines[kid] and lines[kid]["unit"] == "1 kg"
    assert q["subtotal"] == 205.0 and q["delivery_fee"] == 0.0
    r = order(cust, q)
    assert r.status_code == 200, r.text
    assert stock(mdb, mid) == 4500 and stock(mdb, kid) == 7
    over = quote(cust, [{"product_id": kid, "qty": 8}])
    assert over.status_code == 409 and over.json()["detail"]["code"] == "insufficient_stock"


def test_t5_repeat_measured_order_e2e(env, mdb):
    """Repeat a past measured order: fresh price, stock revalidated, quantity preserved, DB consistent."""
    pid = measured(env, price=100.0, stock=3000)
    cust = register("customer")
    first = order(cust, quote(cust, [{"product_id": pid, "qty": 1500}]).json())
    assert first.status_code == 200
    body = {"name": f"TEST Tomato {RUN}", "price": 110.0, "stock": 1500, "category_id": "fruits-veggies", "description": "TEST measured",
            "sell_by": "weight", "measure": {"min_qty": 250, "step": 250, "max_qty": 3000, "presets": [250]}}
    assert requests.patch(f"{BASE}/products/{pid}", json=body, headers=hdr(env["seller"]), timeout=T).status_code == 200
    mine = requests.get(f"{BASE}/orders/mine", headers=hdr(cust), timeout=T).json()
    past = next(o for o in mine if o["id"] == first.json()["id"])
    q = quote(cust, [{"product_id": i["product_id"], "qty": i["qty"]} for i in past["items"]]).json()
    assert q["items"][0]["qty"] == 1500 and q["items"][0]["price"] == 110.0 and q["subtotal"] == 165.0
    again = order(cust, q)
    assert again.status_code == 200, again.text
    assert stock(mdb, pid) == 0
    third = quote(cust, [{"product_id": i["product_id"], "qty": i["qty"]} for i in past["items"]])
    assert third.status_code == 409 and third.json()["detail"]["code"] == "insufficient_stock"


HEAD = "action,sku,product_id,name,brand,unit,price,mrp,stock,category_id,description,available,image_url,sell_by,dimension,base_unit,price_basis,min_qty,step,max_qty,presets\n"


def _csv_row(sku, name, price="40", stock="20000"):
    return f"create,{sku},,{name},,kg,{price},,{stock},fruits-veggies,TEST import,true,,measured,weight,g,per_kg,250,250,5000,250;500\n"


def _import(env, csv_text, apply):
    return requests.post(f"{BASE}/shops/{env['shop_id']}/products/import", headers=hdr(env["seller"]), timeout=T,
                         files={"file": ("t5.csv", csv_text.encode(), "text/csv")}, data={"apply": "true" if apply else "false"})


def test_t5_measured_import_apply_invalid_duplicate_and_rollback(env, mdb):
    a, b = f"T5-IMP-A-{RUN}", f"T5-IMP-B-{RUN}"
    ok = _import(env, HEAD + _csv_row(a, f"TEST Onion {RUN}"), apply=True).json()
    assert ok["applied"] is True and ok["created"] == 1
    p = mdb.products.find_one({"shop_id": env["shop_id"], "sku": a})
    assert p["sell_by"] == "weight" and p["unit"] == "kg" and p["stock"] == 20000 and p["measure"]["min_qty"] == 250
    invalid = _import(env, HEAD + _csv_row(b, f"TEST Garlic {RUN}") + _csv_row(f"{b}-X", f"TEST Bad {RUN}", price="-5"), apply=True).json()
    assert invalid["applied"] is False and invalid["errors"] and mdb.products.count_documents({"sku": {"$in": [b, f"{b}-X"]}}) == 0
    dup = _import(env, HEAD + _csv_row(b, f"TEST Garlic {RUN}") + _csv_row(b, f"TEST Garlic {RUN}"), apply=True).json()
    assert dup["applied"] is False and mdb.products.count_documents({"sku": b}) == 0
    marker = f"TEST_IMPORT_FAIL_{RUN}"
    mdb.command({"collMod": "products", "validator": {"name": {"$ne": marker}}, "validationAction": "error", "validationLevel": "strict"})
    try:
        r = _import(env, HEAD + _csv_row(b, f"TEST Garlic {RUN}") + _csv_row(f"{b}-2", marker), apply=True)
    finally:
        mdb.command({"collMod": "products", "validator": {}, "validationLevel": "off"})
    assert r.status_code == 503 and r.json()["detail"]["code"] == "catalog_import_unavailable", r.text
    assert mdb.products.count_documents({"sku": {"$in": [b, f"{b}-2"]}}) == 0, "partial import was committed"
    assert mdb.catalog_import_history.count_documents({"shop_id": env["shop_id"]}) == 1
    time.sleep(0.1)
