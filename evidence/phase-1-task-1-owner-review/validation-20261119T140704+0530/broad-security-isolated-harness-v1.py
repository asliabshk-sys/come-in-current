"""Current-source security helpers/models in isolation;no server import or I/O.

These are executable function/model checks,not full HTTP/Mongo/provider tests.
Every selected production AST node is compiled unchanged except route decorators,
which are removed to avoid app registration. Database objects below are explicitly
in-memory synthetic doubles. The negative concurrency test asserts the actual
last-admin invariant and is expected to expose a defect;it is not xfailed.
"""
import ast
import asyncio
import copy
import hashlib
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import List, Literal, Optional

import pytest
from bson import ObjectId
from fastapi import Depends, HTTPException
from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator, model_validator

SOURCE = Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py')
SOURCE_SHA256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
SELECTED = {
 'doc_out','public_doc','_assert_shop_owner','_restaurant_owner','require_role',
 '_dp_public','_dp_safe_reason','_tracking_can_read','_object_id_or_404',
 'admin_update_user_role','AdminRoleUpdateIn','UpdateProfileIn','RegisterIn',
 'ProductVariantIn','MeasureIn','ProductIn','CartLine','QuoteLineIn',
 'DeliveryLocationUpdateIn',
}
tree = ast.parse(SOURCE.read_text())
nodes=[]
for node in tree.body:
    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and node.name in SELECTED:
        n=copy.deepcopy(node)
        if not isinstance(n,ast.ClassDef): n.decorator_list=[]
        nodes.append(n)
assert {n.name for n in nodes} == SELECTED
NS={
 'ObjectId':ObjectId,'Depends':Depends,'HTTPException':HTTPException,
 'BaseModel':BaseModel,'EmailStr':EmailStr,'Field':Field,
 'field_validator':field_validator,'model_validator':model_validator,
 'Optional':Optional,'List':List,'Literal':Literal,'datetime':datetime,
 'MEASURED_QTY_LIMIT':100000,'MEASURED_SELL_BY':{'weight':('g','kg'),'volume':('ml','L')},
 'get_current_user':lambda:None,'now_utc':lambda:datetime.now(timezone.utc),
 're':re,'__name__':'isolated_current_source',
}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(SOURCE),'exec'),NS)

@pytest.fixture(autouse=True)
def prohibit_network(monkeypatch):
    import socket
    def deny(*args,**kwargs): raise AssertionError('No network is permitted by this isolated test')
    monkeypatch.setattr(socket.socket,'connect',deny)
    monkeypatch.setattr(socket,'create_connection',deny)

@pytest.mark.parametrize('guard',['_assert_shop_owner','_restaurant_owner'])
@pytest.mark.parametrize('role,identity,allowed',[
 ('admin','another-user',True),('shopkeeper','synthetic-owner',True),
 ('shopkeeper','another-user',False),('customer','synthetic-owner',False),
 ('customer','another-user',False),('delivery_partner','synthetic-owner',False),
])
def test_owner_guards_require_current_role_and_ownership(guard,role,identity,allowed):
    if allowed:
        NS[guard]({'owner_id':'synthetic-owner'},{'id':identity,'role':role})
    else:
        with pytest.raises(HTTPException) as err:
            NS[guard]({'owner_id':'synthetic-owner'},{'id':identity,'role':role})
        assert err.value.status_code==403

@pytest.mark.parametrize('role,allowed',[('admin',True),('customer',False),('shopkeeper',False),('delivery_partner',False)])
def test_admin_dependency_rejects_other_roles(role,allowed):
    async def run():
        dep=NS['require_role']('admin')
        user={'id':'synthetic-user','role':role}
        if allowed: assert await dep(user)==user
        else:
            with pytest.raises(HTTPException) as err: await dep(user)
            assert err.value.status_code==403
    asyncio.run(run())

def test_document_serialization_strips_known_sensitive_fields():
    oid=ObjectId()
    original={'_id':oid,'password_hash':'synthetic-hash-sentinel','grocery_idempotency_scope':'synthetic-scope','name':'fixture'}
    out=NS['doc_out'](original)
    assert out=={'id':str(oid),'name':'fixture'}
    assert original['password_hash']=='synthetic-hash-sentinel'

def test_public_document_strips_default_actor_fields():
    out=NS['public_doc']({'owner_id':'fixture','updated_by':'fixture','uploader_id':'fixture','name':'item'})
    assert out=={'name':'item'}

def test_delivery_progress_whitelist_excludes_encrypted_and_raw_pii():
    out=NS['_dp_public']({'_id':ObjectId(),'full_name_enc':'synthetic-encrypted-sentinel',
      'mobile_enc':'synthetic-encrypted-sentinel','residential_address_enc':'synthetic-encrypted-sentinel',
      'alternate_contact_enc':'synthetic-encrypted-sentinel','full_name':'synthetic-name','mobile':'synthetic-phone'})
    assert not set(out)&{'full_name_enc','mobile_enc','residential_address_enc','alternate_contact_enc','full_name','mobile'}
    assert 'synthetic-encrypted-sentinel' not in repr(out)

def test_delivery_decision_reason_redacts_fixture_identity_shapes():
    # Format-only synthetic values,not real identity/account data.
    value='identity 123456789012, PAN ABCDE1234F, phone 1234567890'
    out=NS['_dp_safe_reason'](value)
    assert '123456789012' not in out and 'ABCDE1234F' not in out and '1234567890' not in out
    assert '[identity-redacted]' in out and '[phone-redacted]' in out

def test_profile_model_does_not_allow_role_mass_assignment():
    out=NS['UpdateProfileIn'](name='fixture',role='admin',password_hash='synthetic').model_dump(exclude_none=True)
    assert out=={'name':'fixture'}

def test_registration_model_does_not_allow_role_mass_assignment():
    out=NS['RegisterIn'](name='fixture',email='fixture@example.test',password='synthetic-only-password',role='admin').model_dump()
    assert 'role' not in out

@pytest.mark.parametrize('price',[float('nan'),float('inf'),float('-inf'),0,-1])
def test_product_model_rejects_nonfinite_or_nonpositive_price(price):
    with pytest.raises(ValidationError):
        NS['ProductIn'](name='fixture',price=price,category_id='fixture',description='fixture')

@pytest.mark.parametrize('qty',[-1,0,100001,1.5])
def test_checkout_quantity_model_rejects_invalid_bounds(qty):
    with pytest.raises(ValidationError): NS['QuoteLineIn'](product_id='synthetic',qty=qty)

@pytest.mark.parametrize('latitude',[float('nan'),float('inf'),float('-inf')])
def test_delivery_coordinates_reject_nonfinite_values(latitude):
    with pytest.raises(ValidationError): NS['DeliveryLocationUpdateIn'](latitude=latitude,longitude=0)

class CurrentOwnerCollection:
    def __init__(self,owner): self.owner=owner
    async def find_one(self,query): return {'_id':query['_id'],'owner_id':self.owner}

@pytest.mark.parametrize('kind',['grocery','restaurant'])
@pytest.mark.parametrize('role,identity,current_owner,allowed',[
 ('admin','admin-fixture','someone-else',True),
 ('customer','customer-fixture','someone-else',True),
 ('customer','stranger-fixture','seller-fixture',False),
 ('shopkeeper','seller-fixture','seller-fixture',True),
 ('shopkeeper','seller-fixture','new-seller-fixture',False),
 ('customer','seller-fixture','seller-fixture',False),
 ('delivery_partner','seller-fixture','seller-fixture',False),
])
def test_tracking_checks_current_owner_role_without_real_records(kind,role,identity,current_owner,allowed):
    oid=ObjectId()
    order={'customer_id':'customer-fixture','restaurant_owner_id':'seller-fixture','shop_id':str(oid),'restaurant_id':str(oid)}
    NS['db']=SimpleNamespace(shops=CurrentOwnerCollection(current_owner),restaurants=CurrentOwnerCollection(current_owner))
    actual=asyncio.run(NS['_tracking_can_read'](order,kind,{'id':identity,'role':role}))
    assert actual==allowed

class AdminUsers:
    def __init__(self,ids):
        self.rows={oid:{'_id':oid,'role':'admin'} for oid in ids}
        self.arrivals=0
        self.both_counted=asyncio.Event()
    async def find_one(self,query,projection=None): return dict(self.rows[query['_id']])
    async def count_documents(self,query):
        snapshot=sum(row['role']=='admin' for row in self.rows.values())
        self.arrivals+=1
        if self.arrivals==2: self.both_counted.set()
        await self.both_counted.wait()
        return snapshot
    async def update_one(self,query,update):
        self.rows[query['_id']].update(update['$set'])
        return SimpleNamespace(modified_count=1)

def test_concurrent_cross_demotion_preserves_at_least_one_admin():
    async def run():
        a,b=ObjectId(),ObjectId()
        users=AdminUsers([a,b])
        NS['db']=SimpleNamespace(users=users)
        body=NS['AdminRoleUpdateIn'](role='customer')
        result=await asyncio.gather(
          NS['admin_update_user_role'](str(b),body,{'id':str(a),'role':'admin'}),
          NS['admin_update_user_role'](str(a),body,{'id':str(b),'role':'admin'}),
        )
        remaining=sum(row['role']=='admin' for row in users.rows.values())
        assert remaining>=1, f'Last-admin invariant failed:both demotions returned;remaining_admins={remaining}'
        return result
    asyncio.run(run())

def test_admin_cannot_demote_their_own_session():
    async def run():
        a=ObjectId()
        NS['db']=SimpleNamespace(users=AdminUsers([a]))
        with pytest.raises(HTTPException) as err:
            await NS['admin_update_user_role'](str(a),NS['AdminRoleUpdateIn'](role='customer'),{'id':str(a),'role':'admin'})
        assert err.value.status_code==409
    asyncio.run(run())
