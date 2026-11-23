# Task 9 — Out-of-Stock Item Replacement

**Status — PARTIALLY COMPLETE.** The historical Task 25 implementation covered Grocery replacement in the cart before checkout. This change adds customer-approved, post-order replacement for signed-in Grocery orders with eligible unpaid cash terms. Starting GitHub `work` commit was `c202f279140a2ead58481d0fdc19b963a9585461` (Task 8).

## How to use it

1. In Seller Orders, report the unavailable line after confirming the units cannot be supplied. The signed-in customer gets one in-app notice with a link to the order. Proposals use the same shop's current catalogue, existing publication and availability gates, similar product names in the same category, and validated pack or measured quantities. They can include different variants, sizes, brands and smaller quantities where the matching catalogue offers them. Stock and prices are checked again when the customer decides.
2. The customer sees the original and proposed line prices, the price difference, the adjusted delivery fee and the resulting total. They can accept one specific offer, reject the options and wait for another offer, or expressly continue without the item. They can contact COME-IN Assist from that order. No seller, administrator or support operator can accept or reject on the customer's behalf.
3. In the existing order-linked support workflow, staff can verify the actual stock and price with the shop and have the shop refresh available options in Seller Orders. The customer reviews those options and decides in Order Tracking. Staff see the outcome in Seller Orders. Online/paid exceptions and issues that would leave the order empty remain open for assisted handling under existing access and payment controls.
4. The order cannot move to ready while a replacement decision or payment-assistance case is open. Eligible cancellation remains available and does not put physically unavailable stock back in the catalogue.

## Source, API and persistence

- `backend/server.py` adds seller/admin `POST /api/orders/{order_id}/replacements` and the customer's `POST /api/orders/{order_id}/replacements/{case_id}/decision`. The existing authorized order reads carry the optional replacement history. The ready transition checks the open state in the same database update used to change status.
- `frontend/src/components/GroceryOrderReplacements.tsx`, `frontend/app/order-tracking.tsx` and `frontend/app/seller/orders.tsx` use the current theme and existing screens. The customer's support link opens the existing COME-IN Assist order picker with the Grocery order selected.
- The existing Grocery checkout pricing and inventory helpers compute the changed line and totals. Grocery applies the existing ₹29 delivery fee below ₹199 and reports no separate checkout tax; pickup delivery remains zero. Saved unaffected lines and instructions are preserved. If catalog price, availability or quoted totals change after review, the decision fails safely and the seller can refresh offers. There is no payment operation or status change on approval.
- Cases, offer revisions and decisions are embedded in the order document. The same replica-set transaction stores the change, reserves accepted stock and inserts the customer in-app notification. Replayed and concurrent reports and decisions do not double-reserve or duplicate notices. No migration, index, collection or dependency added.
- `backend/tests/test_task9_grocery_replacement.py` covers the HTTP and frontend contracts. The repository stores the application change in `patches/task9-grocery-order-replacement.patch`. Apply it after `patches/task8-restaurant-repeat-order.patch`. Both forward and reverse application checks passed. Restaurant Repeat Order, Grocery Repeat Order, Task 21, the Master ZIP and provider integrations were preserved.

## Limits

- The customer-facing self-service flow covers unpaid COD, cash-at-shop and pay-at-pickup Grocery orders with a signed-in owner. Orders with online payments, recorded rewards or legacy tax amounts route to COME-IN Assist. Automatic settlement of replacement price differences, credit/refund on removals and recalculation of legacy taxed orders require a separately approved policy. Guest orders and last-line removals use eligible cancellation or assisted handling. Restaurant post-order replacement has no verified settlement/fulfilment policy and remains outside this implementation.
- Suggestions are bounded and based on current same-shop catalogue data and similar names. Physical verification, customer communication outside the app and any exception settlement are operator work in the existing support workflow. Local tests exercised order-linked ticket delivery to Seller Support. Native Android/iOS and genuine Razorpay TEST transactions remain deferred.

## Verification

- [Focused backend and frontend contracts](focused.log)
- [Full backend regression](full-backend.log)
- [TypeScript](typescript.log), [targeted ESLint](lint.log) and [Expo web export](export.log)
- [Chromium smoke](browser.log) and [reproduction script](browser-smoke.py)
- [Commands and run notes](COMMANDS.md)

Final verification recorded 22 focused passes and 689 full backend passes with zero failures and five skips. Four optional catalogue-parser skips were covered separately after adding the retained parser libraries to the test path. The entire catalogue module then passed 21 tests. The object-storage case remains skipped because external storage is unavailable. [Parser rerun](optional-catalogue.log)

## Follow-up implementation

This report preserves the Grocery milestone. The Restaurant replacement flow and the paid, reward and legacy tax Assist integration were added in a follow-up. [Follow-up report](../task-9-restaurant-assist-20261123/IMPLEMENTATION_REPORT.md)
