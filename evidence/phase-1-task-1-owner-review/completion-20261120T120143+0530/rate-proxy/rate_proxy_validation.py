"""Actual source client-IP and auth-counter validation on a unique local DB.

No server import,.env,provider,production data or real credentials. Candidate
and before-source run the same assertions. Login crypto/token creation are
explicit doubles; counter transactions use actual Motor/PyMongo and helper.
"""
import argparse
import ast
import asyncio
import copy
from datetime import datetime,timedelta,timezone
import hashlib
import ipaddress
import json
from pathlib import Path
import socket
import sys
import time
from types import SimpleNamespace
import uuid
import xml.etree.ElementTree as ET

from bson import ObjectId
from fastapi import HTTPException,Request
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel,EmailStr,Field
from pymongo.errors import DuplicateKeyError

BACKEND=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
sys.path.insert(0,str(BACKEND))
from mongo_transactions import run_transaction

OUT=Path(__file__).resolve().parent
CASES=[]
def case(i,desc):
 def add(fn):CASES.append((i,desc,fn));return fn
 return add
def require(ok,msg):
 if not ok:raise AssertionError(msg)
async def attempt(coro):
 try:return await coro,None
 except Exception as e:return None,e
def denied(error):return isinstance(error,HTTPException) and error.status_code==429
def request(peer='192.0.2.10',forwarded=''):
 headers=[(b'x-forwarded-for',forwarded.encode())] if forwarded else []
 return Request({'type':'http','method':'POST','path':'/auth/login','headers':headers,
  'client':(peer,12345),'server':('127.0.0.1',0),'scheme':'http','query_string':b''})

class ProxyCollection:
 def __init__(self,actual,h):self.actual=actual;self.h=h
 def __getattr__(self,n):return getattr(self.actual,n)
 async def find_one(self,q,*a,**kw):
  row=await self.actual.find_one(q,*a,**kw)
  if self.h.barrier and ':sub:' in q.get('_id',''):
   self.h.readers+=1
   if self.h.readers>=2:self.h.open.set()
   await asyncio.wait_for(self.h.open.wait(),10)
  return row
 async def update_one(self,q,u,*a,**kw):
  if self.h.fail_subject and ':sub:' in q.get('_id','') and u.get('$inc',{}).get('count')==1:
   self.h.fail_subject=False
   raise RuntimeError('Synthetic subject-write boundary failure')
  return await self.actual.update_one(q,u,*a,**kw)

class UsersProxy:
 def __init__(self,actual,h):self.actual=actual;self.h=h
 def __getattr__(self,n):return getattr(self.actual,n)
 async def find_one(self,*a,**kw):
  value=await self.actual.find_one(*a,**kw)
  if self.h.advance_after_lookup:
   self.h.advance_after_lookup=False
   self.h.clock+=timedelta(seconds=900)
  return value

class Harness:
 def __init__(self,client,db,code,num,runid):
  self.client=client;self.actual=db;self.num=num;self.runid=runid
  self.clock=datetime(2026,11,20,1,0,1,tzinfo=timezone.utc)
  self.env={};self.barrier=False;self.readers=0;self.open=asyncio.Event()
  self.fail_subject=False;self.advance_after_lookup=False
  self.ns={'__name__':'source_auth_rate_isolation','datetime':datetime,'timedelta':timedelta,'timezone':timezone,
   'hashlib':hashlib,'ipaddress':ipaddress,'os':SimpleNamespace(environ=self.env),'Request':Request,
   'HTTPException':HTTPException,'DuplicateKeyError':DuplicateKeyError,'BaseModel':BaseModel,'EmailStr':EmailStr,'Field':Field,
   'run_transaction':run_transaction,'client':client,'create_access_token':lambda *args,**kwargs:'synthetic-token-sentinel',
   'verify_password':lambda plain,stored:plain=='valid-fixture-password' and stored=='synthetic-checker-marker'}
  exec(code,self.ns)
  self.ns['now_utc']=lambda:self.clock
  self.ns['db']=SimpleNamespace(auth_rate_limits=ProxyCollection(db.auth_rate_limits,self),users=UsersProxy(db.users,self))
  self.peer=f'192.0.2.{num}'
  self.email=f'fixture-{num}-{runid}@example.com'
 def req(self,**kw):return request(kw.get('peer',self.peer),kw.get('forwarded',''))
 def keys(self,action='forgot',subject=None):return self.ns['_rate_keys'](action,self.req(),self.email if subject is None else subject)
 async def seed_counter(self,key,count):await self.actual.auth_rate_limits.insert_one({'_id':key,'count':count,'expires_at':self.clock+timedelta(hours=1)})
 async def counts(self,keys):
  rows=[await self.actual.auth_rate_limits.find_one({'_id':key}) for key in keys]
  return [r.get('count',0) if r else 0 for r in rows]
 async def enforce(self,action='forgot',subject=None):return await self.ns['_enforce_auth_rate_limit'](action,self.req(),self.email if subject is None else subject)
 async def seed_user(self):
  await self.actual.users.insert_one({'_id':ObjectId(),'email':self.email,'password_hash':'synthetic-checker-marker','role':'customer'})
 async def login(self,valid=True):
  return await self.ns['login'](self.ns['LoginIn'](email=self.email,password='valid-fixture-password' if valid else 'wrong-fixture-password'),self.req())

IP_CASES=[
 ('IP01','Default ignores caller-supplied forwarded address','', '192.0.2.10','198.51.100.10','192.0.2.10'),
 ('IP02','Untrusted connected peer cannot spoof even with a configured proxy','127.0.0.1/32','192.0.2.10','198.51.100.10','192.0.2.10'),
 ('IP03','Owned direct proxy forwards a single valid client','127.0.0.1/32','127.0.0.1','198.51.100.10','198.51.100.10'),
 ('IP04','First untrusted hop stops spoofed leftmost address','127.0.0.1/32','127.0.0.1','203.0.113.99, 198.51.100.10','198.51.100.10'),
 ('IP05','Multiple explicitly trusted proxy hops resolve client','127.0.0.1/32,10.0.0.0/24','127.0.0.1','198.51.100.10, 10.0.0.7','198.51.100.10'),
 ('IP06','Malformed proxy configuration fails closed','not-a-network','127.0.0.1','198.51.100.10','127.0.0.1'),
 ('IP07','Universal IPv4 trust is rejected','0.0.0.0/0','127.0.0.1','198.51.100.10','127.0.0.1'),
 ('IP08','Universal IPv6 trust is rejected','::/0','::1','2001:db8::7','::1'),
 ('IP09','Invalid forwarded IP falls back to connected peer','127.0.0.1/32','127.0.0.1','malformed-client','127.0.0.1'),
 ('IP10','Invalid chain member rejects the entire chain','127.0.0.1/32','127.0.0.1','198.51.100.10, invalid','127.0.0.1'),
 ('IP11','IPv6 trusted proxy/client chain works','::1/128','::1','2001:db8::7','2001:db8::7'),
 ('IP12','No forwarding header preserves socket peer','127.0.0.1/32','127.0.0.1','','127.0.0.1'),
 ('IP13','Overlong forwarding header fails closed','127.0.0.1/32','127.0.0.1','198.51.100.10,'*180+'198.51.100.11','127.0.0.1'),
 ('IP14','No valid proxy match preserves peer','10.0.0.1/32','127.0.0.1','198.51.100.10','127.0.0.1'),
]
for identifier,desc,config,peer,forwarded,wanted in IP_CASES:
 async def check(h,o,config=config,peer=peer,forwarded=forwarded,wanted=wanted):
  h.env['TRUSTED_PROXY_CIDRS']=config
  actual=h.ns['_client_ip'](h.req(peer=peer,forwarded=forwarded))
  require(actual==wanted,'Trusted-proxy client identity mismatch')
  o['identity_matches_expected_boundary']=True
 case(identifier,desc)(check)

@case('RATE01','Forgot serial subject boundary rejects sixth without incrementing either counter')
async def serial_forgot(h,o):
 for _ in range(5):await h.enforce()
 _,error=await attempt(h.enforce());keys=[k for k,f in h.keys()]
 require(denied(error) and await h.counts(keys)==[5,5],'Serial subject cap or rejected-attempt count is wrong')
 rows=[await h.actual.auth_rate_limits.find_one({'_id':k}) for k in keys]
 require(all(h.email not in r['_id'] and 'expires_at' in r for r in rows),'Counter exposes email or omits expiry')

@case('RATE02','Reset IP boundary remains50attempts per configured window')
async def serial_reset(h,o):
 key=h.keys('reset','')[0][0];await h.seed_counter(key,49)
 await h.enforce('reset','');_,error=await attempt(h.enforce('reset',''))
 require(denied(error) and await h.counts([key])==[50],'Reset IP boundary changed or overshot')

@case('RATE03','Two near-cap concurrent requests admit exactly one')
async def near_cap(h,o):
 keys=h.keys();
 for key,factor in keys:await h.seed_counter(key,4 if factor==1 else 0)
 h.barrier=True
 outcomes=await asyncio.gather(*(attempt(h.enforce()) for _ in range(2)))
 allowed=sum(e is None for _,e in outcomes);rejected=sum(denied(e) for _,e in outcomes)
 counts=await h.counts([k for k,f in keys]);o.update(allowed=allowed,rejected429=rejected,counts=counts)
 require(allowed==1 and rejected==1 and counts==[1,5],'Concurrent check/record overshoots or partially charges rejected request')

@case('RATE04','Twenty first-bucket concurrent requests admit only five for one subject')
async def new_bucket(h,o):
 outcomes=await asyncio.gather(*(attempt(h.enforce()) for _ in range(20)))
 allowed=sum(e is None for _,e in outcomes);rejected=sum(denied(e) for _,e in outcomes)
 counts=await h.counts([k for k,f in h.keys()]);o.update(allowed=allowed,rejected429=rejected,counts=counts)
 require(allowed==5 and rejected==15 and counts==[5,5],'New bucket allocation or atomic subject capacity failed')

@case('RATE05','Forty different subjects sharing an IP admit only its25forgot slots')
async def shared_ip(h,o):
 outcomes=await asyncio.gather(*(attempt(h.enforce(subject=f'other-{n}-{h.runid}@example.com')) for n in range(40)))
 allowed=sum(e is None for _,e in outcomes);rejected=sum(denied(e) for _,e in outcomes)
 ipkey=h.keys()[0][0];o.update(allowed=allowed,rejected429=rejected)
 require(allowed==25 and rejected==15 and await h.counts([ipkey])==[25],'Shared-IP cap overshot or legitimate configured slots were lost')

@case('RATE06','Subject rejection rolls back an earlier IP increment')
async def subject_reject(h,o):
 keys=h.keys()
 for key,f in keys:await h.seed_counter(key,5 if f==1 else 3)
 _,error=await attempt(h.enforce());counts=await h.counts([k for k,f in keys])
 require(denied(error) and counts==[3,5],'Rejected subject charged IP or mutated full subject')

@case('RATE07','IP rejection does not charge a separate subject')
async def ip_reject(h,o):
 keys=h.keys()
 for key,f in keys:await h.seed_counter(key,0 if f==1 else 25)
 _,error=await attempt(h.enforce());require(denied(error) and await h.counts([k for k,f in keys])==[25,0],'Rejected IP charged subject')

@case('RATE08','Second-key failure leaves both counters unchanged and clean retry succeeds')
async def atomic_failure(h,o):
 keys=h.keys()
 for key,f in keys:await h.seed_counter(key,0)
 h.fail_subject=True;_,error=await attempt(h.enforce())
 require(isinstance(error,RuntimeError),'Fault did not reach the actual subject update')
 require(await h.counts([k for k,f in keys])==[0,0],'Partial counter update committed after second-key failure')
 await h.enforce();require(await h.counts([k for k,f in keys])==[1,1],'Retry did not reserve exactly one shared slot')

@case('LOGIN01','Twenty legitimate successes do not consume failed-login budgets')
async def success_release(h,o):
 await h.seed_user()
 for _ in range(20):
  result=await h.login();require(result['token']=='synthetic-token-sentinel','Successful login response failed')
 require(await h.counts([k for k,f in h.keys('login')])==[0,0],'Successful authentication consumed failed-attempt slots')

@case('LOGIN02','Ten failed logins count and the next is429')
async def failures_count(h,o):
 await h.seed_user()
 for _ in range(10):
  _,error=await attempt(h.login(False));require(isinstance(error,HTTPException) and error.status_code==401,'Failed login should be401within budget')
 _,error=await attempt(h.login(False));require(denied(error),'Eleventh failed login escaped cap')
 require(await h.counts([k for k,f in h.keys('login')])==[10,10],'Failed budget exceeds configured cap')

@case('LOGIN03','Concurrent final failed-login slot admits only one password check')
async def login_race(h,o):
 await h.seed_user();keys=h.keys('login')
 for key,f in keys:await h.seed_counter(key,9 if f==1 else 0)
 h.barrier=True
 outcomes=await asyncio.gather(*(attempt(h.login(False)) for _ in range(2)))
 wrong=sum(isinstance(e,HTTPException) and e.status_code==401 for _,e in outcomes)
 capped=sum(denied(e) for _,e in outcomes);o.update(failed401=wrong,capped429=capped)
 require(wrong==1 and capped==1 and await h.counts([k for k,f in keys])==[1,10],'Concurrent login failures overshot final subject slot')

@case('LOGIN04','Successful login releases original captured bucket even after window rollover')
async def release_old_bucket(h,o):
 await h.seed_user();old=h.keys('login')
 for key,f in old:await h.seed_counter(key,2)
 h.clock+=timedelta(seconds=900);new=h.keys('login')
 for key,f in new:await h.seed_counter(key,3)
 h.clock-=timedelta(seconds=900);h.advance_after_lookup=True
 result=await h.login()
 require(result['token']=='synthetic-token-sentinel','Window rollover broke legitimate login')
 require(await h.counts([k for k,f in old])==[2,2] and await h.counts([k for k,f in new])==[3,3],'Release decremented wrong window or failed to release its old reservation')

async def main(args):
 raw=args.source.read_bytes();before=hashlib.sha256(raw).hexdigest();tree=ast.parse(raw.decode())
 names={'now_utc','doc_out','LoginIn','_client_ip','_rate_keys','_check_auth_rate_limit','_record_auth_attempt','_enforce_auth_rate_limit','_reserve_auth_attempt','_release_auth_attempt','login'}
 constants={'AUTH_RATE_LIMITS','AUTH_IP_MULTIPLIER'};nodes=[]
 for node in tree.body:
  chosen=isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and node.name in names
  if isinstance(node,ast.Assign):chosen=any(isinstance(t,ast.Name) and t.id in constants for t in node.targets)
  if chosen:
   n=copy.deepcopy(node)
   if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):n.decorator_list=[]
   nodes.append(n)
 code=compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),str(args.source),'exec',dont_inherit=True)
 runid=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]
 dbname='comein_rate_proxy_'+args.stage+'_'+runid.lower();started=datetime.now(timezone.utc).isoformat()
 client=AsyncIOMotorClient('mongodb://127.0.0.1:27018/?replicaSet=rs0',serverSelectionTimeoutMS=7000)
 hello=await client.admin.command('hello');require(hello.get('isWritablePrimary') and hello.get('setName')=='rs0','Local PRIMARY is unavailable')
 require(all(x.startswith(('127.0.0.1:','localhost:')) for x in hello.get('hosts',[])),'Nonlocal Mongo host refused')
 db=client[dbname];rows=[];suite=ET.Element('testsuite',name='SEC03-04 '+args.stage,tests=str(len(CASES)),timestamp=started)
 for n,(identifier,desc,fn) in enumerate(CASES,1):
  h=Harness(client,db,code,n,runid);o={};began=time.monotonic();status='PASS';failure=None
  try:await asyncio.wait_for(fn(h,o),timeout=110)
  except AssertionError as e:status='FAIL';failure=str(e)
  except Exception as e:status='ERROR';failure=type(e).__name__
  seconds=time.monotonic()-began;rows.append({'id':identifier,'invariant':desc,'status':status,'failure':failure,'observations':o})
  item=ET.SubElement(suite,'testcase',classname='sec03_sec04.rate_proxy',name=identifier,time=str(seconds))
  if status!='PASS':ET.SubElement(item,'failure' if status=='FAIL' else 'error',message=failure or status).text=desc
  print(identifier,status,failure or '',flush=True)
 counts={k:sum(x['status']==k for x in rows) for k in ['PASS','FAIL','ERROR']};counts['SKIPPED']=0
 suite.set('failures',str(counts['FAIL']));suite.set('errors',str(counts['ERROR']));suite.set('skipped','0')
 result={'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),'stage':args.stage,'source':str(args.source),'source_SHA256':before,'source_SHA256_after':hashlib.sha256(args.source.read_bytes()).hexdigest(),'runner_SHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_SHA256':hashlib.sha256((BACKEND/'mongo_transactions.py').read_bytes()).hexdigest(),'counts':counts,'cases':rows,'database_retained':dbname,'replica_set':'rs0','command':[sys.executable,'-B',str(Path(__file__).resolve()),'--stage',args.stage,'--source',str(args.source)],'scope':'Actual source functions/model AST with real Motor/Mongo and existing unchanged transaction helper. Login password checker/JWT creation are explicit in-memory doubles;noHTTP/router/provider/productionvalidation.','safety':{'protected_source_changes':0,'credentials_or_raw_PII_saved':False,'global_failpoints':0,'DB_drops':0,'external_provider_calls':0,'native_operations':0}}
 (OUT/('rate-proxy-'+args.stage+'.json')).write_text(json.dumps(result,indent=2)+'\n');ET.ElementTree(suite).write(OUT/('rate-proxy-'+args.stage+'.xml'),encoding='utf-8',xml_declaration=True)
 client.close();require(result['source_SHA256_after']==before,'Source changed during test run');print(json.dumps({'counts':counts,'database_retained':dbname}),flush=True)
 return int(bool(counts['FAIL'] or counts['ERROR']))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True);parser.add_argument('--stage',choices=['before','after'],required=True);args=parser.parse_args()
 raise SystemExit(asyncio.run(main(args)))
