"""Actual source handlers with local in-memory DB/HTTP transport doubles only.

No server import,.env,credentials,real provider requests,DB/network or native tools.
The parent runs the full local ASGI/Mongo regressions after applying reviewed code.
"""
import argparse
import ast
import asyncio
from collections import Counter
from datetime import datetime,timezone
import copy
import hashlib
import hmac
import json
import logging
from pathlib import Path
import re
import socket
import sys
import threading
import time
from types import SimpleNamespace
from unittest.mock import patch
import xml.etree.ElementTree as ET

from bson import ObjectId
from fastapi import Depends,HTTPException,Request
import requests

OUT=Path(__file__).resolve().parent
BACKEND=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
sys.path.insert(0,str(BACKEND))
from payment_webhook import event_payload as actual_event_payload
from refund_rules import amount_to_paise,summarize_provider_refunds,grocery_refund_amount

SELECT={'create_restaurant_payment_intent','verify_restaurant_payment','admin_refund_restaurant_order',
        'admin_refund_grocery_order','create_grocery_payment_intent','verify_grocery_payment',
        'razorpay_webhook','_fetch_razorpay_refunds','_grocery_online_order','_claim_payment_intent'}
CASES=[]
def require(value,msg):
 if not value:raise AssertionError(msg)
def case(i,name):
 def register(fn):CASES.append((i,name,fn));return fn
 return register
async def outcome(awaitable):
 try:return await awaitable,None
 except BaseException as exc:return None,exc
def matches(doc,query):
 for key,value in query.items():
  if isinstance(value,dict):
   if '$exists' in value and (key in doc)!=value['$exists']:return False
   if '$in' in value and doc.get(key) not in value['$in']:return False
  elif doc.get(key)!=value:return False
 return True
class Collection:
 def __init__(self,docs=()):self.docs=[copy.deepcopy(x) for x in docs];self.reads=0;self.writes=0
 async def find_one(self,query,**kwargs):
  self.reads+=1
  return next((copy.deepcopy(x) for x in self.docs if matches(x,query)),None)
 async def update_one(self,query,update,**kwargs):
  self.writes+=1
  for d in self.docs:
   if matches(d,query):
    d.update(copy.deepcopy(update.get('$set',{})))
    return SimpleNamespace(modified_count=1,matched_count=1)
  return SimpleNamespace(modified_count=0,matched_count=0)
 async def insert_one(self,doc,**kwargs):
  self.writes+=1;d=copy.deepcopy(doc);d.setdefault('_id',ObjectId());self.docs.append(d)
  return SimpleNamespace(inserted_id=d['_id'])
class FakeResponse:
 def __init__(self,payload,status=200):self.payload=payload;self.status_code=status
 def json(self):return copy.deepcopy(self.payload)

class Harness:
 def __init__(self,code,kind='restaurant',purpose='create'):
  self.kind=kind;self.purpose=purpose;self.oid=ObjectId();self.pid=ObjectId();self.actor={'id':str(ObjectId()),'role':'customer'}
  self.order={'_id':self.oid,'customer_id':self.actor['id'],'payment_method':'razorpay' if kind=='restaurant' else 'online_razorpay',
              'payment_status':'pending' if kind=='restaurant' else 'razorpay_pending','status':'pending_payment','total':100.0,'ref':'fixture-ref'}
  self.payment={'_id':self.pid,'order_id':str(self.oid),'customer_id':self.actor['id'],'gateway':'razorpay','status':'created',
                'gateway_order_id':'order_fixture','gateway_payment_id':'pay_fixture','amount':100.0,'currency':'INR'}
  if purpose=='refund':
   self.order.update(payment_status='paid',status='cancelled');self.payment['status']='paid';self.actor['role']='admin'
  self.orders=Collection([self.order]);self.payments=Collection([] if purpose=='create' else [self.payment]);self.events=Collection()
  self.db=SimpleNamespace(restaurant_orders=self.orders,orders=self.orders,restaurant_payments=self.payments,
                          grocery_payments=self.payments,restaurant_payment_events=self.events)
  self.calls=[];self.delay=0;self.error=None;self.call_started=threading.Event();self.call_finished=threading.Event();self.settings_missing=False
  self.settings=SimpleNamespace(key_id='mock-public-id',key_secret='mock-private-fixture',webhook_secret='mock-webhook-fixture',mode='test')
  self.secret=self.settings.webhook_secret;self.hmac_calls=0;self.payload_calls=0
  def config(*args,**kwargs):
   if self.settings_missing:raise HTTPException(503,'Payment webhook is not configured')
   return self.settings
  def object_id(value,what):return ObjectId(value)
  async def tx(_client,callback):return await callback(None)
  async def mark_paid(order_oid,payment,payment_id,*args):
   await self.orders.update_one({'_id':order_oid},{'$set':{'payment_status':'paid','status':'placed'}})
   await self.payments.update_one({'_id':payment['_id']},{'$set':{'status':'paid','gateway_payment_id':payment_id}})
   return await self.orders.find_one({'_id':order_oid})
  async def restaurant_capture(order_oid,payment,payment_id,*args):return await mark_paid(order_oid,payment,payment_id)
  async def refund_claim(order_oid,payment_oid,blocked):
   for c,oid in [(self.orders,order_oid),(self.payments,payment_oid)]:
    row=await c.find_one({'_id':oid})
    if row.get('refund_status') in blocked:raise HTTPException(409,'Refund already pending')
    await c.update_one({'_id':oid},{'$set':{'refund_status':'refund_requested'}})
  async def review(payment_oid,order_oid,state,*args,**kwargs):
   await self.orders.update_one({'_id':order_oid},{'$set':{'refund_status':state}})
   await self.payments.update_one({'_id':payment_oid},{'$set':{'refund_status':state}})
  async def refund_apply(payment_oid,order_oid,*args):
   await review(payment_oid,order_oid,'refunded');return {'status':'refunded','refund_status':'refunded'}
  async def record_event(event_id,event,body_hash,mode,**kwargs):
   await self.events.insert_one({'event_id':event_id,'payload_sha256':body_hash,'event':event,**kwargs})
  def payload(raw,event_id):self.payload_calls+=1;return actual_event_payload(raw,event_id)
  self.ns={'__name__':'isolated_payment_handlers','asyncio':asyncio,'ObjectId':ObjectId,'Depends':Depends,'HTTPException':HTTPException,'Request':Request,
           'dict':dict,'Optional':__import__('typing').Optional,'PaymentVerifyIn':SimpleNamespace,'GroceryRefundIn':SimpleNamespace,
           'get_current_user':lambda:None,'require_role':lambda *r:lambda:None,'db':self.db,'client':object(),
           'now_utc':lambda:datetime.now(timezone.utc),'_object_id_or_404':object_id,'_razorpay_settings':config,
           '_grocery_razorpay_keys':lambda:(self.settings.key_id,self.settings.key_secret),'requests':requests,
           'hmac':SimpleNamespace(new=self.hmac_new,compare_digest=hmac.compare_digest),'hashlib':hashlib,'re':re,'logger':logging.getLogger('isolated-payment'),
           'amount_to_paise':amount_to_paise,'summarize_provider_refunds':summarize_provider_refunds,'grocery_refund_amount':grocery_refund_amount,
           'doc_out':lambda d:{k:v for k,v in d.items() if k!='_id'},'run_transaction':tx,'event_payload':payload,
           '_mark_grocery_paid':mark_paid,'_commit_restaurant_capture':restaurant_capture,
           '_claim_restaurant_refund_for_gateway':refund_claim,'_persist_restaurant_admin_refund_state':review,
           '_apply_restaurant_refund_webhook_transactionally':refund_apply,'_apply_grocery_refund_transactionally':refund_apply,'_grocery_refund_review':review,
           '_cancel_grocery_order':lambda *args:None}
  exec(code,self.ns)
 def hmac_new(self,*args,**kwargs):self.hmac_calls+=1;return hmac.new(*args,**kwargs)
 def provider(self,method,url,**kwargs):
  self.calls.append({'method':method,'thread':threading.get_ident(),'timeout':kwargs.get('timeout'),'url_kind':'refund-history' if url.endswith('/refunds') else 'refund' if url.endswith('/refund') else 'order' if url.endswith('/orders') else 'payment'})
  self.call_started.set()
  if self.delay:time.sleep(self.delay)
  self.call_finished.set()
  if self.error:raise self.error
  if url.endswith('/refunds'):return FakeResponse({'items':[]})
  if url.endswith('/refund'):return FakeResponse({'id':'rf_fixture','payment_id':'pay_fixture','amount':10000,'status':'processed'})
  if url.endswith('/orders'):return FakeResponse({'id':'order_fixture','amount':10000,'currency':'INR'})
  return FakeResponse({'id':'pay_fixture','order_id':'order_fixture','status':'captured','currency':'INR','amount':10000})
 def patches(self):
  return patch.multiple(requests,get=lambda url,**kw:self.provider('GET',url,**kw),post=lambda url,**kw:self.provider('POST',url,**kw))
 async def invoke(self):
  if self.purpose=='create':return await self.ns['create_'+self.kind+'_payment_intent'](str(self.oid),self.actor)
  if self.purpose=='verify':
   msg=b'order_fixture|pay_fixture';signature=hmac.new(self.settings.key_secret.encode(),msg,hashlib.sha256).hexdigest()
   body=SimpleNamespace(order_id=str(self.oid),razorpay_order_id='order_fixture',razorpay_payment_id='pay_fixture',razorpay_signature=signature)
   return await self.ns['verify_'+self.kind+'_payment'](body,self.actor)
  if self.kind=='restaurant':return await self.ns['admin_refund_restaurant_order'](str(self.oid),self.actor)
  return await self.ns['admin_refund_grocery_order'](str(self.oid),SimpleNamespace(amount_paise=None,request_id='request_fixture',reason='fixture refund'),self.actor)

for KIND in ('restaurant','grocery'):
 for PURPOSE in ('create','verify','refund'):
  def latency_case(kind=KIND,purpose=PURPOSE):
   async def execute(code,o):
    h=Harness(code,kind,purpose);h.delay=.15;main_thread=threading.get_ident();tick={'ran_while_provider_pending':False}
    async def ticker():
     await asyncio.sleep(.01);tick['ran_while_provider_pending']=h.call_started.is_set() and not h.call_finished.is_set()
    with h.patches():
     await asyncio.gather(h.invoke(),ticker())
    o.update({'calls':len(h.calls),'event_loop_progressed':tick['ran_while_provider_pending'],'all_provider_calls_off_main_thread':all(x['thread']!=main_thread for x in h.calls),'timeouts_preserved':all(x['timeout']==15 for x in h.calls)})
    require(tick['ran_while_provider_pending'] and all(x['thread']!=main_thread for x in h.calls),'Blocking provider I/O occupied the event loop')
    require(all(x['timeout']==15 for x in h.calls),'Existing provider timeout changed')
   return execute
  case('S7-'+KIND+'-'+PURPOSE+'-nonblocking','All '+KIND+' '+PURPOSE+' provider calls run off the event loop')(latency_case())

for KIND in ('restaurant','grocery'):
 for PURPOSE in ('create','verify','refund'):
  def successful_case(kind=KIND,purpose=PURPOSE):
   async def execute(code,o):
    h=Harness(code,kind,purpose)
    with h.patches():result=await h.invoke()
    row=await h.orders.find_one({'_id':h.oid})
    if purpose=='create':require(result['gateway_order_id']=='order_fixture' and row['payment_status'] in ('pending','razorpay_pending'),'Creation falsely confirmed payment or lost original gateway order')
    elif purpose=='verify':require(result['verified'] is True and row['payment_status']=='paid','Verified payment behavior changed')
    else:require(row['refund_status']=='refunded','Acknowledged refund failed to reach existing state handler')
    o['provider_mock_calls']=len(h.calls)
   return execute
  case('S7-'+KIND+'-'+PURPOSE+'-success','Existing '+KIND+' '+PURPOSE+' response/state contract with local provider mock')(successful_case())

for KIND in ('restaurant','grocery'):
 for PURPOSE in ('create','verify','refund'):
  def failure_case(kind=KIND,purpose=PURPOSE):
   async def execute(code,o):
    h=Harness(code,kind,purpose);h.error=requests.Timeout('Synthetic provider timeout')
    with h.patches():_,error=await outcome(h.invoke())
    require(isinstance(error,HTTPException) and error.status_code==502,'Provider failure changed existing failure response')
    row=await h.orders.find_one({'_id':h.oid})
    require(row['payment_status']!='paid' if purpose!='refund' else row['refund_status']=='refund_reconciliation_required','Provider failure produced false paid/refunded state')
    if purpose=='create':require(row['razorpay_intent_state']=='uncertain','Failed intent did not retain uncertain state')
    o['status']=error.status_code
   return execute
  case('S7-'+KIND+'-'+PURPOSE+'-failure','Existing '+KIND+' '+PURPOSE+' timeout failure remains safe')(failure_case())

@case('S7-cancel','Cancellation releases event loop without confirming payment or replaying provider request')
async def cancellation(code,o):
 h=Harness(code);h.delay=.2
 with h.patches():
  task=asyncio.create_task(h.invoke())
  await asyncio.sleep(.01)
  cancelled_while_running=not task.done();task.cancel()
  _,error=await outcome(task)
  await asyncio.sleep(.23)
  row=await h.orders.find_one({'_id':h.oid})
  _,retry_error=await outcome(h.invoke())
 o.update({'cancelled_while_provider_pending':cancelled_while_running,'provider_calls':len(h.calls),'retry_rejected':isinstance(retry_error,HTTPException) and retry_error.status_code==409})
 require(cancelled_while_running and isinstance(error,asyncio.CancelledError),'Cancellation was blocked behind provider I/O')
 require(row['payment_status']=='pending' and len(h.calls)==1,'Cancelled request confirmed payment or replayed outbound operation')
 require(isinstance(retry_error,HTTPException) and retry_error.status_code==409,'Existing intent claim did not block unsafe retry after cancellation')

@case('S7-ownership','Unrelated customer cannot create another customer payment intent')
async def ownership(code,o):
 h=Harness(code);h.actor={'id':str(ObjectId()),'role':'customer'}
 with h.patches():_,error=await outcome(h.invoke())
 require(isinstance(error,HTTPException) and error.status_code==404 and not h.calls,'Ownership guard bypassed or contacted provider')

@case('S7-refund-role','Non-admin Grocery refund rejected before provider access')
async def refund_role(code,o):
 h=Harness(code,'grocery','refund');h.actor['role']='customer'
 with h.patches():_,error=await outcome(h.invoke())
 require(isinstance(error,HTTPException) and error.status_code==403 and not h.calls,'Refund role guard bypassed')

class BytesRequest:
 def __init__(self,raw,headers=None,chunks=None):
  self.raw=raw;self.headers=headers or {};self.chunks=chunks or [raw];self.body_reads=0;self.stream_reads=0
 async def body(self):self.body_reads+=1;return self.raw
 async def stream(self):
  for chunk in self.chunks:self.stream_reads+=1;yield chunk

def signed_request(h,raw,extra=None,chunks=None):
 signature=hmac.new(h.secret.encode(),raw,hashlib.sha256).hexdigest()
 return BytesRequest(raw,{'X-Razorpay-Signature':signature,'X-Razorpay-Event-Id':'evt_fixture',**(extra or {})},chunks)

@case('S8-declared-oversize','Declared oversize rejected before body,HMAC,JSON or DB work')
async def declared_oversize(code,o):
 h=Harness(code);raw=b'{"event":"unknown"}';request=signed_request(h,raw,{'Content-Length':str(1024*1024+1)})
 _,error=await outcome(h.ns['razorpay_webhook'](request))
 o.update({'HMAC_calls':h.hmac_calls,'body_reads':request.body_reads,'stream_chunks_read':request.stream_reads})
 require(isinstance(error,HTTPException) and error.status_code==413,'Declared oversized body was not rejected413')
 require(h.hmac_calls==h.payload_calls==h.events.reads==h.events.writes==0 and request.body_reads==request.stream_reads==0,'Oversize body reached processing/allocation')

for HEADER in (None,'1'):
 def actual_oversize_case(header=HEADER):
  async def execute(code,o):
   h=Harness(code);chunks=[b'x'*(1024*1024),b'y',b'never-read'];raw=b''.join(chunks)
   request=signed_request(h,raw,{} if header is None else {'Content-Length':header},chunks)
   _,error=await outcome(h.ns['razorpay_webhook'](request))
   o.update({'HMAC_calls':h.hmac_calls,'body_reads':request.body_reads,'stream_chunks_read':request.stream_reads})
   require(isinstance(error,HTTPException) and error.status_code==413,'Actual oversized chunked body was not rejected413')
   require(h.hmac_calls==h.payload_calls==h.events.reads==h.events.writes==0,'Oversized bytes reached HMAC/JSON/DB')
   require(request.stream_reads==2 and request.body_reads==0,'Stream was fully buffered/read beyond first over-limit chunk')
  return execute
 case('S8-stream-oversize-'+('missing' if HEADER is None else 'forged'),'Actual bytes enforce bound despite missing/forged Content-Length')(actual_oversize_case())

@case('S8-exact-limit','Exactly1MiB valid raw JSON keeps its signature and event processing')
async def exact_limit(code,o):
 h=Harness(code);prefix=b'{"event":"unknown","padding":"';suffix=b'"}';raw=prefix+b'x'*(1024*1024-len(prefix)-len(suffix))+suffix
 request=signed_request(h,raw,{'Content-Length':str(len(raw))},[raw[:31],raw[31:]])
 result,error=await outcome(h.ns['razorpay_webhook'](request))
 require(error is None and result=={'received':True} and h.events.writes==1,'Valid boundary raw bytes/signature contract changed')
 require(h.hmac_calls==h.payload_calls==1,'Valid payload was not verified exactly once')

@case('S8-invalid-signature','Invalid signature rejected without JSON or DB effects')
async def invalid_signature(code,o):
 h=Harness(code);request=signed_request(h,b'{"event":"unknown"}');request.headers['X-Razorpay-Signature']='invalid-fixture'
 _,error=await outcome(h.ns['razorpay_webhook'](request))
 require(isinstance(error,HTTPException) and error.status_code==400 and h.payload_calls==h.events.reads==h.events.writes==0,'Invalid signature caused event effects')

@case('S8-missing-configuration','Existing503 configuration rejection precedes request reads')
async def missing_configuration(code,o):
 h=Harness(code);h.settings_missing=True;request=signed_request(h,b'{"event":"unknown"}')
 _,error=await outcome(h.ns['razorpay_webhook'](request))
 require(isinstance(error,HTTPException) and error.status_code==503 and request.body_reads==request.stream_reads==h.hmac_calls==0,'Missing configuration consumed/verified body')

@case('S8-malformed-json','Signed malformed JSON remains rejected400 without DB writes')
async def malformed_json(code,o):
 h=Harness(code);_,error=await outcome(h.ns['razorpay_webhook'](signed_request(h,b'{bad-json')))
 require(isinstance(error,HTTPException) and error.status_code==400 and h.events.writes==0,'Malformed envelope accepted')

@case('S8-duplicate','Valid duplicate event remains idempotent without a second audit write')
async def duplicate(code,o):
 h=Harness(code);raw=b'{"event":"unknown"}'
 first,error=await outcome(h.ns['razorpay_webhook'](signed_request(h,raw)))
 second,error2=await outcome(h.ns['razorpay_webhook'](signed_request(h,raw)))
 require(error is error2 is None and first=={'received':True} and second=={'received':True,'duplicate':True},'Duplicate event response changed')
 require(h.events.writes==1,'Duplicate event caused repeated audit write')

@case('S8-body-size-before-signature','Oversized invalid-signature input is size-rejected before HMAC')
async def size_before_signature(code,o):
 h=Harness(code);raw=b'x'*(1024*1024+1);request=BytesRequest(raw,{'X-Razorpay-Signature':'wrong','X-Razorpay-Event-Id':'evt_fixture'})
 _,error=await outcome(h.ns['razorpay_webhook'](request))
 require(isinstance(error,HTTPException) and error.status_code==413 and h.hmac_calls==0,'Unauthenticated oversized payload reached HMAC')

async def main(args):
 started=datetime.now(timezone.utc).isoformat();source=args.source.resolve();raw=source.read_bytes();tree=ast.parse(raw)
 nodes=[]
 for node in tree.body:
  if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name in SELECT:
   n=copy.deepcopy(node);n.decorator_list=[];nodes.append(n)
 require({n.name for n in nodes}==SELECT,'Missing actual source handler/helper')
 code=compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),str(source),'exec',dont_inherit=True)
 original_connect=socket.socket.connect
 def deny(*args,**kwargs):raise AssertionError('External/provider/network access forbidden in local mock suite')
 socket.socket.connect=deny
 results=[];root=ET.Element('testsuite',name='SEC07_SEC08_'+args.stage,tests=str(len(CASES)),timestamp=started)
 try:
  for identifier,invariant,fn in CASES:
   began=time.monotonic();o={};status='PASS';failure=None
   try:await asyncio.wait_for(fn(code,o),timeout=5)
   except AssertionError as exc:status='FAIL';failure=str(exc)
   except BaseException as exc:status='ERROR';failure=type(exc).__name__
   results.append({'id':identifier,'invariant':invariant,'status':status,'failure':failure,'observations':o})
   t=ET.SubElement(root,'testcase',classname='payment_security_local',name=identifier,time=str(time.monotonic()-began))
   if status!='PASS':ET.SubElement(t,'failure' if status=='FAIL' else 'error',message=failure or status)
   print(identifier,status,failure or '',flush=True)
 finally:socket.socket.connect=original_connect
 counts={k:sum(x['status']==k for x in results) for k in ('PASS','FAIL','ERROR')};counts['SKIPPED']=0
 root.set('failures',str(counts['FAIL']));root.set('errors',str(counts['ERROR']));root.set('skipped','0')
 data={'project':'COME-IN','stage':args.stage,'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),
       'source_path':str(source),'source_SHA256':hashlib.sha256(raw).hexdigest(),'source_SHA256_after':hashlib.sha256(source.read_bytes()).hexdigest(),
       'runner_SHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'command':[sys.executable,'-B',str(Path(__file__).resolve()),'--stage',args.stage,'--source',str(source)],
       'counts':counts,'cases':results,'actual_provider_calls':0,'database_calls':0,'native_validation':False,
       'scope':'Actual handler/helper AST bodies;in-memory DB/state/provider mocks,network denied. No HTTP middleware/dependency-injection/realMongo/provider settlement proof.',
       'limitations':['Thread cancellation does not stop the blocking mock;existing operation claim prevents unsafe replay and payment remains unconfirmed.','Production ingress body caps are not tested.','Real Razorpay/Android/iOS validation is explicitly DEFERRED.']}
 (OUT/(args.stage+'-results.json')).write_text(json.dumps(data,indent=2)+'\n');ET.ElementTree(root).write(OUT/(args.stage+'.xml'),encoding='utf-8',xml_declaration=True)
 print(json.dumps({'stage':args.stage,'counts':counts}),flush=True)
 return 1 if counts['FAIL'] or counts['ERROR'] else 0

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--stage',required=True);parser.add_argument('--source',type=Path,required=True)
 raise SystemExit(asyncio.run(main(parser.parse_args())))
