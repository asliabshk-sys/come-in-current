# Report 6 — CHAND AI and Catalogue Import Audit

## Implemented workflow

`app/seller/products.tsx` supports master-catalog linking, CSV preview/apply and universal catalogue-import job creation, review, edit, approve/reject, bulk approve and guarded apply. `POST /shops/{shop_id}/catalogue-import/jobs` stages extracted records only; source explicitly states it does not publish products/inventory at preview time. Seller ownership is checked on jobs and records.

`catalogue_import_engine.py` supports CSV, XLS/XLSX, PDF, JPEG/PNG/WebP/TIFF/BMP and ZIP batches, with signature/metadata checks, per-file/batch bounds, duplicate content protection and review statuses. CSV/XLSX are source-parsed; PDF/image OCR has optional adapters and outputs unverified review material. ZIP handling validates members.

`catalogue_chand_adapter.py` provides optional structured CHAND interpretation; when unconfigured it returns `NOT_CONFIGURED`, not fabricated AI data. Failed interpretation retains source extraction for seller review.

## Classification

| Capability | Status |
|---|---|
| CSV/XLSX preview, validation and review-before-apply | IMPLEMENTED & VERIFIED |
| Transaction-aware guarded apply/audit/idempotency | IMPLEMENTED & VERIFIED (source/contracts) |
| PDF text extraction | IMPLEMENTED BUT NOT VERIFIED (optional adapter dependency) |
| OCR for images/scanned PDFs | PARTIALLY IMPLEMENTED / BLOCKED by optional OCR dependencies/runtime |
| ZIP batch import | IMPLEMENTED & VERIFIED (source/contracts) |
| CHAND structured interpretation | IMPLEMENTED BUT NOT VERIFIED; provider is optional/unconfigured |

Focused import/master-catalog/role-security tests were included in the 84 PASS Task 3 selection. No import was applied to live data.
