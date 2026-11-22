"""Execute legacy contracts against a unique disposable local backend only."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,re,secrets,shutil,socket,subprocess,sys,time,uuid
import xml.etree.ElementTree as ET

P=Path(__file__).resolve().parent
A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
parser=argparse.ArgumentParser();parser.add_argument('--stage',required=True);parser.add_argument('--server-source',type=Path,default=A/'backend/server.py');parser.add_argument('--test-source',type=Path,default=A/'backend/tests/backend_test.py');args=parser.parse_args()
assert re.fullmatch(r'[a-z0-9-]+',args.stage)
out=P/('legacy-'+args.stage);out.mkdir(exist_ok=False)
testdir=out/'test-copy';testdir.mkdir();target=testdir/'backend_test.py';shutil.copyfile(args.test_source,target)
assert sha(target)==sha(args.test_source)
with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
dbname='comein_disposable_test_completion_'+uuid.uuid4().hex[:16]
env={k:os.environ[k] for k in ['PATH','HOME','LANG','LC_ALL','TMPDIR'] if k in os.environ}
env.update(PYTHONPATH=os.pathsep.join([str(P),str(A),str(A/'backend')]),PYTHONDONTWRITEBYTECODE='1',
 APP_ENV='test',MONGO_URL='mongodb://127.0.0.1:27018/?replicaSet=rs0',DB_NAME=dbname,MONGO_EXPECTED_DB_NAME=dbname,
 JWT_SECRET=secrets.token_urlsafe(48),CORS_ORIGINS='http://validation.local',COMEIN_VALIDATION_PORT=str(port),
 COMEIN_VALIDATION_SERVER_SOURCE=str(args.server_source.resolve()),COMEIN_TEST_BASE_URL=f'http://127.0.0.1:{port}',
 COMEIN_TEST_ADMIN_EMAIL='completion.admin.'+uuid.uuid4().hex[:8]+'@example.com',COMEIN_TEST_ADMIN_PASSWORD=secrets.token_urlsafe(24))
env['ADMIN_EMAIL']=env['COMEIN_TEST_ADMIN_EMAIL'];env['ADMIN_PASSWORD']=env['COMEIN_TEST_ADMIN_PASSWORD']
sensitive=[env['JWT_SECRET'],env['COMEIN_TEST_ADMIN_PASSWORD'],'test1234','pw12345']
def redacted(text):
 text=re.sub(r'eyJ[A-Za-z0-9_.-]+','[REDACTED_SYNTHETIC_JWT]',text)
 for value in sensitive:text=text.replace(value,'[REDACTED_SYNTHETIC_FIXTURE]')
 return text
cmd=[sys.executable,'-B','-m','pytest',str(target),'-q','-n','0','-p','no:cacheprovider','-p','isolated_backend_guard','-c',str(A/'backend/pytest.ini'),'--junitxml='+str(out/'junit.xml'),'--basetemp='+str(out/'pytest-tmp')]
source_bindings={str(args.server_source.resolve()):sha(args.server_source),str(args.test_source.resolve()):sha(args.test_source),str(A/'backend/mongo_transactions.py'):sha(A/'backend/mongo_transactions.py')}
d={'stage':args.stage,'started_UTC':datetime.now(timezone.utc).isoformat(),'command':cmd,'server_command':[sys.executable,'-B',str(P/'isolated_backend_bootstrap.py')],'database':dbname,'port':port,'test_copy_byte_identical':True,'source_bindings_before':source_bindings,'dotenv_read':False,'real_provider_calls':0,'native_validation':False}
with (out/'server.log').open('x') as log:
 proc=subprocess.Popen(d['server_command'],cwd=A/'backend',env=env,stdout=log,stderr=subprocess.STDOUT)
 try:
  import requests
  ready=False
  for _ in range(120):
   if proc.poll() is not None:break
   try:
    if requests.get(env['COMEIN_TEST_BASE_URL']+'/api/',timeout=.8).status_code==200:ready=True;break
   except requests.RequestException:pass
   time.sleep(.25)
  if not ready:d.update(status='BLOCKED',reason='Isolated backend startup failed',server_exit=proc.poll())
  else:
   run=subprocess.run(cmd,cwd=A/'backend',env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
   (out/'pytest.log').write_text(redacted(run.stdout));d['exit_code']=run.returncode
   xml=out/'junit.xml';xml.write_text(redacted(xml.read_text()))
   cases=[]
   for c in ET.parse(xml).getroot().iter('testcase'):
    kind=next((n for n in ['failure','error','skipped'] if c.find(n) is not None),None);node=c.find(kind) if kind else None
    cases.append({'classname':c.get('classname'),'name':c.get('name'),'status':{'failure':'FAIL','error':'ERROR','skipped':'SKIPPED'}.get(kind,'PASS'),'message':node.get('message') if node is not None else None,'detail':node.text if node is not None else None})
   d['cases']=cases;d['counts']={s:sum(x['status']==s for x in cases) for s in ['PASS','FAIL','ERROR','SKIPPED']}
 finally:
  proc.terminate()
  try:proc.wait(timeout=15)
  except subprocess.TimeoutExpired:proc.kill();proc.wait()
text=(out/'server.log').read_text();(out/'server.log').write_text(redacted(text))
d.update(finished_UTC=datetime.now(timezone.utc).isoformat(),database_retained=True,database_drops=0,isolated_backend_stopped=True,source_bindings_after={n:sha(n) for n in source_bindings},source_changes=[n for n,h in source_bindings.items() if sha(n)!=h])
(out/'result.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({k:d[k] for k in ['stage','status','counts','exit_code','reason','source_changes'] if k in d}))
