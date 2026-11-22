# COME-IN TEST-only payment validation matrix

No real Razorpay request, payment, refund or provider webhook delivery was executed. PASS entries below refer only to the specified source/local/mock layer. Every real provider scenario A–T remains BLOCKED pending secure TEST bindings, allowed network/provider delivery and native resources. Local signing material is ephemeral and is not a provider credential.

| Case | Scenario | Available layer result | Evidence/scope |
|---|---|---|---|
| A | Successful payment | PASS | Local signed capture + both-order transactional handlers |
| B | Failed payment | PASS | Local signed failed event, pending order retained |
| C | Cancelled payment | PASS source/mock | Native mocked cancellation; existing cancellation/late-capture checks |
| D | Interrupted checkout | PARTIAL | AppState backend refresh source; process-kill/device test BLOCKED |
| E | Duplicate callback | PASS local | Existing idempotent capture/financial tests; native concurrent checkout guard |
| F | Invalid signature | PASS | Pure HMAC/security tests; local HTTP rejection |
| G | Invalid webhook | PASS | Local HTTP + strict JSON/schema signature rejection |
| H | Duplicate webhook | PASS | Concurrent local HTTP, single durable event record |
| I | Delayed webhook | PASS | Late failed after paid preserves state |
| J | Capture after frontend failure | PASS local | Capture independent of UI; receipt failure then retry test |
| K | Payment/order mismatch | PASS | Local mismatch leaves pending; amount/currency verifier tests |
| L | Refund success | PASS local/mock | Admin auth+Mongo+provider mock; signed local refund reconciliation |
| M | Refund failure | PASS local/mock | Provider timeout uncertainty and late failed event protection |
| N | Duplicate refund | PASS local/mock | Concurrent same request one mocked POST; no blind replay |
| O | Partial refund | PASS source/local | Observed partial reconciled; unsupported partial initiation rejected per existing full-only policy |
| P | Unauthorized refund | PASS local | Real JWT HTTP401/403 and admin queue RBAC |
| Q | Grocery payment | PASS local/mock | Intent race/retry, capture/fail, refund transactions |
| R | Restaurant payment | PASS local/mock | Intent race/retry, capture/fail and existing refund regression |
| S | Android native payment | BLOCKED real | Hermes bundle + mocked adapter PASS; SDK/device/provider missing |
| T | iOS native payment | BLOCKED real | Hermes bundle + mocked adapter PASS; Xcode/device/provider missing |

Evidence: [78-test output](evidence/release-completion-20261117T094751Z/step9-payment-v2.log), corresponding XML, Step1 financial results, Step6 mocked native contract and Steps7/8 bundle logs.


## Resume verification 2026-11-18T05:29:47.952268-08:00
78 local/mock selectionPASS and7 final affected checksPASS;5 native adapter mocked checksPASS; both native JS bundlesPASS. All real provider/device rows remain BLOCKED. No actual provider operation. See evidence/resume-20261118 and final reports; no policy relaxation.

## Premium Membership refund additions — 2026-11-23 IST

| Scenario | Validated layer |
|---|---|
| Duplicate capture, one case per payment and one submission | Local HTTP/Mongo and mock gateway PASS |
| Pending, final processing, timeout reconciliation and failure | Local HTTP/Mongo and mock gateway PASS |
| Policy, authorization, extension and rollback | Local unit and integration PASS |
| Seller and admin views | Chromium API fixture PASS |
| Actual Razorpay TEST refund and external reconciliation | DEFERRED — authorized external TEST environment required |
