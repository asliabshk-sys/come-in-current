"""Run reviewed unmodified tests with evidence outputs outside application source."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import platform
import subprocess
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parent
APP=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
PYTHON='/workspace/come-in-tools/py311/bin/python'
EXCLUDED=['test_preview_runtime_e2e.py','test_batch_5task_runtime.py',
          'test_iter_notifications_admin_measured.py','test_task5_live_mongo_transactions.py','backend_test.py']

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sources():
    items={}
    for base in [APP/'backend',APP/'scripts']:
        for p in sorted(base.rglob('*.py')):
            if '__pycache__' not in p.parts:items[str(p)]=sha(p)
    for p in [APP/'backend/pytest.ini',APP/'backend/requirements.txt',APP/'frontend/package.json',APP/'frontend/yarn.lock']:
        if p.exists():items[str(p)]=sha(p)
    return items

source_before=sources()
cmd=[PYTHON,'-m','pytest','tests','-q','-n','0','-p','no:cacheprovider','-p','backend_network_guard']
cmd += ['--ignore=tests/'+x for x in EXCLUDED]
cmd += ['--junitxml='+str(OUT/'backend-offline.xml'),'--basetemp='+str(OUT/'backend-offline-tmp')]
env=dict(os.environ)
for key in list(env):
    if any(s in key for s in ['RAZORPAY','COMEIN_TEST_','COMEIN_RUN_LOCAL_PAYMENT_TESTS','SMTP_', 'COMEIN_AI_', 'OPENAI_', 'STRIPE_']):env.pop(key,None)
env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=os.pathsep.join([str(OUT),str(APP),str(APP/'backend')]),
           APP_ENV='test',MONGO_URL='mongodb://127.0.0.1:27018/?replicaSet=rs0',
           DB_NAME='comein_disposable_test_offline_unused')
start=datetime.now(timezone.utc).isoformat()
with (OUT/'backend-offline.log').open('x') as log:
    result=subprocess.run(cmd,cwd=APP/'backend',env=env,stdout=log,stderr=subprocess.STDOUT,text=True)
finish=datetime.now(timezone.utc).isoformat()
source_after=sources()
source_changed=[p for p,h in source_before.items() if source_after.get(p)!=h]
cases=[]
if (OUT/'backend-offline.xml').exists():
    root=ET.parse(OUT/'backend-offline.xml').getroot()
    for c in root.iter('testcase'):
        failure=c.find('failure');error=c.find('error');skip=c.find('skipped')
        status='FAIL' if failure is not None or error is not None else 'SKIPPED' if skip is not None else 'PASS'
        node=failure if failure is not None else error if error is not None else skip
        cases.append({'class':c.get('classname'),'name':c.get('name'),'status':status,
                      'reason':node.get('message') if node is not None else None})
data={'scope':'All reviewed offline backend/source-contract tests,unmodified;not provider/device/live acceptance',
      'started_UTC':start,'finished_UTC':finish,'cwd':str(APP/'backend'),'command':cmd,
      'python':PYTHON,'platform':platform.platform(),'exit_code':result.returncode,
      'excluded_network_suites':EXCLUDED,'network':'Python socket connections fail closed;reviewed shell subprocesses only fake backup binary/restore refusal paths',
      'cache_and_bytecode':'pytest cacheprovider disabled;PYTHONDONTWRITEBYTECODE=1;tmp_path outside source',
      'source_before':source_before,'source_changed':source_changed,
      'counts':{s:sum(c['status']==s for c in cases) for s in ['PASS','FAIL','SKIPPED']},'cases':cases,
      'source_identity':'Archive extraction outside Git;source hashes identify this exact run;Git HEAD alone does not identify applied uncommitted extraction changes.'}
(OUT/'backend-offline-result.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'exit_code':result.returncode,'counts':data['counts'],'source_changed':source_changed}))
raise SystemExit(result.returncode or (1 if source_changed else 0))
