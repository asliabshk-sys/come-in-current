"""Read-only metadata capture for the previously identified loopback disposable DB."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
from pymongo import MongoClient

out=Path(__file__).resolve().parent
repo=Path('/workspace/come-in-current')
client=MongoClient('mongodb://127.0.0.1:27018/?replicaSet=rs0',serverSelectionTimeoutMS=8000,connectTimeoutMS=5000)
hello=client.admin.command('hello')
assert hello.get('setName')=='rs0' and hello.get('isWritablePrimary') is True
assert all(h.startswith(('127.0.0.1:','localhost:')) for h in hello.get('hosts',[]))
db=client['comein_disposable_test_onboarding']
rows=[]
for c in db.list_collections():
    opts=c.get('options',{})
    rows.append({'name':c['name'],'type':c.get('type'),'raw_options':opts,
                 'validator_key_present':'validator' in opts,'validator_value':opts.get('validator'),
                 'indexes':[dict(i) for i in db[c['name']].list_indexes()]})
decls=json.loads((repo/'evidence/phase-1-task-1-audit/index-inventory.json').read_text())
byname={r['name']:r for r in rows}
matches=[]
for d in decls:
    wanted=[(d['keys'],1)] if isinstance(d['keys'],str) else [tuple(x) for x in d['keys']]
    candidates=[]
    for idx in byname.get(d['collection'],{}).get('indexes',[]):
        if list(idx['key'].items())==wanted and all(idx.get(k,False if k in ('unique','sparse') else None)==v for k,v in d['options'].items()):
            candidates.append(idx['name'])
    matches.append({'collection':d['collection'],'source_line':d['line'],'keys':d['keys'],'declared_options':d['options'],'matching_indexes':candidates,'status':'PASS' if candidates else 'FAIL'})
result={'timestamp_Asia_Kolkata':datetime.now(ZoneInfo('Asia/Kolkata')).isoformat(),
        'status':'PASS' if all(x['status']=='PASS' for x in matches) else 'FAIL',
        'scope':'Current read-only metadata,not record integrity/transaction/provider/production acceptance.',
        'target':'mongodb://127.0.0.1:27018/?replicaSet=rs0','database':'comein_disposable_test_onboarding',
        'hello':{k:hello.get(k) for k in ('isWritablePrimary','setName','hosts','primary','me','maxWireVersion','logicalSessionTimeoutMinutes')},
        'MongoDB_version':client.admin.command('buildInfo')['version'],
        'collections':rows,'index_declaration_comparisons':matches,
        'counts':{'collections':len(rows),'indexes':sum(len(x['indexes']) for x in rows),'declared_indexes':len(matches),'matched_declarations':sum(bool(x['matching_indexes']) for x in matches),'nonempty_validators':sum(bool(x['validator_value']) for x in rows)},
        'commands':['hello','buildInfo','listCollections','listIndexes'],'record_reads':0,'data_writes':0,
        'history_limitation':'Current capture time/raw relevant options are now explicit. This cannot establish missing historical capture time or production configuration.',
        'tooling_note':'First health probe with /workspace/come-in-tools/venv/bin/python failed ModuleNotFoundError:pymongo;existing py311 environment used without installation.'}
(out/'db-metadata-current.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
client.close()
print(json.dumps({'status':result['status'],'replica_set':result['hello']['setName'],'is_primary':result['hello']['isWritablePrimary'],'MongoDB_version':result['MongoDB_version'],'counts':result['counts'],'record_reads':0,'data_writes':0}))
