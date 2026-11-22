# Runtime verification for the 5-task batch (Tasks 15, 16, 20, 21 + 18 regression) — PREVIEW DB only.
# Requires: source tests/preview_test_env.sh && python tests/seed_preview_test_accounts.py
import uuid

import pytest
import requests

from test_preview_runtime_e2e import ADMIN, BASE, CUSTOMER, H, RESTO, SELLER, login

S = {}


def tok(creds):
    r = login(*creds)
    assert r.status_code == 200, r.text
    return r.json()["token"]


@pytest.fixture(scope="module", autouse=True)
def setup():
    S["admin"], S["cust"], S["seller"], S["resto"] = tok(ADMIN), tok(CUSTOMER), tok(SELLER), tok(RESTO)
    shop = requests.get(f"{BASE}/shops/mine", headers=H(S["seller"]), timeout=30).json()
    assert shop and shop.get("id"), "run test_preview_runtime_e2e.py first to create the TEST shop"
    S["shop_id"] = shop["id"]
    requests.patch(f"{BASE}/admin/shops/{shop['id']}/status", headers=H(S["admin"]), json={"status": "approved"}, timeout=30)
    requests.patch(f"{BASE}/shops/{shop['id']}/availability", headers=H(S["seller"]), json={"online": True}, timeout=30)
    prods = requests.get(f"{BASE}/shops/{shop['id']}/products", timeout=30).json()
    S["rice"] = next(p for p in prods if "Rice" in p["name"])
    S["dal"] = next(p for p in prods if "Dal" in p["name"])
    measured = next((p for p in prods if p.get("sell_by") == "weight"), None)
    if not measured:
        r = requests.post(f"{BASE}/shops/{shop['id']}/products", headers=H(S["seller"]), json={
            "name": "TEST Loose Sugar", "price": 48, "stock": 20000, "category_id": "grocery", "description": "Loose sugar sold by weight",
            "sell_by": "weight", "measure": {"min_qty": 250, "max_qty": 5000, "step": 250, "presets": [250, 500, 1000]}}, timeout=30)
        assert r.status_code == 200, r.text
        measured = r.json()
    S["sugar"] = measured


# ---------------- Task 15 — Admin panel
class TestAdminPanel:
    def test_dashboard_summary(self):
        r = requests.get(f"{BASE}/admin/dashboard", headers=H(S["admin"]), timeout=30)
        assert r.status_code == 200, r.text
        d = r.json()
        assert d["users"]["total"] >= 4 and "by_role" in d["users"] and d["push_configured"] is False
        assert "pending_approval" in d["shops"] and "last_24h" in d["grocery_orders"]

    @pytest.mark.parametrize("who", ["cust", "seller"])
    def test_dashboard_forbidden_for_non_admin(self, who):
        assert requests.get(f"{BASE}/admin/dashboard", headers=H(S[who]), timeout=30).status_code == 403

    def test_dashboard_requires_auth(self):
        assert requests.get(f"{BASE}/admin/dashboard", timeout=30).status_code == 401

    def test_announcement_edit_and_validation(self):
        r = requests.post(f"{BASE}/admin/announcements", headers=H(S["admin"]), json={"title": "TEST Notice", "body": "Original body", "audience": "all", "active": True}, timeout=30)
        assert r.status_code == 200, r.text
        aid = r.json()["id"]
        r = requests.patch(f"{BASE}/admin/announcements/{aid}", headers=H(S["admin"]), json={"title": "TEST Notice edited", "body": "Edited body", "audience": "customers"}, timeout=30)
        assert r.status_code == 200 and r.json()["title"] == "TEST Notice edited" and r.json()["audience"] == "customers"
        assert requests.patch(f"{BASE}/admin/announcements/{aid}", headers=H(S["admin"]), json={"audience": "everyone"}, timeout=30).status_code == 422
        assert requests.patch(f"{BASE}/admin/announcements/{aid}", headers=H(S["admin"]), json={"expires_at": "2000-01-01T00:00:00Z"}, timeout=30).status_code == 422
        assert requests.patch(f"{BASE}/admin/announcements/{aid}", headers=H(S["cust"]), json={"active": False}, timeout=30).status_code == 403
        assert requests.patch(f"{BASE}/admin/announcements/{aid}", headers=H(S["admin"]), json={"active": False}, timeout=30).json()["active"] is False

    def test_customer_cannot_change_roles(self):
        me = requests.get(f"{BASE}/auth/me", headers=H(S["cust"]), timeout=30).json()
        assert requests.patch(f"{BASE}/admin/users/{me['id']}/role", headers=H(S["cust"]), json={"role": "admin"}, timeout=30).status_code == 403


# ---------------- Task 16 — Security
class TestSecurity:
    def test_security_headers(self):
        r = requests.get(f"{BASE}/", timeout=30)
        assert r.headers.get("X-Content-Type-Options") == "nosniff" and r.headers.get("X-Frame-Options") == "DENY"

    def test_register_cannot_choose_role(self):
        email = f"test_{uuid.uuid4().hex[:8]}@example.com"
        r = requests.post(f"{BASE}/auth/register", json={"name": "TEST", "email": email, "password": "Passw0rd!", "role": "admin"}, timeout=30)
        assert r.status_code == 200 and r.json()["user"]["role"] == "customer"
        assert "password_hash" not in r.json()["user"]

    def test_forged_token_rejected(self):
        assert requests.get(f"{BASE}/auth/me", headers=H("eyJhbGciOiJIUzI1NiJ9.e30.invalid"), timeout=30).status_code == 401

    def test_login_bruteforce_is_rate_limited(self):
        email = f"nobody_{uuid.uuid4().hex[:8]}@example.com"
        codes = [requests.post(f"{BASE}/auth/login", json={"email": email, "password": "wrong-pass"}, timeout=30).status_code for _ in range(12)]
        assert codes[:10] == [401] * 10 and codes[-1] == 429, codes

    def test_invalid_input_rejected(self):
        r = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": [{"product_id": S["dal"]["id"], "qty": 0}], "fulfillment": "delivery"}, timeout=30)
        assert r.status_code == 422

    def test_customer_cannot_read_other_shop_orders(self):
        assert requests.get(f"{BASE}/shops/{S['shop_id']}/orders", headers=H(S["cust"]), timeout=30).status_code in (403, 404)


# ---------------- Task 21 — Customer shopping workflow (server side)
class TestShopping:
    def test_variant_priced_from_selected_variant(self):
        five = next(v for v in S["rice"]["variants"] if v["id"] == "5kg")
        q = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": [{"product_id": S["rice"]["id"], "variant_id": "5kg", "qty": 1}, {"product_id": S["rice"]["id"], "variant_id": "1kg", "qty": 2}], "fulfillment": "delivery"}, timeout=30)
        assert q.status_code == 200, q.text
        assert q.json()["subtotal"] == five["price"] + 2 * 120
        assert {i.get("variant_id") for i in q.json()["items"]} == {"5kg", "1kg"}

    def test_unknown_variant_rejected(self):
        q = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": [{"product_id": S["rice"]["id"], "variant_id": "nope", "qty": 1}], "fulfillment": "delivery"}, timeout=30)
        assert q.status_code in (400, 404, 409, 422)

    def test_measured_quote_and_order(self):
        sugar = S["sugar"]
        mp = requests.post(f"{BASE}/grocery/measured-price", json={"product_id": sugar["id"], "qty": 750}, timeout=30)
        assert mp.status_code == 200, mp.text
        q = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": [{"product_id": sugar["id"], "qty": 750}], "fulfillment": "pickup"}, timeout=30)
        assert q.status_code == 200, q.text
        assert q.json()["subtotal"] == 36.0 and q.json()["delivery_fee"] == 0
        bad = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": [{"product_id": sugar["id"], "qty": 300}], "fulfillment": "pickup"}, timeout=30)
        assert bad.status_code in (400, 409, 422), bad.text  # off-step amount
        r = requests.post(f"{BASE}/orders", headers=H(S["cust"]), json={"items": [{"product_id": sugar["id"], "qty": 750}], "fulfillment": "pickup", "customer_name": "Preview Customer", "customer_phone": "9999999999", "payment_method": "cash_shop", "quote_token": q.json()["quote_token"], "idempotency_key": uuid.uuid4().hex}, timeout=30)
        assert r.status_code == 200, r.text
        S["measured_order"] = r.json()["id"]

    def test_quote_cannot_be_reused(self):
        q = requests.post(f"{BASE}/grocery/quotes", headers=H(S["cust"]), json={"items": [{"product_id": S["dal"]["id"], "qty": 1}], "fulfillment": "delivery"}, timeout=30).json()
        body = {"items": [{"product_id": S["dal"]["id"], "qty": 1}], "delivery_address": "12 Test Lane", "fulfillment": "delivery", "customer_name": "P", "customer_phone": "9999999999", "payment_method": "cod", "quote_token": q["quote_token"]}
        first = requests.post(f"{BASE}/orders", headers=H(S["cust"]), json={**body, "idempotency_key": uuid.uuid4().hex}, timeout=30)
        assert first.status_code == 200, first.text
        S["cod_order"] = first.json()["id"]
        again = requests.post(f"{BASE}/orders", headers=H(S["cust"]), json={**body, "idempotency_key": uuid.uuid4().hex}, timeout=30)
        assert again.status_code in (409, 410, 422), again.text

    def test_online_payment_disabled_without_keys(self):
        r = requests.get(f"{BASE}/grocery/payments/config", timeout=30)
        assert r.status_code == 200 and not r.json().get("razorpay_enabled")


# ---------------- Task 20 — In-app notifications
class TestNotifications:
    def test_seller_gets_new_order_notification(self):
        r = requests.get(f"{BASE}/notifications/mine", headers=H(S["seller"]), timeout=30)
        assert r.status_code == 200 and r.json()["push_configured"] is False
        assert any(n["kind"] == "new_order" and n["data"].get("order_id") == S["cod_order"] for n in r.json()["items"])

    def test_customer_gets_status_notification_and_unread(self):
        assert requests.patch(f"{BASE}/orders/{S['cod_order']}/status", headers=H(S["seller"]), json={"status": "accepted"}, timeout=30).status_code == 200
        items = requests.get(f"{BASE}/notifications/mine", headers=H(S["cust"]), timeout=30).json()["items"]
        n = next(x for x in items if x["data"].get("order_id") == S["cod_order"] and x["data"].get("status") == "accepted")
        assert n["read"] is False and n["channel"] == "in_app" and n["push_status"] == "not_configured"
        unread = requests.get(f"{BASE}/notifications/unread-count", headers=H(S["cust"]), timeout=30).json()["unread"]
        assert unread >= 1
        assert requests.post(f"{BASE}/notifications/{n['id']}/read", headers=H(S["cust"]), json={}, timeout=30).status_code == 200
        assert requests.get(f"{BASE}/notifications/unread-count", headers=H(S["cust"]), timeout=30).json()["unread"] == unread - 1

    def test_notifications_are_owner_scoped(self):
        items = requests.get(f"{BASE}/notifications/mine", headers=H(S["cust"]), timeout=30).json()["items"]
        assert requests.post(f"{BASE}/notifications/{items[0]['id']}/read", headers=H(S["seller"]), json={}, timeout=30).status_code == 404

    def test_restaurant_status_notifications(self):
        rest = requests.get(f"{BASE}/restaurants/mine", headers=H(S["resto"]), timeout=30).json()[0]
        menu = requests.get(f"{BASE}/restaurants/{rest['id']}/menu", timeout=30).json()
        r = requests.post(f"{BASE}/restaurant/orders", headers=H(S["cust"]), json={"restaurant_id": rest["id"], "items": [{"menu_item_id": menu[0]["id"], "quantity": 1}], "contact_name": "P", "contact_phone": "9999999999", "fulfillment": "pickup", "payment_method": "pickup", "idempotency_key": uuid.uuid4().hex}, timeout=30)
        assert r.status_code == 200, r.text
        oid = r.json()["id"]
        owner_items = requests.get(f"{BASE}/notifications/mine", headers=H(S["resto"]), timeout=30).json()["items"]
        assert any(n["kind"] == "new_order" and n["data"].get("order_id") == oid for n in owner_items)
        assert requests.patch(f"{BASE}/restaurant/orders/{oid}/status", headers=H(S["resto"]), json={"status": "accepted"}, timeout=30).status_code == 200
        items = requests.get(f"{BASE}/notifications/mine", headers=H(S["cust"]), timeout=30).json()["items"]
        assert any(n["data"].get("order_id") == oid and n["data"].get("order_kind") == "restaurant" for n in items)

    def test_read_all(self):
        assert requests.post(f"{BASE}/notifications/read-all", headers=H(S["cust"]), json={}, timeout=30).status_code == 200
        assert requests.get(f"{BASE}/notifications/unread-count", headers=H(S["cust"]), timeout=30).json()["unread"] == 0

    def test_requires_auth(self):
        assert requests.get(f"{BASE}/notifications/mine", timeout=30).status_code == 401
