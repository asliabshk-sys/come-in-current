# Advertisement compensation technical fixes

Apply `patches/task9-advertisement-compensation-verification.patch` after the coupon verification patch. Retained source files changed:

- `backend/server.py` — use the existing Mongo transaction helper to atomically record Admin campaign status and transition audit. An identical immediate state-change replay returns the saved campaign. Reject attempts to move a removed or rejected ad through pause. Apply the active campaign and targeting filters at event intake for legacy and commercial campaigns.
- `backend/tests/test_task9_business_policy.py` — adds authorization, rollback after booking, status and audit writes, concurrent replay, transition evidence and paused-event checks.
- `backend/tests/test_task4_storage_advertisement_integration.py` — binds the fixture's transaction client to its database and covers removed legacy events and attempts to resume removal.

CHAND, poster-only uploads, owner publication, booking economics and delivery snapshot logic remain in force. No new rates, compensation, refund, transfer or credit behavior was introduced. No unrelated app source changed. The restart harness is in this evidence folder.
