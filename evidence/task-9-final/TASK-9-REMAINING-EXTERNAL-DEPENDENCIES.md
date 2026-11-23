# Task 9 remaining dependencies

## Implemented with external validation pending

- **T9-25 — Full refunds.** Existing eligible cancelled-order and provider-backed refund controls passed local mocks. The separately authorized Razorpay TEST phase must verify original-method refund confirmation, provider webhook/reconciliation, and retry behavior using test credentials. The technical implementation is owner-approved. No actual refund was recorded as executed in this cycle.

## Eight blocked policies

| ID | Exact outstanding dependency | Locally verified fallback |
| --- | --- | --- |
| T9-20 | Authorized incremental payment intent and capture connected to the original order, provider capability and idempotency validation, and separate Razorpay TEST authorization. | Explicit consent, server amount revalidation and pending execution. |
| T9-23 | Continuing-order partial-refund eligibility and provider execution protocol, including interaction with prior refunds and seller/partner allocation. | Server quote, customer approval, Admin review and unchanged original payment. |
| T9-24 | Authorized COD refund rail, payee verification, execution proof and reconciliation procedure. | No payout on the basis of a cash status alone. |
| T9-30 | Approved delivery partner agreements, replacement fee/adjustment allocation, and reconciliation evidence. | Existing payout/earnings architecture preserved. |
| T9-34 | Approved earning rates, points valuation, eligibility, funding, expiry and completed-order calculation. | Disabled campaign configuration drafts and existing reward accounting. |
| T9-35 | Approved compensating credit/debit treatment for spent rewards, replacements, partial refunds and cancellations. | Admin review and immutable original ledger. |
| T9-48 | Actual case-specific verified CA guidance and authorized legal issuance/numbering/reconciliation procedure. | Assigned professional review, separate Admin decision, original invoice preservation. |
| T9-50 | Separately authorized native Android/iOS and genuine Razorpay TEST payment, webhook and refund validation phase. | Local Chromium, fixture transactions and restart checks. |

## Unimplemented rules and partially verified policies

- **T9-12:** The historical design proposed expiry and independent offer cancellation. It supplied no approved duration or cancellation terms. Current order and offer-state protections remain active.
- **T9-41–43:** Activation, checkout redemption, and atomic budget spending/exhaustion remain unimplemented. No approved active campaign with publication, funding, redemption, and failed/cancelled order release rules was identified. Draft limit validation and concurrent retry deduplication were exercised. Those do not spend funds or prove concurrency safety of redemption.
- **T9-26, T9-29, T9-31:** A complete replacement provider status lifecycle, replacement-related seller settlement adjustments, and unified approved sponsored/other revenue recognition remain open. Existing status, accounting, and membership paths remain in place. No commission or payout allocation was changed.
- **T9-36–37:** Existing referral attribution and order eligibility controls passed fresh transaction tests. Dedicated identity/fraud evidence and an approved adjustment or reversal procedure for already-awarded benefits remain open. Shared household attributes alone were not added as fraud signals. T9-38 is verified for the existing approved threshold, reward amount, idempotent credit, audit and customer notification.
- **T9-46:** Assigned review and approval safeguards passed on synthetic accounts. Historical corrected amounts must come from actual case-specific professional guidance. The software does not substitute current rates for historical tax treatment.

Individual policy wording and evidence are recorded in the [final register](TASK-9-FINAL-POLICY-MASTER-REGISTER.md). Existing owner approval does not substitute for genuine evidence or an absent business rule.
