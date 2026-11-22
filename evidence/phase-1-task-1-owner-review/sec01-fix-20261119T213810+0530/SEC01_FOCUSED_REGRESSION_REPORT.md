# SEC-01 Focused Before/After Regression Report

COME-IN — Phase1Task1 scoped SEC-01 HIGH correction. Recorded 2026-11-19T16:16:40.606836+00:00 UTC. Repository `/workspace/come-in-current`, expected branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. Application extraction `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115` is outside Git and is bound by exact content hashes.

**Focused result: PASS after correction —20PASS,0FAIL,0ERROR,0SKIP. Concurrency validation: PASS.** The identical new runner produced10PASS/10FAIL before correction. Failed baseline invariants remain visible;no assertions or production helper bodies were weakened. This focused agent changed no protected source;the parent made the authorized reset_password-only correction. This report does not approve/closeTask1 or fix other findings.

## Source and runner binding

- Before source: `/workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/before/backend/server.py` SHA-256 `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db`.
- After source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py` SHA-256 `70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`.
- Runner SHA-256 identical for both invocations: `71d15423b6bf06ce679af2b02456f53233a67ec324f655246855cf6775b70a85`.
- Existing `mongo_transactions.py` helper SHA-256 unchanged: `b22cfd46e59d405cdaabf7585f6ec0a68a298cae718c8aea70f369bbfa06ba30`.
- Both source hashes remained unchanged during their respective executions. All20case IDs and intended invariant statements are identical before/after. JSON and JUnit totals agree.

## Exact commands and outcomes

Working directory: `/workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530`.

```sh
/workspace/come-in-tools/py311/bin/python -B sec01_focused_regression.py --stage before --source before/backend/server.py > focused-before.log 2>&1
/workspace/come-in-tools/py311/bin/python -B sec01_focused_regression.py --stage after --source /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py > focused-after.log 2>&1
```

Before:10PASS/10FAIL/0ERROR/0SKIP,exit1. After:20PASS/0FAIL/0ERROR/0SKIP,exit0. No harness correction/retry was needed. The two commands use the same test logic;only the source path/stage/output/database identity differs.

## Twenty unchanged intended invariants

| Case | Invariant | Before | After |
| --- | --- | --- | --- |
| SEC01-01 | Valid reset preserves the existing response and atomically updates both records | PASS | PASS |
| SEC01-02 | Unknown token returns existing400 without password hashing or writes | PASS | PASS |
| SEC01-03 | Expired token is rejected before TTL deletion without writes | PASS | PASS |
| SEC01-04 | Already consumed token remains rejected | PASS | PASS |
| SEC01-05 | Sequential replay cannot overwrite a committed password | PASS | PASS |
| SEC01-06 | Two synchronized valid preflight reads permit exactly one successful reset | FAIL | PASS |
| SEC01-07 | Three rounds of eight synchronized same-token requests have one winner each | FAIL | PASS |
| SEC01-08 | Token-write failure leaves no partial password change and allows safe retry | FAIL | PASS |
| SEC01-09 | User-write failure after a claim rolls back token consumption | PASS | PASS |
| SEC01-10 | Fault after the real user write but before commit rolls back both documents | FAIL | PASS |
| SEC01-11 | Transient transaction failure retries the body with only one durable paired result | FAIL | PASS |
| SEC01-12 | Unknown commit acknowledgement retries commit without rerunning password writes | FAIL | PASS |
| SEC01-13 | Lost response after committed success cannot make a retry overwrite the password | PASS | PASS |
| SEC01-14 | Missing target user cannot return success or consume a token | FAIL | PASS |
| SEC01-15 | Expiry is rechecked after successful preflight and before transactional claim | FAIL | PASS |
| SEC01-16 | A token consumed after preflight is rejected by the fresh claim | FAIL | PASS |
| SEC01-17 | Only the account bound to the token receives the password update | PASS | PASS |
| SEC01-18 | Unavailable transaction sessions fail closed without a standalone write fallback | FAIL | PASS |
| SEC01-19 | Existing reset request model length requirements are preserved | PASS | PASS |
| SEC01-20 | Existing transaction helper really rolls back an aborted real Mongo write | PASS | PASS |

## Real MongoDB transaction/fault evidence

The existing local `rs0` PRIMARY on127.0.0.1:27018 receives only newly generated synthetic fixtures in unique databases. Actual Motor collection operations execute with the real transaction session. Collection wrappers pass through the session and inject deterministic one-shot local errors;they do not replace persistence with in-memory doubles. No database or collection was dropped. Both test databases are retained.

The independent helper control case performs a real user write inside the unchanged transaction helper,raises a synthetic exception,and observes the field absent afterward. This separately proves the replica-set rollback prerequisite rather than assuming it from PRIMARY metadata.

- **SEC01-06:** both actual successful preflight reads finish before either caller proceeds;after correction exactly one reset succeeds and one receives the existing400 invalid/expired response. Before correction both can succeed.
- **SEC01-07:** after correction three separate rounds of eight synchronized callers each produce exactly one success and seven400 rejections. Before correction the case stops at its first failing eight-way round,not three completed rounds.
- **SEC01-08/09/10:** token-write-before,user-write-before,and failure immediately after an actual user write all leave password/token unchanged after abort. The same token then succeeds on one clean retry and rejects a later replay. Before correction token-marker failure and after-user-write failure leave partial committed state.
- **SEC01-11:** one TransientTransactionError after a real user write causes the driver to abort and rerun the actual callback. The new password is hashed once outside the callback,with one durable paired password/token outcome.
- **SEC01-12:** the first real commit succeeds,then a synthetic UnknownTransactionCommitResult acknowledgement is raised. The existing helper retries commit exactly once;callback and user/token writes execute once each. This is a controlled driver-boundary acknowledgement fault,not a claimed physical network outage.
- **SEC01-13:** a caller-side exception after completed success models response loss. Repeating the same token returns400 and cannot change the already committed password. This preserves existing duplicate-callback semantics;the baseline complete-success path also passed this case.
- **SEC01-14/15/16/18:** missing user rolls back the claim;expiry/used state is rechecked after preflight;unavailable transaction-session acquisition does not fall back to standalone writes. The session-unavailable case is a controlled client-boundary fault over the real replica-set fixture,not an actual standalone Mongo server deployment.

Sanitized after-run observations:

```json
{
  "SEC01-06": {
    "synchronized_preflight_reads": 2,
    "accepted": 1,
    "rejected400": 1
  },
  "SEC01-07": {
    "rounds": [
      {
        "accepted": 1,
        "rejected400": 7
      },
      {
        "accepted": 1,
        "rejected400": 7
      },
      {
        "accepted": 1,
        "rejected400": 7
      }
    ]
  },
  "SEC01-08": {
    "injected_fault_fired": true,
    "error_type": "RuntimeError",
    "password_and_token_unchanged_after_abort": true
  },
  "SEC01-09": {
    "injected_fault_fired": true,
    "error_type": "RuntimeError",
    "password_and_token_unchanged_after_abort": true
  },
  "SEC01-10": {
    "injected_fault_fired": true,
    "error_type": "RuntimeError",
    "password_and_token_unchanged_after_abort": true
  },
  "SEC01-11": {
    "error_type": null,
    "callback_calls": 2,
    "user_write_attempts": 2,
    "password_hash_calls": 1
  },
  "SEC01-12": {
    "error_type": null,
    "commit_calls": 2,
    "callback_calls": 1,
    "user_write_attempts": 1,
    "token_write_attempts": 1
  }
}
```

## Runtime,safety and limits

Python: `3.11.18 (main, Oct 26 2026, 14:05:07) [Clang 23.1.3 ]`. Executable `/workspace/come-in-tools/py311/bin/python`. Installed dependency versions: `{"motor": "3.7.1", "pymongo": "4.18.2", "bcrypt": "4.1.3", "pydantic": "2.14.3", "fastapi": "0.110.1"}`. No package installation or configuration change.

Before database: `comein_sec01_focused_before_20261119t161424z_f23513f3`;retained counts: `{"users": 21, "reset_records": 17}`.
After database: `comein_sec01_focused_after_20261119t161450z_ed7b5aed`;retained counts: `{"users": 21, "reset_records": 19}`.

Actual `reset_password`,request model,password hashing/verification,ObjectId parser and time helper source bodies are AST-extracted. Only route decorators are removed. This is function-level local integration,not FastAPI HTTP routing,dependency injection,middleware,production topology,SMTP delivery or external provider verification. The parent runs related original security/regression checks separately.

The throttle hook is a deliberately isolated no-op here so this focused suite neither changes nor adjudicates SEC-04. JWT,SMTP,password byte-policy,admin-role and other findings are not modified by this runner. Controlled expiry uses an isolated clock;controlled used-state changes act only on newly created token fixtures. No .env or actual credentials are loaded. Raw token/password/JWT/secret values are not written into result artifacts. Synthetic fixture strings in the runner are not real credentials. No real customer,production database,external payment/refund/provider call,global failpoint or database drop.

## Saved evidence and stopping point

- [sec01_focused_regression.py](sec01_focused_regression.py)
- [focused-before.json](focused-before.json), [focused-before.xml](focused-before.xml), [focused-before.log](focused-before.log)
- [focused-after.json](focused-after.json), [focused-after.xml](focused-after.xml), [focused-after.log](focused-after.log)
- [focused-before-after-summary.json](focused-before-after-summary.json)
- [SEC01_FOCUSED_TEST_CHECKPOINT.json](SEC01_FOCUSED_TEST_CHECKPOINT.json)
- [focused-artifact-hashes.json](focused-artifact-hashes.json)

No test operation remains running or interrupted. Parent should include these results in the SEC-01 correction/preservation report and manifest. No further repetition is needed without a new source change or specific unresolved evidence issue. The owner retains finalTask1review/approval;Task2,commit,push,deployment and publishing are not started.
