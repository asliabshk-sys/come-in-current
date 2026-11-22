# Complete Application Security Audit — Workstream I

Project: COME-IN. Recorded 2026-11-19T21:22:47.373958+05:30 (Asia/Kolkata). Repository `/workspace/come-in-current`;branch `work`;HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. Actual application extraction: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`.

**Security validation: FAIL. Task1: REVIEW PENDING.** This is a broad evidence review,not production-security certification or owner approval. The application extraction is outsideGit and contains inherited work;HEAD alone does not identify tested source. Current `server.py` SHA-256 is `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db` and matches the prior source inventory. Original source/configuration/reports/checkpoints were not edited. No fixes or Task2 were started.

## Scope and evidence reviewed

All six previous final reports and ITERATION_CHECKPOINT were read. Their hashes are recorded in [security-audit.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/security-audit.json>). The completed179-API inventory was reused without regeneration. Route dependency declarations,selected sensitive handlers,models,ownership helpers,checkout/payment/refund state guards,upload/storage,delivery projections and configuration boundaries were examined. Counting route registrations or event bindings does not count vulnerabilities and does not prove all endpoints secure.

This finalizer read the saved50-case broad test evidence without rerunning it. The earlier run in this same workflow executed selected **actual current source** AST function/model bodies with routing decorators removed and explicitly synthetic in-memory collection doubles. Networking was prohibited. Pydantic/globals used by these models match the source constants. These are unit/model-double results,not HTTP,real Mongo,device or provider results.

The dedicated password-reset workstream separately executed30cases using actual functions and a unique local MongoDB database. It is cited here and not counted a second time. External provider,native and production-infrastructure validation remain separate gates.

## Actual test results and provenance limits

| Evidence category | Final PASS | Final FAIL | ERROR | SKIPPED | Evidence |
| --- | --- | --- | --- | --- | --- |
| Broad helper/model/role/redaction/tracking/last-admin cases | 49 | 1 | 0 | 0 | [broad-security-isolated-v2.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-isolated-v2.xml>);[broad-security-isolated-v2.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-isolated-v2.log>) |
| Dedicated password-reset cases (separate suite) | 23 | 7 | 0 | 0 | [password-reset-results-v2.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-results-v2.json>);[password-reset-junit-v2.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-junit-v2.xml>) |

The broad run XML records timestamp `2026-11-19T08:42:36.126238+00:00`. Source `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py` is hash-bound,selected source segment hashes and all50case names/results are in the JSON. The saved broad artifacts do not retain the full original shell invocation;that provenance limit is explicit. A reproduction command (not executed by this finalizer) is:

```bash
PYTHONDONTWRITEBYTECODE=1 /workspace/come-in-tools/py311/bin/python -m pytest -q -n 0 -p no:cacheprovider /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/test_broad_security_isolated.py --junitxml=/tmp/comein-security-NEW-RUN.xml --basetemp=/tmp/comein-security-NEW-RUN-tmp
```

Use new unique `/tmp` output names rather than overwriting retained evidence. The dedicated reset report records its own command,environment,controlled barriers/fault wrappers and real test database.

First broad attempt:48PASS/2FAIL. One failure was an invalid harness EmailStr fixture (`example.test`);the fixture was corrected to `example.com`,with source bodies/security assertions unchanged. The other failure is the genuine last-admin invariant defect and remains FAIL in v2. Original harness/log/XML are retained: [broad-security-isolated-harness-v1.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-isolated-harness-v1.py>), [broad-security-isolated.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-isolated.log>), [broad-security-isolated.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-isolated.xml>). No xfail,skip,assertion weakening or source fix was used to get49passes. Earlier attempt counts are not added to final totals.

## Security findings and severity

Identified findings: **0CRITICAL,1HIGH,6MEDIUM,2LOW —9canonical finding IDs**. This is the finding count for this review,not proof that every possible vulnerability is excluded. The previous eight findings remain open;SEC-09 is the new bounded concurrency finding. RESET-10 and RESET-18 are LOW subissues under recovery integrity;they do not create extra canonical finding IDs. A test failure is not automatically a new vulnerability.

| ID | Severity | Validation status | Source/symbols | Evidence / preconditions | Disposition |
| --- | --- | --- | --- | --- | --- |
| SEC-01 | HIGH | FAIL | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>) reset_password/forgot_password/_send_password_reset_email | RESET-16,RESET-17; Actual AST-extracted functions with real Motor/Mongo on a unique retained local database:both same-token consumers accepted under a controlled read barrier;injected token-marker write failure left a changed password and unused token,then accepted retry. An existing account and unused/unexpired valid synthetic token;deliberately forced concurrent read or post-password-write failure. No arbitrary unauthenticated takeover or deployed-account exploit is claimed. | OPEN — owner authorization/decision required |
| SEC-02 | MEDIUM | FAIL | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:250>) create_access_token/get_current_user_optional/reset_password | RESET-19; Actual local Mongo/JWT execution accepted a pre-reset access JWT after a successful password reset. Requires possession of a still-valid prior JWT. Current DB user/role lookup,signature/type/expiry and deleted-account checks still apply. The owner must define relevant recovery/logout-all revocation policy. | OPEN — owner authorization/decision required |
| SEC-03 | MEDIUM | BLOCKED | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:819>) _client_ip/_rate_keys | RESET-29 observation only; Source and helper observation select the first X-Forwarded-For value without an in-function trusted-proxy boundary. Actual bypass depends on exposed direct ingress or an unsanitized proxy;production proxy trust/sanitization was not examined. Helper observation is not a deployed bypass proof. | OPEN — owner authorization/decision required |
| SEC-04 | MEDIUM | FAIL | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:833>) _check_auth_rate_limit/_record_auth_attempt/_enforce_auth_rate_limit | RESET-27; Real local Mongo scheduling test starts the subject count at4 for cap5;two concurrent checks accept and final count is6. Sequential cap checks pass. Both requests read before increments;observed local overshoot is2accepts at the one remaining slot. No load/capacity outage or unlimited-bypass claim. | OPEN — owner authorization/decision required |
| SEC-05 | MEDIUM | BLOCKED | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:687>) create_status_check/list_status_checks | SOURCE pattern;production policy unavailable; Anonymous diagnostic POST inserts a client_name;shared GET feed has a1000limit. No length/auth/rate dependency appears in these route declarations. Intended audience and effective edge caps are unknown;no diagnostic abuse/load test was run. Public intended policy requires owner decision. | OPEN — owner authorization/decision required |
| SEC-06 | LOW | FAIL | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:305>) RegisterIn/ResetPasswordIn/hash_password | RESET-30; Actual current model+bcrypt4.1.3 check accepts distinct long inputs above72UTF-8bytes that authenticate interchangeably. Requires an accepted long password;no production credential collision or account takeover was attempted. Existing compatibility concerns require a considered migration/password policy. | OPEN — owner authorization/decision required |
| SEC-07 | LOW | BLOCKED | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4990>) create_restaurant_payment_intent/verify_grocery_payment/refund helpers | SOURCE pattern;no latency/load exercise; Synchronous requests calls run inside async handlers;provider requests use explicit timeouts. Provider latency/concurrency/SLO impact was not measured;no event-loop outage is claimed. | OPEN — owner authorization/decision required |
| SEC-08 | MEDIUM | BLOCKED | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5362>) razorpay_webhook/event_payload | SOURCE pattern;actual ingress size controls unavailable; Configured webhook reads full request.body and computes HMAC before event_payload enforces1MiB. The standalone verified_event helper bounds size first,but this endpoint does not call it. Missing payment configuration returns503 before buffering. Actual proxy/server body caps are unknown;no oversized request or load test performed. | OPEN — owner authorization/decision required |
| SEC-09 | MEDIUM | FAIL | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3877>) admin_update_user_role | test_concurrent_cross_demotion_preserves_at_least_one_admin; Actual function body with synthetic in-memory collections and a deterministic count barrier accepts two cross-demotions;remaining_admins=0. Existing own-session demotion rejection passes. Two already privileged admins and concurrent cross-demotion are prerequisites. This is model-double execution of an observed source race,not a real Mongo race,customer privilege escalation or production lockout. | OPEN — owner authorization/decision required |

### SEC-01 — HIGH — OPEN

Affected symbols: `reset_password/forgot_password/_send_password_reset_email`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>).

Evidence: Actual AST-extracted functions with real Motor/Mongo on a unique retained local database:both same-token consumers accepted under a controlled read barrier;injected token-marker write failure left a changed password and unused token,then accepted retry.

Preconditions and limits: An existing account and unused/unexpired valid synthetic token;deliberately forced concurrent read or post-password-write failure. No arbitrary unauthenticated takeover or deployed-account exploit is claimed.

Minimal proposed correction / next evidence: Atomically claim the active token and update the user in the same existing transaction/session;check matched user count;ensure rollback and safe retry. Keep existing token-expiry/used/hash checks and API behavior. Owner authorization required. RESET-18 missing-user false success and RESET-10 invalid SMTP_PORT cleanup are LOW subissues within this recovery finding,not extra numbered vulnerabilities.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-02 — MEDIUM — OPEN

Affected symbols: `create_access_token/get_current_user_optional/reset_password`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:250>).

Evidence: Actual local Mongo/JWT execution accepted a pre-reset access JWT after a successful password reset.

Preconditions and limits: Requires possession of a still-valid prior JWT. Current DB user/role lookup,signature/type/expiry and deleted-account checks still apply. The owner must define relevant recovery/logout-all revocation policy.

Minimal proposed correction / next evidence: After owner policy approval,introduce a server-side session/password version or equivalent cutoff and verify it during authentication;include reset/logout revocation semantics. Do not change the approved session policy implicitly.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-03 — MEDIUM — OPEN

Affected symbols: `_client_ip/_rate_keys`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:819>).

Evidence: Source and helper observation select the first X-Forwarded-For value without an in-function trusted-proxy boundary.

Preconditions and limits: Actual bypass depends on exposed direct ingress or an unsanitized proxy;production proxy trust/sanitization was not examined. Helper observation is not a deployed bypass proof.

Minimal proposed correction / next evidence: Obtain authorized ingress evidence;define trusted proxies and use a trustworthy client address at that boundary. No spoofing attack or source correction performed.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-04 — MEDIUM — OPEN

Affected symbols: `_check_auth_rate_limit/_record_auth_attempt/_enforce_auth_rate_limit`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:833>).

Evidence: Real local Mongo scheduling test starts the subject count at4 for cap5;two concurrent checks accept and final count is6. Sequential cap checks pass.

Preconditions and limits: Both requests read before increments;observed local overshoot is2accepts at the one remaining slot. No load/capacity outage or unlimited-bypass claim.

Minimal proposed correction / next evidence: Use an atomic limit reservation/counter update consistent with existing window semantics and preserve both subject/IP protections;authorize source change first.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-05 — MEDIUM — OPEN

Affected symbols: `create_status_check/list_status_checks`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:687>).

Evidence: Anonymous diagnostic POST inserts a client_name;shared GET feed has a1000limit. No length/auth/rate dependency appears in these route declarations.

Preconditions and limits: Intended audience and effective edge caps are unknown;no diagnostic abuse/load test was run. Public intended policy requires owner decision.

Minimal proposed correction / next evidence: Owner decides diagnostic exposure;then authorize role/size/retention/rate safeguards appropriate to that policy. Do not silently remove legacy functionality.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-06 — LOW — OPEN

Affected symbols: `RegisterIn/ResetPasswordIn/hash_password`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:305>).

Evidence: Actual current model+bcrypt4.1.3 check accepts distinct long inputs above72UTF-8bytes that authenticate interchangeably.

Preconditions and limits: Requires an accepted long password;no production credential collision or account takeover was attempted. Existing compatibility concerns require a considered migration/password policy.

Minimal proposed correction / next evidence: Approve a byte-aware bound or compatible prehash/versioned password approach;retain existing hashes and avoid silently invalidating users. Add boundary/migration checks after authorization.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-07 — LOW — OPEN

Affected symbols: `create_restaurant_payment_intent/verify_grocery_payment/refund helpers`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4990>).

Evidence: Synchronous requests calls run inside async handlers;provider requests use explicit timeouts.

Preconditions and limits: Provider latency/concurrency/SLO impact was not measured;no event-loop outage is claimed.

Minimal proposed correction / next evidence: Authorize an existing-architecture compatible async I/O or bounded offload change,then isolated latency/concurrency verification;no new provider calls now.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-08 — MEDIUM — OPEN

Affected symbols: `razorpay_webhook/event_payload`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5362>).

Evidence: Configured webhook reads full request.body and computes HMAC before event_payload enforces1MiB. The standalone verified_event helper bounds size first,but this endpoint does not call it.

Preconditions and limits: Missing payment configuration returns503 before buffering. Actual proxy/server body caps are unknown;no oversized request or load test performed.

Minimal proposed correction / next evidence: Obtain ingress body-limit evidence and authorize bounded transport/application reads before untrusted full allocation/HMAC;preserve raw-body signature verification and retry-safe event handling.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

### SEC-09 — MEDIUM — OPEN

Affected symbols: `admin_update_user_role`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3877>).

Evidence: Actual function body with synthetic in-memory collections and a deterministic count barrier accepts two cross-demotions;remaining_admins=0. Existing own-session demotion rejection passes.

Preconditions and limits: Two already privileged admins and concurrent cross-demotion are prerequisites. This is model-double execution of an observed source race,not a real Mongo race,customer privilege escalation or production lockout.

Minimal proposed correction / next evidence: Serialize admin-role changes through a shared guard/version CAS within the transaction (or equivalent sound serialization),recount and update under that serialization. Merely putting count+updates of different user documents in separate snapshot transactions may allow write skew. Owner authorization and dedicated real-Mongo verification are required.

Protected source modification: **NOT AUTHORIZED / NOT PERFORMED**.

## Twenty-one security review areas

Every row below has one status for its **stated bounded assertion**. A PASS for a selected helper/model/source check does not certify the entire product area. The payment/refund scope is split into two rows for clarity;no roadmap task is invented. BLOCKED rows require missing external configuration,policy or infrastructure evidence. All areas were examined at the available evidence level;production-wide acceptance was not achieved.

| ID / area | Status | Bounded assertion | Evidence / findings | Limitations |
| --- | --- | --- | --- | --- |
| AS-01 Customer accounts | FAIL | Recovery integrity,JWT recovery revocation and long-password invariants failed;normal invalid/expired/type checks passed. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:854>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:889>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>) SEC-01,SEC-02,SEC-06 | Real isolated functions/Mongo plus actual-model/bcrypt unit cases;no customer/production accounts. |
| AS-02 Seller accounts | PASS | Both shop and restaurant owner guards reject wrong roles/owners in the12-case isolated guard matrix. Role and owner are separate conditions. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1211>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4636>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2939>)  | Selected guard function execution;not all seller HTTP/UI lifecycle branches. |
| AS-03 Admin permissions | FAIL | Admin-only dependency rejects3other roles;self-demotion rejection passes,but cross-demotion last-admin invariant fails. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:291>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3877>) SEC-09 | Actual dependency/helper bodies with synthetic users/doubles;no real administrator operations. |
| AS-04 Delivery partner permissions | PASS | Public application projection excludes encrypted/raw PII;decision reason redacts fixture identity/phone shapes. Approval checks and audit writes are source-present. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6751>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6740>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6941>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6999>)  | Selected projection/redaction runtime units plus source review;identity provider and full operational delivery lifecycle remain unverified. |
| AS-05 API authentication | FAIL | Wrong signatures,expired/non-access JWT and missing user are rejected;old valid JWT survives password reset. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:250>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:268>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:284>) SEC-02 | Current isolated Mongo/JWT cases;not production token custody or all middleware. |
| AS-06 API authorization and IDOR boundaries | PASS | Selected role/owner/tracking helper checks enforce current persisted role and current shop/restaurant ownership;the completed179-route dependency inventory was reused. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:291>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1211>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3607>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4636>)  | 49passing helper/model cases include14tracking-role/owner combinations;no exhaustive all179endpoint penetration claim. |
| AS-07 Pricing manipulation | PASS | Actual ProductIn rejects nonfinite/nonpositive price inputs;Grocery resolves current server product lines and ignores client prices;Restaurant rebuilds totals from menu. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:478>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3080>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3236>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4851>)  | Model checks and source trace;source-bound broader local/live regression evidence is separate. |
| AS-08 Cart manipulation | PASS | Actual QuoteLineIn rejects invalid quantity bounds;Restaurant cart is keyed by current user and stores validated identifiers/quantity,not trusted prices. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:575>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4812>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4831>)  | Selected input units plus source inspection;no complete rendered UI/browser cart acceptance. |
| AS-09 Order manipulation | PASS | Source checks quote scope,expiry,fulfilment,shop,price/stock snapshot and idempotency;ownership gates protect authenticated details/tracking/cancellation. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3236>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3522>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3634>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3643>)  | Source declarations and completed local/live regression artifacts;not all policy/error branches. |
| AS-10 Inventory manipulation | PASS | Conditional stock decrement requires available/current sufficient stock and is passed the checkout transaction session;fail-closed transaction helper is source-present. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3217>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3331>)  | Source review plus backend-live transaction suite;does not prove production inventory or restore correctness. |
| AS-11 Payment manipulation | BLOCKED | Server validates payment/order link,signature,captured status,exact INR amount and consistent local commit. Actual provider credentials/delivery are absent. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5041>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5169>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5362>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6470>)  | Local provider-mocked/transaction tests are separate PASS evidence;genuine Razorpay TEST acceptance remains BLOCKED. |
| AS-12 Refund manipulation | BLOCKED | Admin-only eligibility and transactionally claimed request keys avoid blind retries;COD eligibility and provider reconciliation rules are source-present. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5670>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6186>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6254>) SEC-07 | Local mocks/real Mongo are not real provider refund creation/status/settlement evidence. |
| AS-13 Upload validation | PASS | Image handler authenticates,reads at most5MiB+1,and requires matching JPEG/PNG/GIF/WebP signature before storage;current offline guard tests are present. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1142>)  | Bounded allocation/signature source+offline tests;not full image decoding,malware scanning or object-store delivery. |
| AS-14 File access | BLOCKED | Public serve route rejects .. and requires an active DB file record before using internal storage credentials. Public-image versus private-file policy needs explicit scope. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1185>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:161>)  | No object-store/private-file/provider requests;do not infer an IDOR solely from an intentional public image route. |
| AS-15 Sensitive customer data | PASS | Selected doc/public/projection helpers strip known password/actor/encrypted PIIfields;addresses and order reads use current user/owner conditions. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:201>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:215>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4775>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6920>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6927>)  | Synthetic redaction/ownership tests plus source;not exhaustive every response or production data-access certification. |
| AS-16 Logging | PASS | Isolated SMTP failure cases capture no raw reset token or recipient email;other reviewed handlers generally log exception type or bounded generic payment mismatch. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1087>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6888>)  | RESET-09proves only selected failure logs;production logs/retention/access and every route error remain unverified. |
| AS-17 Session management | FAIL | Current DB roles/deleted-account checks are retained,but relevant pre-reset JWT remains accepted after reset. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:250>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:268>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>) SEC-02 | Dedicated isolated reset/JWT case;owner recovery/logout-all session policy still required. |
| AS-18 Rate limiting and abuse protection | FAIL | Sequential limits pass;controlled concurrent subject checks exceed cap. First forwarded header observation does not establish ingress trust. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:819>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:833>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:841>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:847>) SEC-03,SEC-04,SEC-05 | Actual local counter-race proof plus source;no abuse/load attack on external services. |
| AS-19 Fraud prevention | PASS | Source uses server-derived totals,scoped order idempotency,unique indexes and provider identity/amount reconciliation;referral decisions stay admin protected. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:960>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1014>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3236>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5041>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6254>)  | Bounded source/local regression review;no real fraud/chargeback/provider operational certification. |
| AS-20 Configuration and secrets | BLOCKED | CORS production wildcard rejection,JWT startup requirements and explicit Razorpay environment/key-mode guards are source-present;actual deployed bindings and secret custody are not audited. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5813>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:7030>)  | Read templates/source only;no production secrets,credential values,deployments or billing operations. |
| AS-21 Database access and infrastructure | BLOCKED | Current loopback rs0 metadata is documented separately;application transactions/indexes are source-present. Actual production users/grants/firewalls/TLS/backup controls remain unavailable. | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5813>); [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5840>)  | Read-only local metadata and isolated test DB evidence;no production DB records,modifications or recovery test. |

## Cross-workstream evidence and release boundaries

- Current safe regression evidence is in [backend-offline.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-offline.xml>) and [backend-live.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-live.xml>);source/command/isolation records are owned by the regression workstream. The local ASGI/Mongo payment tests at [backend-local-payments.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-local-payments.xml>) use provider mocks and cannot establish real Razorpay TEST delivery/refund settlement.
- Dedicated recovery evidence is [password-reset-results-v2.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-results-v2.json>). SEC-01 is now **locally validated FAIL / OPEN — REMEDIATION AUTHORIZATION REQUIRED**,not merely the previous source-only validation block. Controlled scheduling and injected failure wrappers expose possible source interleavings while retaining real Motor writes. Real customer impact,SMTP delivery and production ingress are not inferred.
- Real Android/iOS build/device evidence and actual Razorpay TEST payment/webhook/refund acceptance remain BLOCKED as detailed in [ANDROID_IOS_NATIVE_VALIDATION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/ANDROID_IOS_NATIVE_VALIDATION_REPORT.md>) and [RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md>).
- Current loopback DB metadata is in [db-metadata-current.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/db-metadata-current.json>):metadata is not proof of production DB grants,TLS,record integrity or recoverability. This finalizer queried no database.
- No production credentials,customer records,external systems,paid resources or real payment/refund operations were used. No source/configuration/dependency edits or installs were made. The final preservation workstream must recheck all protected hashes and Git status after all outputs are saved.

## Owner decisions and precise next action

KeepTask1 **REVIEW PENDING**. The owner must review the confirmed HIGH recovery-atomicity failures and authorize minimal protected-source corrections before implementation. Separate owner policy decisions remain for session revocation,forwarded-proxy trust,diagnostic exposure,long-password compatibility and public/private file scope. SEC-09 requires a serialized admin-role correction and later real-Mongo concurrency acceptance;wrapping count+different-user updates in independent snapshot transactions alone is insufficient because of write skew.

No finding is closed by the presence of a report. No correction,Task2,commit,push or deployment is started here. The exact safe next action is personal owner review of the canonical9-risk register and a separate,explicit correction/verification authorization. Evidence-first disposition remains **REVIEW PENDING**.

## Current independent reproduction addendum — 2026-11-19T21:25:39.572920+05:30

The root workflow independently reproduced the unchanged50-case broad suite to close the current-command provenance gap. The exact invocation,cwd,start/end times,source/test SHA-256 and exit status are now preserved in [broad-security-reproduction.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduction.json>) and the executed [reproduce-broad-security.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/reproduce-broad-security.py>) runner. Current results are **49PASS /1FAIL /0ERROR /0SKIPPED**,exit1;the same last-admin invariant remains unsuppressed. Evidence: [broad-security-reproduced.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduced.xml>) and [broad-security-reproduced.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduced.log>).

The source SHA-256 before and after is `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db`;the test SHA-256 is `8e02180373829fd4c09e57c3cdd64f9f5483bb86fc186ef15894dc91acdd73ea`. The receipt records `2026-11-19T15:54:41.894482+00:00` to `2026-11-19T15:54:42.949221+00:00`. All socket connections were denied by the test fixture;no server import,real DB,provider or production call was involved. The security finalizer did not run these tests again.

Count **one canonical50-case outcome** only;do not add the reproduced50cases to the saved v2 or initial attempt as extra coverage. The original v2 full shell command remains missing historically. This fresh,fully bound reproduction does not backdate or authenticate that older invocation;the earlier provenance limitation is preserved. Security dispositions and the9-finding severity denominator are unchanged. Source/configuration fixes remain unauthorized and unperformed. Task1 remains **REVIEW PENDING**.
