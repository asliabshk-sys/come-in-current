# Proposed Premium Membership Balanced Refund Policy

This is a proposed operational policy subject to owner confirmation and applicable legal review. The membership price remains ₹299 for 30 days. The seller may request review from their own membership payment history. A request or approval carries no promise of a refund or bank-credit date.

| Case | Proposed treatment |
|---|---|
| Duplicate verified capture | Keep the original membership payment. Review the additional charge only. |
| Capture without activation | Reverify the capture and attempt activation. If activation remains unavailable, review the captured payment for refund. |
| Cancellation before activation or wrong purchase | Review the full captured payment after verifying shop ownership and purchase association. |
| Change of mind after activation | Normally non-refundable. The seller can submit a case and the admin records the decision. A separately evidenced technical or suspension issue should be presented under its corresponding reason. |
| Verified technical outage | Investigate and restore service. At the threshold, review a full refund, an admin-specified partial amount, or an extension according to verified impact. |
| Suspension | Investigation and verified misconduct do not establish refund eligibility. A documented mistaken or technical/administrative suspension can qualify for restoration, extension or applicable refund. AI suspicion alone is not a verified finding. |

`MEMBERSHIP_PRE_ACTIVATION_REFUNDS` defaults to true for policy eligibility. `MEMBERSHIP_OUTAGE_HOURS` defaults to 48. `MEMBERSHIP_REFUNDS_ENABLED` defaults to false and gates gateway submissions and reconciliation. Keep it disabled until the owner confirms the policy, legal review is complete, and the target environment is authorized. Enabling the gateway does not bypass case approval.

Admins record a verified server-side incident and the source evidence for highlight, search, discovery, or entitlement. The record is deduplicated by service and start time and includes recovery when known. The server computes consecutive overlap with paid membership intervals. Intake depends on verified incident records supplied by an admin. A missing impression, customer device issue, or isolated connection issue does not create an outage. Revisit an open incident in the admin form at the threshold or on recovery to evaluate affected memberships. No automated monitoring feed or outage polling is configured. The membership interval is used for impact calculation, and historical suspension intervals are not reconstructed.

An approved full refund of the entitlement payment places a hold when gateway execution is enabled. A confirmed full refund cancels the entitlement and retains the history. Confirmed gateway failure clears the hold. Duplicate-payment refunds, partial refunds and extensions preserve the applicable entitlement. The review extension has no automatic calculation formula.

An uncertain submission stays processing. Reconciliation reads the provider refund history and validates the payment ID, amount and stored refund reference. A case does not send another refund after an uncertain or terminal attempt. Unmatched provider history and uncertain submissions with no matching reference need controlled manual reconciliation. This implementation does not change Grocery or Restaurant refund rules.
