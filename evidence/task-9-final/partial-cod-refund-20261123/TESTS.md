# Scoped refund verification

Run from the retained app with the [disposable MongoDB fixture setup](../approval-readiness-20261123/COMMANDS.md). Restart harness uses loopback 8274 and its own disposable database.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_restaurant_replacement.py backend/tests/test_grocery_refund*.py backend/tests/test_restaurant_refund_webhook_transaction_offline.py backend/tests/test_step1_final_refund_admin_offline.py backend/tests/test_task10_payment_refund_notification_contract.py backend/tests/test_task11_grocery_refund_status_contract.py backend/tests/test_task18_refund_safety_iteration3.py
python /workspace/come-in-current/evidence/task-9-final/partial-cod-refund-20261123/restart.py
```

**56 passed, 0 failed, 0 skipped, 7 framework deprecation warnings.** Two additional restart checks passed. No scoped environment blockers. Partial and COD execution lacks approved allocation or payout rules. Actual COD amount has no independent collection evidence. These are policy/evidence limits, separate from test results. Genuine provider and physical device validation remains **DEFERRED — POST ALL APP TASKS**.

[Focused output](focused.log) · [Restart output](restart.log)
