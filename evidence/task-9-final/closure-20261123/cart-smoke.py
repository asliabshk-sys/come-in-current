"""Test replacement of a persisted cart line against the real local catalogue."""
from bson import ObjectId
from playwright.sync_api import expect, sync_playwright
from pymongo import MongoClient

mongo = MongoClient("mongodb://127.0.0.1:27018/?replicaSet=rs0")
db = mongo.comein_disposable_task9_closure
shop = db.shops.insert_one({"name": "Cart fixture", "status": "approved", "online": True}).inserted_id
original, measured_original, eligible, excluded, unaffected = [ObjectId() for _ in range(5)]
products = {"shop_id": str(shop), "available": True, "category_id": "atta-rice-dal", "unit": "1 kg"}
db.products.insert_many([
    {**products, "_id": eligible, "name": "Fixture packet", "price": 40, "stock": 10},
    {**products, "_id": excluded, "name": "Measured bulk rice", "price": 35, "stock": 1000,
     "sell_by": "weight", "measure": {"min_qty": 250, "max_qty": 1000, "step": 250}},
    {**products, "_id": unaffected, "name": "Fixture unaffected", "price": 10, "stock": 8, "category_id": "dairy"},
])
snapshots = {
    str(identifier): {"id": str(identifier), "name": name, "categoryId": category, "shopId": str(shop),
                      "shopName": "Cart fixture", "source": "live", "price": price, "unit": "1 kg",
                      "sellBy": sell_by, "image": ""}
    for identifier, name, category, price, sell_by in (
        (original, "Fixture unavailable", "atta-rice-dal", 25, "pack"),
        (measured_original, "Unavailable bulk rice", "atta-rice-dal", 30, "weight"),
        (unaffected, "Fixture unaffected", "dairy", 10, "pack"),
    )
}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 425, "height": 950})
    page.route("https://**", lambda route: route.abort())
    page.goto("http://localhost:8081/cart")
    page.evaluate("""([items, snapshots]) => {
      localStorage.setItem("@comein_cart_v1", JSON.stringify(JSON.stringify(items)));
      localStorage.setItem("@comein_cart_product_snapshots_v1", JSON.stringify(JSON.stringify(snapshots)));
    }""", [{str(original): 2, str(measured_original): 500, str(unaffected): 1}, snapshots])
    page.reload()
    option = page.get_by_test_id(f"replace-{original}-with-{eligible}")
    expect(option).to_be_visible()
    expect(page.get_by_test_id(f"replace-{original}-with-{excluded}")).to_have_count(0)
    expect(page.get_by_test_id(f"replacement-options-{measured_original}")).to_have_count(0)
    option.evaluate("(element) => { element.click(); element.click(); }")
    expect(page.get_by_test_id(f"cart-price-{eligible}")).to_have_text("₹80")
    expect(page.get_by_test_id(f"cart-row-{original}")).to_have_count(0)
    expect(page.get_by_test_id(f"cart-price-{unaffected}")).to_have_text("₹10")
    page.reload()
    expect(page.get_by_test_id(f"cart-price-{eligible}")).to_have_text("₹80")
    expect(page.get_by_test_id(f"cart-price-{unaffected}")).to_have_text("₹10")
    print("PASS real catalogue, pack-only eligibility, double-click protection, unaffected line and persisted cart reload.")
    browser.close()
