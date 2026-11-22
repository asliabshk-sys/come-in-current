"""Documentation-only compilation. Does not import/run the application or tests."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
REPO = Path('/workspace/come-in-current')
APP = Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
OLD = HERE.parent
AUDIT = REPO / 'evidence/phase-1-task-1-audit'
HEAD = 'a223290a8866a1ebeaac982f546491fdc197ae7a'
NOW = datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
STATUSES = {'VERIFIED', 'PARTIALLY VERIFIED', 'UNVERIFIED', 'CONTRADICTED', 'BLOCKED'}

def read(p):
    return json.loads(Path(p).read_text())

def write(name, contents):
    with (HERE / name).open('x') as out:
        out.write(contents)

def dump(name, obj):
    write(name, json.dumps(obj, indent=2, ensure_ascii=False) + '\n')

def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()

def git(*args):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(REPO), *args], text=True)

def link(path, line=None, label=None):
    path = Path(path)
    return f'[{label or path.name}](<{path}{":" + str(line) if line else ""}>)'

def cell(s):
    return str(s).replace('|', '\\|').replace('\n', '<br>')

def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] + [
        '| ' + ' | '.join(cell(x) for x in row) + ' |' for row in rows]) + '\n'

def preamble(title):
    return f'''# {title}

Project: COME-IN. Review recorded **{NOW} (Asia/Kolkata)**. This existing dated iteration was opened on 18 November and resumed on 19 November; it is not a new audit restart.

Repository: `{REPO}`; branch: `work`; HEAD: `{HEAD}`. Application extraction: `{APP}` (outside the Git checkout).

Scope: read-only evidence investigation and NEW documentation only. All seven original audit reports and all six original owner-review reports/manifests were read before this iteration's investigation. Originals are retained verbatim. No application tests, browser actions, database queries/writes, account/token creation, provider calls, installs, configuration changes or implementation were performed. Task 2 was not started. The owner has not approved or closed Task 1.

Classification vocabulary: VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / CONTRADICTED / BLOCKED. Each assessed assertion has one classification. Source correctness, runtime acceptance and owner approval are separate assertions.

'''

nav = read(HERE / 'navigation-closure.json')
api = read(HERE / 'complete-api-inventory.json')
reset = read(HERE / 'reset-flow-validation.json')
prov = read(HERE / 'provenance-gap-dispositions.json')
effects = read(HERE / 'get-side-effect-inventory.json')
assert git('branch', '--show-current').strip() == 'work'
assert git('rev-parse', 'HEAD').strip() == HEAD
assert len(api['endpoints']) == 179 and len(api['request_models']) == 60
assert len(nav['omitted_branches']) == 5

# All 20 gaps are retained. Root integration narrows the assessed statement and
# incorporates source-specific peer evidence instead of silently closing acceptance.
gap_updates = {
 'R01': ('VERIFIED', 'Five omitted conditional leaves and all destination files are source-mapped.',
         'Source inventory documentation gap CLOSED:113 literal leaves=107 unconditional occurrences+six leaves of three ternaries;old108 included only one of the six conditional leaves.',
         'Actual handler execution, rendered screens, permissions and navigation remain UNVERIFIED.', ['navigation-closure.json', 'FINAL_NAVIGATION_AND_API_INVENTORY.md']),
 'R02': ('PARTIALLY VERIFIED', 'Href and dynamic destination inventory coverage.',
         'All five href attributes and14 dynamic non-back arguments have a source disposition;12 entity templates and one finite RestaurantNav list are bounded. The auth next parameter remains unbounded in this inspection.',
         'Dynamic values, allowed-return policy, encoding, permissions and runtime navigation remain open. Owner/security review must define allowed return targets;no exploit inferred.', ['navigation-closure.json', 'FINAL_NAVIGATION_AND_API_INVENTORY.md']),
 'R03': ('VERIFIED', 'Special-file public-path qualification.',
         'Documentation gap CLOSED:layout/document/fallback files are not ordinary public URL proof;the original mistaken fields remain unchanged.',
         'Router/runtime acceptance remains open;no route change is required for this additive correction.', ['navigation-closure.json', 'FINAL_NAVIGATION_AND_API_INVENTORY.md']),
 'R04': ('VERIFIED', 'All179 explicit API signatures,defaults and constraint expressions are inventoried from source.',
         'Source metadata gap CLOSED:387 parameters,216 Python defaults,27 Query parameters across19 endpoints,60 model declarations with fields/validators and all explicit response decorators are recorded. All179 method/path/function triples match the original inventory.',
         'Generated OpenAPI, helper errors, dependency effects, serialization and request/response behavior remain UNVERIFIED;source metadata is not runtime acceptance.', ['complete-api-inventory.json', 'FINAL_NAVIGATION_AND_API_INVENTORY.md']),
 'R05': ('CONTRADICTED', 'The original SEC-01 related test pointer supports reset coverage.',
         'Citation correction supplied additively:the named functional-blocker file has zero reset assertions;restaurant contract lines33-34 establish route presence only. Original incorrect pointer is preserved.',
         'No atomic consumption, rollback, concurrency, SMTP delivery or revocation passing evidence was found. HIGH remains OPEN.', ['reset-flow-validation.json', 'FINAL_SECURITY_VALIDATION_REPORT.md']),
 'R06': ('PARTIALLY VERIFIED', 'GET-based probe safety coverage.',
         'Source safety addendum records81 GET handlers and three potential local/transitive Mongo write paths,including the previously omitted admin detail access-audit write. No GETs called.',
         'Absence of a recognized write site is not a purity guarantee:dynamic/external helpers,aliases and telemetry are not exhaustively resolved. Any future probe needs operation-specific review.', ['get-side-effect-inventory.json', 'FINAL_NAVIGATION_AND_API_INVENTORY.md']),
}
gaps = []
for original in prov['gap_dispositions']:
    x = dict(original)
    if x['gap_id'] in gap_updates:
        status, assessed, doc, acceptance, evidence = gap_updates[x['gap_id']]
        x.update(classification=status, claim_assessed=assessed, documentation_disposition=doc,
                 underlying_acceptance=acceptance, iteration_evidence=evidence)
    else:
        x['iteration_evidence'] = ['provenance-gap-dispositions.json', 'FINAL_PRESERVATION_VERIFICATION.md'] if x['gap_id'] in {'R07','R08','R09','R10','R11','R18','R20'} else ['FINAL_SECURITY_VALIDATION_REPORT.md' if x['gap_id'] in {'R12','R13'} else 'FINAL_OWNER_DECISION_READINESS.md']
    assert x['classification'] in STATUSES
    gaps.append(x)
dump('final-gap-ledger.json', {'scope': '20 evidence/owner-decision gap assertions,not vulnerabilities or task completion counts',
     'timestamp': NOW, 'classifications': dict(Counter(x['classification'] for x in gaps)), 'gaps': gaps})

# Retain historical IDs and contradictions; only two bounded source assertions gain evidence.
claims = read(OLD / 'review-claim-ledger.json')
for x in claims:
    x['prior_classification'] = x.pop('verdict')
    x['classification'] = x['prior_classification']
    x['current_basis'] = 'Retained scoped owner-review assessment;original evidence remains byte-identical within the captured baseline. No fresh application run inferred.'
    x['iteration_evidence'] = [str(HERE / 'FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md')]
    if x['id'] == 'F05':
        x['classification'] = 'VERIFIED'
        x['current_basis'] = 'Corrected bounded source coverage now includes113 literal leaves;original108-set was incomplete. Full runtime navigation is a separate UNVERIFIED assertion.'
        x['iteration_evidence'] = [str(HERE / 'navigation-closure.json')]
    if x['id'] == 'B06':
        x['classification'] = 'VERIFIED'
        x['current_basis'] = 'Full179 source signatures/defaults/constraint expressions now recorded,including File/Form/Query declarations. Runtime input/response acceptance remains separate.'
        x['iteration_evidence'] = [str(HERE / 'complete-api-inventory.json')]
    assert x['classification'] in STATUSES
dump('final-claim-ledger.json', {'denominator': len(claims), 'basis': 'Inherited93material claim-units,not unique vulnerabilities,tests,buttons or taskcompletion. OnlyF05/B06 source-inventory dispositions revised;original3contradictions retained.',
     'counts': dict(Counter(x['classification'] for x in claims)), 'claims': claims})

txt = preamble('Final Evidence Gap Closure Report')
txt += '## Result and evidence boundaries\n\n**Recommendation B — REVIEW PENDING — EVIDENCE GAPS REMAIN.** Source-inventory and documentation gaps can close without accepting application behavior or closing security risks. No verification percentages are asserted.\n\n'
txt += 'The original20gap IDs are all addressed below. “Documentation CLOSED” means an additive correction or bounded inventory exists;it does not mean the underlying release/security gate passed.\n\n'
txt += table(['Gap', 'Assessed claim', 'Classification', 'Documentation disposition', 'Underlying acceptance / remaining action', 'Evidence'], [
    [x['gap_id'], x['claim_assessed'], x['classification'], x['documentation_disposition'], x['underlying_acceptance'] + ' Next: ' + x['required_closure_evidence_or_decision'] + ' Responsible: ' + x['responsible_party'],
     '; '.join(link(HERE / s) for s in x['iteration_evidence'])] for x in gaps])
txt += '\n## Original claim accountability\n\nAll93material claim-units from the original owner review retain their IDs. OnlyF05(literal source-inventory completeness) andB06(full source signatures) advance to VERIFIED based on new bounded metadata. The old M05 preservation blanket statement,F06 special-file URL interpretation andS09 reset-test relevance remain CONTRADICTED as historical assertions;this addendum does not rewrite them. Counts apply to these93claim-units only;overlapping source and severity assertions are not unique vulnerabilities or completion percentages.\n\n'
txt += table(['Classification', 'Claim units'], sorted(Counter(x['classification'] for x in claims).items()))
txt += '\n' + table(['ID', 'Original assessed assertion', 'Current classification', 'Evidence / qualification'], [
 [x['id'], x['claim'], x['classification'], x['reference'] + ' ' + x['current_basis'] + ' ' + link(OLD/'REPORT_BY_REPORT_REVIEW.md')] for x in claims])
txt += '\n## Historical records and actions actually executed\n\n'
txt += f'''The39 unique historical XML artifact paths in the original manifest still exist and their bytes match the previous owner-review captures. Their recorded timestamps and results are historical, not fresh execution. {link(HERE/'provenance-gap-dispositions.json')} retains all39 hashes/timestamps and missing provenance fields. No trusted contemporaneous per-run source/build/hash/command/environment binding was recovered for decisive acceptance. Finding some commands and logs does not authenticate every run against this exact extraction. Current hashes cannot backdate trust.

Fresh work consisted of Git identity/status/diff inspection, file reads and SHA-256 comparisons, AST-only parsing, static TypeScript navigation evidence review, XML/provenance interpretation and document/reference validation. No application modules were imported and no tests or databases were invoked. Commands/scripts used: `git --no-optional-locks -C /workspace/come-in-current branch --show-current`, `rev-parse HEAD`, `status --porcelain=v1 --untracked-files=all`, `diff --no-ext-diff --exit-code`, `diff --cached --no-ext-diff --exit-code`, Python standard-library file hashing/JSON/XML/AST parsing, `python {HERE/'extract-complete-api.py'}`, `python {HERE/'augment-api-effects.py'}` and this documentation compiler. The application and provider test count freshly executed is **0**;there are no fresh application PASS/FAIL/SKIPPED counts.

Historical TypeScript0errors,ESLint0errors/10warnings and backend558passed/6skipped are retained as historical reports only,not rerun or newly certified. No build/native/provider/transaction suite was repeated. Source identity and hash equality do not turn these into fresh test outcomes.

Inputs: {link(AUDIT/'PHASE_1_TASK_1_EVIDENCE_MANIFEST.json')}, {link(OLD/'REVIEW_EVIDENCE_MANIFEST.json')}, {link(OLD/'EVIDENCE_GAP_REGISTER.md')}, {link(HERE/'final-claim-ledger.json')}, {link(HERE/'final-gap-ledger.json')}. Input13report hashes and reference checks are recorded in the new manifest/reference index.
'''
write('FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md', txt)

txt = preamble('Final Security Validation Report')
txt += f'''## Highest-priority finding

**SEC-01 — reported HIGH — OPEN / VALIDATION BLOCKED.** Source non-atomic control structure is VERIFIED. Current runtime impact is UNVERIFIED;closure is BLOCKED by absent isolated concurrency/failure evidence and absent owner disposition. These are separate assertions,not two classifications of the same claim. No account takeover,password reset,replay or exploitation was attempted or proved.

Original finding: {link(AUDIT/'PHASE_1_TASK_1_SECURITY_FINDINGS.md',13)}. Prior assessment: {link(OLD/'SECURITY_FINDINGS_REVIEW.md')}. New full trace/citations/proposed tests: {link(HERE/'reset-flow-validation.json')}.

## Complete password-reset flow traced from source

'''
for stage in reset['flow_stages']:
    txt += f"### {stage['stage']}. {stage['name']}\n\nAssessed assertion: the following control declarations exist in `{stage['symbols']}` — **VERIFIED** at source level.\n\n"
    txt += 'Evidence: ' + '; '.join(link(e['path'], e['line_start']) for e in stage['evidence']) + '.\n\n'
    txt += '\n'.join('- ' + s for s in stage['controls_found']) + '\n\n'
    txt += 'Remaining limitations: ' + ' '.join(stage['limits_or_gaps']) + '\n\n'
txt += '''## Exact risk,preconditions and impact boundary

The consumer reads a matching unused/unexpired SHA-256 token record,then awaits the user password write,then independently marks the reset record used. There is no shared transaction/session or conditional atomic token claim across these steps. A second consumer may read the same valid record before it is marked;an error after the first write can leave password and token state inconsistent. This is a source-derived interleaving/failure concern,not a demonstrated runtime exploit. Missing user update-result checks are also visible in this path.

The prerequisite is an existing account plus a valid unused/unexpired token or access to the authorized issuance flow. Arbitrary wrong,expired or used token input is filtered. A concurrency/failure timing condition is additionally needed for the claimed atomicity impact. SMTP bindings,actual delivery,current token availability,proxy controls and live DB behavior were not inspected. HIGH is a defensible provisional priority for recovery integrity,not proof of arbitrary unauthenticated takeover. Keep it open pending adequate isolated evidence and owner decision.

Applicable protections include EmailStr and length constraints, cryptographic token issuance, hashed storage, explicit 30-minute expiry/used checks, generic forgot response, attempt counters, target-user ID derived from the stored token record, bcrypt hashing and no new JWT issued on reset. These do not make the two writes atomic. Reset nominal limit is **IP-only 50 per 900 seconds** (configured 10 multiplied by IP factor 5), not 10 per-token attempts. Forgot is nominally 5 per-email and 25 per-IP per hour. These source values do not prove strict concurrent or ingress enforcement.

Separate SEC-02:the access JWT has a seven-day expiry and the current user/role is reloaded,but no session version/password-change cutoff/jti revocation is checked. Local client logout does not prove server invalidation of a copied JWT. The owner must define reset/logout-all policy before acceptance.

## Test-citation validation

'''
txt += table(['Citation', 'Evidence actually provided', 'Classification'], [
 [link(reset['irrelevant_original_citation']['path']), 'Zero password-reset-specific assertions;original SEC-01 related-test pointer is irrelevant.', 'CONTRADICTED'],
 *[[link(t['reference']['path'],t['reference']['line_start']), t['test'] + ': ' + t['scope'], 'VERIFIED'] for t in reset['related_existing_tests']]])
txt += '\nThe VERIFIED labels above concern cited test contents only;the tests were not run. Historical cases below are existing artifacts,not newly executed atomicity evidence.\n\n'
txt += table(['Historical XML', 'Recorded suite timestamp', 'Relevant recorded cases', 'Classification'], [
 [link(t['path']),t['recorded_suite_timestamp'],'; '.join(c['name'] + ' (' + c['result'] + ',static route/storage/logout scope only)' for c in t['cases']), 'VERIFIED'] for t in reset['historical_artifacts']])
txt += '\n## All eight original findings retained\n\nReported arithmetic remains oneHIGH,fiveMEDIUM,twoLOW. Eight findings are not multiplied by the number of routes,events or evidence gaps. Source-pattern assertions remain VERIFIED;severity/exposure/impact acceptance remains PARTIALLY VERIFIED for the reasons below. No finding was fixed or closed.\n\n'
security_rows = [
 ('SEC-01','HIGH','reset_password',1123,'Sequential token read,password write,used-marker write;valid-token/race/failure prerequisites.','OPEN / VALIDATION BLOCKED;owner disposition plus isolated atomicity/failure evidence.'),
 ('SEC-02','MEDIUM','create_access_token/get_current_user_optional/reset_password',250,'No server revocation/version cutoff;DB user/role/expiry still checked.','OPEN;owner revocation policy and isolated old-JWT evidence.'),
 ('SEC-03','MEDIUM','_client_ip/_rate_keys',819,'First X-Forwarded-For trusted in-function;deployment proxy sanitization unknown.','OPEN;authorized ingress/proxy evidence;no spoofing performed.'),
 ('SEC-04','MEDIUM','_check_auth_rate_limit/_record_auth_attempt/login',833,'Read/check and increment separated;burst magnitude not measured.','OPEN;approved isolated concurrency criteria/evidence.'),
 ('SEC-05','MEDIUM','create_status_check/list_status_checks',687,'Anonymous diagnostic writes and shared feed;intended audience/edge caps unknown.','OPEN;owner endpoint policy and bounded abuse-control evidence.'),
 ('SEC-06','LOW','RegisterIn/ResetPasswordIn/hash_password',305,'128-character input versus bcrypt byte semantics;no fresh collision proof.','OPEN;deployed bcrypt/version byte-aware compatibility evidence.'),
 ('SEC-07','LOW','create_restaurant_payment_intent/verify_grocery_payment',4990,'Blocking requests calls in async handlers;availability impact unmeasured.','OPEN;separately scoped event-loop/load evidence.'),
 ('SEC-08','MEDIUM','razorpay_webhook/event_payload',5362,'Body buffered/HMAC before payload size guard;missing config rejects before buffering.','OPEN;actual ingress body limits and approved isolated transport validation.')]
txt += table(['ID / reported severity','Component / evidence','Source claim classification','Severity/impact classification','Impact qualification / next evidence'], [
 [i+' / '+severity, sym+' '+link(APP/'backend/server.py',line), 'VERIFIED','PARTIALLY VERIFIED', impact+' '+action] for i,severity,sym,line,impact,action in security_rows])
txt += '\n## Additional bounded observations\n\n'
txt += '\n'.join('- ' + s for s in reset['additional_source_review_caveats']) + '\n\n'
txt += f'''The admin application-detail GET also writes an access audit;referral GETs can mutate referral state. This is a probe-safety documentation correction,not a newly exploited vulnerability. See {link(HERE/'get-side-effect-inventory.json')}. `auth.tsx:64` passes the route `next` parameter to the router after authentication;allowed-target behavior remains UNVERIFIED. No open-redirect exploit is claimed. Production proxy/rate/body/DB/TLS/CORS/secret/logging controls remain unverified by local source.

## Required safe validation proposals — none executed

All11 proposals below require separately authorized bounded testing/inspection. No production/customer accounts,real email,provider calls or credentials are authorized by this report. Tests that write data must use explicitly isolated disposable fixtures. A proposal is not evidence of a pass.

'''
txt += table(['ID','Proposed check','Safe scope / acceptance need','Execution status'], [[t['id'], t['name'],t['proposal']+' '+t['safety'],'NOT EXECUTED — future authorization required'] for t in reset['proposed_tests_NOT_EXECUTED']])
txt += '\n**Disposition: SEC-01 remains OPEN / VALIDATION BLOCKED. No owner approval,remediation or task closure is inferred.**\n'
write('FINAL_SECURITY_VALIDATION_REPORT.md',txt)

txt = preamble('Final Navigation and API Inventory')
txt += f'''## Navigation count reconciliation

Source scope is the previously inventoried95TS/TSX modules,including53app route/layout files. The579event bindings are occurrences,not579working buttons or vulnerabilities. The108 previously selected literal targets resolve at source level,but did not exhaust conditional leaves. Complete bounded count: **107unconditional literal/pathname calls +6leaves of3two-branch conditional calls =113literal destination occurrences**. The old108set retained the Restaurant leaf at `orders.tsx:193` and omitted the five below. These are destination occurrences,not unique URLs or completed journeys.

Original108checks: {link(AUDIT/'navigation-target-checks.json')}. New predicates,components,source/target hashes and input hashes: {link(HERE/'navigation-closure.json')}. The file-existence/source mapping assertions below are VERIFIED;runtime navigation remains UNVERIFIED.

'''
txt += table(['Omitted leaf','Source','Exact static condition','Destination / parameters','Existing destination file','Classification'], [[
 x['claim_id'],link(x['source']['path'],x['source']['line']),x['effective_static_predicate'],x['destination'] + ('; '+x['pathname_object_expression'] if x['pathname_object_expression'] else ''),
 '; '.join(link(t['path'],t['entry_line'],t['default_component']) for t in x['target_file_candidates']),x['status']] for x in nav['omitted_branches']])
txt += '\nHome uses truthiness of `user` from useAuth;no extra authorization predicate is inferred. Notification seller branches require `n.data?.seller`;Restaurant additionally requires matchingorder_kind,the other seller branch requires its negation. Notification `open(n)` can POST a read marker and update local state before navigation;it was not invoked. Orders branch uses the item kind,not an extra invented role guard. The already recorded Restaurant alternative is `/restaurant/orders/[id]` with `{id:item.id}`. No id validity or ownership was exercised.\n\n'
txt += '## Href attributes\n\n' + table(['ID','Source / expression','Base target / candidate','Classification / scope'], [[
 x['claim_id'],link(x['source']['path'],x['source']['line'])+' '+x['source']['href_expression'],x['target_or_base']+' '+ '; '.join(link(t['path'],t['entry_line']) for t in x['target_file_candidates']), x['status']+'; '+x['scope'] + (' '+json.dumps(x['dynamic_query_mapping'],ensure_ascii=False) if x.get('dynamic_query_mapping') else '')] for x in nav['href_attributes']])
txt += '\n## Fourteen dynamic router arguments\n\nSource classification includes12entity-template occurrences,one unbounded auth next,and one finite RestaurantNav route list. Parameter values,encoding,permissions and actual rendering/navigation remain untested.\n\n'
txt += table(['ID','Source / argument','Lexical conditions','Route pattern / files','Classification / remaining evidence'], [[
 x['claim_id'],link(x['source']['path'],x['source']['line'])+' '+x['source']['argument'],json.dumps(x['all_lexical_ancestor_conditions'],ensure_ascii=False),
 (x.get('static_route_pattern') or 'No single static pattern')+' '+ '; '.join(link(t['path'],t['entry_line']) for t in x.get('target_file_candidates',[]))+' '+ '; '.join(y['target']+': '+', '.join(link(t['path'],t['entry_line']) for t in y['candidates']) for y in x.get('finite_targets',[])),
 x['status']+'; '+x.get('open_question',x['limits'])] for x in nav['dynamic_arguments']])
txt += '\n`_layout` files compose route trees,`+html` is a document helper and`+not-found` is a fallback. File-derived pseudo-path fields for these are not ordinary navigable-page acceptance. This corrects documentation only;no source route was changed.\n\n'
txt += f'''## Complete API source inventory:179registrations

All179explicit method/path/function triples match the old inventory. No duplicate method/path pairs were found within the parsed application decorators. This does not inspect dynamic runtime registrations or mounted external apps. Source SHA-256: `{api['counts']['source_sha256']}` for {link(APP/'backend/server.py')}. No application import,OpenAPI generation,dependency execution or request occurred.

There are387signature parameters,216with Python defaults,27Queryparameters across19endpoints,and60BaseModel declarations. Only4endpoints declare an explicit response_model. None of these counts proves runtime validity or full ownership/security coverage. Full structured source metadata: {link(HERE/'complete-api-inventory.json')};extractor: {link(HERE/'extract-complete-api.py')}. Model fields/defaults/validators are preserved in that JSON and summarized after the179rows.

The table preserves exact argument annotations/default expressions,including Query/Body/Form/File/Depends declarations. **Python default presence is not HTTP optionality**:File(...)/Form(...) are required despite Python defaults. Request model constraints,Annotated metadata and manual request reads also matter. No generated OpenAPI requiredness was asserted. Response columns show declared decorators,return annotations,direct exception sites and return expressions. Helper-raised errors,dependency errors,implicit framework422validation,conditional serialization and actual wire contracts are not exhaustively inferred and remain UNVERIFIED.

'''
for i,e in enumerate(api['endpoints'],1):
    txt += f"### API-{i:03d} — {e['method']} `{e['path']}`\n\n"
    txt += f"Classification: **VERIFIED — source declarations only**. Function `{e['function']}`; {link(APP/'backend/server.py',e['line'])}.\n\n"
    txt += '```python\n'+ e['function']+'('+e['signature_arguments']+')'+ (' -> '+e['return_annotation'] if e['return_annotation'] else '') +'\n```\n\n'
    txt += 'Request declarations: ' + ('; '.join(e['request_models']) or 'No directly annotated inventoried model') + '. Dependencies: ' + json.dumps(e['dependencies'],ensure_ascii=False) + '. Manual request-body reads: '+json.dumps(e['manual_request_body_reads'],ensure_ascii=False)+'.\n\n'
    txt += 'Declared response_model: `'+ str(e['declared_response_model'])+'`;return annotation: `'+str(e['return_annotation'])+'`;status_code decorator: `'+str(e['declared_status_code'])+'`.'
    txt += ' Other explicit response declarations: '+json.dumps(e['declared_response_details'],ensure_ascii=False)+'.\n\n'
    txt += 'Direct HTTPException sites: '+json.dumps(e['direct_HTTPException_sites'],ensure_ascii=False)+'.\n\n'
    txt += 'Return expressions (source branches,not a validated schema): '+json.dumps(e['return_expression_sites'],ensure_ascii=False)+'.\n\n'
txt += '## Sixty model declarations and constraints\n\nEvery field annotation/default/Field expression and validator body below is source-only. The set includes request,response and base classes;60does not mean60HTTP request bodies.\n\n'
for name,m in api['request_models'].items():
    txt += '### Model `'+name+'`\n\n**VERIFIED — source declarations only**;bases: `'+', '.join(m['bases'])+'`;'+link(APP/'backend/server.py',m['line'])+'.\n\n'
    txt += table(['Field','Annotation','Default / constraints','Source line'],[[f['name'],f['annotation'],f['default_or_constraints'],link(APP/'backend/server.py',f['line'])] for f in m['fields']])+'\n'
    if m['validators']:
        txt += 'Validator source metadata:\n\n```json\n'+json.dumps(m['validators'],indent=2,ensure_ascii=False)+'\n```\n\n'
txt += '## GET probe side effects — no requests executed\n\n' + f"The conservative AST-local call graph inspects81GET handlers. Three have recognized potential Mongo write paths;all81entries and the analysis are in {link(HERE/'get-side-effect-inventory.json')} and {link(HERE/'augment-api-effects.py')}. The analysis follows local functions and dependency helpers;unresolved dynamic/external effects mean the remaining78are **not certified pure**. A potential site is not proof every branch writes.\n\n"
txt += table(['GET endpoint','Handler','Potential direct/transitive write','Classification'], [[e['path'],link(APP/'backend/server.py',e['line'],e['function']),'; '.join(w['receiver']+'.'+w['method']+' via '+w['function']+' '+link(APP/'backend/server.py',w['line']) for w in e['possible_local_transitive_write_sites']),'VERIFIED — source possibility only'] for e in effects['GET_endpoints'] if e['possible_local_transitive_write_sites']])
txt += '\nNo evidence here authorizes a GET probe or marks an API,button,screen,auth boundary or workflow runtime-accepted.\n'
write('FINAL_NAVIGATION_AND_API_INVENTORY.md',txt)

txt = preamble('Final Preservation Verification')
txt += '''## Corrected scope — no backdated coverage

The original Master audit's blanket statement about protecting all inherited evidence/history overstated its actual hash set. That historical assertion stays CONTRADICTED;this new addendum records the exact measurable scope. Three nested baselines must not be treated as one contemporaneous snapshot.

'''
txt += table(['Baseline','Captured file count / composition','What equality proves / limitation'],[
 ['Original audit','8150=8128application+20root+2patch files;zero root/evidence XMLs','Equality is limited to captured bytes after that capture;inherited root/evidence/history excluded.'],
 ['Previous owner review','8476=8150+326root/evidence files;includes39historicalXMLpaths','Current equality proves preservation against this later baseline,not original run/source authenticity.'],
 ['Current dated iteration','8504=8476+28previous-owner-review files','Includes all13original required reports/manifests and priorreview support;new iteration files excluded from its own baseline.']])
txt += f'''
Baselines: {link(AUDIT/'protected-file-hashes-before.json')}, {link(OLD/'preservation-before.json')}, {link(HERE/'preservation-baseline.json')}. Scope reconstruction: {link(HERE/'provenance-gap-dispositions.json')}. The original8150set is a subset of8476,which is a subset of8504.

Actual secret.env files,node_modules/dependency trees,.git internals,selected Python/Expo caches and uploads were excluded from the captures. Covered environment templates and source config bytes are protected;uncaptured runtime settings,deployed secret values,installed dependency state or past integrity are not proven. No secret values were read,printed or written. A current hash cannot retroactively attest missing historical evidence.

## Current verification and Git boundaries

The final verifier checks every one of the8476user-specified protected paths and every one of the8504iteration-baseline paths for existence and byte-identicalSHA-256. It separately checks13required originals,the five canonical checkpoints,the original sourceZIP and inherited patches. Expected result is recorded from actual comparisons in {link(HERE/'verification-results.json')};a mismatch causes nonzero exit,not a pass. The source extraction is outsideGit,so an emptyGitdiff alone is insufficient;the hashes cover its captured files.

Git identity must remain`work`/`{HEAD}`. Before/after porcelain status is compared after excluding **only this new dated iteration**;tracked working-tree and staged diffs must be empty. Existing untracked changes outside the iteration remain unchanged. Full starting and ending status are retained in {link(HERE/'git-status-before.txt')}, {link(HERE/'git-status-resume-20261119.txt')} and {link(HERE/'git-status-after.txt')};tracked diff outputs in {link(HERE/'git-diff-after.txt')} and {link(HERE/'git-diff-cached-after.txt')}. Status is not shortened into an inaccurate clean-repository claim.

No original report,manifest,checkpoint,ZIP,patch,source/configuration/UI/API/authentication/payment/database schema or Git history was edited. Only NEWdated-iteration documentation/evidence/scripts were written. Original files are not silently corrected. NoDBrecord was accessed/changed and no services were restarted or newly probed.

## SHA-256 and reference validation

{link(HERE/'FINAL_REVIEW_MANIFEST.json')} lists the five finalMarkdown documents and all supporting iteration evidence hashes/sizes. Its own hash is kept separately in`FINAL_REVIEW_MANIFEST.sha256` to avoid recursive self-hashing. {link(HERE/'reference-index.json')} covers generated Markdown link targets/line bounds and structured source/input artifact path references. A resolver checks them without running application code. Hash comparison is integrity evidence for these saved bytes,not proof that cited historic tests ran under this source.

The verification command is`python {HERE/'verify-final-review.py'}`;it performs file/JSON/AST/Git/reference checks only. It must be executed successfully before the user-facing final report claims preservation or hash verification. No application tests are part of it.

## Remaining unverified preservation scope

- Uncaptured historical execution states and omitted secret/runtime/dependency files cannot be authenticated retrospectively.
- No unauthorized remote fetch/branch change/reset/checkout was performed;remote main freshness isUNVERIFIED.
- Files newly created outside a historical baseline cannot be retrospectively hash-compared;this iteration's deliberate output set is separately inventoried.
- DB contents,provider accounts,native build hosts and production configuration are outside these file-preservation checks.

These limitations are explicit,not waived. Task1is not approved/closed by preservation success.
'''
write('FINAL_PRESERVATION_VERIFICATION.md',txt)

txt = preamble('Final Owner Decision Readiness')
txt += '''## Recommendation

**B. REVIEW PENDING — EVIDENCE GAPS REMAIN.** The owner can review the improved Task1audit package now,but evidence does not support unconditional task approval. The reviewer is not authorized to approve or close Task1. Task2is not started and no production readiness is claimed.

'''
txt += table(['Owner-review area','Classification','Established evidence','What still prevents acceptance'],[
 ['Workspace identity and captured file preservation','VERIFIED','Expectedwork/HEAD;all captured originals checked by final verifier.','Coverage exclusions and historical provenance remain explicit;see verification-results.json.'],
 ['Navigation source-inventory closure','VERIFIED','Five omitted leaves mapped;113bounded literal occurrences.','Actual UI/button/navigation acceptance is a separateUNVERIFIEDclaim;dynamicnext requires policy/evidence.'],
 ['API signature/constraint documentation','VERIFIED','179registrations,387parameters,216defaults,27Queryparameters,60models.','Runtime request/response/dependency/authorization behavior not tested.'],
 ['Password-reset source concern','VERIFIED','Non-atomic token/password writes;full flow and correct citation scope documented.','HIGH risk staysOPEN/VALIDATIONBLOCKED;source-only review cannot close it.'],
 ['Historical run/source provenance','UNVERIFIED','39historicalXMLs preserved and classified as historical.','Trusted per-run source/command/environment/recordedhash bindings missing.'],
 ['Current database metadata/data/transaction acceptance','PARTIALLY VERIFIED','Saved67declarations match savedmetadata;source patterns and historical subset evidence exist.','No new DBcapture;rawvalidatoroptions/capturetime/current data/financial/recovery evidence incomplete.'],
 ['Other security risk acceptance','PARTIALLY VERIFIED','Eight original patterns retained;severity/exposure caveats recorded.','Owner policies/ingress/revocation/rate/body-limit/load evidence absent.'],
 ['Native Android/iOS builds and devices','BLOCKED','Historicalbundle/autolink/prebuild artifacts are distinguished.','No corresponding successfulcompiled native binary and physical-device acceptance proof supplied;no new tooling/build probe allowed.'],
 ['Actual providerTEST/webhook/refund/externaldelivery','BLOCKED','Local/mocked/source proof identified.','GenuineauthorizedTESTdelivery/reconciliation/settlement and platform evidence unavailable;no currentcredentials/providercalls examined.'],
 ['Production infrastructure acceptance','BLOCKED','Localguards/syntheticTLS/backup reports identified.','ActualauthorizedTLS/CORS/DBroles/secretcustody/backup/log/ingress evidence missing.'],
 ['Operational scope and complete working workflows','PARTIALLY VERIFIED','Existing delivery/guest/replacement pieces and gaps separated.','Owner product/acceptance decisions and approved disposable workflow evidence remain.']])
txt += f'''
## Safe next action — owner decision only

The owner should read {link(HERE/'FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md')} and {link(HERE/'FINAL_SECURITY_VALIDATION_REPORT.md')},acknowledge preservation/provenance limits,and decide the scope of a **separate** isolated password-reset validation proposal. The11proposed checks have not been run and do not authorize tests or fixes. HIGH remainsOPEN/VALIDATIONBLOCKED until adequate evidence and owner disposition exist. Device/provider/production custodians must supply their respective source-bound artifacts if those claims are needed for acceptance. No secrets should be shared in chat.

No acceptance criterion was waived or new canonical task added. Evidence gaps do not automatically prove features absent. Source-present does not mean externally verified. Owner risk acceptance must be explicit;this review supplies neither a personal signature nor approval on the owner's behalf.

## Output package and execution record

The fiveMarkdown reports are linked here;the sixth required file is the manifest:

1. {link(HERE/'FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md')}
2. {link(HERE/'FINAL_SECURITY_VALIDATION_REPORT.md')}
3. {link(HERE/'FINAL_NAVIGATION_AND_API_INVENTORY.md')}
4. {link(HERE/'FINAL_PRESERVATION_VERIFICATION.md')}
5. {link(HERE/'FINAL_OWNER_DECISION_READINESS.md')}
6. {link(HERE/'FINAL_REVIEW_MANIFEST.json')}

Every input/output hash,source reference and actual static verification command is retained in the manifest/supporting evidence. Fresh application tests:0. Fresh DBoperations:0. Fresh provider/native/browser operations:0. No application source/configuration/UI/API/database/Git-history changes. Original five checkpoints remain untouched per the latest preservation instruction;durable progress/resume information lives only in the new {link(HERE/'ITERATION_CHECKPOINT.md')}.

## Owner checklist

- [ ] Read the5finalreports and newmanifest;confirm automated preservation/reference/hash verification.
- [ ] Acknowledge that original3contradicted documentation claims are preserved and corrected only additively.
- [ ] Review unresolvedHIGHSEC-01and its preconditions;no automatic closure.
- [ ] Decide whether to authorize isolated future validation;no tests or implementation start until separately authorized.
- [ ] Decide operational scope and the remaining historical/runtime/device/provider/production evidence requirements.
- [ ] Personally record any eventual approval/limitations;this iteration remainsREVIEWPENDINGand does not authorizeTask2.

REVIEW PENDING
'''
write('FINAL_OWNER_DECISION_READINESS.md',txt)

# The original checkpoints must not be overwritten;append progress only here.
with (HERE/'ITERATION_CHECKPOINT.md').open('a') as f:
    f.write(f'''\n## {NOW} — source evidence gap closure saved\n\nProject: COME-IN. Repository `{REPO}`; application `{APP}`; branch `work`; HEAD `{HEAD}`. Current task: Phase 1 Task 1 final owner review; not approved or closed. All 13 inputs were fully read. Added five final Markdown reports, the complete 179 API signature/default/Query/model source inventory, five omitted navigation leaves, 20 gap and 93 claim dispositions, a ten-stage reset trace with 11 NOT EXECUTED test proposals, and bounded GET side effects (81 GETs / three potential write paths). Source counts are not runtime acceptance. HIGH SEC-01 remains OPEN / VALIDATION BLOCKED. No application tests, DB queries/writes, provider/native/browser calls, installs, configuration or source changes. Historical backend 558 passed / 6 skipped, TypeScript 0 errors and ESLint 0 errors / 10 warnings were NOT RERUN.\n\nFiles modified: only new iteration documentation/supporting scripts/evidence; all original reports and checkpoints untouched. Services, current database and credentials were not probed; no environment changes. Next operation: run `python {HERE/'verify-final-review.py'}` for 8,476 protected and 8,504 iteration hash comparisons, 13 original reports and five checkpoint preservation, branch/HEAD, status/diff, references and manifest checks. If verification fails, record the exact failure without changing originals. Safe to rerun: yes, the verifier reads original files and writes only new iteration verification artifacts; it never runs application tests.\n\nAfter verification, stop for owner review. Pending: runtime atomicity, source-bound historical provenance, current DB validation, working buttons/dynamic next, native-device/provider TEST/production evidence and owner policies. No Task 2 or fixes are authorized.\n\nNEXT_SESSION_RESUME_PROMPT:\nRead all 13 original audit/owner-review files and all six final review files in `{HERE}` first, then ITERATION_CHECKPOINT.md, verification-results.json and final-gap-ledger.json. Inspect repository identity `work` / HEAD `{HEAD}`, Git status and preservation before continuing. Verify the last recorded operation; never assume an unrecorded operation succeeded. Preserve all originals and checkpoints. Do not rerun application tests, change source/configuration/database or fetch external resources. HIGH SEC-01 remains OPEN / VALIDATION BLOCKED; Task 1 REVIEW PENDING, not approved or closed. Wait for the owner's explicit decision on scoped future work; do NOT start Task 2. Update only the new iteration checkpoint after meaningful authorized progress.\n''')

print(json.dumps({'created_five_final_reports':True, 'gap_classifications':dict(Counter(x['classification'] for x in gaps)),
 'claim_denominator':len(claims), 'claim_counts':dict(Counter(x['classification'] for x in claims)),
 'next':'Run standalone file/Git/reference/hash verifier;no application tests.'}))
