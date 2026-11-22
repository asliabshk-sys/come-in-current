"""Run the exported Seller/Admin refund UI with local deterministic API fixtures."""
import json
from urllib.parse import quote, urlsplit

from playwright.sync_api import expect, sync_playwright

WEB = "http://127.0.0.1:8090"
API = "http://127.0.0.1:18328/api"
payment = {"id": "fixture-payment", "payment_verified": True, "status": "payment_confirmed", "created_at": "2026-11-23T00:00:00Z"}
case = {"id": "pay_fixture", "shop_id": "fixture-shop", "membership_id": payment["id"],
        "reason": "pre_activation", "created_at": payment["created_at"], "state": "REQUESTED"}
sent = []

def simulate(browser, role):
    page = browser.new_page(viewport={"width": 420, "height": 900})
    user = {"id": "local-fixture", "role": role, "name": "Fixture", "email": "fixture@example.test"}

    def mock(route):
        path = urlsplit(route.request.url).path.removeprefix("/api")
        method = route.request.method
        headers = {"access-control-allow-origin": "*", "access-control-allow-headers": "authorization, content-type",
                   "access-control-allow-methods": "GET,POST,PATCH,OPTIONS"}
        if method == "OPTIONS":
            return route.fulfill(status=204, headers=headers)
        data = []
        if path == "/auth/login": data = {"user": user, "token": "fixture-token"}
        if path == "/auth/me": data = user
        if path == "/shops/mine": data = {"id": "fixture-shop", "name": "Fixture Shop"}
        if path == "/shops/fixture-shop/membership": data = payment
        if path == "/shops/fixture-shop/membership/history": data = [payment]
        if path == "/shops/fixture-shop/membership/refunds":
            if method == "POST":
                body = route.request.post_data_json
                assert body["membership_id"] == payment["id"] and body["reason"] == "pre_activation"
                sent.append(body)
                data = case
            else:
                data = [case] if sent else []
        if path == "/admin/memberships/report":
            data = {"total_requests": 1, "exposure": {"by_shop": [], "search": {}, "ctr": None}}
        if path == "/admin/membership-refunds": data = [case]
        if path == "/admin/membership-refunds/pay_fixture" and method == "PATCH":
            body = route.request.post_data_json
            assert body["action"] == "approve" and body["reason"] == "Documented fixture approval"
            case.update(state="APPROVED", remedy="refund", decision_reason=body["reason"])
            data = case
        return route.fulfill(status=200, headers=headers, content_type="application/json", body=json.dumps(data))

    page.route(API + "/**", mock)
    page.route("https://**", lambda route: route.abort())
    target = "/seller/membership" if role == "shopkeeper" else "/admin-memberships"
    page.goto(WEB + "/auth?next=" + quote(target, safe=""))
    page.get_by_test_id("auth-email").fill(user["email"])
    page.get_by_test_id("auth-password").fill("local-fixture")
    page.get_by_test_id("auth-submit").click()
    page.wait_for_url(WEB + target)
    expect(page.get_by_text("Membership refunds", exact=True)).to_be_visible()
    if role == "shopkeeper":
        page.get_by_role("button", name="fixture-payment", exact=False).click()
        page.get_by_label("Refund explanation").fill("Cancellation requested before activation")
        page.get_by_text("Request refund review", exact=True).click()
        expect(page.get_by_text("REQUESTED · pre activation", exact=True)).to_be_visible()
        print("PASS Chromium seller selects verified payment, supplies reason, and sees submitted case")
    else:
        expect(page.get_by_text("REQUESTED · pre activation", exact=True)).to_be_visible()
        page.get_by_label("Decision reason").fill("Documented fixture approval")
        page.get_by_text("approve", exact=True).click()
        expect(page.get_by_text("APPROVED · pre activation", exact=True)).to_be_visible()
        expect(page.get_by_text("Process approved refund", exact=True)).to_be_visible()
        print("PASS Chromium admin reviews and approves without displaying gateway success")
    page.close()

with sync_playwright() as play:
    browser = play.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    simulate(browser, "shopkeeper")
    simulate(browser, "admin")
    browser.close()
