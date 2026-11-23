# Task 9 financial audit linkage and pending policy

**Status — PARTIALLY COMPLETE.** This increment links applied replacements to the existing finalized-order accounting ledger. The original idempotency key and order accounting policy still govern eligibility, amounts, and retries. Successful accounting recording indicates an eligible order ledger entry, while payout execution remains subject to the existing settlement controls.

- `backend/server.py` preserves original monetary values on new replacement records. Assist shows all applicable financial blockers, the order and replacement references, customer decision and timestamp, and any proposed item difference. The ticket update and order decision share the existing MongoDB transaction.
- The existing Admin support tab in `frontend/app/admin.tsx` displays the review and confirmation status. The existing support status actions do not execute a financial action.
- `backend/tests/test_task9_restaurant_replacement.py` covers combined blockers, Admin access, preservation of invoice data, simulated interruption and rollback, replay, and confirmed cash accounting without duplicate entries.

No payment, refund, payout, reward-balance, or tax-correction workflow was introduced. Backward-compatible optional fields were added to existing order, financial ledger and Assist documents. No migration, new collection, index or dependency was required. Task 8, Task 21 and the Master ZIP were preserved. Apply `patches/task9-financial-review.patch` after `patches/task9-restaurant-and-assist.patch`. Forward and reverse checks passed.

[Exact owner approvals and safe handling](DECISION_REGISTER.md)

## Verification

[Focused tests](focused.log) · [Full regression](full.log) · [TypeScript](typescript.log) · [ESLint](lint.log) · [Expo export](expo.log) · [Chromium](browser.log) · [Browser script](browser-smoke.py)

Native Android and iOS, genuine Razorpay TEST payments, and external TEST webhook and refund delivery remain deferred. No provider credentials or real transactions were used.

Final verification recorded 29 focused passes and 695 full regression passes with zero failures. The sole skip was the external object-storage case. TypeScript, targeted ESLint, Expo web export and both Chromium scenarios passed.

## Owner-approved policy follow-up

See the [approved policy implementation and remaining decisions](../task-9-approved-financial-policies-20261123/IMPLEMENTATION_REPORT.md).
