# Report 1 — Home Screen and Navigation Audit

**Evidence level:** SOURCE VERIFIED plus focused source-contract tests; not a device-runtime claim.

## Customer Home

`frontend/app/(tabs)/index.tsx` implements a branded header, voice-to-CHAND, language, notifications/account actions, search/filter entry, grocery hero, referral banner, separate Online/Offline/Restaurant/Home Services discovery cards, category grid, location selector, CHAND entry, quick products, popular products and Home Services section.

`useCatalogProducts.ts` calls `GET /catalog/products`; Home deliberately falls back to separate demo preview products when live catalog data is unavailable. This is **IMPLEMENTED BUT NOT VERIFIED** in a live customer session.

## Bottom navigation and routes

`frontend/app/(tabs)/_layout.tsx` defines Home, Categories, Search, Cart and Account, including cart count badges. The 53-route static inventory produced in Task 2 reported zero parse diagnostics. Home routes categories to `/category/[slug]`, products through `ProductCard`, search to `/(tabs)/search`, Cart through tabs and checkout through `checkout.tsx`.

Restaurant discovery goes to `/restaurant`; it does not reuse the grocery tab flow. Restaurant routing is **IMPLEMENTED BUT NOT VERIFIED** at runtime; no Restaurant Mode code was changed.

## Findings

| Item | Classification | Evidence / limitation |
|---|---|---|
| Header, search, category, account, CHAND actions | IMPLEMENTED & VERIFIED | Source bindings; `test_frontend_contracts.py` in 84-pass Task 3 selection. |
| Five bottom tabs/cart badge | IMPLEMENTED & VERIFIED | `_layout.tsx`; static route inventory. |
| Product/category/cart/checkout route wiring | IMPLEMENTED & VERIFIED | Route source plus shopping/catalog contract selection. |
| Deep-link/device back behavior | IMPLEMENTED BUT NOT VERIFIED | Expo Router source exists; no native/device session run. |
| Loading/empty/error presentation | PARTIALLY IMPLEMENTED | `useCatalogProducts` has loading/error/fallback; static inventory shows state markers, but full manual route coverage was not run. |
| Responsive overflow/text clipping | NOT TESTED | Requires viewport/device visual exercise. |

## Audit-only observation

Home renders five promotional dots with one static hero in inspected source. This may be a presentational expectation mismatch, but is not confirmed as a functional defect without product/runtime evidence. No change was made.
