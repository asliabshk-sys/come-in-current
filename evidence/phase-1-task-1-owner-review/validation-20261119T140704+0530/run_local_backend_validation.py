"""Real local Mongo/HTTP regression;no actual providers,credentials or production data."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,secrets,shutil,socket,subprocess,time,uuid
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parent
APP=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
PYTHON='/workspace/come-in-tools/py311/bin/python'
URI='mongodb://127.0.0.1:27018/?replicaSet=rs0'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(path):
    cases=[]
    if not path.exists():return {'PASS':0,'FAIL':0,'SKIPPED':0},cases
    for c in ET.parse(path).getroot().iter('testcase'):
        status='FAIL' if c.find('failure') is not None or c.find('error') is not None else 'SKIPPED' if c.find('skipped') is not None else 'PASS'
        node=c.find('failure')
        if node is None:node=c.find('error')
        if node is None:node=c.find('skipped')
        cases.append({'class':c.get('classname'),'name':c.get('name'),'status':status,'reason':node.get('message') if node is not None else None})
    return {s:sum(c['status']==s for c in cases) for s in ['PASS','FAIL','SKIPPED']},cases

def env_base(dbname,port):
    # Deliberately whitelist OS/tool metadata rather than inheriting provider/DB secrets.
    e={k:os.environ[k] for k in ['PATH','HOME','LANG','LC_ALL','TMPDIR'] if k in os.environ}
    e.update(PYTHONPATH=os.pathsep.join([str(OUT),str(APP),str(APP/'backend')]),PYTHONDONTWRITEBYTECODE='1',
        APP_ENV='test',MONGO_URL=URI,DB_NAME=dbname,MONGO_EXPECTED_DB_NAME=dbname,
        JWT_SECRET=secrets.token_urlsafe(48),CORS_ORIGINS='http://validation.local',
        COMEIN_VALIDATION_PORT=str(port))
    return e

started=datetime.now(timezone.utc).isoformat()
sourcefiles=[p for base in [APP/'backend',APP/'scripts'] for p in base.rglob('*.py') if '__pycache__' not in p.parts]
sourcehashes={str(p):sha(p) for p in sourcefiles}
records=[]

# The two existing opt-in modules create unique new DBs themselves. Their in-process
# provider mocks are deliberately labelled mock integration,not real Razorpay.
local_env=env_base('comein_disposable_test_review_import_'+uuid.uuid4().hex[:10],0)
local_env['COMEIN_RUN_LOCAL_PAYMENT_TESTS']='1'
cmd=[PYTHON,'-m','pytest','tests/test_payment_webhook_local_integration.py','tests/test_grocery_refund_local_integration.py',
     '-q','-n','0','-p','no:cacheprovider','-p','backend_local_guard','--junitxml='+str(OUT/'backend-local-payments.xml'),
     '--basetemp='+str(OUT/'backend-local-payment-tmp')]
with (OUT/'backend-local-payments.log').open('x') as log:r=subprocess.run(cmd,cwd=APP/'backend',env=local_env,stdout=log,stderr=subprocess.STDOUT)
counts,cases=parse(OUT/'backend-local-payments.xml')
records.append({'category':'actual local ASGI+MongoDB with provider mocked','command':cmd,'exit_code':r.returncode,'counts':counts,'cases':cases,
                'pytest_source_paths':[str(APP/'backend/tests/test_payment_webhook_local_integration.py'),str(APP/'backend/tests/test_grocery_refund_local_integration.py')],
                'provider_calls':'0 actual external calls;existing tests install in-process provider mocks',
                'dotenv_files_read':False,'databases':'unique comein_disposable_test_webhooks_* and comein_disposable_test_refund_* allocated by existing tests;retained,not dropped'})

# Byte-identical copies preserve every assertion while preventing the legacy test
# module's fallback ROOT/.env path from finding any actual environment file.
testdir=OUT/'live-tests';testdir.mkdir()
names=['test_preview_runtime_e2e.py','test_batch_5task_runtime.py','test_iter_notifications_admin_measured.py','test_task5_live_mongo_transactions.py','seed_preview_test_accounts.py']
copies=[]
for name in names:
    original=APP/'backend/tests'/name;target=testdir/name;shutil.copyfile(original,target)
    assert sha(original)==sha(target)
    copies.append({'original':str(original),'copy':str(target),'sha256':sha(original),'byte_identical':True})
with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
dbname='comein_disposable_test_review_'+uuid.uuid4().hex[:16]
e=env_base(dbname,port);e['EXPO_PUBLIC_BACKEND_URL']=f'http://127.0.0.1:{port}'
suffix=uuid.uuid4().hex[:10]
for role in ['ADMIN','CUSTOMER','SELLER','RESTO']:
    e[f'COMEIN_TEST_{role}_EMAIL']=f'review.{role.lower()}.{suffix}@comein-preview.com'
    e[f'COMEIN_TEST_{role}_PASSWORD']=secrets.token_urlsafe(22)
e['ADMIN_EMAIL']=e['COMEIN_TEST_ADMIN_EMAIL'];e['ADMIN_PASSWORD']=e['COMEIN_TEST_ADMIN_PASSWORD']
server_cmd=[PYTHON,str(OUT/'local_backend_bootstrap.py')]
with (OUT/'isolated-backend-server.log').open('x') as log:
    p=subprocess.Popen(server_cmd,cwd=APP/'backend',env=e,stdout=log,stderr=subprocess.STDOUT)
    try:
        import requests
        ready=False
        for _ in range(120):
            if p.poll() is not None:break
            try:
                response=requests.get(e['EXPO_PUBLIC_BACKEND_URL']+'/api/',timeout=0.8)
                if response.status_code==200:ready=True;break
            except requests.RequestException:pass
            time.sleep(0.25)
        if not ready:
            records.append({'category':'isolated local HTTP four-module regression','status':'BLOCKED','reason':'isolated backend did not become ready','server_exit':p.poll(),'command':server_cmd,'database':dbname})
        else:
            seed_cmd=[PYTHON,str(testdir/'seed_preview_test_accounts.py')]
            with (OUT/'backend-live-seed.log').open('x') as seedlog:
                seed=subprocess.run(seed_cmd,cwd=APP/'backend',env=e,stdout=seedlog,stderr=subprocess.STDOUT)
            if seed.returncode:
                records.append({'category':'isolated local HTTP four-module regression','status':'FAIL','reason':'synthetic fixture seeding failed','exit_code':seed.returncode,'command':seed_cmd,'database':dbname})
            else:
                livecmd=[PYTHON,'-m','pytest',*[str(testdir/n) for n in names[:-1]],'-q','-n','0','-p','no:cacheprovider','-p','backend_local_guard',
                    '-c',str(APP/'backend/pytest.ini'),'--junitxml='+str(OUT/'backend-live.xml'),'--basetemp='+str(OUT/'backend-live-tmp')]
                with (OUT/'backend-live.log').open('x') as livelog:live=subprocess.run(livecmd,cwd=APP/'backend',env=e,stdout=livelog,stderr=subprocess.STDOUT)
                counts,cases=parse(OUT/'backend-live.xml')
                records.append({'category':'isolated local HTTP+real MongoDB four-module regression','command':livecmd,'exit_code':live.returncode,'counts':counts,'cases':cases,
                    'database':dbname,'loopback_port':port,'test_copies':copies,'dotenv_files_read':False,
                    'test_copy_reason':'Byte-identical test copies execute against explicit process env;their fallback ROOT/backend/.env and ROOT/frontend/.env paths do not exist. No assertions changed.',
                    'provider_calls':'No provider bindings;backend socket guard allows onlyloopbacktestportandMongo27018',
                    'database_retention':'Database retained,no drops. Existingtask5teardowndeletesonlyitssyntheticfixtureswithinthisnewDB.'})
    finally:
        p.terminate()
        try:p.wait(timeout=15)
        except subprocess.TimeoutExpired:p.kill();p.wait()
changed=[str(p) for p in sourcefiles if sha(p)!=sourcehashes[str(p)]]
result={'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),'records':records,
        'source_hashes_before':sourcehashes,'source_changed':changed,
        'totals':{s:sum(x.get('counts',{}).get(s,0) for x in records) for s in ['PASS','FAIL','SKIPPED']},
        'isolated_backend_stopped':True,'production_operations':0,'real_provider_operations':0,'source_or_configuration_changes':0}
(OUT/'backend-local-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'totals':result['totals'],'record_summaries':[{k:v for k,v in x.items() if k in ['category','status','counts','exit_code','reason']} for x in records],'source_changed':changed}))
