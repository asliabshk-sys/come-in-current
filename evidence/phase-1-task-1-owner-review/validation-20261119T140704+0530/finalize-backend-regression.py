"""Compile already executed regression results;no application/test execution."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter,defaultdict
import hashlib,json,shlex

OUT=Path(__file__).resolve().parent
APP=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
HEAD='a223290a8866a1ebeaac982f546491fdc197ae7a'
offline=json.loads((OUT/'backend-offline-result.json').read_text())
local=json.loads((OUT/'backend-local-result.json').read_text())
frontend=json.loads((OUT/'frontend-validation.json').read_text())
legacy=json.loads((OUT/'backend-legacy-result.json').read_text()) if (OUT/'backend-legacy-result.json').exists() else None

def link(p,label=None):return f'[{label or Path(p).name}](<{p}>)'
def command(c):return shlex.join(c)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+[
        '| '+' | '.join(str(x).replace('|','\\|').replace('\n','<br>') for x in row)+' |' for row in rows])+'\n'

assert offline['exit_code']==0 and not offline['source_changed']
assert not local['source_changed'] and local['isolated_backend_stopped']
assert all(x['exit_code']==0 for x in local['records'])
all_cases=offline['cases']+[case for rec in local['records'] for case in rec.get('cases',[])]+(legacy.get('cases',[]) if legacy else [])
counts={s:sum(x['status']==s for x in all_cases) for s in ['PASS','FAIL','SKIPPED']}
module_counts=defaultdict(Counter)
for case in offline['cases']:
    module_counts[case['class']][case['status']]+=1
skip_cases=[case for case in offline['cases'] if case['status']=='SKIPPED']
opt_in_skips=[x for x in skip_cases if x['class'].endswith(('test_payment_webhook_local_integration','test_grocery_refund_local_integration'))]
assert len(opt_in_skips)==2
test_bindings=[]
for p in sorted((APP/'backend/tests').glob('*.py')):
    test_bindings.append({'path':str(p),'sha256':sha(p)})

data={'project':'COME-IN','recorded_Asia_Kolkata':datetime.now(ZoneInfo('Asia/Kolkata')).isoformat(),
 'repository':'/workspace/come-in-current','branch':'work','HEAD':HEAD,'application_path':str(APP),
 'scope':'Fresh existing safe backend/source-contract regression plus isolated ASGI/Mongo/HTTP integration. Does not include the separately owned password-reset/security tests.',
 'status':'FAIL — legacy suite exposed unchanged source/fixture contract mismatches;other executed selections pass' if legacy else 'PASS for executed regression selections;unexecuted/native/provider/production gates not promoted',
 'offline':{'result_file':'backend-offline-result.json','log':'backend-offline.log','junit':'backend-offline.xml',
            'counts':offline['counts'],'exit_code':offline['exit_code'],'command':offline['command']},
 'local_suites':local['records'],'execution_counts':counts,
 'unique_existing_case_counts':{'PASS':counts['PASS'],'FAIL':counts['FAIL'],'SKIPPED':counts['SKIPPED']-2},
 'unique_count_basis':'The two opt-in local payment/refund cases skipped in offline invocation were then executed successfully once in opt-in local invocation. Deduplicate those two skip occurrences;four optional-parser skipped cases remain,plus the additional legacy object-storage skip when that suite is included. Four live-module copies and the legacy copy are byte-identical to their originals and occur only in their respective live execution.',
 'offline_skipped_cases':skip_cases,
 'legacy_remote_suite':({'path':str(APP/'backend/tests/backend_test.py'),'status':'FAIL','result_file':'backend-legacy-result.json',
                        'log':'backend-legacy.log','junit':'backend-legacy.xml','counts':legacy['counts'],'exit_code':legacy['exit_code'],
                        'pytest_failure_elements':sum(c.get('node_kind')=='failure' for c in legacy['cases']),
                        'pytest_error_elements':sum(c.get('node_kind')=='error' for c in legacy['cases']),
                        'source_and_contract_assessment':'Duplicate registration409 contradicts legacy400 expectation. Required ProductIn.description absent from shared created_productfixture causes3setup errors. Legacy product-deletecreation omitsdescription/category_id then assumesid,causingKeyError. These are actual unsuccessful tests;no assertions rewritten. Order endpoint calls inside two fixture-dependent cases never reached.'}
                       if legacy else {'path':str(APP/'backend/tests/backend_test.py'),'status':'NOT RUN','reason':'No corresponding local legacy execution recorded.'}),
 'frontend_summary':[{k:v for k,v in c.items() if k not in {'environment'}} for c in frontend['checks']],
 'frontend_details':'frontend-validation.json','source_bindings':offline['source_before'],'test_source_bindings':test_bindings,
 'current_source_hashes_still_match':all(sha(p)==h for p,h in offline['source_before'].items()) and (not legacy or not legacy['source_changed']),
 'isolated_databases_retained':True,'isolated_backend_stopped':True,
 'production_or_real_customer_operations':0,'real_external_provider_operations':0,'source_config_or_assertion_changes':0,
 'historical_boundary':'Historical558PASS6SKIP is not a fresh count. Current574PASS6SKIP offline reflects actual present test tree;new run is bound to file hashes and commands. HEAD identifies repositoryarchive,not the modified extraction by itself.'}
assert data['current_source_hashes_still_match']
(OUT/'backend-regression.json').write_text(json.dumps(data,indent=2)+'\n')

text=f'''# Complete Regression Validation Report

Project: COME-IN. Recorded {data['recorded_Asia_Kolkata']} (Asia/Kolkata).
Repository `/workspace/come-in-current`; branch `work`; HEAD `{HEAD}`.
Application source: `{APP}` (archive extraction outside Git).

This report records newly executed safe existing regression checks. Source/configuration/test assertions were not modified, dependencies were not installed, and no production/customer/provider operation was performed. No tests are rerun by this report compiler. Password-reset/security audit tests are reported separately and are **not** included in the totals below. The owner has not approved Task 1 and Task 2 was not started.

## Fresh backend and integration results

'''
text+=table(['Selection','PASS','FAIL','SKIPPED','Exit','Evidence'],[
 ['Offline backend and source-contract suite',offline['counts']['PASS'],offline['counts']['FAIL'],offline['counts']['SKIPPED'],offline['exit_code'],link(OUT/'backend-offline.xml')+'; '+link(OUT/'backend-offline.log')],
 ['Actual local ASGI + Mongo;provider mocks',local['records'][0]['counts']['PASS'],local['records'][0]['counts']['FAIL'],local['records'][0]['counts']['SKIPPED'],local['records'][0]['exit_code'],link(OUT/'backend-local-payments.xml')+'; '+link(OUT/'backend-local-payments.log')],
 ['Four existing live suites;isolated HTTP + Mongo',local['records'][1]['counts']['PASS'],local['records'][1]['counts']['FAIL'],local['records'][1]['counts']['SKIPPED'],local['records'][1]['exit_code'],link(OUT/'backend-live.xml')+'; '+link(OUT/'backend-live.log')]]+
 ([['Additional unchanged legacy suite;fresh isolated HTTP + Mongo',legacy['counts']['PASS'],str(legacy['counts']['FAIL'])+' (2 assertion failures +3 fixture errors)',legacy['counts']['SKIPPED'],legacy['exit_code'],link(OUT/'backend-legacy.xml')+'; '+link(OUT/'backend-legacy.log')]] if legacy else []))
text+=f'''
Invocation totals: **{counts['PASS']} PASS / {counts['FAIL']} FAIL / {counts['SKIPPED']} SKIPPED**. Two skip occurrences were deliberate offline opt-outs that subsequently passed in the local opt-in run. Deduplicated existing test-case outcomes are therefore **{counts['PASS']} PASS / {counts['FAIL']} FAIL / {counts['SKIPPED']-2} SKIPPED**. JavaScript assertions, compiler/lint/build checks and separately owned new security tests are not added to this pytest denominator.

The previous558PASS/6SKIP backend claim remains historical. This run observed the present suite, not a reconstruction of the old run. Exact current commands, start/end UTC times, all cases, Python/platform, source/test hashes and exit codes are in {link(OUT/'backend-offline-result.json')}, {link(OUT/'backend-local-result.json')} and {link(OUT/'backend-regression.json')}. Fresh evidence is reproducible from the retained new runners;reruns must use fresh output paths/unique DBs rather than overwrite these logs.

## Commands actually executed

Launcher1:

```sh
/workspace/come-in-tools/py311/bin/python {OUT/'run_backend_regression.py'}
```

It executed, in `{APP/'backend'}`:

```sh
{command(offline['command'])}
```

Launcher2:

```sh
/workspace/come-in-tools/py311/bin/python {OUT/'run_local_backend_validation.py'}
```

It executed both local commands below and started/stopped the isolated application with `local_backend_bootstrap.py`. The fixture seeding command was the byte-identical `live-tests/seed_preview_test_accounts.py`; fixture credentials existed only in process memory/environment and were not written to source, reports or command text.

'''
for rec in local['records']:text+='```sh\n'+command(rec['command'])+'\n```\n\n'
if legacy:
    text+='Additional necessary legacy coverage check (executed once;previous574/70/local selections were not rerun):\n\n```sh\n/workspace/come-in-tools/py311/bin/python '+str(OUT/'run_legacy_backend_validation.py')+'\n'+command(legacy['command'])+'\n```\n\n'
text+='## Isolation and safety review\n\n'
text+=f'''- Inspected existing `backend/pytest.ini` (required pytest-xdist;`-n0` used as its documented serial override), found no conftest, reviewed import/network/subprocess/db patterns across all test modules. The four HTTP suites and legacy module were excluded from offline collection. The two explicit local opt-in cases remained skipped in that offline process.
- Offline socket guard denied all Python socket connections. No pytest cache or application bytecode was written: `-p no:cacheprovider`, `PYTHONDONTWRITEBYTECODE=1`;all temporary fixtures were allocated in this new evidence iteration. Reviewed backup/restore subprocess tests use fake dump binaries or preflight refusal paths, not actual DB backups/restores.
- Local runners whitelist required OS metadata and inject new test-only environment values. Actual dotenv loading is disabled before importing the unmodified application. External provider variables are absent. The local socket guard allows only localhostMongo27018 and the allocated loopback HTTP port. This is test-process isolation, not a change to production controls.
- Existing opt-in payment/refund modules allocate fresh unique `comein_disposable_test_webhooks_*` and `comein_disposable_test_refund_*` databases, operate via actual ASGI/Motor/PyMongo transactions and mock provider calls in process. These are **not** real Razorpay payment/webhook/refund delivery results.
- The full HTTP server used unique DB `{local['records'][1]['database']}` and loopback port `{local['records'][1]['loopback_port']}`. It used fresh synthetic admin/customer/seller/restaurant fixtures, never the retained application backend8001 or existing acceptance database. The ephemeral backend process was stopped in a `finally` block after the run. Databases were retained;none was dropped. The existing task5teardown deletes only its own synthetic fixtures inside this new test database.
- Four live test modules and their seeder were copied byte-identically into the new iteration. This prevents their fallback relative backend/frontend `.env` loader from finding actual secret files. Explicit process environment supplies all test endpoints and fixture data. Every copied file's SHA-256 equals its original;no assertions were changed. The copy binding is recorded in {link(OUT/'backend-local-result.json')}.
- All captured backend/script source hashes still match the pre-run values. Git HEAD alone cannot bind this extracted source because inherited work exists outside the checkout;the file-hash maps and command/environment scope do.

## Coverage established and limits

The offline selection exercises pure helper behavior,source contracts and in-memory transaction doubles for authentication/role boundaries,input validation,cart/checkout,stock/payment/refund transitions,uploads,notifications,seller/admin/delivery,Grocery,Restaurant and CHAND integration contracts. The live70selection exercises actual HTTP authentication and role guards,customer/seller/admin/restaurant workflows,orders,inventory/measured stock,concurrent transactions,idempotency,measured imports/repeat orders,notifications and rollback paths covered by those tests. Passing these selected cases does not prove every API/button/state or the complete production application.

The local2selection exercises actual local HTTP/ASGI and Mongo consistency with mocked provider ordering/signatures/events/refunds. It includes invalid and duplicate webhook handling,out-of-order state protection,amount mismatch,receipt retry safety,concurrent payment intents,refund authorization,COD exclusion,duplicate prevention,uncertain-provider retry protection,partial/full observed refund reconciliation and validator-injected transaction rollback. Genuine provider settlement/delivery remains externally unverified.

The legacy `tests/backend_test.py` suite was initially deferred,then independently reviewed in full and **executed once** on a second fresh disposable backend/database. Its actual unsuccessful outcomes remain FAIL and are detailed below. No previous passing selection was rerun for this addition. Browser/native-device/provider/production checks are not supplied by this backend run. Exact original53route/179API inventories were reused,not regenerated.

## Skipped cases and reasons

'''
text+=table(['Class','Case','Recorded skip reason','Final disposition'],[
 [c['class'],c['name'],c['reason'],'Passed subsequently in local opt-in run' if c in opt_in_skips else 'SKIPPED — missing optional parser dependency,not a pass'] for c in skip_cases]+[
 [c['class'],c['name'],c['reason'],'SKIPPED — external object storage unavailable;not a pass'] for c in (legacy['cases'] if legacy else []) if c['status']=='SKIPPED'])
if legacy:
    text+=f'''\n## Additional legacy suite:actual failures and source-based disposition

The fresh legacy run recorded **17PASS /2assertionFAIL /3fixtureERROR /1SKIPPED**,exit1. Normalized PASS/FAIL/SKIP accounting is17/5/1;five unsuccessful case outcomes are not five unique application vulnerabilities. The full original module and `STALE_CONTRACT_TESTS.txt` were inspected;that list contains **no backend_test.py entries** and was not used to skip or alter this run. All23unchanged tests were collected. Test-copy SHA-256 equals the original. A fresh isolated database `{legacy['database']}` and backend port `{legacy['port']}` were used;the backend stopped and DB was retained without drops.

The current source requires ProductIn.description at {link(str(APP/'backend/server.py')+':487','server.py:487')} and category_id at {link(str(APP/'backend/server.py')+':486','server.py:486')};the legacy shared product fixture omitsdescription at {link(str(APP/'backend/tests/backend_test.py')+':195','backend_test.py:195')}. This produces422before product creation and three dependent fixture errors. The legacy delete test omitsbothdescription andcategory_id at {link(str(APP/'backend/tests/backend_test.py')+':227','backend_test.py:227')},then blindly indexesid atline229,causingKeyError. It is not evidence that a valid product delete request failed. The duplicate-registration endpoint explicitly returns409 at {link(str(APP/'backend/server.py')+':859','server.py:859')};the legacy test expects400 at {link(str(APP/'backend/tests/backend_test.py')+':80','backend_test.py:80')}.

These source declarations and observed responses support a legacy/current contract mismatch classification. They are **not converted to PASS**,and no assertion or source was changed. Whether to update legacy contract expectations requires owner authorization;this validation does not change policy. The two order cases errored during product-fixture setup,so their order API calls were **not reached**. Missing quote/idempotency requirements are visible in current order source but were not demonstrated by those two legacy cases. No duplicate whole-suite rerun is needed merely to preserve these failures.

Synthetic fixture passwords/JWT representations were redacted from the retained legacy log and XML;assertions,outcomes and source files remain unchanged. The valid upload case skipped because object storage was unconfigured/returned503;actual object delivery remains BLOCKED.

'''
    text+=table(['Case','Actual outcome','Observed cause / evidence'],[[c['name'],c['node_kind'].upper() if c.get('node_kind') else c['status'],c['reason']] for c in legacy['cases'] if c['status']=='FAIL'])
text+='\n## Offline module coverage and exact case counts\n\n'
text+=table(['Module','PASS','FAIL','SKIPPED'],[[name,c.get('PASS',0),c.get('FAIL',0),c.get('SKIPPED',0)] for name,c in sorted(module_counts.items())])
text+='\n## Fresh frontend checks owned by the frontend validation workstream\n\n'
text+=table(['Check','Actual command','Result','Evidence / limit'],[
 [c['id'],c['command'],c['result']+(' (0 errors,10warnings)' if c['id']=='FE-ESLINT' else ''),link(c['stdout_log'])+'; '+c['scope']] for c in frontend['checks']])
text+=f'''
Fresh TypeScript: **0 errors**. Fresh ESLint: **0 errors /10warnings**,with no fixes or rule suppression. Existing CHAND planner stdout reports11assertions;the frontend report explicitly distinguishes13source assertion sites rather than inflating counts. Native adapter VM test has5mock scenarios and config guards9checks. Actual Expo web export completed successfully from source-hash-bound scratch copies;it is not native compilation or browser/device acceptance. The95frontend-source binding and full diagnostics are in {link(OUT/'frontend-validation.json')} and {link(OUT/'FRONTEND_VALIDATION_NOTES.md')}.

## Final regression disposition

**FAIL for complete existing regression coverage because the unchanged legacy suite has five unsuccessful case outcomes.** The reviewed offline574andlocal72selections passed;the additional legacy17passes do not erase its2assertion failures/3fixture errors. The observed legacy failures match the exact source/fixture contract mismatches above;they do not prove valid checkout or deletion failed. Separate security findings and external gates remain independently open. Task1remains **REVIEW PENDING**,pending owner disposition of security,legacy contract and external evidence. No source fixes,assertion changes,Task2,commit,push,deployment or production operation occurred.
'''
(OUT/'COMPLETE_REGRESSION_VALIDATION_REPORT.md').write_text(text)
print(json.dumps({'backend_report_saved':True,'invocation_counts':counts,'unique_case_counts':data['unique_existing_case_counts'],'frontend_checks':len(frontend['checks']),'source_hashes_match':True}))
