from pathlib import Path
import ast,json,collections,re
A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115');E=Path(__file__).parent;S=A/'backend/server.py';s=S.read_text();tree=ast.parse(s);api=[];schemas=[];indexes=[];functions={n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
def text(n):return ast.get_source_segment(s,n) or ast.unparse(n)
def depends(n):
 return [text(x.args[0]) for x in ast.walk(n) if isinstance(x,ast.Call) and isinstance(x.func,ast.Name) and x.func.id=='Depends' and x.args]
def dbcols(n):return sorted({x.attr for x in ast.walk(n) if isinstance(x,ast.Attribute) and isinstance(x.value,ast.Name) and x.value.id=='db'})
for n in tree.body:
 if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
  for d in n.decorator_list:
   if isinstance(d,ast.Call) and isinstance(d.func,ast.Attribute) and isinstance(d.func.value,ast.Name) and d.func.value.id in ['api','app'] and d.func.attr in ['get','post','patch','put','delete','head','options'] and d.args and isinstance(d.args[0],ast.Constant):
    deps=depends(n);kw={x.arg:text(x.value) for x in d.keywords};api.append({'method':d.func.attr.upper(),'path':('/api' if d.func.value.id=='api' else '')+d.args[0].value,'function':n.name,'line':n.lineno,'end_line':n.end_lineno,'dependencies':deps,'authorization':'role dependency' if any('require_role' in x for x in deps) else 'authenticated' if any(x=='get_current_user' for x in deps) else 'optional authentication' if any('optional' in x for x in deps) else 'no declared Depends;inspect body','schemas':{arg.arg:text(arg.annotation) for arg in n.args.args if arg.annotation},'response':kw,'collections':dbcols(n),'body_permission_markers':[x for x in ['_assert_shop_owner','_assert_restaurant_owner','_tracking_can_read','_delivery_active_record','require_role','get_current_user','verify_signature','compare_digest'] if x in text(n)]})
 if isinstance(n,ast.ClassDef) and any(text(b) in ['BaseModel','BaseDoc'] for b in n.bases):schemas.append({'name':n.name,'line':n.lineno,'fields':[{'name':x.target.id,'type':text(x.annotation),'constraint':text(x.value) if x.value else None} for x in n.body if isinstance(x,ast.AnnAssign) and isinstance(x.target,ast.Name)],'validators':[x.name for x in n.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))]})
for x in ast.walk(tree):
 if isinstance(x,ast.Call) and isinstance(x.func,ast.Attribute) and x.func.attr=='create_index':
  col=x.func.value.attr if isinstance(x.func.value,ast.Attribute) and isinstance(x.func.value.value,ast.Name) and x.func.value.value.id=='db' else text(x.func.value)
  def literal(v):
   try:return ast.literal_eval(v)
   except (ValueError,TypeError):return text(v)
  indexes.append({'collection':col,'line':x.lineno,'keys':literal(x.args[0]) if x.args else None,'options':{k.arg:literal(k.value) for k in x.keywords}})
(E/'api-inventory.json').write_text(json.dumps(api,indent=2));(E/'model-inventory.json').write_text(json.dumps(schemas,indent=2));(E/'index-inventory.json').write_text(json.dumps(indexes,indent=2));(E/'collection-source-inventory.json').write_text(json.dumps(dbcols(tree),indent=2));duplicates=[{'method':k[0],'path':k[1],'count':v} for k,v in collections.Counter((x['method'],x['path']) for x in api).items() if v>1];(E/'duplicate-api-routes.json').write_text(json.dumps(duplicates,indent=2));(E/'function-line-map.json').write_text(json.dumps({k:{'line':v.lineno,'end_line':v.end_lineno} for k,v in functions.items()},indent=2));print(len(api),'APIs',len(schemas),'models',len(indexes),'indexes',len(dbcols(tree)),'collection references;duplicate routes',duplicates);print('Public mutation candidates',[(x['path'],x['function']) for x in api if x['method'] not in ['GET','HEAD','OPTIONS'] and x['authorization']=='no declared Depends;inspect body'])
