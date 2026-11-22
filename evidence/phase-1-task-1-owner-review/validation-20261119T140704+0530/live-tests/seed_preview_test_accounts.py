"""Seed disposable PREVIEW test accounts (never run against production).

Registers TEST customer/seller/restaurant users through the public API and promotes the
seller accounts with the admin role-change endpoint. Idempotent.
Usage: python tests/seed_preview_test_accounts.py  (reads EXPO_PUBLIC_BACKEND_URL + admin env)
"""
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(__file__))
from test_preview_runtime_e2e import BASE  # noqa: E402

ADMIN = (os.environ["COMEIN_TEST_ADMIN_EMAIL"], os.environ["COMEIN_TEST_ADMIN_PASSWORD"])
ACCOUNTS = [
    ("COMEIN_TEST_CUSTOMER", "customer", "TEST Customer"),
    ("COMEIN_TEST_SELLER", "shopkeeper", "TEST Seller"),
    ("COMEIN_TEST_RESTO", "shopkeeper", "TEST Restaurant Owner"),
]


def main() -> None:
    admin = requests.post(f"{BASE}/auth/login", json={"email": ADMIN[0], "password": ADMIN[1]}, timeout=30)
    admin.raise_for_status()
    headers = {"Authorization": f"Bearer {admin.json()['token']}"}
    for prefix, role, name in ACCOUNTS:
        email, password = os.environ[f"{prefix}_EMAIL"], os.environ[f"{prefix}_PASSWORD"]
        r = requests.post(f"{BASE}/auth/login", json={"email": email, "password": password}, timeout=30)
        if r.status_code != 200:
            r = requests.post(f"{BASE}/auth/register", json={"name": name, "email": email, "password": password}, timeout=30)
            r.raise_for_status()
        user = r.json()["user"]
        if user["role"] != role:
            requests.patch(f"{BASE}/admin/users/{user['id']}/role", json={"role": role}, headers=headers, timeout=30).raise_for_status()
        print(f"{prefix}: {email} -> {role}")


if __name__ == "__main__":
    main()
