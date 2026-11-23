# Task 9 closure evidence gates — 23 November 2026

Local HEAD, fetched origin/work and GitHub's work ref initially matched `54ebb6865de79ee6aba73ef628118a3fbaa897a8`. All 50 existing IDs and earlier evidence were read and preserved. This increment builds on the previous reconciliation patch. The retained app changes are published in `patches/task9-closure-evidence-gates.patch`.

| Area | Implemented local behavior and test coverage |
| --- | --- |
| Coupon | Admin reconciliation now validates each spend/release against its actual order receipt, including released receipts. A misattributed audit entry is detected even when the totals match. Orders with active refund evidence are counted for review. No automatic paid-refund release was added. Prior cash checkout transaction, cancellation and rollback tests still run. |
| Advertisement | An ended campaign review checks the original unique booking evidence claim, terms version, fee and caps. A booking claimed by another campaign is flagged for reconciliation. Fixed-duration shortfall and excess remain measurable with no compensation posted. |
| Delivery | New finalized ledger entries include the source delivery fee. Admin replacement reconciliation compares it to the current order fee when both are available. Historical entries are retained, and partner payable remains unavailable without a valid order-to-partner allocation. |
| Reward/referral | Admin replacement reconciliation joins the qualifying referral and award through the reviewed customer's original order. After cancellation/refund makes the linked order ineligible, it flags an existing award for reversal review while preserving the original balance and credits. |
| Incremental collection | A network-free Razorpay adapter prepares a separate INR order with a stable receipt, original capture link and amount in paise. It validates fixture orders, payments and signed webhook evidence. The Admin approval audit persists the sanitized request preview when a valid original capture exists. A read-only readiness endpoint revalidates consent, catalogue totals, payment linkage and refund conflicts. The endpoint and the stored preview keep execution disabled. |
| Partial/COD refunds | The same readiness check revalidates an approved refund review against live order and capture evidence. COD shows whether order delivery, cash confirmation, and the corresponding audit event are available. The checked audit marks cash collection only. Even a perfect match leaves payout pending an authorized rail. Existing partial legacy review and full-refund fixtures remain in the suite. |
| Statutory invoice | New professional approvals bind the original reference, tax detail and financial snapshot. Admin approval and draft creation reject a changed snapshot. The order version serializes review writes with concurrent order changes. Old approval rows and unique internal draft IDs are retained. No statutory numbering format, CA approval, tax computation or issuance was added. |

## Files

- `backend/server.py`
- `backend/integrations/replacement_collection.py`
- `backend/tests/test_task9_collection_adapter.py`
- `backend/tests/test_task9_business_policy.py`
- `backend/tests/test_task9_coupon_checkout.py`
- `backend/tests/test_task9_restaurant_replacement.py`
- `frontend/app/admin.tsx`
- `frontend/app/admin-earnings.tsx`

No new collection, migration, production index or external execution configuration. Task 8 and Task 21 have no direct diff, and the Master ZIP blob matches the baseline. No genuine payment, refund, transfer, ad credit or statutory document was issued.

Task 9 remains **PARTIALLY VERIFIED**. There are 31 verified policies with owner approval, 1 implemented awaiting external validation, 9 partially verified, 1 unimplemented, and 8 blocked. The [approval handoff](APPROVAL-HANDOFF.md) records the remaining decisions.
