# Task 3 — Security, Data Isolation and Backup Verification

## Source-level security verification

- `_assert_shop_owner` requires either admin or the `shopkeeper` role with matching `owner_id`.
- `GET /shops/{shop_id}/orders` resolves the shop then applies `_assert_shop_owner`.
- `PATCH /orders/{order_id}/status` requires the currently authorized owner and uses conditional status updates to reject stale/conflicting transitions.
- `GET /earnings/mine` restricts requested shop/restaurant IDs to the authenticated owner's set and rejects another tenant with 403.
- `GET/PATCH /seller/support` derives tickets from orders owned by the authenticated seller.
- The new overview is read-only. Help has no provider/action endpoint and explicitly warns against disclosing passwords, OTPs, API keys, or full bank numbers.

No new CRITICAL, HIGH, MEDIUM, or LOW Seller Dashboard security defect was confirmed in this completion run. The earlier LOW metric-label issue remains corrected in the review patch.

## Backup integrity

- Tracked archive: `archives/COME-IN-COMPLETE-MASTER-SOURCE-20261122-current-state-sanitized.zip`.
- SHA-256: `4cb8a397bee482b263e9b2f3ccf60d5818d20b42ecd60ef6c2bcc9fe6b041e33` — matched expected value.
- `unzip -t` passed; archive contains 752 members.
- The Task 3 patch applied and reverse dry-run passed against a separate restored directory.

## Backup limitation

The sanitization process excludes `.env.example` templates as well as secret `.env` files. `frontend/.env.example` was absent from the archive, so the first recovered-source frontend contract command failed before application execution. Its retained-source copy was hash-verified (`645046a9fe6badd1ee57345da0ad36fbe0b82009471dcf0a765e611f772f8d19`) and supplied only to the isolated restore; the rerun passed. This is a **backup-restoration completeness gap**, not a Seller Dashboard source defect. No archive or production source was altered in this session.

## Limits

No live multi-seller session, real database, native device, provider AI/OCR/push/payment/bank service, or production environment was used. Those boundaries remain deferred or blocked.
