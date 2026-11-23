# Security and consistency review

This audit did not independently verify a critical defect that calls for a behavior change under the existing approved rules. Current tests establish limited existing behavior. New timed expiry and cancellation checks cannot be exercised until the rules are approved.

| Scenario | Current evidence | Gap after decision |
| --- | --- | --- |
| Expired offer | State/catalog invalidation is separate from timed expiry. No replacement deadline exists to evaluate. | Persist authority and start event, guard at inclusive/exclusive boundary as approved, and return actionable stale status. |
| Duplicate accept and cancel | Exact decision replay returns the saved outcome and concurrent acceptance tested one write. Independent cancellation is absent. | Atomically idempotent cancel/expiry with only one outcome and one audit/notice. |
| Concurrent customer/Admin action | Customer decisions and scoped staff refresh use order transactions. Admin has separate review permissions, without offer-cancel authority. Exact accept-versus-cancel race is untestable now. | Use conditional live state, case version and permitted order stage. Validate races with refresh, progress, Assist review and order cancellation. |
| Unauthorized or wrong order | Customer role and owning order query, then lookup of case embedded on that order. Seller/Admin proposal scope is separate. | Reuse scoped ownership. Test cross-order IDs, anonymous/other-customer/seller/Admin boundaries for the new action. |
| Expiry after acceptance | Applied `accepted` decisions and recorded Assist intent are distinct. Historical exact replays may return before open-state checks. No clock can revoke either. | Decide explicit protection for both categories. Maintain idempotent historical replay distinct from new acceptance. |
| Restart | Cases and decisions persist on orders. Prior closure verified restart for adjacent flows. This campaign did not start a separate replacement-expiry process because none exists. | Restart with fixtures immediately before/at/after deadline, including no partial writes or repeated event/notice. |
| Audit | Actor/time, prior amount and action are recorded; supersession and financial review have separate records. | Capture prior/new state, policy version, clock and deadline, reason, order/case and optional reoffer link. Test rolled-back state/audit/notice under failure. |

No source code, policy, permission, financial record or customer balance was changed.
