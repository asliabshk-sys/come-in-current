# Scoped expiry tests

Run from retained source with the [disposable MongoDB setup](../approval-readiness-20261123/COMMANDS.md). The restart script uses port 8275 and an isolated fixture database.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_coupon_checkout.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_premium_membership_integration.py backend/tests/test_task9_business_policy.py
python /workspace/come-in-current/evidence/task-9-final/offer-expiry-rules-20261123/restart.py
```

**12 passed, 0 failed, 0 skipped**, seven framework deprecation warnings. **Two restart checks passed.** No scoped environment blocker. Delayed online coupon payment, independent replacement expiry/cancellation, scheduled notices, multi-server clock skew and device-specific time presentation remain outside the tested cases. External devices and provider validation remain **DEFERRED — POST ALL APP TASKS**.

[Focused output](focused.log) · [Restart output](restart.log)
