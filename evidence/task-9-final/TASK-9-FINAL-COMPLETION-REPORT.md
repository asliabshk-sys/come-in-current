# Task 9 Final Completion Report

**Overall status — PARTIALLY VERIFIED.** All 50 policies are accounted for. The referral closure increment completed technical verification of the existing reward and notification rule. The previous removal, cart, and measured replacement evidence remains in force. Active coupons, campaign spending, and genuine financial or statutory execution remain outside the completed scope.

## Owner Approval Summary

The owner explicitly pre-authorized previously approved Task 9 implementation and verification in this execution turn. With successful technical evidence, **32 policies are technically owner-approved**. **31** are **OWNER APPROVED — IMPLEMENTED AND VERIFIED** and **1** is **OWNER APPROVED — EXTERNAL VALIDATION PENDING**. **9** remain partially verified, **1** is not implemented, and **8** are blocked by specific missing dependencies. No separate approval task was created for already authorized work.

| Status | Count |
| --- | ---: |
| VERIFIED | 31 |
| IMPLEMENTED — EXTERNAL VALIDATION PENDING | 1 |
| PARTIALLY VERIFIED | 9 |
| NOT IMPLEMENTED | 1 |
| BLOCKED | 8 |

## Completed changes

- Grocery and Restaurant paid offers now calculate the potential refund for a cheaper accepted replacement from the server-calculated total, including the applicable fee or tax. The customer sees the amount before accepting. Admin can approve a review only after matching consent and renewed price, order and payment-state validation. The original order and payment remain intact during review. The new path never creates a refund, charge or settlement record.
- The Grocery cart no longer shows unsupported measured-item replacements. A rapid repeated action cannot add the replacement twice, and an unrelated line stays intact. Separately, the post-order Grocery workflow was verified with a valid measured-size substitution, reduced stock and an incompatible unit.
- Existing full-refund controls were verified locally and are technically approved while genuine Razorpay validation remains deferred. The approved business rules, no-commission model, Grocery/Restaurant tax separation, Task 8, Task 21 and Master ZIP were preserved.

Changed extracted source covers `backend/server.py`, Grocery and Restaurant replacement tests, shared replacement UI, Admin/CHAND review UI, and the Grocery cart screen and cart store. The repo stores these changes in `patches/task9-final-authorized-scope.patch`, applied after the policy audit correction patch. No MongoDB migration, collection, index, provider rail, settlement formula, or legal issuance was introduced.

## Referral closure increment

Starting at `bc392cf69b658ae70d2ba69571828367022cfe74`, reward threshold evaluation was moved into the same MongoDB transaction as referral qualification. Concurrent approvals of distinct referrals for the same referrer serialize on the existing user record. Failure rolls back both qualification and reward work. The reward decision checks the referenced orders again and writes its notification with the ledger change. The customer can open Referral & Earn from the notification. Non-finite amounts cannot qualify. No thresholds, reward amounts, commissions, payout rules, indices, collections, or provider operations changed.

Apply `patches/task9-referral-closure.patch` after the final authorized scope patch. Referral fraud and previously awarded-benefit reversal remain partial. No automated reversal or household-based disqualification was added.

## Readouts

- [Final Policy Master Register](TASK-9-FINAL-POLICY-MASTER-REGISTER.md)
- [Test evidence](TASK-9-TEST-EVIDENCE.md)
- [Remaining dependencies and safe fallbacks](TASK-9-REMAINING-EXTERNAL-DEPENDENCIES.md)

The Mission baseline was GitHub work `1a87ca116836502741613ab3049f02f4bb2cb310`. The delivered increment is identified by this report's containing commit.

## Payout and campaign business policy increment

The owner-approved weekly payout configuration, cycle eligibility, merchant CSV, single-use manual payout reference, fixed-duration accepted campaign budget, and explicit coupon draft funding were implemented. The focused and browser paths verify this code. Sensitive terms are omitted from public advertising responses, and existing poster and owner approval gates still govern publication. Task 9 remains **PARTIALLY VERIFIED**. The 50-policy register retains 31 fully verified, one externally pending, six partial, four unimplemented and eight blocked.

Changed source covers `backend/server.py`, its new business policy integration test, Admin and Seller Earnings, Seller Advertisements and the API statement client. Apply `patches/task9-payout-campaign-policy.patch` after the referral closure patch. No approved payout split, rate, reward, referral or membership amount changed. No payment or refund was executed. [Business policy and evidence boundaries](TASK-9-PAYOUT-AND-CAMPAIGN-POLICY.md)

## Grocery coupons and advertisement delivery increment

At baseline `cc3d0368969167a45d20c135b9b9681c299b1e33`, promotions had no checkout path. Admin can now activate qualifying COME-IN-funded Grocery cash campaigns with explicit audience and unpaid cancellation terms. One coupon applies to the server quote and cannot stack with shopping rewards. The customer sees the discount, funder and terms. A quote does not reserve budget. A successful order reserves and spends the coupon budget atomically with stock and order insertion. Eligible unpaid cancellation releases the same receipt once. Failed transactions make no ledger/budget change. Active coupon terms are copied from the draft. The original order retains the benefit and any unsupported paid adjustment goes through existing review.

Commercial advertisement discovery and event intake now filter explicit area/category context and active moderated poster approval. Sellers can view measured event counts and timing. Attributed orders are explicitly unavailable. The request context is not independently verified geolocation and no new Home/Search ad placement or contractual compensation mechanism was enabled.

The three coupon rules T9-41–43 moved from unimplemented to partial because Grocery cash works and broader commerce does not. The resulting 50-policy totals are 31 verified, 1 implemented awaiting external validation, 9 partial, 1 unimplemented, 8 blocked. The existing 32 whole-policy owner approvals remain, and the newly verified bounded controls are owner-approved under the same authorization. Changes are in `backend/server.py`, Task 9 tests, checkout, Admin promotions and Seller Advertisements. Apply `patches/task9-coupon-checkout-and-ad-delivery.patch` after the payout campaign patch. No new collection, index or migration.

## Local campaign lifecycle milestone

Admin coupon campaign listing and audited pause, resume and terminal close now operate in the funded Grocery cash path. Advertisers can review and accept an optional fixed-duration impression target. Reports distinguish in-progress delivery, excess and ended shortfall. No compensation or new placement was enabled.

## Local financial review milestone

The existing referral ledger now rechecks qualifying orders when an approved reward is made available or processing begins. A newly refunded qualifying order blocks that transition without changing the original credit. Admin can create one immutable internal invoice correction draft after separate verified-professional and Admin approvals. It links the original invoice, order, replacement and approval records. It is marked pending statutory issuance. The Admin financial review also shows recorded payment status, locally recorded capture and existing seller/platform ledger entries for the same order. Partner allocations and external settlement stay pending.

The 50-policy classification is unchanged at **31 verified and owner-approved, 1 implemented awaiting external validation, 9 partial, 1 unimplemented, 8 blocked**. New bounded local controls are verified under the existing owner authorization. Cash disbursement, provider confirmation and statutory issuance were not executed. No migration, new index or collection was added. Apply `patches/task9-local-financial-reconciliation.patch` after the campaign lifecycle patch. [Milestone commands](local-policy-20261123/COMMANDS.md)

## Review consistency — 23 November 2026

Task 9 remains **PARTIALLY VERIFIED**. The follow-up adds coupon and advertiser replay safeguards, stored payment/refund consistency checks before replacement review approval, explicit reward rejection notice, and original financial snapshot validation before creating an invoice correction draft. Existing seller and partner rules stay in force. [Seven-area implementation and remaining work](review-consistency-20261123/IMPLEMENTATION.md)

## Seven-area reconciliation campaign — 23 November 2026

Task 9 remains **PARTIALLY VERIFIED**. Cash coupon reconciliation, closed advertisement delivery review, replacement accounting evidence, disabled payment/refund review contracts and invoice readiness checks extend existing flows. The exact scope and open approvals are recorded in the [implementation report](reconciliation-controls-20261123/IMPLEMENTATION.md).

Implementation checkpoint `dfc65425f7864076c2f161ac49e348109f199de2` was verified on GitHub `work`. Full backend rerun recorded 700 passes and one external object-storage skip. The final evidence also includes 75 expanded passes, seven Chromium scenarios and four restart checks. [Test evidence](TASK-9-TEST-EVIDENCE.md)

## Closure evidence gates — 23 November 2026

The closure increment implements receipt-level coupon checks, verified booking linkage, delivery and referral discrepancy evidence, a network-free incremental collection adapter and read-only preflight, COD cash audit linkage and invoice approval binding. Task 9 is **PARTIALLY VERIFIED**. [Implementation](closure-evidence-20261123/IMPLEMENTATION.md) · [Exact approval and integration handoff](closure-evidence-20261123/APPROVAL-HANDOFF.md)
