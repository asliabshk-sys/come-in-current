# T9-12 replacement lifecycle

## Scope and baseline

GitHub and local `work` matched `e42124c92ca6a77e5fbc11f2b0ebb600acbb165a` before changes. The retained application source extends the existing expiry and sequential-offer implementation. Apply `patches/task9-replacement-lifecycle.patch` immediately after `patches/task9-replacement-expiry-sequence.patch`.

## Approved decisions and runtime behavior

1. **Expiry policy.** New offers default to 15 minutes after transactional in-app availability. Admin can narrow the configured bounds and change the default within 5–30 minutes. Individual changes are bounded by those settings and anchored to the original offer creation time. Admin must supply the current option and expiry, plus a reason. The audit event and customer notice commit with the adjustment. A closed, expired or fulfillment-locked offer cannot be reactivated.
2. **Independent withdrawal and removal.** An authenticated order owner can decline to see the next eligible option, withdraw to stop offers, or preview removal. The preview shows the original item and status, server-computed total and potential refund where an authoritative amount can be calculated. The confirmation is bound to the order, decision, active deadline, items, financial snapshot and quote. The server recomputes it before applying anything. Existing clients retain their explicit removal paths under the earlier order and quote guards. Eligible unpaid removals use existing calculators and leave the other items in place. Discounts, historical taxes, collected payments, invalid remaining carts and other protected cases retain their original financial state and go to the existing Assist review workflow. Refund review remains pending execution. No replacement-specific fee is added.
3. **Fulfillment and support.** Both modes use the existing `preparing` status for the onset of Grocery packing or Restaurant preparation. The transition closes automated alternatives and creates or links an Assist ticket atomically. A recorded acceptance stays locked, including acceptance pending financial review. Before preparation, the customer can request changes through the existing order-linked Assist ticket. Restaurant staff retain the existing ownership-scoped Support workflow. To clear a readiness hold after a protected case, authorized Admin must first resolve the linked ticket and explicitly confirm that the order can be fulfilled as recorded. This closes only the replacement case. Any change to items or charges requires the appropriate separate review. Normal order transitions, tracking, complaint and refund routes remain available. Dispatch closes replacement mutations and does not mark delivery complete.
4. **Legacy migration.** Authorized Admin enrolls a selected case by order mode, order ID and case ID. Campaign `t9-12-legacy-v1` records affected case IDs and events. The service checks pending status, no prior decision, pre-preparation stage, original line and total, existing expiry if present, and current alternatives. Excluded records and reasons are visible to Admin. Successful grace notice starts a 24-hour period with legacy behavior intact. The existing worker rechecks eligible cases after grace and atomically writes the active option, notice and audit. The first migrated offer lasts exactly 15 minutes from activation. Original report timestamps and option records are preserved. Closed, changed or ambiguous cases stay out of the timed flow. Failed activation schedules a bounded-rate retry and appears in Admin status, with each failure retained in audit. Duplicate enrollment and worker replay do not duplicate notices.

## Admin and API

The existing Admin Support tab contains the settings, active offer lookup and adjustment, protected-case closure, legacy enrollment and migration report. Migration reporting includes historical eligible enrollments, current grace, successful migration and exclusion counts, current failed cases, reasons and recent audit events.

| Method | Route under `/api` | Access |
| --- | --- | --- |
| GET, PUT | `/admin/replacements/expiry-settings` | Admin |
| GET, PATCH | `/admin/replacements/{kind}/{order_id}/{case_id}/expiry` | Admin |
| POST | `/admin/replacements/{kind}/{order_id}/{case_id}/manual-resolution` | Admin |
| POST | `/admin/replacements/migration/{kind}/{order_id}/{case_id}` | Admin |
| GET | `/admin/replacements/migration` | Admin |
| GET | Existing Grocery or Restaurant replacement case path plus `/removal-preview` | Order owner |
| POST | Existing Grocery or Restaurant replacement case path plus `/decision` | Order owner |

## Database and recovery

Optional fields on existing replacement case records store migration progress and fulfillment locks. Two sparse indexes, one per order collection, support the migration worker. Existing transaction, order, notification, financial audit and support storage are reused. No live records were enrolled or migrated during verification.

Stop migration enrollment if a rollout is paused. Disable the migration worker through a code rollback before reverting an application deployment, and retain the stored schedule and audit records. Existing grace notices and pending activation must be reconciled before resuming. Already activated offers should remain on the timed policy until they resolve. Reverting to a legacy binary while they remain open could remove the new lifecycle safeguards. No automated cleanup deletes history, notifications, financial records or customer decisions.

See [verification](TESTS.md).
