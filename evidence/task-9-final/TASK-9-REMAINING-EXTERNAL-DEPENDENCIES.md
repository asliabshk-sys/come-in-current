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
- **T9-41–43:** Fully COME-IN-funded Grocery cash campaigns support activation, checkout redemption, atomic budget spending, eligible unpaid cancellation release, and Admin reconciliation. Other funding splits and checkout flows remain pending approved posting, reversal, and paid-refund rules.
- **T9-26, T9-29, T9-31:** A complete replacement provider status lifecycle, replacement-related seller settlement adjustments, and unified approved sponsored/other revenue recognition remain open. Existing status, accounting, and membership paths remain in place. No commission or payout allocation was changed.
- **T9-36–37:** Existing referral attribution and order eligibility controls passed fresh transaction tests. Dedicated identity/fraud evidence and an approved adjustment or reversal procedure for already-awarded benefits remain open. Shared household attributes alone were not added as fraud signals. T9-38 is verified for the existing approved threshold, reward amount, idempotent credit, audit and customer notification.
- **T9-46:** Assigned review and approval safeguards passed on synthetic accounts. Historical corrected amounts must come from actual case-specific professional guidance. The software does not substitute current rates for historical tax treatment.

Individual policy wording and evidence are recorded in the [final register](TASK-9-FINAL-POLICY-MASTER-REGISTER.md). Existing owner approval does not substitute for genuine evidence or an absent business rule.

## Business policy addendum (historical pre-activation milestone)

Seller payout scheduling and fixed-duration commercial accounting have a local implementation. Automatic transfers and COD reconciliation still need independently verified bank or provider integration and approved delivery partner allocation. CPM/CPC billing, delivery shortfall compensation, and full revenue consolidation need verified metering, accepted delivery and compensation terms, and approved recognition rules. Promotion drafts now support explicit discount and funding splits. Active coupon checkout, consumption and release still require a bound campaign and funding/settlement workflow. See the [payout and campaign policy](TASK-9-PAYOUT-AND-CAMPAIGN-POLICY.md).

## Grocery cash coupon closure

Grocery cash activation, quote, transaction spend and unpaid cancellation release for fully COME-IN-funded campaigns are now working. T9-41–43 remain partial because seller and advertiser funding, mixed splits, Restaurant checkout, online checkout and paid refund adjustments remain unsupported. Broader funding requires a posting and reconciliation procedure, with independently verifiable provider outcomes for online usage. Ad delivery reports expose measured events. Contracted quantities and accepted shortfall/over-delivery terms are still required for financial remediation. Delivery partner allocation, reward/referral reversals, incremental provider execution, partial/COD disbursement, seller replacement adjustments and CA-approved invoice correction retain their recorded dependencies.

## Local campaign lifecycle milestone

Accepted impression targets are now reportable. The financial treatment of measured shortfall or excess still requires accepted remediation terms and independently authorized execution. Geographic verification and new placements remain outside this increment.

## Local financial review safeguards

The internal correction draft leaves tax values and the original invoice untouched. The final correction content and numbering require case-specific CA guidance and an authorized issuance procedure. Reward release now fails safely once a qualifying order is refunded. An approved reversal and compensating-entry policy is needed to change the customer balance. Existing captured payment and seller/platform ledger evidence appears together in Admin review. It does not authorize incremental payments, partial or COD disbursement, replacement settlement allocation or partner reconciliation.

### Review consistency follow-up

Recorded capture and refund checks are local approval safeguards. They do not replace the missing T9-20 linked execution protocol, T9-23 partial-refund policy or T9-24 COD verification rail. The internal draft validates the original order snapshot and does not supply the professional guidance, numbering or issuance procedures for T9-48. [Implementation and remaining work](review-consistency-20261123/IMPLEMENTATION.md)

### Seven-area reconciliation campaign

Coupon funding comparisons, ad shortfall review, recorded delivery fees and reward evidence, execution-disabled payment/refund contracts, and invoice readiness are locally available. Policy decisions and external integration required for real execution remain listed above and in the [seven-area report](reconciliation-controls-20261123/IMPLEMENTATION.md).

### Closure evidence gates

The replacement collection adapter now implements the network-free Razorpay wire contract, validated with fixture records, signatures and restart persistence. Genuine transports and verified payment, refund or payout execution are still blocked. Closure adds more evidence for reviewing the remaining financial decisions without posting changes. [Required decisions, authorizers and next integration steps](closure-evidence-20261123/APPROVAL-HANDOFF.md)

The final campaign strengthens quote-to-contract binding but leaves approved funding scope, unapproved compensation and payout rules, case-specific legal approval and genuine external validation unchanged. [Consolidated approvals, impacts and evidence required](TASK-9-APPROVAL-HANDOFF.md)

### Coupon funding and channels — 23 November 2026

T9-41–43 remain **PARTIALLY VERIFIED**. Existing COME-IN-funded Grocery cash controls passed fresh tests including release rollback, wrong-order release, paid-order denial and Admin reconciliation after restart. Commercial expansion awaits explicit approval. [Decision record](coupon-funding-20261123/OWNER-DECISION.md) · [Tests and commands](coupon-funding-20261123/TESTS.md)

### Advertisement compensation — 23 November 2026

Advertisement compensation remains **PARTIALLY VERIFIED**. Campaign status and audit writes are atomic, identical status replays are deduplicated, and inactive campaigns cannot record events. Compensation eligibility and execution remain disabled pending explicit approval. [Audit](advertisement-compensation-20261123/AUDIT.md) · [Owner decisions](advertisement-compensation-20261123/OWNER-DECISION.md) · [Tests](advertisement-compensation-20261123/TESTS.md)
