"""Construct candidate only. Parent owns applying changes to production source."""
from pathlib import Path
import ast,difflib,hashlib,json

OUT=Path(__file__).resolve().parent
BEFORE=OUT/'before-server.py'
text=BEFORE.read_text()
tree=ast.parse(text)
lines=text.splitlines(keepends=True)
offsets=[0]
for line in lines:offsets.append(offsets[-1]+len(line))
def span(n):return offsets[n.lineno-1]+n.col_offset,offsets[n.end_lineno-1]+n.end_col_offset
targets={'create_restaurant_payment_intent','verify_restaurant_payment','admin_refund_restaurant_order',
         'admin_refund_grocery_order','create_grocery_payment_intent','verify_grocery_payment'}
edits=[];sites=[]
for fn in tree.body:
 if not isinstance(fn,ast.AsyncFunctionDef) or fn.name not in targets:continue
 for node in ast.walk(fn):
  if not isinstance(node,ast.Call):continue
  direct=isinstance(node.func,ast.Attribute) and isinstance(node.func.value,ast.Name) and node.func.value.id in {'requests','http_requests'} and node.func.attr in {'get','post'}
  history=isinstance(node.func,ast.Name) and node.func.id=='_fetch_razorpay_refunds'
  if not(direct or history):continue
  start,end=span(node);old=text[start:end]
  if direct:new='await asyncio.to_thread(lambda: '+old+')'
  else:new='await asyncio.to_thread(_fetch_razorpay_refunds, '+old[len('_fetch_razorpay_refunds('):-1]+')'
  edits.append((start,end,new));sites.append({'function':fn.name,'original_line':node.lineno,'operation':ast.unparse(node.func),'replacement':new})
assert len(edits)==8
for start,end,new in sorted(edits,reverse=True):text=text[:start]+new+text[end:]
old='    raw=await request.body(); signature=request.headers.get("X-Razorpay-Signature","")\n'
new='''    # Bound raw bytes before allocation/HMAC, including chunked or dishonest lengths.
    max_body_bytes = 1024 * 1024
    declared_length = request.headers.get("Content-Length")
    if declared_length is not None:
        try:
            declared_size = int(declared_length)
        except (TypeError, ValueError):
            raise HTTPException(status_code=400, detail="Invalid webhook Content-Length")
        if declared_size < 0:
            raise HTTPException(status_code=400, detail="Invalid webhook Content-Length")
        if declared_size > max_body_bytes:
            raise HTTPException(status_code=413, detail="Webhook body exceeds 1 MiB limit")
    raw_buffer = bytearray()
    async for chunk in request.stream():
        if len(raw_buffer) + len(chunk) > max_body_bytes:
            raise HTTPException(status_code=413, detail="Webhook body exceeds 1 MiB limit")
        raw_buffer.extend(chunk)
    raw = bytes(raw_buffer)
    signature=request.headers.get("X-Razorpay-Signature","")
'''
assert text.count(old)==1
text=text.replace(old,new)
after=OUT/'candidate-server.py';after.write_text(text)
a=ast.parse(text)
before_nodes={getattr(x,'name',None):x for x in tree.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))}
after_nodes={getattr(x,'name',None):x for x in a.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))}
changed=[k for k,n in before_nodes.items() if ast.dump(n,include_attributes=False)!=ast.dump(after_nodes[k],include_attributes=False)]
assert set(changed)==targets|{'razorpay_webhook'}
assert [ast.dump(x,include_attributes=False) for x in tree.body if not(isinstance(x,ast.AsyncFunctionDef) and x.name in changed)]==[ast.dump(x,include_attributes=False) for x in a.body if not(isinstance(x,ast.AsyncFunctionDef) and x.name in changed)]
patch=''.join(difflib.unified_diff(BEFORE.read_text().splitlines(True),text.splitlines(True),fromfile='a/backend/server.py',tofile='b/backend/server.py'))
(OUT/'candidate.patch').write_text(patch)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
info={'before_source_SHA256':sha(BEFORE),'candidate_source_SHA256':sha(after),'changed_functions':changed,
      'offload_sites':sites,'imports_or_schema_or_routes_changed':False,'actual_source_modified':False,
      'scope':'SEC07 andSEC08 candidate only;all provider tests local mocks. ActualRazorpay/nativevalidation DEFERRED.'}
(OUT/'candidate-change-summary.json').write_text(json.dumps(info,indent=2)+'\n')
print(json.dumps({'changed_functions':changed,'offload_sites':len(sites),'candidate_SHA256':sha(after)}))
