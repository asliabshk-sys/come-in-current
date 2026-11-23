# COD evidence consistency fix

Apply `patches/task9-partial-cod-refund-verification.patch` after the rewards/referral verification patch.

- `backend/server.py` now commits existing manual cash confirmation, its audit, and any eligible finalized order ledger snapshot in one Mongo transaction. It adds prior/new payment state, persisted order total and currency to the audit. Legacy evidence and existing amount/eligibility rules are preserved.
- `backend/tests/test_task9_restaurant_replacement.py` verifies pre-delivery and unauthorized rejection, audit failure rollback, concurrent replay and stable audit evidence.
- The restart harness creates a disposable COD order, exercises merchant confirmation and Admin reconciliation, and verifies one audit, one eligible ledger entry and zero provider payment records after restart.

The audit total is the amount on the order. This does not attest actual cash amount and adds no payout route, refund formula, provider change, migration or new API.
