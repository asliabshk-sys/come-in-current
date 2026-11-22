"""Execute unchanged application callbacks against real local Motor transactions.
Synthetic rows only; no Razorpay calls, signature or provider-delivery claim.
"""
import asyncio,sys,json
from pathlib import Path
from bson import ObjectId
from fastapi import HTTPException
ROOT=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
sys.path[:0]=[str(ROOT/'backend'),str(ROOT)]
import server
from scripts.mongo.comein_mongo import init_db
from pymongo import MongoClient
name='comein_disposable_test_financial_20261117_final'
sync=MongoClient('mongodb://127.0.0.1:27018/?replicaSet=rs0')
assert name not in sync.list_database_names(), 'Existing acceptance DB must be preserved; choose a new name.'
init_db(sync[name])
server.db=server.client[name]
results=[]
async def seed():
 oid,pid=ObjectId(),ObjectId()
 await server.db.restaurant_orders.insert_one({'_id':oid,'customer_id':'synthetic-customer','idempotency_key':str(oid),'total':120.0,'status':'delivered','payment_status':'paid','refund_status':'refund_requested'})
 await server.db.restaurant_payments.insert_one({'_id':pid,'order_id':str(oid),'status':'paid','gateway_payment_id':'pay_synthetic_'+str(pid),'refund_status':'refund_requested'})
 await server.db.financial_ledger.insert_one({'idempotency_key':f'order:restaurant:{oid}:finalized:v1','platform_earnings':12,'gross_merchandise':120})
 return oid,pid
async def main():
 oid,pid=await seed()
 f=server._apply_restaurant_refund_webhook_transactionally
 a,b=await asyncio.gather(f(pid,oid,'rf_synthetic',12000,'processed'),f(pid,oid,'rf_synthetic',12000,'processed'))
 assert a['status']==b['status']=='refunded'
 assert await server.db.financial_ledger.count_documents({'event_type':'refund_reversal','order_id':str(oid)})==1
 assert len((await server.db.restaurant_payments.find_one({'_id':pid}))['provider_refunds'])==1
 results.append('concurrent refund replay commits one reversal and one refund entry')
 assert (await f(pid,oid,'rf_synthetic',12000,'failed'))['status']=='refunded'
 results.append('late failed webhook cannot downgrade processed refund')
 try: await server._persist_restaurant_admin_refund_state(pid,oid,'refund_uncertain')
 except HTTPException as exc: assert exc.status_code==409
 else: raise AssertionError('Admin downgraded completed refund')
 results.append('admin state cannot downgrade completed webhook state')
 oid,pid=await seed()
 # Reject only this synthetic order update, without changing other rows.
 await server.db.command({'collMod':'restaurant_orders','validator':{'$or':[{'_id':{'$ne':oid}},{'refund_status':{'$ne':'refunded'}}]},'validationLevel':'strict','validationAction':'error'})
 try: await f(pid,oid,'rf_reject',12000,'processed')
 except HTTPException as exc: assert exc.status_code==503
 else: raise AssertionError('Second write failure was not surfaced')
 p=await server.db.restaurant_payments.find_one({'_id':pid}); o=await server.db.restaurant_orders.find_one({'_id':oid})
 assert p['refund_status']==o['refund_status']=='refund_requested' and 'provider_refunds' not in p
 assert await server.db.financial_ledger.count_documents({'event_type':'refund_reversal','order_id':str(oid)})==0
 results.append('real validator failure rolls back refund payment/order/ledger writes')
 # Capture helpers use the same real driver/session implementation, no external gateway.
 oid,pid=ObjectId(),ObjectId()
 await server.db.restaurant_orders.insert_one({'_id':oid,'customer_id':'synthetic-customer','idempotency_key':str(oid),'total':225.5,'status':'pending_payment','payment_status':'pending','status_history':[]})
 await server.db.restaurant_payments.insert_one({'_id':pid,'order_id':str(oid),'amount':225.5,'status':'created'})
 await server._commit_restaurant_capture(oid,{'_id':pid},'pay_synthetic_capture','synthetic verified DB acceptance')
 await server._commit_restaurant_capture(oid,{'_id':pid},'pay_synthetic_capture','synthetic replay')
 assert (await server.db.restaurant_payments.find_one({'_id':pid}))['status']=='paid'
 assert (await server.db.restaurant_orders.find_one({'_id':oid}))['payment_status']=='paid'
 results.append('Restaurant capture and repeat are atomic and durable')
 server.client.close()
asyncio.run(main())
Path(__file__).with_suffix('.json').write_text(json.dumps({'ok':True,'checks':results,'scope':'DB callbacks only; no provider webhook signatures, external refunds, fault-injected commit uncertainty'},indent=2))
print(json.dumps({'ok':True,'checks':results}))
