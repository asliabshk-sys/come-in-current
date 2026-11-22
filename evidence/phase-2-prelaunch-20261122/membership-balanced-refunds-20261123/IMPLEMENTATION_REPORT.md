# Premium Membership Balanced Refund Policy — implementation and local evidence

Verified baseline: GitHub `work` at `0664e4bcd635c343973298e700c7e9394495247a`. Apply `patches/membership-balanced-refunds.patch` after the Razorpay pre-test patch. The archive and previous patches are preserved. See [the proposed policy](../../../docs/PREMIUM_MEMBERSHIP_REFUND_POLICY.md).

- Seller requests and history are integrated in the existing Membership screen. Admin Membership adds case filters, documented decisions, suspension findings, refund execution/reconciliation and verified outage intake. Seller sees date, status, decision and gateway refund ID when known. The existing in-app notification system records transitions and alerts admins on new work.
- `backend/server.py` integrates ownership, payment association, transaction locking, membership entitlement and audit. `backend/membership_refund_policy.py` centralizes configurable policy and outage eligibility. The seller/admin routes reuse `frontend/src/components/MembershipRefunds.tsx`.
- Seller APIs are `GET/POST /shops/{shop_id}/membership/refunds`. Admin APIs are `GET /admin/membership-refunds`, `GET/PATCH /admin/membership-refunds/{payment_id}`, `POST /admin/membership-refunds/{payment_id}/process` and `/reconcile`, and `POST /admin/membership-outages`. Status transitions record actor, time and reason. Activation and review use server-side payment records and gateway evidence; payout is reserved for explicit admin processing.
- MongoDB uses one case per captured gateway payment, a shop/date index, and deduplicated incident records. Membership/audit mutations are transactional. Provider network I/O is outside driver-retried transactions. The same receipt ties preflight and reconciliation to the approved case. Existing membership entitlement and Razorpay refund-history infrastructure are reused. No new dependency was added.
- Full technical impact depends on operator-verified incident evidence, with no automated incident feed. Open incidents are reevaluated when re-submitted or closed. Terminal cases and uncertain gateway outcomes without a matching reference require controlled review and do not automatically reopen or send another refund. A formal partial-refund formula remains an owner decision.

## Tests

| Evidence | Executed result |
|---|---|
| [Focused backend](focused-backend.log) | 19 passed, zero failed or skipped |
| [Full backend](full-backend.log) | 685 passed, zero failed, five skips |
| [Browser](browser.log) | Two Chromium fixture flows passed, seller submission and admin approval |
| [Frontend](frontend.log) | TypeScript, ESLint with zero warnings, Expo web export and patch checks passed |

Focused command used `python -m pytest -q -n 0 --tb=short` over membership refund policy, Mongo portability, Premium membership integration, local payment webhook and local Grocery refund integration. It used synthetic JWTs, a disposable loopback MongoDB replica set, and in-process gateway responses. The new cases include request and approval concurrency, forged fields, cross-shop and seller/admin boundaries, exact amount limits, refund holds, duplicate capture, timeout and reconcile, terminal-state replay, failed refund, outage duration and deduplication, extension, notifications and transaction rollback.

The full regression used `python -m pytest -q -n 0 --tb=short -rs`, with preview and batch runtime modules first and the remaining backend tests in sorted order, against a fresh disposable backend database. The five skips were object storage and four optional catalogue import dependencies. The browser harness uses exported Expo web with local API fixtures and blocks external HTTPS. From `frontend`, the build commands were `tsc --noEmit`, targeted `eslint --max-warnings 0`, and `expo export --platform web`.

## Deferred

Genuine Razorpay TEST refunds and external reconciliation require an authorized Razorpay TEST account, securely configured TEST key ID/secret, an isolated test backend with authorized egress, and a captured eligible TEST payment. Production refunds and live customer financial activity require separate owner, legal and production approval, securely configured credentials, and approved operational controls. No external financial operation was attempted. Gateway refund execution remains disabled by default.
