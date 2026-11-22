# Task 3 Increment 01 — Security Findings

## Findings

| ID | Severity | Finding | Evidence | Disposition |
|---|---|---|---|---|
| INC01-REV-01 | LOW | A stock-positive count was labelled “Active products.” | `frontend/app/seller/dashboard.tsx` source review. | Corrected to “Products with stock”; regression checks passed. |

## Verified controls at source level

- The Overview requires a frontend `shopkeeper` role guard, but the security boundary remains backend authorization.
- `GET /shops/{shop_id}/orders` calls `_assert_shop_owner`.
- `GET /earnings/mine` accepts only shop/restaurant IDs owned by the authenticated user and returns 403 for another tenant.
- `GET /seller/support` derives permitted tickets from the authenticated owner’s Grocery/Restaurant orders.
- Overview has no mutation request. Help has no provider request and routes only to existing seller surfaces.
- Help text tells sellers not to provide passwords, OTPs, API keys, or complete bank numbers.

## Limitations

No live multi-user/tenant, authenticated Expo runtime, external-provider, bank, payment, push, OCR, or native-device security validation was performed. Therefore this review does not claim the entire Seller Dashboard or application is security-complete.
