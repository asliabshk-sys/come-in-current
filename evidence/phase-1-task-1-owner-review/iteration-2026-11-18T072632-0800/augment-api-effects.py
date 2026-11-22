from pathlib import Path
import ast,json,re,collections
E=Path(__file__).parent;P=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py');s=P.read_text();tree=ast.parse(s);nodes={n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))};data=json.loads((E/'complete-api-inventory.json').read_text());writes={'insert_one','insert_many','update_one','update_many','replace_one','delete_one','delete_many','find_one_and_update','find_one_and_replace','find_one_and_delete','bulk_write','create_index','create_indexes','drop','drop_collection'};direct={};calls={}
for name,n in nodes.items():
 direct[name]=[];calls[name]=set()
 for c in ast.walk(n):
  if not isinstance(c,ast.Call):continue
  if isinstance(c.func,ast.Name) and c.func.id in nodes:calls[name].add(c.func.id)
  if isinstance(c.func,ast.Name) and c.func.id=='Depends' and c.args:
   a=c.args[0]
   if isinstance(a,ast.Name) and a.id in nodes:calls[name].add(a.id)
  if isinstance(c.func,ast.Attribute) and c.func.attr in writes:direct[name].append({'function':name,'line':c.lineno,'method':c.func.attr,'receiver':ast.unparse(c.func.value),'scope':'Possible source-level write site;branch and receiver must be interpreted,not executed.'})
results=[]
for ep in data['endpoints']:
 n=nodes[ep['function']];ep['signature_arguments']=ast.unparse(n.args);path_names=set(re.findall(r'\{([^}:]+)(?::[^}]+)?\}',ep['path']))
 for p in ep['parameters']:
  cs=p['constraint_or_dependency_calls'];factories=[x for x in cs if x['constructor'] in ['Query','Path','Body','Form','File','Header','Cookie']]
  if any(x['constructor'] in ['Depends','Security'] for x in cs):hint='Dependency-injected;not a client payload field'
  elif p['annotation'] in ['Request','Response']:hint='Framework request/response object'
  elif factories:hint='Declared '+','.join(x['constructor'] for x in factories)
  elif p['name'] in path_names:hint='Path placeholder'
  elif p['request_model_refs']:hint='Pydantic body-model reference (source)'
  else:hint='Framework binding inference required;annotation/default recorded verbatim'
  p['source_binding_hint']=hint;p['framework_requiredness_note']='Python signature default is not the same as HTTP field optionality;for example File(...)/Form(...) remain required despite a Python default. Factory expressions/Annotated metadata and Pydantic model fields are authoritative source declarations;no live OpenAPI schema or request execution was performed.'
 if ep['method']!='GET':continue
 visited=set();queue=[ep['function']]
 while queue:
  name=queue.pop()
  if name in visited:continue
  visited.add(name);queue.extend(calls.get(name,set())-visited)
 sites=[q for name in sorted(visited) for q in direct.get(name,[])];results.append({'path':ep['path'],'function':ep['function'],'line':ep['line'],'possible_local_transitive_write_sites':sites,'classification':'VERIFIED','scope':'Bounded static local call-graph only. Presence is a possible write,not proof every request writes. Absence does not prove purity:dynamic aliases/external helpers/telemetry/conditions are not fully resolved. No GET request issued.'})
(E/'complete-api-inventory.json').write_text(json.dumps(data,indent=2));(E/'get-side-effect-inventory.json').write_text(json.dumps({'classification':'VERIFIED','scope':'Static possibility inventory only;not safe-to-execute permission.','GET_endpoints':results},indent=2));print('GET routes',len(results),'with possible localwritepath',sum(bool(x['possible_local_transitive_write_sites']) for x in results));print([(x['path'],sorted({q['function'] for q in x['possible_local_transitive_write_sites']})) for x in results if x['possible_local_transitive_write_sites']])
