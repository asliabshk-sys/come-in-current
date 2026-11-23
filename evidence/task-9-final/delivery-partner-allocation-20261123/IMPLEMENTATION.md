# Delivery allocation reconciliation fix

Retained source changed only in `backend/server.py` and `backend/tests/test_task9_restaurant_replacement.py`. Apply `patches/task9-delivery-partner-allocation-verification.patch` after the advertisement compensation patch.

An invalid stored fee could abort Admin replacement reconciliation. The comparison now reports a mismatch and retains the stored values for review. Missing fee data continues to report an unavailable comparison. Tests cover matching, mismatched and malformed evidence plus owner-scoped onboarding access by application status. The script in this folder exercises fee evidence across a real API process restart using synthetic records. No order data, historical ledger, fee, payout rule, schema, or assignment model was changed in production. New eligibility, assignment priority and payable behavior await actual authorization.
