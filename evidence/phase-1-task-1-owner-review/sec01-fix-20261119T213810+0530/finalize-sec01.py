"""Verify the one authorized source delta and save an immutable review package."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import ast,hashlib,json,re,subprocess,xml.etree.ElementTree as ET

P=Path(__file__).resolve().parent
R=Path('/workspace/come-in-current')
A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
S=A/'backend/server.py'
OLD=P.parent/'validation-20261119T140704+0530'
HEAD='a223290a8866a1ebeaac982f546491fdc197ae7a'
BEFORE='a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db'
AFTER='70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07'
NOW=datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def save(n,d):(P/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def git(*args):return subprocess.check_output(['git','--no-optional-locks','-C',str(R),*args],text=True)
def link(p,line=None,label=None):
 p=Path(p);return f'[{label or p.name}](<{p}{":"+str(line) if line else ""}>)'
def table(headers,rows):
 def cell(v):return str(v).replace('|','\\|').replace('\n','<br>')
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])+'\n'
def xmlcounts(p):
 cs=list(ET.parse(p).getroot().iter('testcase'))
 return {'PASS':sum(all(x.find(k) is None for k in ('failure','error','skipped')) for x in cs),'FAIL':sum(x.find('failure') is not None for x in cs),'ERROR':sum(x.find('error') is not None for x in cs),'SKIPPED':sum(x.find('skipped') is not None for x in cs)}

assert git('branch','--show-current').strip()=='work' and git('rev-parse','HEAD').strip()==HEAD
assert sha(S)==AFTER and sha(P/'before/backend/server.py')==BEFORE and sha(P/'after/backend/server.py')==AFTER
baseline=read(P/'preservation-before.json')
assert len(baseline)==8746 and baseline[str(S)]==BEFORE
changes=[];bad=[]
for name,oldsha in baseline.items():
 p=Path(name)
 if not p.is_file():bad.append({'path':name,'error':'missing'});continue
 current=sha(p)
 if current!=oldsha:
  item={'path':name,'before_SHA256':oldsha,'after_SHA256':current}
  if name==str(S) and current==AFTER:changes.append(item)
  else:bad.append(item)
assert len(changes)==1 and not bad,f'Unauthorized change:{bad}'
before_tree=ast.parse((P/'before/backend/server.py').read_text())
after_tree=ast.parse(S.read_text())
before_reset=next(n for n in before_tree.body if isinstance(n,ast.AsyncFunctionDef) and n.name=='reset_password')
after_reset=next(n for n in after_tree.body if isinstance(n,ast.AsyncFunctionDef) and n.name=='reset_password')
assert ast.dump(before_reset.args)==ast.dump(after_reset.args)
assert [ast.dump(x) for x in before_reset.decorator_list]==[ast.dump(x) for x in after_reset.decorator_list]
assert len(before_tree.body)==len(after_tree.body)
outside_before=[n for n in before_tree.body if n is not before_reset]
outside_after=[n for n in after_tree.body if n is not after_reset]
assert [ast.dump(x,include_attributes=False) for x in outside_before]==[ast.dump(x,include_attributes=False) for x in outside_after]
helper=A/'backend/mongo_transactions.py'
assert sha(helper)==baseline[str(helper)]

oldmanifest=read(OLD/'TASK_1_FINAL_MASTER_MANIFEST.json')
assert sha(OLD/'TASK_1_FINAL_MASTER_MANIFEST.json')=='24de73630bdcd28412a0b270e32ac5da7f88e61bb4ce85f2c2a405d17f563588'
assert len(oldmanifest['files'])==211 and all(sha(OLD/e['relative_path'])==e['SHA256'] for e in oldmanifest['files'])
prefix=str(P.relative_to(R))+'/'
filtered=lambda text:sorted(x for x in text.splitlines() if not x[3:].startswith(prefix))
before_status=(P/'git-status-before.txt').read_text();status=git('status','--porcelain=v1','--untracked-files=all')
assert filtered(before_status)==filtered(status)
assert not git('diff','--no-ext-diff','--exit-code') and not git('diff','--cached','--no-ext-diff','--exit-code')
(P/'git-status-after.txt').write_text(status)
(P/'git-diff-after.txt').write_text(git('diff','--no-ext-diff'))

focus_before=read(P/'focused-before.json');focus_after=read(P/'focused-after.json')
strong=P/'distinct-password-concurrency'
strong_before=read(strong/'focused-before.json');strong_after=read(strong/'focused-after.json')
assert focus_before['counts']=={'PASS':10,'FAIL':10,'ERROR':0,'SKIPPED':0}
assert focus_after['counts']=={'PASS':20,'FAIL':0,'ERROR':0,'SKIPPED':0}
assert strong_before['counts']=={'PASS':0,'FAIL':2,'ERROR':0,'SKIPPED':0}
assert strong_after['counts']=={'PASS':2,'FAIL':0,'ERROR':0,'SKIPPED':0}
assert focus_before['runner_SHA256']==focus_after['runner_SHA256']
assert strong_before['runner_SHA256']==strong_after['runner_SHA256']
for base,b,a in [(P,focus_before,focus_after),(strong,strong_before,strong_after)]:
 assert b['source_SHA256']==b['source_SHA256_after']==BEFORE
 assert a['source_SHA256']==a['source_SHA256_after']==AFTER
 for phase,d in [('before',b),('after',a)]:assert xmlcounts(base/f'focused-{phase}.xml')==d['counts']
old30=read(P/'old-30-before-after-results.json')
assert old30[0]['counts']=={'PASS':23,'FAIL':7,'ERROR':0,'SKIPPED':0}
assert old30[1]['counts']=={'PASS':26,'FAIL':4,'ERROR':0,'SKIPPED':0}
assert set(old30[1]['fail_cases'])=={'RESET-10','RESET-19','RESET-27','RESET-30'}
oldexisting=read(P/'old-related-existing-results.json')
assert oldexisting['counts']==xmlcounts(P/'old-related-existing.xml')=={'PASS':78,'FAIL':0,'ERROR':0,'SKIPPED':0}
assert read(P/'old-30-runner-compatibility.json')['all_original_invariant_assertions_preserved']
summary={'timestamp_Asia_Kolkata':NOW,'SEC01_HIGH':'FIXED — verified scoped implementation;owner review pending',
 'focused_before':focus_before['counts'],'focused_after':focus_after['counts'],
 'distinct_password_concurrency_before':strong_before['counts'],'distinct_password_concurrency_after':strong_after['counts'],
 'old_related_after':oldexisting['counts'],'old_30_before':old30[0]['counts'],'old_30_after':old30[1]['counts'],
 'unrelated_failure_cases_unchanged':old30[1]['fail_cases'],
 'count_scope':'20focused cases plus2strengthened variants of existing concurrency cases;do not present them as22unique caseIDs or sum baseline/after/diagnostic runs.',
 'source_before_SHA256':BEFORE,'source_after_SHA256':AFTER,'helper_unchanged':True,
 'source_files_modified':1,'source_symbol_modified':'reset_password','Task1_status':'REVIEW PENDING','owner_approval_or_closure':False}
save('SEC01_TEST_AND_STATUS_SUMMARY.json',summary)

preservation={'timestamp_Asia_Kolkata':NOW,'status':'PASS','protected_baseline_paths':len(baseline),
 'unchanged_protected_paths':len(baseline)-1,'authorized_changed_paths':changes,'unauthorized_or_missing_paths':bad,
 'before_source_exact_backup_verified':True,'after_source_snapshot_verified':True,
 'top_level_AST_nodes':len(before_tree.body),'unchanged_nodes_outside_reset_password':len(outside_before),
 'only_changed_AST_symbol':'reset_password','API_signature_and_decorators_unchanged':True,
 'existing_transaction_helper_SHA256':sha(helper),'helper_schema_config_UI_and_other_findings_unchanged':True,
 'previous_211_manifest_members_unchanged':True,'previous_master_manifest_SHA256':sha(OLD/'TASK_1_FINAL_MASTER_MANIFEST.json'),
 'branch':'work','HEAD':HEAD,'Git_tracked_and_staged_diff_empty':True,'Git_status_outside_new_evidence_unchanged':True,
 'limits':'Git doesnottracktheapplicationextraction;explicitpatch/contenthashescoverthesourcechange. Actualsecret.env/dependency/cacheexcludedhistoricalscopeisnotbackdatedproductioncustodyproof.',
 'original_reports_checkpoints_ZIPs_and_inherited_patches_unchanged':True,'Task2_commit_push_deploy_publish':False}
save('SEC01_PRESERVATION_VERIFICATION.json',preservation)

txt=f'''# COME-IN — SEC-01 scoped fix and owner-review report

Recorded {NOW} (Asia/Kolkata). Repository `{R}`, branch `work`, HEAD `{HEAD}`. Application source is retained at `{A}` outside Git.

**SEC-01 HIGH (token reuse and reset atomicity): FIXED. Focused regression: PASS. Concurrency validation: PASS. Task 1: REVIEW PENDING — not APPROVED or CLOSED.**

The owner explicitly authorized this minimal SEC-01 HIGH correction and focused tests. No other HIGH/MEDIUM/LOW finding was modified. The separate SMTP configuration LOW subissue remains open. Original reports,checkpoints,ZIP backups and Git history are retained unchanged as historical evidence;this report records the authorized delta.

## Exact source change

Only {link(S,after_reset.lineno,'backend/server.py — reset_password')} changed. {link(P/'SEC01_SOURCE_CHANGE.patch','' or None,'Exact source patch')} and {link(P/'source-change-before-after.json')} provide the complete delta. No imports,transaction-helper implementation,endpoint signature,request models,response fields,database schema/index definitions,UI or business architecture changed.

1. Keep the existing unused/unexpired-token preflight so invalid tokens still reject before bcrypt work.
2. Prepare the password hash once after that preflight, outside callback retries.
3. Inside the existing `run_transaction(client, apply)`, atomically claim the same token using `_id`,digest,`used=False` and a fresh expiry check. The claim and its `used_at` update use the supplied session.
4. Derive the account from the claimed record and update its password using that same session. Require exactly one matched user;otherwise abort with the existing generic HTTP400 error,rolling back the claim.
5. Commit both documents together. Transaction/failure paths never fall back to sequential standalone writes. Driver transient/unknown-commit behavior stays in the existing unchanged helper.

The matched-user check is necessary to the SEC-01 atomicity guarantee:consuming a token without a real password update must not return success. This also resolves the previously documented missing-user false-success subcase. It does not add schema or session-revocation policy. SMTP delivery,JWT revocation,rate limiting,bcrypt and admin-role behavior are unchanged.

## Before/after executable evidence

'''
txt+=table(['Validation','Before fix','After fix','Evidence'],[
 ['Dedicated SEC-01 invariants','10 PASS / 10 FAIL / 0 ERROR / 0 SKIP','20 PASS / 0 FAIL / 0 ERROR / 0 SKIP',link(P/'SEC01_FOCUSED_REGRESSION_REPORT.md')+'; '+link(P/'focused-before.json')+'; '+link(P/'focused-after.json')],
 ['Stronger concurrency:distinct contender passwords','0 PASS / 2 FAIL','2 PASS / 0 FAIL',link(strong/'focused-before.json')+'; '+link(strong/'focused-after.json')],
 ['Existing related tests (9 original modules)','Not unnecessarily repeated before the edit','78 PASS / 0 FAIL / 0 ERROR / 0 SKIP',link(P/'OLD_RELATED_REGRESSION_REPORT.md')+'; '+link(P/'old-related-existing.xml')],
 ['Historical 30-case security harness,with documented transaction-compatible instrumentation','23 PASS / 7 FAIL','26 PASS / 4 FAIL',link(P/'old-30-before-after-results.json')+'; '+link(P/'old-30-runner-harness.diff')]])
txt+='''
The same focused runner/assertions are used for each before/after pair. The two stronger concurrency variants are not counted as22unique case IDs. All55original broader-harness invariant assertions were preserved;one HTTP400 guard was added for correct missing-user rejection. The post-user-write fault was moved to that actual operation boundary so it still tests the same no-partial-state invariant under the new operation ordering. No failure was skipped,xfailed or suppressed.

## Concurrency,rollback and retry results

Tests use actual extracted production function/model bodies,real bcrypt/Motor/PyMongo,and retained unique disposable MongoDB databases on loopback `rs0`. No production accounts,actual customer data,SMTP calls,provider credentials or payments were used. Full HTTP routing/middleware/provider/native acceptance is outside this focused scope. The dedicated suite stubs throttling to isolate SEC-01;the broader historical harness separately confirms the unchanged rate-limit finding.

- Two synchronized valid preflight reads produce exactly one successful reset and one existing HTTP400 rejection.
- Three independent eight-contender rounds produce exactly one success and seven HTTP400 rejections each. The stronger variants use distinct short synthetic passwords and verify that only the actual winner's credential authenticates;no loser's credential does. Password values are not logged.
- Faults before the token write,before the user write and after the real user write but before commit leave both password and token unchanged after abort. A clean retry succeeds once;replay cannot overwrite it.
- A labelled transient failure retries the callback after rollback with only one durable paired result and one prepared hash.
- A controlled lost commit acknowledgement after the real commit causes two commit calls,one callback,one token-write attempt and one user-write attempt. The callback is not replayed after success.
- A lost response after committed success cannot make a client retry overwrite the winning password.
- Expiry or consumption between preflight and transactional claim is rechecked. A missing target account rolls back the token claim. Transaction-session unavailability fails closed.

These are controlled function-level real-database integration tests,not a statistical load test,deployed exploit,actual network outage or standalone-server certification. No global MongoDB failpoint was used;no database was dropped. Per-run source/test hashes,versions,commands,timestamps,collection counts and retained database names are in the result JSONs.

## Remaining security findings and unchanged failures

'''
txt+=table(['Case / finding','Current result','Disposition'],[
 ['RESET-10 — SEC-01 SMTP configuration LOW subissue','FAIL unchanged','Malformed SMTP_PORT cleanup is outside this authorized HIGH atomicity fix;forgot/email-helper source is unchanged.'],
 ['RESET-19 — SEC-02 MEDIUM','FAIL unchanged','Old JWT remains valid after reset;session policy/correction still requires separate owner authorization.'],
 ['RESET-27 — SEC-04 MEDIUM','FAIL unchanged','Concurrent rate-limit overshoot remains;rate helper unchanged.'],
 ['RESET-30 — SEC-06 LOW','FAIL unchanged','bcrypt long-input ambiguity remains;hashing/input policy unchanged.'],
 ['SEC-03 / SEC-05 / SEC-07 / SEC-08 / SEC-09','No change and no new closure claim','Original reported ingress/diagnostic/availability/body-limit/admin findings remain open with their prior evidence boundaries.']])
txt+='''
The eight other canonical findings (six MEDIUM,two LOW) remain unmodified. The additional SMTP LOW subissue remains associated with SEC-01;it is not silently closed or renumbered. The broad 30-case suite therefore still has4known failures even though every authorized SEC-01 HIGH acceptance case now passes. Existing legacy-contract failures,native/device/provider blockers and production-evidence gaps are unchanged;large unrelated suites/builds were not rerun for this one-function Python change.

Task1is still **REVIEW PENDING**. This correction does not approve or close Task1,waive remaining gates or authorize Task2. Historical source-line references belong to the captured pre-fix source;the exact before-source backup is retained. Current source hashes and this patch supersede only the authorized SEC-01 code state.

## Preservation and hashes

'''
txt+=table(['Item','Verified result'],[
 ['Existing protected baseline','8,746 paths checked:8,745 unchanged;exactly1authorized change,backend/server.py;zero unauthorized/missing paths.'],
 ['Outside changed function',f'{len(outside_before)} other top-level AST nodes unchanged out of{len(before_tree.body)};signature/decorators unchanged.'],
 ['Before-source backup SHA-256',BEFORE],['Current/after-source SHA-256',AFTER],
 ['Transaction helper SHA-256 (unchanged)',sha(helper)],
 ['Previous owner-review package','Original manifest SHA24de73630bdcd28412a0b270e32ac5da7f88e61bb4ce85f2c2a405d17f563588 and all211member hashes unchanged.'],
 ['Git','Branchwork/expectedHEAD;tracked/staged diff empty;pre-existing status outside new evidence unchanged. Application source delta is explicitly stored in the patch because extraction is outsideGit.']])
txt+=f'''
Detailed proof: {link(P/'SEC01_PRESERVATION_VERIFICATION.json')}. Original root checkpoints and prior reports/manifests are not overwritten. Exact before and after source copies are {link(P/'before/backend/server.py')} and {link(P/'after/backend/server.py')}. Actual secret.env/dependency/runtime-cache exclusions in historical baselines are not backdated or presented as production custody proof.

## Review package and stopping point

- {link(P/'SEC01_INDEPENDENT_DESIGN_REVIEW.md')}
- {link(P/'SEC01_FOCUSED_REGRESSION_REPORT.md')}
- {link(P/'OLD_RELATED_REGRESSION_REPORT.md')}
- {link(P/'SEC01_TEST_AND_STATUS_SUMMARY.json')}
- {link(P/'SEC01_PRESERVATION_VERIFICATION.json')}
- {link(P/'SEC01_RESUME_CHECKPOINT.md')}
- {link(P/'SEC01_EVIDENCE_MANIFEST.json')}
- {link(P/'SEC01_EVIDENCE_MANIFEST.sha256')}

No Task2,commit,push,deploy or publish. No protected source beyond the one authorized function/file changed. No remaining finding was modified. All test databases are retained and test processes ended. Exact next action:owner reviews this fix,patch and evidence and records the Task1review decision or separately scoped next authorization. No additional implementation is queued.

**SEC-01 HIGH: FIXED — scoped verification PASS. Task1: REVIEW PENDING.**
'''
(P/'SEC01_FIX_REPORT.md').write_text(txt)

with (P/'SEC01_RESUME_CHECKPOINT.md').open('a') as f:
 f.write(f'''\n## {NOW} — SEC-01 correction verified; stop for owner review\n\nProject: COME-IN. Repository `{R}`; application `{A}`; branch `work`; HEAD `{HEAD}`. The owner authorized only the minimum SEC-01 HIGH reset-atomicity fix. Changed application file: backend/server.py, reset_password only. Before SHA-256 `{BEFORE}`; after SHA-256 `{AFTER}`. Exact before/after snapshots and patch are retained. Existing transaction helper, schema, API signature, UI and unrelated security code are unchanged.\n\nFresh results: 20 focused cases changed from 10 PASS / 10 FAIL before to 20 PASS / 0 FAIL after. Stronger distinct-password concurrency variants changed from 0 PASS / 2 FAIL to 2 PASS / 0 FAIL. Nine original related modules: 78 PASS. Old 30-case security suite: 23 PASS / 7 FAIL before to 26 PASS / 4 FAIL after. No errors or skips. Paired-run assertions are preserved. The remaining RESET-10/19/27/30 failures are unchanged and outside this fix. SEC-01 HIGH is FIXED for token reuse, concurrency and partial-write consistency. Task 1 is not approved. The SMTP LOW subissue and eight other canonical findings remain open.\n\nPreservation: 8,746 baseline paths checked; 8,745 unchanged, one authorized source change, zero unauthorized changes. Prior 211 manifest members and original reports/checkpoints/ZIP/patches are preserved. Git branch/HEAD/status outside this new folder are unchanged. No commit, push, deployment or Task 2. Disposable synthetic databases are retained; no global failpoints, database drops, production/customer/provider/credential operations. All tests finished; no operation is interrupted. Last operation: final file/Git/AST/XML/report-link verification and new manifest hash comparison by `python {P/'finalize-sec01.py'}`. Safe to rerun this file verifier if documentation needs rehashing; do not repeat completed application suites without a specific reason.\n\nNEXT_SESSION_RESUME_PROMPT:\nContinue COME-IN from `{R}`, expected branch `work` and HEAD `{HEAD}`. First read SEC01_FIX_REPORT.md, SEC01_EVIDENCE_MANIFEST.json, SEC01_TEST_AND_STATUS_SUMMARY.json, SEC01_PRESERVATION_VERIFICATION.json and this checkpoint in `{P}`; then the previous Task 1 master review/checkpoints in `{OLD}`. Verify current server SHA-256 `{AFTER}`, original before SHA-256 `{BEFORE}`, Git status and the one-file allowlist before work. SEC-01 HIGH core correction is verified; Task 1 remains REVIEW PENDING, not APPROVED or CLOSED. Preserve all originals and evidence. Do not change SMTP/JWT/rate/bcrypt/admin or any other finding without separate owner authorization. Do not regenerate completed inventories or repeat passing suites unnecessarily. Wait for the owner's review and next scope. No Task 2, commit, push, deployment, publishing or production operations. Update only this new session checkpoint after meaningful authorized progress.\n''')

# Check every local Markdown link/line target without contacting external URLs.
refs=[]
for md in P.rglob('*.md'):
 text=md.read_text();pos=0
 while True:
  i=text.find('](',pos)
  if i<0:break
  j=i+2
  if j<len(text) and text[j]=='<':
   k=text.find('>',j+1)
   if k<0:break
   target=text[j+1:k];pos=k+1
  else:
   depth=1;k=j
   while k<len(text) and depth:
    if text[k]=='(':depth+=1
    elif text[k]==')':depth-=1
    k+=1
   target=text[j:k-1];pos=k
  if not target or target.startswith(('http:','https:','#','mailto:')):continue
  m=re.fullmatch(r'(.+?)(?::(\d+)(?:[-–]\d+)?)?',target)
  if not m:continue
  path=Path(m[1]);path=path if path.is_absolute() else md.parent/path
  if path.name in {'SEC01_EVIDENCE_MANIFEST.json','SEC01_EVIDENCE_MANIFEST.sha256'}:continue
  assert path.exists(),f'Missingreference:{md}:{target}'
  lineno=int(m[2]) if m[2] else None
  if lineno:assert path.is_file() and 1<=lineno<=len(path.read_text().splitlines()),f'Badline:{path}:{lineno}'
  refs.append({'report':str(md.relative_to(P)),'target':str(path),'line':lineno,'resolved':True})
save('SEC01_FINAL_VERIFICATION.json',{'timestamp':NOW,'status':'PASS — scoped file/test-evidence verification',
 'protected_paths_checked':8746,'unchanged_paths':8745,'authorized_source_changes':1,'unauthorized_changes':0,
 'only_reset_password_AST_changed':True,'before_after_XML_JSON_counts_match':True,'original55broader_invariants_preserved':True,
 'previous_master_manifest211members_match':True,'local_Markdown_references_checked':len(refs),'unresolved_references':[],
 'Git_branch_HEAD_and_status_verified':True,'owner_approved_Task1':False,'Task2_started':False,'SEC01_HIGH':'FIXED;ownerreviewpending','Task1':'REVIEW PENDING',
 'next_action':'Stop for owner review;no new source correction or Task2 authorization inferred.'})
files=[x for x in sorted(P.rglob('*')) if x.is_file() and x.name not in {'SEC01_EVIDENCE_MANIFEST.json','SEC01_EVIDENCE_MANIFEST.sha256'}]
manifest={'project':'COME-IN','timestamp_Asia_Kolkata':NOW,'repository':str(R),'branch':'work','HEAD':HEAD,
 'scope':'Owner-authorized SEC-01HIGH minimum correction and focused regression only;not Task1approval or remaining-findings permission.',
 'approved_source_changes':changes,'source_backup':'before/backend/server.py','source_after_snapshot':'after/backend/server.py',
 'previous_master_manifest_SHA256':sha(OLD/'TASK_1_FINAL_MASTER_MANIFEST.json'),
 'files':[{'path':str(x.relative_to(P)),'bytes':x.stat().st_size,'SHA256':sha(x)} for x in files],
 'self_hash_policy':'Self and sidecar excluded from members;sidecar contains this manifest SHA256.',
 'test_summary':'SEC01_TEST_AND_STATUS_SUMMARY.json','preservation':'SEC01_PRESERVATION_VERIFICATION.json',
 'SEC01_HIGH':'FIXED — scoped tests passed','Task1_status':'REVIEW PENDING','Task1_approved_or_closed':False,
 'remaining_other_findings_modified':False,'Task2_commit_push_deploy_publish':False}
save('SEC01_EVIDENCE_MANIFEST.json',manifest)
(P/'SEC01_EVIDENCE_MANIFEST.sha256').write_text(sha(P/'SEC01_EVIDENCE_MANIFEST.json')+'  SEC01_EVIDENCE_MANIFEST.json\n')
for e in manifest['files']:
 f=P/e['path'];assert f.stat().st_size==e['bytes'] and sha(f)==e['SHA256'],f'Evidence changed while finalizing:{f}'
assert (P/'SEC01_EVIDENCE_MANIFEST.sha256').read_text().split()[0]==sha(P/'SEC01_EVIDENCE_MANIFEST.json')
assert sha(S)==AFTER and git('rev-parse','HEAD').strip()==HEAD
assert filtered(git('status','--porcelain=v1','--untracked-files=all'))==filtered(before_status)
print(json.dumps({'SEC01_HIGH':'FIXED','focused_after':focus_after['counts'],'stronger_concurrency_after':strong_after['counts'],
 'old_related_after':oldexisting['counts'],'old_security_after':old30[1]['counts'],
 'preservation':{'unchanged':8745,'authorized_changed':1,'unauthorized_changed':0},
 'manifest_members_verified':len(files),'report_references_checked':len(refs),
 'manifest_SHA256':sha(P/'SEC01_EVIDENCE_MANIFEST.json'),'Task1_status':'REVIEW PENDING'},indent=2))
