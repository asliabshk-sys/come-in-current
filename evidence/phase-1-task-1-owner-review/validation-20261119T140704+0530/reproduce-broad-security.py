"""Independent reproduction justified by the original command-provenance gap."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parent
source=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py')
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
cmd=[sys.executable,'-m','pytest',str(p/'test_broad_security_isolated.py'),'-c',str(source.parent/'pytest.ini'),'-n','0','-p','no:cacheprovider','-q','--junitxml='+str(p/'broad-security-reproduced.xml'),'--basetemp='+str(p/'broad-security-reproduction-tmp')]
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
before=sha(source);started=datetime.now(timezone.utc).isoformat()
r=subprocess.run(cmd,cwd=p,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(p/'broad-security-reproduced.log').write_text(r.stdout)
cases=list(ET.parse(p/'broad-security-reproduced.xml').getroot().iter('testcase'))
counts={'PASS':sum(all(x.find(k) is None for k in ('failure','error','skipped')) for x in cases),'FAIL':sum(x.find('failure') is not None for x in cases),'ERROR':sum(x.find('error') is not None for x in cases),'SKIPPED':sum(x.find('skipped') is not None for x in cases)}
d={'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),'command':cmd,'cwd':str(p),'exit_code':r.returncode,'counts':counts,'source_path':str(source),'source_sha256_before':before,'source_sha256_after':sha(source),'test_path':str(p/'test_broad_security_isolated.py'),'test_sha256':sha(p/'test_broad_security_isolated.py'),'reason_for_reproduction':'Saved v2 outcomes existed,but the exact original shell command was not persisted. Independent unchanged-source reproduction binds the current command/source/environment without inventing past provenance.','scope':'Actual AST-extracted models/helpers with in-memory synthetic collection doubles. Autouse fixture denies all socket connections;no server import or DB/provider calls.','original_attempts_retained':True,'source_modified':False,'failure_is_NOT_suppressed':True,'new_provenance_cannot_authenticate_old_run':True}
(p/'broad-security-reproduction.json').write_text(json.dumps(d,indent=2)+'\n')
assert before==sha(source)
print(json.dumps({'exit_code':r.returncode,'counts':counts,'source_hash_unchanged':True}))
