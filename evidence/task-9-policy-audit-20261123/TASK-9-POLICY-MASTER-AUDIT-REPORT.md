# Task 9 Policy Master Audit Report

**Overall status — PARTIALLY VERIFIED.** The current application was reconstructed in the retained source and tested with a local FastAPI runtime, synthetic accounts, isolated MongoDB replica-set databases and Chromium. No genuine payment, refund, payout or invoice issuance was attempted.

## Results

Recovered **50** policies. **27** were confirmed correctly loaded or applied and **27** were confirmed correctly persisted or supported by persistent inputs and effects for the complete rule. These are conservative whole-policy counts. Partial evidence appears separately in the table. **27** were fully runtime-verified, **11** partially verified, **4** not implemented, **0** import failures, **0** unresolved rule conflicts, and **8** blocked. Fixed implementation defects are recorded below.

Correct import means the existing source or authorized data was actually used in a runtime path with the intended values. It does not imply a separate bulk import occurred. Correct persistence means the entire policy's observable stored inputs, decisions or effects were checked. Restart testing directly covered drafts and pending collection state, while other verified policies were checked through isolated Mongo-backed reads and writes. This audit did not certify a deployed environment.

## Evidence keys

- **G / R:** [Focused Mongo/HTTP tests](focused.log) in `test_task9_grocery_replacement.py` and `test_task9_restaurant_replacement.py`. These cover in-scope ownership, stock, tax, ledger preservation, recalculation, notified decisions, refusal, duplication, and rollback.
- **F:** [Full regression](full.log) includes existing refund eligibility, mocked refund/webhook, financial, reward, referral, Task 8 and Task 21 checks. These checks do not count as genuine gateway or device validation.
- **B:** [Chromium workflow](browser.log) and [reproduction script](browser-smoke.py). Covers Restaurant proposal/notification/approval, paid removal Assist handoff, Admin reward rejection, and draft creation.
- **S:** [Process restart evidence](restart.log) and [reproduction script](restart-audit.py). Verifies actual API reload and replay after stopping and restarting the application with the same isolated MongoDB.
- **Build:** [TypeScript](typescript.log), [ESLint](lint.log) and [Expo web export](expo.log).

## Per-policy verification

| Policy ID | Policy Name | Imported Correctly | Persisted Correctly | Runtime Verified | Tests Passed | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T9-01 | Grocery cart substitution | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | Cart logic remains separate; fresh suite covers contracts but this run did not drive the isolated browser through the cart substitution control. |
| T9-02 | Seller reports unavailable line | Yes | Yes | Yes | Yes | VERIFIED | G/R and B cover actual report and unauthorized actors. |
| T9-03 | Customer-only acceptance and rejection | Yes | Yes | Yes | Yes | VERIFIED | G/R and B cover success, wrong owner and inappropriate roles. |
| T9-04 | Same merchant and valid alternatives | Yes | Yes | Yes | Yes | VERIFIED | G/R cover invalid catalogue entries, foreign options and variants. |
| T9-05 | Alternative quantity, sizes and options | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | R checked quantity and add-on compatibility. Exhaustive Grocery measured/brand and partial stock UI matrix was not exercised here. |
| T9-06 | Stale offers and price validation | Yes | Yes | Yes | Yes | VERIFIED | G/R covered both stale price and unavailable stock/menu. |
| T9-07 | No reservation before consent | Yes | Yes | Yes | Yes | VERIFIED | G includes reservation and rollback assertions. |
| T9-08 | Original unavailable inventory | Yes | Yes | Yes | Yes | VERIFIED | G verified zero unavailable stock and restoration for unaffected lines. |
| T9-09 | Fulfilment ready gate | Yes | Yes | Yes | Yes | VERIFIED | G/R tested pending gate and order status preservation. |
| T9-10 | Order line and decision history | Yes | Yes | Yes | Yes | VERIFIED | G/R exercised preservation, retries and superseding. |
| T9-11 | Replacement presentation and notification | Yes | Yes | Yes | Yes | VERIFIED | G/R and B verified notices, links, amounts and duplicate protection. |
| T9-12 | Offer expiry and independent cancellation | No | No | No | No | NOT IMPLEMENTED | Establish business-approved expiry duration and cancellation semantics before implementing; superseded and non-open order gates already apply. |
| T9-13 | Unpaid Grocery repricing | Yes | Yes | Yes | Yes | VERIFIED | G verified fee threshold, affected amount and order preservation. |
| T9-14 | Unpaid Restaurant repricing | Yes | Yes | Yes | Yes | VERIFIED | R and B covered tax and exact payable. |
| T9-15 | Decline surcharge and remove item | Yes | Yes | Yes | Yes | VERIFIED | G/R verify paid handoff and R covers successful unpaid removal and unavailable remainder; B drives paid route. |
| T9-16 | Empty or unfulfillable order fallback | Yes | Yes | Yes | Yes | VERIFIED | G and R distinguish empty and unavailable remainder; B checks linked request. |
| T9-17 | Assist linked to actor and order | Yes | Yes | Yes | Yes | VERIFIED | G/R and B exercised linkage, dedupe and scoped visibility. |
| T9-18 | Paid original record preservation | Yes | Yes | Yes | Yes | VERIFIED | G/R verified unchanged paid order, invoice and no payment writes. |
| T9-19 | Incremental collection quote and consent | Yes | Yes | Yes | Yes | VERIFIED | R verified approval gated by consent, stale price/coupon/cancel protection and false execution flag. |
| T9-20 | Incremental real collection | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Approve separate linked intent, capture and reconciliation protocol and perform authorized gateway TEST. |
| T9-21 | Paid cheaper or removed-item quote | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | G/R cover removal quote. Cheaper accepted replacement has no standalone refund quote; define applicable eligibility and a dedicated price-difference workflow. |
| T9-22 | Review approval and conflicting financial state | Yes | Yes | Yes | Yes | VERIFIED | R covered cancellation, price drift, coupon change and open refund rejection after correction. |
| T9-23 | Partial refund execution | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Approve active-order partial-refund amount, prior-refund accounting and idempotent settlement/reconciliation, then validate provider path. |
| T9-24 | Verified COD refund execution | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Authorize COD refund rail, payee proof and reconciliation. Legacy/manual collections are not sufficient evidence. |
| T9-25 | Existing full refund controls | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | Offline and mock paths passed in F, including rejected amounts. Genuine provider confirmation and external delivery were deferred. |
| T9-26 | Refund status and customer notices | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | Review states and mock confirmation tested. Unified replacement execution states and real confirmation unavailable until K dependencies. |
| T9-27 | Atomic replacement and replay | Yes | Yes | Yes | Yes | VERIFIED | G/R concurrent duplicate and injected rollback tests passed. |
| T9-28 | Seller approved financial split | Yes | Yes | Yes | Yes | VERIFIED | R/F verify eligible accounting, amount and no accounting before confirmed collection. |
| T9-29 | Seller settlement requests and execution | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | F verifies existing authorization and accounting rules; replacement payout adjustment/real payout requires agreement and execution validation. |
| T9-30 | Delivery partner reconciliation | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Approve delivery partner agreements, funding and fee allocation before wiring verified delivery settlement. |
| T9-31 | COME-IN recognized revenue categories | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | F covers accounting and verified membership separately; authorize recognition rules and reconcile ad/other income sources. |
| T9-32 | Spent reward ledger protection | Yes | Yes | Yes | Yes | VERIFIED | G/R and B verified preserved ledger, action/replay and rejection visibility. |
| T9-33 | Reward Admin decision and audit | Yes | Yes | Yes | Yes | VERIFIED | R and B cover role, replay and decision; no balance change. |
| T9-34 | New reward earning campaign | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Approve earning rate, valuation, payout/expiry and checkout/finalized-order application. Proposed reward units are not the legacy shopping credit balance. |
| T9-35 | Compensating reward adjustments | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Approve benefit allocation, refund/cancellation, coupon/loyalty treatment and compensating entries before enabling. |
| T9-36 | Referral identity and attribution | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | F verifies attribution guardrails and status. Dedicated verified identity and duplicate-risk evidence requires additional production-safe validation. |
| T9-37 | Referral qualifying order | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | F covers existing eligibility. Replacement plus already-awarded/refunded qualifier reversal needs explicitly approved published rules. |
| T9-38 | Referral reward and notification | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | F covers existing tracked reward rules. New configurable campaign linkage, fraud review breadth and reversal remain unverified. |
| T9-39 | Promotion draft configuration | Yes | Yes | Yes | Yes | VERIFIED | R/B/S verified draft write, read, normalized values, reload and disabled redemption. |
| T9-40 | Campaign cap configuration | Yes | Yes | Yes | Yes | VERIFIED | R/S verify invalid caps, concurrent identical drafts and persisted normalized limits. |
| T9-41 | Coupon activation and eligibility | No | No | No | No | NOT IMPLEMENTED | Implement published version, active/paused/expired status and server checkout evaluation after campaign approval. |
| T9-42 | Coupon redemption and refund policy | No | No | No | No | NOT IMPLEMENTED | Add checkout quote and checkout application from an approved campaign, plus release/reversal and transparent display rules. |
| T9-43 | Concurrent campaign spend and exhaustion | No | No | No | No | NOT IMPLEMENTED | Implement transactional reservation/consumption and spend ledger, idempotency keys and exhaustion notice before activation. |
| T9-44 | Historical tax recognition and original snapshots | Yes | Yes | Yes | Yes | VERIFIED | R/F preserved original invoice references and historical values. |
| T9-45 | Tax professional eligibility and access | Yes | Yes | Yes | Yes | VERIFIED | R exercises verified fixtures, assignment and denied unassigned/ordinary roles; real reviewer provisioning still pending. |
| T9-46 | Case-specific tax recommendation | Partial | Partial | Partial | Scoped only | PARTIALLY VERIFIED | R verified guideline requirement and audit. No authoritative corrected tax proposal calculator exists for historical records without approved guidance. |
| T9-47 | Separate Admin tax decision | Yes | Yes | Yes | Yes | VERIFIED | R verified missing review denial, separate role and approved pending accounting status. |
| T9-48 | Correction document issuance | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Obtain issuer responsibilities, case treatment, numbering, reporting and authorized reconciliation process. Do not generate documents from this audit. |
| T9-49 | Confidentiality and customer visibility | Yes | Yes | Yes | Yes | VERIFIED | R and B exercised projections, owner rendering and blocked unauthorized Admin audit. |
| T9-50 | Real provider and device gate | No for blocked operation | No for blocked operation | No | Safety gate only | BLOCKED | Native Android/iOS and authorized genuine Razorpay TEST payment, webhook and refund validation remain deferred. |


## Cross-policy checks and conflicts

| Combination | Result |
| --- | --- |
| Replacement + coupon and reward | Existing historical coupon/reward indicators prevent automated repricing. A coupon introduced after a collection quote now blocks Admin approval. Ledger protection and Admin rejection passed without posting a debit or credit. No active coupon engine was available to test. |
| Replacement + referral | Existing rule and attribution contracts passed. The final order remains the normal qualification input. Replacement reversal after a referral benefit has been awarded remains pending approved rules. |
| Replacement + incremental collection | Customer consent precedes Admin approval. Repricing, cancellation or a changed coupon now blocks stale approval. Stored and replayed approval remains pending execution. |
| Replacement + partial refund | A valid removal quote is review-only. An in-flight refund now blocks a second stale approval. The audit cannot validate an active-order partial payout. |
| Replacement + COD | Eligible unpaid order recalculation, cash status preservation and final accounting after confirmed cash state passed. A COD refund rail was unavailable. |
| Replacement + seller / delivery partner accounting | Finalized seller ledger linkage passed. Replacement allocation for delivery payouts lacks an approved agreement and verified execution. |
| Replacement + campaign budget | Draft caps survive reload and identical concurrent submissions reuse a draft. Active spend and exhaustion have no runtime evaluator and could not be exercised. |
| Replacement + tax / invoice | Legacy values remain untouched. Assigned professional access and separate Admin approval passed with fixture users. Statutory correction issuance remains disabled. |

The historical Grocery-only design was superseded by the approved Restaurant extension. Its proposed expiry and separate cancellation did not establish an approved duration. Draft campaign caps never override legacy checkout terms. Existing full-refund controls and the newer partial-refund review are separate workflows. No unresolved contradiction between two approved rules was demonstrated. Pending cases are described in the [framework decision register](../task-9-financial-policy-framework-20261123/DECISION_REGISTER.md).

## Confirmed defect corrected

An Admin payment review previously relied on the original ticket quote after the underlying order changed. Approval now reloads the owned order and embedded case and checks that they are still open, the monetary snapshot and customer decision match, no conflicting refund is present, and current catalogue and tax values reproduce the quote. It writes to the order in the same transaction as the approval so competing order changes cannot commit against the same snapshot. Rejection and exact recorded replays remain supported. Fresh negative tests cover cancellation, added coupon, catalogue price change and a pending refund. The application does not move money through this review.

The correction is recorded in `patches/task9-policy-audit-corrections.patch`, applied after the framework patch. It changes only `backend/server.py` and the Restaurant Task 9 tests. No collection, index or migration was added. Task 8, Task 21 and the Master ZIP were unchanged. No real payment or native checks were executed.

## Replay instructions

See [commands](COMMANDS.md). The [master register](TASK-9-POLICY-MASTER-REGISTER.md) includes provenance and source locations.

Fresh verification finished with **61 focused passed** and **695 full backend passed**, with zero failures and **one skip** for unavailable external object storage. TypeScript, targeted ESLint, Expo web export, the four Chromium scenarios and process restart checks passed. Genuine Razorpay TEST, live webhook and refund, and native Android/iOS remain deferred.
