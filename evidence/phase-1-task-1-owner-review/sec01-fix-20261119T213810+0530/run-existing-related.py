from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,json,hashlib,xml.etree.ElementTree as ET
p=Path(__file__).resolve().parent
b=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
modules=['test_mongo_transactions.py','test_transaction_commit_retry.py','test_restaurant_api_contract.py','test_frontend_contracts.py','test_shared_system_integration_contract.py','test_grocery_capture_transaction_offline.py','test_restaurant_capture_transaction_offline.py','test_restaurant_refund_webhook_transaction_offline.py','test_final_payment_transition_races.py']
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
files=[b/'server.py',b/'mongo_transactions.py',b/'pytest.ini',*(b/'tests'/x for x in modules)]
bindings={str(f):sha(f) for f in files}
env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(p)+':'+str(b)+':'+str(b/'tests'))
cmd=['/workspace/come-in-tools/py311/bin/python','-B','-m','pytest',*[str(b/'tests'/x) for x in modules],'-q','-n','0','-p','no:cacheprovider','-p','old_related_network_guard','--junitxml='+str(p/'old-related-existing.xml'),'--basetemp='+str(p/'old-related-existing-tmp')]
started=datetime.now(timezone.utc).isoformat()
with (p/'old-related-existing.log').open('w') as log:r=subprocess.run(cmd,cwd=b,env=env,stdout=log,stderr=subprocess.STDOUT)
cases=list(ET.parse(p/'old-related-existing.xml').getroot().iter('testcase'))
counts={'PASS':sum(all(x.find(k) is None for k in ('failure','error','skipped')) for x in cases),'FAIL':sum(x.find('failure') is not None for x in cases),'ERROR':sum(x.find('error') is not None for x in cases),'SKIPPED':sum(x.find('skipped') is not None for x in cases)}
d={'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),'command':cmd,'cwd':str(b),'exit_code':r.returncode,'counts':counts,'modules':modules,'bindings_before':bindings,'bindings_after':{str(f):sha(f) for f in files},'protected_source_or_test_edits_by_runner':False,'network_guard':'allsocketconnect/create_connectiondeniedinthisprocess','rationale':'Existingtransactionhelper/retryandsharedauth/API/frontendcontractspluspayment/refundtransactioncallbackschecktheexistinghelperandunrelatedcriticalroutesafterreset_passwordonlychanges;nofull574or70rerun.'}
(p/'old-related-existing-results.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'exit_code':r.returncode,'counts':counts,'bindings_unchanged':d['bindings_before']==d['bindings_after']}))
