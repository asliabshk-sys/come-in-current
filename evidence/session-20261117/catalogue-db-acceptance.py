"""Real MongoDB catalogue import callbacks, synthetic rows; no source replacement."""
import sys,asyncio,json
from pathlib import Path
from bson import ObjectId
from pymongo import MongoClient
from fastapi import HTTPException
root=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
sys.path[:0]=[str(root/'backend'),str(root/'backend/tests'),str(root)]
import server
from test_catalogue_transaction_apply_offline import make_job
from scripts.mongo.comein_mongo import init_db
c=MongoClient('mongodb://127.0.0.1:27018/?replicaSet=rs0'); name='comein_disposable_test_catalogue_20261117'
assert all(c[name][table].count_documents({})==0 for table in ['shops','products','catalogue_import_jobs','catalogue_import_audit']), 'Do not rerun after synthetic rows exist; use a new database.'
init_db(c[name]);server.db=server.client[name]; results=[]
async def main():
 shop=ObjectId(); sid=str(shop); seller=str(ObjectId())
 await server.db.shops.insert_one({'_id':shop,'owner_id':seller,'status':'approved'})
 async def job(key,prefix='SKU'):
  j=make_job(job_id=key,seller=seller,sku_prefix=prefix);j['_id']=ObjectId();j['shop_id']=sid
  await server.db.catalogue_import_jobs.insert_one(j);return j
 await job('job1')
 a,b=await asyncio.gather(*[server._apply_catalogue_import_job_transactionally(sid,'job1',seller) for _ in range(2)])
 assert a['product_ids']==b['product_ids'] and len(a['product_ids'])==2
 assert await server.db.products.count_documents({})==2 and await server.db.catalogue_import_audit.count_documents({})==1
 assert await server.db.products.count_documents({'available':False,'stock':1000})==2
 results.append('concurrent import/replay creates two products and one audit without double stock')
 await job('job2')
 try:await server._apply_catalogue_import_job_transactionally(sid,'job2',seller)
 except HTTPException as e:assert e.status_code==409
 else:raise AssertionError('Duplicate SKU was not refused')
 assert (await server.db.catalogue_import_jobs.find_one({'job_id':'job2'}))['applied'] is False
 assert await server.db.products.count_documents({})==2
 results.append('conflicting SKU rolls back claim and products')
 await job('job3','OTHER')
 await server.db.shops.update_one({'_id':shop},{'$set':{'owner_id':'different-owner'}})
 try:await server._apply_catalogue_import_job_transactionally(sid,'job3',seller)
 except HTTPException as e:assert e.status_code==403
 else:raise AssertionError('Changed owner permitted import')
 assert await server.db.products.count_documents({})==2
 results.append('ownership is rechecked inside real transaction')
 server.client.close()
asyncio.run(main())
Path(__file__).with_suffix('.json').write_text(json.dumps({'ok':True,'checks':results},indent=2))
print(json.dumps({'ok':True,'checks':results}))
