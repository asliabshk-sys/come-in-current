# Task 3 — Seller Feature Status

| Feature | Status | Verification boundary |
|---|---|---|
| Registration, shop profile, approval and availability | VERIFIED COMPLETE | Existing routes/contracts; live seller interaction not run. |
| Products, SKU, variants, pricing and stock | VERIFIED COMPLETE | Existing UI/API and 91-test union source-contract coverage. |
| Grocery seller order list and valid status changes | VERIFIED COMPLETE | Existing ownership/transition guards and contracts. Restaurant workflow remains separate. |
| CSV/XLSX/ZIP staged catalogue import and review | VERIFIED COMPLETE at source/contract level | Optional OCR/PDF/CHAND adapters not represented as live PASS. |
| Overview metrics and quick links | VERIFIED COMPLETE | Recovered overview uses authorized existing read APIs; 44 focused tests and web export pass. |
| Earnings, settlement summaries and masked bank data | VERIFIED COMPLETE at source level | Read-only authorized API. No money movement or provider check. |
| Seller support and Help | VERIFIED COMPLETE at source level | Owner-scoped support API and bounded Help screen. |
| Notifications | PARTIALLY IMPLEMENTED | Existing generic notifications/support sources; real delivery not tested. |
| Low-stock dashboard UX/history/export analytics | PARTIALLY IMPLEMENTED | Data fields/restock alerts exist; no new dashboard/report policy invented. |
| Advertising, premium membership, staff/branches, review moderation | OUT OF APPROVED SCOPE | Requires owner policy, commercial rules and dedicated acceptance criteria. |

This table does not turn source-level verification into live seller, device, provider, or production acceptance.
