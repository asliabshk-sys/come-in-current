from pathlib import Path
import requests,json
from dotenv import dotenv_values
from pymongo import MongoClient
root=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
v=dotenv_values(root/'backend/.env'); accounts=json.loads(Path('/workspace/come-in-tools/continuation-test-accounts.json').read_text())
base='http://127.0.0.1:8001/api'; results=[]
def login(email,password):
 r=requests.post(base+'/auth/login',json={'email':email,'password':password},timeout=15); assert r.status_code==200
 return {'Authorization':'Bearer '+r.json()['token']},r.json()['user']['id']
c,uid=login('continuation.customer@comein-preview.com',accounts['CUSTOMER']); a,_=login(v['ADMIN_EMAIL'],v['ADMIN_PASSWORD']); s,_=login('continuation.seller@comein-preview.com',accounts['SELLER'])
def check(method,path,headers,expected,payload=None):
 r=requests.request(method,base+path,headers=headers,json=payload,timeout=15); assert r.status_code==expected, (path,r.status_code)
 results.append({'method':method,'path':path,'expected':expected,'actual':r.status_code});return r
check('GET','/delivery-partner/provider-status',c,200)
check('PUT','/delivery-partner/application',c,200,{'full_name':'TEST Preview Rider','mobile':'9876500001','residential_address':'TEST 12 Preview Street, Pune','alternate_contact':'9876500002','consent_identity_verification':True,'consent_data_processing':True,'consent_declaration':True})
check('GET','/delivery-partner/application/mine',c,200)
check('POST','/delivery-partner/application/submit',c,409)
check('POST','/delivery-partner/otp/request',c,503,{})
check('GET','/delivery-partner/admin/applications',c,403)
check('GET','/delivery-partner/admin/applications',a,200)
check('GET','/delivery-partner/access',c,403)
check('GET','/delivery-partner/application/mine',{},401)
other=check('GET','/delivery-partner/application/mine',s,200)
assert 'TEST Preview Rider' not in other.text
Path(__file__).with_suffix('.json').write_text(json.dumps({'ok':True,'checks':results,'scope':'local synthetic identities; external verification remains disabled'},indent=2))
print('10 scoped delivery checks PASS, including expected fail-closed provider responses.')
