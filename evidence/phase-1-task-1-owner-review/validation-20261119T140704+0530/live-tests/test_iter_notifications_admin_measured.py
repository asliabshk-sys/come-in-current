# Iteration regression: in-app notifications, admin RBAC/announcements, measured pricing.
import os
import pytest
import requests

from test_preview_runtime_e2e import _base
BASE_URL = (os.environ.get("EXPO_PUBLIC_BACKEND_URL") or _base()).rstrip("/")
API = f"{BASE_URL}/api"


def _login(email, password):
    r = requests.post(f"{API}/auth/login", json={"email": email, "password": password}, timeout=20)
    if r.status_code != 200:
        pytest.skip(f"login failed for {email}: {r.status_code}")
    return {"Authorization": f"Bearer {r.json()['token']}"}


@pytest.fixture(scope="module")
def customer():
    return _login(os.environ["COMEIN_TEST_CUSTOMER_EMAIL"], os.environ["COMEIN_TEST_CUSTOMER_PASSWORD"])


@pytest.fixture(scope="module")
def seller():
    return _login(os.environ["COMEIN_TEST_SELLER_EMAIL"], os.environ["COMEIN_TEST_SELLER_PASSWORD"])


@pytest.fixture(scope="module")
def admin():
    return _login(os.environ["COMEIN_TEST_ADMIN_EMAIL"], os.environ["COMEIN_TEST_ADMIN_PASSWORD"])


@pytest.fixture(scope="module")
def sugar_id(seller):
    """Measured sugar (48/kg, 250-5000 g, step 250) in the seller's shop; created when missing so the suite is portable."""
    shop = requests.get(f"{API}/shops/mine", headers=seller, timeout=20).json()
    products = requests.get(f"{API}/shops/{shop['id']}/products", timeout=20).json()
    products = products.get("items", products) if isinstance(products, dict) else products
    found = next((p for p in products if p.get("name") == "TEST Loose Sugar"), None)
    if found:
        return found["id"]
    r = requests.post(f"{API}/shops/{shop['id']}/products", headers=seller, timeout=20, json={
        "name": "TEST Loose Sugar", "price": 48, "stock": 20000, "category_id": "atta-rice-dal", "description": "TEST measured sugar",
        "sell_by": "weight", "measure": {"min_qty": 250, "step": 250, "max_qty": 5000, "presets": [250, 500, 1000]}})
    assert r.status_code == 200, r.text
    return r.json()["id"]


# Notifications
class TestNotifications:
    def test_mine_shape(self, customer):
        r = requests.get(f"{API}/notifications/mine", headers=customer, timeout=20)
        assert r.status_code == 200
        d = r.json()
        assert isinstance(d["items"], list) and isinstance(d["unread"], int) and d["push_configured"] is False
        assert all("_id" not in i for i in d["items"])

    def test_unauthenticated_rejected(self):
        assert requests.get(f"{API}/notifications/mine", timeout=20).status_code in (401, 403)

    def test_cannot_mark_other_users_notification(self, customer, seller):
        items = requests.get(f"{API}/notifications/mine", headers=seller, timeout=20).json()["items"]
        if not items:
            pytest.skip("seller has no notifications")
        r = requests.post(f"{API}/notifications/{items[0]['id']}/read", headers=customer, timeout=20)
        assert r.status_code == 404

    def test_read_all_zeroes_unread(self, seller):
        r = requests.post(f"{API}/notifications/read-all", headers=seller, timeout=20)
        assert r.status_code == 200 and "updated" in r.json()
        assert requests.get(f"{API}/notifications/unread-count", headers=seller, timeout=20).json()["unread"] == 0

    def test_invalid_id_404(self, customer):
        assert requests.post(f"{API}/notifications/notanid/read", headers=customer, timeout=20).status_code in (400, 404, 422)


# Admin RBAC + announcements
class TestAdmin:
    def test_customer_forbidden_admin_routes(self, customer):
        assert requests.get(f"{API}/admin/announcements", headers=customer, timeout=20).status_code == 403
        r = requests.patch(f"{API}/admin/users/000000000000000000000000/role", headers=customer, json={"role": "admin"}, timeout=20)
        assert r.status_code == 403

    def test_announcement_create_edit_deactivate(self, admin):
        r = requests.post(f"{API}/admin/announcements", headers=admin, json={"title": "TEST_pytest ann", "body": "TEST_ body", "audience": "all"}, timeout=20)
        assert r.status_code in (200, 201), r.text
        ann = r.json().get("announcement", r.json())
        aid = ann["id"]
        r = requests.patch(f"{API}/admin/announcements/{aid}", headers=admin, json={"title": "TEST_pytest ann EDITED"}, timeout=20)
        assert r.status_code == 200, r.text
        r = requests.patch(f"{API}/admin/announcements/{aid}", headers=admin, json={"active": False}, timeout=20)
        assert r.status_code == 200, r.text
        rows = requests.get(f"{API}/admin/announcements", headers=admin, timeout=20).json()
        rows = rows.get("items", rows) if isinstance(rows, dict) else rows
        mine = [a for a in rows if a["id"] == aid][0]
        assert mine["title"] == "TEST_pytest ann EDITED" and mine["active"] is False
        active = requests.get(f"{API}/announcements/active", timeout=20).json()
        active = active.get("items", active) if isinstance(active, dict) else active
        assert all(a["id"] != aid for a in active)


# Measured / loose pricing
class TestMeasured:
    def test_750g_sugar_price(self, sugar_id):
        r = requests.post(f"{API}/grocery/measured-price", json={"product_id": sugar_id, "qty": 750}, timeout=20)
        assert r.status_code == 200, r.text
        assert abs(float(r.json().get("amount", r.json().get("line_total", r.json().get("price", 0)))) - 36) < 0.01, r.text

    @pytest.mark.parametrize("qty", [700, 100, 6000, 0])
    def test_invalid_amounts_rejected(self, qty, sugar_id):
        r = requests.post(f"{API}/grocery/measured-price", json={"product_id": sugar_id, "qty": qty}, timeout=20)
        assert r.status_code in (400, 422), f"{qty}: {r.status_code} {r.text}"
