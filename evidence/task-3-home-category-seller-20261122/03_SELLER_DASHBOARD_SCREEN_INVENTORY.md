# Report 3 — Seller Dashboard Screen Inventory

| Surface | Route / source | Classification | Evidence |
|---|---|---|---|
| Registration/shop setup/profile | `app/become-seller.tsx` | IMPLEMENTED BUT NOT VERIFIED | `POST/PATCH /shops`, image upload, shop fields, pending status. |
| Seller products/catalog | `app/seller/products.tsx` | IMPLEMENTED & VERIFIED | Product CRUD, master link, imports; related contracts pass. |
| Seller orders/availability | `app/seller/orders.tsx` | IMPLEMENTED & VERIFIED | `/shops/mine`, shop orders, availability, status API bindings. |
| Seller support | `app/seller/support.tsx` | IMPLEMENTED & VERIFIED | seller-scoped list/update bindings and Task 13/14 contracts. |
| Earnings/bank/settlements | `app/seller-earnings.tsx` | IMPLEMENTED BUT NOT VERIFIED | earnings, bank details, settlement request UI; no real settlement. |
| Dashboard overview | `become-seller.tsx` account-linked links | PARTIALLY IMPLEMENTED | No separate rich seller dashboard route found; seller functions are distributed across routes. |
| Metrics/low-stock alerts | products/orders/earnings sources | PARTIALLY IMPLEMENTED | Stock fields/restock infrastructure exists; dedicated seller low-stock dashboard was not found. |
| Shop images/timing/open status | `become-seller.tsx`, `/shops/{id}/availability` | IMPLEMENTED BUT NOT VERIFIED | Source/API present; no live seller session. |
| Advertisements/premium membership | inspected seller routes | NOT IMPLEMENTED / NOT FOUND | No dedicated seller UI/API found. |

Restaurant seller surfaces are intentionally separate and were not redesigned or combined with grocery seller routes.
