# COME-IN Task 3 — Seller Dashboard Implementation Checklist

**Authorized:** 22 November 2026 (Asia/Kolkata)
**Starting Git commit:** `87c6c3631e4660cec32aff622dd5870d49d9eee4`
**Source root:** `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`
**Status:** IN PROGRESS — owner-authorized implementation; final owner review still required.

## Confirmed reuse targets

- Existing seller registration/profile: `frontend/app/become-seller.tsx` and `/api/shops*`.
- Existing product, stock, import and order surfaces: `frontend/app/seller/{products,orders,support}.tsx` and `/api/shops/*`.
- Existing financial/settlement data: `frontend/app/seller-earnings.tsx` and `/api/earnings/mine`.
- Existing customer CHAND remains separate. Seller help must be bounded to seller operations and cannot expose credentials, bank details, other tenants, or execute irreversible actions.

## First implementation increment

- [x] Recover Task 3 audit and inspect current seller source/API/data evidence.
- [x] Add an authenticated seller overview that uses existing authorized data only; no fabricated metrics.
- [x] Add bounded Help Center/human-support entry points without requiring an unconfigured AI provider.
- [x] Add focused source/contract tests and regression checks (44 PASS; TypeScript/targeted ESLint/web export PASS).
- [x] Record the Increment 01 source patch and evidence; commit/push/remote verification follows this checkpoint.
- [x] Complete independent Increment 01 review, focused regression, security/gap audit and direct-label correction; evidence commit `e2c7e87` was merged with concurrent remote Task 3 documentation and remote verification passed at `8a30193`.
- [x] Restore verified archive into an isolated directory, apply/reverse-check the Increment 01 patch, and verify recovered Seller Dashboard sources.
- [x] Run final seller contract union (91 PASS), TypeScript (0 errors), targeted ESLint (0 errors/warnings), Expo web export (1,632 modules), authorization-source review and archive integrity checks.
- [x] Prepare the final Task 3 completion and owner-approval package at `evidence/task-3-seller-implementation-20261122/final-completion-20261122/`.

## Explicitly deferred or policy-gated

- Real provider-backed AI, OCR, push, bank verification, payment/refund or settlement transfers.
- Advertisement campaign rules, membership commerce/₹299 activation, multi-branch/staff roles, review moderation, and new commercial policies: require dedicated owner decisions before data/API implementation.
- Android/iOS device validation and final visual/device testing.
- Archive-restoration completeness: sanitized archive intentionally omits dependency directories and `.env*` templates. The isolated recovery required an existing public `frontend/.env.example` template; this is disclosed in the final backup report and does not justify a Seller Dashboard source change.

## Completion state

The currently approved local Task 3 Seller Dashboard scope is **REVIEW PENDING** for owner decision. Do not start Task 4. Advertisement, membership commerce, staff/branch roles, reviews/moderation and policy-driven analytics are not silently included: they require separate owner policy/acceptance authorization.
