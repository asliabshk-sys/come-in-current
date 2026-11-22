"""Only hello/listCollections/listIndexes on the previously identified disposable local DB.
No health/init/transaction helper imports, queries of application records or writes.
"""
from pathlib import Path
import json
from pymongo import MongoClient
out=Path(__file__).parent/'local-db-readonly-metadata.json'
try:
 client=MongoClient('mongodb://127.0.0.1:27018/?replicaSet=rs0',serverSelectionTimeoutMS=3000,connectTimeoutMS=3000)
 hello=client.admin.command('hello')
 assert hello.get('setName')=='rs0'
 assert all(host.startswith(('127.0.0.1:','localhost:')) for host in hello.get('hosts',[]))
 db=client['comein_disposable_test_onboarding'];collections=[]
 for c in db.list_collections():
  name=c['name'];collections.append({'name':name,'type':c.get('type'),'validator_present':bool(c.get('options',{}).get('validator')),'validationLevel':c.get('options',{}).get('validationLevel'),'indexes':[{k:v for k,v in dict(i).items() if k not in ['ns']} for i in db[name].list_indexes()]})
 result={'status':'RUNTIME VERIFIED read-only metadata only','target':'previously identified local disposable DB','replica_set':hello['setName'],'is_primary':hello.get('isWritablePrimary'),'collections':collections,'record_data_read':False,'writes':0,'production_access':False,'commands':['hello','listCollections','listIndexes']};client.close();out.write_text(json.dumps(result,indent=2,default=str));print('Read-only metadata:',len(collections),'collections;writes0;no application records read')
except Exception as exc:
 out.write_text(json.dumps({'status':'BLOCKED','error_type':type(exc).__name__,'writes':0,'next':'Use retained historical DB/index evidence;do not start/reconfigure database.'},indent=2));print('Read-only DB metadata BLOCKED:',type(exc).__name__)
