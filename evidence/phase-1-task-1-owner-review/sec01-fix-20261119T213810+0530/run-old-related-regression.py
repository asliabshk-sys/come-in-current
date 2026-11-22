from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,json,hashlib,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parent
app=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
py='/workspace/come-in-tools/py311/bin/python'
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
results=[]
for label,source in [('before',p/'before/backend/server.py'),('after',app/'backend/server.py')]:
 out=p/('old-30-'+label);out.mkdir(exist_ok=True)
 env=os.environ.copy();env.update(SEC01_OUTPUT_DIR=str(out),SEC01_SOURCE=str(source),PYTHONDONTWRITEBYTECODE='1')
 cmd=[py,'-B',str(p/'old-30-runner-compatible.py')]
 started=datetime.now(timezone.utc).isoformat();before=sha(source)
 with (out/'execution.log').open('w') as log:r=subprocess.run(cmd,cwd=p,env=env,stdout=log,stderr=subprocess.STDOUT)
 d=json.loads((out/'password-reset-results-v2.json').read_text())
 rec={'phase':label,'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),'command':cmd,'cwd':str(p),'source_path':str(source),'source_SHA256_before':before,'source_SHA256_after':sha(source),'exit_code':r.returncode,'counts':d['counts'],'database_retained':d['database']['name'],'fail_cases':[x['id'] for x in d['cases'] if x['status']=='FAIL'],'error_cases':[x['id'] for x in d['cases'] if x['status']=='ERROR'],'result_path':str(out/'password-reset-results-v2.json')}
 results.append(rec);(p/'old-30-before-after-results.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(rec),flush=True)
