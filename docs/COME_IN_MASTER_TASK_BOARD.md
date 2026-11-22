# COME-IN Master Task Board

**Reconciled:** 22 November 2026 (Asia/Kolkata)
**Repository:** `asliabshk-sys/come-in-current` — `/workspace/come-in-current`
**Branch / verified remote-local HEAD:** `work` / `0ecfbd08cc999d7106efbb0e28a6a9d3d56b114f`
**Authority:** recovered original roadmap (`COME_IN_TASK_1_ORIGINAL_ROADMAP_RECOVERY.md`), existing master tracker, Task 1 evidence package, and owner-approval record.

## How to read this board

`COMPLETED` means retained implementation and supporting evidence exist. It is not a new runtime claim and it does not supersede an external validation gate. `VERIFIED` is used only where the cited evidence was independently checked for the current documented state. `REVIEW PENDING` requires an owner decision. `IN PROGRESS`, `BLOCKED`, `DEFERRED`, and `NOT STARTED` retain their ordinary meanings.

The recovered roadmap contains **22 canonical tasks**. Report labels such as Task 23–25 and Task 26–30 are later report/work labels, not extra canonical roadmap tasks; no new task order is inferred from them.

## Current control gate

| Gate | Status | Evidence / exact next action |
|---|---|---|
| Task 1 — Existing Project Audit | **REVIEW PENDING** | Final package manifest: 189/189 hashes verified; owner must accept limitations, review the seven intentional source/test changes, explicitly approve/reject closure, and separately authorize Task 2. |
| Task 2 and later execution | **BLOCKED** | Task 2 is prepared below but must not start until the owner expressly approves Task 1. |
| Android / iOS native validation | **DEFERRED** | Separate authorized native/device phase required. |
| Razorpay TEST payment, webhook, refund | **DEFERRED** | Separate authorized provider phase with TEST credentials and webhook endpoint required. |
| Production configuration / infrastructure validation | **BLOCKED** | Requires approved non-production-equivalent deployment evidence and owner-controlled configuration; no production action is authorized. |

## Canonical task board

| ID | Canonical task | Original objective (condensed) | Reconciled status | Existing evidence / completed work | Pending, deferred, or dependency | Exact next action |
|---:|---|---|---|---|---|---|
| 1 | Existing Project Audit | Audit app, routes, workflows, API, DB, auth, gaps and duplicates before fixes. | **REVIEW PENDING** | Final owner package, security evidence, regression records; 189-entry final manifest verified. | Owner review/approval; external validation remains separate. | Owner completes the Task 1 checklist below. |
| 2 | Theme and Design | Consistent mobile design: yellow/forest-green/pale-mint, readable rounded cards and spacing. | **COMPLETED** | Historical theme reports and preserved source. | Visual/device recheck is not fresh evidence. Depends on Task 1 approval for any new work. | Do not execute; use prepared Task 2 brief after approval. |
| 3 | Home Screen and Navigation | Clear access to online/offline shops, restaurants, Home Services and return paths. | **COMPLETED** | Historical route/UI evidence; CHAND-only decision retained. | Full device check deferred. | Revalidate only if a future approved change touches navigation. |
| 4 | Categories and Catalog | Grocery, essentials, local shops and restaurant catalog/menu. | **COMPLETED** | Historical catalog runtime evidence and source. | No fresh runtime run in this reconciliation. | Revisit only when catalog scope changes. |
| 5 | Quantity, Variants and Units | Size, weight, quantity, variants, unit pricing. | **COMPLETED** | Historical Mongo/transaction and measured-order evidence. | Low finding F-1: conflict loser response semantics; native/provider out of scope. | Triage F-1 only under an authorized defect task. |
| 6 | Search and Filters | Product/shop/restaurant search and relevant filters. | **COMPLETED** | Earlier reports and source retained. | Runtime recency not established. | Revalidate only on approved search/filter changes. |
| 7 | Cart and Checkout | Secure cart, price/stock revalidation, separate restaurant/grocery carts. | **COMPLETED** | Checkout/idempotency source and historical COD/pickup evidence. | Expo/device runtime deferred. | Revalidate on approved checkout change. |
| 8 | Repeat Order | Re-select old items with current stock and price checks. | **COMPLETED** | Earlier Task 24 report and source. | Measured extension not independently fresh. | Revalidate only on approved repeat-order work. |
| 9 | Out-of-Stock Replacement | Customer-controlled replacement/removal. | **COMPLETED** | Earlier Task 25 report and source. | No fresh run. | Revalidate only on approved replacement work. |
| 10 | Live Tracking | Truthful order tracking when backed by real data. | **COMPLETED** | Historical tracking endpoint E2E evidence. | No fresh runtime evidence. | Revalidate with a safe runtime environment when scope changes. |
| 11 | Order Help and Refund Status | Help, cancellation, refund status and shop-call assistance. | **IN PROGRESS** | Restaurant safeguards and grocery summary-state/offline coverage. | Provider-backed grocery refunds, notification/reconciliation and live role synchronization. | Schedule only after explicit provider-validation authorization. |
| 12 | Excel/CSV Price and Stock Import | Validated stable-ID price/stock import without duplicates. | **COMPLETED** | Import hardening and parser coverage retained. | Disposable-DB measured import apply evidence is historical/limited. | Revalidate when import flow is changed. |
| 13 | Login and Account | Secure account, profile and order history across modes. | **COMPLETED** | Historical auth/rate-limit evidence and Task 1 security corrections. | OTP is not part of current verified scope. | Revalidate upon any auth change. |
| 14 | Seller/Shop/Restaurant Panel | Manage products, prices, availability, menus and orders. | **COMPLETED** | Source and historical seller/restaurant evidence. | Fresh device/runtime test deferred. | Revalidate on approved panel change. |
| 15 | Admin Panel | Admin controls, management, announcements and RBAC. | **COMPLETED** | Historical UI/API/RBAC evidence. | Full current runtime test not established. | Revalidate on approved admin change. |
| 16 | Backend, Database and Security | Auth, authorization, validation, secrets, DB protection and recovery. | **IN PROGRESS** | SEC-01–SEC-09 local corrections and guarded test evidence. | SMTP delivery, restore drill, deployed CORS and external audit; OTP/session-management product decisions. | Address only under an approved security/reliability task. |
| 17 | Payments and Notifications | Secure payment and notification architecture. | **IN PROGRESS** | Local payment/webhook mocks and gated source controls. | Real Razorpay TEST flows, native sheets, provider refund lifecycle, push configuration. | Wait for separate TEST-provider authorization/resources. |
| 18 | Testing and Bug Fixes | Regression, bug reconciliation and release quality. | **IN PROGRESS** | Guarded local suites and Task 1 regression package. | External/runtime/native/provider coverage and future defect work. | Run focused tests only when an approved change warrants them. |
| 19 | Production Build and Launch | Production build/deployment/launch. | **BLOCKED** | No production action taken. | Owner approval, credentials, deployment plan, costs, production validation. | Do not start without separate authorization. |
| 20 | Smart Notification System | In-app and push notification behavior. | **IN PROGRESS** | In-app center/read state/role scope evidence retained. | Firebase/native configuration and real push delivery. | Await native/push authorization and configuration. |
| 21 | Smart Price Comparison | Comparison UI and data rules. | **IN PROGRESS** | Source/UI preserved. | Linked-master endpoint runtime and distance data evidence. | Define/authorize data source and runtime validation. |
| 22 | Home Services Logo/Icon and Tile Integration | Home Services visual tile and entry integration. | **COMPLETED** | Existing report and source/evidence retained. | No new work identified. | Revisit only if product direction changes. |

## Task 1 owner approval checklist

- [x] Final evidence package exists at `evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/`.
- [x] `TASK_1_FINAL_MASTER_MANIFEST.json` records 189 entries; all were hash-verified in the saved review.
- [x] SEC-01–SEC-09 local source-level corrections and focused evidence are recorded.
- [x] Locally guarded backend/frontend/security evidence is preserved; the unscoped diagnostic with 17 environment errors is disclosed and excluded from guarded PASS totals.
- [x] Architecture, source archive and protected-file preservation evidence is recorded.
- [ ] Owner accepts the historical and external-validation limitations.
- [ ] Owner reviews the seven intentional source/test changes listed in `TASK_1_CHANGED_FILES_AND_PATCHES.md`.
- [ ] Owner explicitly approves or rejects Task 1 closure.
- [ ] Owner separately authorizes Task 2.

**Missing acceptance evidence (not a local failure):** native Android device/build validation; native iOS device/build validation; genuine Razorpay TEST payment, webhook and refund delivery; production infrastructure/configuration validation. These remain deferred or blocked and must never be reported as PASS without their own evidence.

## Prepared next task — do not start

**Canonical Task ID:** 2 — Theme and Design
**Status:** `NOT STARTED` for the next governed execution, notwithstanding retained historical implementation evidence.
**Dependency:** explicit owner approval of Task 1 and a clean, verified `origin/work` checkpoint.

**Objective:** verify and, only if authorized by the Task 2 work order, make minimal changes necessary to maintain the existing yellow/forest-green/pale-mint, mobile-friendly visual system, readable cards/text, spacing and component consistency.

**Included:** source/evidence inventory of theme tokens/styles; approved visual consistency/accessibility defects; focused web/UI regression evidence; task-specific documentation and GitHub checkpoint.

**Excluded:** Home/navigation product redesign; Restaurant Mode behavior change; backend/API/auth/database change; Android/iOS device testing; Razorpay provider testing; production deployment; dependency/framework upgrades unless separately authorized.

**Acceptance criteria:** preserve existing UI decisions; record every changed visual file and before/after rationale; run focused checks for affected screens; avoid unsupported device claims; no regressions to customer, seller, admin, delivery, Restaurant Mode or CHAND surfaces; checkpoint is committed and remote-verified.

**Security requirements:** no secrets or `.env` files in Git; no production services/data; review uploads/URLs only if a Task 2 change touches them; do not weaken client-side protections to satisfy a visual test.

**Expected deliverables:** Task 2 scope/evidence report, change log, focused test logs, updated five checkpoints, updated handover, and a verified `origin/work` commit. A ready-to-copy execution prompt is in `docs/TASK_2_PREPARATION_PROMPT.md`.

## Permanent GitHub checkpoint protocol

After each meaningful work session: (1) update `COME_IN_LIVE_CHECKPOINT.md`; (2) update this master board/tracker; (3) update decisions, blockers and session log; (4) record completed/pending/deferred work; (5) record exact test evidence; (6) state the exact next resume point; (7) review every changed file; (8) exclude `.env`, credentials, keys, caches, dependencies and generated build output; (9) make a meaningful commit; (10) push to `origin/work` without force; (11) fetch `origin/work`; (12) verify local `HEAD == origin/work` with zero ahead/behind; and (13) verify a clean working tree. If any push fails, preserve the local checkpoint and report the failure and recovery command honestly.

## Reconciliation evidence and next action

This reconciliation performed no application test, source change, deployment, provider operation or Task 2 work. It fetched `origin/work` and verified local/remote equality at `0ecfbd08cc999d7106efbb0e28a6a9d3d56b114f` before documentation changes.

**Exact next action:** owner reviews the Task 1 checklist and explicitly approves or rejects Task 1. If approved, begin only the prepared canonical Task 2 scope after first fetching and verifying `origin/work`.
