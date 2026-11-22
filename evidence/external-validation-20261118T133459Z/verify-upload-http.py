from pathlib import Path
import json,requests
root=Path('/workspace/come-in-tools');password=json.loads((root/'continuation-test-accounts.json').read_text())['CUSTOMER'];base='http://127.0.0.1:8001/api';checks=[]
s=requests.Session();res=s.post(base+'/auth/login',json={'email':'continuation.customer@comein-preview.com','password':password},timeout=10);assert res.status_code==200;token=res.json()['token'];auth={'Authorization':'Bearer '+token};checks.append('existing local customer authenticated; token not persisted')
res=s.post(base+'/uploads/image',files={'file':('untrusted.txt',b'<html>not an image</html>','image/png')},timeout=10);assert res.status_code==401;checks.append('unauthenticated upload401')
for mime in ['image/jpeg','image/png','image/gif','image/webp']:
 for data in [b'',b'<html>not an image</html>']:
  res=s.post(base+'/uploads/image',headers=auth,files={'file':('untrusted.txt',data,mime)},timeout=10);assert res.status_code==400,(mime,res.status_code);assert res.json()['detail']=='Image bytes do not match the declared file type';checks.append(mime+' empty/spoof rejected400 before storage')
for path in ['/grocery/payments/config','/restaurant/payments/config']:
 res=s.get(base+path,timeout=10);assert res.status_code==200;value=res.json();assert value['razorpay_enabled'] is False;assert value['razorpay_key_id'] is None;checks.append(path+' unconfigured fails closed')
r={'passed':len(checks),'failed':0,'skipped':0,'checks':checks,'scope':'Local real HTTP/auth negative uploads and config GET; no object upload/provider payment/refund/webhook delivery attempted'};Path(__file__).with_name('upload-http-results.json').write_text(json.dumps(r,indent=2));print(len(checks),'PASS,0FAIL,0SKIP; local HTTP only')
