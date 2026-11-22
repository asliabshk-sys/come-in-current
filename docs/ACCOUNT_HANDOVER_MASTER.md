# COME-IN account handover master

## 22 November 2026 — master task-board checkpoint

The canonical 22-task roadmap is reconciled in [COME_IN_MASTER_TASK_BOARD.md](COME_IN_MASTER_TASK_BOARD.md). At the start of that reconciliation, branch `work` and `origin/work` were equal at `0ecfbd08cc999d7106efbb0e28a6a9d3d56b114f` (zero ahead/behind; clean tree). This documentation-only session did not modify application source or run tests.

**Current decision point:** Task 1 is **APPROVED** by explicit owner decision on 22 November 2026; see `docs/TASK_1_OWNER_APPROVAL_RECORD_20261122.md`. This does not establish production readiness. `docs/TASK_2_PREPARATION_PROMPT.md` is a prepared, non-executable scope for canonical Task 2 (Theme and Design), which still requires separate owner authorization.

**Deferred/blocked:** native Android/iOS validation; genuine Razorpay TEST payment, webhook and refund validation; production configuration/infrastructure validation. These are neither failures nor passes and require a separate authorized phase/resources.

**Future checkpoint requirement:** after each meaningful session, update all five checkpoints plus relevant handover/decision records; review for secrets; commit and non-force push; fetch `origin/work`; verify exact HEAD equality, zero ahead/behind and a clean tree. If pushing fails, preserve the local checkpoint and document recovery rather than claiming synchronization.

## Task 2 status — 22 November 2026

Task 2 (Theme and Design / official app icon integration) is **REVIEW PENDING** following its owner-authorized local audit. The official owner-reference icon was already configured in Expo, Android adaptive-icon and web favicon paths; no source/artwork change was needed. Fresh local evidence: TypeScript 0 errors, ESLint 0 errors/7 warnings, Expo config PASS, web export PASS, static inventory 95 modules/53 route-layout files/0 parse diagnostics, and CHAND planner 11 assertions PASS. Native Android/iOS verification remains deferred and full runtime visual validation is not tested. Resume from `docs/TASK_2_EXECUTION_CHECKLIST.md` and `evidence/task-2-theme-icon-20261122/TASK_2_FINAL_REPORT.md`; wait for owner review and do not start Task 3.

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
