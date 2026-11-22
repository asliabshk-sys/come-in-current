# COME-IN Task 3 — Pending Work and Blockers

**Current status (23 November 2026 IST): Task 3 is APPROVED and CLOSED.** See the [owner approval and final completion record](../../TASK_3_OWNER_APPROVAL_RECORD_20261123.md). The entries below are historical. Live seller runtime, native Android/iOS, external provider and production-only validation remain deferred. Task 4 requires separate authorization.

1. **Source authority:** verify whether November 22 sanitized archive is later than and compatible with November 15 source and Increment 01. GitHub `work` has no standalone `frontend/` or `backend/` tree. Do not overwrite current source.
2. **Patch reconciliation:** compare/apply `patches/task3-seller-dashboard-overview.patch` only in isolated disposable source, verify no duplicate or regression. Missing in historical ZIP: seller dashboard/help routes and dashboard contract test.
3. **Seller Dashboard:** verify role guard, shop ownership, order counts, real earnings and settlement semantics, inventory calculations, refresh race/stale values, error/empty/loading states, mobile/responsive layout.
4. **Seller Help:** verify navigation, seller-scoped support permissions, categories, errors/empty states, no duplicate support system.
5. **Backend/security:** inspect ownership, cross-shop isolation, auth, financial consistency, validation and sensitive logging. Fix only confirmed Task 3 issues.
6. **QA:** run full relevant backend tests with project-required plugins, dashboard contract tests, TypeScript, targeted ESLint, Expo export, regression, and inspect changes. Record exact commands/results; do not claim device verification.
7. **Owner approval:** independent final review and owner acceptance remain pending. Task 4 locked.

Blocked/deferred: standard pytest config requires unavailable `pytest-xdist`; isolated frontend has no `node_modules`; Android/iOS physical devices and live Razorpay TEST are separately deferred. No fake data, production credential/payment changes or new unrelated features.

## Added blocker — November 22 sanitized source inaccessible
GitHub blob `b1e1d2c813185967dde4c979509410a95abd4d30` identified, but binary contents unavailable through connector; Git blob endpoint UTF-8-only; local Git HTTPS DNS blocked. Do not infer completeness, duplicate patch state, latest source authority, or compatibility. Require exact archive bytes before Task 3 implementation continues. No new source conflicts independently confirmed in this session.

## Binary retrieval blockers and safe alternatives
- Direct raw HTTPS and repository archive download: container DNS blocked.
- Connector contents/blob API: UTF-8-only; `fetch_blob` UnicodeDecodeError.
- No November 22 ZIP bytes, therefore no SHA-256, CRC, manifest or patch inclusion verdict.
- Safe next method: authorized network-enabled Git/Codex workspace fetches exact Git object `b1e1d2c813185967dde4c979509410a95abd4d30` to isolated directory. If needed, obtain owner authorization to create a temporary GitHub Actions artifact workflow; do not change workflows without approval.
- After retrieval, compare SHA-256, ZIP CRC, file-level hashes and `patch -p1 --dry-run`/reverse dry-run against isolated copies. Keep Task 3 owner approval pending.

## Workspace blocker update
Current container Git 2.47.3 exists, but github.com/raw.githubusercontent.com/api.github.com DNS unavailable; cannot clone/fetch. GitHub connector cannot deliver November 22 ZIP binary. No local ZIP. Authentication for terminal GitHub and write permissions from terminal are **NOT VERIFIED**; connector documentation writes are authorized and separately verifiable. Do not claim a network-enabled Codex workspace has been identified/tested. Required: network-enabled authorized workspace with actual `git ls-remote`/clone success, or supported binary-capable GitHub Actions artifact route after owner approval. Then inspect ZIP and Increment 01 patch safely.
