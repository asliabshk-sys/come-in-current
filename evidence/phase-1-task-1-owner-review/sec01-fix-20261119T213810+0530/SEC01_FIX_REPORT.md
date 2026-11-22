# COME-IN — SEC-01 scoped fix and owner-review report

Recorded 2026-11-19T21:53:23.407856+05:30 (Asia/Kolkata). Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. Application source is retained at `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115` outside Git.

**SEC-01 HIGH (token reuse and reset atomicity): FIXED. Focused regression: PASS. Concurrency validation: PASS. Task 1: REVIEW PENDING — not APPROVED or CLOSED.**

The owner explicitly authorized this minimal SEC-01 HIGH correction and focused tests. No other HIGH/MEDIUM/LOW finding was modified. The separate SMTP configuration LOW subissue remains open. Original reports,checkpoints,ZIP backups and Git history are retained unchanged as historical evidence;this report records the authorized delta.

## Exact source change

Only [backend/server.py — reset_password](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>) changed. [Exact source patch](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_SOURCE_CHANGE.patch>) and [source-change-before-after.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/source-change-before-after.json>) provide the complete delta. No imports,transaction-helper implementation,endpoint signature,request models,response fields,database schema/index definitions,UI or business architecture changed.

1. Keep the existing unused/unexpired-token preflight so invalid tokens still reject before bcrypt work.
2. Prepare the password hash once after that preflight, outside callback retries.
3. Inside the existing `run_transaction(client, apply)`, atomically claim the same token using `_id`,digest,`used=False` and a fresh expiry check. The claim and its `used_at` update use the supplied session.
4. Derive the account from the claimed record and update its password using that same session. Require exactly one matched user;otherwise abort with the existing generic HTTP400 error,rolling back the claim.
5. Commit both documents together. Transaction/failure paths never fall back to sequential standalone writes. Driver transient/unknown-commit behavior stays in the existing unchanged helper.

The matched-user check is necessary to the SEC-01 atomicity guarantee:consuming a token without a real password update must not return success. This also resolves the previously documented missing-user false-success subcase. It does not add schema or session-revocation policy. SMTP delivery,JWT revocation,rate limiting,bcrypt and admin-role behavior are unchanged.

## Before/after executable evidence

| Validation | Before fix | After fix | Evidence |
| --- | --- | --- | --- |
| Dedicated SEC-01 invariants | 10 PASS / 10 FAIL / 0 ERROR / 0 SKIP | 20 PASS / 0 FAIL / 0 ERROR / 0 SKIP | [SEC01_FOCUSED_REGRESSION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_FOCUSED_REGRESSION_REPORT.md>); [focused-before.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/focused-before.json>); [focused-after.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/focused-after.json>) |
| Stronger concurrency:distinct contender passwords | 0 PASS / 2 FAIL | 2 PASS / 0 FAIL | [focused-before.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/distinct-password-concurrency/focused-before.json>); [focused-after.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/distinct-password-concurrency/focused-after.json>) |
| Existing related tests (9 original modules) | Not unnecessarily repeated before the edit | 78 PASS / 0 FAIL / 0 ERROR / 0 SKIP | [OLD_RELATED_REGRESSION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/OLD_RELATED_REGRESSION_REPORT.md>); [old-related-existing.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-related-existing.xml>) |
| Historical 30-case security harness,with documented transaction-compatible instrumentation | 23 PASS / 7 FAIL | 26 PASS / 4 FAIL | [old-30-before-after-results.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-before-after-results.json>); [old-30-runner-harness.diff](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/old-30-runner-harness.diff>) |

The same focused runner/assertions are used for each before/after pair. The two stronger concurrency variants are not counted as22unique case IDs. All55original broader-harness invariant assertions were preserved;one HTTP400 guard was added for correct missing-user rejection. The post-user-write fault was moved to that actual operation boundary so it still tests the same no-partial-state invariant under the new operation ordering. No failure was skipped,xfailed or suppressed.

## Concurrency,rollback and retry results

Tests use actual extracted production function/model bodies,real bcrypt/Motor/PyMongo,and retained unique disposable MongoDB databases on loopback `rs0`. No production accounts,actual customer data,SMTP calls,provider credentials or payments were used. Full HTTP routing/middleware/provider/native acceptance is outside this focused scope. The dedicated suite stubs throttling to isolate SEC-01;the broader historical harness separately confirms the unchanged rate-limit finding.

- Two synchronized valid preflight reads produce exactly one successful reset and one existing HTTP400 rejection.
- Three independent eight-contender rounds produce exactly one success and seven HTTP400 rejections each. The stronger variants use distinct short synthetic passwords and verify that only the actual winner's credential authenticates;no loser's credential does. Password values are not logged.
- Faults before the token write,before the user write and after the real user write but before commit leave both password and token unchanged after abort. A clean retry succeeds once;replay cannot overwrite it.
- A labelled transient failure retries the callback after rollback with only one durable paired result and one prepared hash.
- A controlled lost commit acknowledgement after the real commit causes two commit calls,one callback,one token-write attempt and one user-write attempt. The callback is not replayed after success.
- A lost response after committed success cannot make a client retry overwrite the winning password.
- Expiry or consumption between preflight and transactional claim is rechecked. A missing target account rolls back the token claim. Transaction-session unavailability fails closed.

These are controlled function-level real-database integration tests,not a statistical load test,deployed exploit,actual network outage or standalone-server certification. No global MongoDB failpoint was used;no database was dropped. Per-run source/test hashes,versions,commands,timestamps,collection counts and retained database names are in the result JSONs.

## Remaining security findings and unchanged failures

| Case / finding | Current result | Disposition |
| --- | --- | --- |
| RESET-10 — SEC-01 SMTP configuration LOW subissue | FAIL unchanged | Malformed SMTP_PORT cleanup is outside this authorized HIGH atomicity fix;forgot/email-helper source is unchanged. |
| RESET-19 — SEC-02 MEDIUM | FAIL unchanged | Old JWT remains valid after reset;session policy/correction still requires separate owner authorization. |
| RESET-27 — SEC-04 MEDIUM | FAIL unchanged | Concurrent rate-limit overshoot remains;rate helper unchanged. |
| RESET-30 — SEC-06 LOW | FAIL unchanged | bcrypt long-input ambiguity remains;hashing/input policy unchanged. |
| SEC-03 / SEC-05 / SEC-07 / SEC-08 / SEC-09 | No change and no new closure claim | Original reported ingress/diagnostic/availability/body-limit/admin findings remain open with their prior evidence boundaries. |

The eight other canonical findings (six MEDIUM,two LOW) remain unmodified. The additional SMTP LOW subissue remains associated with SEC-01;it is not silently closed or renumbered. The broad 30-case suite therefore still has4known failures even though every authorized SEC-01 HIGH acceptance case now passes. Existing legacy-contract failures,native/device/provider blockers and production-evidence gaps are unchanged;large unrelated suites/builds were not rerun for this one-function Python change.

Task1is still **REVIEW PENDING**. This correction does not approve or close Task1,waive remaining gates or authorize Task2. Historical source-line references belong to the captured pre-fix source;the exact before-source backup is retained. Current source hashes and this patch supersede only the authorized SEC-01 code state.

## Preservation and hashes

| Item | Verified result |
| --- | --- |
| Existing protected baseline | 8,746 paths checked:8,745 unchanged;exactly1authorized change,backend/server.py;zero unauthorized/missing paths. |
| Outside changed function | 433 other top-level AST nodes unchanged out of434;signature/decorators unchanged. |
| Before-source backup SHA-256 | a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db |
| Current/after-source SHA-256 | 70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07 |
| Transaction helper SHA-256 (unchanged) | b22cfd46e59d405cdaabf7585f6ec0a68a298cae718c8aea70f369bbfa06ba30 |
| Previous owner-review package | Original manifest SHA24de73630bdcd28412a0b270e32ac5da7f88e61bb4ce85f2c2a405d17f563588 and all211member hashes unchanged. |
| Git | Branchwork/expectedHEAD;tracked/staged diff empty;pre-existing status outside new evidence unchanged. Application source delta is explicitly stored in the patch because extraction is outsideGit. |

Detailed proof: [SEC01_PRESERVATION_VERIFICATION.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_PRESERVATION_VERIFICATION.json>). Original root checkpoints and prior reports/manifests are not overwritten. Exact before and after source copies are [server.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/before/backend/server.py>) and [server.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/after/backend/server.py>). Actual secret.env/dependency/runtime-cache exclusions in historical baselines are not backdated or presented as production custody proof.

## Review package and stopping point

- [SEC01_INDEPENDENT_DESIGN_REVIEW.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_INDEPENDENT_DESIGN_REVIEW.md>)
- [SEC01_FOCUSED_REGRESSION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_FOCUSED_REGRESSION_REPORT.md>)
- [OLD_RELATED_REGRESSION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/OLD_RELATED_REGRESSION_REPORT.md>)
- [SEC01_TEST_AND_STATUS_SUMMARY.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_TEST_AND_STATUS_SUMMARY.json>)
- [SEC01_PRESERVATION_VERIFICATION.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_PRESERVATION_VERIFICATION.json>)
- [SEC01_RESUME_CHECKPOINT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_RESUME_CHECKPOINT.md>)
- [SEC01_EVIDENCE_MANIFEST.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_EVIDENCE_MANIFEST.json>)
- [SEC01_EVIDENCE_MANIFEST.sha256](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/SEC01_EVIDENCE_MANIFEST.sha256>)

No Task2,commit,push,deploy or publish. No protected source beyond the one authorized function/file changed. No remaining finding was modified. All test databases are retained and test processes ended. Exact next action:owner reviews this fix,patch and evidence and records the Task1review decision or separately scoped next authorization. No additional implementation is queued.

**SEC-01 HIGH: FIXED — scoped verification PASS. Task1: REVIEW PENDING.**
