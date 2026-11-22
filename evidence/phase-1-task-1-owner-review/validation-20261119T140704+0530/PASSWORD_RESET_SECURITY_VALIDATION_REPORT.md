# Password Reset Security Validation Report

COME-IN — Phase1 Task1 owner validation. Recorded 2026-11-19T21:21:15.123617+05:30 (Asia/Kolkata).

Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. Actual application `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`. This is newly authorized isolated validation, not Task2 or remediation. Protected application source/configuration/original reports/checkpoints were not edited.

**Result: 30 freshly executed cases —23 PASS,7 FAIL,0 ERROR,0 SKIPPED. Exit1.** Two PASS cases (RESET-28/29) are explicitly observation checks; the other28 security/input/control assertions total21 PASS/7 FAIL. Seven failed assertions map to existing SEC-01/02/04/06 and two LOW SEC-01 subissues. No new canonical security identifier is created. Existing SEC-03 ingress exposure remains unverified. SEC-01 HIGH stays **OPEN — locally confirmed atomicity failure**, replacing its earlier source-only/local-validation-blocked boundary for these specific scenarios. No production or external account takeover is claimed.

## Executed scope and safety

The runner compiled the original AST nodes of21 actual functions/classes and5 actual constants from `backend/server.py`. Only API route decorators were removed; function/model bodies were not rewritten. `compile(..., dont_inherit=True)` preserves the original file's non-future annotation semantics. Actual Pydantic, bcrypt12, PyJWT, ObjectId, Motor and PyMongo are used. Function calls use real Starlette Request objects without HTTP transport; FastAPI routing/dependency injection/middleware/startup is not exercised. Source SHA-256 before and after: `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db`.

Real local MongoDB 7.0.45 was `rs0` PRIMARY at `127.0.0.1:27018`. Corrected run database `comein_reset_validation_20261119t154740z_b138456219` is retained:20 synthetic users,15 reset records,29 rate counters. First attempt DB `comein_reset_validation_20261119t154652z_30b1113b8a` is also retained. No existing application/production DB, schema or record was read/written by this runner. No DB/collection drop/reset. The actual forgot function's deletion applies only to its own newly created synthetic accounts inside this unique DB.

Environment variables are an isolated synthetic dictionary supplied only to the extracted functions; no `.env` or process production credentials are loaded. JWT fixture secret/raw reset tokens exist only in memory. Database stores fixture password hashes and token hashes. SMTP email construction executes the actual helper, with its SMTP transport replaced by OfflineSMTP. No real email/provider request/payment/refund occurs. Process socket connections allow only loopback hosts. Test artifacts omit raw tokens, JWTs, passwords, SMTP/JWT secrets and message bodies; the runner contains clearly synthetic input strings, never actual credentials.

Controlled collection wrappers force both real token reads to finish before either reset proceeds, and inject a token-mark failure after the preceding real user write. These preserve application code and expose possible schedules; they are not a statistical concurrency/load test or a deployed HTTP exploit.

## Commands and runtime

Working directory: `/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530`.

```sh
/workspace/come-in-tools/py311/bin/python -B validate_password_reset.py > password-reset-run.log 2>&1
/workspace/come-in-tools/py311/bin/python -B validate_password_reset.py > password-reset-run-v2.log 2>&1
```

First attempt:15 PASS,6 FAIL,9 ERROR,0 SKIP; exit1. Nine `PydanticUserError`s were a harness-only annotation issue, not product failures. No attempt1 log/JSON/JUnit was overwritten. The compile flag was corrected to match actual source semantics, then the same30 cases rerun because these errors prevented forgot-flow coverage. Final corrected attempt:23 PASS,7 FAIL,0 ERROR,0 SKIP; exit1. All seven real failures remain; no assertion/rule was suppressed. The first script hash was not captured before the harness correction; final executed script and all saved artifacts are hashed separately.

Python `3.11.18 (main, Oct 26 2026, 14:05:07) [Clang 23.1.3 ]` at `/workspace/come-in-tools/py311/bin/python`. Installed versions: `{"PyJWT": "2.15.1", "bcrypt": "4.1.3", "fastapi": "0.110.1", "motor": "3.7.1", "pydantic": "2.14.3", "pymongo": "4.18.2"}`. No package installation or service restart by this workstream. Parent started the retained local Mongo and raised its inherited nofile limit before this runner; this report does not claim a new Mongo installation.

Final run UTC interval: `2026-11-19T15:47:42.074742+00:00` to `2026-11-19T15:47:51.316681+00:00`. Folder name remains the earlier session identifier; it is not the actual test timestamp.

## Every freshly executed case

| Case | Result | Intended invariant / observation | Scope note |
| --- | --- | --- | --- |
| RESET-01 | PASS | Forgot input rejects invalid email |  |
| RESET-02 | PASS | Reset input rejects a token shorter than 32 characters |  |
| RESET-03 | PASS | Reset input rejects a password shorter than eight characters |  |
| RESET-04 | PASS | Reset input rejects token/password values above declared maxima |  |
| RESET-05 | PASS | Known and unknown forgot calls share a generic response and reveal no raw token |  |
| RESET-06 | PASS | Forgot generates a random token, stores SHA256 only, and applies 30-minute expiry |  |
| RESET-07 | PASS | Sequential forgot issuance invalidates an older token |  |
| RESET-08 | PASS | Missing SMTP configuration leaves no newly usable reset token |  |
| RESET-09 | PASS | SMTP failure is cleaned up and logs no raw reset token or email |  |
| RESET-10 | FAIL | Invalid SMTP port fails safely with generic response and token cleanup |  |
| RESET-11 | PASS | A valid token updates password and is consumed |  |
| RESET-12 | PASS | Expired tokens are rejected even before TTL deletion |  |
| RESET-13 | PASS | An invalid random token cannot change password |  |
| RESET-14 | PASS | An already used token cannot change password |  |
| RESET-15 | PASS | Sequential replay is rejected and does not overwrite the first reset |  |
| RESET-16 | FAIL | At most one concurrent request can consume the same reset token |  |
| RESET-17 | FAIL | A failure between password write and token write leaves no partial state or reusable token |  |
| RESET-18 | FAIL | Reset cannot report success for a missing target account |  |
| RESET-19 | FAIL | Password reset invalidates a previously issued access JWT |  |
| RESET-20 | PASS | Invalid-signature access JWT is rejected |  |
| RESET-21 | PASS | Expired access JWT is rejected |  |
| RESET-22 | PASS | Non-access JWT type is rejected |  |
| RESET-23 | PASS | JWT for a missing account is rejected |  |
| RESET-24 | PASS | Authorization uses current persisted role and strips password hash |  |
| RESET-25 | PASS | Forgot subject limit accepts five attempts then rejects the sixth |  |
| RESET-26 | PASS | Reset IP limit accepts 50 attempts then rejects the next |  |
| RESET-27 | FAIL | Concurrent rate-limit checks cannot overshoot the configured subject limit |  |
| RESET-28 | PASS | Concurrent forgot issuance is measured without inventing an owner token-count policy | Observation only; not a security acceptance gate |
| RESET-29 | PASS | Direct forwarded-IP behavior is measured; trusted-ingress policy remains external | Observation only; not a security acceptance gate |
| RESET-30 | FAIL | Distinct accepted long passwords must not authenticate interchangeably |  |

## Failed assertions, severity and proposed corrections

### RESET-10 — SEC-01 / LOW configuration subissue

Source: `server.py:1087–1104,1112–1119` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

SMTP_PORT integer conversion occurs before the helper try block. Invalid local configuration raises ValueError out of forgot_password and bypasses the delivered=False cleanup, leaving one unused token hash. This does not prove the unknown token was disclosed or a deployed service has malformed settings.

Recorded sanitized observation:

```json
{
  "configuration_exception_escaped": true,
  "active_undelivered_tokens": 1
}
```

Minimal proposed correction, **not implemented**: Validate SMTP port safely inside the guarded configuration/delivery path; ensure undelivered tokens are invalidated on every failure. Validate configuration without printing values.

### RESET-16 — SEC-01 / HIGH OPEN

Source: `server.py:1123–1129` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

Both real MongoDB find_one reads observed the same unused, unexpired token; the controlled barrier then released both actual reset function bodies. Both returned reset=True. This proves a possible local interleaving, not an external-account takeover.

Recorded sanitized observation:

```json
{
  "accepted_resets": 2,
  "matching_valid_reads": 2,
  "token_used_afterwards": true,
  "controlled_interleaving": "Both actual MongoDB token reads finish before either function resumes"
}
```

Minimal proposed correction, **not implemented**: Use the existing transaction architecture for a conditional unused/unexpired token claim and a checked user-password update in the same transaction; reject a losing claim. Preserve retry/unknown-commit handling and add this deterministic race case to an approved regression suite.

### RESET-17 — SEC-01 / HIGH OPEN

Source: `server.py:1128–1130` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

The actual users.update_one committed. A collection-boundary fault then raised before the actual token-used update could execute. The password was changed, token still unused, and retrying the same token succeeded with another password. No automatic rollback occurred.

Recorded sanitized observation:

```json
{
  "injected_exception_escaped": true,
  "password_changed_before_failure": true,
  "token_unused_after_failure": true,
  "same_token_retry_accepted": true,
  "fault_scope": "Token-mark update raises before execution; preceding real users.update_one committed"
}
```

Minimal proposed correction, **not implemented**: Make password change and token consumption one durable transaction with checked matched/modified results. Do not merely consume the token outside a transaction before updating the password.

### RESET-18 — SEC-01 / LOW consistency subissue

Source: `server.py:1127–1130;_object_id_or_404:4624–4628` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

An isolated token referring to a syntactically valid but absent ObjectId was consumed and the function returned reset=True although no user matched. The ObjectId parser validates syntax, not account existence. No real account was deleted for this test.

Recorded sanitized observation:

```json
{
  "success_reported": true,
  "token_consumed": true
}
```

Minimal proposed correction, **not implemented**: Check the target user update matched exactly one authorized token-bound account and fail consistently within the same transaction otherwise.

### RESET-19 — SEC-02 / MEDIUM OPEN

Source: `server.py:250–281,1123–1130` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

An actual PyJWT access token minted before the reset remained accepted by actual get_current_user_optional after the reset. Invalid signatures/expiry/type and missing-user rejection separately passed. This is a failed explicit recovery-revocation invariant; the existing seven-day JWT design and final revocation policy still require owner disposition.

Recorded sanitized observation:

```json
{
  "pre_reset_jwt_still_accepted": true,
  "policy": "Security recovery revocation requirement; existing seven-day JWT design does not implement it"
}
```

Minimal proposed correction, **not implemented**: Agree on recovery/session-revocation policy, then use a server-checked session or token/password version and invalidate old sessions on reset while preserving persisted-role authorization.

### RESET-27 — SEC-04 / MEDIUM OPEN

Source: `server.py:833–850` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

A subject counter began at4 with cap5. Two controlled actual MongoDB reads both passed before the increment stage. Both requests were accepted and the persisted counter became6. Serial limit enforcement passed separately. This is a bounded local concurrency test, not an external abuse/load test.

Recorded sanitized observation:

```json
{
  "initial_subject_count": 4,
  "concurrent_allowed": 2,
  "final_subject_count": 6,
  "configured_subject_limit": 5
}
```

Minimal proposed correction, **not implemented**: Use an atomic capped shared counter with correct upsert/conflict behavior and an explicit multi-key rejection policy; preserve hashed subject keys and expiry cleanup.

### RESET-30 — SEC-06 / LOW OPEN

Source: `server.py:233–243,1083–1085;backend/requirements.txt:11` in [server.py](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py).

The actual reset Pydantic model accepted both distinct passwords above72 UTF-8 bytes. bcrypt4.1.3 hash_password/verify_password authenticated the second suffix against the first hash because their first72 bytes match. These are synthetic test inputs, not actual credentials or an exploited user account.

Recorded sanitized observation:

```json
{
  "model_accepted_both": true,
  "utf8_bytes_exceed_72": true,
  "distinct_suffix_authenticates": true
}
```

Minimal proposed correction, **not implemented**: Choose an explicit UTF-8 byte-aware length policy or reviewed versioned long-password strategy. Preserve compatibility with stored credentials; do not silently change hashing or truncate inputs.


## Full recovery flow and evidence boundary

1. Actual `ForgotPasswordIn` requires EmailStr (`server.py:1080–1081`), while ResetPasswordIn bounds token32–256 and password8–128 characters (`1083–1085`). Bad-email/length tests pass; byte-aware long-password semantics fail separately.
2. Actual forgot rate control runs before user lookup (`1107–1110`;helpers`813–850`). Email is lowercased/trimmed, unknown accounts receive the same response. Serial subject/IP boundaries and hashed subject keys pass; concurrent subject counting fails its strict cap invariant.
3. Actual `secrets.token_urlsafe(36)` is used. Only SHA256 is stored with unused state and30-minute expiry; prior per-user reset records are deleted (`1112–1114`). Generation/expiry/hash-only storage and sequential invalidation pass.
4. Actual email helper builds the token URL, calls STARTTLS then send via a transport stub (`1087–1104`). Missing configuration and synthetic STARTTLS failure cleanup pass. Malformed SMTP_PORT is outside try and fails safely-cleaned-up expectation. No actual delivery, recipient identity, SMTP TLS certificate, reset URL deployment or production email configuration is verified.
5. Reset hashes the submitted token and requires unused/unexpired lookup (`1123–1127`). Invalid, expired and already-used tokens reject without password writes. A normal reset and subsequent sequential replay handling pass.
6. Password write then token marking (`1128–1130`) are distinct awaits. Both concurrent consumption and rollback/failure consistency fail against real Mongo. Missing-user update success reporting also fails. `ObjectId` syntax parsing (`4624–4628`) does not prove account existence.
7. JWT authentication verifies signature/type/expiry and reloads the user (`250–281`). Invalid tokens, missing users, persisted-role precedence, password-hash projection and admin role rejection pass. Old JWT acceptance after reset fails the explicit recovery-revocation invariant; final policy requires owner disposition.
8. Two concurrent forgot calls leave two active delivered-to-stub token hashes. This is a measured observation, not a failure invented from an unspecified one-active-token policy. Actual helper selects the first forwarded-IP value; no production proxy trust configuration or external bypass was tested.

## Historical evidence and unexecuted scope

Earlier `reset-flow-validation.json` and six final reports/checkpoint were read and hashed as input; their zero-runtime-test claims remain accurate for that earlier iteration. This new run supplies only the new bounded proof above. Existing source tests `test_restaurant_api_contract.py:32–39` check route existence only; `test_frontend_contracts.py:14–21` checks storage source strings; `test_shared_system_integration_contract.py:116–121` checks logout/role source strings. `test_functional_blockers_regression.py` has no located reset-specific coverage, so the original SEC-01 citation cannot be used as reset-atomicity evidence. None of these old tests was rerun by this workstream.

Previously reported full regression558PASS/6SKIP, TypeScript0 errors, ESLint0 errors/10 warnings and older provider/live results were **not rerun here**. This runner executes30 new cases, not the backend regression suite. Native builds/devices, real SMTP/provider payment/webhook/refund, deployed ingress/HTTPS/log sink and production account/DB behavior remain unverified or externally blocked; no source-bound local result is labeled a real provider/device acceptance PASS.

## Evidence files and stopping point

- [Final result JSON](/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-results-v2.json) — all30 outcomes, sanitized observations, original source segments/hashes, dependencies, input hashes and DB retention metadata.
- [Final JUnit](/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-junit-v2.xml) and [actual command output](/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-run-v2.log).
- [Executable runner](/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/validate_password_reset.py) and [execution provenance/hashes](/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-execution-provenance.json).
- Attempt1 JSON/JUnit/log remain beside these; they include the disclosed harness errors.

No test operation remains running or interrupted. Last completed operation: corrected source-bound30-case run and evidence generation, source hash equality verified. No source fix was implemented or authorized. Do not aggregate attempt1 with attempt2 as60 independent acceptance cases;30 final unique cases are the denominator. Do not count two SEC-01 scenarios/subissues as newly numbered risks.

Next precise action: parent consolidates these confirmed failures with the other Task1 validation evidence and verifies preservation. Owner must explicitly authorize scoped source remediation before any fix; then repeat only affected deterministic cases plus justified regression. Task1 remains **REVIEW PENDING**, and HIGH SEC-01 must not be closed from documentation or passing route tests. Task2 is not started. No production readiness or owner approval is claimed.
