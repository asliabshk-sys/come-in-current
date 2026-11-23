# Task 9 — Restaurant replacement and financial review

The starting GitHub `work` tip was `7c38337097dc540573eddae41e2a5cec6cf1500d`. The original Grocery flow and previous evidence are retained. Apply `patches/task9-restaurant-and-assist.patch` after the Grocery Task 9 patch. Forward and reverse patch checks passed.

## Delivered

- Restaurant sellers use the existing dashboard to report an unavailable line and choose a same-restaurant menu item or variant. Customers open the existing Restaurant order detail from an in-app notification, compare the line prices and applicable tax and fees, then approve an offer or reject it. The API also accepts up to five explicit options, including validated add-ons. The dashboard presents one seller-selected option per offer. Unaffected lines and original preparation instructions are retained.
- Eligible unpaid Restaurant approvals use the existing menu resolver and Restaurant tax calculator. The current tax rules must reproduce the original Restaurant subtotal, tax, delivery fee and total before repricing is allowed. The saved delivery fee is retained. Approval checks current menu and variant availability, options and price. Restaurant menu records represent stock availability as available/unavailable and carry no numeric stock counters. App updates to the same menu or tax configuration records conflict with a concurrent approval transaction. Customers alone can decide. A pending replacement blocks the ready transition. Replayed reports and decisions reuse the saved result.
- Paid or online orders and orders with rewards, coupons, historical tax discrepancies or recorded invoice details go to the existing COME-IN Assist queue with an explicit reason and the correct order kind. These offers show the item price difference with any financial change left for review. Acceptance records customer consent for review and preserves the original order, payment, rewards, tax and invoice records. The linked seller and customer can view the existing ticket. A case refresh reuses its linked ticket. A matching support submission returns the existing ticket. An existing open missing-item ticket can be reused by the replacement workflow.
- Existing earnings recognizes finalized and confirmed payment records. Existing administrative refund flows independently validate their own eligibility and provider confirmation. Neither provides policy that authorizes settlement, extra capture, refund or reward ledger amendment for a replacement proposal. Referral eligibility still uses the final eligible order under the existing rules. Replacement approval itself does not create a reward or settlement.

## Changes and boundaries

Source changed in `backend/server.py`, the Grocery and new Restaurant Task 9 tests, the shared replacement component, the Restaurant seller dashboard and order-detail screen, and the notification deep link. Added two Restaurant replacement endpoints that use existing roles, order collections, Mongo transactions, notification collection and support collection. Optional fields store replacement cases on Restaurant orders, link support cases, and serialize catalogue changes during approval. No migration, index, dependency, provider or new financial endpoint. Task 8, Task 21 and the Master ZIP were preserved.

**Pending policy** covers automated post-order financial settlement, reward-ledger amendments and any historical tax or invoice correction. Assist records decisions for review while those policies are pending. Paid order consent does not apply the replacement or alter the captured amount. The combined Task 9 tracker remains partially complete. Native Android/iOS, genuine Razorpay TEST payment, external webhook delivery and genuine TEST refunds are deferred to the authorized live-validation phase.

## Verification

- [Focused tests](focused.log)
- [Full backend regression](full.log)
- [TypeScript](typescript.log), [targeted ESLint](lint.log), [Expo web export](expo.log)
- [Local Chromium run](browser.log) and [reproduction script](browser-smoke.py)

Final result was 24 focused passes and 695 full backend passes with zero failures. The only skipped case required external object storage. TypeScript, targeted ESLint with zero warnings, Expo web export and the Chromium seller/customer scenario passed. The Mongo-backed suites covered assisted consent, reward and historical tax preservation, duplicate handling, and absence of financial ledger changes.
