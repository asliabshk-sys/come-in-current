# Focused rewards and referral verification

Run with the existing [disposable MongoDB setup](../approval-readiness-20261123/COMMANDS.md). The restart harness uses loopback port 8273 and removes only its uniquely named fixture database.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_referral*.py backend/tests/test_shopping_rewards_redemption_contract.py backend/tests/test_task9_restaurant_replacement.py
python /workspace/come-in-current/evidence/task-9-final/rewards-referral-reversal-20261123/restart.py
```

Focused **17 passed, 0 failed, 0 skipped**, seven framework deprecation warnings. Restart **2 checks passed**, covering persisted credit and notice, duplicate approval, and full-refund release rejection with the original ledger unchanged. No environment-blocked checks in the focused scope. Executable reversal and compensating adjustments require approved rules. Physical device, external identity and genuine provider validations remain **DEFERRED — POST ALL APP TASKS**.

[Focused output](focused.log) · [Restart output](restart.log)
