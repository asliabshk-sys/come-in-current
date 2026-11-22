# Task 3 Seller Dashboard — Increment 01

## Delivered

This increment extends the existing Seller Dashboard; it does not create a second seller backend, database model, or order workflow.

- Added `frontend/app/seller/dashboard.tsx`: an authenticated Shopkeeper-only overview that composes existing `GET /shops/mine`, `GET /earnings/mine?shop_id=...`, `GET /shops/{shop_id}/orders`, and `GET /seller/support` responses.
- The overview displays only calculated authorized data: sales, pending/in-progress/completed/cancelled orders, currently active/low/out-of-stock products, pending settlement records, and unresolved seller tickets. It explicitly states that no figure is a demo value and no financial or inventory action occurs from the screen.
- Added links to existing Orders, Products & stock/catalogue imports, Earnings, Support, Shop Profile, and the new Seller Help screen.
- Added `frontend/app/seller/help.tsx`: a bounded seller-operation Help Center with guides that route to existing functionality and a human-support route. It explicitly does not impersonate CHAND or claim an AI provider is configured; it cannot execute refunds, bank changes, ads, or other irreversible actions.
- Added overview/help entry points to existing Account and seller-profile surfaces.
- Added static contract coverage in `backend/tests/test_task3_seller_dashboard_contract.py`.

## Changed retained-source files

| Path | Change |
|---|---|
| `frontend/app/seller/dashboard.tsx` | New seller overview route. |
| `frontend/app/seller/help.tsx` | New bounded Help Center route. |
| `frontend/app/(tabs)/account.tsx` | Adds seller overview/help links for shopkeepers. |
| `frontend/app/become-seller.tsx` | Adds seller overview/help links for an existing shop. |
| `backend/tests/test_task3_seller_dashboard_contract.py` | New focused static route/privacy contracts. |

Reviewable source patch: `patches/task3-seller-dashboard-overview.patch` (SHA-256 `d02c50b2cd559f8a77049b8ec31f90194c827c193cb815931fb46d892b6816f9`). `patch -p1 -R --dry-run` passed against the retained modified source, proving the recorded patch reverses cleanly.

## Actual verification

| Command | Result | Boundary |
|---|---|---|
| Focused seller/frontend contract selection | PASS — 44 passed, 0 failed, 3.51s | Static/source contracts, no database writes. |
| `expo export --platform web` | PASS — 1,632 modules bundled | Web bundle contains the new routes; no device session. |
| `tsc --noEmit` after Expo route generation | PASS — 0 errors | Static TypeScript. |
| Targeted ESLint for four changed frontend files | PASS — 0 errors/warnings | Targeted lint only. |
| `patch -p1 -R --dry-run` | PASS | Patch reversibility only; no source was reverted. |

`yarn` was unavailable on PATH, so the project's installed local binaries were used. The first typecheck was blocked by stale Expo typed-route output; a short offline Expo startup regenerated the ignored route declaration. The startup emitted a non-fatal React Native DevTools cache warning due a read-only home cache. It did not alter source; final TypeScript passed.

## Not completed in this increment

- Real seller Expo/device session, visual/responsive exercise, Android/iOS build, push delivery, OCR, configured AI-provider response, real settlement/bank verification, Razorpay/payment/refund and production checks.
- Advertisement, premium membership, multi-branch/staff permissions, review moderation, complaint policy, and commercial analytics/export rules require explicit policy/acceptance decisions before new data/API behavior is invented.
- Existing product/stock/order/import/earnings implementation remains the source of truth and was not duplicated or changed.

Task 3 remains **IN PROGRESS** and later must be **REVIEW PENDING** for owner review; Task 4 remains locked.
