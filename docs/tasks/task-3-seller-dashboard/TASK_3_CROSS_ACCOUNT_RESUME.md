# COME-IN Task 3 — Cross-Account Resume (READ FIRST)

**Repository:** https://github.com/asliabshk-sys/come-in-current
**Authorized branch:** `work`
**Task 3:** IN PROGRESS; **owner approval:** PENDING; **Task 4:** NOT STARTED.

## Latest verified checkpoint
Pre-session verified remote HEAD: `5732f3d343ef0fd4c9261ca0118d69528231a352`. This document is committed as part of a later evidence-only checkpoint. **Resolve the actual latest `work` remote SHA before resuming**; the final session message verifies it. Do not assume this embedded pre-session SHA is current.

## Completed and preserved
- November 15 source ZIP verified: 646 entries, SHA-256 `3233dcd9c8f1997b06035fd5cd7b458ab511658faf25e184044b17aec624d28c`; matches GitHub blob.
- Increment 01 recorded as `patches/task3-seller-dashboard-overview.patch`, historical implementation commit `d0f7297bb95b7a7470a533d2c0f3f590cf676391`; independent review `adb74acdf48e5823de2ed1d4d4b50b128d4e605a`; source reports `c828c840be22b33989b43fe7b01d10e045044c2a`, `d9deb11a0b74927df182f53ec463c51964cc0d40`.
- Current session: isolated historical source extraction; backend compile PASS; four focused seller contract test files yielded 18 PASS with `pytest -c /dev/null`; no application code changes.

## Read in order
1. `docs/tasks/task-3-seller-dashboard/TASK_3_CROSS_ACCOUNT_RESUME.md`
2. `TASK_3_MASTER_STATUS.md`
3. `TASK_3_CHECKPOINT.md`
4. `TASK_3_PENDING_WORK.md`
5. `TASK_3_VERIFICATION_REPORT.md` and `TASK_3_PROGRESS_LOG.md`
6. `AGENTS.md`, `COME_IN_LIVE_CHECKPOINT.md`, `COME_IN_MASTER_TASK_TRACKER.md`, `COME_IN_DECISIONS_AND_BLOCKERS.md`, `docs/TASK_3_IMPLEMENTATION_CHECKLIST.md`, `evidence/task-3-seller-implementation-20261122/`.

## Exact source candidates
- Historical archive: `COME-IN-COMPLETE-MASTER-SOURCE-20261115.zip` (in repository root).
- Potential newer snapshot: `archives/COME-IN-COMPLETE-MASTER-SOURCE-20261122-current-state-sanitized.zip`; **not yet byte-verified** in this session. Do not assume it is authoritative.
- Increment 01 patch: `patches/task3-seller-dashboard-overview.patch`.
- Source paths expected after reconciliation: `frontend/app/seller/dashboard.tsx`, `frontend/app/seller/help.tsx`, `frontend/app/(tabs)/account.tsx`, `frontend/app/become-seller.tsx`, `backend/tests/test_task3_seller_dashboard_contract.py`.

## Exact next actions
1. Connect to this existing GitHub repository; checkout `work`, pull and verify remote HEAD and clean local status; verify permissions rather than assuming access.
2. Inspect latest sanitized snapshot and November 15 source in **separate** isolated directories; calculate hashes and ZIP CRC; compare contents and patch applicability; never overwrite newer work.
3. Restore a disposable **review** working copy, preserve source architecture and history; verify Increment 01 without duplicate implementation.
4. Review seller dashboard/help/API/auth/ownership/financial/stock/security; run focused and regression tests, TypeScript, ESLint, Expo export where dependencies permit. Log PASS/FAIL/BLOCKED accurately.
5. Update all six Task 3 handoff files, review diff/secrets, commit/push evidence and actual authorized fixes to existing `work`; verify remote commit and all files. Do not start Task 4.

## Restrictions
No rebuild, blind restore, force push, unrelated feature, destructive migration, fake seller metrics, production payment changes or credentials in Git. CHAND customer UI text/voice only. Image uploads only in separately approved advertisement banner/poster feature. Owner alone may approve/close Task 3. Android/iOS device and Razorpay TEST checks deferred.

## Follow-up: November 22 archive cannot yet be verified
At start of this follow-up, `work` HEAD was `6e4d9e93a2567bf9115204d34be2f32c68b59c6a`. The sanitized archive exists as Git blob `b1e1d2c813185967dde4c979509410a95abd4d30` but GitHub connector returned no binary content; blob API UTF-8-only and terminal GitHub DNS blocked. **Do not assume patch is included or missing.** No code changed or QA rerun. Read the latest remote `work` HEAD (the final commit of this evidence-only follow-up is reported in the session response). Obtain the exact sanitized ZIP bytes via authorized network-enabled checkout or user upload, verify SHA-256/CRC/file list, compare against November 15 and Increment 01 patch, then resume safe implementation and tests. Task 3 IN PROGRESS; owner approval PENDING; Task 4 locked.

## 2026-11-22 binary recovery continuation
The GitHub November 22 sanitized archive is known as blob `b1e1d2c813185967dde4c979509410a95abd4d30`, but all tested binary retrieval methods failed: raw HTTPS and repo ZIP DNS failure; REST Contents/Git Blob UTF-8-only; connector `fetch_blob` UnicodeDecodeError; `fetch_file` empty. Do **not** claim its SHA-256/CRC or infer whether Increment 01 is included. Prior verified remote checkpoint at start: `7515e35afc2f1adeea7c6db6b8f85a482d3cfe9c`; check current remote `work` HEAD for this documentation-only follow-up. In a network-enabled authorized Codex environment retrieve the exact blob as binary to an isolated directory, verify hashes/integrity and compare November 15 archive and `patches/task3-seller-dashboard-overview.patch`. Do not apply patch twice. If proposing a new GitHub Actions workflow, obtain owner approval first. No app code changed. Task 3 IN PROGRESS, owner approval PENDING, Task 4 NOT STARTED.
