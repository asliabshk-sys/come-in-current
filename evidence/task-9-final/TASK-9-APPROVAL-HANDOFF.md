# Task 9 approval and integration handoff

| Area | Who must authorize or provide evidence | Exact decision or artifact | Technical step after authorization |
| --- | --- | --- | --- |
| Coupon T9-41–43 | Project owner and relevant funding merchant/advertiser | Signed funding parties and shares, posting/settlement rules, eligible channels and order modes, whether and when to restore budget on paid cancellation or refunds, accepted customer terms. | Bind the funding ledger to eligible Restaurant/online checkout, verified provider outcomes and idempotent restoration. |
| Ads and revenue T9-31 | Project owner and contracting advertiser, with finance verification | Accepted shortfall/excess remedy, threshold, price or credits, caps, rounding, eligibility and verified booking/payment evidence. | Calculate an approved adjustment, add independent approval and reconcile the advertiser/platform ledger. The current preview shows quantities and booking differences only. |
| Partner and seller settlement T9-29–30 | Project owner, delivery partner and impacted seller/restaurant | Authoritative order-to-assignment source, signed delivery fee allocation, replacement adjustments, settlement period and evidence standards. | Enable a partner payable ledger and statements, prevent duplicate payouts and reconcile verified disbursements. |
| Rewards T9-34–37 | Project owner and authorized finance/promotions administrators | Approved valuation, funding and compensation treatment for spent rewards, replacements, cancellations and qualifying-order refunds. Also specify customer notification and review authority for compensating entries. | Post idempotent compensating entries in a transaction, protect spent balances and preserve the credit. |
| Incremental collection T9-20 | Project owner and Razorpay integration owner in the separately authorized TEST phase | Verify provider acceptance of distinct operation receipts and notes, merchant-account scope, creation/retrieval and retry semantics, capture confirmation and webhook ownership. | Add a gated provider transport, persist the linked intent and idempotent verified event outcome, then validate price changes, timeout recovery and duplicate delivery against TEST. The wire adapter and local preview are implemented. |
| Partial refund T9-23 and full refund T9-25 | Project owner, accounting and provider integration owner | Continuing-order eligibility, prior refund allocation, exact eligible components, coupon/reward/seller/partner linkage, provider partial execution and confirmation in TEST. | Persist approved allocation and enforce cumulative balance with the verified provider lifecycle before any execution. |
| COD refund T9-24 | Project owner, accounting and authorized payout integration owner | Permitted payee and payment method, audited collection and delivery requirements, verified payout evidence, duplicate prevention/reversal and reconciliation procedure. | Connect the pending request to a verified payout and immutable settlement reference. |
| Historical tax and invoice T9-46, T9-48 | Assigned verified CA/tax professional, separate Admin and authorized statutory issuer | Case-specific correction type, treatment and values, actual invoice issuer, sequencing scope and format, cancellation and reconciliation procedure. | Validate the actual correction document and implement transactional statutory numbering and issuance under those rules. Internal IDs do not consume statutory numbers. |
| Offer expiry T9-12 | Project owner | Explicit duration and independent cancellation semantics. | Implement expiry and cancellation without changing concluded offers or financial history. |
| External validation T9-50 | Project owner and authorized test operator | Physical Android/iOS environment and separately authorized Razorpay TEST payment, webhook and refund setup. | Execute the authorized external validation phase and record genuine evidence. |

Broader reward policy, advertising compensation, third-party funding, statutory approval and authorized real or TEST financial execution remain pending. The requested local request and evidence checks are available with execution disabled.

## Proposed dispositions pending decision

| Policy IDs | Proposed decision pending approval | Financial, customer and compliance impact |
| --- | --- | --- |
| T9-41–43 | Retain currently approved funding and channels until all parties sign terms for any expansion. | Current benefits stay available within their existing limits. Broader redemption or paid restoration would create new funding and disclosure obligations. |
| T9-31 | Keep delivery variance review-only until the advertiser accepts a defined remedy. | No credit, liability or automatic compensation is recorded. |
| T9-29–30 | Require an authoritative assignment and signed allocation before any payable change. | Existing balances and the shop-sales commission rule remain in force. |
| T9-34–37 | Require approved valuation, notification and spent-credit treatment before posting compensating entries. | Customer balances and historic credits remain protected. |
| T9-20, T9-23–25, T9-50 | Keep execution disabled pending the approved rail and controlled provider TEST evidence. | Customers see review status. No money moves on review approval. |
| T9-46, T9-48 | Require case-specific CA guidance and issuer authorization before statutory numbering or issuance. | Internal drafts preserve original evidence and leave statutory sequences untouched. |
| T9-12 | Obtain explicit expiry duration and cancellation terms before changing offer availability. | No offer is closed or reopened under an invented duration. |

The current sign-off forms record authority, effective date and evidence. [Owner decisions](approval-readiness-20261123/OWNER-DECISIONS.md) · [External validation](approval-readiness-20261123/EXTERNAL-HANDOFF.md)

### Coupon funding and channels — 23 November 2026

T9-41–43 remain **PARTIALLY VERIFIED**. Existing COME-IN-funded Grocery cash controls passed fresh tests including release rollback, wrong-order release, paid-order denial and Admin reconciliation after restart. Commercial expansion awaits explicit approval. [Decision record](coupon-funding-20261123/OWNER-DECISION.md) · [Tests and commands](coupon-funding-20261123/TESTS.md)
