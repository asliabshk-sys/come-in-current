# Report 8 — Customer and Seller Journey Audit

| Journey step | Classification | Evidence / gap |
|---|---|---|
| Customer: open → Home → category/search | IMPLEMENTED & VERIFIED | Home/tab/category sources and Task 3 contracts. |
| Product → cart → checkout | IMPLEMENTED & VERIFIED | product/cart/checkout routes and shopping contracts. |
| Customer visual/device journey | NOT TESTED | no final-stage native/device or browser interaction pass in Task 3. |
| Seller registration → pending shop | IMPLEMENTED & VERIFIED | `POST /shops`, `ShopIn`, registration contracts. |
| Approval → seller products/orders | IMPLEMENTED & VERIFIED | status/availability/product/order source/contracts. |
| Seller catalogue import → review → apply | IMPLEMENTED & VERIFIED | staged workflow source/contracts. |
| Seller earnings/settlement completion | IMPLEMENTED BUT NOT VERIFIED | UI/API exists; no real settlement/provider exercise. |
| Restaurant separation | IMPLEMENTED BUT NOT VERIFIED | separate `/restaurant` routes/data; no runtime exercise. |

No destructive customer/seller operations were performed.
