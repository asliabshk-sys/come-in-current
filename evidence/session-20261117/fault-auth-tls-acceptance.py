"""Isolated TLS replica: real driver retries and authorization; never application rs0.
Requires one-use bootstrap outside Git. Test credentials/cert private keys stay outside repo.
"""
from pathlib import Path
import sys,asyncio,json
from pymongo import MongoClient
from pymongo.errors import OperationFailure,ServerSelectionTimeoutError
from pymongo.monitoring import CommandListener
from motor.motor_asyncio import AsyncIOMotorClient
sys.path.insert(0,'/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
from mongo_transactions import run_transaction
p=Path('/workspace/come-in-tools/fault-tls-20261117'); v=json.loads((p/'accounts.json').read_text())
uri='mongodb://127.0.0.1:27019/?replicaSet=acceptance-rs'
opts={'tls':True,'tlsCAFile':str(p/'cert.pem'),'serverSelectionTimeoutMS':3000,'connectTimeoutMS':2000}
a=MongoClient(uri,username='acceptance_admin',password=v['admin'],**opts)
dbname='comein_disposable_test_faults_v2'; db=a[dbname];results=[]
assert db.retry_cases.count_documents({})==0,'Do not replay completed fault tests; use new IDs and evidence filenames.'
db.retry_cases.insert_one({'_id':'seed'})
class Counter(CommandListener):
 def __init__(self):self.commits=0
 def started(self,event):
  if event.command_name=='commitTransaction':self.commits+=1
 def succeeded(self,event):pass
 def failed(self,event):pass
monitor=Counter()
async def main():
 c=AsyncIOMotorClient(uri,username='acceptance_admin',password=v['admin'],event_listeners=[monitor],**opts);db=c[dbname]
 a.admin.command({'configureFailPoint':'failCommand','mode':{'times':1},'data':{'failCommands':['insert'],'errorCode':112,'errorLabels':['TransientTransactionError']}})
 calls=0
 async def transient(session):
  nonlocal calls;calls+=1
  await db.retry_cases.insert_one({'_id':'transient'},session=session)
 await run_transaction(c,transient)
 assert calls==2 and await db.retry_cases.count_documents({'_id':'transient'})==1
 results.append({'check':'TransientTransactionError reruns callback without duplicate write','callback_attempts':calls})
 a.admin.command({'configureFailPoint':'failCommand','mode':{'times':1},'data':{'failCommands':['commitTransaction'],'errorCode':91,'errorLabels':['UnknownTransactionCommitResult']}})
 calls=0;before=monitor.commits
 async def ambiguous(session):
  nonlocal calls;calls+=1
  await db.retry_cases.insert_one({'_id':'unknown-commit'},session=session)
 await run_transaction(c,ambiguous)
 assert calls==1 and monitor.commits-before>=2 and await db.retry_cases.count_documents({'_id':'unknown-commit'})==1
 results.append({'check':'UnknownTransactionCommitResult retries commit with one durable write','callback_attempts':calls,'commit_attempts':monitor.commits-before})
 c.close()
try:asyncio.run(main())
finally:a.admin.command({'configureFailPoint':'failCommand','mode':'off'})
a.admin.command('updateUser','acceptance_reader',roles=[{'role':'read','db':dbname}])
reader=MongoClient(uri,username='acceptance_reader',password=v['reader'],**opts)
assert reader[dbname].retry_cases.count_documents({})==3
try:reader[dbname].retry_cases.insert_one({'_id':'forbidden'})
except OperationFailure as exc:assert exc.code==13
else:raise AssertionError('Read-only role permitted write')
results.append({'check':'read-only authenticated identity can read and cannot write'})
unauth=MongoClient(uri,**opts)
try:unauth[dbname].retry_cases.find_one({})
except OperationFailure as exc:assert exc.code==13
else:raise AssertionError('Unauthenticated data access accepted')
results.append({'check':'unauthenticated data access rejected'})
for label,kw in [('plaintext',{'tls':False}),('untrusted-certificate',{'tls':True})]:
 c=MongoClient(uri,serverSelectionTimeoutMS=1200,connectTimeoutMS=800,**kw)
 try:c.admin.command('ping')
 except ServerSelectionTimeoutError:results.append({'check':label+' connection rejected'})
 else:raise AssertionError(label+' connection accepted')
 finally:c.close()
Path(__file__).with_suffix('.json').write_text(json.dumps({'ok':True,'checks':results,'scope':'isolated local synthetic TLS/auth replica; does not validate production TLS or external providers'},indent=2))
print(json.dumps({'ok':True,'checks':results}))
