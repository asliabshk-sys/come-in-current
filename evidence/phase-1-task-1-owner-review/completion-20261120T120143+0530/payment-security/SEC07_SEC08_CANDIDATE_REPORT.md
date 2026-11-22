# SEC-07 / SEC-08 Candidate Correction and Local Validation

COME-IN Phase 1 Task 1. Recorded 2026-11-20T12:14:08.411964+05:30 (Asia/Kolkata).

**Candidate result: SEC-07 PASS and SEC-08 PASS within local mocked scope.** Only an isolated candidate copy changed. Parent owns merging the reviewed delta and integrated backend verification. Actual Razorpay payment/webhook/refund settlement,Android and iOS validation remain explicitly **DEFERRED**. No external credentials,provider/network call,DB operation,package installation or native tool invocation occurred.

## Recovered findings and minimum candidate

- SEC-07 LOW: synchronous payment/refund HTTP requests inside async handlers blocked the event loop. Production latency/SLO impact was previously unmeasured.
- SEC-08 MEDIUM: configured webhook buffered the request and calculated HMAC before the existing 1 MiB parser limit. Actual production ingress caps were unavailable.

Seven existing functions differ;all other AST nodes,imports,route signatures,models,schema,transaction-helper implementation and SEC-01 reset code are identical. The candidate does not redesign provider architecture or UI.

| Function | Minimal correction |
| --- | --- |
| create_restaurant_payment_intent | Offload provider POST |
| verify_restaurant_payment | Offload provider GET |
| admin_refund_restaurant_order | Offload existing refund-history helper and provider POST |
| admin_refund_grocery_order | Offload existing refund-history helper and provider POST |
| create_grocery_payment_intent | Offload provider POST |
| verify_grocery_payment | Offload provider GET |
| razorpay_webhook | Bound raw stream before HMAC/JSON/DB |

Eight provider I/O sites across six handlers use existing `asyncio.to_thread`. Direct calls use a lambda preserving original requests arguments/timeouts/exception behavior;the entire existing synchronous pagination helper is offloaded at its two call sites. Provider calls remain outside retried DB callbacks. No provider retry was added.

Webhook configuration503 remains first. Declared Content-Length is an early optimization,not trusted as the actual size. The stream checks accumulated raw bytes and rejects more than1MiB with413 before extending the buffer or computing HMAC/JSON/DB work,including absent/forged lengths. It stops at the first over-limit chunk. Exact valid raw bytes are retained for signature verification. Existing event validation,deduplication and state/transaction handlers are unchanged.

Cancellation cannot stop a requests thread already running. The event loop/coroutine can be released while an existing operation claim remains pending/unconfirmed;duplicate creation is blocked and no payment is inferred as paid. This is uncertainty requiring reconciliation,not a claim that provider effects can be undone. Production load/ingress and genuine provider outcomes remain outside these local assertions.

## Before/after executable evidence

| Phase | PASS | FAIL | ERROR | SKIPPED |
| --- | --- | --- | --- | --- |
| Before | 19 | 11 | 0 | 0 |
| Candidate | 30 | 0 | 0 | 0 |

The corrected runner and all30invariant assertions are identical for both source copies. Six heartbeat/thread checks reproduce blocking before and prove all eight I/O calls run off the event-loop thread afterward. Other checks cover six successful state/response paths,six timeout502 paths,ownership/refund-role protection,and cancellation without false confirmation/automatic outbound replay.

Webhook checks cover declared oversize,chunked missing length,forged short length,stop at first over-limit chunk,invalid-signature oversize rejected before HMAC,exact1MiB valid signature,invalid signature,missing configuration503,malformed JSON and duplicate-event idempotency. Actual source handler/helper bodies are AST-extracted;state/database/provider transports are explicitly in-memory doubles and socket connect is denied. Full HTTP middleware/dependency injection,real Mongo transaction safety and real provider delivery are not certified by this suite. Parent must run existing localASGI/Mongo regressions against merged source.

Initial attempts remain:before16PASS/12FAIL/2ERROR,candidate26PASS/2FAIL/2ERROR. Missing ledger/event-recorder mock bindings caused those harness errors and two failed fixture checks. Added bindings only;no source/assertion changed. The original harness snapshot is retained. Initial attempts are not new independent coverage or product defects.

## Exact commands and hashes

```sh
cd /workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security
/workspace/come-in-tools/py311/bin/python -B build_candidate.py
/workspace/come-in-tools/py311/bin/python -B validate_payment_security.py --stage before-v2 --source before-server.py
/workspace/come-in-tools/py311/bin/python -B validate_payment_security.py --stage candidate-v2 --source candidate-server.py
```

Before source SHA-256: `70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`.
Candidate SHA-256: `3c4a5f258f1af0c06245b2bec0a9262c7a733da9b638ba39f21c26a67945d379`.
Same corrected runner SHA-256: `a7b64f0bd853d7a01dbc175100c1f4648fd69bad9b135b42d28a57e4c0ae5c68`.

Candidate/patch/merge plan: [candidate-server.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security/candidate-server.py>), [candidate.patch](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security/candidate.patch>), [merge-plan.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security/merge-plan.json>).
Results: [before-v2-results.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security/before-v2-results.json>), [candidate-v2-results.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security/candidate-v2-results.json>);raw XML/logs are retained alongside them.
Detailed limitations/status: [payment-security-results.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/completion-20261120T120143+0530/payment-security/payment-security-results.json>).

## Safe stopping point

No actual protected source was edited by this workstream. All mock processes finished. Next exact action:parent merges only these seven functions,then runs this harness against merged actual source and the existing localASGI/Mongo payment/refund suites. No real provider/native validation is authorized. Task1 is not approved or closed by this candidate report.
