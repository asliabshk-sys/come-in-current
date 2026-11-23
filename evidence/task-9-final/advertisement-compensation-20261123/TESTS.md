# Advertisement compensation verification

Run from the retained app with the [disposable MongoDB setup](../approval-readiness-20261123/COMMANDS.md). The restart harness creates its own disposable database on loopback port 8271 and cleans it up.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_business_policy.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py
python /workspace/come-in-current/evidence/task-9-final/advertisement-compensation-20261123/restart.py
```

- Focused final suite: **8 passed, 0 failed, 0 skipped**, seven framework deprecation warnings. Covers accepted terms, wrong owner, budget caps, duplicate references/events/review, authorization, shortfall/excess, invalid booking linkage, moderation/publication, Admin removal and transaction rollback after both booking and status audit writes.
- Restart: **2 checks passed**, verifying persisted immutable delivery review and removal replay without a duplicate audit or budget mutation.
- Initial focused run: **7 passed and 1 failed**. The older integration fixture pointed the application database at one Mongo client while the new transaction used another. The fixture now binds both to its disposable client and passed on rerun.
- Environment-blocked tests: none in the focused scope. External object storage, genuine booking/payment confirmation, compensation formula and financial execution are **DEFERRED — POST ALL APP TASKS** or require owner approval. Advertiser self-cancellation and dispute workflows are absent, so no execution cases exist for them.

[Final output](focused.log) · [Initial output](focused-initial.log) · [Restart output](restart.log)
