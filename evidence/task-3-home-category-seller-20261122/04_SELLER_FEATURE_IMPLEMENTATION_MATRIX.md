# Report 4 — Seller Dashboard Feature Matrix

| Feature | Classification | Source/API evidence | Test/runtime boundary |
|---|---|---|---|
| Register one shop, pending approval | IMPLEMENTED & VERIFIED | `POST /shops`; customer→shopkeeper promotion; `ShopIn` validation | shop-registration contracts in Task 3 suite |
| Seller access/ownership | IMPLEMENTED & VERIFIED | `_assert_shop_owner`, role/owner checks | role/security contracts in Task 3 suite |
| Shop edit/profile/images/timings | IMPLEMENTED BUT NOT VERIFIED | `become-seller.tsx`, `PATCH /shops/{id}`, upload | no live seller UI run |
| Approval and online/offline availability | IMPLEMENTED & VERIFIED | admin status route; `PATCH /shops/{id}/availability` rejects unapproved shop | seller/admin contracts |
| Product CRUD, SKU/variants/measured units | IMPLEMENTED & VERIFIED | seller products UI; `POST /shops/{id}/products`, `PATCH/DELETE /products/{id}` | catalog/variant contracts |
| Order list/status progression | IMPLEMENTED & VERIFIED | seller orders UI; `GET /shops/{id}/orders`, `PATCH /orders/{id}/status` | seller workflow contracts |
| Inventory/stock and restock alert data | PARTIALLY IMPLEMENTED | product stock fields, `_fire_restock_alerts` | dashboard alert UX not verified |
| Master catalog linking | IMPLEMENTED & VERIFIED | `/catalog/master-products`, seller scoped link route | master-catalog seller contract |
| CSV import preview/apply | IMPLEMENTED & VERIFIED | seller product import UI/API; validation before writes | import contracts |
| Universal file import/review/apply | IMPLEMENTED & VERIFIED | staged import jobs and record review | source/contracts; optional adapters not live-verified |
| Earnings/settlements/bank data | IMPLEMENTED BUT NOT VERIFIED | `/earnings/mine`, bank-account, settlement routes | no real money movement |
| Notifications/support | PARTIALLY IMPLEMENTED | seller support routes; generic notifications | runtime delivery not tested |
| Ads/premium/performance dashboards | NOT IMPLEMENTED / NOT FOUND | no dedicated seller surfaces located | static inspection |
