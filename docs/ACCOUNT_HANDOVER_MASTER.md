# COME-IN account handover master

Date: 22 November 2026 (Asia/Kolkata)  
Repository: `https://github.com/asliabshk-sys/come-in-current`  
Working branch at handover preparation: `work`  
Pre-handover HEAD: `a223290a8866a1ebeaac982f546491fdc197ae7a`

## Purpose and recovery order

This repository is a handover package for a different Codex account. Start by reading `AGENTS.md`, the five root `COME_IN_*` checkpoint files, this document, and the latest Task 1 evidence package:

`evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/`

The original master source archive is `COME-IN-COMPLETE-MASTER-SOURCE-20261115.zip`. The current sanitized source snapshot is `archives/COME-IN-COMPLETE-MASTER-SOURCE-20261122-current-state-sanitized.zip` with SHA-256 `4cb8a397bee482b263e9b2f3ccf60d5818d20b42ecd60ef6c2bcc9fe6b041e33`. It contains the active source state but excludes `.env` files, keys, dependencies, caches and generated web output. Never use repository documentation as a source for credentials.

## Architecture

- Frontend: React Native + Expo Router, with web export; current source snapshot contains the Expo application and assets.
- Backend: FastAPI/Python service, MongoDB via Motor/PyMongo, API authentication/role dependencies and transaction helper.
- Database: MongoDB replica-set-capable design, application indexes and transactional order/payment/inventory paths. Test evidence uses retained disposable local databases only.
- Product surfaces: customer grocery shopping, Restaurant Mode, seller/admin/delivery workflows, Home Services entry points and CHAND AI. Preserve existing UI/theme/navigation and Restaurant Mode.
- Payments: Razorpay architecture with local source/mock coverage only. Provider TEST transactions, webhooks and refunds were not performed in this handover.

## Current status

Phase 1 Task 1 is **REVIEW PENDING — not approved or closed**. The final evidence package recommends “complete for owner approval,” but Codex cannot approve it. Task 2 is locked until explicit owner approval.

Task 1’s locally executable security/regression work is recorded as complete in the final evidence package. The current source snapshot includes all prior work plus the Task 1 corrections. Do not silently recreate or replace that work from the older original archive.

## Fresh Task 1 evidence

- Guarded backend offline/contracts: 578 PASS, 2 SKIPPED.
- Legacy isolated HTTP/Mongo: 23 PASS, 1 external-object-storage SKIPPED.
- SEC-01: 20 focused PASS plus 2 distinct-password concurrency PASS.
- Auth/JWT/bcrypt/SMTP: 25 PASS; proxy/rate limiting: 27 PASS; roles/diagnostics: 27 PASS.
- Payment/webhook local mocks: 30 PASS; not provider verification.
- Frontend lifecycle: 3 PASS; CHAND planner: 11 assertions PASS; TypeScript 0 errors; ESLint command PASS; web export PASS.
- A separate broad unscoped pytest diagnostic recorded 560 PASS, 26 SKIPPED and 17 environment errors caused by unavailable preview services, `/app` paths and a missing runtime server. It is retained as a diagnostic and is not included in guarded final PASS counts.

Read `TASK_1_FINAL_COMPLETION_REPORT.md`, `TASK_1_SECURITY_FINDINGS_SEC01_SEC09.md`, `TASK_1_PRESERVATION_VERIFICATION.md` and `TASK_1_FINAL_MASTER_MANIFEST.json` for exact scope and hashes.

## Security and approvals

SEC-01 through SEC-09 are documented as locally corrected and focused-tested. This does not establish production security. Remaining evidence limitations include production infrastructure, historical-run provenance, actual SMTP delivery and external-provider behavior.

Explicitly deferred, and **not authorized to run during Task 1**:

1. Android native build/device/payment validation.
2. iOS native build/device/payment validation.
3. Real Razorpay TEST payment, webhook delivery and refund settlement validation.

Use TEST credentials only when separately authorized; never place credentials in Git, chat, evidence or source. No production payment, refund, database modification, deployment or publishing is authorized by this handover.

## Important decisions and restrictions

- CHAND AI is the approved primary shopping-assistant entry point; do not restore obsolete “Request Anything” Home UI merely to satisfy stale tests.
- Preserve current architecture, authentication/API contracts, database, UI/theme/navigation and Restaurant Mode.
- Do not reset, clean, force-push, overwrite Git history, delete backups/evidence, or replace the application.
- The root checkout tracks archives, evidence and handover material. The active implementation has historically lived outside the checkout, so restore the sanitized source archive into a separate working directory and configure local placeholder/test environment files only.
- The repository’s original source ZIP SHA-256 is `3233dcd9c8f1997b06035fd5cd7b458ab511658faf25e184044b17aec624d28c`.

## Exact next safe action

1. Clone the repository and inspect `git status`, branch and HEAD; do not assume a historical test is fresh.
2. Verify the sanitized archive SHA-256 and `unzip -t` it, then extract it outside the Git checkout.
3. Read the five root checkpoints and all twelve final Task 1 reports before any source change.
4. Obtain explicit owner approval or rejection of Task 1 using `TASK_1_OWNER_APPROVAL_CHECKLIST.md`.
5. Only after approval and separately scoped authorization may the next task begin. Keep native/provider validations deferred until specifically authorized.

## Handover commit verification

After this document is committed, use `git log -1 --format=%H` and `git ls-remote origin refs/heads/work` to obtain the authoritative handover commit SHA. Do not infer it from this pre-commit snapshot.

## Synchronization record

The first handover-content commit `831481f456fe758c4bb15a643530da2c3cf27339` was pushed and independently verified at `refs/heads/work`. This follow-up record is committed separately so the final handover state itself is durable. The new account must always treat `git log -1` and `git ls-remote origin refs/heads/work` as authoritative rather than relying on an embedded SHA.

## Task 1 final reconciliation

On 22 November 2026 the final evidence manifest verified 189/189 entries. No unverified local implementation work remained. Task 1 is **REVIEW PENDING / ready for owner approval**, not approved/closed. Read `docs/TASK_1_FINAL_OWNER_APPROVAL_REPORT_20261122.md`; verify the current remote SHA at resume time.
