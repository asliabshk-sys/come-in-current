"""Read/verify candidate receipts and save new-only SEC05/09 evidence."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import ast,hashlib,json,xml.etree.ElementTree as ET

P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(n):return json.loads((P/n).read_text())
def save(n,d):(P/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def counts(n):
 c=list(ET.parse(P/n).getroot().iter('testcase'))
 return {'PASS':sum(all(x.find(k) is None for k in ('failure','error','skipped')) for x in c),'FAIL':sum(x.find('failure') is not None for x in c),'ERROR':sum(x.find('error') is not None for x in c),'SKIPPED':sum(x.find('skipped') is not None for x in c)}
before=load('roles-before.json');after=load('roles-after.json');meta=load('candidate-metadata.json')
assert before['counts']==counts('roles-before.xml')=={'PASS':10,'FAIL':17,'ERROR':0,'SKIPPED':0}
assert after['counts']==counts('roles-after.xml')=={'PASS':27,'FAIL':0,'ERROR':0,'SKIPPED':0}
assert before['runner_SHA256']==after['runner_SHA256']==sha(P/'validate_roles_diagnostics.py')
assert before['source_SHA256']==before['source_SHA256_after']==meta['source_base_SHA256']
assert after['source_SHA256']==after['source_SHA256_after']==sha(P/'server.candidate.py')==meta['candidate_SHA256']
cases={x['id']:x for x in after['cases']}
assert all(cases[i]['observations']['remaining_admins']>=1 for i in ('R06','R07','R08','R09'))
now=datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
result={'project':'COME-IN','timestamp_Asia_Kolkata':now,'scope':'Isolated candidate SEC05/SEC09 only;root owns production merge/final regression',
 'source_before_SHA256':before['source_SHA256'],'candidate_SHA256':after['source_SHA256'],'runner_SHA256':after['runner_SHA256'],
 'changed_source_nodes':meta['changed_AST_nodes'],'production_source_edited_by_this_agent':False,
 'candidate_status':'PASS','before_counts':before['counts'],'candidate_after_counts':after['counts'],
 'findings':[{'id':'SEC-05','severity':'MEDIUM','classification':'Confirmed source/runtime authorization and validation defect',
              'candidate_status':'PASS','change':'Admin-only existing status POST/GET;request client_name1..256;public health and historical response records unchanged.',
              'test_ids':['D01','D02','D03','D04','D05','D06','D07','D08','D09','D10','D11','D12','D13','D14','D15']},
             {'id':'SEC-09','severity':'MEDIUM','classification':'Confirmed controlled real-Mongo concurrent last-admin invariant failure before fix',
              'candidate_status':'PASS','change':'One security_locks shared guard write inside existing transaction before fresh actor/target/count/update;all user operations same session.',
              'test_ids':['R01','R02','R03','R04','R05','R06','R07','R08','R09','R10','R11','R12']}],
 'schema_delta':meta['schema_delta'],'no_destructive_migration':True,'global_failpoints':0,'DB_drops':0,'actual_provider_calls':0,
 'test_databases_retained':before['retained_databases']+after['retained_databases'],
 'concurrency_observations':{i:cases[i]['observations'] for i in ('R06','R07','R08','R09','R10')},
 'limits':after['limits'],'source_reference_note':'Line references in before/candidate receipts identify exact captured source state,not a claim root production merge already occurred.',
 'next_action':'Parent sequentially merges these four AST-node changes and runs final actual-source regression. Do not startTask2/provider/native work.'}
save('SEC05_SEC09_RESULTS.json',result)
text=f'''# SEC-05 / SEC-09 isolated candidate correction report

COME-IN Phase1 Task1. Recorded {now} (Asia/Kolkata). Production source remains owned by the parent merge workflow;this workstream changed only a new isolated candidate and new evidence.

**Same27tests:before10PASS/17FAIL/0ERROR/0SKIP → candidate27PASS/0FAIL/0ERROR/0SKIP.** Both source hashes and the identical runner hash were checked against JSON and JUnit. The tests write only retained unique disposable loopbackMongoDB databases;no production/customer data,provider/native execution,global failpoint or database drop.

## SEC-05 — MEDIUM — candidate PASS

Original finding:anonymous `/api/status` POST accepted unbounded diagnostic names and shared GET exposed the feed. Candidate keeps both routes and response shape but uses existing `require_role("admin")` for each. Anonymous receives401;customer/shopkeeper/delivery partner403. Existing public `/api/` health remains200/read-only. Admin status create/read remain200. `StatusCheckCreate.client_name` now requires1..256characters;missing/empty/257characters reject422before storage. Response `StatusCheck` remains unchanged,so a prior300-character stored record still reads successfully for an admin. No old diagnostic rows are deleted or truncated.

This is the owner-authorized minimum security boundary;no diagnostic UI or business route is removed. Retention and upstream ingress policies are not newly certified by these tests. ASGI identity is supplied through a clearly synthetic authentication dependency;the actual source role dependency and handler/model bodies execute. Full JWT/production-ingress acceptance belongs to root integration/security work.

## SEC-09 — MEDIUM — candidate PASS

Before-source count-then-write race is now reproduced on realMongoDB,not merely a collection double. Tests hold old nontransactional count reads before writes;two/four already privileged admins then cross-demote each other and leave zero admins. This remains a controlled local schedule with synthetic accounts,not a production attack or privilege escalation.

Candidate initializes a dedicated `security_locks` control document `_id="admin-role-mutations",version=0` safely. A duplicate initial-upsert race is tolerated only when the expected guard record exists. Inside the unchanged `run_transaction` helper it first increments that shared guard,then rereads the actor as a currentadmin,reads the target,checks last-admin count,writes the role and reads the response using the same session. A competing transaction must retry on the shared document;merely wrapping independent user documents/counts in snapshot transactions would not suffice.

The current actor check rejects an already-demoted in-flight actor403. Existing self-demotion409,target404,legitimate customer→shopkeeper updates and customer→admin promotions remain. All response password fields stay excluded. User data/schema is not migrated;one related metadata collection/document is added with the implicit unique `_id` index. A deployment using restrictive collection grants must grant this normal control-document access;no production permission/configuration was changed here.

Both two-admin and four-admin tests run with the guard initially absent and already present. After candidate execution every cohort retains at least one admin;no generic500or duplicate-upsert failure occurs. A fault after the real user write rolls back user role and guard version;clean retry succeeds. Transaction-session unavailability fails closed. Tests do not barrier the transactional count read,because correct serialization would deadlock such a test;the invariant and actual persisted roles are checked after all concurrent calls instead.

## Exact candidate delta and evidence

- `server.candidate.py`:full isolated source copy,only `StatusCheckCreate`, `create_status_check`, `list_status_checks`, `admin_update_user_role` differ.
- `SEC05_SEC09_CANDIDATE.patch`:complete source patch for parent review/sequential merge.
- `candidate-metadata.json`:AST-node scope;noimports changed;SEC-01reset function unchanged.
- `roles-before.json/xml/log`, `roles-after.json/xml/log`:all27cases,commands,timestamps,source/runner hashes,real-Mongo observations and54retained database names.
- `SEC05_SEC09_RESULTS.json`:machine-readable final summary.
- `validate_roles_diagnostics.py`:same executable intended-invariant runner for both source states.

Before sourceSHA256:`{before['source_SHA256']}`.

Candidate sourceSHA256:`{after['source_SHA256']}`.

RunnerSHA256:`{after['runner_SHA256']}`.

No original reports/checkpoints/ZIPs,application source,other security finding,UI/schema migration,dependency or Git history was modified by this workstream. Android,iOSand actualRazorpayvalidation remainDEFERREDand were not executed.

Next:parent merges the four-node candidate,then reruns actual-source integration/regression. Candidate success alone is not Task1owner approval or a claim production has already changed. No tests remain running.
'''
(P/'SEC05_SEC09_CANDIDATE_REPORT.md').write_text(text)
save('checkpoint.json',{'timestamp_Asia_Kolkata':now,'last_completed_operation':'Candidate27casebefore/afterrun and source/runner/XML/hash verification complete.',
 'before':before['counts'],'after':after['counts'],'production_edits':0,'candidate_scope':meta['changed_AST_nodes'],
 'next':'Parent sequential merge and actual-source regression;do not rerun this baseline without a reason. No operation running/interrupted. Original evidence preserved.'})
files=[p for p in sorted(P.iterdir()) if p.is_file() and p.name!='artifact-hashes.json']
save('artifact-hashes.json',{'timestamp':now,'files':[{'file':p.name,'bytes':p.stat().st_size,'SHA256':sha(p)} for p in files],
 'self_excluded':True,'production_source_edited':False})
for x in load('artifact-hashes.json')['files']:assert sha(P/x['file'])==x['SHA256']
print(json.dumps({'candidate_status':'PASS','before':before['counts'],'after':after['counts'],'artifacts_verified':len(files),'candidate_SHA256':after['source_SHA256']}))
