# Runtime E2E verification of Come-In preview (isolated local test DB).
# Creates TEST_ seller shop + products and TEST_ restaurant + menu, places COD orders.
import os
import uuid
import pytest
import requests


def _base():
    url = os.environ.get("EXPO_PUBLIC_BACKEND_URL") or os.environ.get("REACT_APP_BACKEND_URL")
    if not url:
        for line in open("/app/frontend/.env"):
            if line.startswith("EXPO_PUBLIC_BACKEND_URL="):
                url = line.split("=", 1)[1].strip()
    return url.rstrip("/")


BASE = _base() + "/api"
ADMIN = (os.environ.get("COMEIN_TEST_ADMIN_EMAIL", ""), os.environ.get("COMEIN_TEST_ADMIN_PASSWORD", ""))
CUSTOMER = (os.environ.get("COMEIN_TEST_CUSTOMER_EMAIL", ""), os.environ.get("COMEIN_TEST_CUSTOMER_PASSWORD", ""))
SELLER = (os.environ.get("COMEIN_TEST_SELLER_EMAIL", ""), os.environ.get("COMEIN_TEST_SELLER_PASSWORD", ""))
RESTO = (os.environ.get("COMEIN_TEST_RESTO_EMAIL", ""), os.environ.get("COMEIN_TEST_RESTO_PASSWORD", ""))
S = {}


def login(email, pw):
    r = requests.post(f"{BASE}/auth/login", json={"email": email, "password": pw}, timeout=30)
    return r


def ensure_user(email, pw, name):
    r = login(email, pw)
    if r.status_code == 200:
        return r.json()["token"]
    r = requests.post(f"{BASE}/auth/register", json={"name": name, "email": email, "password": pw}, timeout=30)
    assert r.status_code == 200, r.text
    return r.json()["token"]


def H(tok):
    return {"Authorization": f"Bearer {tok}"}


# --- Health / auth
class TestAuth:
    def test_root(self):
        r = requests.get(f"{BASE}/", timeout=30)
        assert r.status_code == 200

    def test_admin_login(self):
        r = login(*ADMIN)
        assert r.status_code == 200, r.text
        assert r.json()["user"]["role"] == "admin"
        S["admin"] = r.json()["token"]

    def test_customer_login(self):
        r = login(*CUSTOMER)
        assert r.status_code == 200, r.text
        assert r.json()["user"]["role"] == "customer"
        S["cust"] = r.json()["token"]

    def test_bad_login(self):
        assert login(ADMIN[0], "wrong").status_code == 401

    def test_register_new_and_me(self):
        email = f"test_{uuid.uuid4().hex[:8]}@example.com"
        r = requests.post(f"{BASE}/auth/register", json={"name": "TEST User", "email": email, "password": "Passw0rd!"}, timeout=30)
        assert r.status_code == 200, r.text
        me = requests.get(f"{BASE}/auth/me", headers=H(r.json()["token"]), timeout=30)
        assert me.status_code == 200 and me.json()["email"] == email

    def test_register_dup(self):
        r = requests.post(f"{BASE}/auth/register", json={"name": "x", "email": CUSTOMER[0], "password": "Passw0rd!"}, timeout=30)
        assert r.status_code == 409


# --- Seller shop + products
class TestSeller:
    def test_create_shop_and_approve(self):
        tok = ensure_user(*SELLER, "TEST Seller")
        r = requests.get(f"{BASE}/shops/mine", headers=H(tok), timeout=30)
        if r.status_code == 200 and r.json():
            shop = r.json()
        else:
            r = requests.post(f"{BASE}/shops", headers=H(tok), json={
                "name": "TEST Kirana Store", "phone": "9876543210", "area": "Sector 1", "city": "Delhi",
                "address": "1 Test Road", "pincode": "110001", "delivery_available": True, "pickup_available": True,
                "payment_methods": ["cod", "pickup", "cash_shop"], "shop_type": "both", "category_ids": ["grocery"],
                "description": "Test shop"}, timeout=30)
            assert r.status_code == 200, r.text
            shop = r.json()
        S["shop_id"] = shop["id"]
        S["seller"] = login(*SELLER).json()["token"]  # refresh token for shopkeeper role
        r = requests.patch(f"{BASE}/admin/shops/{shop['id']}/status", headers=H(S["admin"]), json={"status": "approved"}, timeout=30)
        assert r.status_code == 200 and r.json()["status"] == "approved", r.text
        r = requests.patch(f"{BASE}/shops/{shop['id']}/availability", headers=H(S["seller"]), json={"online": True}, timeout=30)
        assert r.status_code == 200 and r.json()["online"] is True, r.text

    def test_add_products(self):
        r = requests.get(f"{BASE}/shops/{S['shop_id']}/products", timeout=30)
        assert r.status_code == 200, r.text
        prods = r.json()
        if len(prods) < 2:
            for p in [
                {"name": "TEST Basmati Rice", "unit": "1 kg", "price": 120, "mrp": 140, "stock": 50, "category_id": "grocery", "description": "Test rice",
                 "variants": [{"id": "1kg", "unit": "1 kg", "price": 120, "mrp": 140, "stock": 50}, {"id": "5kg", "unit": "5 kg", "price": 550, "mrp": 650, "stock": 20}]},
                {"name": "TEST Toor Dal", "unit": "500 g", "price": 80, "mrp": 90, "stock": 40, "category_id": "grocery", "description": "Test dal"},
            ]:
                r = requests.post(f"{BASE}/shops/{S['shop_id']}/products", headers=H(S["seller"]), json=p, timeout=30)
                assert r.status_code == 200, r.text
            prods = requests.get(f"{BASE}/shops/{S['shop_id']}/products", timeout=30).json()
        assert len(prods) >= 2
        S["prod"] = next(p for p in prods if "Dal" in p["name"])

    def test_public_listing(self):
        r = requests.get(f"{BASE}/shops", timeout=30)
        assert r.status_code == 200 and any(s["id"] == S["shop_id"] for s in r.json()), r.text[:300]
        r = requests.get(f"{BASE}/catalog/products", params={"q": "Dal"}, timeout=30)
        assert r.status_code == 200, r.text
        print("catalog search count", len(r.json()) if isinstance(r.json(), list) else r.json())


# --- Grocery COD order
class TestGroceryOrder:
    def test_quote_and_cod_order(self):
        items = [{"product_id": S["prod"]["id"], "qty": 2}]
        q = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": items, "fulfillment": "delivery"}, timeout=30)
        assert q.status_code == 200, q.text
        qt = q.json()
        assert qt["subtotal"] == 160
        r = requests.post(f"{BASE}/orders", headers=H(S["cust"]), json={
            "items": items, "delivery_address": "12 Test Lane, Delhi 110001", "fulfillment": "delivery",
            "customer_name": "Preview Customer", "customer_phone": "9999999999", "payment_method": "cod",
            "quote_token": qt["quote_token"], "idempotency_key": uuid.uuid4().hex}, timeout=30)
        assert r.status_code == 200, r.text
        o = r.json()
        assert o["payment_status"] == "cod_pending" and o["status"] == "pending"
        S["order_id"] = o["id"]

    def test_orders_mine_and_seller_orders(self):
        r = requests.get(f"{BASE}/orders/mine", headers=H(S["cust"]), timeout=30)
        assert r.status_code == 200 and any(o["id"] == S["order_id"] for o in r.json())
        r = requests.get(f"{BASE}/shops/{S['shop_id']}/orders", headers=H(S["seller"]), timeout=30)
        assert r.status_code == 200 and any(o["id"] == S["order_id"] for o in r.json())

    def test_status_update_and_tracking(self):
        r = requests.patch(f"{BASE}/orders/{S['order_id']}/status", headers=H(S["seller"]), json={"status": "accepted"}, timeout=30)
        assert r.status_code == 200, r.text
        r = requests.get(f"{BASE}/orders/{S['order_id']}/tracking", headers=H(S["cust"]), timeout=30)
        assert r.status_code == 200, r.text
        print("tracking", r.json())

    def test_customer_cannot_update_status(self):
        r = requests.patch(f"{BASE}/orders/{S['order_id']}/status", headers=H(S["cust"]), json={"status": "delivered"}, timeout=30)
        assert r.status_code in (401, 403)


# --- Restaurant mode
class TestRestaurant:
    def test_create_approve_menu(self):
        tok = ensure_user(*RESTO, "TEST Resto Owner")
        mine = requests.get(f"{BASE}/restaurants/mine", headers=H(tok), timeout=30).json()
        if mine:
            rest = mine[0]
        else:
            r = requests.post(f"{BASE}/restaurants", headers=H(tok), json={
                "name": "TEST Spice Kitchen", "cuisines": ["North Indian"], "phone": "9876500000", "address": "5 Food Street",
                "city": "Delhi", "delivery_serviceable_pincodes": ["110001"], "payment_methods": ["cod", "pickup"], "delivery_fee": 30}, timeout=30)
            assert r.status_code == 200, r.text
            rest = r.json()
        S["rest_id"] = rest["id"]
        S["resto"] = login(*RESTO).json()["token"]
        r = requests.patch(f"{BASE}/admin/restaurants/{rest['id']}/status", headers=H(S["admin"]), json={"status": "approved", "available": True}, timeout=30)
        assert r.status_code == 200 and r.json()["available"] is True, r.text
        menu = requests.get(f"{BASE}/restaurants/{rest['id']}/menu", timeout=30).json()
        if not menu:
            r = requests.post(f"{BASE}/restaurants/{rest['id']}/menu", headers=H(S["resto"]), json={
                "name": "TEST Paneer Butter Masala", "price": 220, "category": "Main", "vegetarian": True, "description": "Test"}, timeout=30)
            assert r.status_code == 200, r.text
            menu = requests.get(f"{BASE}/restaurants/{rest['id']}/menu", timeout=30).json()
        items = menu if isinstance(menu, list) else menu.get("items", [])
        assert items, menu
        S["menu_id"] = items[0]["id"]

    def test_public_restaurant_list(self):
        r = requests.get(f"{BASE}/restaurants", timeout=30)
        assert r.status_code == 200 and any(x["id"] == S["rest_id"] for x in r.json())

    def test_restaurant_pickup_order(self):
        r = requests.post(f"{BASE}/restaurant/orders", headers=H(S["cust"]), json={
            "restaurant_id": S["rest_id"], "items": [{"menu_item_id": S["menu_id"], "quantity": 1}], "contact_name": "Preview Customer",
            "contact_phone": "9999999999", "fulfillment": "pickup", "payment_method": "pickup", "idempotency_key": uuid.uuid4().hex}, timeout=30)
        assert r.status_code == 200, r.text
        S["rorder"] = r.json()["id"]
        print("restaurant order", {k: r.json().get(k) for k in ("status", "payment_status", "total")})

    def test_restaurant_cod_delivery_order(self):
        r = requests.post(f"{BASE}/restaurant/orders", headers=H(S["cust"]), json={
            "restaurant_id": S["rest_id"], "items": [{"menu_item_id": S["menu_id"], "quantity": 2}], "contact_name": "Preview Customer",
            "contact_phone": "9999999999", "fulfillment": "delivery", "payment_method": "cod",
            "delivery_address": "12 Test Lane, Delhi 110001", "idempotency_key": uuid.uuid4().hex}, timeout=30)
        print("cod delivery", r.status_code, r.text[:300])
        assert r.status_code == 200, r.text

    def test_restaurant_orders_mine(self):
        r = requests.get(f"{BASE}/restaurant/orders/mine", headers=H(S["cust"]), timeout=30)
        assert r.status_code == 200 and any(o["id"] == S["rorder"] for o in r.json())

    def test_razorpay_config_blocked(self):
        r = requests.get(f"{BASE}/restaurant/payments/config", timeout=30)
        print("razorpay config", r.status_code, r.text[:200])
        assert r.status_code == 200


# --- Admin
class TestAdmin:
    @pytest.mark.parametrize("path", ["/admin/users", "/admin/shops", "/admin/orders", "/admin/earnings", "/admin/restaurants", "/admin/restaurant/orders"])
    def test_admin_get(self, path):
        r = requests.get(f"{BASE}{path}", headers=H(S["admin"]), timeout=30)
        assert r.status_code == 200, f"{path}: {r.status_code} {r.text[:200]}"

    def test_admin_forbidden_for_customer(self):
        r = requests.get(f"{BASE}/admin/users", headers=H(S["cust"]), timeout=30)
        assert r.status_code == 403
