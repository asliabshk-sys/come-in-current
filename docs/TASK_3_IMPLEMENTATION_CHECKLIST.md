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

## Explicitly deferred or policy-gated

- Real provider-backed AI, OCR, push, bank verification, payment/refund or settlement transfers.
- Advertisement campaign rules, membership commerce/₹299 activation, multi-branch/staff roles, review moderation, and new commercial policies: require dedicated owner decisions before data/API implementation.
- Android/iOS device validation and final visual/device testing.
