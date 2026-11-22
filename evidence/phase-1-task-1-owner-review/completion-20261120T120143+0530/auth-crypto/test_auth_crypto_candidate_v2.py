"""Actual source auth/crypto functions on isolated Mongo;no server/.env import."""
import ast
import asyncio
import copy
from datetime import datetime,timedelta,timezone
import hashlib
import importlib.metadata
import io
import json
import logging
from pathlib import Path
import secrets
import smtplib
import socket
import sys
from types import SimpleNamespace
from typing import Optional
import uuid
import xml.etree.ElementTree as ET

import bcrypt
from bson import ObjectId
from fastapi import HTTPException,Request
import jwt
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel,EmailStr,Field

HERE=Path(__file__).resolve().parent
BACKEND=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
sys.path.insert(0,str(BACKEND))
from mongo_transactions import run_transaction

SELECT={'now_utc','doc_out','hash_password','verify_password','_jwt_secret',
 'create_access_token','get_bearer_token','get_current_user_optional','get_current_user',
 'ResetPasswordIn','ForgotPasswordIn','LoginIn','login','reset_password','forgot_password',
 '_send_password_reset_email','_object_id_or_404'}
CONSTANTS={'BCRYPT_ROUNDS','JWT_ALG','ACCESS_TTL_MIN'}
CASES=[]
def case(id,invariant):
 def register(fn):CASES.append((id,invariant,fn));return fn
 return register
def require(value,message):
 if not value:raise AssertionError(message)

class OfflineSMTP:
 messages=[]
 fail=False
 def __init__(self,host,port,timeout):
  if not 1<=port<=65535:raise ValueError('Synthetic invalid port')
 def __enter__(self):return self
 def __exit__(self,*args):return False
 def starttls(self):
  if self.fail:raise RuntimeError('Synthetic TLS failure')
 def login(self,*args):pass
 def send_message(self,message):self.messages.append(message)

class AbortUsers:
 def __init__(self,actual):self.actual=actual
 def __getattr__(self,name):return getattr(self.actual,name)
 async def update_one(self,*args,**kwargs):
  result=await self.actual.update_one(*args,**kwargs)
  raise RuntimeError('Synthetic failure after actual user write')

class Harness:
 def __init__(self,client,db,code,caseid,runid):
  self.client=client;self.db=db;self.caseid=caseid;self.runid=runid
  self.environ={'JWT_SECRET':secrets.token_urlsafe(48)}
  self.logs=io.StringIO();self.logger=logging.getLogger('comein.auth.crypto.'+runid+caseid)
  self.logger.propagate=False;self.logger.setLevel(logging.DEBUG)
  self.logger.addHandler(logging.StreamHandler(self.logs))
  async def rate_stub(*args,**kwargs):return None
  self.ns={'__name__':'auth_crypto_source_isolation','datetime':datetime,'timedelta':timedelta,
    'timezone':timezone,'Optional':Optional,'BaseModel':BaseModel,'EmailStr':EmailStr,'Field':Field,
    'bcrypt':bcrypt,'jwt':jwt,'hashlib':hashlib,'secrets':secrets,'ObjectId':ObjectId,
    'HTTPException':HTTPException,'Request':Request,'os':SimpleNamespace(environ=self.environ),
    'logger':self.logger,'client':client,'db':db,'run_transaction':run_transaction,
    '_enforce_auth_rate_limit':rate_stub,'_check_auth_rate_limit':rate_stub,'_record_auth_attempt':rate_stub}
  exec(code,self.ns)
  self.user=None
 async def seed(self):
  self.password='Initial synthetic fixture!'
  self.user={'_id':ObjectId(),'name':'Synthetic fixture','email':(self.caseid+'-'+self.runid+'@example.com').lower(),
    'role':'customer','password_hash':self.ns['hash_password'](self.password),'validation_run':self.runid}
  await self.db.users.insert_one(self.user)
 def request(self,token=None):
  headers=[] if token is None else [(b'authorization',('Bearer '+token).encode())]
  return Request({'type':'http','method':'POST','path':'/auth/fixture','scheme':'http',
   'headers':headers,'client':('127.0.0.1',1),'server':('127.0.0.1',0),'query_string':b''})
 def mint(self,user=None,**extra):
  u=user or self.user
  data={'sub':str(u['_id']),'role':u['role'],'email':u['email'],'type':'access',
   'exp':self.ns['now_utc']()+timedelta(days=7)}
  data.update(extra)
  return jwt.encode(data,self.environ['JWT_SECRET'],algorithm='HS256')
 async def authenticate(self,token):return await self.ns['get_current_user_optional'](self.request(token))
 async def issue_token(self):
  raw=secrets.token_urlsafe(36)
  rec={'user_id':str(self.user['_id']),'token_hash':hashlib.sha256(raw.encode()).hexdigest(),
   'used':False,'created_at':self.ns['now_utc'](),'expires_at':self.ns['now_utc']()+timedelta(minutes=30)}
  result=await self.db.password_resets.insert_one(rec);rec['_id']=result.inserted_id
  return raw,rec
 async def reset(self):
  raw,rec=await self.issue_token()
  await self.ns['reset_password'](self.ns['ResetPasswordIn'](token=raw,new_password='Changed synthetic fixture!'),self.request())
  return rec
 def smtp(self,port='587'):
  self.environ.update(SMTP_HOST='smtp.fixture.invalid',SMTP_FROM='fixture@example.com',
   PASSWORD_RESET_URL='https://example.invalid/reset',SMTP_PORT=port)
 async def forgot(self):return await self.ns['forgot_password'](self.ns['ForgotPasswordIn'](email=self.user['email']),self.request())

@case('AUTH-01','Legacy JWT without pwdv remains valid for unchanged legacy account')
async def legacy_token(h,o):require(await h.authenticate(h.mint()) is not None,'Unchanged legacy session was rejected')

@case('AUTH-02','New token preserves seven-day expiry and role-authoritative authentication')
async def minted(h,o):
 token=h.ns['create_access_token'](str(h.user['_id']),'admin',h.user['email'])
 result=await h.authenticate(token);payload=jwt.decode(token,h.environ['JWT_SECRET'],algorithms=['HS256'])
 require(result and result['role']=='customer','Token role bypassed persisted user role')
 require(abs(payload['exp']-(h.ns['now_utc']()+timedelta(days=7)).timestamp())<3,'Existing expiry changed')

@case('AUTH-03','Successful password reset revokes a previously issued access token')
async def reset_revokes(h,o):
 token=h.mint();require(await h.authenticate(token) is not None,'Fixture token was invalid before reset')
 await h.reset();accepted=await h.authenticate(token) is not None;o['old_token_accepted_after_reset']=accepted
 require(not accepted,'Pre-reset token remains accepted')

@case('AUTH-04','Login after reset mints the current version and remains usable')
async def login_after_reset(h,o):
 await h.reset();result=await h.ns['login'](h.ns['LoginIn'](email=h.user['email'],password='Changed synthetic fixture!'),h.request())
 saved=await h.db.users.find_one({'_id':h.user['_id']});payload=jwt.decode(result['token'],h.environ['JWT_SECRET'],algorithms=['HS256'])
 require(payload.get('pwdv',0)==saved.get('password_version',0),'Login minted an obsolete token version')
 require(await h.authenticate(result['token']) is not None,'Fresh login token was rejected')
 require('password_version' not in result['user'] and 'password_hash' not in result['user'],'Private password metadata leaked')

@case('AUTH-05','Other accounts active sessions are preserved after a reset')
async def other_session(h,o):
 other={'_id':ObjectId(),'email':'other-'+h.runid+'@example.com','role':'shopkeeper','password_hash':h.user['password_hash']}
 await h.db.users.insert_one(other);token=h.mint(other)
 await h.reset();require(await h.authenticate(token) is not None,'Reset revoked an unrelated account session')

@case('AUTH-06','Password version increments only on the reset account')
async def increment(h,o):
 await h.reset();saved=await h.db.users.find_one({'_id':h.user['_id']});o['version_after_reset']=saved.get('password_version',0)
 require(saved.get('password_version',0)==1,'Successful reset did not increment password version')

@case('AUTH-07','Aborted password update rolls back password version and token claim')
async def version_rollback(h,o):
 raw,rec=await h.issue_token();h.ns['db']=SimpleNamespace(users=AbortUsers(h.db.users),password_resets=h.db.password_resets)
 try:await h.ns['reset_password'](h.ns['ResetPasswordIn'](token=raw,new_password='Changed synthetic fixture!'),h.request())
 except RuntimeError:pass
 else:require(False,'Injected failure did not occur')
 saved=await h.db.users.find_one({'_id':h.user['_id']});token=await h.db.password_resets.find_one({'_id':rec['_id']})
 require(saved['password_hash']==h.user['password_hash'] and saved.get('password_version',0)==0 and token['used'] is False,'Transaction left partial password/version/token state')

@case('AUTH-08','Missing-version JWT cannot access an account with a later password version')
async def missing_version(h,o):
 await h.db.users.update_one({'_id':h.user['_id']},{'$set':{'password_version':2}})
 require(await h.authenticate(h.mint()) is None,'Unversioned token bypassed revocation')

@case('AUTH-09','A token version different from the persisted account version is rejected')
async def mismatched_version(h,o):require(await h.authenticate(h.mint(pwdv=1)) is None,'Mismatched version was ignored')

@case('AUTH-10','Malformed signed token-version metadata fails closed')
async def malformed_version(h,o):require(await h.authenticate(h.mint(pwdv='not-a-version')) is None,'Malformed version was accepted')

@case('AUTH-11','Expired and invalid-signature tokens remain rejected')
async def invalid_tokens(h,o):
 require(await h.authenticate(h.mint(exp=h.ns['now_utc']()-timedelta(seconds=1))) is None,'Expired token accepted')
 token=h.mint();head,payload,sig=token.split('.');tampered=head+'.'+payload+'.'+('A' if sig[0]!='A' else 'B')+sig[1:]
 require(await h.authenticate(tampered) is None,'Invalid signature accepted')

@case('AUTH-12','Password version and hash are not exposed by doc_out')
async def private_version(h,o):
 out=h.ns['doc_out']({'_id':h.user['_id'],'password_hash':'synthetic','password_version':7,'role':'customer'})
 require('password_version' not in out and 'password_hash' not in out,'Password metadata exposed')

@case('HASH-01','Existing short raw-bcrypt hashes remain compatible')
async def legacy_short(h,o):
 raw=bcrypt.hashpw(b'Legacy synthetic password!',bcrypt.gensalt(rounds=12)).decode()
 require(h.ns['verify_password']('Legacy synthetic password!',raw),'Existing raw bcrypt hash failed')
 require(not h.ns['verify_password']('Wrong synthetic password!',raw),'Wrong legacy password accepted')

@case('HASH-02','Legacy72-byte password stays valid but appended suffix aliases are rejected')
async def legacy_limit(h,o):
 value='A'*72;raw=bcrypt.hashpw(value.encode(),bcrypt.gensalt(rounds=12)).decode()
 require(h.ns['verify_password'](value,raw),'Exactly72byte legacy password rejected')
 require(not h.ns['verify_password'](value+'different suffix',raw),'Legacy truncated suffix alias accepted')

@case('HASH-03','Distinct accepted long ASCII passwords do not authenticate interchangeably')
async def long_ascii(h,o):
 a='A'*72+'one';b='A'*72+'two';hashed=h.ns['hash_password'](a)
 require(h.ns['verify_password'](a,hashed),'New long password failed its own hash')
 require(not h.ns['verify_password'](b,hashed),'Long ASCII suffix alias accepted')

@case('HASH-04','Distinct long UTF8 passwords do not authenticate interchangeably')
async def long_utf8(h,o):
 a='प'*25+'one';b='प'*25+'two';hashed=h.ns['hash_password'](a)
 require(h.ns['verify_password'](a,hashed),'New long Unicode password failed')
 require(not h.ns['verify_password'](b,hashed),'UTF8 suffix alias accepted')

@case('HASH-05','Short new passwords retain bcrypt12 format and randomized salt')
async def cost_and_salt(h,o):
 a=h.ns['hash_password']('Short synthetic value!');b=h.ns['hash_password']('Short synthetic value!')
 require(a.startswith('$2b$12$') and b.startswith('$2b$12$') and a!=b,'Short bcrypt cost or salt contract changed')

@case('HASH-06','Tagged full-input hashes use bcrypt12 and verify only the full password')
async def tagged_cost(h,o):
 value='Synthetic long prefix '*5;hashed=h.ns['hash_password'](value)
 require(hashed.startswith('bcrypt_sha256_v1$$2b$12$'),'Long hash lacks explicit version/cost')
 require(h.ns['verify_password'](value,hashed) and not h.ns['verify_password'](value[:-1],hashed),'Tagged verification discarded input')

@case('HASH-07','Malformed stored hashes fail verification safely')
async def malformed_hash(h,o):
 for value in ['invalid','bcrypt_sha256_v1$invalid','',None]:
  try:result=h.ns['verify_password']('Synthetic value',value)
  except Exception:result=True
  require(result is False,'Malformed password hash did not fail closed')

@case('HASH-08','Accepted128character Unicode password is supported without truncation')
async def max_chars(h,o):
 a='प'*127+'A';b='प'*127+'B';model=h.ns['ResetPasswordIn'](token='t'*48,new_password=a)
 hashed=h.ns['hash_password'](model.new_password)
 require(h.ns['verify_password'](a,hashed) and not h.ns['verify_password'](b,hashed),'Accepted maximum input truncates')

@case('SMTP-01','Missing SMTP configuration returns generic response and removes undelivered token')
async def missing_smtp(h,o):
 result=await h.forgot();require('message' in result and len(result)==1,'Forgot response exposed data')
 require(await h.db.password_resets.count_documents({'user_id':str(h.user['_id'])})==0,'Undelivered token remained')

@case('SMTP-02','Malformed SMTP_PORT is safely handled and leaves no active token')
async def invalid_smtp(h,o):
 h.smtp('not-a-number')
 try:result=await h.forgot();escaped=False
 except Exception:escaped=True;result={}
 active=await h.db.password_resets.count_documents({'user_id':str(h.user['_id']),'used':False})
 o.update({'configuration_exception_escaped':escaped,'active_undelivered_tokens':active})
 require(not escaped and 'message' in result and active==0,'SMTP parsing escaped cleanup or retained an active token')

@case('SMTP-03','Out-of-range SMTP port leaves no active token')
async def port_range(h,o):
 h.smtp('65536');await h.forgot()
 require(await h.db.password_resets.count_documents({'user_id':str(h.user['_id'])})==0,'Out-of-range SMTP token remained')

@case('SMTP-04','Transport failure cleanup reveals no token or SMTP credentials')
async def transport_failure(h,o):
 h.smtp();h.environ.update(SMTP_USER='synthetic-user-sentinel',SMTP_PASSWORD='synthetic-secret-sentinel')
 OfflineSMTP.fail=True
 try:result=await h.forgot()
 finally:OfflineSMTP.fail=False
 require('message' in result and await h.db.password_resets.count_documents({'user_id':str(h.user['_id'])})==0,'SMTP failure was not cleaned up')
 require('synthetic-secret-sentinel' not in h.logs.getvalue() and h.user['email'] not in h.logs.getvalue(),'SMTP credentials or fixture identity logged')

@case('SMTP-05','Configured synthetic SMTP transport retains only a token digest')
async def transport_success(h,o):
 h.smtp();OfflineSMTP.messages=[];result=await h.forgot()
 rows=await h.db.password_resets.find({'user_id':str(h.user['_id'])}).to_list(10)
 require(len(OfflineSMTP.messages)==1 and len(rows)==1,'Synthetic transport did not issue one token')
 require('token_hash' in rows[0] and len(rows[0]['token_hash'])==64 and 'token' not in rows[0] and len(result)==1,'Raw token exposed or not hashed')

async def main(source,stage):
 raw=source.read_bytes();source_sha=hashlib.sha256(raw).hexdigest();tree=ast.parse(raw.decode())
 nodes=[];refs=[]
 for node in tree.body:
  selected=isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and node.name in SELECT
  if isinstance(node,ast.Assign):selected=any(isinstance(t,ast.Name) and t.id in CONSTANTS for t in node.targets)
  if selected:
   clone=copy.deepcopy(node)
   if isinstance(clone,(ast.FunctionDef,ast.AsyncFunctionDef)):clone.decorator_list=[]
   nodes.append(clone);refs.append({'symbol':getattr(node,'name',ast.unparse(node.targets[0]) if isinstance(node,ast.Assign) else None),'line':node.lineno,'end_line':node.end_lineno})
 require(len(nodes)==len(SELECT)+len(CONSTANTS),'Source extraction incomplete')
 code=compile(ast.fix_missing_locations(ast.Module(body=nodes,type_ignores=[])),str(source),'exec',dont_inherit=True)
 client=AsyncIOMotorClient('mongodb://127.0.0.1:27018/?replicaSet=rs0',serverSelectionTimeoutMS=8000,tz_aware=True)
 hello=await client.admin.command('hello');require(hello.get('setName')=='rs0' and hello.get('isWritablePrimary') is True,'Expected local PRIMARY unavailable')
 require(all(x.startswith(('127.0.0.1:','localhost:')) for x in hello.get('hosts',[])),'Nonlocal Mongo member')
 runid=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]
 dbname='comein_auth_crypto_'+stage+'_'+runid.lower();db=client[dbname]
 started=datetime.now(timezone.utc).isoformat();results=[];suite=ET.Element('testsuite',name='auth-crypto-'+stage,tests=str(len(CASES)),timestamp=started)
 original_smtp=smtplib.SMTP;smtplib.SMTP=OfflineSMTP
 try:
  for id,invariant,fn in CASES:
   h=Harness(client,db,code,id,runid);await h.seed();observations={};status='PASS';failure=None
   try:await asyncio.wait_for(fn(h,observations),timeout=30)
   except AssertionError as exc:status='FAIL';failure=str(exc)
   except Exception as exc:status='ERROR';failure=type(exc).__name__
   results.append({'id':id,'invariant':invariant,'status':status,'failure':failure,'observations':observations})
   t=ET.SubElement(suite,'testcase',classname='completion.auth_crypto',name=id)
   if status!='PASS':ET.SubElement(t,'failure' if status=='FAIL' else 'error',message=failure or status)
   print(id,status,failure or '',flush=True)
 finally:smtplib.SMTP=original_smtp
 counts={k:sum(x['status']==k for x in results) for k in ('PASS','FAIL','ERROR')};counts['SKIPPED']=0
 for key,label in [('FAIL','failures'),('ERROR','errors'),('SKIPPED','skipped')]:suite.set(label,str(counts[key]))
 result={'stage':stage,'source':str(source),'source_SHA256':source_sha,'source_SHA256_after':hashlib.sha256(source.read_bytes()).hexdigest(),
  'runner_SHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_symbols':refs,'started_UTC':started,'finished_UTC':datetime.now(timezone.utc).isoformat(),
  'database':dbname,'database_retained':True,'replica_set':'rs0','counts':counts,'cases':results,'python':sys.version,'executable':sys.executable,
  'versions':{x:importlib.metadata.version(x) for x in ('motor','pymongo','bcrypt','PyJWT','pydantic')},
  'command':[sys.executable,'-B',str(Path(__file__).resolve()),str(source),stage],
  'safety':{'production_access':False,'provider_calls':0,'SMTP_transport_stubbed':True,'DB_drops':0,'global_failpoints':0,'source_modified':False,'actual_credentials_read_or_written':False},
  'limitations':['Actual AST-extracted function/model bodies and real Mongo transactions;not full HTTP/startup/middleware.','Auth throttle stubs isolate SEC02/06;separate rate workstream validates limits.','SMTP transport is in-memory;actualSMTPdelivery/certificates/configurationremainexternal.']}
 (HERE/(stage+'-results.json')).write_text(json.dumps(result,indent=2)+'\n');ET.ElementTree(suite).write(HERE/(stage+'-junit.xml'),encoding='utf-8',xml_declaration=True)
 client.close();require(result['source_SHA256_after']==source_sha,'Source changed during run')
 print(json.dumps({'stage':stage,'counts':counts,'database_retained':dbname}),flush=True)
 return 1 if counts['FAIL'] or counts['ERROR'] else 0

if __name__=='__main__':
 source=Path(sys.argv[1]);stage=sys.argv[2]
 # Any accidental external connection is rejected,including from transport code.
 original_connect=socket.socket.connect
 def local_only(sock,address):
  if not isinstance(address,tuple) or address[0] not in ('127.0.0.1','localhost','::1') or address[1]!=27018:
   raise RuntimeError('Nonlocal network access prohibited by isolated auth tests')
  return original_connect(sock,address)
 socket.socket.connect=local_only
 raise SystemExit(asyncio.run(main(source,stage)))
