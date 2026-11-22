"""Compile and verify this NEW validation package;never edit application/originals."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter
import hashlib,json,re,subprocess,xml.etree.ElementTree as ET

P=Path(__file__).resolve().parent
R=Path('/workspace/come-in-current')
A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
OLD=P.parent/'iteration-2026-11-18T072632-0800'
HEAD='a223290a8866a1ebeaac982f546491fdc197ae7a'
NOW=datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
def load(p):return json.loads(Path(p).read_text())
def save(n,d):(P/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def git(*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(R),*args],text=True)
def l(p,line=None,label=None):
 p=Path(p);return f'[{label or p.name}](<{p}{":"+str(line) if line else ""}>)'
def table(h,rows):
 def c(x):return str(x).replace('|','\\|').replace('\n','<br>')
 return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(c(x) for x in row)+' |' for row in rows])+'\n'
def header(title):return f'''# {title}

COME-IN — Phase 1 Task 1. Recorded {NOW} (Asia/Kolkata).
Repository `{R}`; branch `work`; HEAD `{HEAD}`.
Application extraction `{A}` is outside Git;current source is bound by content hashes,not falsely equated to Git HEAD.

Latest owner instruction authorizes safe local tests and isolated disposable resources,not protected source/configuration fixes. All original reports/checkpoints/ZIP/source are preserved. Only this new validation iteration is written. No production/customer/provider operations,installs,commit,push,deploy or Task 2.

'''

assert git('branch','--show-current').strip()=='work' and git('rev-parse','HEAD').strip()==HEAD
baseline=load(P/'preservation-baseline.json')
bad=[name for name,want in baseline.items() if not Path(name).is_file() or sha(name)!=want]
assert len(baseline)==8533 and not bad, f'Protected mismatch:{bad}'
for oldbase,count in [(OLD/'preservation-baseline.json',8504),(P.parent/'preservation-before.json',8476)]:
 d=load(oldbase);assert len(d)==count and all(sha(n)==h for n,h in d.items())
assert sha(OLD/'FINAL_REVIEW_MANIFEST.json')=='7fbe1ee4d606157421f7192cc69fc0ee59f8fd9409ac655fe1fd4a6a8308b8af'
oldmanifest=load(OLD/'FINAL_REVIEW_MANIFEST.json')
assert len(oldmanifest['files'])==27 and all(sha(OLD/x['relative_path'])==x['sha256'] for x in oldmanifest['files'])
status=git('status','--porcelain=v1','--untracked-files=all')
prefix=str(P.relative_to(R))+'/'
filtered=lambda s:sorted(x for x in s.splitlines() if not x[3:].startswith(prefix))
assert filtered(status)==filtered((P/'git-status-before.txt').read_text()),'Git status changed outside this new iteration'
assert not git('diff','--no-ext-diff','--exit-code') and not git('diff','--cached','--no-ext-diff','--exit-code')
(P/'git-status-after.txt').write_text(status)
(P/'git-diff-after.txt').write_text(git('diff','--no-ext-diff'))
(P/'git-diff-cached-after.txt').write_text(git('diff','--cached','--no-ext-diff'))

source_map={n:h for n,h in baseline.items() if n.startswith(str(A)+'/')}
binding={'timestamp':NOW,'repository_HEAD_context':HEAD,'source_is_exact_Git_HEAD':False,
 'source_note':'Git tracks the original ZIP/README;retained extraction contains preserved later uncommitted work. Current content hashes bind execution,HEAD alone does not.',
 'captured_app_files':len(source_map),'source_tree_fingerprint_SHA256':hashlib.sha256(json.dumps(source_map,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'source_mapping_baseline':str(P/'preservation-baseline.json'),'baseline_SHA256':sha(P/'preservation-baseline.json'),
 'server_py_SHA256':sha(A/'backend/server.py'),'all_captured_source_bytes_unchanged':True,
 'exclusions':'Actual secret.env files,node_modules/dependency trees,.git internals and selected caches/uploads are not retrospective preservation proof. Runtime/process/test DB changes are separately authorized.'}
save('source-state-binding.json',binding)

def xml(name):
 r=ET.parse(P/name).getroot();cases=list(r.iter('testcase'))
 return {'PASS':sum(all(x.find(k) is None for k in ('failure','error','skipped')) for x in cases),'FAIL':sum(x.find('failure') is not None for x in cases),'ERROR':sum(x.find('error') is not None for x in cases),'SKIPPED':sum(x.find('skipped') is not None for x in cases),'total':len(cases)}
suite_specs=[('Existing offline backend/contracts','backend-offline.xml'),('Local ASGI/Mongo payment/refund;providers mocked','backend-local-payments.xml'),('Isolated HTTP/Mongo four-module regression','backend-live.xml'),('Legacy backend,unchanged assertions','backend-legacy.xml'),('Password reset actual functions + real disposable Mongo','password-reset-junit-v2.xml'),('Broad helpers/models;synthetic DB doubles,independent reproduction','broad-security-reproduced.xml')]
suites=[{'scope':s,'artifact':n,**xml(n)} for s,n in suite_specs]
assert [x['total'] for x in suites]==[580,2,70,23,30,50]
totals={k:sum(x[k] for x in suites) for k in ('PASS','FAIL','ERROR','SKIPPED','total')}
assert totals=={'PASS':735,'FAIL':10,'ERROR':3,'SKIPPED':7,'total':755}
unique={**totals,'SKIPPED':totals['SKIPPED']-2,'total':totals['total']-2}
save('current-test-results.json',{'scope':'Six final suite outcomes;not earlier harness attempts. Two offline opt-in skips laterpassed locally,so unique final cases remove those two skip observations.',
 'suites':suites,'invocation_outcomes':totals,'unique_final_case_outcomes':unique,
 'FAIL_semantics':'For owner validation status,the10assertionFAILplus3fixtureERRORare13unsuccessfulcases. Raw XML retains the distinction.',
 'diagnostic_attempts_NOT_summed':['password-reset-junit.xml','broad-security-isolated.xml','broad-security-isolated-v2.xml'],
 'frontend_check_counts':'Six frontend command checks are separate;planner stdout reports11assertions but13assertcall sites were found. JShelper counts are not added to Python testcase totals.'})
sec=load(P/'security-audit.json');assert len(sec['findings'])==9
assert Counter(x['severity'] for x in sec['findings'])==Counter({'HIGH':1,'MEDIUM':6,'LOW':2})
actions=load(P/'consolidated-action-register.json')['actions'];assert len(actions)==20
assert all(x['status'] in {'PASS','FAIL','BLOCKED','NOT RUN','NOT APPLICABLE'} for x in actions),'Wait for final action register statuses'
frontend=load(P/'frontend-validation.json');assert len(frontend['checks'])==6 and all(x['exit_code']==0 for x in frontend['checks'])
native=load(P/'native-provider-validation.json');assert native['final_native_status']=='BLOCKED' and native['final_actual_provider_status']=='BLOCKED'

gates=[]
def gate(i,title,status,evidence,limit):gates.append({'id':i,'validation':title,'status':status,'evidence':evidence,'limit_or_next_action':limit})
for i,title,ev in [('V01','Repository identity','recovery.json'),('V02','Previous manifest and27members','recovery.json'),('V03','8476protected file integrity','final-preservation.json'),('V04','8504previous-iteration baseline integrity','final-preservation.json'),('V05','8533current baseline integrity','final-preservation.json'),('V06','Local MongoDB PRIMARY','db-metadata-current.json'),('V07','67declared indexes match current metadata','db-metadata-current.json'),('V08','Current timestamp/raw relevant DB options captured','db-metadata-current.json'),('V09','Offline backend/contracts','backend-offline.xml'),('V10','Local ASGI/Mongo payment/refund mocks','backend-local-payments.xml'),('V11','Isolated HTTP/Mongo regression','backend-live.xml'),('V12','TypeScript zero-error check','frontend-validation.json'),('V13','ESLint zero-error check','frontend-eslint.json'),('V14','CHAND planner helper check','frontend-planner.log'),('V15','Native SDK adapter VM mock','frontend-native-mock.log'),('V16','Config/command guard checks','frontend-config-guard.log'),('V17','Actual web export','frontend-web-build-execution.json'),('V18','New execution source/provenance binding','source-state-binding.json'),('V19','All20gap dispositions documented','FINAL_EVIDENCE_GAP_DISPOSITION_REPORT.md'),('V20','Android autolinking metadata','android-autolinking-current.stdout'),('V21','iOS autolinking metadata','ios-autolinking-current.stdout')]:
 gate(i,title,'PASS',ev,'Executed bounded check only;not an owner approval,runtime/device/provider guarantee. ESLint retains10warnings;planner count caveat is recorded.' if i in {'V13','V14'} else 'Bounded scope only;see linked report for exclusions.')
for i,title,ev,limit in [('V22','Password-reset security invariants','password-reset-junit-v2.xml','23PASS/7FAIL. SEC01confirmed locally;protected source correction requires owner authorization.'),('V23','Last-admin security invariant','broad-security-reproduced.xml','49PASS/1FAIL;synthetic collection doubles only,privileged concurrency preconditions.'),('V24','Legacy backend contract compatibility','backend-legacy.xml','17PASS/2assertionFAIL/3fixtureERROR/1SKIP;owner reviews409contract and required product fixture fields before any source/assertion edits.')]:gate(i,title,'FAIL',ev,limit)
for i,title,ev,limit in [('V25','Historical per-run exact source/commit attestation','TEST_PROVENANCE_AND_REPRODUCTION_REPORT.md','Missing contemporaneous trusted binding cannot be fabricated or recreated by current hashes.'),('V26','Android native compilation','ANDROID_IOS_NATIVE_VALIDATION_REPORT.md','Missing javac/AndroidSDK/buildtools/Gradle development build prerequisites.'),('V27','Android device acceptance','ANDROID_IOS_NATIVE_VALIDATION_REPORT.md','No emulator/adb/KVM/physical device.'),('V28','iOS native compilation','ANDROID_IOS_NATIVE_VALIDATION_REPORT.md','Linux,no macOS/Xcode/CocoaPods/nativebuild host.'),('V29','iOS device acceptance','ANDROID_IOS_NATIVE_VALIDATION_REPORT.md','No iPhone/simulator/Xcode host.'),('V30','Actual RazorpayTEST payment','RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md','Explicit TESTkey/secret/mode unavailable;no provider call.'),('V31','Actual provider webhook delivery','RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md','TESTwebhook binding/owned delivery endpoint/evidence unavailable.'),('V32','Actual provider refund settlement','RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md','TESTpayment/refund credentials and genuine provider references unavailable.'),('V33','Actual production security/configuration','COMPLETE_APPLICATION_SECURITY_AUDIT.md','No authorized production infrastructure evidence;source/local checks cannot establish it.'),('V34','Four optional parser cases','COMPLETE_REGRESSION_VALIDATION_REPORT.md','Missing pypdf,openpyxl,PIL,fitz;no installation authorized/performed.'),('V35','Legacy object-storage upload case','backend-legacy.xml','Storage provider unconfigured;HTTP503skip is not a passing upload.'),('V36','Personal owner approval/security disposition','TASK_1_OWNER_APPROVAL_CHECKLIST.md','Owner has not authorized fixes or approved/closedTask1.')]:gate(i,title,'BLOCKED',ev,limit)
gate('V37','Every rendered button/state/device workflow','NOT RUN','FINAL_EVIDENCE_GAP_DISPOSITION_REPORT.md','Complete 579-binding/browser/device acceptance matrix was not executed. Static contracts/helpers/API tests are narrower evidence.')
assert all(x['status'] in {'PASS','FAIL','BLOCKED','NOT RUN','NOT APPLICABLE'} for x in gates)
counts=Counter(x['status'] for x in gates)
save('validation-status-register.json',{'denominator':len(gates),'basis':'37named review/validation gates,not unique vulnerabilities or Python testcases. Multiple evidence gates may share a suite. PASS only for the precisely bounded executed statement.',
 'counts':dict(counts),'allowed_statuses':['PASS','FAIL','BLOCKED','NOT RUN','NOT APPLICABLE'],'gates':gates})

txt=header('Final Preservation and Git Audit Report')
txt+=f'''## Result — PASS within the captured scope

All8,476protected files,all8,504previous-iteration baseline files and all8,533current baseline files match their captured SHA-256 values;zero missing paths or mismatches. The current baseline adds the previous iteration's29files to8,504. Original reports,manifests,checkpoints,ZIP and inherited patches remain byte-identical. All captured application source/config/template/test files are preserved. No tracked/staged Git diff;status outside this new validation directory is unchanged. Branch `work` and HEAD `{HEAD}` remain unchanged. No Git history mutation command was used.

Previous manifest SHA-256 remains `7fbe1ee4d606157421f7192cc69fc0ee59f8fd9409ac655fe1fd4a6a8308b8af`;all27member hashes match. This recheck is required after newly authorized tests,not a regenerated route/API inventory.

Evidence: {l(P/'preservation-baseline.json')},{l(P/'final-preservation.json')},{l(P/'source-state-binding.json')},{l(P/'git-status-before.txt')},{l(P/'git-status-after.txt')},{l(P/'git-diff-after.txt')},{l(P/'git-diff-cached-after.txt')}.

## Intentional authorized effects and exclusions

Only new validation reports/tests/logs/exports/manifests/checkpoints were written here. Existing local Mongo container was started after it was found stopped;its known process nofile limit was restored to16,384. No MongoDB rebuild,reset or database drop. Metadata capture read no application records;test writes used uniquely named synthetic disposable databases,retained afterward. Ephemeral test backend processes were stopped. No real customer/provider/production operation. Web export used a scratch source copy and existing pinned dependencies. No packages installed/upgraded or protected configuration changed.

Actual secret.env files,dependency trees,.git internals and selected caches/uploads were excluded from historical hash baselines. Frontend validation separately retained file bindings/metadata;these do not backdate uncaptured configuration or prove production secret custody. Original audit8,150coverage versus later8,476/8,504sets remains qualified in the preserved earlier reports. Current source fingerprint is `{binding['source_tree_fingerprint_SHA256']}` over{binding['captured_app_files']}captured application paths. It binds current preserved extraction bytes,not an assertion that this extraction equals GitHEAD.

## Verification commands and manifest

`python {P/'finalize-task1-package.py'}` verifies identity,status,diffs,all protected bytes,new report references,XML totals and manifest hashes. Git invocations are read-only `git --no-optional-locks` status/branch/rev-parse/diff commands. No reset,clean,checkout,restore,rebase,commit,push or deployment.

{l(P/'TASK_1_FINAL_MASTER_MANIFEST.json')} hashes every new saved artifact except itself/its sidecar;the standaloneSHA-256sidecar avoids self-hash recursion. The verifier must finish successfully before the final message asserts manifest verification. Existing manifests are never refreshed by this program. All original root checkpoints remain unchanged;the new resume checkpoint is the durable stopping record per the current preservation instruction.
'''
(P/'FINAL_PRESERVATION_AND_GIT_AUDIT_REPORT.md').write_text(txt)

txt=header('Consolidated Task 1 Action Register')
txt+='All20inherited evidence-gap IDs are retained;these are not20vulnerabilities or new canonical tasks. The nine security risks below are separate source/security findings,not counts of buttons/APIs.\n\n'
txt+=table(['Finding / gap','Description','Severity / priority','Evidence required','Current status','Validation method','Final disposition'],[[x['id'],x['description'],x.get('severity_or_priority','Owner decision'),x['evidence_required'],x['status'],x['validation_method'],x['final_disposition']] for x in actions])
txt+='\n## Nine security findings\n\n'+table(['ID','Description / source','Severity','Evidence / validation status','Minimal proposed correction / owner action'],[[x['id'],x['symbols']+' '+l(x['source']['path'],x['source']['line']),x['severity'],x['validation_status']+'; '+x['evidence']+' Limits:'+x['preconditions_and_limits'],x['minimal_proposed_correction']] for x in sec['findings']])
txt+='\nAuthoritative action data: '+l(P/'consolidated-action-register.json')+'. No issue is closed by a documentation-only correction.\n'
(P/'TASK_1_CONSOLIDATED_ACTION_REGISTER.md').write_text(txt)

txt=header('Proposed Minimal Corrections — Owner Authorization Required')
txt+='''No protected source was changed. The following proposals are concrete review items,not implemented fixes or altered business policies. Existing failed tests are retained as acceptance evidence;assertions must not be weakened to conceal defects.\n\n'''
txt+=table(['Finding','Confirmed basis / exact source','Minimal correction proposal','Acceptance evidence / decision'],[[x['id'],x['evidence']+' '+l(x['source']['path'],x['source']['line']),x['minimal_proposed_correction'],x['preconditions_and_limits']+' Owner authorization required before any source change.'] for x in sec['findings']])
txt+='''\nAdditional precision:SEC-01requires token claim and user update in one transaction/session with conditional unused/expiry check and matched-user validation;simply marking used before the password write without rollback is insufficient. Handle invalid SMTP configuration before issuing a token or ensure targeted cleanup. SEC-09requires serialized last-admin mutation through a shared guard/versionCAS or equivalent;count-then-write inside snapshot transactions alone can permit write skew across different user documents. Session revocation and long-password compatibility require explicit owner policy and backward-compatibility decisions.\n\nLegacy compatibility is a separate decision:currentduplicate-registration409versuslegacyexpected400;product fixtures omit required description,and delete setup also omits category_id. Decide the intended supported API contract/fixture scope from product requirements before authorizing any test or application changes. This run does not prove an order/guest-workflow defect when setup prevented the HTTP call. The storage-upload skip requires configured nonproduction storage,not an assertion rewrite.\n\nNext authorized stage,if the owner approves:apply the smallest reviewed SEC-01correction on preserved source,run existing failing reset cases without weakening them,then address other approved corrections and scoped regression. No Task2or implementation is started by this proposal.\n'''
(P/'PROPOSED_MINIMAL_CORRECTIONS_REQUIRING_OWNER_AUTHORIZATION.md').write_text(txt)

report_names=['TASK_1_CONSOLIDATED_ACTION_REGISTER.md','PASSWORD_RESET_SECURITY_VALIDATION_REPORT.md','FINAL_EVIDENCE_GAP_DISPOSITION_REPORT.md','TEST_PROVENANCE_AND_REPRODUCTION_REPORT.md','COMPLETE_REGRESSION_VALIDATION_REPORT.md','ANDROID_IOS_NATIVE_VALIDATION_REPORT.md','RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md','FINAL_PRESERVATION_AND_GIT_AUDIT_REPORT.md','COMPLETE_APPLICATION_SECURITY_AUDIT.md','PROPOSED_MINIMAL_CORRECTIONS_REQUIRING_OWNER_AUTHORIZATION.md','TASK_1_FINAL_MASTER_REVIEW_REPORT.md','TASK_1_OWNER_APPROVAL_CHECKLIST.md','TASK_1_FINAL_RESUME_CHECKPOINT.md']
txt=header('Task 1 Owner Approval Checklist')
txt+='''Task1remains **REVIEW PENDING**. Completed evidence work does not satisfy unresolved security,external or personal approval requirements. Only the owner may approve or close Task1.\n\n'''
txt+=table(['Criterion','Evidence / current result','Owner decision'],[
 ['AllA–Jworkstreams examined','Reports/actions/source-bound outputs saved;completed inventories reused.','Review scope/limitations.'],['All20gaps dispositioned','PASS for disposition documentation;underlying open gates retained.','Accept bounded closures and decide outstanding scope.'],['HIGHpassword-reset genuinely validated/resolved','ValidatedFAIL:23PASS/7FAIL;SEC01OPEN,not remediated.','NOT SATISFIED:authorize reviewed minimal fix or explicitly record formal disposition;no hidden risk acceptance.'],['No hiddenCritical/HIGHfinding','1HIGH/6MED/2LOW retained;noCriticalestablished in this bounded audit.','Review severity/preconditions;not an exhaustive production security warranty.'],['Reproducible regression','CurrentXMLs/commands/source hashes;legacy2FAIL/3ERRORpreserved.','Decide legacy contract/fixture alignment and approve any changes.'],['Native/provider limitations','BLOCKED builds/devices/realTESTprovider/production evidence.','Supply authorized environment/custodian evidence.'],['Preservation','PASS8533/8504/8476zero mismatches;oldmanifest27matches.','Review excluded runtime/configuration scope.'],['Newmanifest/hashes','Verified at final program completion;selfhash sidecar.','Confirm SHA-256/readreports.'],['Personal owner approval','NOT GIVEN;Task1notclosed,Task2notstarted.','Owner must record their decision after outstanding mandatory items are resolved/dispositioned.']])
txt+='\n- [ ] Read '+l(P/'TASK_1_FINAL_MASTER_REVIEW_REPORT.md')+' and all linked reports.\n- [ ] Review '+l(P/'PROPOSED_MINIMAL_CORRECTIONS_REQUIRING_OWNER_AUTHORIZATION.md')+'.\n- [ ] Authorize any protected source/test correction explicitly;no automatic implementation.\n- [ ] Provide native/provider/production evidence through authorized custodians;never paste secrets in chat.\n- [ ] Personally decide approval only after applicable mandatory gaps are satisfied or formally dispositioned.\n\nREVIEW PENDING\n'
(P/'TASK_1_OWNER_APPROVAL_CHECKLIST.md').write_text(txt)

txt=header('Task 1 Final Master Review Report')
txt+='''## Overall decision

**REVIEW PENDING — confirmed security and legacy validation failures remain;external validation and owner decisions remain outstanding.** This is the highest currently verified state of the authorized validation workflow,not approval,closure or production readiness. No source fix was authorized or applied. All independent safe workstreams were completed through evidence generation;blocked external gates were not disguised as passes.

Previously completed five navigation branches,179API/default/constraint inventory,60models,20gap disposition and877references were reused,not regenerated. The previous manifest and27entries were checked intact. The latest owner authorization allowed new isolated tests;it did not authorize protected code changes.

## Current executable results

'''
txt+=table(['Scope','PASS','FAIL','ERROR','SKIPPED','Artifact'],[[x['scope'],x['PASS'],x['FAIL'],x['ERROR'],x['SKIPPED'],l(P/x['artifact'])] for x in suites])
txt+=f'''
Six final suite executions produce **{totals['PASS']}PASS,{totals['FAIL']}assertionFAIL,{totals['ERROR']}fixtureERROR,{totals['SKIPPED']}SKIPPED** ({totals['total']}observations). Deduplicating the two offline opt-in skips that laterpassed gives **{unique['PASS']}PASS/{unique['FAIL']}FAIL/{unique['ERROR']}ERROR/{unique['SKIPPED']}SKIPPED across{unique['total']}unique cases**. Under the requested validation status rules,the10assertionfailures and3fixtureerrors are13unsuccessfulcases;rawXMLnever hides their distinction. These totals exclude initial diagnostic attempts and exclude JSassertion counts. Four optional parser dependencies and one object-storage binding remain unavailable.

Existing regression alone:663PASS/2assertionFAIL/3fixtureERROR/7SKIPinvocation outcomes;deduplicated663PASS/2FAIL/3ERROR/5SKIP. Initially omitted legacy tests were reviewed and then safely executed unchanged,not suppressed for being old. Duplicate registration returns409while the legacy test expects400;fixture omissions cause422and three setup errors;delete setup also omits category_id. Downstream order paths not reached by those failed fixtures are not claimed tested or defective.

New reset tests:23PASS/7FAIL on actual extracted functions with real Motor/Mongo and synthetic users/tokens;SMTP/fault scheduling controlled. The HIGH atomicity risk is now a locally reproducedFAIL/OPEN,not merelyVALIDATIONBLOCKED. Concurrent consumers both accepted;second-write failure left password changed/token unused and allowed retry. Other failures cover missing-user false success,invalidSMTP_PORTcleanup,oldJWTpersistence,concurrent throttle overshoot,and bcrypt72-byte suffix alias. Seven cases map to existingSEC01/02/04/06,not seven new vulnerabilities.

New broad helper/model tests:49PASS/1FAIL with synthetic collection doubles. Independent reproduction closes the current command/source-provenance gap;it cannot authenticate the unrecorded originalv2shellcommand. SEC09shows cross-demotion by two alreadyprivilegedadmins can leave zero admins under the controlled model. ActualMongo/adminHTTPconcurrency remains unverified;no arbitrary privilege escalation is claimed.

Frontend:TypeScript0errors;ESLint0errors/10warnings;planner helperPASS(script reports11assertions,13call sites found);nativeadapterVMmock5PASS;config/guard9PASS;actualwebexportPASSfrom a hash-bound scratchcopy with existing dependencies. Allsix frontend commands exited0. These are not browser/allbuttons/nativebinary/provider acceptance. {l(P/'FRONTEND_VALIDATION_NOTES.md')} and {l(P/'frontend-validation.json')} retain exact commands/count caveats/warnings.

Initial harness attempts are visible:reset15PASS/6FAIL/9ERRORbefore fixing inheritedfuture-annotation compile semantics;final23/7/0withactualsourceunchanged. Broadfirst48PASS/2FAILincluded an invalid reserved.testemailfixture;fixture corrected toexample.com,then49/1. Final independent broad reproduction also49/1. No assertion was weakened or finding xfailed;do not sum these attempts as extra unique coverage.

## Defined validation-gate denominator

There are{len(gates)}named bounded gates in {l(P/'validation-status-register.json')}: {dict(counts)}. Counts describe those named statements only,not canonical roadmap tasks,vulnerabilities or testcase percentages. Eachgate has one allowed status.

'''
txt+=table(['ID','Validation','Status','Evidence','Limitation / next action'],[[x['id'],x['validation'],x['status'],l(P/x['evidence']),x['limit_or_next_action']] for x in gates])
txt+='\n## Security findings and authorization\n\nCanonicalriskcount: **1HIGH,6MEDIUM,2LOW**;noCriticalfinding established within this bounded review. Allnine remainOPENpending owner-authorized correction,policy or environmental evidence. Source/API/event counts are not vulnerability counts.\n\n'
txt+=table(['ID','Severity','Validation','Affected symbols','Disposition / evidence boundary'],[[x['id'],x['severity'],x['validation_status'],x['symbols'],x['disposition']+' '+x['preconditions_and_limits']] for x in sec['findings']])
txt+=f'''
Detailed proposed corrections are in {l(P/'PROPOSED_MINIMAL_CORRECTIONS_REQUIRING_OWNER_AUTHORIZATION.md')}. HIGHSEC01requires atomic token claim plus user update/check in the same existing transaction/session and rollback-safe retries. SEC09needs serialized sharedguard/CAS semantics,not only count-then-write inside snapshot isolation. Session invalidation,bcrypt compatibility and legacyAPIexpectations require explicit owner decisions. No policy was invented or changed.

## Provenance,environment and external boundaries

Current localMongoDBis7.0.45/rs0PRIMARY,not an assumed8.0.38. Existing container was started andknownnofilelimit corrected;no rebuild/reset/drop. Fresh read-only current metadata:52collections,119indexes,all67declaredindexes match,zero nonempty validators observed withraw relevantoptions and timestamp saved. This does not prove production DB access controls,data-wide financial integrity or historicalcapturetime. New localASGI/HTTP/transaction tests use unique retained synthetic databases;backendtest processes stopped.

All39historicalXMLartifacts were reviewed. Historical558PASS/6SKIPversus currentoffline574PASS/6SKIPis explained exactly by16additional`test_image_upload_type_boundary`cases;all564historical testcase identities remain,none removed. Current results are bound to actualpreservedsource hashes,tool/environment metadata and commands. Historical per-run exactsource/commit attestation remains unavailable;currentHEADis repositorycontext,not the extraction's exactsourcecommit. See {l(P/'TEST_PROVENANCE_AND_REPRODUCTION_REPORT.md')}.

NativeAndroid/iOSautolink metadata resolvesRazorpay3.0.0,with installedExpo58.0.17/RN0.88.0. This is not a native build. Androidlacksjavac/SDK/buildtools/adb/emulator/device; iOSlacks macOS/Xcode/CocoaPods/device. No signing/distribution/paidbuild was attempted. Nativebinary/devicegates remainBLOCKED.

RazorpayactualTESTpayment/webhook/refundgates remainBLOCKED:explicit TESTkey/secret/webhook/mode bindings unavailable. No realproviderdelivery/settlement/payments/refunds orLIVEcredential used. Localprovider mocks/signatures are correctly separated. ActualproductionTLS/CORS/DBgrants/secrets/backup/log/edgecontrol evidence remainsBLOCKED;no productionaccess/deployment was performed.

Preservation:8,476+8,504+8,533nested captured pathsets each havezero mismatches;all original reports/checkpoints/ZIP/patches preserved. Current source fingerprint: `{binding['source_tree_fingerprint_SHA256']}`. Tracked/stageddiffempty;existingGitstatusoutside newiteration unchanged. Historicalsecret/runtime/dependency exclusions are explicit. Newmanifest/selfhashsidecar is verified by finalizer completion.

## Workstreams A–J and exact stopping point

A:consolidatedactionregister and ownerchecklist prepared. B:30isolatedresetcasesexecuted;confirmedFAILsdocumented. C:all20gaps re-evaluated. D:39historicalartifacts/sourcebindings/commands/counts reviewed and currentapplicabletests reproduced. E:offline,localHTTP/ASGI/Mongo,legacy,frontendstatic/helpers/webexport executed with failures preserved. F/G:freshnative/provider prerequisites andautolink audited;external gatesBLOCKED. H:full captured preservation/Git auditPASS. I:21securityareasreviewed;50isolatedhelpercasesreproduced. J:master,manifest,checklist and durablecheckpoint saved. Process completion is not approval of the underlying failed/blocked gates.

**Exact next action:**owner reviews the confirmedSEC01security failures and {l(P/'PROPOSED_MINIMAL_CORRECTIONS_REQUIRING_OWNER_AUTHORIZATION.md')},then explicitly decides whether to authorize the minimal protected-source correction and focused regression. Separately decide session/password policy,legacy contract alignment,remainingriskacceptance,and requirednative/provider/production evidence. No further implementation/tests are queued or authorized by this package. Task2wasnotstarted;no commit,push,deploy or publish.

## Report locations

'''
txt+='\n'.join(f'- {l(P/n)}' for n in report_names)+'\n- '+l(P/'TASK_1_FINAL_MASTER_MANIFEST.json')+'\n- '+l(P/'TASK_1_FINAL_MASTER_MANIFEST.sha256')+'\n\nREVIEW PENDING\n'
(P/'TASK_1_FINAL_MASTER_REVIEW_REPORT.md').write_text(txt)

preserve={'timestamp_Asia_Kolkata':NOW,'status':'PASS','repository':str(R),'branch':'work','HEAD':HEAD,
 'protected_file_counts':[8476,8504,8533],'hash_mismatches':[],'original_reports_and_checkpoints_preserved':True,'source_ZIP_and_inherited_patches_preserved':True,
 'previous_manifest_SHA256':sha(OLD/'FINAL_REVIEW_MANIFEST.json'),'previous_manifest_members_checked':27,
 'captured_source_files':len(source_map),'source_fingerprint':binding['source_tree_fingerprint_SHA256'],
 'tracked_diff_empty':True,'staged_diff_empty':True,'Git_status_outside_new_iteration_unchanged':True,
 'intentional_changes':'Only this new validation/evidence folder plus authorized disposable database test records and temporary processes;no protected source/configuration fixes.',
 'scope_limits':binding['exclusions']}
save('final-preservation.json',preserve)

# Complete the new durable checkpoint BEFORE hashing it. Do not alter originals.
with (P/'TASK_1_FINAL_RESUME_CHECKPOINT.md').open('a') as f:
 f.write(f'''\n## {NOW} — final auditable stopping point\n\nRepository `{R}`; branch `work`; HEAD `{HEAD}`. Current task: Phase 1 Task 1 validation, REVIEW PENDING, not approved or closed. Previous inventories were reused; all A–J workstreams were examined. Final unique Python cases: 735 PASS / 10 assertion FAIL / 3 fixture ERROR / 5 SKIPPED (753 cases). Invocation outcomes: 735/10/3/7 (755 observations); two offline opt-in skips later passed. Six frontend commands passed: TypeScript 0 errors, ESLint 0 errors / 10 warnings, planner (reported11assertions with count caveat), native VM5, guard9 and web export. Reset: 23 PASS / 7 FAIL on real disposable MongoDB. Broad security: 49 PASS / 1 FAIL with synthetic doubles. Initial diagnostic attempts are retained but not summed. Legacy: 17 PASS / 2 FAIL / 3 ERROR / 1 SKIP. HIGH SEC-01 is confirmed FAIL / OPEN; no protected source fix. Nine canonical findings: 1 HIGH / 6 MEDIUM / 2 LOW.\n\nAll 8,476 / 8,504 / 8,533 captured files match their baselines; previous manifest SHA and all27entries unchanged. Only new validation evidence was written. MongoDB7.0.45 / rs0 PRIMARY remains running; all temporary test backends stopped; disposable synthetic databases retained, no drops. No real provider payments/refunds, production access, packages, Task2, commits, pushes, deployment or publishing. Native binaries/devices, actual provider TEST and production evidence remain BLOCKED. Historical per-run attestation is missing; full UI-binding acceptance was NOT RUN.\n\nLast operation: final file/Git/XML/report-reference verification and master-manifest generation/hash comparison by `python {P/'finalize-task1-package.py'}`. No test operation remains running or interrupted. Rerun the finalizer only if new report changes need rehashing; do not repeat application tests without a specific reason. Exact next action: owner reads TASK_1_FINAL_MASTER_REVIEW_REPORT.md and PROPOSED_MINIMAL_CORRECTIONS_REQUIRING_OWNER_AUTHORIZATION.md, then explicitly decides whether to authorize protected source corrections, legacy alignment or further validation. Do not start Task2.\n\nNEXT_SESSION_RESUME_PROMPT:\nContinue COME-IN from `{R}`, expected branch `work` / HEAD `{HEAD}`. Read the previous six final reports and ITERATION_CHECKPOINT.md in `{OLD}`, then all current reports, master manifest, current-test-results.json, validation-status-register.json and this checkpoint in `{P}`. Inspect Git status and verify the 8,533-file baseline and previous manifest before work. Never assume an unrecorded operation succeeded. Do not regenerate the completed179API/60model/navigation inventories or repeat completed regression/reset/security/frontend checks without a specific change or provenance issue. HIGH SEC-01 remains confirmed FAIL / OPEN and unremediated; the owner has not approved Task1or protected source fixes. Follow the owner's next explicit decision. No source/config/UI changes, production database/provider LIVE operations, Task2, commit, push or deployment. Append only this new iteration checkpoint after meaningful authorized progress.\n''')

# Parse Markdown link destinations with balanced parentheses (Expo (tabs) paths).
refs=[]
for md in sorted(P.glob('*.md')):
 text=md.read_text();start=0
 while True:
  i=text.find('](',start)
  if i<0:break
  j=i+2
  if j<len(text) and text[j]=='<':
   end=text.find('>',j+1)
   if end<0:break
   target=text[j+1:end];start=end+1
  else:
   depth=1;end=j
   while end<len(text) and depth:
    if text[end]=='(':depth+=1
    elif text[end]==')':depth-=1
    end+=1
   target=text[j:end-1];start=end
  if not target or target.startswith(('http:','https:','#','mailto:')):continue
  m=re.fullmatch(r'(.+?)(?::(\d+)(?:[-–]\d+)?)?',target)
  if not m:continue
  path=Path(m[1]);path=path if path.is_absolute() else md.parent/path
  # Only file references;inline textual expressions are not treated as paths.
  if path.name in {'TASK_1_FINAL_MASTER_MANIFEST.json','TASK_1_FINAL_MASTER_MANIFEST.sha256'}:continue
  assert path.exists(),f'Missing Markdown reference:{md.name}:{target}'
  lineno=int(m[2]) if m[2] else None
  if lineno:assert path.is_file() and 1<=lineno<=len(path.read_text().splitlines()),f'Badline:{path}:{lineno}'
  refs.append({'report':md.name,'target':str(path),'line':lineno,'resolved':True})
save('final-reference-verification.json',{'timestamp':NOW,'references_checked':len(refs),'missing':[],'references':refs,'scope':'All local Markdown link targets/line references in top-level generated reports;external URLs are not contacted.'})
save('final-package-verification.json',{'timestamp':NOW,'required_report_files_checked':len(report_names),'missing_reports':[n for n in report_names if not (P/n).is_file()],
 'protected_baseline_mismatches':[],'old_manifest27hashes_match':True,'source_unchanged':True,'Git_identity_matches':True,'tracked_staged_diffs_empty':True,
 'status_outside_new_iteration_unchanged':True,'XML_and_JSON_case_totals_verified':True,'security_findings9_consistent':True,'gate_counts':dict(counts),
 'local_Markdown_reference_targets_checked':len(refs),'all_local_Markdown_references_resolve':True,
 'application_source_fixes':0,'Task2_started':False,'owner_approved':False,'final_status':'REVIEW PENDING','next_action':'Stop for owner authorization/decision;no test or implementation running.'})
assert all((P/n).is_file() for n in report_names)
files=[x for x in sorted(P.rglob('*')) if x.is_file() and x.name not in {'TASK_1_FINAL_MASTER_MANIFEST.json','TASK_1_FINAL_MASTER_MANIFEST.sha256'}]
manifest={'project':'COME-IN','created_Asia_Kolkata':NOW,'repository':str(R),'branch':'work','HEAD':HEAD,'application_extraction':str(A),
 'source_state_binding':'source-state-binding.json','previous_manifest_SHA256':sha(OLD/'FINAL_REVIEW_MANIFEST.json'),'required_reports':report_names,
 'files':[{'relative_path':str(x.relative_to(P)),'bytes':x.stat().st_size,'SHA256':sha(x)} for x in files],
 'self_hash_policy':'Self and sidecar excluded to avoid recursive hashes;sidecar stores manifest SHA256. Original manifests untouched.',
 'test_results':'current-test-results.json','gate_counts':dict(counts),'gate_denominator':len(gates),'risk_severity_counts':{'HIGH':1,'MEDIUM':6,'LOW':2},
 'protected_files':8533,'protected_hash_mismatches':0,'original_source_changes':0,'owner_approved':False,'Task1_status':'REVIEW PENDING','Task2_started':False}
save('TASK_1_FINAL_MASTER_MANIFEST.json',manifest)
(P/'TASK_1_FINAL_MASTER_MANIFEST.sha256').write_text(sha(P/'TASK_1_FINAL_MASTER_MANIFEST.json')+'  TASK_1_FINAL_MASTER_MANIFEST.json\n')
for entry in manifest['files']:
 file=P/entry['relative_path'];assert file.stat().st_size==entry['bytes'] and sha(file)==entry['SHA256'],f'Manifest mismatch:{file}'
assert (P/'TASK_1_FINAL_MASTER_MANIFEST.sha256').read_text().split()[0]==sha(P/'TASK_1_FINAL_MASTER_MANIFEST.json')
assert all(sha(name)==h for name,h in baseline.items())
assert filtered(git('status','--porcelain=v1','--untracked-files=all'))==filtered((P/'git-status-before.txt').read_text())
print(json.dumps({'status':'PASS — package/preservation verification,not application approval','protected8533_mismatches':0,'previous8476_and8504_unchanged':True,
 'manifest_members_verified':len(manifest['files']),'report_references_verified':len(refs),'gates':dict(counts),'gate_denominator':len(gates),
 'unique_Python_cases':unique,'manifest_SHA256':sha(P/'TASK_1_FINAL_MASTER_MANIFEST.json'),'final_Task1_status':'REVIEW PENDING'},indent=2))
