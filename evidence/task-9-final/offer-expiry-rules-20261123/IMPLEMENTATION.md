# Expiry boundary fixes

Apply `patches/task9-offer-expiry-verification.patch` after the partial/COD verification patch.

- `backend/server.py` enforces explicit timezone offsets for new advertisement windows, returns UTC campaign timestamps, rejects expired publication/resume, and checks both coupon window bounds at the atomic budget write. An expired/unavailable coupon returns the existing quote-refresh error contract, keeping the cart intact.
- `backend/tests/test_task9_coupon_checkout.py` exercises invalid/missing dates, just-before/at/after cutoff, rollback at final spend, and rejection of resume after expiry.
- `backend/tests/test_task4_storage_advertisement_integration.py` exercises missing/naive/reversed window validation, UTC conversion and expired publication.
- `restart.py` uses isolated test data to verify expiry and eligible cancellation release after API restart.

No duration, benefit, coupon liability, historical record, GST behavior, UI layout, payment transport or owner approval was changed.
