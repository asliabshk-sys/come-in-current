# Invoice field checklist

| Field/evidence | Available in reviewed source | CA verification required |
| --- | --- | --- |
| Original document identity | Existing order invoice reference, if supplied | Original statutory document, actual issuer, document date, series and fiscal-period proof |
| Order linkage | Order kind and ID, customer link, replacement case and history | Map order and reference to the actual document and confirm recipient details |
| Values | Persisted subtotal, delivery, tax or tax amount, discounts, total and currency as present | Case-specific taxable components, rates and exemption/discount treatment |
| Historical tax | Optional order tax details; no backfilled or inferred mandatory values | Verify source tax breakup, applicable jurisdiction and classification |
| Correction draft | Internal ID, reason, source reference, approvals, timestamps and original values | Decide credit note, debit note, other treatment or no correction. Define statutory fields per outcome |
| Statutory supplier and recipient fields | Review payload is not a complete statutory invoice schema | Confirm legal identity, registrations, place of supply, applicable product/service codes and required recipient fields against genuine records |
| Numbering/issuance | No Task 9 statutory sequence exists | Authorized issuer, uniqueness scope, numbering, effective date, submission/reporting and cancellation rules |
