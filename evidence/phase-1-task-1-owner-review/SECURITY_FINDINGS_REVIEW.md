# Security Findings Owner Review

Review time: 2026-11-18T07:17:41.372443-08:00 (UTC−08). Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`: all match the expected identity. Application source is `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`, outside the Git checkout.

**Final decision: REVIEW PENDING.** This is an evidence review for the owner, not personal owner approval, task closure or production readiness. Original reports, manifests, checkpoints, ZIP, source and configuration are preserved. Only this NEW review folder was written. No application tests, DB queries/writes, browser actions, provider calls, attacks, installs or service changes were performed in this review. Task 2 and implementation were not started.

## Assessment rules

All eight reported source control patterns are VERIFIED. Reported severity arithmetic is correct: one HIGH, five MEDIUM and two LOW. Severity, deployment exposure, runtime impact and closure are PARTIALLY VERIFIED. No successful exploit, account takeover, load failure, provider effect or remediation test was established. HIGH SEC-01 remains OPEN. No new vulnerability count is inferred from documentation gaps.

## SEC-01 — reported HIGH — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:13`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123`; symbols: `reset_password`.
- Evidence: Token find_one,users.update_one,password_resets.update_one are sequential and not under a shared transaction/CAS token claim.
- Potential impact described by the original report (not demonstrated by this review): Concurrent reuse or a failure between writes can permit a token to remain usable or competing resets to overwrite the password. This is a source-derived race/failure concern;no exploit or reset was attempted.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: High priority is defensible for account recovery integrity;production attackability and token/provider availability remain UNVERIFIED. A valid token or access to its flow is still a prerequisite;no arbitrary unauthenticated takeover demonstrated.
- Review priority: P1 — owner security decision first.
- Further investigation/decision: Keep OPEN;owner decision plus isolated concurrency/failure evidence required. Incorrectly specific related-test pointer: test_functional_blockers_regression.py contains no password-reset test.
- No fix, exploitation, credential creation or application test was performed.

## SEC-02 — reported MEDIUM — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:22`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:250`; symbols: `create_access_token/get_current_user_optional/reset_password`.
- Evidence: 7-day JWT;no jti/password version/session revocation check in DB-backed authentication;reset only updates password_hash.
- Potential impact described by the original report (not demonstrated by this review): A previously obtained valid token can retain access until expiry after a password change,unless the account is removed or other checks deny it. Native/client logout alone does not revoke a copied token.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Medium justified subject to owner session policy;DB role lookup,deleted-account rejection and expiry still provide controls.
- Review priority: P2 — session policy.
- Further investigation/decision: Need logout-all/reset revocation acceptance policy and approved isolated tests;frontend storage logout tests do not prove server revocation.
- No fix, exploitation, credential creation or application test was performed.

## SEC-03 — reported MEDIUM — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:31`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:819`; symbols: `_client_ip/_rate_keys`.
- Evidence: _client_ip unconditionally takes first X-Forwarded-For value.
- Potential impact described by the original report (not demonstrated by this review): If directly reachable or behind an unsanitized proxy,IP-based registration/reset/login throttles can be evaded. Email/subject counters still provide separate protection where used.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Medium conditional on ingress trust/sanitization;subject/email counters remain independent.
- Review priority: P2 — deployment/proxy trust.
- Further investigation/decision: Actual trusted-proxy deployment config and direct-access exposure needed. No spoofed request attempted.
- No fix, exploitation, credential creation or application test was performed.

## SEC-04 — reported MEDIUM — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:40`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:833`; symbols: `_check_auth_rate_limit/_record_auth_attempt/login`.
- Evidence: Limit read and later atomic increment are separate operations;failed login increments after password check.
- Potential impact described by the original report (not demonstrated by this review): Burst concurrency may exceed the intended per-window limit. No concurrency/abuse attack was run.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Medium for bursts is plausible but excess rate/capacity impact unmeasured.
- Review priority: P2 — rate-limit acceptance.
- Further investigation/decision: Need approved isolated burst/race coverage;do not infer no limits at all.
- No fix, exploitation, credential creation or application test was performed.

## SEC-05 — reported MEDIUM — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:49`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:687`; symbols: `create_status_check/list_status_checks`.
- Evidence: Anonymous POST inserts client_name with no length bound/auth/rate dependency;GET shared feed1000limit.
- Potential impact described by the original report (not demonstrated by this review): Untrusted callers can create diagnostic data/storage load and retrieve the shared diagnostic feed. This is legacy behavior,not assumed to be intentional public operational policy.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Medium conditional on public intended policy/edge limits;storage/metrics abuse not exploitation tested.
- Review priority: P2 — legacy endpoint policy.
- Further investigation/decision: Owner must classify diagnostic endpoint intended audience and ingress caps before closure.
- No fix, exploitation, credential creation or application test was performed.

## SEC-06 — reported LOW — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:58`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:305`; symbols: `RegisterIn/hash_password/ResetPasswordIn`.
- Evidence: Password schemas permit128characters;UTF8 bytes passed directly to pinned bcrypt4.1.3;no72byte guard.
- Potential impact described by the original report (not demonstrated by this review): bcrypt byte truncation/compatibility can make distinct long inputs equivalent or otherwise cause password-contract ambiguity. Exact runtime behavior was not exercised;do not report a tested credential collision.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Low is a defensible provisional policy/compatibility item;byte truncation collision not freshly demonstrated.
- Review priority: P3 — byte-aware password compatibility.
- Further investigation/decision: Need deployed library behavior evidence and reviewed compatible password policy;no salts/passwords created.
- No fix, exploitation, credential creation or application test was performed.

## SEC-07 — reported LOW — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:67`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4990`; symbols: `create_restaurant_payment_intent/verify_grocery_payment`.
- Evidence: Sync requests.post/get run directly inside async handlers with15second timeouts.
- Potential impact described by the original report (not demonstrated by this review): Slow provider responses can occupy the event loop and reduce availability;this is a source-level performance/availability concern,not a measured outage.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Low availability concern justified;concurrency/provider latency/SLO impact unmeasured.
- Review priority: P3 — availability/load scope.
- Further investigation/decision: Need async/event-loop/load evidence under separate safe scope,not new provider calls now.
- No fix, exploitation, credential creation or application test was performed.

## SEC-08 — reported MEDIUM — OPEN

- Original report: `/workspace/come-in-current/evidence/phase-1-task-1-audit/PHASE_1_TASK_1_SECURITY_FINDINGS.md:76`.
- Source: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5362`; symbols: `razorpay_webhook/event_payload`.
- Evidence: request.body buffers fully;HMAC computed before event_payload1MiB size check.
- Potential impact described by the original report (not demonstrated by this review): When the provider route is configured,oversized unauthenticated bodies can consume buffering/HMAC resources before rejection. This was not load-tested and no large request was sent.
- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.
- Severity and potential impact: Medium conditional on upstream limits and route configured;missing config returns503 before buffering.
- Review priority: P2 — ingress and request-size controls.
- Further investigation/decision: Need ingress maximum body evidence or isolated transport-cap review;no oversized requests sent.
- No fix, exploitation, credential creation or application test was performed.

## Additional review boundaries

- **Wrong related-test pointer:** original Security report line 20 names a file with no reset coverage. `test_restaurant_api_contract.py:33–34` only checks route existence. Do not infer atomic token consumption, rollback or revocation coverage.
- **GET mutation omissions:** `server.py:942–946` inserts referral-link events; `:900–905` calls a helper that can persist a code. Add a side-effect map before any future “read-only GET” probes. This is a safety/coverage omission, not a new exploited vulnerability.
- **Dynamic return target:** `auth.tsx:64` passes `next` to the router. The selected literal checks do not establish a safe allowlist or an exploit; no navigation attack was attempted.
- **Deployment mitigations:** actual proxy sanitization, body caps, edge rate limits, DB grants, TLS/CORS, secret handling and logging are not validated by local source.
- **Coverage is not exhaustive security acceptance:** registration/dependency counts do not exercise every ownership branch or response field. No full IDOR/XSS/error/log exposure test was performed. Such work needs separate scope and approval.
