# T9-12 owner decision packet

**Decision record — 23 November 2026.** The project owner explicitly approved the three decisions below in the T9-12 Owner Decisions Record Update. **Implementation status: NOT IMPLEMENTED.** Operational parameters listed below are still open.

## OWNER APPROVED — Configurable expiry duration

- Admin controls the default replacement-offer validity duration.
- An authorized Admin may adjust the duration for an individual offer.
- Each offer must have an explicit expiry timestamp and audit history.
- The customer should be informed of the expiry.

## OWNER APPROVED — Independent cancellation permissions

- A customer may cancel their own eligible pending offer.
- A shopkeeper may withdraw their own pending offer. A shopkeeper must not silently change an accepted offer.
- An Admin may cancel an eligible offer with a documented reason and audit record.
- The system automatically expires pending offers when their configured expiry is reached.
- Cancellation or expiry of an offer leaves the whole order in place. Accepted offers and offers after dispatch starts require protected handling and a separately authorized process.

## OWNER APPROVED — Controlled migration

- New offers follow the new expiry policy from its effective activation.
- Existing unaccepted offers must be reviewed for controlled migration under Admin authority.
- Customer notice and a reasonable grace period must be considered where needed.
- Already accepted offers must not be silently changed or migrated.

## Owner clarification required

| Area | Parameters still open |
| --- | --- |
| Expiry configuration | Default duration and units, countdown start event, scope across Grocery and Restaurant, and treatment of reoffers. Clarify which Admin permissions qualify, what limits apply to individual adjustments, and when an adjustment can take effect. |
| Cancellation and protections | Exact eligible pending case and order states for each actor, dispatch milestone, treatment of accepted intent pending Assist, reason requirements for customer/shopkeeper actions, and separately authorized handling after acceptance or dispatch. Clarify what follow-up resolves an unavailable line when the order remains open. |
| Notices and audit | Customer notice method and timing for expiry, changed deadlines and migration. Clarify whether separate cancellation/expiry notices are required, and which audit details and reasons are required beyond the approved Admin reason, explicit expiry and audit history. |
| Activation and migration | Effective activation date/time, migration timing and eligibility, handling of in-flight or reissued offers, circumstances requiring notice or grace, grace-period duration and start event, notification method, and the Admin review procedure. |

No values or operational choices were assigned to these parameters. The earlier options below are preserved as historical evidence of the pre-approval packet.

---

## Historical packet — before owner approval

**Pending explicit owner approval.** All options are unselected. Decisions apply to post-order replacement offers. Define whether Grocery and Restaurant share the same rules or approve separate wording for each.

## Decision 1 — What determines validity?

Choose one.

| Option | Customer experience | Shop and delivery impact | Expiry, complexity and risk |
| --- | --- | --- | --- |
| 1A — Fixed elapsed duration | Predictable window and clear deadline. Late notification can leave less time to decide. | Shop can time follow-up. Delivery may wait while availability and fulfillment remain open. | Persist a server-calculated deadline at the approved start event. Lowest configuration complexity. One window may fit some fulfillment modes poorly. |
| 1B — Configurable duration | Window can fit the order context. Customers need the exact deadline before responding. | More flexibility and administration. Delivery teams need predictable permitted bounds. | Approve configuration scope, authority, limits, missing-value behavior and immutable case snapshot. Higher testing burden and inconsistent-duration risk. |
| 1C — Valid until a defined order state | Customer sees which fulfillment milestone ends the offer. No fixed countdown is implied. | Shop can close via fulfillment milestones, but current open-case progression guards can conflict with a stage-triggered cutoff. | Approve exact Grocery/Restaurant states and transition order. A stalled order may never expire unless an additional rule is separately approved. Race handling is required. |

Record chosen option, exact duration if applicable, units, start event, cutoff inclusivity, and eligible states. Specify whether a reoffer starts a new window, whether acceptance stops the expiry clock, and what expiry does to the order and any unresolved Assist case. Specify who is notified and how. No duration is supplied by this packet.

## Decision 2 — Who may independently cancel?

For each row, choose **deny** or **permit with explicitly selected guards**. The conditions below are options for approval, not existing powers. Specify whether `awaiting_customer`, `rejected`, or `assist_required` qualifies, and select eligible Grocery/Restaurant order states explicitly. Decide whether a recorded acceptance pending Assist is protected like an applied replacement.

| Actor | Optional timing and order states | Reason | Original order and finality | Required evidence if permitted |
| --- | --- | --- | --- | --- |
| Customer | Owning customer, pending response, while order is in selected pre-dispatch states. | Optional customer explanation or mandatory category. | Proposal-only closure can leave the order and original line intact and require a reoffer or Assist. An accepted/applied case or active delivery would require a separate approved support action. | Authenticated customer, order/case, decision timestamp, reason if required, previous and new case status. |
| Shop or Restaurant | Owning merchant, unaccepted case in selected editable states, for stale/missing alternative or another approved cause. | Choose required reason or controlled reason categories. | Proposal-only withdrawal, then reoffer or Assist. Define customer notice and preserve acceptance or fulfillment as protected unless separately approved. | Merchant ownership, unavailable/changed option evidence, actor/time, old/new status, notice. |
| Admin | Scoped Admin exception in expressly named order states. Decide whether acceptable only before dispatch. | Choose mandatory reason and case/evidence reference, or exclude exceptional override. | Preserve order and applied acceptance under a proposal-only rule. Changes after acceptance or delivery start need separately approved handling, financial checks and support authority. | Role and case ownership evidence, reason, approval context, old/new status, actor/time. |
| System | Only after an approved server cutoff, in selected states, while the offer is still actionable. Choose authoritative lazy check, scheduled processing, or both with one outcome. | System reason code and deadline evidence. | Close only the eligible proposal. Specify subsequent reoffer/Assist; ensure accepted replacements and in-flight fulfillment follow the explicit decision. | System actor, rule version, cutoff, transaction time, old/new status, stable idempotency key and notice result. |

Specify the order consequence separately for every allowed actor. Preserving the original order under proposal-only closure leaves the unavailable item unresolved until a supported decision is taken. Cancelling the whole order, unwinding an applied substitution, restoring stock or changing payments is a separate choice with separate financial consequences. No delivery-partner cancellation role is proposed by default.

## Decision 3 — Which offers fall under the new rule?

Choose one.

| Option | Customer and operational effect | Required rollout evidence |
| --- | --- | --- |
| 3A — New offers only | Already-issued offers stay under their original behavior. Shop/support may operate two rule versions temporarily. | Effective timestamp and version persisted for new cases. Define whether a refresh counts as new. |
| 3B — Existing unaccepted offers | More consistent handling, but active customers may lose time unless the owner chooses notice, grace or a fresh deadline. | Exact eligible states, treatment of recorded Assist consent, deadline basis and notices. Preserve applied and final outcomes. |
| 3C — All existing offers after controlled migration | Broadest coverage and highest risk of changing expectations or mislabeling accepted/historical cases. | Approve dry run, eligible-state mapping, grace and communication, idempotent backfill, rollback and protection for completed outcomes and financial records. Historical data stays read-only unless migration is explicitly authorized. |

- Decision 1 option, exact duration or state rule, start/cutoff and modes ____________________
- Decision 2 allow/deny by actor, permitted case/order states, reason, acceptance and delivery handling ____________________
- Decision 3 option, effective time, legacy coverage, notice and approval for any migration ____________________
- Owner name, signature, date and evidence reference ____________________

### 24 November 2026 — T9-12 replacement offer expiry

The owner subsequently approved a 15-minute Grocery and Restaurant default starting when an offer successfully becomes available to the customer, bounded Admin configuration and audited per-offer changes, and sequential re-offers on rejection or expiry with Assist fallback. No numerical min/max or independent cancellation eligibility, protected handling, migration notice, grace or timing were supplied by this decision. [Implementation record](../replacement-expiry-implementation-20261124/IMPLEMENTATION.md)


### 24 November 2026 — Four decisions approved

The owner approved Admin-adjustable offer expiry within 5–30 minutes and a 15-minute default, with individual edits anchored to original offer creation. The customer may withdraw independently or explicitly confirm unavailable-item removal before preparation. Acceptance is locked and packing, preparation and dispatch restrict automation. Admin may enroll eligible legacy cases in a 24-hour notice and grace campaign. After revalidation, successful migration starts a fresh 15-minute expiry. This latest approval supersedes earlier unresolved values for this scope. Live migration remains an Admin rollout action. [Implementation and recovery](../replacement-lifecycle-20261124/IMPLEMENTATION.md)
