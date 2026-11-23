# Scoped test evidence — 23 November 2026

Run from the retained source with the [disposable Mongo setup](../approval-readiness-20261123/COMMANDS.md). The restart harness uses port 8272 and deletes its uniquely named fixture database.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_delivery_partner_onboarding_contract.py backend/tests/test_step1_final_delivery_partner_transactions_offline.py backend/tests/test_delivery_tracking_contract.py backend/tests/test_financial_rules.py backend/tests/test_financial_security_contract.py backend/tests/test_task9_restaurant_replacement.py backend/tests/test_task9_business_policy.py
python /workspace/come-in-current/evidence/task-9-final/delivery-partner-allocation-20261123/restart.py
```

**51 passed, 0 failed, 0 skipped**, with seven framework deprecation warnings. Two restart checks passed. Verified onboarding approval rollback and retry behavior, fee linkage, malformed/mismatched evidence, payout reference constraints on the existing seller workflow, and absence of partner payable. Assignment, duplicate assignment, reassignment, partner failure/cancellation stages, and partner adjustment tests cannot exercise endpoints that are absent. No environment blockers in the focused run. External validation remains **DEFERRED — POST ALL APP TASKS**.

[Focused log](focused.log) · [Restart log](restart.log)
