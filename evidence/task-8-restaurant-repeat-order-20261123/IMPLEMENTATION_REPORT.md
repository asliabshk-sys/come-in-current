# Task 8 — Restaurant Repeat Order

Baseline: `asliabshk-sys/come-in-current` branch `work` at `b4402235523be3b487a5416c1c47711f139a8a57`. Local and fetched/advertised GitHub references matched. Task 8 was partially verified at baseline. The retained Task 24 repeat-order report documents Grocery Repeat Order and explicitly identifies Restaurant Repeat Order as absent. The existing `backend/tests/test_task24_repeat_order_contract.py` contains five Grocery source tests. No earlier Restaurant repeat endpoint or six-test Restaurant suite was found. The Grocery tests and implementation are preserved.

## Implementation

- Restaurant order history offers **Repeat Order** for delivered and picked-up orders. The authenticated API rechecks ownership and eligibility. It reads the archived selections only, never mutating the original order or reusing its payment.
- `POST /restaurant/orders/{id}/repeat` uses current restaurant/menu data to resolve the exact item, variant, add-ons and instructions. Closed/unavailable restaurants and incompatible carts are blocked. Invalid individual lines are reported and skipped with no replacements. The customer sees unavailable selections and old-to-current unit price differences. If no line is valid, the cart is left unchanged.
- Compatible lines merge by restaurant, item, variant, add-on IDs and instructions. Valid quantities are preserved within the existing 99-per-line and 100-line limits. Existing cart stock/configuration errors require cart review. The app serializes the Repeat button and reuses its request ID after an interrupted response. The existing unique customer cart, compare-and-update and last-repeat receipt protect the write from the same request and concurrent changes.
- `POST /restaurant/cart/quote` recalculates current items, subtotal, restaurant tax and configured fulfilment fees. Restaurant checkout shows the server result, refreshes it before submission, and uses an optional quote fingerprint to detect a price/configuration change between review and final creation. The existing order endpoint still owns amount calculation and existing creation idempotency. Client-supplied prices and totals are ignored. Checkout refuses stale fingerprints and never charges an old amount. The existing COD, pickup and Razorpay paths remain in use.
- The existing Restaurant Cart displays variants, add-ons, instructions and repeat notices. Its quantities use configuration-specific row identity. No new screen, provider, collection, index or migration. Existing cart documents carry the optional last-repeat receipt beside their normal cart contents.

## Changed source

`backend/server.py`, `backend/tests/test_task8_restaurant_repeat.py` and the existing shared integration contract for the Restaurant pricing/ownership check. Frontend files: `frontend/app/restaurant/orders/index.tsx`, `frontend/app/restaurant/cart.tsx`, `frontend/app/restaurant/checkout.tsx`, and `frontend/src/restaurant/cart.ts`.

The repo stores application changes as a continuation patch. Apply `patches/task8-restaurant-repeat-order.patch` last, after the Task 4 storage and advertisement patch. Forward and reverse dry runs passed. The Master ZIP, Grocery Mode, Task 9 replacement and Task 21 comparison were left intact. The existing Task 7 checkout was extended only at its Restaurant quote integration point. Its address ownership, delivery serviceability, order creation, transaction/idempotency and payment paths were exercised in regression.

## Test commands and evidence

Tests used `APP_ENV=test`, synthetic local accounts, loopback FastAPI and a disposable MongoDB replica-set database. The fixtures do not call a real payment provider.

- `python -m pytest -q -n 0 --tb=short` over Test Task 8 Restaurant Repeat, Task 24 Grocery repeat contract, Restaurant API/pricing/serviceability and shared integration. **40 passed**. [Focused backend](focused.log)
- Full backend `python -m pytest -q -n 0 --tb=short -rs` with preview E2E and batch runtime first, then sorted remaining backend test modules including `backend_test.py`. [Full backend](full-backend.log)
- From `frontend/`, `tsc --noEmit`, targeted `eslint --max-warnings 0 app/restaurant/{cart,checkout,orders/index}.tsx src/restaurant/cart.ts`, `expo config --type public` and `expo export --platform web`. Python compilation and patch restoration also passed. [Build](frontend.log)
- `python test-repeat-browser.py` using a local Expo export, seeded synthetic history and real local HTTP. Verified Repeat through cart, a missing item notice and changed price, exact saved configuration, tax/fee summary and a new pay-at-pickup order. [Browser](browser.log)
- `python evidence/task-4-project-verification-20261123/test-checkout-browser.py` with loopback fixture origins. Grocery, Restaurant and Membership mocked payment flows all passed. [Mock payment regression](payment-regression.log)

The first integration run used a Restaurant fixture missing its delivery-available flag, so the existing coverage gate rejected the checkout before the price assertion. The fixture now opts into delivery explicitly. A previous source assertion expected the totals call inline; it now checks the shared authoritative pricing helper and its call from order creation. The earlier order/payment, Grocery and Task 9 assertions were preserved.

Physical Android and iOS device acceptance and genuine Razorpay TEST/payment operations remain deferred. No live gateway or device pass is claimed.

Final regression result: **687 passed, 0 failed, 5 skipped**. The skips were one unavailable external object-storage check and four optional catalogue-parser dependencies outside Restaurant Repeat Order. The two initial failures were resolved and rerun. There is no outstanding Task 8 local blocker.
