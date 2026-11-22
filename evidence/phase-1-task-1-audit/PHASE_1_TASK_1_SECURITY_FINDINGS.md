# PHASE 1 TASK 1 — Security Findings

Audit timestamp: 2026-11-18T06:59:35.322181-08:00 (UTC−08). **Final status: REVIEW PENDING.** Canonical Phase1/Task1=Existing Project Audit under the recovered22-task roadmap. Roadmap Recovery is preserved and is not proof that this application audit passed. No canonical task added/renamed/merged/renumbered. Task2/implementation NOT STARTED. Only files in `/workspace/come-in-current/evidence/phase-1-task-1-audit` are created/updated. Existing source,ZIP,patches and all five checkpoints are protected unchanged.

Evidence labels: **SOURCE VERIFIED**=located in current code/document;**STATICALLY VERIFIED**=read-only parser/structural check;**TEST EVIDENCE FOUND**=persisted result with date/scope,not freshly run;**RUNTIME VERIFIED**=only the specified actual runtime observation;**EXTERNAL INTEGRATION VERIFIED**=requires real external provider evidence (none newly established);**HISTORICAL REPORT ONLY**,**NOT FOUND**,**UNVERIFIED**,**BLOCKED** retain their narrow meaning.

Allowed item statuses: VERIFIED,PARTIALLY VERIFIED,NOT IMPLEMENTED,NOT FOUND,HISTORICAL CLAIM ONLY,UNVERIFIED,BLOCKED,REVIEW REQUIRED. A VERIFIED inventory/declaration is not VERIFIED business behavior. Owner approval for audit acceptance/fixes/Task2 remains pending.

## Severity summary and review boundary

**0 CRITICAL,1 HIGH,5 MEDIUM,2 LOW findings/review items.** Findings are source-observed control gaps or risks,not successful exploits. Deployment mitigations and actual production exposure are UNVERIFIED. No attack,credential guessing,production API call or state-changing security test was performed. No fix applied. Status for every finding is REVIEW REQUIRED until owner review and approved validation/remediation.

## SEC-01 — HIGH — Password-reset token consumption and password update are not atomic

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[reset_password](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>).
- Finding:The function reads a live unused token,updates users.password_hash,then marks password_resets.used in a separate update. There is no token-state compare-and-set claim or shared transaction across these operations.
- Potential impact:Concurrent reuse or a failure between writes can permit a token to remain usable or competing resets to overwrite the password. This is a source-derived race/failure concern;no exploit or reset was attempted.
- Safe recommendation:In a separately approved fix,use one transactional conditional token-consumption/password-update flow with expiry checks and failure recovery;add isolated concurrency/rollback tests.
- Related tests/evidence:test_functional_blockers_regression.py; password-reset contracts in existing suites do not establish concurrent one-time consumption.

## SEC-02 — MEDIUM — Seven-day access JWTs have no server-side session/password-version revocation

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[create_access_token](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:250>), [get_current_user_optional](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:268>), [reset_password](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>).
- Finding:Tokens carry sub,role,email,type,exp;authorization reloads DB roles,which is positive,but no session ID/token version/password-changed cutoff is checked. Password reset does not revoke existing access JWTs. No logout-all/revoke endpoint found in179 registrations.
- Potential impact:A previously obtained valid token can retain access until expiry after a password change,unless the account is removed or other checks deny it. Native/client logout alone does not revoke a copied token.
- Safe recommendation:Agree on session-revocation policy;then add server-checked token version/session state and invalidate sessions on sensitive account changes without weakening role checks.
- Related tests/evidence:test_frontend_contracts.py;source/session inventory;no new token test executed.

## SEC-03 — MEDIUM — IP rate-limit identity trusts caller-supplied X-Forwarded-For

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[_client_ip](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:819>), [_rate_keys](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:824>).
- Finding:The first forwarded header value is accepted without an application trusted-proxy check. A sanitizing ingress may mitigate this,but actual ingress configuration is unavailable.
- Potential impact:If directly reachable or behind an unsanitized proxy,IP-based registration/reset/login throttles can be evaded. Email/subject counters still provide separate protection where used.
- Safe recommendation:Verify trusted proxy/ingress behavior;derive client identity only from trusted forwarding information and retain subject controls.
- Related tests/evidence:Source inspection only;no spoofing requests or bypass attempts performed.

## SEC-04 — MEDIUM — Authentication throttle check and increment are separate operations

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[_check_auth_rate_limit](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:833>), [_record_auth_attempt](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:841>), [login](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:889>).
- Finding:A request reads counters before later $inc;concurrent requests can all pass the same limit check. Login increments only after failed verification.
- Potential impact:Burst concurrency may exceed the intended per-window limit. No concurrency/abuse attack was run.
- Safe recommendation:Use a reviewed atomic limiting primitive with shared worker semantics and explicit rejection policy;test only on an isolated service.
- Related tests/evidence:Existing auth tests show basic rate behavior historically,not strict burst-cap enforcement.

## SEC-05 — MEDIUM — Legacy diagnostic status endpoint permits anonymous persistent writes

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[create_status_check](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:687>), [list_status_checks](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:694>), [StatusCheckCreate](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:682>).
- Finding:POST /api/status directly inserts client_name into status_checks without auth or endpoint rate control;client_name has no explicit length bound. GET returns up to1000 records. Global ingress controls are unverified.
- Potential impact:Untrusted callers can create diagnostic data/storage load and retrieve the shared diagnostic feed. This is legacy behavior,not assumed to be intentional public operational policy.
- Safe recommendation:Owner should decide whether to retire,restrict or bound this legacy endpoint;require suitable authorization/rate/size controls before production. Do not remove it during audit.
- Related tests/evidence:Static route/body inspection;no diagnostic record created.

## SEC-06 — LOW — Password character limits exceed bcrypt byte limit

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[RegisterIn](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:305>), [hash_password](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:233>), [bcrypt4.1.3 pin](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/requirements.txt:11>).
- Finding:Registration permits128 characters and reset128,while hash_password passes UTF-8 directly to bcrypt4.1.3. No explicit72-byte bound or reviewed long-password handling is present.
- Potential impact:bcrypt byte truncation/compatibility can make distinct long inputs equivalent or otherwise cause password-contract ambiguity. Exact runtime behavior was not exercised;do not report a tested credential collision.
- Safe recommendation:Review byte-aware password policy/library behavior and provide compatible migration/tests rather than silently truncating credentials.
- Related tests/evidence:SOURCE VERIFIED configuration mismatch;runtime UNVERIFIED;no passwords/salts/credentials created.

## SEC-07 — LOW — Blocking provider HTTP inside async payment routes

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[create_restaurant_payment_intent](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4990>), [verify_grocery_payment](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6470>).
- Finding:Synchronous requests/http_requests calls appear in async handlers with timeouts. Real-provider latency/load behavior is not verified.
- Potential impact:Slow provider responses can occupy the event loop and reduce availability;this is a source-level performance/availability concern,not a measured outage.
- Safe recommendation:After approval,review bounded async HTTP or safe thread offload while keeping all provider effects outside retried DB callbacks and preserving idempotency.
- Related tests/evidence:No provider/load test performed.

## SEC-08 — MEDIUM — Webhook size check occurs after whole request body is buffered

- Status:REVIEW REQUIRED;evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.
- Affected component/evidence:[razorpay_webhook](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5362>), [event_payload](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/payment_webhook.py:19>).
- Finding:The route awaits request.body(),computes HMAC,then event_payload checks1MiB. The check does not bound the earlier body read. Production ingress body-size protection is unknown.
- Potential impact:When the provider route is configured,oversized unauthenticated bodies can consume buffering/HMAC resources before rejection. This was not load-tested and no large request was sent.
- Safe recommendation:Review ingress caps and an endpoint streaming/body cap before full buffering,while preserving exact raw bytes for signature validation.
- Related tests/evidence:Source inspection;test_webhook_envelope_security.py checks parser bounds,not pre-buffer transport allocation.

## Controls found and limits

- Registration assigns customer server-side;shop registration promotes only to shopkeeper,not admin. Admin endpoints declare role dependencies;shop/Restaurant/order ownership helpers are present. No direct role-escalation or IDOR exploit was attempted/proven. See API inventory for per-endpoint declared/body checks;absence of Depends alone is not a vulnerability.
- Mongo document serialization removes password_hash and internal Grocery idempotency/session fields. Public record projection removes selected internal actors. No secret values were printed or copied. Actual production response/log redaction remains unverified.
- Payment settings enforce explicit environment/key-mode consistency;server-side signatures/provider amount/currency/order checks and raw-body webhook HMAC present. Refund eligibility/admin authorization/claim/reconciliation and transactional ledger mechanisms present. Actual provider success is not established.
- General image upload checks auth,5MB bounded read and JPEG/PNG/GIF/WebP signatures before storage. Header validation is not full decoding/malware scanning. Existing25 focused/12HTTP artifacts are historical evidence,not a new run.
- Catalogue importer validates extension/MIME/magic,batch/row/ZIP expansion/ratio/path bounds. Legacy product import rejects formula-like text;universal importer preserves raw untrusted cell text for provenance,not execution;XLSX uses read_only/data_only. No live spreadsheet execution/export performed. No universal sanitization change recommended without preserving the approved untrusted-source-text contract.
- CORS production explicit-origin guard and native production HTTPS/ATS/cleartext config found. Actual ingress,TLS/HSTS,CSP,secret rotation,DB roles/firewall/backup/monitoring and infrastructure/dependency advisories remain BLOCKED/UNVERIFIED without actual environment evidence. No network vulnerability scanner/npm audit/pip audit was run.
- Local disposable metadata shows52 collections,0 MongoDB collection validators. Pydantic/input validators are present;storage-level validation is a separate REVIEW REQUIRED data-integrity gap,not grounds to mutate schemas during audit.
- Web auth storage is JavaScript-accessible AsyncStorage abstraction;native uses SecureStore. No user-controlled dangerouslySetInnerHTML path found in inspected source;the +html usage is a fixed stylesheet. This is not a complete XSS proof or production CSP audit.
