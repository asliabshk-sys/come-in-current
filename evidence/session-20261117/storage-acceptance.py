"""Local disposable real MongoDB validator, uniqueness, rollback and restore acceptance.
No provider calls or production data. Newly created DBs are retained for inspection.
"""
from pathlib import Path
import sys,json,subprocess,datetime
from pymongo import MongoClient
from pymongo.errors import WriteError,DuplicateKeyError
ROOT=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
sys.path.insert(0,str(ROOT))
from scripts.mongo import comein_mongo, catalogue_audit_validator, verify_disposable_restore
out=Path(__file__).parent
name='comein_disposable_test_acceptance_20261117'
target=name+'_restored'
c=MongoClient('mongodb://127.0.0.1:27018/?replicaSet=rs0',serverSelectionTimeoutMS=8000)
assert name not in c.list_database_names() and target not in c.list_database_names(), 'Refuse to overwrite an existing database; choose new unique names.'
db=c[name]; result={'source':name,'restore_target':target,'checks':{}}
result['init']=comein_mongo.init_db(db)
result['checks']['validator_install']=catalogue_audit_validator.install_validator(db)
valid={'apply_key':'catalogue-import:acceptance','shop_id':'synthetic-shop','seller_id':'synthetic-seller','job_id':'synthetic-job','record_count':1,'product_ids':['synthetic-product'],'created_at':datetime.datetime.now(datetime.timezone.utc)}
db.catalogue_import_audit.insert_one(dict(valid))
try: db.catalogue_import_audit.insert_one({'invalid':True})
except WriteError as e: assert e.code==121; result['checks']['invalid_document_rejected']=True
else: raise AssertionError('Validator did not reject invalid document')
try:
 with c.start_session() as session:
  with session.start_transaction():
   db.users.insert_one({'_id':'rollback-check','email':'rollback@synthetic.invalid'},session=session)
   db.catalogue_import_audit.insert_one({'invalid':True},session=session)
except WriteError as e: assert e.code==121
else: raise AssertionError('Transaction failure missing')
assert db.users.find_one({'_id':'rollback-check'}) is None
result['checks']['second_write_failure_rolls_back_first']=True
db.users.insert_one({'_id':'unique-first','email':'unique@synthetic.invalid'})
try: db.users.insert_one({'_id':'unique-second','email':'unique@synthetic.invalid'})
except DuplicateKeyError: result['checks']['unique_index_enforced']=True
else: raise AssertionError('Unique index did not reject duplicate')
assert comein_mongo.preflight_unique_indexes(db)['ok']
result['checks']['index_duplicate_preflight']=True
archive=out/'synthetic-acceptance.archive.gz'
with archive.open('xb') as f:
 subprocess.run(['docker','exec','comein-onboarding-mongo','mongodump','--port','27018','--db',name,'--archive','--gzip'],stdout=f,stderr=(out/'dump.log').open('w'),check=True)
with archive.open('rb') as f:
 subprocess.run(['docker','exec','-i','comein-onboarding-mongo','mongorestore','--port','27018','--archive','--gzip','--nsFrom',name+'.*','--nsTo',target+'.*'],stdin=f,stdout=(out/'restore.stdout.log').open('w'),stderr=(out/'restore.log').open('w'),check=True)
result['restore']=verify_disposable_restore.check_restore(db,c[target])
assert result['restore']['verified']
assert c[target].catalogue_import_audit.options()['validator']==catalogue_audit_validator.VALIDATOR
assert c[target].catalogue_import_audit.count_documents({})==1
result['checks']['validator_restored']=True
result['ok']=True
(out/'storage-acceptance.json').write_text(json.dumps(result,indent=2,default=str))
print(json.dumps({'ok':True,'checks':result['checks'],'restored_collections':len(result['restore']['collections'])}))
