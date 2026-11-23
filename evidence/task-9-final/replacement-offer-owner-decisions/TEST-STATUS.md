# Existing tests rerun — 23 November 2026

From `/workspace/task4-source` with the existing [disposable MongoDB fixture setup](../approval-readiness-20261123/COMMANDS.md):

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_grocery_replacement.py backend/tests/test_task9_restaurant_replacement.py backend/tests/test_task9_order_actions_contract.py
```

Actual result: **14 passed, 0 failed, 0 skipped, 0 environment blockers**. Pytest reported seven framework deprecation warnings and completed in 5.04 seconds.

The suites exercised existing report and accept/reject paths, stale options, stock rollback, duplicate requests, non-owner denial, supersession and reoffer, order action guards and financial review. No timed replacement expiry, independent cancellation, legacy-offer migration or corresponding restart test was executed. Those behaviors are unimplemented and await policy. All writes used disposable fixtures. No test or application source changed.
