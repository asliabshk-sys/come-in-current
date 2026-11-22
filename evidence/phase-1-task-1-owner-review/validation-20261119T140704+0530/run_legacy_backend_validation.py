"""One additional unchanged legacy suite on a fresh disposable local backend."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,secrets,shutil,socket,subprocess,time,uuid
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parent
APP=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
PYTHON='/workspace/come-in-tools/py311/bin/python'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def redacted(text):
    text=re.sub(r'eyJ[A-Za-z0-9_.-]+','[REDACTED_SYNTHETIC_JWT]',text)
    for value in sensitive:
        text=text.replace(value,'[REDACTED_SYNTHETIC_FIXTURE]')
    return text

original=APP/'backend/tests/backend_test.py'
stale=APP/'backend/tests/STALE_CONTRACT_TESTS.txt'
sourcepaths=[p for base in [APP/'backend',APP/'scripts'] for p in base.rglob('*.py') if '__pycache__' not in p.parts]
source_before={str(p):sha(p) for p in sourcepaths}
testdir=OUT/'legacy-tests';testdir.mkdir()
copy=testdir/'backend_test.py';shutil.copyfile(original,copy)
assert sha(original)==sha(copy)
with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
dbname='comein_disposable_test_review_'+uuid.uuid4().hex[:16]
env={k:os.environ[k] for k in ['PATH','HOME','LANG','LC_ALL','TMPDIR'] if k in os.environ}
env.update(PYTHONPATH=os.pathsep.join([str(OUT),str(APP),str(APP/'backend')]),PYTHONDONTWRITEBYTECODE='1',
           APP_ENV='test',MONGO_URL='mongodb://127.0.0.1:27018/?replicaSet=rs0',DB_NAME=dbname,
           MONGO_EXPECTED_DB_NAME=dbname,JWT_SECRET=secrets.token_urlsafe(48),CORS_ORIGINS='http://validation.local',
           COMEIN_VALIDATION_PORT=str(port),COMEIN_TEST_BASE_URL=f'http://127.0.0.1:{port}',
           COMEIN_TEST_ADMIN_EMAIL='review.legacy.admin.'+uuid.uuid4().hex[:8]+'@comein-preview.com',
           COMEIN_TEST_ADMIN_PASSWORD=secrets.token_urlsafe(24))
env['ADMIN_EMAIL']=env['COMEIN_TEST_ADMIN_EMAIL'];env['ADMIN_PASSWORD']=env['COMEIN_TEST_ADMIN_PASSWORD']
sensitive=[env['JWT_SECRET'],env['COMEIN_TEST_ADMIN_PASSWORD'],'test1234','pw12345']
cmd=[PYTHON,'-m','pytest',str(copy),'-q','-n','0','-p','no:cacheprovider','-p','backend_local_guard',
     '-c',str(APP/'backend/pytest.ini'),'--junitxml='+str(OUT/'backend-legacy.xml'),
     '--basetemp='+str(OUT/'backend-legacy-tmp')]
started=datetime.now(timezone.utc).isoformat()
servercmd=[PYTHON,str(OUT/'local_backend_bootstrap.py')]
result={'started_UTC':started,'scope':'Additional legacy regression on fresh isolated local HTTP+Mongo;no assertion changes',
        'command':cmd,'server_command':servercmd,'database':dbname,'port':port,
        'copied_original':str(original),'copied_test':str(copy),'test_sha256':sha(original),'byte_identical':True,
        'stale_contract_list':{'path':str(stale),'sha256':sha(stale),'read_in_full':True,
                               'legacy_backend_test_entries_found':sum('backend_test.py' in x for x in stale.read_text().splitlines())},
        'dotenv_read':False,'real_provider_calls':0,'source_before':source_before}
with (OUT/'isolated-legacy-server.log').open('x') as serverlog:
    p=subprocess.Popen(servercmd,cwd=APP/'backend',env=env,stdout=serverlog,stderr=subprocess.STDOUT)
    try:
        import requests
        ready=False
        for _ in range(120):
            if p.poll() is not None:break
            try:
                response=requests.get(env['COMEIN_TEST_BASE_URL']+'/api/',timeout=0.8)
                if response.status_code==200:ready=True;break
            except requests.RequestException:pass
            time.sleep(.25)
        if ready:
            r=subprocess.run(cmd,cwd=APP/'backend',env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (OUT/'backend-legacy.log').write_text(redacted(r.stdout))
            result['exit_code']=r.returncode
            xml=OUT/'backend-legacy.xml'
            xml.write_text(redacted(xml.read_text()))
            cases=[]
            for c in ET.parse(xml).getroot().iter('testcase'):
                node=c.find('failure');kind='failure'
                if node is None:node=c.find('error');kind='error'
                if node is None:node=c.find('skipped');kind='skipped'
                status='FAIL' if kind in {'failure','error'} and node is not None else 'SKIPPED' if node is not None else 'PASS'
                cases.append({'class':c.get('classname'),'name':c.get('name'),'status':status,
                              'node_kind':kind if node is not None else None,
                              'reason':node.get('message') if node is not None else None,
                              'detail':node.text if node is not None else None})
            result['cases']=cases
            result['counts']={s:sum(c['status']==s for c in cases) for s in ['PASS','FAIL','SKIPPED']}
        else:
            result.update(status='BLOCKED',reason='Isolated backend failed startup',server_exit=p.poll())
    finally:
        p.terminate()
        try:p.wait(timeout=15)
        except subprocess.TimeoutExpired:p.kill();p.wait()
result.update(finished_UTC=datetime.now(timezone.utc).isoformat(),isolated_backend_stopped=True,
              database_retained=True,database_drops=0,source_changed=[p for p,h in source_before.items() if sha(p)!=h],
              log_redaction='Synthetic fixture password/JWT representations redacted in logs/XML;assertions and outcomes unchanged.')
(OUT/'backend-legacy-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['counts','exit_code','source_changed','database_retained','isolated_backend_stopped'] if k in result}))
