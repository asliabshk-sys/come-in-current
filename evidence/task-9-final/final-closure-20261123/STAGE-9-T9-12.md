# Stage 9 — T9-12 Offer expiry and independent cancellation

**NOT IMPLEMENTED.** The authoritative register identifies T9-12. Existing Grocery and Restaurant replacement state checks reject superseded proposals or orders no longer open for replacement. Existing customer choice and reoffer flows continue. The dated coupon, advertisement and membership windows do not define replacement-offer expiry.

The owner must specify duration, start event, whether the cutoff is exclusive, independent cancellation actor and permitted states, effect on already-issued offers, handling of new offers, and notice/audit requirements. [Unsigned decision record](../offer-expiry-rules-20261123/OWNER-DECISION.md)

With approval, the minimal integration is to use the existing replacement case and decision transaction, record the server deadline, reject stale/superseded state atomically and record actor, reason and timestamps without changing historical outcomes. Test the precise boundary, concurrent accept/cancel, replay, rollback and restart under the approved rule. No policy mutation was introduced now.

Existing guards exercised with `python -m pytest -q -n 0 --tb=short backend/tests/test_task9_grocery_replacement.py backend/tests/test_task9_order_actions_contract.py`. [Output](stage-9-focused.log)
