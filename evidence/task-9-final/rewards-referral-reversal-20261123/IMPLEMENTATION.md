# Reward verification changes

Apply `patches/task9-rewards-referral-reversal-verification.patch` after the delivery-partner allocation verification patch. Retained files changed:

- `backend/server.py` — Admin reward advancement revalidates exactly ten distinct qualifying referral/order/customer links against the assigned reward referrer. Repeated, unrelated, or mismatched order links fail closed before ledger writes. Reward audit records previous and resulting status.
- `backend/tests/test_referral_task9_review_integration.py` — covers unauthorized approval, duplicate/foreign order references, cancellation and partial-refund preservation, accurate notification, and transaction rollback after a notification write.

The existing reward amount, eligibility threshold, payment attestation and release semantics are preserved. No reversal formula, payout, new benefit, balance rewrite, schema change, or external identity check was introduced.
