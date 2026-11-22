from pathlib import Path
from dotenv import dotenv_values
import os,subprocess,secrets,json,sys
root=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
evidence=Path('/workspace/come-in-current/evidence/resume-20261118')
v=dotenv_values(root/'backend/.env')
assert v['DB_NAME']=='comein_disposable_test_onboarding'
e=os.environ.copy(); e.update({'EXPO_PUBLIC_BACKEND_URL':'http://127.0.0.1:8001','COMEIN_TEST_ADMIN_EMAIL':v['ADMIN_EMAIL'],'COMEIN_TEST_ADMIN_PASSWORD':v['ADMIN_PASSWORD']})
accounts=Path('/workspace/come-in-tools/continuation-test-accounts.json')
if not accounts.exists():
 accounts.write_text(json.dumps({p:secrets.token_urlsafe(20) for p in ['CUSTOMER','SELLER','RESTO']})); accounts.chmod(0o600)
for prefix,pw in json.loads(accounts.read_text()).items():
 e['COMEIN_TEST_'+prefix+'_EMAIL']='continuation.'+prefix.lower()+'@comein-preview.com'
 e['COMEIN_TEST_'+prefix+'_PASSWORD']=pw
with (evidence/'live-seed-final.log').open('w') as log:
 r=subprocess.run([sys.executable,'tests/seed_preview_test_accounts.py'],cwd=root/'backend',env=e,stdout=log,stderr=subprocess.STDOUT)
if r.returncode: raise SystemExit(r.returncode)
with (evidence/'live-regression-final.log').open('w') as log:
 r=subprocess.run([sys.executable,'-m','pytest','-n','0','-q','tests/test_preview_runtime_e2e.py','tests/test_batch_5task_runtime.py','tests/test_iter_notifications_admin_measured.py','tests/test_task5_live_mongo_transactions.py','--junitxml='+str(evidence/'live-regression-final.xml')],cwd=root/'backend',env=e,stdout=log,stderr=subprocess.STDOUT)
raise SystemExit(r.returncode)
