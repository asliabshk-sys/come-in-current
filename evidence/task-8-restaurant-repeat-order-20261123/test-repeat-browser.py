"""Browser rehearsal against a disposable COME-IN API, with synthetic order history."""
from os import environ
from playwright.sync_api import expect, sync_playwright

base = "http://127.0.0.1:8093"
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 425, "height": 950})
    page.route("https://**", lambda route: route.abort())
    page.goto(base + "/auth?next=%2Frestaurant%2Forders")
    page.get_by_test_id("auth-email").fill(environ["TASK8_BROWSER_EMAIL"])
    page.get_by_test_id("auth-password").fill(environ["TASK8_BROWSER_PASSWORD"])
    page.get_by_test_id("auth-submit").click()
    expect(page.get_by_text("TASK8-HISTORY", exact=True)).to_be_visible()
    page.get_by_role("button", name="Repeat Order", exact=True).click()
    expect(page.get_by_text("Repeat order started.", exact=False)).to_be_visible()
    expect(page.get_by_text("Removed side:", exact=False)).to_be_visible()
    expect(page.get_by_text("price changed from ₹45.00 to ₹110.00", exact=False)).to_be_visible()
    expect(page.get_by_text("Large · Dip", exact=True)).to_be_visible()
    expect(page.get_by_text("No onions", exact=True)).to_be_visible()
    print("PASS Restaurant history -> repeat cart, removed line, price change, saved selections and instructions")
    page.get_by_text("Continue to checkout", exact=True).click()
    expect(page.get_by_text("Current order summary", exact=True)).to_be_visible()
    expect(page.get_by_text("Total ₹121.00", exact=True)).to_be_visible()
    expect(page.get_by_text("Tax ₹11.00 · Delivery ₹0.00", exact=False)).to_be_visible()
    page.get_by_text("Pay at Pickup", exact=True).click()
    page.get_by_text("Place order", exact=True).click()
    page.wait_for_url("**/restaurant/order-confirmation**")
    print("PASS Updated server quote shown before checkout; new pay-at-pickup order placed")
    browser.close()
