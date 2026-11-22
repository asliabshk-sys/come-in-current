"""Source parsing only. Does not import/start the app or query OpenAPI/DB/providers."""
from pathlib import Path
import ast,json,hashlib,collections
E=Path(__file__).parent;A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115');P=A/'backend/server.py';s=P.read_text();t=ast.parse(s);out=[];models={}
def text(n):return ast.get_source_segment(s,n) or ast.unparse(n)
def expr(n):return None if n is None else text(n)
def callname(n):return ast.unparse(n.func) if isinstance(n,ast.Call) else None
for n in t.body:
 if isinstance(n,ast.ClassDef) and any(ast.unparse(b) in ['BaseModel','BaseDoc'] for b in n.bases):
  models[n.name]={'line':n.lineno,'bases':[text(x) for x in n.bases],'fields':[{'name':x.target.id,'annotation':text(x.annotation),'default_or_constraints':expr(x.value),'line':x.lineno} for x in n.body if isinstance(x,ast.AnnAssign) and isinstance(x.target,ast.Name)],'validators':[{'name':x.name,'line':x.lineno,'decorators':[text(d) for d in x.decorator_list],'source':text(x)} for x in n.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))]}
for n in t.body:
 if not isinstance(n,(ast.AsyncFunctionDef,ast.FunctionDef)):continue
 routes=[]
 for d in n.decorator_list:
  if isinstance(d,ast.Call) and isinstance(d.func,ast.Attribute) and isinstance(d.func.value,ast.Name) and d.func.value.id in ['api','app'] and d.func.attr in ['get','post','put','patch','delete','head','options'] and d.args and isinstance(d.args[0],ast.Constant):routes.append(d)
 if not routes:continue
 pos=n.args.posonlyargs+n.args.args;defaults=[None]*(len(pos)-len(n.args.defaults))+n.args.defaults;params=[]
 allargs=[(x,default,'positional-only' if i<len(n.args.posonlyargs) else 'positional-or-keyword') for i,(x,default) in enumerate(zip(pos,defaults))]+[(x,d,'keyword-only') for x,d in zip(n.args.kwonlyargs,n.args.kw_defaults)]
 if n.args.vararg:allargs.append((n.args.vararg,None,'var-positional'))
 if n.args.kwarg:allargs.append((n.args.kwarg,None,'var-keyword'))
 for arg,default,kind in allargs:
  constraint_calls=[]
  for container in [arg.annotation,default]:
   if container is None:continue
   for x in ast.walk(container):
    if isinstance(x,ast.Call) and isinstance(x.func,ast.Name) and x.func.id in ['Query','Path','Body','Form','File','Header','Cookie','Depends','Security','Field']:
     constraint_calls.append({'constructor':x.func.id,'arguments':[text(v) for v in x.args],'keywords':{k.arg:text(k.value) for k in x.keywords},'source':text(x)})
  names={x.id for x in ast.walk(arg.annotation) if isinstance(x,ast.Name)} if arg.annotation is not None else set();linked=sorted(names&models.keys());params.append({'name':arg.arg,'kind':kind,'annotation':expr(arg.annotation),'default_present':default is not None,'default_expression':expr(default),'constraint_or_dependency_calls':constraint_calls,'request_model_refs':linked,'line':arg.lineno,'required_at_python_signature':default is None})
 errors=[];returns=[];bodyreads=[];dependencies=[]
 for x in ast.walk(n):
  if isinstance(x,ast.Call):
   if isinstance(x.func,ast.Name) and x.func.id=='HTTPException':errors.append({'line':x.lineno,'arguments':[text(v) for v in x.args],'keywords':{v.arg:text(v.value) for v in x.keywords}})
   if isinstance(x.func,ast.Name) and x.func.id=='Depends':dependencies.extend(text(v) for v in x.args)
   if isinstance(x.func,ast.Attribute) and isinstance(x.func.value,ast.Name) and x.func.value.id=='request' and x.func.attr in ['body','json','form']:bodyreads.append({'line':x.lineno,'call':text(x)})
  if isinstance(x,ast.Return):
   keys=[]
   if isinstance(x.value,ast.Dict):keys=[k.value for k in x.value.keys if isinstance(k,ast.Constant) and isinstance(k.value,str)]
   returns.append({'line':x.lineno,'expression':expr(x.value),'literal_dict_keys':keys,'scope':'Static branch expression only;not a validated runtime response schema.'})
 for d in routes:
  kwargs={k.arg:text(k.value) for k in d.keywords};path=d.args[0].value;path=('/api' if d.func.value.id=='api' else '')+path;linked=sorted({m for p in params for m in p['request_model_refs']});out.append({'method':d.func.attr.upper(),'path':path,'function':n.name,'line':n.lineno,'end_line':n.end_lineno,'decorator_source':text(d),'decorator_kwargs':kwargs,'parameters':params,'return_annotation':expr(n.returns),'declared_response_model':kwargs.get('response_model'),'declared_status_code':kwargs.get('status_code'),'framework_default_status_if_unspecified':'200 in FastAPI route defaults;no live invocation performed','declared_response_details':{k:v for k,v in kwargs.items() if k.startswith('response') or k in ['status_code','summary','description','deprecated','include_in_schema']},'direct_HTTPException_sites':errors,'return_expression_sites':returns,'manual_request_body_reads':bodyreads,'dependencies':dependencies,'request_models':linked,'classification':'VERIFIED','verification_scope':'Current source signatures/defaults/constraint expressions/decorators/direct branch metadata only;not runtime acceptance. Helper-raised errors,dependency effects,conditional serialization and implicit schema generation require separate evidence.'})
old=json.loads((E.parent.parent/'phase-1-task-1-audit/api-inventory.json').read_text());newset={(x['method'],x['path'],x['function']) for x in out};oldset={(x['method'],x['path'],x['function']) for x in old};assert newset==oldset and len(out)==179 and len(models)==60
counts={'APIs':len(out),'models':len(models),'parameters':sum(len(x['parameters']) for x in out),'defaulted_parameters':sum(p['default_present'] for x in out for p in x['parameters']),'endpoints_with_Query':sum(any(c['constructor']=='Query' for p in x['parameters'] for c in p['constraint_or_dependency_calls']) for x in out),'Query_parameters':sum(any(c['constructor']=='Query' for c in p['constraint_or_dependency_calls']) for x in out for p in x['parameters']),'explicit_response_model_endpoints':sum(x['declared_response_model'] is not None for x in out),'duplicate_method_paths':[list(k) for k,v in collections.Counter((x['method'],x['path']) for x in out).items() if v>1],'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest()}
(E/'complete-api-inventory.json').write_text(json.dumps({'scope':out[0]['verification_scope'],'counts':counts,'endpoints':out,'request_models':models},indent=2));print(json.dumps(counts))
