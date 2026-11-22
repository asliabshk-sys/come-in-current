"""File/Git/reference integrity verification only;never import or call the app."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import ast
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
REPO = Path('/workspace/come-in-current')
OLD = HERE.parent
AUDIT = REPO/'evidence/phase-1-task-1-audit'
HEAD = 'a223290a8866a1ebeaac982f546491fdc197ae7a'
STATUSES = {'VERIFIED','PARTIALLY VERIFIED','UNVERIFIED','CONTRADICTED','BLOCKED'}
REPORTS = [
 'FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md','FINAL_SECURITY_VALIDATION_REPORT.md',
 'FINAL_NAVIGATION_AND_API_INVENTORY.md','FINAL_PRESERVATION_VERIFICATION.md',
 'FINAL_OWNER_DECISION_READINESS.md']
AUDIT_REPORTS = [AUDIT/x for x in [
 'PHASE_1_TASK_1_MASTER_AUDIT_REPORT.md','PHASE_1_TASK_1_SCREEN_AND_ROUTE_INVENTORY.md',
 'PHASE_1_TASK_1_API_AND_DATABASE_INVENTORY.md','PHASE_1_TASK_1_SECURITY_FINDINGS.md',
 'PHASE_1_TASK_1_GAP_AND_BLOCKER_REGISTER.md','PHASE_1_TASK_1_FINAL_CHECKLIST.md',
 'PHASE_1_TASK_1_EVIDENCE_MANIFEST.json']]
OLD_REPORTS = [OLD/x for x in ['OWNER_REVIEW_MASTER_REPORT.md','REPORT_BY_REPORT_REVIEW.md',
 'SECURITY_FINDINGS_REVIEW.md','EVIDENCE_GAP_REGISTER.md','OWNER_APPROVAL_CHECKLIST.md',
 'REVIEW_EVIDENCE_MANIFEST.json']]
CHECKPOINTS = [REPO/x for x in ['COME_IN_LIVE_CHECKPOINT.md','COME_IN_MASTER_TASK_TRACKER.md',
 'COME_IN_DECISIONS_AND_BLOCKERS.md','COME_IN_SESSION_LOG.md','COME_IN_NEXT_SESSION_RESUME_PROMPT.md']]

def now():
    return datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()

def read(p):
    return json.loads(Path(p).read_text())

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()

def git(*args):
    return subprocess.check_output(['git','--no-optional-locks','-C',str(REPO),*args],text=True)

def check_baseline(p):
    d=read(p)
    mismatches=[]
    for name,wanted in d.items():
        f=Path(name)
        if not f.is_file():
            mismatches.append({'path':name,'error':'missing'})
        elif sha(f)!=wanted:
            mismatches.append({'path':name,'error':'SHA-256 mismatch'})
    return {'baseline':str(p),'files_checked':len(d),'mismatches':mismatches}

branch=git('branch','--show-current').strip()
head=git('rev-parse','HEAD').strip()
assert branch=='work' and head==HEAD, 'Identity mismatch;stop without changing originals'
baselines=[check_baseline(p) for p in [AUDIT/'protected-file-hashes-before.json',OLD/'preservation-before.json',HERE/'preservation-baseline.json']]
assert [x['files_checked'] for x in baselines]==[8150,8476,8504]
assert not any(x['mismatches'] for x in baselines), 'Protected bytes differ;do not repair originals'
prior=read(OLD/'preservation-before.json')
current=read(HERE/'preservation-baseline.json')
original=read(AUDIT/'protected-file-hashes-before.json')
assert set(original)<=set(prior)<=set(current)
assert all(current[str(p)]==sha(p) for p in AUDIT_REPORTS+OLD_REPORTS+CHECKPOINTS)

status=git('status','--porcelain=v1','--untracked-files=all')
prefix=str(HERE.relative_to(REPO))+'/'
def filtered_status(s):
    return sorted(line for line in s.splitlines() if not line[3:].startswith(prefix))
before=(HERE/'git-status-before.txt').read_text()
assert filtered_status(status)==filtered_status(before),'Gitstatus changed outside the new iteration'
(HERE/'git-status-after.txt').write_text(status)
diff=git('diff','--no-ext-diff','--exit-code')
staged=git('diff','--cached','--no-ext-diff','--exit-code')
assert not diff and not staged
(HERE/'git-diff-after.txt').write_text(diff)
(HERE/'git-diff-cached-after.txt').write_text(staged)

api=read(HERE/'complete-api-inventory.json')
assert len(api['endpoints'])==179 and len(api['request_models'])==60
assert api['counts']['source_sha256']==sha('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py')
assert all(e['classification']=='VERIFIED' for e in api['endpoints'])
assert len(set((e['method'],e['path']) for e in api['endpoints']))==179
assert sum(len(e['parameters']) for e in api['endpoints'])==387
assert sum(p['default_present'] for e in api['endpoints'] for p in e['parameters'])==216
assert all('signature_arguments' in e for e in api['endpoints'])
for name in ['extract-complete-api.py','augment-api-effects.py','compile-final-review.py','verify-final-review.py']:
    ast.parse((HERE/name).read_text(),filename=name)
for name in REPORTS:
    assert (HERE/name).is_file() and (HERE/name).stat().st_size>1000
report=(HERE/'FINAL_NAVIGATION_AND_API_INVENTORY.md').read_text()
assert len(re.findall(r'^### API-\d{3} ',report,re.M))==179
assert len(re.findall(r'^### Model `',report,re.M))==60
assert 'OPEN / VALIDATION BLOCKED' in (HERE/'FINAL_SECURITY_VALIDATION_REPORT.md').read_text()
claim=read(HERE/'final-claim-ledger.json')
gap=read(HERE/'final-gap-ledger.json')
assert len(claim['claims'])==93 and len(gap['gaps'])==20
assert len({x['id'] for x in claim['claims']})==93
assert {x['gap_id'] for x in gap['gaps']}=={f'R{i:02d}' for i in range(1,21)}
assert all(x['classification'] in STATUSES for x in claim['claims']+gap['gaps'])
reset=read(HERE/'reset-flow-validation.json')
assert reset['fresh_tests_executed']==0
assert len(reset['proposed_tests_NOT_EXECUTED'])==11
nav=read(HERE/'navigation-closure.json')
assert len(nav['omitted_branches'])==5 and nav['counts']['literal_leaf_occurrences']==113
assert len(nav['href_attributes'])==5 and len(nav['dynamic_arguments'])==14

# Collect all actual file/path citations from the newly generated Markdown and
# structured evidence. Source expressions/API route strings are not file paths.
references={}
future={str(HERE/'FINAL_REVIEW_MANIFEST.json')}
def ref(path,line=None,origin=None):
    p=Path(path)
    assert p.is_absolute()
    key=(str(p),line)
    references.setdefault(key,set()).add(origin or 'structured reference')

for name in REPORTS:
    s=(HERE/name).read_text()
    for target in re.findall(r'\[[^\]\n]+\]\(<([^>\n]+)>\)',s):
        match=re.fullmatch(r'(.+?)(?::(\d+))?',target)
        ref(match[1],int(match[2]) if match[2] else None,name)

def walk(x,origin):
    if isinstance(x,dict):
        if isinstance(x.get('path'),str) and x['path'].startswith('/workspace/'):
            line=x.get('line_start',x.get('line',x.get('entry_line')))
            ref(x['path'],line if isinstance(line,int) else None,origin)
            if isinstance(x.get('line_end'),int): ref(x['path'],x['line_end'],origin)
        for k,v in x.items():
            if k in {'path','file','source_root','source_file','repo','repository','app','iteration','allowed_output'} and isinstance(v,str) and v.startswith('/workspace/'):
                # Exact structured paths only;code/path+symbol prose is not a path citation.
                ref(v,None,origin)
            walk(v,origin)
    elif isinstance(x,list):
        for v in x: walk(v,origin)

for name in ['navigation-closure.json','reset-flow-validation.json','provenance-gap-dispositions.json','final-claim-ledger.json']:
    walk(read(HERE/name),name)
for p in AUDIT_REPORTS+OLD_REPORTS+CHECKPOINTS:
    ref(p,None,'required original input')
for e in api['endpoints']:
    ref('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py',e['line'],'API source declaration')

# These files are generated below and become real references before final validation.
generated_pending={str(HERE/'reference-index.json'),str(HERE/'verification-results.json'),str(HERE/'FINAL_REVIEW_MANIFEST.json')}
reference_rows=[]
for (path,line),origins in sorted(references.items(),key=lambda i:(i[0][0],i[0][1] or 0)):
    p=Path(path)
    if path not in generated_pending:
        assert p.exists(), f'Missing evidence reference:{path}'
        if line:
            assert p.is_file() and 1<=line<=len(p.read_text().splitlines()),f'Badline reference:{path}:{line}'
    reference_rows.append({'path':path,'line':line,'origins':sorted(origins),'resolved':True})
save('reference-index.json',{'scope':'All generated Markdown link targets/line bounds and structured path-key evidence references. Literal API paths,code expressions and historical prose are not executable filesystem references.',
 'references':reference_rows})
input_rows=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in AUDIT_REPORTS+OLD_REPORTS]
result={'timestamp_Asia_Kolkata':now(),'project':'COME-IN','repository':str(REPO),'branch':branch,'HEAD':head,
 'classifications':'File/identity/reference/source-metadata checks only;not application or external verification.',
 'preservation_baselines':baselines,'nested_baseline_sets_verified':True,
 'original13reports_preserved':True,'original5checkpoints_preserved':True,
 'original_ZIP_and_inherited_patches_preserved':True,'tracked_git_worktree_diff_empty':True,'tracked_git_staged_diff_empty':True,
 'git_status_outside_new_iteration_unchanged':True,'generated_markdown_files':5,'generated_API_sections':179,'generated_model_sections':60,
 'claim_units':93,'gap_rows':20,'reference_targets_checked':len(reference_rows),
 'application_tests_executed':0,'DB_queries':0,'DB_writes':0,'provider_calls':0,'native_builds_or_device_tests':0,
 'originals_modified':0,'owner_approval':False,'Task2_started':False,
 'command':'python '+str(HERE/'verify-final-review.py'),
 'last_completed_operation':'All baseline/Git/source-metadata/reference checks passed. Final manifest generated and verified at end of this same command.',
 'next_action':'Stop for personal owner review. No tests,source fixes,Task2 or external operations authorized.',
 'final_recommendation':'REVIEW PENDING — EVIDENCE GAPS REMAIN'}
save('verification-results.json',result)

# Record a durable,readable stop point before hashing the new checkpoint itself.
with (HERE/'ITERATION_CHECKPOINT.md').open('a') as f:
    f.write(f'''\n## {now()} — preservation and document verification\n\nAll 8,476 protected files and the 8,504 iteration-baseline files match their captured SHA-256 values; all 8,150 original-audit entries also match. All 13 original reports and the five original checkpoints are preserved. Branch `work` / HEAD `{HEAD}` verified; tracked and staged diffs empty; pre-existing Git status outside this dated iteration unchanged. Five final reports, 179 API sections, 60 model sections, 20 gap dispositions, 93 claim dispositions and {len(reference_rows)} evidence targets checked. This is file/static evidence verification, not application testing. Application tests, database operations, provider calls, native builds and device tests: zero. HIGH SEC-01 remains OPEN / VALIDATION BLOCKED.\n\nLast operation: standalone file/Git/reference verification followed by manifest generation/hash comparison in this command. No operation was interrupted or remains running. Safe to rerun this verifier if needed; it reads original files and only refreshes NEW iteration evidence/checkpoint files. It must never change application source or original checkpoints. Exact stopping point: deliver this package for personal owner review. Next action: owner reads FINAL_OWNER_DECISION_READINESS.md and decides separately scoped future evidence work; no Task 2, fixes or application tests start here. If resuming, read all final reports, this checkpoint and verification-results.json first, verify branch/HEAD/Git status and manifest hashes, then wait for explicit owner instructions.\n''')

manifest_paths=[p for p in sorted(HERE.rglob('*')) if p.is_file() and p.name not in {'FINAL_REVIEW_MANIFEST.json','FINAL_REVIEW_MANIFEST.sha256'}]
manifest={'project':'COME-IN','created_Asia_Kolkata':now(),'repository':str(REPO),'application_extraction':'/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115',
 'branch':branch,'HEAD':head,'scope':'New final owner-review iteration;source-only and documentary verification,not owner approval or runtime release acceptance.',
 'required_final_Markdown_reports':REPORTS,'input13_original_reports':input_rows,
 'files':[{'relative_path':str(p.relative_to(HERE)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in manifest_paths],
 'self_hash_policy':'This manifest and its sidecar are excluded from files to avoid recursive hashes. The standalone sidecar records this manifest SHA-256.',
 'verification_artifact':'verification-results.json','source_declarations':api['counts'],'application_tests_run':0,
 'HIGH_SEC01':'OPEN / VALIDATION BLOCKED','Task1_status':'REVIEW PENDING;not approved or closed','Task2_started':False}
save('FINAL_REVIEW_MANIFEST.json',manifest)
(HERE/'FINAL_REVIEW_MANIFEST.sha256').write_text(sha(HERE/'FINAL_REVIEW_MANIFEST.json')+'  FINAL_REVIEW_MANIFEST.json\n')
for entry in manifest['files']:
    p=HERE/entry['relative_path']
    assert p.stat().st_size==entry['bytes'] and sha(p)==entry['sha256'],'New report hash mismatch'
assert (HERE/'FINAL_REVIEW_MANIFEST.sha256').read_text().split()[0]==sha(HERE/'FINAL_REVIEW_MANIFEST.json')
for row in reference_rows:
    assert Path(row['path']).exists(),'Generated reference did not resolve'
assert git('branch','--show-current').strip()=='work' and git('rev-parse','HEAD').strip()==HEAD
assert filtered_status(git('status','--porcelain=v1','--untracked-files=all'))==filtered_status(before)
print(json.dumps({'verification':'PASS — file/static evidence only','protected8476_mismatches':len(baselines[1]['mismatches']),
 'iteration8504_mismatches':len(baselines[2]['mismatches']),'required_final_files':6,
 'manifest_member_hashes_checked':len(manifest['files']),'reference_targets_checked':len(reference_rows),
 'manifest_sha256':sha(HERE/'FINAL_REVIEW_MANIFEST.json'),'application_tests_executed':0,
 'final_decision':'REVIEW PENDING'},indent=2))
