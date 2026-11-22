# Report 5 — Seller Backend, API and Database Audit

## API / authorization evidence

- Shop lifecycle: `POST /shops`, `GET /shops/mine`, `PATCH /shops/{shop_id}`, `PATCH /shops/{shop_id}/availability`, public `GET /shops` (`backend/server.py` ~1330–1422).
- Product/catalog lifecycle: `GET /shops/{shop_id}/products`, `GET /catalog/products`, `POST /shops/{shop_id}/products`, `PATCH/DELETE /products/{product_id}` (~2990–3120).
- Orders: `GET /shops/{shop_id}/orders`, `PATCH /orders/{order_id}/status` (~3652–3705).
- Financial: `GET /earnings/mine`, shop bank-account routes and settlement routes (~4344–4586).
- Support: `GET/PATCH /seller/support` (~5673–5695).

`_assert_shop_owner` enforces shopkeeper role plus owner ID (admins permitted where intended). Product update/delete repeat role/ownership checks. `ShopIn`, `ProductIn`, variants and measured units use Pydantic bounds/validators. Order transition rules reject invalid state changes.

## Data/index evidence

Relevant collections: `shops`, `products`, `orders`, `catalogue_import_jobs`, `catalogue_import_audit`, `restock_alerts`, `financial_ledger`, `financial_audit`, `payout_bank_accounts`, `settlement_requests`, `seller_support`.

Indexes include shop owner/status, product shop/owner/SKU, order customer/shop/idempotency, import audit identity and financial settlement/idempotency indexes (`server.py` ~6040 onward). Database runtime was not modified or queried in Task 3.

## Boundary

This is source/test evidence, not a production API/database audit. Real settlement, backup/restore, provider and production access remain outside Task 3.
