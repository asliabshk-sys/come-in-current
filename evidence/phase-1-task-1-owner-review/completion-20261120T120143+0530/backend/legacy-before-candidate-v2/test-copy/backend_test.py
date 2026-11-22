"""Come In backend regression tests (pytest)."""
import io
import os
import uuid
import pytest
import requests

# These are destructive-ish integration tests: they create accounts and shops.
# They only run against an explicitly configured disposable test deployment.
BASE_URL = os.environ.get("COMEIN_TEST_BASE_URL", "").rstrip("/")
API = f"{BASE_URL}/api" if BASE_URL else ""
ADMIN_EMAIL = os.environ.get("COMEIN_TEST_ADMIN_EMAIL", "")
ADMIN_PASSWORD = os.environ.get("COMEIN_TEST_ADMIN_PASSWORD", "")
pytestmark = pytest.mark.skipif(
    not BASE_URL,
    reason="Set COMEIN_TEST_BASE_URL to an isolated disposable test deployment to run remote integration tests",
)


# ---------- Fixtures ----------
@pytest.fixture(scope="session")
def s():
    return requests.Session()


@pytest.fixture(scope="session")
def customer(s):
    """Create a fresh customer; return (token, user)."""
    email = f"TEST_cust_{uuid.uuid4().hex[:8]}@test.com"
    r = s.post(f"{API}/auth/register", json={
        "name": "Test Customer", "email": email, "password": "test1234", "phone": "9999900000"
    })
    assert r.status_code == 200, r.text
    data = r.json()
    return {"token": data["token"], "user": data["user"], "email": email, "password": "test1234"}


@pytest.fixture(scope="session")
def admin(s):
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        pytest.skip("Set COMEIN_TEST_ADMIN_EMAIL and COMEIN_TEST_ADMIN_PASSWORD for admin integration tests")
    r = s.post(f"{API}/auth/login", json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD})
    assert r.status_code == 200, f"Admin login failed: {r.text}"
    data = r.json()
    assert data["user"]["role"] == "admin"
    return {"token": data["token"], "user": data["user"]}


def h(tok):
    return {"Authorization": f"Bearer {tok}"}


# ---------- Health ----------
def test_health(s):
    r = s.get(f"{API}/")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


# ---------- Auth ----------
def test_register_login_me(s):
    email = f"TEST_u_{uuid.uuid4().hex[:8]}@test.com".lower()
    r = s.post(f"{API}/auth/register", json={"name": "U", "email": email, "password": "pw12345"})
    assert r.status_code == 200
    tok = r.json()["token"]
    assert r.json()["user"]["role"] == "customer"

    # login
    r2 = s.post(f"{API}/auth/login", json={"email": email, "password": "pw12345"})
    assert r2.status_code == 200
    # me
    me = s.get(f"{API}/auth/me", headers=h(tok))
    assert me.status_code == 200
    assert me.json()["email"] == email
    # bad login
    bad = s.post(f"{API}/auth/login", json={"email": email, "password": "wrong"})
    assert bad.status_code == 401
    # duplicate registration
    dup = s.post(f"{API}/auth/register", json={"name": "U", "email": email, "password": "pw12345"})
    assert dup.status_code == 409


def test_me_unauth(s):
    r = s.get(f"{API}/auth/me")
    assert r.status_code == 401


# ---------- Shop lifecycle ----------
@pytest.fixture(scope="session")
def shop_owner(s):
    email = f"TEST_shop_{uuid.uuid4().hex[:8]}@test.com"
    r = s.post(f"{API}/auth/register", json={"name": "Owner", "email": email, "password": "pw12345"})
    assert r.status_code == 200
    return {"token": r.json()["token"], "user": r.json()["user"]}


@pytest.fixture(scope="session")
def created_shop(s, shop_owner):
    body = {
        "name": f"TEST Shop {uuid.uuid4().hex[:4]}",
        "phone": "9876543210",
        "address": "123 Test Street",
        "area": "Testville",
        "city": "Testopolis",
        "shop_type": "offline",
        # Existing canonical catalogue category (frontend/src/data/catalog.ts).
        "category_ids": ["atta-rice-dal"],
        "delivery_available": True,
    }
    r = s.post(f"{API}/shops", json=body, headers=h(shop_owner["token"]))
    assert r.status_code == 200, r.text
    data = r.json()
    assert data["status"] == "pending"
    assert data["online"] is False
    # Owner role promotion
    me = s.get(f"{API}/auth/me", headers=h(shop_owner["token"]))
    assert me.json()["role"] == "shopkeeper"
    return data


def test_shop_mine(s, shop_owner, created_shop):
    r = s.get(f"{API}/shops/mine", headers=h(shop_owner["token"]))
    assert r.status_code == 200
    assert r.json()["id"] == created_shop["id"]


def test_duplicate_shop_rejected(s, shop_owner, created_shop):
    r = s.post(f"{API}/shops", json={
        "name": "Second", "phone": "9876543210", "address": "x"
    }, headers=h(shop_owner["token"]))
    assert r.status_code == 400


def test_availability_blocked_until_approved(s, shop_owner, created_shop):
    r = s.patch(
        f"{API}/shops/{created_shop['id']}/availability",
        json={"online": True}, headers=h(shop_owner["token"]),
    )
    assert r.status_code == 400


def test_public_list_hides_pending(s, created_shop):
    r = s.get(f"{API}/shops")
    assert r.status_code == 200
    ids = [sh["id"] for sh in r.json()]
    assert created_shop["id"] not in ids, "Pending shop leaked into public list!"


def test_public_shop_detail_hidden_until_approved(s, created_shop):
    r = s.get(f"{API}/shops/{created_shop['id']}")
    assert r.status_code == 404


# ---------- Admin approval ----------
def test_admin_approves_shop(s, admin, created_shop):
    # Admin list sees it
    lst = s.get(f"{API}/admin/shops", headers=h(admin["token"]))
    assert lst.status_code == 200
    ids = [sh["id"] for sh in lst.json()]
    assert created_shop["id"] in ids

    r = s.patch(
        f"{API}/admin/shops/{created_shop['id']}/status",
        json={"status": "approved"}, headers=h(admin["token"]),
    )
    assert r.status_code == 200
    assert r.json()["status"] == "approved"

    # Public now visible
    pub = s.get(f"{API}/shops/{created_shop['id']}")
    assert pub.status_code == 200


def test_non_admin_cannot_approve(s, shop_owner, created_shop):
    r = s.patch(
        f"{API}/admin/shops/{created_shop['id']}/status",
        json={"status": "approved"}, headers=h(shop_owner["token"]),
    )
    assert r.status_code == 403


def test_availability_after_approval(s, shop_owner, created_shop):
    r = s.patch(
        f"{API}/shops/{created_shop['id']}/availability",
        json={"online": True}, headers=h(shop_owner["token"]),
    )
    assert r.status_code == 200
    assert r.json()["online"] is True

    # Online filter
    online = s.get(f"{API}/shops?online=true").json()
    assert created_shop["id"] in [x["id"] for x in online]


# ---------- Products ----------
@pytest.fixture(scope="session")
def created_product(s, shop_owner, created_shop):
    assert created_shop["category_ids"] == ["atta-rice-dal"]
    body = {"name": "TEST Product", "price": 50.0, "stock": 10,
            "category_id": created_shop["category_ids"][0],
            "description": "Synthetic regression product"}
    r = s.post(f"{API}/shops/{created_shop['id']}/products", json=body, headers=h(shop_owner["token"]))
    assert r.status_code == 200, r.text
    return r.json()


def test_product_crud(s, shop_owner, created_shop, created_product):
    # List
    lst = s.get(f"{API}/shops/{created_shop['id']}/products")
    assert lst.status_code == 200
    assert any(p["id"] == created_product["id"] for p in lst.json())
    # Update
    upd = s.patch(f"{API}/products/{created_product['id']}", json={
        "name": "TEST Product Edited", "price": 55.0, "stock": 8,
        "category_id": created_product["category_id"],
        "description": created_product["description"],
    }, headers=h(shop_owner["token"]))
    assert upd.status_code == 200
    assert upd.json()["name"] == "TEST Product Edited"
    assert upd.json()["price"] == 55.0
    # This module intentionally exercises a shared shop lifecycle. Keep the
    # fixture's independently asserted price/stock state current for checkout.
    created_product.update(upd.json())


def test_product_validation(s, shop_owner, created_shop):
    # Empty name
    r = s.post(f"{API}/shops/{created_shop['id']}/products",
               json={"name": "", "price": 10}, headers=h(shop_owner["token"]))
    assert r.status_code == 422
    # Negative price
    r2 = s.post(f"{API}/shops/{created_shop['id']}/products",
                json={"name": "X", "price": -5}, headers=h(shop_owner["token"]))
    assert r2.status_code == 422


def test_product_delete(s, shop_owner, created_shop):
    r = s.post(f"{API}/shops/{created_shop['id']}/products",
               json={"name": "TEST Del", "price": 1, "stock": 1,
                     "category_id": created_shop["category_ids"][0],
                     "description": "Synthetic product for deletion"}, headers=h(shop_owner["token"]))
    assert r.status_code == 200, r.text
    pid = r.json()["id"]
    d = s.delete(f"{API}/products/{pid}", headers=h(shop_owner["token"]))
    assert d.status_code == 200


# ---------- Orders ----------
def checkout_quote(s, product, qty, headers):
    """Exercise the existing authoritative quote flow,not invented test tokens."""
    response = s.post(f"{API}/grocery/quotes", json={
        "items": [{"product_id": product["id"], "qty": qty}],
        "fulfillment": "delivery",
    }, headers=headers)
    assert response.status_code == 200, response.text
    quote = response.json()
    assert len(quote["items"]) == 1
    assert quote["items"][0]["product_id"] == product["id"]
    assert quote["items"][0]["price"] == product["price"]
    # Existing Grocery policy: delivery costs29 below a199 subtotal. Check
    # independently from the quote instead of merely echoing its total.
    subtotal = round(product["price"] * qty, 2)
    delivery_fee = 0.0 if subtotal >= 199.0 else 29.0
    assert quote["subtotal"] == subtotal
    assert quote["delivery_fee"] == delivery_fee
    assert quote["total"] == round(subtotal + delivery_fee, 2)
    assert quote["currency"] == "INR"
    return quote, subtotal, delivery_fee


def test_order_create_guest(s, created_product, created_shop):
    headers = {"x-comein-guest-session": uuid.uuid4().hex}
    quote, subtotal, delivery_fee = checkout_quote(s, created_product, 2, headers)
    body = {
        "items": [{"product_id": created_product["id"], "name": "x", "price": 55, "qty": 2, "shop_id": created_shop["id"]}],
        "delivery_address": "Addr 1",
        "customer_name": "Guest",
        "customer_phone": "9999",
        "payment_method": "cod",
        "shop_id": created_shop["id"],
        "quote_token": quote["quote_token"],
        "idempotency_key": uuid.uuid4().hex,
    }
    r = s.post(f"{API}/orders", json=body, headers=headers)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data["ref"].startswith("CI-")
    assert data["subtotal"] == subtotal
    assert data["delivery_fee"] == delivery_fee
    assert data["total"] == round(subtotal + delivery_fee, 2)
    assert data["payment_status"] == "cod_pending"


def test_order_customer_and_seller_views(s, customer, shop_owner, created_shop, created_product):
    quote, subtotal, delivery_fee = checkout_quote(s, created_product, 1, h(customer["token"]))
    body = {
        "items": [{"product_id": created_product["id"], "name": "x", "price": 55, "qty": 1, "shop_id": created_shop["id"]}],
        "delivery_address": "Addr 1",
        "customer_name": "C",
        "customer_phone": "9999",
        "payment_method": "cod",
        "shop_id": created_shop["id"],
        "quote_token": quote["quote_token"],
        "idempotency_key": uuid.uuid4().hex,
    }
    r = s.post(f"{API}/orders", json=body, headers=h(customer["token"]))
    assert r.status_code == 200
    assert r.json()["subtotal"] == subtotal
    assert r.json()["delivery_fee"] == delivery_fee
    assert r.json()["total"] == round(subtotal + delivery_fee, 2)
    oid = r.json()["id"]

    # Customer view
    mine = s.get(f"{API}/orders/mine", headers=h(customer["token"]))
    assert mine.status_code == 200
    assert any(o["id"] == oid for o in mine.json())

    # Seller view
    so = s.get(f"{API}/shops/{created_shop['id']}/orders", headers=h(shop_owner["token"]))
    assert so.status_code == 200
    assert any(o["id"] == oid for o in so.json())

    # Seller advance status
    adv = s.patch(f"{API}/orders/{oid}/status", json={"status": "accepted", "note": "ok"},
                  headers=h(shop_owner["token"]))
    assert adv.status_code == 200
    assert adv.json()["status"] == "accepted"


def test_order_empty_items_rejected(s):
    r = s.post(f"{API}/orders", json={"items": [], "delivery_address": "x"})
    assert r.status_code == 422


# ---------- Requests ----------
def test_request_anything(s, admin):
    body = {"description": "Need something", "drop": "Main road", "pickup": "Shop", "customer_phone": "9"}
    r = s.post(f"{API}/requests/anything", json=body)
    assert r.status_code == 200
    assert r.json()["ref"].startswith("RQ-")
    # Admin can see
    lst = s.get(f"{API}/admin/requests/anything", headers=h(admin["token"]))
    assert lst.status_code == 200
    assert any(x["ref"] == r.json()["ref"] for x in lst.json())


def test_agent_assist(s, admin, created_shop):
    body = {"reason": "Help me buy", "shop_id": created_shop["id"], "customer_phone": "9"}
    r = s.post(f"{API}/requests/assist", json=body)
    assert r.status_code == 200
    assert r.json()["ref"].startswith("AG-")
    lst = s.get(f"{API}/admin/requests/assist", headers=h(admin["token"]))
    assert lst.status_code == 200
    assert any(x["ref"] == r.json()["ref"] for x in lst.json())


# ---------- Admin orders ----------
def test_admin_orders(s, admin):
    r = s.get(f"{API}/admin/orders", headers=h(admin["token"]))
    assert r.status_code == 200
    assert isinstance(r.json(), list)


# ---------- Role guards ----------
def test_admin_endpoints_require_admin(s, customer):
    for ep in ["/admin/shops", "/admin/orders", "/admin/requests/anything", "/admin/requests/assist", "/status"]:
        r = s.get(f"{API}{ep}", headers=h(customer["token"]))
        assert r.status_code == 403, f"{ep} expected 403 got {r.status_code}"


def test_status_diagnostics_require_admin(s, admin, customer, shop_owner):
    for headers, expected in [({}, 401), (h(customer["token"]), 403), (h(shop_owner["token"]), 403)]:
        assert s.get(f"{API}/status", headers=headers).status_code == expected
        denied = s.post(f"{API}/status", json={"client_name": "synthetic-regression"}, headers=headers)
        assert denied.status_code == expected
    name = f"synthetic-regression-{uuid.uuid4().hex}"
    created = s.post(f"{API}/status", json={"client_name": name}, headers=h(admin["token"]))
    assert created.status_code == 200, created.text
    assert created.json()["client_name"] == name
    listed = s.get(f"{API}/status", headers=h(admin["token"]))
    assert listed.status_code == 200
    assert any(row["client_name"] == name for row in listed.json())
    oversized = s.post(f"{API}/status", json={"client_name": "x" * 257}, headers=h(admin["token"]))
    assert oversized.status_code == 422


# ---------- Image upload ----------
def test_image_upload(s, customer):
    # 1x1 PNG
    png = (
        b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
        b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0\x00\x00\x00\x03\x00\x01\x5c\xcd\xff\x69\x00\x00\x00\x00IEND\xaeB`\x82"
    )
    files = {"file": ("t.png", io.BytesIO(png), "image/png")}
    r = s.post(f"{API}/uploads/image", files=files, headers=h(customer["token"]))
    if r.status_code == 503:
        pytest.skip("Object storage unavailable")
    assert r.status_code == 200, r.text
    url = r.json()["url"]
    assert url.startswith("/api/uploads/")
    # Fetch back
    full = f"{BASE_URL}{url}"
    g = s.get(full)
    assert g.status_code == 200
    assert g.headers.get("content-type", "").startswith("image/")


def test_image_upload_unauth(s):
    files = {"file": ("t.png", io.BytesIO(b"x"), "image/png")}
    r = s.post(f"{API}/uploads/image", files=files)
    assert r.status_code == 401
