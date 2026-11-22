from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,collections
E=Path(__file__).parent;R=E.parents[1];O=R/'evidence/phase-1-task-1-audit';A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115');claims=json.loads((E/'review-claim-ledger.json').read_text());count=json.loads((E/'claim-counts.json').read_text());stamp=datetime.now(timezone(timedelta(hours=-8))).isoformat()
# Human-readable labels and independent explanations. Original reference/verdict is unchanged.
rows={
'M01':('Expected project identity','Fresh Git root, branch and HEAD match the required values.'),
'M02':('Extracted source versus repository and remote','The app is outside Git; no remote fetch was performed. Remote main is not assumed current.'),
'M03':('ZIP hash, integrity and 62 changed members','Independent CRC/hash and byte comparison reproduce the reported snapshot differences.'),
'M04':('Declared frontend/backend architecture','Package, provider, router, cart and mode source supports the described architecture, not runtime acceptance.'),
'M05':('Protection of all inherited report/history files','The 8,150-file baseline excludes every root/evidence file, including all 39 historical XMLs. The blanket coverage wording is contradicted; no modification is demonstrated.'),
'M06':('Original no-write / no-record-read assertion','The saved metadata script is read-only, but a complete historical DB command audit trail is absent.'),
'M07':('Whole-application workflow coverage','Static mappings and selected historical results exist; current business/error branches were not all exercised.'),
'M08':('CHAND Home entry behavior','Source and a prior five-check web artifact support the entry behavior; current device/provider behavior is unverified.'),
'M09':('No application test run in recorded audit tools','Inspected audit tools parse/read evidence rather than execute application suites. This is bounded to the recorded work.'),
'M10':('No owner acceptance or Task 2 authorization','All original outputs retain REVIEW PENDING and distinguish audit review from closure.'),
'M11':('Actual native, provider and production acceptance','No corresponding real device/provider/production evidence is supplied.'),
'F01':('53 app route/layout files','Independent traversal confirms 53 files, including layouts, HTML, redirects and the fallback.'),
'F02':('95 scoped TS/TSX modules','The app/src scope contains 95 modules; adding expo-env.d.ts gives 96 frontend TS files. The scope matters.'),
'F03':('579 explicit event bindings','Source, saved JSON and report rows match exactly. There are 391 onPress attributes; these are not 579 tested buttons.'),
'F04':('108 recorded literal targets resolve','All selected candidates match file/group route candidates. No runtime router execution was performed.'),
'F05':('Exhaustiveness of literal navigation coverage','Branch-aware inspection finds 113 literal leaves: five branches are omitted, though their destination files exist.'),
'F06':('Public-path fields for special files','/_layout, +html and +not-found are file-derived placeholders, not ordinary public URLs. Their table fields require qualification.'),
'F07':('Href and dynamic navigation coverage','Five href attributes and 14 dynamic router arguments lie outside the 108 selected checks.'),
'F08':('Loading, empty and error state coverage','Lexical markers are present, but neither their presence nor absence proves component behavior.'),
'F09':('Intentional redirect and compatibility routes','Root, Restaurant account, addresses and support aliases are source-supported; they are not automatically dead duplicates.'),
'F10':('The single empty inline callback','It is a modal-sheet container callback with actionable children; context supports the audit interpretation.'),
'F11':('Stale payment information and demo notice','Current payment-methods.tsx and RestaurantPage.tsx support UI-01/UI-02. No UI change was made.'),
'F12':('Every screen/button/native workflow works','Selected historical smoke checks cannot establish full current interaction or device behavior.'),
'F13':('Dynamic authentication return target safety','auth.tsx:64 forwards next to router.replace. Allowed-target behavior and exploitability were not tested.'),
'B01':('179 explicit API registrations','Independent method/path/function extraction exactly matches the current source.'),
'B02':('60 Pydantic classes','Independent BaseModel/BaseDoc class extraction matches the inventory.'),
'B03':('Model fields and constraints','All 292 declared field records and recorded class validators match the source.'),
'B04':('No duplicate API registrations','No duplicate method plus literal path exists in the inspected server router; implicit/future routers are outside this claim.'),
'B05':('Declared authentication counts','50 role, 96 authenticated and three optional dependency registrations match; body checks are separately identified.'),
'B06':('Complete endpoint signature extraction','Annotations are captured, but defaults and Query constraints are omitted. server.py:3643 is a concrete example.'),
'B07':('Response-contract completeness','Only four endpoints declare response_model. Other response shapes require review; they are not automatically broken.'),
'B08':('Six apparent API-call mismatches','Their base earnings/Restaurant endpoints exist; query suffixes explain the lexical mismatch.'),
'B09':('Missing dedicated lifecycle endpoints','Absence is supported within the current registration inventory, not as proof that every external or operational implementation is absent.'),
'B10':('Safety of GET-based probes','GET referral/validate inserts an event; GET referrals/me can persist a code. These side effects were not inventoried.'),
'B11':('51 literal collection references','The independent server AST collection set matches the saved set.'),
'B12':('67 declarations and 27 unique indexes','Independent source keys and options match the original declaration inventory.'),
'B13':('52 collections and 119 indexes in the snapshot','Saved arrays contain 52 distinct collections, including 52 _id indexes. This is snapshot evidence.'),
'B14':('All 67 indexes match saved metadata','A stricter comparison of keys/options, including defaults and partial/TTL/name fields, still matches 67/67.'),
'B15':('No nonempty validators observed in the snapshot','All 52 boolean flags are false. The saved boolean cannot distinguish absent from empty validator objects.'),
'B16':('Global/current/production absence of validators','No such broader absence is established. The observation must stay within the inspected local snapshot.'),
'B17':('DB capture time and exact provenance','The script identifies the local target, but the JSON lacks capture time and raw hello/collection options.'),
'B18':('Transactions, references and financial consistency','Source helpers and old tests are available; index metadata is not current record-integrity or transaction evidence.'),
'B19':('Production DB, TLS and recovery configuration','Actual production grants, retention, RPO/RTO and infrastructure evidence are not supplied.'),
'S09':('Relevance of the SEC-01 named test reference','test_functional_blockers_regression.py has no password-reset coverage. The report does not claim atomicity was tested; the named related-test pointer is nevertheless irrelevant.'),
'G01':('Actual native binary and device validation','JavaScript exports/autolinking do not substitute for compiled binaries and device runs.'),
'G02':('Actual payment/refund/webhook provider validation','Source, local Mongo and mocks do not establish real provider TEST delivery or settlement.'),
'G03':('Production security/configuration acceptance','No authorized actual production infrastructure evidence is present.'),
'G04':('Complete delivery lifecycle is missing','Onboarding/admin/access exist. NOT IMPLEMENTED should be scoped to the missing full provider/assignment lifecycle.'),
'G05':('Actual AI/STT/vision provider behavior','Entry/planner evidence is not an external AI/media provider result.'),
'G06':('External push/SMTP/object delivery','Fail-closed source boundaries exist; successful external deliveries are not demonstrated.'),
'G07':('Guest Grocery post-order lifecycle gap','Guest creation and authenticated history/detail/cancel paths differ in the current source.'),
'G08':('Replacement scope distinction','Pack-only pre-checkout replacement exists; a paid post-placement replacement route is not found in the inspected inventory.'),
'G09':('UI-01/UI-02 inconsistency','The stale informational copy and global demo footer are independently source-supported.'),
'G10':('Security disposition and closure','The eight source patterns exist, but severity assumptions, owner acceptance and closure are not established.'),
'G11':('Storage validators and references','Local false flags do not prove global absence or current record/reference correctness.'),
'G12':('Every button works at runtime','579 bindings and 17 historical browser checks are insufficient for complete behavior coverage.'),
'G13':('Optional import/OCR readiness','The saved project-venv inventory reports missing optional packages; current feature acceptance remains limited.'),
'G14':('Historical quality results are not fresh','TypeScript/lint results are explicitly historical; no current advisory or semantic-check sign-off is implied.'),
'G15':('Remote main is the latest authority','No remote fetch was made. Only the local repository/archive/extraction relationship is established.'),
'G16':('All operational/error branches accepted','HomeServices, financial, referral and other source paths were not completely runtime-verified.'),
'C01':('All original Task 1 application criteria accepted','There is broad static evidence, but acceptance still depends on unresolved runtime and security decisions.'),
'C02':('Working-button criterion fulfilled','Binding inventory and selected smoke checks are not full working-control evidence.'),
'C03':('Seven required audit outputs exist','Six Markdown reports plus the original JSON manifest are readable and hash-consistent.'),
'C04':('Unbounded original configuration preservation','Covered bytes match, but actual .env, node_modules and root/evidence were excluded from the original baseline.'),
'C05':('Owner review and Task 2 gate preserved','REVIEW PENDING remains in the original outputs; no implementation/Task 2 approval is created.'),
'P01':('Six original report hashes and sizes','All six match the original manifest now.'),
'P02':('31 supporting hashes and sizes','All supporting entries match the original manifest now.'),
'P03':('Current source binding to the original baseline','All 8,150 covered file hashes match current bytes; this is not an attestation of excluded files or all actions.'),
'P04':('Historical XML run/source/hash provenance','The original manifest records paths and suite attributes, not XML hashes or complete run/source bindings.'),
'P05':('39 unique historical XML paths exist','All 39 are present, unique and parseable. This is not 39 green runs.'),
'P06':('Indexed XML suite attributes are accurate','Every indexed suite attribute matches the underlying XML.'),
'P07':('Selected historical test arithmetic','Actual testcase states support 558 passed/6 skipped, 70 passed, 78 passed and 25 passed, with overlapping scope.'),
'P08':('Failed and empty histories remain visible','Ten failed-run XMLs and one zero-test artifact remain in the indexed history; reports do not call them fresh green runs.'),
'P09':('Metadata capture and validator provenance','The finalization timestamp is not a DB-capture timestamp, and raw validator options were not retained.'),
'P10':('Absolute historical zero-action attestation','The recorded tools support the stated read-only scope, but no complete process/DB/provider audit trail is supplied.'),
'P11':('Availability of report source targets','The source paths and inventory bindings are available. Link existence does not establish test relevance or behavior.'),
'P12':('Explicit manifest self-hash exclusion','Recursive self-hash exclusion is documented. This review separately hashes the original manifest.')}
sec=json.loads((E/'backend-security-review-notes.json').read_text())['findings']
for i,f in enumerate(sec,1):
 rows[f'S{i:02d}A']=(f['id']+' source control structure',f['evidence_available'])
 rows[f'S{i:02d}B']=(f['id']+' severity, impact and closure',f['severity_assessment']+' '+f['more_investigation'])
assert set(rows)=={c['id'] for c in claims},(set(rows)-{c['id'] for c in claims},{c['id'] for c in claims}-set(rows))
for c in claims:c['claim'],c['independent_evidence']=rows[c['id']]
(E/'review-claim-ledger.json').write_text(json.dumps(claims,indent=2));counts=count['counts'];common=f'''Review time: {stamp} (UTC−08). Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`: all match the expected identity. Application source is `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`, outside the Git checkout.

**Final decision: REVIEW PENDING.** This is an evidence review for the owner, not personal owner approval, task closure or production readiness. Original reports, manifests, checkpoints, ZIP, source and configuration are preserved. Only this NEW review folder was written. No application tests, DB queries/writes, browser actions, provider calls, attacks, installs or service changes were performed in this review. Task 2 and implementation were not started.

'''
by='# Report-by-Report Owner Review\n\n'+common+'''## Counting method

The ledger contains **93 material claim-units**. They are scoped assertions or grouped inventory datasets, not all sentences, individual APIs, tests, events or unique issues. Each security finding has separate source-pattern and severity/closure units. Repeated cross-report assertions can therefore refer to the same underlying issue. All seven actual report files were read; the complete large screen/API inventories and JSON manifest were inspected rather than only their summaries.

'''
by+='| Verdict | Claim-units |\n|---|---:|\n'+''.join(f'| {k} | {v} |\n' for k,v in counts.items())+'\nThe complete finite denominator is in review-claim-ledger.json and claim-counts.json. Source/runtime scope must be read with each verdict.\n'
for file in [x['original_report'] for x in claims]:
 if file in globals().get('seen',set()):continue
 globals().setdefault('seen',set()).add(file);subset=[c for c in claims if c['original_report']==file];by+=f'\n## {file}\n\n{len(subset)} material claim-units. Original hashes and read sizes are in original-report-read-index.json.\n\n| ID | Original report reference | Claim / scope | Verdict | Independent evidence and remaining boundary |\n|---|---|---|---|---|\n'
 for c in subset:by+='| '+' | '.join(str(c[k]).replace('|','\\|').replace('\n','<br>') for k in ['id','reference','claim','verdict','independent_evidence'])+' |\n'
(E/'REPORT_BY_REPORT_REVIEW.md').write_text(by)
master='# COME-IN — Owner Review Master Report\n\n'+common+'''## Overall review result

All seven audit reports were independently inspected against current source, saved metadata, historical XMLs, manifests and preservation evidence. Independent reviewers checked frontend, backend/security and DB/history; the primary reviewer reconciled scope, provenance, contradictions and the final decision.

**93 material claim-units: 47 VERIFIED, 30 PARTIALLY VERIFIED, 6 UNVERIFIED, 3 CONTRADICTED and 7 BLOCKED.** This denominator is explicit in the ledger. It is not a completion percentage or a count of working screens/tests. Source patterns and their severity/closure claims are separate units.

## What was independently verified

- Exact workspace, `work` branch and required HEAD. The extraction is outside Git; no assumption was made about current remote `main` because no fetch was performed.
- All six original Markdown report hashes/sizes and all 31 supporting hashes/sizes match the original audit manifest. The original JSON manifest is separately hashed by this review.
- All 8,150 files covered by the original preservation baseline still match current bytes. This proves covered-file identity, not the excluded-file history or every action taken in the earlier session.
- Frontend: 53 app files, 95 scoped app/src modules, 579 explicit event attributes, including 391 `onPress` attributes. Saved row/handler multisets match current source. All 108 selected literal route candidates resolve to existing file/group candidates.
- Backend: 179 explicit route decorators, 60 Pydantic classes and 292 declared fields match. No duplicate method plus literal path was found in the inspected router. Only four endpoints explicitly declare `response_model`; other responses are not thereby proven broken or accepted.
- Database evidence: 67 current index declarations, 27 unique declarations and a strict 67/67 match against the saved 52-collection/119-index snapshot. The saved snapshot has 52 false validator flags. No fresh DB query was performed in this review.
- Historical evidence: all 39 unique XMLs exist and their indexed suite attributes match. Actual testcase arithmetic supports the selected historical 558 passed/6 skipped, 70 passed, 78 passed and 25 passed. Ten failed-run XMLs and one zero-test artifact also remain visible. These are not fresh tests or independent non-overlapping totals.
- Original ZIP: 5,484,042 bytes; SHA-256 `3233dcd9c8f1997b06035fd5cd7b458ab511658faf25e184044b17aec624d28c`; fresh read-only CRC PASS. Byte comparison reproduces 62 changed existing archive members in the extraction.

## Important discrepancies

1. **Overbroad preservation wording — CONTRADICTED.** Master report line 19 claims all inherited report/history files were protected. The baseline has 8,128 app files, 20 root files and two patches, but zero root/evidence files, including zero of the 39 historical XMLs. This is a coverage discrepancy, not evidence that any excluded file changed. Current review hashes cannot be backdated to the audit.
2. **Special-file public-path fields — CONTRADICTED as URL semantics.** The screen table assigns `/_layout`, `+html` and `+not-found` file-derived paths to special files. They are not ordinary public URLs. The original table does identify file kinds, but the “public path” field needs explicit qualification. No dead application route was demonstrated.
3. **SEC-01 related-test relevance — CONTRADICTED.** The named `test_functional_blockers_regression.py` file has no password-reset coverage. Existing reset-route existence assertions elsewhere do not verify one-time atomic consumption. The original report correctly says concurrency is untested; the wrong citation does not invalidate the source finding or close HIGH risk.

## Important coverage and provenance gaps

- Branch-aware analysis finds 113 literal navigation leaves, not just the 108 selected checks. Five omitted branches at Home `index.tsx:102`, `notifications.tsx:42` and `orders.tsx:193` all reference existing paths. Five `href` attributes and 14 dynamic router arguments are outside those checks. `auth.tsx:64` forwards dynamic `next`; allowed-target behavior remains unverified, not a proven redirect exploit.
- The API inventory captures annotations but omits endpoint defaults and `Query` constraints. The “all signatures” statement is stronger than the data, although API/model counts are correct. `server.py:3643` provides a concrete omitted `kind` pattern/default.
- GET is not automatically read-only: referral validation can insert `referral_link_events`, and `/referrals/me` can persist a referral code. A future safe-runtime plan needs transitive side-effect classification. No such GET request was issued here.
- The DB snapshot has no capture-specific timestamp or raw `hello`/collection validator options. False flags support only “no nonempty validator observed in those 52 local snapshot entries,” not current, global or production absence.
- Historical XML paths and suite attributes were captured, but original XML hashes and complete source/command/environment run bindings were not. This review records current XML hashes for future integrity, not retrospective attestation.
- Actual environment files, dependency trees and inherited root/evidence were outside the original baseline. Covered-file preservation is verified; an unlimited all-configuration/history claim is not independently established.

## Security review

All eight source patterns are supported. The reported total—one HIGH, five MEDIUM and two LOW—is correct, but impact/severity and closure remain conditional on policies, deployment mitigations and missing isolated evidence. No attack or fix was performed.

**HIGH SEC-01 remains OPEN:** reset token lookup, password update and token marking are separate operations without a shared transaction/conditional claim. High-priority review is defensible for account recovery integrity, but arbitrary unauthenticated takeover was not demonstrated and a valid token/flow is a prerequisite. Personal owner disposition and separately approved evidence are still required.

The seven other findings concern revocation policy, forwarded-IP trust, throttle atomicity, public diagnostic writes, bcrypt byte handling, synchronous HTTP in async routes and webhook buffering limits. Full source/report references, impact, severity justification and remaining evidence are in SECURITY_FINDINGS_REVIEW.md.

## Runtime and external limits

Bindings are not working buttons. The historical 17 browser checks are limited web login/render/navigation evidence, not every workflow, error state, permission or native checkout. JS exports and autolink discovery are not native binary/device evidence. Local Mongo/mocked-provider/signed-event tests do not establish actual Razorpay TEST payments, provider webhook delivery, refund settlement or other external deliveries. Production TLS, CORS, secrets, DB roles, retention/RPO/RTO, ingress and logging remain blocked without authorized infrastructure evidence. No production readiness claim is made.

## Decision and next action

**Final review decision and recommendation: REVIEW PENDING.** Counts and much source evidence are sound. The unresolved HIGH disposition, coverage/provenance qualifications and missing runtime/external evidence prevent automatic closure or final owner approval. Twenty evidence/decision gaps are recorded; they are not twenty new canonical tasks.

The six required review outputs and supporting notes are in this NEW folder. Before/after Git status and final preservation verification are recorded by the review manifest. All original reports, the original manifest, checkpoints, source, configuration, ZIP and Git history were left unchanged.

**STOP:** wait for personal owner review and explicit approval of any further scope. Do not implement fixes, start Task 2, install anything, change configuration or deploy. No application test/build/service/DB/provider operation was started by this review.
'''
(E/'OWNER_REVIEW_MASTER_REPORT.md').write_text(master)
security='# Security Findings Owner Review\n\n'+common+'''## Assessment rules

All eight reported source control patterns are VERIFIED. Reported severity arithmetic is correct: one HIGH, five MEDIUM and two LOW. Severity, deployment exposure, runtime impact and closure are PARTIALLY VERIFIED. No successful exploit, account takeover, load failure, provider effect or remediation test was established. HIGH SEC-01 remains OPEN. No new vulnerability count is inferred from documentation gaps.

'''
priorities=['P1 — owner security decision first','P2 — session policy','P2 — deployment/proxy trust','P2 — rate-limit acceptance','P2 — legacy endpoint policy','P3 — byte-aware password compatibility','P3 — availability/load scope','P2 — ingress and request-size controls']
for i,f in enumerate(sec):
 security+=f"## {f['id']} — reported {f['reported_severity']} — OPEN\n\n- Original report: `{f['report_ref']}`.\n- Source: `{f['source_ref']}`; symbols: `{f['symbols']}`.\n- Evidence: {f['evidence_available']}\n- Source structure: VERIFIED. Severity/impact/closure: PARTIALLY VERIFIED.\n- Severity and potential impact: {f['severity_assessment']}\n- Review priority: {priorities[i]}.\n- Further investigation/decision: {f['more_investigation']}\n- No fix, exploitation, credential creation or application test was performed.\n\n"
security+='''## Additional review boundaries

- **Wrong related-test pointer:** original Security report line 20 names a file with no reset coverage. `test_restaurant_api_contract.py:33–34` only checks route existence. Do not infer atomic token consumption, rollback or revocation coverage.
- **GET mutation omissions:** `server.py:942–946` inserts referral-link events; `:900–905` calls a helper that can persist a code. Add a side-effect map before any future “read-only GET” probes. This is a safety/coverage omission, not a new exploited vulnerability.
- **Dynamic return target:** `auth.tsx:64` passes `next` to the router. The selected literal checks do not establish a safe allowlist or an exploit; no navigation attack was attempted.
- **Deployment mitigations:** actual proxy sanitization, body caps, edge rate limits, DB grants, TLS/CORS, secret handling and logging are not validated by local source.
- **Coverage is not exhaustive security acceptance:** registration/dependency counts do not exercise every ownership branch or response field. No full IDOR/XSS/error/log exposure test was performed. Such work needs separate scope and approval.
''';(E/'SECURITY_FINDINGS_REVIEW.md').write_text(security)
# Preserve the machine gap IDs/closure mapping, render clearer descriptions.
gaps=json.loads((E/'evidence-gaps.json').read_text());descriptions=[
('Navigation branches','Five conditional leaf occurrences are absent from the 108-check inventory.','Add a source-based branch inventory; all five destination files already exist.'),
('Href/dynamic navigation','Five href attributes and 14 dynamic arguments are outside literal checks.','Qualify scope and review allowed return targets; no malicious navigation is authorized.'),
('Special-file URL fields','Layout/document/fallback placeholders look like public paths.','Issue an explanatory addendum; do not change application routes.'),
('Endpoint signatures','Defaults and Query/Form/File constraints are not fully inventoried.','Provide complete parameter metadata in a separately approved addendum.'),
('Reset test reference','The named test has no reset coverage; atomicity evidence is missing.','Correct the evidence citation in an addendum and retain HIGH as open.'),
('GET side effects','Some referral GET handlers write data.','Classify direct and transitive effects before runtime probes.'),
('Preservation coverage','The original baseline excludes inherited root/evidence and historical XMLs.','Narrow the blanket statement; current hashes do not authenticate the past.'),
('Historical run provenance','Original XML hashes and complete command/source-run bindings are absent.','Use trusted run/source/environment provenance for decisive acceptance evidence.'),
('DB snapshot provenance','No capture-specific time or raw validator options were retained.','Obtain scoped, timestamped, redacted metadata only if separately authorized.'),
('Validator scope','Local false flags do not prove global/current/production absence.','Retain the bounded observation; do not infer a production result.'),
('Configuration preservation','Actual environment files and dependencies were excluded from the old baseline.','Define non-secret metadata/hash coverage; never print secret values.'),
('HIGH finding disposition','Reset atomicity has no owner closure or isolated failure/race evidence.','Owner must decide priority and authorize any future investigation/remediation.'),
('Other security impacts','Policy/ingress/burst/body-limit and load evidence remain incomplete.','Approve operation-specific acceptance criteria; no attack or fix in this review.'),
('Working actions','Event bindings and limited historical smoke checks do not prove all workflows.','Define an owner-approved disposable action/state/error/permission matrix.'),
('Native binary/device','No corresponding compiled Android/iOS and physical-device evidence is supplied.','Provide actual build/device artifacts from authorized hosts and devices.'),
('Actual providers','Mocks and local signed events are not provider TEST delivery/settlement.','Provide authorized secure TEST configuration and real provider evidence.'),
('Production infrastructure','Actual TLS/CORS/DB/secrets/backup/log/abuse controls are unavailable.','Provide authorized read-only infrastructure evidence; do not deploy.'),
('Data/transaction consistency','Metadata cannot establish record integrity, financial consistency or recoverability.','Use trusted source-bound historical results or separately approved disposable checks.'),
('Operational scope','Delivery, guest lifecycle and replacement acceptance need product decisions.','Keep existing functionality distinct from missing full lifecycle scope.'),
('Remote/quality state','Remote main and remaining quality/advisory gates are not newly verified.','Owner must scope any further read-only evidence work; no install/upgrade/reset.')]
gaptext='# Evidence Gap Register\n\n'+common+'''The following 20 entries are evidence or owner-decision gaps, not new canonical tasks or 20 proven vulnerabilities. Closure actions are recommendations only. No original report is silently corrected.

| ID | Area | Missing evidence | Required closure evidence / decision | Claim IDs |
|---|---|---|---|---|
'''
for g,(area,missing,closure) in zip(gaps,descriptions):
 g.update(area=area,missing=missing,closure_evidence=closure);gaptext+='| '+' | '.join([g['id'],area,missing,closure,g['claims']])+' |\n'
(E/'evidence-gaps.json').write_text(json.dumps(gaps,indent=2));gaptext+='\nThe owner/security team owns risk acceptance and future scope; developer/device/provider/production custodians must supply their respective evidence. No external blocker was resolved in this review.\n';(E/'EVIDENCE_GAP_REGISTER.md').write_text(gaptext)
check='# Owner Approval Checklist\n\n'+common+'''None of these unchecked items is an approval already granted:

- [ ] Review all seven original reports, this report-by-report review and the explicit 93-claim denominator.
- [ ] Accept the counts only as source/static evidence: 53 app files; 95 scoped modules; 579 events (391 onPress); 179 APIs; 60 models/292 fields; 67 index declarations/27 unique.
- [ ] Acknowledge 108 selected navigation checks, five omitted conditional leaves, five hrefs, 14 dynamic arguments and special-file path qualifications.
- [ ] Require a separate addendum for omitted endpoint constraints, GET side effects and the wrong SEC-01 test reference; preserve originals.
- [ ] Personally decide HIGH SEC-01 priority and any separately authorized evidence/remediation scope. Do not close it from route-existence tests.
- [ ] Review all seven other security findings, their assumptions, severity conditions and owner policies.
- [ ] Accept DB observations only as the saved local snapshot; require capture time/raw options if needed for closure.
- [ ] Treat all 39 XML artifacts as historical. Require trusted run/source/hash provenance for decisive acceptance; failing and empty runs stay visible.
- [ ] Acknowledge the original preservation exclusions; do not backdate current review hashes.
- [ ] Define which runtime/button/guest/replacement/delivery requirements are mandatory for Task 1 acceptance and which remain recorded limitations.
- [ ] Keep native/provider/production gates blocked without their actual evidence. Static checks and mocks are not substitutes.
- [ ] Review the evidence-gap register and final preservation/hash manifest.
- [ ] Personally record one permitted decision: APPROVED FOR TASK CLOSURE / APPROVED WITH RECORDED LIMITATIONS / REVIEW PENDING / REJECTED — CORRECTIONS OR EVIDENCE REQUIRED.
- [ ] Give explicit new approval and scope before further work. This review does not authorize Task 2, fixes, installs, provider operations or deployment.

**Reviewer recommendation: REVIEW PENDING.** Many source claims are verified. Unresolved HIGH disposition, coverage/provenance issues and missing runtime/external evidence prevent automatic final approval. No personal owner approval is created on the owner's behalf.
''';(E/'OWNER_APPROVAL_CHECKLIST.md').write_text(check)
print('Readable owner reports finalized;93claim verdicts unchanged:',counts)
