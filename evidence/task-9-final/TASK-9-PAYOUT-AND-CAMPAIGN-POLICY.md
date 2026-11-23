# Task 9 payout and campaign policy

GitHub Work baseline `cbb48eecf4c6349eefde09cd4cc52df5c3028bfb`. This increment uses the owner-approved weekly starting structure, zero merchant sales commission and fixed-duration campaign recommendation. It preserves the approved delivery split and reward/referral/membership amounts.

| Workstream | Implemented and owner-approved at the code level | Pending |
| --- | --- | --- |
| Seller payouts | Versioned Admin cycle anchor, days, UTC processing weekday, reconciliation days, eligible fulfilment states and optional minimum. The schedule gates existing settlement requests using recorded finalized ledger entries and stores the schedule version, cutoff and payable by order. Merchant-owned CSV statements and single-use manual payout references. New nonzero merchant sales commissions are rejected. | Separate dispute holds beyond existing order eligibility, original evidenced deductions, settlement automation and independently verified transfer confirmation. Legacy amounts are not reconstructed. |
| Delivery Partner | Existing fee and earning rules preserved. | Separate partner settlement automation, COD reconciliation, incentive evidence and signed policy for adjustments. No new split or arbitrary penalty. |
| Advertisement terms | Admin stores the pricing model, funding reference, objective, area, categories and caps. Seller sees period and price and accepts the version. Existing poster, CHAND and designated-owner publication approval are preserved. Configured campaigns must have accepted fixed-duration terms before publication. | Validated CPM/CPC metering and billing, enforced geographic/product targeting, campaign resumption, delivery reconciliation, and attributed performance beyond existing event telemetry. |
| Fixed campaign budget | One atomic reservation within daily and total cap, manually evidenced booking, release, concurrent replay protection, unique evidence reference and private funding data. Public tracking does not generate spend. | Independent evidence verification and recognition rules, automated billing/refunds, and under-delivery compensation or credit authorization. |
| Coupons | Drafts can specify fixed or percentage discounts and explicit funding allocation by seller, COME-IN and advertiser. Server validates bounds and shares. Existing draft identifiers and disabled redemption are preserved. | Approved active published terms, checkout reservation/spend/release, funding ledger and settlement integration. |
| COME-IN revenue | Existing separate platform earnings and membership records preserved. Merchant product sales remain separate. | Consolidated ad/reward revenue recognition and provider-charge reconciliation. |
| Membership, rewards and replacement payments | Existing functionality, approved amounts and safeguards preserved. | Approved compensating reward entries, linked incremental capture, partial/COD refund execution and genuine provider validation. |

The new code reuses existing policy, ledger, settlement, advertisement and audit collections with built-in document uniqueness. No index or migration was added. Existing historic settlement rows stay intact. The payout and campaign actions implement local scheduling and accounting controls. They do not initiate provider transfers, debit advertisers or issue statutory documents.

## Public reference approach

The owner-supplied references were used as design pointers for documented terms, finite campaigns and transparent accounting. The environment's HTTPS proxy denied direct access to the supplied pages during this run. Exact competitor rates, private workflows and any legal conclusions were excluded.

[Zomato sponsored listings](https://www.zomato.com/policies/ads/growth-pack-policy/) · [Zomato title partner terms](https://www.zomato.com/policies/ads/title-partner-policy/) · [Zomato ordering](https://www.zomato.com/policies/online-ordering/) · [Blinkit seller fees](https://seller.blinkit.com/fees-commission) · [Blinkit Brand Central](https://brands.blinkit.com/dashboard/) · [Blinkit terms](https://blinkit.com/terms)

## Follow-up

See the [completion report](TASK-9-FINAL-COMPLETION-REPORT.md) for bounded Grocery cash redemption, commercial advertisement targeting and measured delivery. The first increment above records its historical scope.
