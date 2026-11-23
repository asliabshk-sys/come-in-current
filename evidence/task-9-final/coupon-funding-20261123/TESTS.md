# Coupon-only verification — 23 November 2026

Run from the existing retained app with the [disposable replica set test setup](../approval-readiness-20261123/COMMANDS.md). The restart harness uses loopback port 8270 and deletes only its uniquely named fixture database.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_coupon_checkout.py
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_referral*.py backend/tests/test_financial*.py backend/tests/test_grocery_refund*.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_restaurant_refund_webhook_transaction_offline.py
python /workspace/come-in-current/evidence/task-9-final/coupon-funding-20261123/restart.py
```

Focused 1 passed. Expanded 82 passed. Both had zero failures/skips and seven deprecation warnings. The API restart harness passed two checks. Its first setup attempt exceeded MongoDB's database-name length limit. After shortening the fixture name, both checks passed. [Focused](focused.log) · [Expanded](expanded.log) · [Restart](restart.log)

The coupon test now covers mixed funding and Restaurant-target activation rejection, paid-order cancellation denial, rollback after the release write and detection of release audit entries tied to the wrong order. Prior budget race, wrong-order spend, refund-review, replay, authorization and closure checks still pass. The restart test creates a real fixture order, closes the campaign, checks the unchanged Admin ledger response after restart and verifies exactly one release on eligible unpaid cancellation. No production code or policy was changed.
