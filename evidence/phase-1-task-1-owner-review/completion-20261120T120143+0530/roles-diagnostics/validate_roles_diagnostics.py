"""Before/after SEC-05/09 tests: actual AST bodies,ASGI DI and real disposable Mongo."""
import argparse,ast,asyncio,copy,hashlib,importlib.metadata,json,socket,sys,time,uuid
from datetime import datetime,timezone
from pathlib import Path
from typing import List,Literal
from types import SimpleNamespace
import xml.etree.ElementTree as ET
from bson import ObjectId
from fastapi import APIRouter,Depends,FastAPI,HTTPException,Request
from httpx import ASGITransport,AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel,Field
from pymongo.errors import DuplicateKeyError

P=Path(__file__).resolve().parent
BACKEND=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
sys.path.insert(0,str(BACKEND))
from mongo_transactions import run_transaction

SELECT={'now_utc','now_iso','doc_out','require_role','root','StatusCheck','StatusCheckCreate',
        'create_status_check','list_status_checks','AdminRoleUpdateIn','admin_update_user_role','_object_id_or_404'}
CASES=[]
def case(i,description):
 def add(f):CASES.append((i,description,f));return f
 return add
def need(v,message):
 if not v:raise AssertionError(message)
async def outcome(awaitable):
 try:return await awaitable,None
 except Exception as e:return None,e

class Users:
 def __init__(self,real,h):self.real=real;self.h=h
 def __getattr__(self,name):return getattr(self.real,name)
 async def count_documents(self,*a,**kw):
  count=await self.real.count_documents(*a,**kw)
  if kw.get('session') is not None:self.h.session_count_reads+=1
  elif self.h.barrier_parties:
   self.h.nontransactional_count_reads+=1
   if self.h.nontransactional_count_reads>=self.h.barrier_parties:self.h.barrier.set()
   await asyncio.wait_for(self.h.barrier.wait(),10)
  return count
 async def update_one(self,*a,**kw):
  result=await self.real.update_one(*a,**kw)
  if self.h.fail_after_role_write:
   self.h.fail_after_role_write=False
   raise RuntimeError('Synthetic post-role-write fault')
  return result

class Client:
 def __init__(self,real,h):self.real=real;self.h=h
 async def start_session(self,*a,**kw):
  if self.h.session_unavailable:raise RuntimeError('Synthetic session unavailable')
  return await self.real.start_session(*a,**kw)

class Harness:
 def __init__(self,real,code,db_name):
  self.real=real;self.actual=real[db_name];self.db_name=db_name
  self.barrier_parties=0;self.barrier=asyncio.Event();self.nontransactional_count_reads=0;self.session_count_reads=0
  self.fail_after_role_write=False;self.session_unavailable=False
  self.ids={role:ObjectId() for role in ['admin','customer','shopkeeper','delivery_partner']}
  async def fixture_auth(request:Request):
   role=request.headers.get('X-Fixture-Role')
   if role not in self.ids:raise HTTPException(status_code=401,detail='Not authenticated')
   return {'id':str(self.ids[role]),'role':role}
  self.api=APIRouter(prefix='/api')
  self.ns={'__name__':'isolated_roles_source','datetime':datetime,'timezone':timezone,'uuid':uuid,'ObjectId':ObjectId,
           'BaseModel':BaseModel,'Field':Field,'List':List,'Literal':Literal,'Depends':Depends,
           'HTTPException':HTTPException,'get_current_user':fixture_auth,'api':self.api,
           'DuplicateKeyError':DuplicateKeyError,'run_transaction':run_transaction,'client':Client(real,self)}
  self.ns['db']=SimpleNamespace(users=Users(self.actual.users,self),status_checks=self.actual.status_checks,
                                 security_locks=self.actual.security_locks)
  exec(code,self.ns)
  self.app=FastAPI();self.app.include_router(self.api)
 async def seed(self):
  await self.actual.users.insert_many([{'_id':oid,'role':role,'password_hash':'synthetic-private-marker','password_reset_token_hash':'synthetic-private-marker'} for role,oid in self.ids.items()])
 async def http(self,method,path,role=None,json_body=None):
  headers={'X-Fixture-Role':role} if role else {}
  async with AsyncClient(transport=ASGITransport(app=self.app,raise_app_exceptions=False),base_url='http://isolated.invalid') as c:
   return await c.request(method,path,headers=headers,json=json_body)
 async def mutate(self,actor,target,role):
  return await self.ns['admin_update_user_role'](str(target),self.ns['AdminRoleUpdateIn'](role=role),{'id':str(actor),'role':'admin'})
 async def admin_cohort(self,n):
  # The initial fixture admin is repurposed;all other fixture users remain nonadmin.
  ids=[self.ids['admin']]+[ObjectId() for _ in range(n-1)]
  if n>1:await self.actual.users.insert_many([{'_id':oid,'role':'admin'} for oid in ids[1:]])
  return ids

@case('D01','Public health remains anonymous/read-only')
async def health(h,o):
 r=await h.http('GET','/api/')
 need(r.status_code==200 and r.json()['status']=='ok','Public health contract changed')
 need(await h.actual.status_checks.count_documents({})==0,'Health wrote a diagnostic record')

async def denied_status(h,o,method,role,expected):
 before=await h.actual.status_checks.count_documents({})
 r=await h.http(method,'/api/status',role,{'client_name':'synthetic diagnostic'} if method=='POST' else None)
 o.update({'actual_status':r.status_code,'expected_status':expected})
 need(r.status_code==expected,'Diagnostic authorization boundary not enforced')
 need(await h.actual.status_checks.count_documents({})==before,'Denied diagnostic request wrote data')

for i,method,role,status in [
 ('D02','POST',None,401),('D03','GET',None,401),
 ('D04','POST','customer',403),('D05','POST','shopkeeper',403),('D06','POST','delivery_partner',403),
 ('D07','GET','customer',403),('D08','GET','shopkeeper',403),('D09','GET','delivery_partner',403)]:
 async def test(h,o,method=method,role=role,status=status):await denied_status(h,o,method,role,status)
 CASES.append((i,f'{method} diagnostics denies {role or "anonymous"} with{status}',test))

@case('D10','Admin can write the existing diagnostic response shape')
async def admin_create(h,o):
 r=await h.http('POST','/api/status','admin',{'client_name':'synthetic diagnostic'})
 need(r.status_code==200,'Admin diagnostic write rejected')
 need(set(r.json())=={'id','client_name','timestamp'} and r.json()['client_name']=='synthetic diagnostic','Diagnostic response shape changed')
 need(await h.actual.status_checks.count_documents({})==1,'Admin write was not persisted')

@case('D11','Admin diagnostic feed preserves legacy stored records and response shape')
async def admin_list(h,o):
 # Existing historical entries may be longer than the new input cap;do not break reads.
 await h.actual.status_checks.insert_one({'id':'synthetic-existing','client_name':'x'*300,'timestamp':datetime.now(timezone.utc)})
 r=await h.http('GET','/api/status','admin')
 need(r.status_code==200 and len(r.json())==1,'Admin diagnostic feed failed')
 need(r.json()[0]['client_name']=='x'*300,'Legacy diagnostic response record was truncated or rejected')

@case('D12','256-character diagnostic name is accepted')
async def boundary_ok(h,o):
 r=await h.http('POST','/api/status','admin',{'client_name':'x'*256})
 need(r.status_code==200,'Diagnostic upper boundary rejected')

@case('D13','257-character diagnostic name is rejected without storage')
async def boundary_long(h,o):
 r=await h.http('POST','/api/status','admin',{'client_name':'x'*257})
 o['actual_status']=r.status_code
 need(r.status_code==422 and await h.actual.status_checks.count_documents({})==0,'Oversized diagnostic name was accepted')

@case('D14','Empty diagnostic name is rejected without storage')
async def boundary_empty(h,o):
 r=await h.http('POST','/api/status','admin',{'client_name':''})
 need(r.status_code==422 and await h.actual.status_checks.count_documents({})==0,'Empty diagnostic name was accepted')

@case('D15','Existing required diagnostic field remains required')
async def boundary_missing(h,o):
 r=await h.http('POST','/api/status','admin',{})
 need(r.status_code==422,'Missing diagnostic field was accepted')

@case('R01','Admin can update a legitimate customer role and response redacts secrets')
async def legitimate(h,o):
 result=await h.mutate(h.ids['admin'],h.ids['customer'],'shopkeeper')
 need(result['role']=='shopkeeper' and result['role_updated_by']==str(h.ids['admin']),'Legitimate role update failed')
 need(not({'password_hash','password_reset_token_hash'}&set(result)),'Role response leaked private password material')

@case('R02','Admin can promote a customer while retaining current admin')
async def promote(h,o):
 result=await h.mutate(h.ids['admin'],h.ids['customer'],'admin')
 need(result['role']=='admin' and await h.actual.users.count_documents({'role':'admin'})==2,'Legitimate admin promotion failed')

@case('R03','Own-session last-admin demotion retains existing409')
async def self_demotion(h,o):
 _,error=await outcome(h.mutate(h.ids['admin'],h.ids['admin'],'customer'))
 need(isinstance(error,HTTPException) and error.status_code==409,'Own-session demotion protection changed')
 need(await h.actual.users.count_documents({'role':'admin'})==1,'Last admin was removed')

@case('R04','Missing target retains404 and changes no user role')
async def missing(h,o):
 _,error=await outcome(h.mutate(h.ids['admin'],ObjectId(),'customer'))
 need(isinstance(error,HTTPException) and error.status_code==404,'Missing-target contract changed')
 need(await h.actual.users.count_documents({'role':'admin'})==1,'Missing target changed roles')

@case('R05','An already-demoted in-flight actor cannot mutate another account')
async def stale_actor(h,o):
 await h.actual.users.update_one({'_id':h.ids['admin']},{'$set':{'role':'customer'}})
 target=h.ids['customer']
 _,error=await outcome(h.mutate(h.ids['admin'],target,'shopkeeper'))
 need(isinstance(error,HTTPException) and error.status_code==403,'Demoted in-flight actor retained mutation authority')
 saved=await h.actual.users.find_one({'_id':target})
 need(saved['role']=='customer','Demoted actor changed target role')

async def cross_demote(h,o,n,preexisting_guard):
 ids=await h.admin_cohort(n)
 if preexisting_guard:await h.actual.security_locks.insert_one({'_id':'admin-role-mutations','version':0})
 h.barrier_parties=n
 results=await asyncio.wait_for(asyncio.gather(*(outcome(h.mutate(ids[i],ids[(i+1)%n],'customer')) for i in range(n))),35)
 successes=sum(error is None for _,error in results)
 failures=[error for _,error in results if error is not None]
 remaining=await h.actual.users.count_documents({'role':'admin'})
 o.update({'actors':n,'successes':successes,'rejected_statuses':[getattr(e,'status_code',type(e).__name__) for e in failures],
           'remaining_admins':remaining,'nontransactional_count_barrier_reads':h.nontransactional_count_reads,
           'session_bound_count_reads':h.session_count_reads,'guard_preexisting':preexisting_guard})
 need(remaining>=1,'Concurrent cross-demotion removed every admin')
 need(successes<=n-1 and all(isinstance(e,HTTPException) and e.status_code in (403,409) for e in failures),'Unexpected concurrency outcome or server failure')

for i,n,existing in [('R06',2,False),('R07',2,True),('R08',4,False),('R09',4,True)]:
 async def test(h,o,n=n,existing=existing):await cross_demote(h,o,n,existing)
 CASES.append((i,f'{n}-admin cross-demotion preserves at least one admin;guard preexisting={existing}',test))

@case('R10','Fault after actual role write rolls back the user and serialization guard')
async def role_abort(h,o):
 h.fail_after_role_write=True
 _,error=await outcome(h.mutate(h.ids['admin'],h.ids['customer'],'shopkeeper'))
 saved=await h.actual.users.find_one({'_id':h.ids['customer']})
 guard=await h.actual.security_locks.find_one({'_id':'admin-role-mutations'})
 o.update({'error_type':type(error).__name__ if error else None,'role_after':saved['role'],'guard_version':guard.get('version') if guard else None})
 need(isinstance(error,RuntimeError) and saved['role']=='customer','Aborted role write left a committed user change')
 need(guard is not None and guard['version']==0,'Aborted role write committed the guard mutation')
 result=await h.mutate(h.ids['admin'],h.ids['customer'],'shopkeeper')
 need(result['role']=='shopkeeper','Safe role retry after rollback failed')

@case('R11','Unavailable transaction session does not fall back to unsafe role writes')
async def no_session(h,o):
 h.session_unavailable=True
 _,error=await outcome(h.mutate(h.ids['admin'],h.ids['customer'],'shopkeeper'))
 saved=await h.actual.users.find_one({'_id':h.ids['customer']})
 need(error is not None and saved['role']=='customer','Unavailable transactions allowed standalone role mutation')

@case('R12','HTTP role endpoint retains nonadmin403 before mutation')
async def role_http_nonadmin(h,o):
 for role in ['customer','shopkeeper','delivery_partner']:
  r=await h.http('PATCH',f'/api/admin/users/{h.ids["customer"]}/role',role,{'role':'admin'})
  need(r.status_code==403,'Nonadmin role endpoint access accepted')
 need(await h.actual.users.count_documents({'role':'admin'})==1,'Unauthorized role request changed roles')

async def main(args):
 raw=args.source.read_text();tree=ast.parse(raw);nodes=[];refs=[]
 for n in tree.body:
  if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and n.name in SELECT:
   nodes.append(copy.deepcopy(n));refs.append({'symbol':n.name,'line':n.lineno,'end':n.end_lineno,'SHA256':hashlib.sha256(ast.get_source_segment(raw,n).encode()).hexdigest()})
 need({n.name for n in nodes}==SELECT,'Incomplete source extraction')
 code=compile(ast.Module(body=nodes,type_ignores=[]),str(args.source),'exec',dont_inherit=True)
 client=AsyncIOMotorClient('mongodb://127.0.0.1:27018/?replicaSet=rs0',serverSelectionTimeoutMS=7000,tz_aware=True)
 hello=await client.admin.command('hello')
 need(hello.get('setName')=='rs0' and hello.get('isWritablePrimary') is True,'Expected loopback PRIMARY unavailable')
 need(all(x.startswith(('127.0.0.1:','localhost:')) for x in hello.get('hosts',[])),'Nonlocal replica member refused')
 started=datetime.now(timezone.utc).isoformat();runid=uuid.uuid4().hex[:12];results=[];dbs=[]
 suite=ET.Element('testsuite',name='roles_diagnostics_'+args.stage,tests=str(len(CASES)),timestamp=started)
 for number,(identifier,description,fn) in enumerate(CASES,1):
  db_name=f'comein_roles_{args.stage}_{runid}_{number}'
  h=Harness(client,code,db_name);await h.seed();dbs.append(db_name)
  status='PASS';failure=None;obs={};began=time.monotonic()
  try:await asyncio.wait_for(fn(h,obs),50)
  except AssertionError as e:status='FAIL';failure=str(e)
  except Exception as e:status='ERROR';failure=type(e).__name__
  elapsed=time.monotonic()-began
  results.append({'id':identifier,'description':description,'status':status,'failure':failure,'seconds':elapsed,'observations':obs})
  el=ET.SubElement(suite,'testcase',classname='SEC05_SEC09',name=identifier,time=str(elapsed))
  if status!='PASS':ET.SubElement(el,'failure' if status=='FAIL' else 'error',message=failure or status).text=description
  print(identifier,status,failure or '',flush=True)
 counts={x:sum(c['status']==x for c in results) for x in ('PASS','FAIL','ERROR')};counts['SKIPPED']=0
 for key,tag in [('FAIL','failures'),('ERROR','errors'),('SKIPPED','skipped')]:suite.set(tag,str(counts[key]))
 d={'project':'COME-IN','stage':args.stage,'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),
    'source':str(args.source),'source_SHA256':hashlib.sha256(raw.encode()).hexdigest(),'source_SHA256_after':hashlib.sha256(args.source.read_bytes()).hexdigest(),
    'runner_SHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_symbols':refs,
    'command':[sys.executable,'-B',str(Path(__file__).resolve()),'--stage',args.stage,'--source',str(args.source)],
    'versions':{x:importlib.metadata.version(x) for x in ('motor','pymongo','fastapi','pydantic','httpx')},
    'counts':counts,'cases':results,'retained_databases':dbs,'replica_set':'rs0',
    'limits':['Actual source models/handlers/role dependency are executed;ASGI authentication is a synthetic fixture identity dependency,not JWT validation.',
              'Role state/concurrency and transaction rollback use real Motor/MongoDB;only the old nontransactional count reads are barrier-synchronized;session reads cannot barrier without deadlock.',
              'Only unique local fixture databases written,retained,no drops/migrations/provider/native/production calls.'],
    'production_source_modified':False,'global_failpoints':0,'provider_calls':0,'DB_drops':0}
 (P/f'roles-{args.stage}.json').write_text(json.dumps(d,indent=2)+'\n');ET.ElementTree(suite).write(P/f'roles-{args.stage}.xml',encoding='utf-8',xml_declaration=True)
 client.close();print(json.dumps({'counts':counts,'database_count':len(dbs)}),flush=True)
 return int(bool(counts['FAIL'] or counts['ERROR']))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--stage',choices=['before','after'],required=True);p.add_argument('--source',type=Path,required=True)
 args=p.parse_args()
 original_connect=socket.socket.connect
 def loopback_only(sock,address):
  if not isinstance(address,tuple) or address[0] not in ('127.0.0.1','localhost','::1') or address[1]!=27018:
   raise RuntimeError('External socket blocked by isolated security runner')
  return original_connect(sock,address)
 socket.socket.connect=loopback_only
 raise SystemExit(asyncio.run(main(args)))
