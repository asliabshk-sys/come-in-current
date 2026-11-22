"""Exercise exported Expo payment UI with deterministic API and Checkout fixtures."""
import os
import json
from urllib.parse import quote, urlsplit

from playwright.sync_api import expect, sync_playwright

WEB = os.environ.get("COMEIN_WEB_FIXTURE_URL", "http://127.0.0.1:8089")
API = os.environ.get("COMEIN_API_FIXTURE_URL", "http://127.0.0.1:18325")
SDK = """
window.checkoutCalls = [];
window.checkoutMode = 'cancel';
window.Razorpay = class {
  constructor(options) { this.options = options; }
  on(name, callback) { this.failed = callback; }
  open() {
    window.checkoutCalls.push({order: this.options.order_id, amount: this.options.amount, currency: this.options.currency});
    if (window.checkoutMode === 'cancel') this.options.modal.ondismiss();
    else if (window.checkoutMode === 'fail') this.failed({error: {description: 'Mock payment declined'}});
    else {
      const result = {razorpay_order_id: this.options.order_id, razorpay_payment_id: 'pay_fixture', razorpay_signature: 'fixture'};
      this.options.handler(result);
      this.options.handler(result);
    }
  }
};
"""

def run(browser, kind):
    page = browser.new_page(viewport={"width": 400, "height": 850})
    page.add_init_script(SDK)
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    member = kind == "membership"
    restaurant = kind == "restaurant"
    user = {"id": "fixture-user", "name": "Local Fixture", "email": "local@example.test",
            "role": "shopkeeper" if member else "customer"}
    order = {"id": "fixture-order", "ref": "ORDER FIXTURE", "total": 20,
             "status": "pending_payment", "payment_status": "pending" if restaurant else "razorpay_pending",
             "payment_method": "razorpay" if restaurant else "online_razorpay", "items": []}
    membership = {"id": "fixture-membership", "status": "payment_pending", "payment_verified": False}
    root = "/shops/fixture-shop/membership"
    seen = {"intent": 0, "verify": 0, "refresh": 0}
    verify_mode = "reject"

    def mock(route):
        path = urlsplit(route.request.url).path.removeprefix("/api")
        cors = {"access-control-allow-origin": "*", "access-control-allow-headers": "authorization, content-type",
                "access-control-allow-methods": "GET, POST, OPTIONS"}
        if route.request.method == "OPTIONS":
            route.fulfill(status=204, headers=cors)
            return
        status, value = 200, []
        if path == "/auth/login":
            value = {"user": user, "token": "local-browser-fixture"}
        elif path == "/auth/me":
            value = user
        elif path == "/shops/mine":
            value = {"id": "fixture-shop", "name": "Fixture Shop"}
        elif path == root:
            seen["refresh"] += 1
            value = membership
        elif path == root + "/history":
            value = [membership]
        elif path == "/orders/mine":
            value = [] if restaurant or member else [order]
        elif path == "/restaurant/orders/mine":
            seen["refresh"] += 1
            value = [order] if restaurant else []
        elif path == "/orders/fixture-order":
            seen["refresh"] += 1
            value = order
        elif path.endswith("/payment-intent"):
            seen["intent"] += 1
            value = {"key_id": "fixture", "gateway_order_id": "order_fixture", "currency": "INR",
                     "amount": 29900 if member else 2000, "order_ref": "ORDER FIXTURE",
                     "membership_id": membership["id"]}
        elif path.endswith("/payment-verify") or path.endswith("/payments/verify"):
            seen["verify"] += 1
            body = route.request.post_data_json
            assert body["razorpay_order_id"] == "order_fixture" and body["razorpay_payment_id"] == "pay_fixture"
            if not member:
                assert body["order_id"] == order["id"]
            if verify_mode == "reject":
                status, value = 502, {"detail": "Mock verification unavailable"}
            elif member:
                membership.update(status="payment_confirmed", payment_verified=True)
                value = membership
            else:
                order.update(status="pending", payment_status="paid")
                value = {"verified": True, "order": order}
        route.fulfill(status=status, body=json.dumps(value), content_type="application/json", headers=cors)

    page.route(API + "/api/**", mock)
    page.route("https://**", lambda route: route.abort())
    target = "/seller/membership" if member else "/restaurant/orders/fixture-order" if restaurant else "/orders"
    page.goto(WEB + "/auth?next=" + quote(target, safe=""))
    page.get_by_test_id("auth-email").fill(user["email"])
    page.get_by_test_id("auth-password").fill("local-fixture-password")
    page.get_by_test_id("auth-submit").click()
    page.wait_for_url(WEB + target)
    pay = page.get_by_text("Pay ₹299", exact=True) if member else page.get_by_test_id("grocery-pay-now-fixture-order")
    expect(pay).to_be_visible()
    pay.click()
    expect(page.get_by_text("Payment window closed.", exact=False)).to_be_visible()
    assert seen["verify"] == 0
    page.evaluate("window.checkoutMode = 'fail'")
    pay.click()
    expect(page.get_by_text("Mock payment declined", exact=True)).to_be_visible()
    assert seen["verify"] == 0
    page.evaluate("window.checkoutMode = 'success'")
    # Same-tick click pair exercises the synchronous lock before React disables the button.
    pay.evaluate("(element) => { element.click(); element.click(); }")
    expect(page.get_by_text("Mock verification unavailable", exact=True)).to_be_visible()
    assert seen["intent"] == 3 and seen["verify"] == 1
    expect(pay).to_be_visible()
    refresh_count = seen["refresh"]
    verify_mode = "confirm"
    pay.click()
    expect(pay).to_have_count(0)
    if member:
        expect(page.get_by_text("Payment confirmed — activation pending", exact=True)).to_be_visible()
        assert seen["refresh"] > refresh_count
    assert seen["verify"] == 2 and seen["intent"] == 4
    expected = {"order": "order_fixture", "amount": 29900 if member else 2000, "currency": "INR"}
    assert page.evaluate("window.checkoutCalls") == [expected] * 4
    assert not errors, errors
    print(f"PASS {kind}: dismiss, decline, duplicate tap/callback, failed verification, retry, and confirmed server result")
    page.close()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=os.environ.get("COMEIN_CHROMIUM", "/usr/bin/chromium"),
                                         args=["--no-sandbox"])
    for flow in ("grocery", "restaurant", "membership"):
        run(browser, flow)
    browser.close()
