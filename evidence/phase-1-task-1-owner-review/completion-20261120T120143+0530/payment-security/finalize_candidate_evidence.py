"""Compile candidate evidence only;never apply source or call external services."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import ast,hashlib,json,xml.etree.ElementTree as ET

P=Path(__file__).resolve().parent
def read(n):return json.loads((P/n).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(n,d):(P/n).write_text(json.dumps(d,indent=2)+'\n')
def link(n):return f'[{n}](<{P/n}>)'
b=read('before-v2-results.json');a=read('candidate-v2-results.json');m=read('candidate-change-summary.json')
assert b['runner_SHA256']==a['runner_SHA256']==sha(P/'validate_payment_security.py')
assert b['counts']=={'PASS':19,'FAIL':11,'ERROR':0,'SKIPPED':0}
assert a['counts']=={'PASS':30,'FAIL':0,'ERROR':0,'SKIPPED':0}
for phase,data in [('before-v2',b),('candidate-v2',a)]:
 cases=list(ET.parse(P/(phase+'.xml')).getroot().iter('testcase'))
 assert len(cases)==30 and sum(c.find('failure') is not None for c in cases)==data['counts']['FAIL']
 assert not any(c.find('error') is not None for c in cases)
 assert data['source_SHA256']==data['source_SHA256_after']
before=(P/'before-server.py').read_text();candidate=(P/'candidate-server.py').read_text()
t0=ast.parse(before);t1=ast.parse(candidate);nodes=[]
for name in m['changed_functions']:
 n=next(n for n in t0.body if isinstance(n,ast.AsyncFunctionDef) and n.name==name)
 z=next(n for n in t1.body if isinstance(n,ast.AsyncFunctionDef) and n.name==name)
 assert ast.dump(n.args)==ast.dump(z.args)
 assert [ast.dump(x) for x in n.decorator_list]==[ast.dump(x) for x in z.decorator_list]
 nodes.append({'name':name,'before_line':n.lineno,'candidate_line':z.lineno,
 'before_segment_SHA256':hashlib.sha256(ast.get_source_segment(before,n).encode()).hexdigest(),
 'candidate_segment_SHA256':hashlib.sha256(ast.get_source_segment(candidate,z).encode()).hexdigest()})
now=datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
data={'timestamp_Asia_Kolkata':now,'scope':'Candidate source plus local mock verification;parent must apply and run integrated regressions.',
 'candidate_before_SHA256':sha(P/'before-server.py'),'candidate_after_SHA256':sha(P/'candidate-server.py'),
 'candidate_patch':'candidate.patch','changed_functions':nodes,'offload_sites':8,
 'code_level_candidate_status':{'SEC-07':'FIXED in isolated candidate;local mock tests PASS','SEC-08':'FIXED in isolated candidate;boundedrawstream verified'},
 'before_counts':b['counts'],'candidate_counts':a['counts'],'same_corrected_runner_SHA256':a['runner_SHA256'],
 'initial_harness_attempts_retained':{'before':{'PASS':16,'FAIL':12,'ERROR':2},'candidate':{'PASS':26,'FAIL':2,'ERROR':2},
 'cause':'Missing in-memory ledger/event-recorder bindings caused errors and failed fixture checks. Added stubs only;original runner retained;no source/assertion weakened. Do not aggregate attempts.'},
 'actual_provider_validation':'DEFERRED — PENDING SEPARATE PAYMENT TESTING PHASE','Android_iOS_validation':'DEFERRED;no execution',
 'actual_provider_or_network_calls':0,'DB_operations':0,'protected_source_changes_by_workstream':0,'packages_installed':0,
 'limitations':a['limitations']+['Actual routing/dependency/realMongo regressions are parent-owned,not certified by these doubles.',
 'Cancellation cannot abort a started requests thread;existing claimed operation remains pending/unconfirmed and duplicate creation is blocked.',
 'Blocking object-storage helpers are outside this payment I/O finding and were not modified.']}
save('payment-security-results.json',data)
save('merge-plan.json',{'candidate_path':str(P/'candidate-server.py'),'base_path':str(P/'before-server.py'),
 'changed_functions':nodes,'new_imports':[],'new_top_level_functions':[],'new_constants':[],
 'changed_protected_paths_if_accepted':['backend/server.py'],'all_other_AST_nodes_identical':True})

report=f'''# SEC-07 / SEC-08 Candidate Correction and Local Validation

COME-IN Phase 1 Task 1. Recorded {now} (Asia/Kolkata).

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
cd {P}
/workspace/come-in-tools/py311/bin/python -B build_candidate.py
/workspace/come-in-tools/py311/bin/python -B validate_payment_security.py --stage before-v2 --source before-server.py
/workspace/come-in-tools/py311/bin/python -B validate_payment_security.py --stage candidate-v2 --source candidate-server.py
```

Before source SHA-256: `{data['candidate_before_SHA256']}`.
Candidate SHA-256: `{data['candidate_after_SHA256']}`.
Same corrected runner SHA-256: `{a['runner_SHA256']}`.

Candidate/patch/merge plan: {link('candidate-server.py')}, {link('candidate.patch')}, {link('merge-plan.json')}.
Results: {link('before-v2-results.json')}, {link('candidate-v2-results.json')};raw XML/logs are retained alongside them.
Detailed limitations/status: {link('payment-security-results.json')}.

## Safe stopping point

No actual protected source was edited by this workstream. All mock processes finished. Next exact action:parent merges only these seven functions,then runs this harness against merged actual source and the existing localASGI/Mongo payment/refund suites. No real provider/native validation is authorized. Task1 is not approved or closed by this candidate report.
'''
(P/'SEC07_SEC08_CANDIDATE_REPORT.md').write_text(report)
(P/'PAYMENT_SECURITY_CHECKPOINT.md').write_text(f'''# SEC-07 / SEC-08 candidate checkpoint

{now}. Isolated candidate only:seven functions,eight I/O sites. Before19PASS11FAIL to candidate30PASS0FAIL/ERROR/SKIP. Same corrected runner SHA{a['runner_SHA256']}. Candidate SHA{data['candidate_after_SHA256']}. Source/provider/native/config/dependency operations by this workstream:zero. Diagnostic harness attempts retained and disclosed.

Last operation:corrected before/candidate local mock runs,JSON/XML/source/runner consistency verification and report generation. No tests remain running. Next action:parent merges reviewed source and performs integrated regression. Reproduction commands are in SEC07_SEC08_CANDIDATE_REPORT.md. Real Razorpay/Android/iOS remain DEFERRED. Do not infer production readiness or owner approval.
''')
files=[x for x in sorted(P.iterdir()) if x.is_file() and x.name!='payment-artifact-hashes.json']
save('payment-artifact-hashes.json',{'timestamp':now,'scope':'Candidate artifacts;self excluded','files':[{'name':x.name,'bytes':x.stat().st_size,'SHA256':sha(x)} for x in files]})
assert all(sha(P/x['name'])==x['SHA256'] for x in read('payment-artifact-hashes.json')['files'])
print(json.dumps({'before':b['counts'],'candidate':a['counts'],'artifacts':len(files),'report_SHA256':sha(P/'SEC07_SEC08_CANDIDATE_REPORT.md'),'candidate_SHA256':data['candidate_after_SHA256']}))
