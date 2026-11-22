# Old Related Regression and Historical Security Runner Report

COME-IN — SEC-01 HIGH scoped remediation. Recorded 2026-11-19T21:44:08.792562+05:30 (Asia/Kolkata).

Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. Application source remains `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`. The parent alone applies the owner-authorized `reset_password` fix. This regression workstream changed no protected source, original tests, configuration, reports or checkpoints.

## Results actually executed

| Execution | PASS | FAIL | ERROR | SKIPPED | Process exit |
| --- | ---: | ---: | ---: | ---: | ---: |
| Nine original related regression modules, current fixed source | 78 | 0 | 0 | 0 | 0 |
| Same compatible historical30-case runner, immutable BEFORE source backup | 23 | 7 | 0 | 0 | 1 |
| Same compatible historical30-case runner, AFTER fixed source | 26 | 4 | 0 | 0 | 1 |

The AFTER 30-case suite is deliberately not reported all-green: four unrelated known security cases still fail. These failures remain real assertions, not xfails or suppressed results. This workstream validates the authorized fix and preserves unrelated findings rather than changing them.

| Authorized defect case | BEFORE | AFTER |
| --- | --- | --- |
| RESET-16 | FAIL | PASS |
| RESET-17 | FAIL | PASS |
| RESET-18 | FAIL | PASS |

`RESET-16` now permits at most one of two controlled concurrent consumers. `RESET-17` now observes rollback after a real password write followed by an injected failure and then permits a clean retry. `RESET-18` rejects a token referencing a missing user rather than reporting success;the transaction aborts its token claim. Parent focused tests provide additional stricter state, high-concurrency and retry coverage;these existing-case results are not substituted for that independent evidence.

Unchanged failing cases:

- `RESET-10`: malformed SMTP port raises before cleanup;LOW configuration subissue outside this HIGH atomicity correction.
- `RESET-19`: SEC-02 existing JWT revocation,MEDIUM.
- `RESET-27`: SEC-04 concurrent throttling cap,MEDIUM.
- `RESET-30`: SEC-06 bcrypt long-input alias,LOW.

## Exact source and harness boundaries

BEFORE source: `/workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/before/backend/server.py`; SHA-256 `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db`.

AFTER source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py`; SHA-256 `70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`.

Both stayed byte-identical throughout their individual executions. Same adapted runner SHA-256: `35dce6bb6dd30c633ab74130adc36ee35c7e11cf3a45388f92a0ca47e150a6d6`. Original historical runner SHA-256: `79952bdfc4bc80b54cb54709728eb9d80e299e469460c4ca50d3edc492ea27fd`. Both original and adapted runner are retained,with [old-30-runner-harness.diff](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-runner-harness.diff>) and [old-30-runner-compatibility.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-runner-compatibility.json>).

This is not a claim of byte-identical invocation of the old harness: transactional globals and test plumbing had to be supplied. All55original `require` calls remain AST-identical with multiplicity;one additional HTTP400 guard checks the intended missing-user rejection. No original invariant was removed or weakened.

Adaptations:

1. Source/output selectors choose the immutable BEFORE backup or current AFTER file and separate new output directories. Unique disposable database names prevent use of retained customer/application data.
2. Supply the real Motor client and unchanged existing `mongo_transactions.run_transaction` helper to the AST-extracted function namespace. No `server` import/startup or actual `.env` read.
3. For `RESET-17`,inject a failure immediately after the real `users.update_one` completes,forwarding `session`. The old implementation commits that password write before the fault;the new transaction must roll it and the token claim back. The existing partial-state assertion is unchanged. The former token-marker-specific fault would miss the new claim-first write ordering.
4. For `RESET-18`,accept the existing invalid-reset HTTP400 as rejection before the unchanged no-false-success assertion;without handling the expected exception,a correct fix would become a harness ERROR.

Real local MongoDB `rs0` PRIMARY at loopback27018 was used. BEFORE retained database: `comein_reset_sec01_compat_20261119t161203z_35dcae00a0`. AFTER retained database: `comein_reset_sec01_compat_20261119t161214z_3a4efd6dcb`. No drops/resets/global failpoints,real account credentials,SMTP delivery,provider requests or production access. Only synthetic fixture documents are written. The process permits loopback connections only;the actual email helper's transport is stubbed. Function tests do not establish FastAPI transport/middleware or provider/device behavior.

## Existing regression scope and safety

The nine original modules were read with `pytest.ini` before execution. They use static source checks,real pure helpers or explicitly in-memory collection/session doubles. An independent pytest plugin denied all socket connections. `PYTHONDONTWRITEBYTECODE=1`,`-p no:cacheprovider` and a new basetemp avoid writes to protected source/caches. No assertions or original test files changed.

- `test_mongo_transactions.py`
- `test_transaction_commit_retry.py`
- `test_restaurant_api_contract.py`
- `test_frontend_contracts.py`
- `test_shared_system_integration_contract.py`
- `test_grocery_capture_transaction_offline.py`
- `test_restaurant_capture_transaction_offline.py`
- `test_restaurant_refund_webhook_transaction_offline.py`
- `test_final_payment_transition_races.py`

The selection checks the existing transaction helper/commit-retry contract,shared auth/role/API/frontend contracts,and unchanged Grocery/Restaurant payment/refund transaction behavior after the single reset function change. Full574offline/70live and frontend builds were not unnecessarily repeated. All12bound source/test/config/helper paths matched before/after this78-case execution.

## Reproducible commands and artifacts

The wrappers record exact subprocess commands,cwd,timestamps,source hashes,exit codes and fixture database names:

```sh
/workspace/come-in-tools/py311/bin/python -B /workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/run-old-related-regression.py
/workspace/come-in-tools/py311/bin/python -B /workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/run-existing-related.py
```

The first command runs the same compatible runner serially with process-only `SEC01_SOURCE`/`SEC01_OUTPUT_DIR` selectors;no application environment file is changed. The precise actual subprocess commands and phase selectors are in [old-30-before-after-results.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-before-after-results.json>). The nine-module pytest command is in [old-related-existing-results.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-related-existing-results.json>).

- [related-regression.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/related-regression.json>) — combined evidence,hashes and source bindings.
- [old-related-existing.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-related-existing.xml>) and [old-related-existing.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-related-existing.log>) —78-case original regression output.
- [old-30-before/password-reset-results-v2.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-before/password-reset-results-v2.json>), [old-30-before/password-reset-junit-v2.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-before/password-reset-junit-v2.xml>), [old-30-before/execution.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-before/execution.log>).
- [old-30-after/password-reset-results-v2.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-after/password-reset-results-v2.json>), [old-30-after/password-reset-junit-v2.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-after/password-reset-junit-v2.xml>), [old-30-after/execution.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-after/execution.log>).

Only new run-specific evidence and compatibility-test scripts were written. No test operation remains running or interrupted. Last operation: both30-case executions and78-case original selection completed;source and assertion bindings verified. Next action: parent verifies the independent focused suite/concurrency evidence and final preservation/manifest. Task1 remains REVIEW PENDING;no owner approval,Task2,commit,push,deployment or publishing.
