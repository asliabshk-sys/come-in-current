# Task 9 financial policy implementation

Starting GitHub commit `8e35b0ad2214c86d3d4edc749c3c3b3985f24a35`. Apply `patches/task9-approved-financial-policies.patch` after `patches/task9-financial-review.patch`. Forward and reverse patch validation passed.

- **Policy A.** The existing offer UI shows original and replacement prices and the difference. Rejecting an offer exposes a removal action that applies only to the affected line. Eligible unpaid Grocery and Restaurant orders use existing pricing and tax rules. The removal path rechecks remaining catalogue and menu references and enforces Restaurant minimum order. Grocery already-reserved units are checked for catalogue eligibility without deducting them again. Unfulfillable, legacy financial and paid cases enter Assist. A paid removal can show the proposed total and arithmetic difference when prices can be safely calculated. That amount is a review estimate. It is neither gateway eligibility nor an approved refund. Paid orders and provider records are preserved. Approval of a more expensive paid offer remains consent to Assist review. Refund and collection execution remain subject to the existing gateway rules.
- **Policy B.** Admin gets an order-scoped review showing original redeemed amount, current shopping reward balance, customer decision and reason. An authorized Admin can approve preserving the ledger or reject the adjustment. Decisions append to the existing audit collection and send one in-app notification in the same transaction. No automatic debit or balance change was introduced.
- **Policy C.** Admin can review the original invoice reference, original stored values, existing tax detail and decision history. Only externally verified Admin accounts configured as tax professionals can record professional review. A separate Admin decides after an approved professional review. The audit retains actor, date, guidance reference, proposed document type and reason. Customer ticket status excludes the confidential audit details. Approval remains pending the approved issuance procedure. No correction document is generated and original invoices are untouched.

**Files and persistence.** Changes in the patch cover `backend/server.py`, the Grocery and Restaurant replacement tests, the shared replacement component, Admin support and the existing CHAND support status. Optional fields were added to existing order and support documents, with decisions in the existing financial audit collection. No migration, collection, index, dependencies or payment provider changes. Task 8, Task 21 and the Master ZIP were preserved.

**Status — PARTIALLY COMPLETE.** [Decision register](DECISION_REGISTER.md) records the outstanding conditions. Native Android and iOS and genuine Razorpay TEST payment, webhook and refund verification remain deferred.

## Evidence

[Focused tests](focused.log) · [Full regression](full.log) · [TypeScript](typescript.log) · [ESLint](lint.log) · [Expo export](expo.log) · [Chromium](browser.log) · [Browser script](browser-smoke.py)

Final verification returned 46 focused passes and 695 full backend passes with zero failures. The external object-storage case was the sole skip. TypeScript, targeted ESLint, Expo web export and Chromium passed. Browser verification covered a Restaurant approval, the paid removal handoff and Admin reward rejection.

## Financial framework follow-up

See the [framework implementation and remaining decisions](../task-9-financial-policy-framework-20261123/IMPLEMENTATION_REPORT.md).
