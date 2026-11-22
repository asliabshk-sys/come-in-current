#!/usr/bin/env python3
"""Build NEW reset validation documentation from saved, executed results only."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json

OUT = Path(__file__).resolve().parent
data = json.loads((OUT / 'password-reset-results-v2.json').read_text())
first = json.loads((OUT / 'password-reset-results.json').read_text())
stamp = datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
source = Path(data['source_path'])
assert hashlib.sha256(source.read_bytes()).hexdigest() == data['source_sha256'] == data['source_sha256_after']

mapping = {
    'RESET-10': ('SEC-01 / LOW configuration subissue', 'server.py:1087–1104,1112–1119',
                 'SMTP_PORT integer conversion occurs before the helper try block. Invalid local configuration raises ValueError out of forgot_password and bypasses the delivered=False cleanup, leaving one unused token hash. This does not prove the unknown token was disclosed or a deployed service has malformed settings.',
                 'Validate SMTP port safely inside the guarded configuration/delivery path; ensure undelivered tokens are invalidated on every failure. Validate configuration without printing values.'),
    'RESET-16': ('SEC-01 / HIGH OPEN', 'server.py:1123–1129',
                 'Both real MongoDB find_one reads observed the same unused, unexpired token; the controlled barrier then released both actual reset function bodies. Both returned reset=True. This proves a possible local interleaving, not an external-account takeover.',
                 'Use the existing transaction architecture for a conditional unused/unexpired token claim and a checked user-password update in the same transaction; reject a losing claim. Preserve retry/unknown-commit handling and add this deterministic race case to an approved regression suite.'),
    'RESET-17': ('SEC-01 / HIGH OPEN', 'server.py:1128–1130',
                 'The actual users.update_one committed. A collection-boundary fault then raised before the actual token-used update could execute. The password was changed, token still unused, and retrying the same token succeeded with another password. No automatic rollback occurred.',
                 'Make password change and token consumption one durable transaction with checked matched/modified results. Do not merely consume the token outside a transaction before updating the password.'),
    'RESET-18': ('SEC-01 / LOW consistency subissue', 'server.py:1127–1130;_object_id_or_404:4624–4628',
                 'An isolated token referring to a syntactically valid but absent ObjectId was consumed and the function returned reset=True although no user matched. The ObjectId parser validates syntax, not account existence. No real account was deleted for this test.',
                 'Check the target user update matched exactly one authorized token-bound account and fail consistently within the same transaction otherwise.'),
    'RESET-19': ('SEC-02 / MEDIUM OPEN', 'server.py:250–281,1123–1130',
                 'An actual PyJWT access token minted before the reset remained accepted by actual get_current_user_optional after the reset. Invalid signatures/expiry/type and missing-user rejection separately passed. This is a failed explicit recovery-revocation invariant; the existing seven-day JWT design and final revocation policy still require owner disposition.',
                 'Agree on recovery/session-revocation policy, then use a server-checked session or token/password version and invalidate old sessions on reset while preserving persisted-role authorization.'),
    'RESET-27': ('SEC-04 / MEDIUM OPEN', 'server.py:833–850',
                 'A subject counter began at4 with cap5. Two controlled actual MongoDB reads both passed before the increment stage. Both requests were accepted and the persisted counter became6. Serial limit enforcement passed separately. This is a bounded local concurrency test, not an external abuse/load test.',
                 'Use an atomic capped shared counter with correct upsert/conflict behavior and an explicit multi-key rejection policy; preserve hashed subject keys and expiry cleanup.'),
    'RESET-30': ('SEC-06 / LOW OPEN', 'server.py:233–243,1083–1085;backend/requirements.txt:11',
                 'The actual reset Pydantic model accepted both distinct passwords above72 UTF-8 bytes. bcrypt4.1.3 hash_password/verify_password authenticated the second suffix against the first hash because their first72 bytes match. These are synthetic test inputs, not actual credentials or an exploited user account.',
                 'Choose an explicit UTF-8 byte-aware length policy or reviewed versioned long-password strategy. Preserve compatibility with stored credentials; do not silently change hashing or truncate inputs.'),
}
rows = []
for result in data['cases']:
    note = 'Observation only; not a security acceptance gate' if result['observations'].get('observation_only') else ''
    rows.append(f"| {result['id']} | {result['status']} | {result['invariant']} | {note} |")

failure_sections = []
for case_id, (risk, refs, meaning, recommendation) in mapping.items():
    result = next(x for x in data['cases'] if x['id'] == case_id)
    failure_sections.append(f"### {case_id} — {risk}\n\nSource: `{refs}` in [{source.name}]({source}).\n\n{meaning}\n\nRecorded sanitized observation:\n\n```json\n{json.dumps(result['observations'], indent=2)}\n```\n\nMinimal proposed correction, **not implemented**: {recommendation}\n")

artifacts = ['validate_password_reset.py', 'password-reset-run.log', 'password-reset-results.json',
             'password-reset-junit.xml', 'password-reset-run-v2.log', 'password-reset-results-v2.json',
             'password-reset-junit-v2.xml']
hash_rows = []
for name in artifacts:
    raw = (OUT / name).read_bytes()
    hash_rows.append({'file': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
provenance = {
    'project': 'COME-IN', 'recorded_Asia_Kolkata': stamp,
    'repository': '/workspace/come-in-current', 'branch': 'work', 'HEAD': 'a223290a8866a1ebeaac982f546491fdc197ae7a',
    'working_directory': str(OUT),
    'first_attempt': {'command': '/workspace/come-in-tools/py311/bin/python -B validate_password_reset.py > password-reset-run.log 2>&1',
                      'exit_code': 1, 'counts': first['counts'], 'database': first['database'],
                      'harness_issue': 'compile inherited harness future annotations, creating unresolved EmailStr forward references. Nine PydanticUserError results are harness errors, not application failures. Preserved verbatim.',
                      'historical_script_hash_limit': 'Initial script hash was not captured before correction; original execution log, result JSON and JUnit remain preserved.'},
    'corrected_attempt': {'command': '/workspace/come-in-tools/py311/bin/python -B validate_password_reset.py > password-reset-run-v2.log 2>&1',
                          'exit_code': 1, 'counts': data['counts'],
                          'correction': 'compile(..., dont_inherit=True) matches server.py no-future-import annotation semantics. Output filenames changed to v2 to retain attempt1. No application assertion weakened or source modified.',
                          'rerun_reason': 'Nine harness errors blocked the forgot paths; corrected run rechecks the same30 cases and preserves all genuine failures.'},
    'source_sha256_before_and_after': data['source_sha256'],
    'canonical_findings': {case_id: risk for case_id, (risk, *_rest) in mapping.items()},
    'new_canonical_finding_ids_created': [],
    'artifact_hashes': hash_rows,
    'safety': data['safety'], 'limitations': data['limitations'],
}
(OUT / 'password-reset-execution-provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')

report = f'''# Password Reset Security Validation Report

COME-IN — Phase1 Task1 owner validation. Recorded {stamp} (Asia/Kolkata).

Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. Actual application `{source.parent.parent}`. This is newly authorized isolated validation, not Task2 or remediation. Protected application source/configuration/original reports/checkpoints were not edited.

**Result: 30 freshly executed cases —23 PASS,7 FAIL,0 ERROR,0 SKIPPED. Exit1.** Two PASS cases (RESET-28/29) are explicitly observation checks; the other28 security/input/control assertions total21 PASS/7 FAIL. Seven failed assertions map to existing SEC-01/02/04/06 and two LOW SEC-01 subissues. No new canonical security identifier is created. Existing SEC-03 ingress exposure remains unverified. SEC-01 HIGH stays **OPEN — locally confirmed atomicity failure**, replacing its earlier source-only/local-validation-blocked boundary for these specific scenarios. No production or external account takeover is claimed.

## Executed scope and safety

The runner compiled the original AST nodes of21 actual functions/classes and5 actual constants from `backend/server.py`. Only API route decorators were removed; function/model bodies were not rewritten. `compile(..., dont_inherit=True)` preserves the original file's non-future annotation semantics. Actual Pydantic, bcrypt12, PyJWT, ObjectId, Motor and PyMongo are used. Function calls use real Starlette Request objects without HTTP transport; FastAPI routing/dependency injection/middleware/startup is not exercised. Source SHA-256 before and after: `{data['source_sha256']}`.

Real local MongoDB {data['database']['version']} was `rs0` PRIMARY at `127.0.0.1:27018`. Corrected run database `{data['database']['name']}` is retained:20 synthetic users,15 reset records,29 rate counters. First attempt DB `{first['database']['name']}` is also retained. No existing application/production DB, schema or record was read/written by this runner. No DB/collection drop/reset. The actual forgot function's deletion applies only to its own newly created synthetic accounts inside this unique DB.

Environment variables are an isolated synthetic dictionary supplied only to the extracted functions; no `.env` or process production credentials are loaded. JWT fixture secret/raw reset tokens exist only in memory. Database stores fixture password hashes and token hashes. SMTP email construction executes the actual helper, with its SMTP transport replaced by OfflineSMTP. No real email/provider request/payment/refund occurs. Process socket connections allow only loopback hosts. Test artifacts omit raw tokens, JWTs, passwords, SMTP/JWT secrets and message bodies; the runner contains clearly synthetic input strings, never actual credentials.

Controlled collection wrappers force both real token reads to finish before either reset proceeds, and inject a token-mark failure after the preceding real user write. These preserve application code and expose possible schedules; they are not a statistical concurrency/load test or a deployed HTTP exploit.

## Commands and runtime

Working directory: `{OUT}`.

```sh
/workspace/come-in-tools/py311/bin/python -B validate_password_reset.py > password-reset-run.log 2>&1
/workspace/come-in-tools/py311/bin/python -B validate_password_reset.py > password-reset-run-v2.log 2>&1
```

First attempt:15 PASS,6 FAIL,9 ERROR,0 SKIP; exit1. Nine `PydanticUserError`s were a harness-only annotation issue, not product failures. No attempt1 log/JSON/JUnit was overwritten. The compile flag was corrected to match actual source semantics, then the same30 cases rerun because these errors prevented forgot-flow coverage. Final corrected attempt:23 PASS,7 FAIL,0 ERROR,0 SKIP; exit1. All seven real failures remain; no assertion/rule was suppressed. The first script hash was not captured before the harness correction; final executed script and all saved artifacts are hashed separately.

Python `{data['python'].splitlines()[0]}` at `{data['python_executable']}`. Installed versions: `{json.dumps(data['versions'], sort_keys=True)}`. No package installation or service restart by this workstream. Parent started the retained local Mongo and raised its inherited nofile limit before this runner; this report does not claim a new Mongo installation.

Final run UTC interval: `{data['started_utc']}` to `{data['finished_utc']}`. Folder name remains the earlier session identifier; it is not the actual test timestamp.

## Every freshly executed case

| Case | Result | Intended invariant / observation | Scope note |
| --- | --- | --- | --- |
{chr(10).join(rows)}

## Failed assertions, severity and proposed corrections

{chr(10).join(failure_sections)}

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

- [Final result JSON]({OUT / 'password-reset-results-v2.json'}) — all30 outcomes, sanitized observations, original source segments/hashes, dependencies, input hashes and DB retention metadata.
- [Final JUnit]({OUT / 'password-reset-junit-v2.xml'}) and [actual command output]({OUT / 'password-reset-run-v2.log'}).
- [Executable runner]({OUT / 'validate_password_reset.py'}) and [execution provenance/hashes]({OUT / 'password-reset-execution-provenance.json'}).
- Attempt1 JSON/JUnit/log remain beside these; they include the disclosed harness errors.

No test operation remains running or interrupted. Last completed operation: corrected source-bound30-case run and evidence generation, source hash equality verified. No source fix was implemented or authorized. Do not aggregate attempt1 with attempt2 as60 independent acceptance cases;30 final unique cases are the denominator. Do not count two SEC-01 scenarios/subissues as newly numbered risks.

Next precise action: parent consolidates these confirmed failures with the other Task1 validation evidence and verifies preservation. Owner must explicitly authorize scoped source remediation before any fix; then repeat only affected deterministic cases plus justified regression. Task1 remains **REVIEW PENDING**, and HIGH SEC-01 must not be closed from documentation or passing route tests. Task2 is not started. No production readiness or owner approval is claimed.
'''
(OUT / 'PASSWORD_RESET_SECURITY_VALIDATION_REPORT.md').write_text(report)
checkpoint = f'''# Password reset validation checkpoint

COME-IN; {stamp}; `/workspace/come-in-current`; branch `work`; HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`.

Task1 isolated security validation, source fixes not authorized. Last completed operation: actual-function local-Mongo corrected run30cases23PASS7FAIL0ERROR0SKIP, exit1; source SHA256 `{data['source_sha256']}` unchanged. All inputs and attempt1 retained. Initial9harness errors disclosed and corrected by matching original compile annotation semantics; final tests did not weaken assertions.

Confirmed local findings: SEC01 token race/partial-write retry (HIGH OPEN); low SMTP config and missing-user consistency subissues; SEC02 oldJWT remains; SEC04 shared throttle overshoot; SEC06 bcrypt72-byte suffix alias. No new canonical IDs. Two observation cases do not approve production ingress or concurrent-forgot policy.

DB `{data['database']['name']}` retained on localhost27018 rs0 PRIMARY Mongo7.0.45; synthetic fixtures only. First attempt DB also retained. No drop/reset/source/config/provider/realemail/production operation. No operation running/interrupted. Existing checkpoints/reports untouched. New files: runner, attempt1+v2log/JSON/JUnit, report builder, executionprovenance, this checkpoint and report. Parent will finalize overall preservation/checkpoint.

Next action: consolidate report and owner evidence; owner authorization is required before any remediation. Current runner automatically selects a new DB but writes fixed v2 artifact names, so do NOT rerun it in this preserved folder: if future approved validation is needed, place the reviewed runner in a newly authorized dated output folder and redirect to a new log. No completed check needs rerun absent a related source or harness change.

NEXT_SESSION_RESUME_PROMPT: Read PASSWORD_RESET_SECURITY_VALIDATION_REPORT.md, password-reset-results-v2.json, password-reset-execution-provenance.json and the parent Task1 validation checkpoint first. Verify work/HEADa223290a8866a1ebeaac982f546491fdc197ae7a, Git status and all captured source/report hashes. Preserve every original and both retained test DBs. The corrected30-case run finished23PASS7FAIL0ERROR0SKIP; do not infer a passing reset gate or repeat it without cause. HIGH SEC01 is locally confirmed OPEN; no source fixes or Task2 are authorized. Continue only the exact owner-authorized next scope, keeping new evidence in a new dated output folder and updating its checkpoint after progress. Never contact production/provider SMTP or expose fixture tokens/secrets.
'''
(OUT / 'PASSWORD_RESET_VALIDATION_CHECKPOINT.md').write_text(checkpoint)
for filename in ['PASSWORD_RESET_SECURITY_VALIDATION_REPORT.md', 'PASSWORD_RESET_VALIDATION_CHECKPOINT.md', 'password-reset-execution-provenance.json']:
    raw = (OUT / filename).read_bytes()
    assert raw
    print(json.dumps({'saved_verified': filename, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}))
