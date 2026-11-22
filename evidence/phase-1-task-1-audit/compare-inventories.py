from pathlib import Path
import json,re,collections
E=Path(__file__).parent;front=json.loads((E/'frontend-static-inventory.json').read_text());api=json.loads((E/'api-inventory.json').read_text());review=[]
for m in front:
 for call in m['api']:
  raw=call['path'];method=call['method'].split('.')[1].upper()
  if method not in ['GET','POST','PUT','PATCH','DELETE']:continue
  if len(raw)<2 or raw[0] not in ['"',"'",'`']:continue
  path=raw[1:-1]
  if not path.startswith('/'):continue
  path=re.split(r'\?(?![^{}]*\})',path)[0]
  pattern=re.escape('/api'+path);pattern=re.sub(r'\\\$\\\{.*?\\\}',r'[^/]+',pattern)
  # Match both parameterized backend routes and concrete frontend literals.
  def matches(route):
   a=re.sub(r'\{[^}]+\}','DYNAMIC',route)
   b=re.sub(r'\$\{[^}]+\}','DYNAMIC','/api'+path)
   ar='^'+re.escape(a).replace('DYNAMIC','[^/]+')+'$';br='^'+re.escape(b).replace('DYNAMIC','[^/]+')+'$'
   return re.match(ar,b) or re.match(br,a)
  if not any(x['method']==method and matches(x['path']) for x in api):review.append({'file':m['file'],'line':call['line'],'method':method,'expression':raw,'classification':'REVIEW REQUIRED lexical mismatch;dynamic/query expression may prevent automatic match'})
(E/'api-call-review-candidates.json').write_text(json.dumps(review,indent=2));print('API lexical review candidates',len(review));print(review[:15])
# Compare source index keys/options with read-only observed metadata.
live=json.loads((E/'local-db-readonly-metadata.json').read_text());specs=json.loads((E/'index-inventory.json').read_text());actual={x['name']:x for x in live.get('collections',[])};comparison=[]
for spec in specs:
 keys=spec['keys'];keys=[(keys,1)] if isinstance(keys,str) else [tuple(x) for x in keys];options=spec['options'];matches=[]
 for ix in actual.get(spec['collection'],{}).get('indexes',[]):
  if list(ix.get('key',{}).items())==keys and all(ix.get(k,False if k in ['unique','sparse'] else None)==v for k,v in options.items() if k!='name'):matches.append(ix['name'])
 comparison.append({'collection':spec['collection'],'line':spec['line'],'matching_live_indexes':matches,'status':'VERIFIED metadata' if matches else 'REVIEW REQUIRED'})
(E/'index-metadata-comparison.json').write_text(json.dumps(comparison,indent=2));print('Index declaration matches',sum(bool(x['matching_live_indexes']) for x in comparison),'/',len(comparison));print('unmatched',[x for x in comparison if not x['matching_live_indexes']])
