# COME-IN Task 3 — Pending Work and Blockers

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
