from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,collections,ast,re,hashlib,subprocess
E=Path(__file__).parent;R=Path('/workspace/come-in-current');A=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115');T=datetime.now(timezone(timedelta(hours=-8))).isoformat();apis=json.loads((E/'api-inventory.json').read_text());front=json.loads((E/'frontend-static-inventory.json').read_text());models=json.loads((E/'model-inventory.json').read_text());indexes=json.loads((E/'index-inventory.json').read_text());db=json.loads((E/'local-db-readonly-metadata.json').read_text());lines=json.loads((E/'function-line-map.json').read_text());provenance=json.loads((E/'workspace-provenance.json').read_text());tests=json.loads((E/'existing-test-result-index.json').read_text());actions=json.loads((E/'button-action-inventory.json').read_text())
def loc(rel,line=1,label=None):return f'[{label or rel}](<{A/rel}:{line}>)'
def fun(name):return loc('backend/server.py',lines[name]['line'],name)
def test(rel):return loc('backend/tests/'+rel)
def jsline(rel,needle):
 for i,s in enumerate((A/rel).read_text().splitlines(),1):
  if needle in s:return i
 return 1
def mdescape(s):return str(s).replace('|','\\|').replace('\n','<br>')
intro=f'''Audit timestamp: {T} (UTC−08). **Final status: REVIEW PENDING.** Canonical Phase1/Task1=Existing Project Audit under the recovered22-task roadmap. Roadmap Recovery is preserved and is not proof that this application audit passed. No canonical task added/renamed/merged/renumbered. Task2/implementation NOT STARTED. Only files in `{E}` are created/updated. Existing source,ZIP,patches and all five checkpoints are protected unchanged.

Evidence labels: **SOURCE VERIFIED**=located in current code/document;**STATICALLY VERIFIED**=read-only parser/structural check;**TEST EVIDENCE FOUND**=persisted result with date/scope,not freshly run;**RUNTIME VERIFIED**=only the specified actual runtime observation;**EXTERNAL INTEGRATION VERIFIED**=requires real external provider evidence (none newly established);**HISTORICAL REPORT ONLY**,**NOT FOUND**,**UNVERIFIED**,**BLOCKED** retain their narrow meaning.

Allowed item statuses: VERIFIED,PARTIALLY VERIFIED,NOT IMPLEMENTED,NOT FOUND,HISTORICAL CLAIM ONLY,UNVERIFIED,BLOCKED,REVIEW REQUIRED. A VERIFIED inventory/declaration is not VERIFIED business behavior. Owner approval for audit acceptance/fixes/Task2 remains pending.

'''
findings=[
 {'id':'SEC-01','severity':'HIGH','title':'Password-reset token consumption and password update are not atomic','status':'REVIEW REQUIRED','evidence':fun('reset_password'),'detail':'The function reads a live unused token,updates users.password_hash,then marks password_resets.used in a separate update. There is no token-state compare-and-set claim or shared transaction across these operations.','impact':'Concurrent reuse or a failure between writes can permit a token to remain usable or competing resets to overwrite the password. This is a source-derived race/failure concern;no exploit or reset was attempted.','recommendation':'In a separately approved fix,use one transactional conditional token-consumption/password-update flow with expiry checks and failure recovery;add isolated concurrency/rollback tests.','test':'test_functional_blockers_regression.py; password-reset contracts in existing suites do not establish concurrent one-time consumption.'},
 {'id':'SEC-02','severity':'MEDIUM','title':'Seven-day access JWTs have no server-side session/password-version revocation','status':'REVIEW REQUIRED','evidence':fun('create_access_token')+', '+fun('get_current_user_optional')+', '+fun('reset_password'),'detail':'Tokens carry sub,role,email,type,exp;authorization reloads DB roles,which is positive,but no session ID/token version/password-changed cutoff is checked. Password reset does not revoke existing access JWTs. No logout-all/revoke endpoint found in179 registrations.','impact':'A previously obtained valid token can retain access until expiry after a password change,unless the account is removed or other checks deny it. Native/client logout alone does not revoke a copied token.','recommendation':'Agree on session-revocation policy;then add server-checked token version/session state and invalidate sessions on sensitive account changes without weakening role checks.','test':'test_frontend_contracts.py;source/session inventory;no new token test executed.'},
 {'id':'SEC-03','severity':'MEDIUM','title':'IP rate-limit identity trusts caller-supplied X-Forwarded-For','status':'REVIEW REQUIRED','evidence':fun('_client_ip')+', '+fun('_rate_keys'),'detail':'The first forwarded header value is accepted without an application trusted-proxy check. A sanitizing ingress may mitigate this,but actual ingress configuration is unavailable.','impact':'If directly reachable or behind an unsanitized proxy,IP-based registration/reset/login throttles can be evaded. Email/subject counters still provide separate protection where used.','recommendation':'Verify trusted proxy/ingress behavior;derive client identity only from trusted forwarding information and retain subject controls.','test':'Source inspection only;no spoofing requests or bypass attempts performed.'},
 {'id':'SEC-04','severity':'MEDIUM','title':'Authentication throttle check and increment are separate operations','status':'REVIEW REQUIRED','evidence':fun('_check_auth_rate_limit')+', '+fun('_record_auth_attempt')+', '+fun('login'),'detail':'A request reads counters before later $inc;concurrent requests can all pass the same limit check. Login increments only after failed verification.','impact':'Burst concurrency may exceed the intended per-window limit. No concurrency/abuse attack was run.','recommendation':'Use a reviewed atomic limiting primitive with shared worker semantics and explicit rejection policy;test only on an isolated service.','test':'Existing auth tests show basic rate behavior historically,not strict burst-cap enforcement.'},
 {'id':'SEC-05','severity':'MEDIUM','title':'Legacy diagnostic status endpoint permits anonymous persistent writes','status':'REVIEW REQUIRED','evidence':fun('create_status_check')+', '+fun('list_status_checks')+', '+loc('backend/server.py',682,'StatusCheckCreate'),'detail':'POST /api/status directly inserts client_name into status_checks without auth or endpoint rate control;client_name has no explicit length bound. GET returns up to1000 records. Global ingress controls are unverified.','impact':'Untrusted callers can create diagnostic data/storage load and retrieve the shared diagnostic feed. This is legacy behavior,not assumed to be intentional public operational policy.','recommendation':'Owner should decide whether to retire,restrict or bound this legacy endpoint;require suitable authorization/rate/size controls before production. Do not remove it during audit.','test':'Static route/body inspection;no diagnostic record created.'},
 {'id':'SEC-06','severity':'LOW','title':'Password character limits exceed bcrypt byte limit','status':'REVIEW REQUIRED','evidence':loc('backend/server.py',305,'RegisterIn')+', '+fun('hash_password')+', '+loc('backend/requirements.txt',11,'bcrypt4.1.3 pin'),'detail':'Registration permits128 characters and reset128,while hash_password passes UTF-8 directly to bcrypt4.1.3. No explicit72-byte bound or reviewed long-password handling is present.','impact':'bcrypt byte truncation/compatibility can make distinct long inputs equivalent or otherwise cause password-contract ambiguity. Exact runtime behavior was not exercised;do not report a tested credential collision.','recommendation':'Review byte-aware password policy/library behavior and provide compatible migration/tests rather than silently truncating credentials.','test':'SOURCE VERIFIED configuration mismatch;runtime UNVERIFIED;no passwords/salts/credentials created.'},
 {'id':'SEC-07','severity':'LOW','title':'Blocking provider HTTP inside async payment routes','status':'REVIEW REQUIRED','evidence':fun('create_restaurant_payment_intent')+', '+fun('verify_grocery_payment'),'detail':'Synchronous requests/http_requests calls appear in async handlers with timeouts. Real-provider latency/load behavior is not verified.','impact':'Slow provider responses can occupy the event loop and reduce availability;this is a source-level performance/availability concern,not a measured outage.','recommendation':'After approval,review bounded async HTTP or safe thread offload while keeping all provider effects outside retried DB callbacks and preserving idempotency.','test':'No provider/load test performed.'},
 {'id':'SEC-08','severity':'MEDIUM','title':'Webhook size check occurs after whole request body is buffered','status':'REVIEW REQUIRED','evidence':fun('razorpay_webhook')+', '+loc('backend/payment_webhook.py',19,'event_payload'),'detail':'The route awaits request.body(),computes HMAC,then event_payload checks1MiB. The check does not bound the earlier body read. Production ingress body-size protection is unknown.','impact':'When the provider route is configured,oversized unauthenticated bodies can consume buffering/HMAC resources before rejection. This was not load-tested and no large request was sent.','recommendation':'Review ingress caps and an endpoint streaming/body cap before full buffering,while preserving exact raw bytes for signature validation.','test':'Source inspection;test_webhook_envelope_security.py checks parser bounds,not pre-buffer transport allocation.'}
]
(E/'security-findings.json').write_text(json.dumps(findings,indent=2));security='# PHASE 1 TASK 1 — Security Findings\n\n'+intro+'''## Severity summary and review boundary

**0 CRITICAL,1 HIGH,5 MEDIUM,2 LOW findings/review items.** Findings are source-observed control gaps or risks,not successful exploits. Deployment mitigations and actual production exposure are UNVERIFIED. No attack,credential guessing,production API call or state-changing security test was performed. No fix applied. Status for every finding is REVIEW REQUIRED until owner review and approved validation/remediation.

'''
for f in findings:security+=f"## {f['id']} — {f['severity']} — {f['title']}\n\n- Status:{f['status']};evidence label:SOURCE VERIFIED control structure,STATICALLY VERIFIED inventory;runtime exploitability UNVERIFIED.\n- Affected component/evidence:{f['evidence']}.\n- Finding:{f['detail']}\n- Potential impact:{f['impact']}\n- Safe recommendation:{f['recommendation']}\n- Related tests/evidence:{f['test']}\n\n"
security+='''## Controls found and limits

- Registration assigns customer server-side;shop registration promotes only to shopkeeper,not admin. Admin endpoints declare role dependencies;shop/Restaurant/order ownership helpers are present. No direct role-escalation or IDOR exploit was attempted/proven. See API inventory for per-endpoint declared/body checks;absence of Depends alone is not a vulnerability.
- Mongo document serialization removes password_hash and internal Grocery idempotency/session fields. Public record projection removes selected internal actors. No secret values were printed or copied. Actual production response/log redaction remains unverified.
- Payment settings enforce explicit environment/key-mode consistency;server-side signatures/provider amount/currency/order checks and raw-body webhook HMAC present. Refund eligibility/admin authorization/claim/reconciliation and transactional ledger mechanisms present. Actual provider success is not established.
- General image upload checks auth,5MB bounded read and JPEG/PNG/GIF/WebP signatures before storage. Header validation is not full decoding/malware scanning. Existing25 focused/12HTTP artifacts are historical evidence,not a new run.
- Catalogue importer validates extension/MIME/magic,batch/row/ZIP expansion/ratio/path bounds. Legacy product import rejects formula-like text;universal importer preserves raw untrusted cell text for provenance,not execution;XLSX uses read_only/data_only. No live spreadsheet execution/export performed. No universal sanitization change recommended without preserving the approved untrusted-source-text contract.
- CORS production explicit-origin guard and native production HTTPS/ATS/cleartext config found. Actual ingress,TLS/HSTS,CSP,secret rotation,DB roles/firewall/backup/monitoring and infrastructure/dependency advisories remain BLOCKED/UNVERIFIED without actual environment evidence. No network vulnerability scanner/npm audit/pip audit was run.
- Local disposable metadata shows52 collections,0 MongoDB collection validators. Pydantic/input validators are present;storage-level validation is a separate REVIEW REQUIRED data-integrity gap,not grounds to mutate schemas during audit.
- Web auth storage is JavaScript-accessible AsyncStorage abstraction;native uses SecureStore. No user-controlled dangerouslySetInnerHTML path found in inspected source;the +html usage is a fixed stylesheet. This is not a complete XSS proof or production CSP audit.
''';(E/'PHASE_1_TASK_1_SECURITY_FINDINGS.md').write_text(security)
# Screen and every event binding inventory.
screen='# PHASE 1 TASK 1 — Screen, Route and Action Inventory\n\n'+intro+'''## Scope and interpretation

53 app TSX files were read/parsed:2 layouts,1 HTML document and50 page/redirect/not-found entries. Shared modules bring the parsed TS/TSX set to95;0 parser diagnostics is syntax evidence only,not a fresh semantic TypeScript check.579 JSX event bindings across app/shared source are indexed.108 literal router targets resolve to existing route/group/public-path candidates;dynamic runtime navigation remains UNVERIFIED. Zero duplicate FastAPI registrations found separately;frontend aliases/overlapping public paths need framework-aware interpretation.

Every row has SOURCE VERIFIED route/binding evidence and item status PARTIALLY VERIFIED unless it is a static layout/intentional alias. A source file or nonempty callback does not prove rendering,working business actions or all empty/error states. State columns below are lexical source markers,not UI tests. An absent marker may be handled by a child/shared component or a screen with no async operation;it is not automatically a bug. Render evidence covers only the historically exercised pages listed below.

Historical browser evidence18Nov2026:Home/CHAND entry,voice-typing navigation/focus and four mode cards (5checks);real customer/seller/Restaurant-owner/admin UI logins plus/orders,/delivery-partner,/seller/products,/seller/support,/restaurant/dashboard,/restaurant/orders,/admin,/admin-delivery-partners (12checks). Scope:web login/navigation/render only,not every control/native/provider workflow. See root evidence/resume-20261118/home-chand-browser.json and browser-roles-v2.json. These were NOT rerun. No new browser navigation/clicks were performed because arbitrary UI effects may write local/app data.

## Complete app route/layout inventory

| File / source | Logical route;public path | Kind / redirect | Events / direct API calls | Loading / empty / error markers | Render evidence / status |
|---|---|---|---|---|---|
'''
history={'/','/chand','/orders','/delivery-partner','/seller/products','/seller/support','/restaurant/dashboard','/restaurant/orders','/admin','/admin-delivery-partners'}
for x in front:
 if not x['route']:continue
 state='/'.join(str(len(x['stateMarkers'][k])) for k in ['loading','empty','error']);render='TEST EVIDENCE FOUND18Nov(web limited)' if x['publicPath'] in history else 'UNVERIFIED rendering';screen+=f"| {loc('frontend/'+x['file'])} | `{x['route']}`;`{x['publicPath']}` | {x['kind']};redirect={x['redirect']} | {len(x['actions'])}/{len(x['api'])} | {state} | {render};PARTIALLY VERIFIED |\n"
screen+='''
## Aliases, duplicates, obsolete routes and gaps

- app/index.tsx redirects to /(tabs);both normalize near the web root but represent an intentional router-group entry pattern. Runtime ambiguity is not proven by a lexical duplicate path.
- restaurant/account.tsx redirects to the shared Account/AuthProvider;restaurant/addresses.tsx to /addresses;restaurant/support.tsx to /chand?openHelp=1 with order parameters. These are intentional compatibility routes,not abandoned duplicate account/address/support implementations.
- /orders aggregates modes while /restaurant/orders provides Restaurant-specific history;separate routes are not duplicate endpoint collisions. Grocery/shop cart and Restaurant cart use separate stores.
- Legacy /request remains alongside CHAND;Home has only the approved CHAND assistant entry in prior browser evidence. Preserve the alias/operational flow rather than restoring obsolete Request Anything Home UI.
- One empty inline onPress was found:app/(tabs)/account.tsx:195 on the modal sheet container,inside an outer dismiss backdrop. This appears intentional tap containment,not an unimplemented primary action;child shop-registration controls have navigation callbacks. No fix requested/performed.
- UI-01 REVIEW REQUIRED:frontend/app/payment-methods.tsx advertises COD-only/no customer gateway while Grocery checkout and Restaurant checkout now contain gated Razorpay flow. It is a stale information screen,not evidence that checkout lacks SDK integration. Owner-approved copy reconciliation should follow,not happen in read-only audit.
- UI-02 REVIEW REQUIRED:RestaurantPage unconditionally appends a DEVELOPMENT DEMO CATALOGUE notice even around pages that can show approved live data. Sample/live flags are present and demo checkout is rejected;the blanket notice can still confuse interpretation. Source verified;real-user effect untested.
- Customer guest Grocery checkout source exists,but order history/tracking/cancel endpoints require authenticated ownership. Guest post-order self-service is not found as a dedicated guest read/cancel API;document product intent before claiming full guest lifecycle.
- Native/device render,camera/microphone/permission flows,deep-link/app-death/payment return,geolocation and actual external URLs remain BLOCKED or UNVERIFIED. No native binary/device verification is inferred from JS export.

## Per-screen API, navigation and state evidence

Full expressions,all marker line numbers and shared component tags are retained in frontend-static-inventory.json;all579 event bindings are in button-action-inventory.json. The following per-page API list preserves direct integrations;shared hooks/components can add API calls even when a page has0direct calls.

'''
for x in front:
 if not x['route']:continue
 screen+=f"### `{x['route']}` — {loc('frontend/'+x['file'])}\n\nDirect APIs:"+('; '.join(f"{q['method']} {q['path']} (line{q['line']})" for q in x['api']) or 'NOT FOUND locally;inspect shared components/hooks or static/redirect behavior')+'.\n\nNavigation:'+('; '.join(f"{q['callee']} {q['target']} (line{q['line']})" for q in x['navigation']) or 'NOT FOUND local router call;may be shared shell/Redirect/links')+'.\n\nState marker lines:'+json.dumps(x['stateMarkers'])+'. Handler count:'+str(len(x['actions']))+'. Actual working/render status remains scoped as in table.\n\n'
screen+='## Complete event/button binding index\n\nEntries include onPress and input/modal change events;only binding presence is verified. Full original handler expressions are in JSON;the table gives a readable prefix,not an execution verdict.\n\n| File:line | Event | Source handler prefix | Status |\n|---|---|---|---|\n'
for x in actions:
 handler=x['handler'];prefix=handler[:190]+('… (full JSON)' if len(handler)>190 else '');screen+=f"| {loc('frontend/'+x['file'],x['line'])} | {x['event']} | {mdescape(prefix)} | SOURCE VERIFIED binding;runtime UNVERIFIED |\n"
(E/'PHASE_1_TASK_1_SCREEN_AND_ROUTE_INVENTORY.md').write_text(screen)
# API/database full inventory.
ad='# PHASE 1 TASK 1 — API and Database Inventory\n\n'+intro+f'''## Architecture and extraction

FastAPI APIRouter /api is declared in backend/server.py with{len(apis)}HTTP registrations and{len(models)}Pydantic input/model classes. All decorators/signatures/dependency expressions,body authorization markers,collections and response_model declarations were extracted without importing/running the application. See api-inventory.json,model-inventory.json,function-line-map.json. Other Python modules supply pricing/refunds/transactions/providers;their presence does not create a separate server architecture.

0 duplicate method+path registrations found. Many endpoints use plain dictionaries rather than explicit response_model;this is a contract-review/typing risk,not proof of inconsistent runtime responses. Route rows distinguish public read/auth/provider routes from authenticated/role-protected operations. Internal helper checks must still be reviewed;Depends absence alone is not a vulnerability.

## Full endpoint inventory

| Method / path | Handler / source | Declared/body authentication | Schemas | Collections | Response declaration |
|---|---|---|---|---|---|
'''
for x in apis:ad+=f"| {x['method']} `{x['path']}` | {fun(x['function'])} | {mdescape(x['authorization']+';'+', '.join(x['dependencies']))} | {mdescape(json.dumps(x['schemas']))} | {', '.join(x['collections']) or 'none direct'} | {mdescape(json.dumps(x['response']))} |\n"
ad+='''
## Permission and contract review

- require_role declares50 endpoints;96 declare get_current_user;3 declare optional auth. Additional Grocery quote/order and public request handlers call optional auth in the body. Auth/reset endpoints are intentionally public with rate controls. Razorpay webhook is public but requires valid raw-body HMAC and configuration. No blanket “all public routes vulnerable” claim.
- _assert_shop_owner checks both current role and ownership;Restaurant helpers check owner/eligible seller record;_tracking_can_read resolves customer/shop/Restaurant/admin ownership;delivery access requires an APPROVED application. Profile update schema does not include role;shop creation assigns pending/online=false and server-side shopkeeper promotion only.
- Guest Grocery create uses scope/header quote+idempotency;server re-resolves prices/variants/stock. Owner-authenticated history/cancel/tracking is separate;guest post-order management remains REVIEW REQUIRED.
- Missing dedicated APIs identified by inventory:server session revocation/logout-all,push token registration/refresh,delivery job assignment/dashboard completion,and post-placement replacement workflow. Some are intentionally gated/not in approved current scope;do not invent endpoints or infer implementation from frontend cart replacement.
- 6 lexical API-call mismatch candidates were manually resolved as query suffix/template construction (earnings and Restaurant listing/menu). Matching base endpoints exist;they are not6missing APIs. Dynamic expressions beyond literal resolution remain UNVERIFIED. No stale assertion changed.
- API-01 REVIEW REQUIRED:plain dict request/response paths need operation-specific schema/response-contract review;mode-specific states (Grocery pending vsRestaurant placed,etc.) must not be incorrectly unified. No runtime response fuzzing performed.

## Database architecture and read-only observation

Target was the previously identified LOCAL disposable `comein_disposable_test_onboarding` on127.0.0.1:27018/rs0,not production. Executed ONLY hello,listCollections,listIndexes after verifying rs0/loopback hosts. No application document values read,no insert/update/delete/createIndex/schema command,no transactions executed. No health/init helper imported (those helpers can write transaction probes).

Fresh RUNTIME VERIFIED(metadata only):PRIMARY=true,52collections,119total indexes including52_id;all67source declarations matched keys/options,27unique declarations.0collection-level validators observed.51distinct literal db.<collection> references exist in source;one additional observed collection does not prove deadness or a defect. Pydantic/application validation is distinct from collection validators. Metadata does not prove all existing data satisfies references/uniqueness semantics beyond current indexes.

## Collection inventory (no records read)

| Collection | Live index count | Collection validator | Source reference |
|---|---:|---|---|
'''
cols=set(json.loads((E/'collection-source-inventory.json').read_text()))
for x in db.get('collections',[]):ad+=f"| `{x['name']}` | {len(x['indexes'])} | {'present' if x['validator_present'] else 'NOT FOUND'} | {'SOURCE VERIFIED literal reference' if x['name'] in cols else 'not a literal server db reference;REVIEW REQUIRED provenance'} |\n"
ad+='\n## Complete source index declaration inventory\n\n| Collection | Source | Keys | Options | Observation |\n|---|---|---|---|---|\n'
for ix in indexes:ad+=f"| {ix['collection']} | {loc('backend/server.py',ix['line'])} | {mdescape(json.dumps(ix['keys']))} | {mdescape(json.dumps(ix['options']))} | VERIFIED metadata match |\n"
ad+='\n## Pydantic model inventory\n\nAll60class field types/constraints and declared validator names are preserved in model-inventory.json. No current database-schema migration was inferred from these input types.\n\n| Model | Source | Fields | Declared validators |\n|---|---|---|---|\n'
for m in models:ad+=f"| {m['name']} | {loc('backend/server.py',m['line'])} | {', '.join(x['name']+':'+x['type'] for x in m['fields'])} | {', '.join(m['validators']) or 'none in this class'} |\n"
ad+='''
## Relationships, transactions and consistency

Logical refs include products.shop_id→shops,orders.customer_id/shop_id/items product/variant IDs;grocery_quotes scope/token→orders;grocery_payments/restaurant_payments order_id+gateway order/payment IDs;restaurant_orders restaurant/customer/owner refs;support tickets linked order/kind/customer;notifications user_id;delivery applications user/referrer/admin records;financial ledger scoped order/refund/event idempotency keys. MongoDB does not supply relational foreign keys here;helper lookups/ownership checks/transactions enforce application relationships. No orphan/PII records scanned in this audit.

run_transaction in backend/mongo_transactions.py wraps session-bound DB callbacks,driver transient retry and bounded UnknownTransactionCommitResult commit retry;callbacks must exclude provider side effects. Grocery order/stock/quote/reward and payment/order/refund/ledger paths use transactions and conditional statuses. Provider intent/refund I/O is outside retried callbacks. Separate creating/uncertain financial claims fail closed and require reconciliation;do not clear them to force a retry. Existing receipt-after-processing and reference idempotency protect duplicate/delayed provider callbacks. Historical local fault/stock/payment/refund tests exist;no fresh transaction mutation was allowed.

Remaining integrity reviews:SEC-01 reset cross-record writes not transactional;no collection validators on observed local DB;not all API write workflows share a transaction (e.g.shop creation/role promotion are separate writes);database foreign-reference/orphan correctness not freshly tested. Persistent schema/transaction changes need separate approval.

Backup scripts use timestamped protected archives/config file instead of secret URI in command argv;restore refuses unsafe overwrite/target behavior as documented. Prior isolated51-collection restore drill/fault-auth-TLS reports found;not rerun. No production backup schedule/retention/RPO/RTO/DB user grant/TLS cert/firewall access is available. Production DB audit is BLOCKED;local development no-auth loopback setup must not be treated as production policy.
''';(E/'PHASE_1_TASK_1_API_AND_DATABASE_INVENTORY.md').write_text(ad)
# Gap register.
gaps=[
 ('G-01','BLOCKED','Native Android/iOS runtime','No compiler/SDK/adb/emulator/macOS/Xcode/CocoaPods/devices;prior native commands blocked. JS exports/autolink are not binaries.','Native reports and runtime-dependency-inventory.json','Owner/developer supplies native host/devices;no install/config change authorized in audit.'),
 ('G-02','BLOCKED','Actual payment/refund/webhook','Provider configuration/delivery unverified;prior presence audit0bindings/no Razorpay egress. Source/local tests are not real TEST provider evidence.','payment modules;root EXTERNAL_VALIDATION_REPORT.md','Secure TEST setup and explicit separately scoped provider verification;never use production money.'),
 ('G-03','BLOCKED','Actual production configuration/security','No authorized production target/access,secret bindings,ingress,CORS,DB TLS/roles,backup schedule/log policy evidence.','mongo_config.py;security_config.py;deployment docs','Owner supplies read-only infrastructure evidence;no production mutation.'),
 ('G-04','NOT IMPLEMENTED','Full delivery-partner provider/assignment lifecycle','Onboarding/admin/access exists,but OTP/Aadhaar/PAN/document providers return ADAPTER_PENDING;no complete delivery-job assignment API/dashboard found.','server.py delivery_partner_provider_status/access;integrations/delivery_provider.py','Provider/business integration and approved delivery workflow;do not fabricate verified identity/rider/ETA.'),
 ('G-05','PARTIALLY VERIFIED','CHAND AI/STT/vision','Source/server routes and browser entry/planner tests found;actual AI/STT/vision config/provider/network/device media not verified.','assistant_health;frontend/app/chand.tsx','Secure nonproduction provider and devices after scope approval.'),
 ('G-06','PARTIALLY VERIFIED','Push/SMTP/object storage','In-app notifications/API exist;push provider is deliberately not_sent/not_configured;SMTP/object-store external delivery/upload not verified.','_notify;order_notifications.py;_send_password_reset_email;put_object','Provider setup/testing separately;no delivery success claim from variable presence.'),
 ('G-07','REVIEW REQUIRED','Guest Grocery after-order lifecycle','Guest quote/create allowed;mine/detail/tracking/cancel require authenticated ownership. No guest read/cancel scope route found.','create_grocery_quote/create_order/my_orders/get_grocery_order_details','Document intended guest history/help/cancel behavior before implementation.'),
 ('G-08','PARTIALLY VERIFIED','Replacement scope conflict','Cart same-shop/category fixed-pack replacement exists;measured replacement excluded. No post-placement paid-order replacement route found;historical Task25 incomplete vscanonical tracker completed.','cart.tsx replaceLine;API inventory;recovery report','Owner resolves scope/acceptance;do not merge numbering or invent refund policy.'),
 ('G-09','REVIEW REQUIRED','Stale informational UI','Payment methods screen still says online checkout absent;Restaurant shared page shows blanket sample-data notice.','frontend/app/payment-methods.tsx;src/restaurant/RestaurantPage.tsx','Owner approves narrowly scoped copy review later;no UI change now.'),
 ('G-10','REVIEW REQUIRED','Security source gaps','8security findings:reset atomicity,session revoke,proxy/rate/public diagnostic controls,bcrypt boundary,blocking providerHTTP,webhook buffer cap.','PHASE_1_TASK_1_SECURITY_FINDINGS.md','Prioritize HIGH first;approve isolated tests/fixes separately.'),
 ('G-11','REVIEW REQUIRED','Storage validation/reference coverage','0collection validators observed;refs enforced in application,no live orphan/data-quality scan performed.','local-db-readonly-metadata.json;source schemas/indexes','Review production-like schema/data safely;no schema mutation during audit.'),
 ('G-12','UNVERIFIED','Full per-screen/button runtime','All53 appfiles/579events indexed;historical browser covers17checks only. No fresh form/order/localStorage/DB mutation allowed.','screen inventory;historical browser JSON','Dedicated disposable runtime acceptance after owner review;do not label bindings working.'),
 ('G-13','BLOCKED','Optional imports/OCR in project venv','pypdf/openpyxl/Pillow/PyMuPDF absent in app venv though some exist in host Python;4historical tests skipped.','runtime-dependency-inventory.json;FINAL_REGRESSION_REPORT.md','Owner defines feature scope and approves dependency setup;do not install here.'),
 ('G-14','REVIEW REQUIRED','Historical lint/type/dependency quality','HistoricalTypeScript0/ESLint0errors10warnings retained;9hooks+generated directive need scoped follow-up. pydantic range is broad,dependency advisory audit not executed.','frontend package/yarn.lock;backend requirements;existing lint JSON','No framework upgrade/suppression;approved narrow quality/security review later.'),
 ('G-15','UNVERIFIED','Remote main/source authority','Current extracted tree differs from uploaded ZIP62existing members;extra source is persisted in cumulative patch. Remote main not fetched;only local origin/HEAD checked.','workspace-provenance.json;git-history.txt','Owner review current source/patch;do not checkout/reset or assume remote latest.'),
 ('G-16','UNVERIFIED','Remaining operations/history edge cases','HomeServices fee/provider appointments,earnings/manual settlements/referrals and all error/permission branches source-present;not fully runtime audited here.','fullAPI inventory;models;historical current live suites','Use owner-approved disposable test matrix,not real users/payments.'),
]
gap='# PHASE 1 TASK 1 — Gap and Blocker Register\n\n'+intro+'| ID | Status | Area | Observed gap | Evidence | Safe next step / approval |\n|---|---|---|---|---|---|\n'
for row in gaps:gap+='| '+' | '.join(mdescape(x) for x in row)+' |\n'
gap+='\nAll next steps are recommendations only. No fix/install/provider activation/Task2 authorized or started. Existing external-validation acceptance gates remain blocked;this audit is not production approval.\n';(E/'PHASE_1_TASK_1_GAP_AND_BLOCKER_REGISTER.md').write_text(gap)
# Master report.
master='# PHASE 1 TASK 1 — Master Existing Project Audit\n\n'+intro+f'''## Executive summary

**REVIEW PENDING — inventory/source investigation completed for owner review;whole-application runtime/security acceptance is NOT claimed.** Reviewed95frontend TS/TSX modules,53app route/layout files,579JSX event bindings,108literal navigation targets,179API registrations,60Pydantic models,67index declarations and51source collection references. Fresh read-only local Mongo metadata:52collections/119indexes,all67declarations matched,0collection validators. No application records read or database writes.0application tests,provider calls,UI clicks/builds/install/config changes performed. Existing39JUnit result artifacts indexed as historical evidence.

Security review records1HIGH,5MEDIUM,2LOW items,all REVIEW REQUIRED,no exploit or fix. Source and persisted test artifacts show substantial shopping/Restaurant/admin/provider-boundary work;actual native devices,provider deliveries and production configuration remain BLOCKED/UNVERIFIED.

## Workspace, Git, ZIP and preservation

Cwd/workspace `/workspace`;repository `{R}`,origin GitHub asliabshk-sys/come-in-current,branch work,HEAD `{provenance['head']}`. App is extracted at `{A}`,outside Git. Suggested/workspaces path is not active. Local Git tracks README+source ZIP,not the complete current app diff.62archived members differ in current tree;new files/continuation changes also exist and are captured in patches/continuation.patch. A differing timestamp/name is not a remote-authority proof. Remote main was not fetched,so latest remote comparison is UNVERIFIED. No checkout/reset/rebase/clean/restore/commit/push performed.

Available master ZIP:5,484,042bytes,SHA256 `{provenance['zip_sha256']}`,read-onlyCRC PASS. Original Roadmap Recovery SHA256 preserved as baseline;canonical roadmap defines22 tasks. Existing five checkpoints,all inherited report/history/source/ZIP/patch files were hash-protected and are not edited. Current audit checkpoint is AUDIT_PROGRESS.md inside this new evidence folder to respect latest preservation/no-overwrite instruction. Before/after Git status and hashes are retained;the only expected new Git addition is this audit folder.

## Architecture and project structure

ReactNative0.88/Expo58/React19 with Expo Router and TypeScript;one root AuthProvider,CartProvider,LocationProvider,I18nProvider,ReactQuery provider,ErrorBoundary. Shopping bottom tabs Home/Categories/Search/Cart/Account;Restaurant mode uses its own shell/theme/navigation and separate cart storage,reusing account/address/support aliases. Static demo and live catalog paths coexist with data labels/checkout guards. CHAND remains the sole approved Home shopping-assistant entry;legacy request/support compatibility routes remain.

Backend FastAPI0.110.1 single large server.py with /api router and helper modules for pricing,serviceability,financial/refund rules,Mongo config/transactions,catalogue import,CHAND/provider adapters. Pydantic2 field validators and explicit role/ownership helpers are present. The monolithic module and shared helpers are coupling/maintainability observations,not permission for refactor. Historical storage comment says local disk but current put/get object helpers use an external object-store boundary;documentation should be reviewed,not automatically rewritten.

MongoDB is document-oriented with application-level references,unique/TTL/partial indexes and transactions. app startup validates config/topology/indexes;some startup/health helpers perform writes and were deliberately not invoked. Actual production database has not been identified/accessed.

## Frontend and UI findings

See complete screen/action inventory. File existence or AST parse is not render/interaction proof. All108literal router target candidates matched;dynamic paths and all error/permission branches remain unverified. Four intentional redirect/compatibility pages and overlapping mode histories are not automatically dead duplicate routes. One empty modal-sheet event callback is intentional container behavior;not a missing primary button.

Historical limited browser evidence18Nov showsHome/CHAND/voice typing/mode cards plus customer/seller/Restaurant-owner/admin login/navigation/render. No current route clicks were performed due potential implicit storage/API mutations. Loading/empty/error lexical markers were recorded per file;missing local markers can be inherited and require component-aware runtime review. Stale payment-method information and blanket Restaurant demo footer are review findings(UI-01/UI-02),not fixed. Native permissions,deep links,screen crashes/media/native payment lifecycle remain BLOCKED.

## Backend/API findings

179route registrations parsed,0duplicate method/path pairs;per-route dependency/body-auth/model/collection evidence is linked.96auth and50role-dependency registrations are source-observed,not a statement that every branch is safe. Public reads/auth entries/provider webhook/guest operations were manually distinguished;no Depends does not automatically mean missing permission. Legacy diagnostic/status persistence is SEC-05. No general current IDOR or admin escalation exploit is claimed.

Role/input/ownership and authoritative quote/stock/payment checks are present. Many responses and some requests use untyped dictionaries;schema completeness and error contract consistency remain REVIEW REQUIRED. Six initially unmatched frontend call expressions were query-template cases with existing base endpoints. Missing/not-complete lifecycle APIs are logged in gap register,not invented. Grocery/Restaurant state names and cart/order/payment collections remain intentionally separate.

## Database findings

Read-only observation verified rs0PRIMARY and52collection metadata entries;67source index definitions(27unique) matched live keys/options.119live indexes include52_id indexes.0collection validators observed;Pydantic constraints are not persistent collection validation. No documents/PII/balances/stock values were read and no DB write/schema/index operation performed. No orphan scan,recovery drill or transaction probe was executed;those need approved isolated mutation scopes.

run_transaction includes driver transient/unknown-commit retry handling;stock/order/quote/payment/refund/ledger paths use sessions/idempotency/CAS. Existing local tests substantiate particular historical scenarios,not all current data/production behavior. Password-reset cross-record atomicity remains a HIGH source review finding. Provider effects must stay outside retried DB callbacks. Backup/restore scripts and historical disposable drill exist;production retention/RPO/RTO/access/TLS/security evidence remains BLOCKED.

## Authentication and permission findings

Bcrypt password hashing,BearerHS256 JWT with7-dayexpiry,DB-backed role lookup,server-assigned customer registration,shopkeeper promotion only,owner-scoped shop/Restaurant/order/address routes and admin require_role checks present. Password hash/internal Grocery scope fields removed from serialized docs. Native tokens useSecureStore;web storage is JS-accessible AsyncStorage abstraction. Delivery-partner access uses approved application status rather than blindly trusting a frontend role label.

Password reset hashes one-time tokens and uses expiry/generic forgot response,but token consumption/user update are separate writes. No session-version/password cutoff/logout-all endpoint found. Trusted forwarded-IP and throttle atomicity need review. Password byte limits vsbcrypt compatibility not tested. No account/role/token modifications made.

## Customer workflow map (source vsruntime)

| Workflow | Source path / symbols | Evidence / audited status |
|---|---|---|
| Register/login/profile | app/auth.tsx;store/auth.tsx;register/login/me/update_me | SOURCE VERIFIED;historical live/browser found;PARTIALLY VERIFIED current/full lifecycle |
| Browse online/offline shops/catalog | shops.tsx,shop/[id].tsx,category/[slug].tsx,useCatalogProducts,list_shops/list_catalog_products | Source/API present;historical live lists;data freshness/current button behavior UNVERIFIED |
| Search/variants/measure | tabs/search.tsx,product/[id].tsx,measure.ts,ProductVariantIn/MeasureIn,_resolve_grocery_lines | Static source+existing tests;no fresh scenario execution |
| Cart/remove/quantity/BuyNow | store/cart.tsx,tabs/cart.tsx,checkout.tsx | Separate persistent/cart-key/BuyNow source;legacy+measured pack constraints;runtime replay not run |
| Quote/checkout/COD/manual UPI/pickup | create_grocery_quote/create_order,_quote_totals,_cancel_grocery_order | Guest/auth scope,price/stock revalidation,quote expiry/idempotency found;historical70live;current business write not executed |
| Online Grocery payment | payment config,intent,verify,GroceryOnlinePayment/native adapter | Source/local tests found;actual provider/native BLOCKED |
| Orders/tracking/help/cancel | orders.tsx,order-tracking.tsx,CHAND shared help,_tracking_can_read | Prior browser/runtime fragments found;GPS provider not configured;guest follow-up gap;PARTIALLY VERIFIED |
| Repeat order | orders.tsx current-catalog aggregation | Source/historical Task24 tests found;no new cart mutation |
| Out-of-stock replacement | tabs/cart.tsx,store/cart.tsx replaceLine | Pre-checkout same-shop/category pack replacement source;measured/post-placement replacement not full implementation |
| Refund status | _refund_summary,orders.tsx,admin Grocery refund routes | Source/local mocked+Mongo evidence;actual provider settlement BLOCKED |

## Seller,Restaurant,Admin,Delivery and HomeServices workflow map

- Seller:authenticated shop application pending approval,admin approval,own product/price/stock/import/orders/earnings/support flows;some owner/role/inventory contracts historically tested. Current submission/import/order mutations not executed. Manual financial operations are distinct from provider-settled payments.
- Restaurant:live approved listing/menu/serviceability alongside explicit samples,separate food cart,delivery/pickup/shared addresses,order creation/status/dashboard/support/cancel,gated Razorpay backend/UI and existing refund policy. Historical source/API/browser evidence exists;device/provider/actual coverage data remains unverified.
- Admin:shop/Restaurant/HomeServices/delivery application approvals,orders/support/announcements/financial views/settlements/referrals and refund controls. API dependency coverage present;all admin buttons/error branches not runtime-tested here. Grocery refund admin API exists;no full current admin-UI end-to-end initiation/settlement claim.
- Delivery:encrypted personal application fields,consents,admin status/audit records andAPPROVED access gate present. OTP/Aadhaar/PAN/document adapters explicitly pending;no fake verification bypass. Complete job assignment/live rider/provider location unavailable. Identity data was not read.
- HomeServices:/services route and backend provider list/profile/photo,admin approval,fee policy,appointments/provider-customer status paths exist. It is more than a tile,but external scheduling/operational capacity/cash handling/device/runtime edge cases are not verified. Do not invent a second service route or redesign the tile.

## Security findings

See dedicated eight-item register:1HIGH,5MEDIUM,2LOW. SOURCE VERIFIED risk structures,not exploitation success. HIGH=non-atomic reset token/password update. MEDIUM=session revocation gap,untrustedXFF,non-atomic throttle,anonymous diagnostic persistence,webhook pre-buffer cap. LOW=password byte-boundary/library policy and blocking syncHTTP in async payment paths. All REVIEW REQUIRED;no source fix. Production security remains BLOCKED,not approved because old tests passed.

## Integration inventory

| Integration | Source present | Configuration | Existing offline/local evidence | Runtime evidence | External provider verified | Status |
|---|---|---|---|---|---|---|
| MongoDB | config/transactions/index/backup tools | Known isolated local target;production UNVERIFIED | Existing67index/stock/retry/restore artifacts | Fresh read-only52collections/67declarations matched;prior live transactions | Production provider/roles/TLS UNVERIFIED | PARTIALLY VERIFIED |
| CHAND/planner/STT/vision | screen,assistant routes,provider selection,party planner | Current secret values not read;prior audit absent | Planner11,CHAND/media contracts historical | Home entry/typing browser historical | NOT FOUND real provider evidence | BLOCKED external |
| Razorpay/web/native | mode guard,intents,verification,web/native SDK3.0.0 | Current binding access not attempted;prior credentials/egress absent | Historical78focused,7affected,5native mock | LocalMongo/mock HTTP historical;JS exports/autolink historical | NOT FOUND actualTEST payment/delivery/settlement | BLOCKED external/native |
| Refunds | Grocery full-only admin;Restaurant original policy;webhooks/ledger | Requires corresponding provider and eligible payment | Mock-provider+localMongo/history/rollback evidence | Historical local only | NOT FOUND actual settlement | BLOCKED actual |
| In-app notifications | _notify and scoped read/read-all/unread | Internal persistence source | Existing offline/live fragments | Historical local/live | Push provider unconfigured/default not_sent | PARTIALLY VERIFIED;pushBLOCKED |
| SMTP/reset | send-email boundary,generic public response | Current secrets not read;prior absent | Existing source contracts | NOT FOUND real email delivery | NOT FOUND | BLOCKED external |
| Images/files | authenticated/bounded/signature upload,object proxy | Existing source config names;prior object key absent | Historical25upload/12HTTP | No fresh provider upload | NOT FOUND | PARTIALLY VERIFIED source;externalBLOCKED |
| CSV/XLSX/universal import | validate/extract/stage/approve/transactional apply | Optional deps missing in app venv;CSV source works historically | Existing parser/rollback/CHAND provenance tests | Historical live isolated apply/rollback | No external price-feed verification | PARTIALLY VERIFIED |
| Delivery identity/tracking | app/admin/access and fail-closed adapters | ADAPTER_PENDING | Offline boundaries/ownership evidence | No actual rider/device/provider | NOT FOUND | BLOCKED |
| HomeServices/Restaurant operations | backend+UI+data adapters | Merchant/coverage/provider data currentvalues not read | Existing regression sources/artifacts | Limited historical local flows | External operations not verified | PARTIALLY VERIFIED |
| Stripe/retailer live feeds | Generic payment labels/reference comparison data only | No verified provider binding | No verified full active Stripe/live retailer flow | NOT FOUND | NOT FOUND | NOT IMPLEMENTED/UNVERIFIED scope;do not activate |

## Existing tests vsfresh checks

Found39persisted JUnit artifacts plus browser/native/build/lint/TypeScript/report evidence. Historical latest broad558PASS6SKIP,70livePASS,78focusedPASS,25upload+12HTTP,17browserchecks,TypeScript0/ESLint0errors10warnings retained as historical only. Four optional document/OCR skips remain missing in app venv;host Python packages do not make app venv adapters available. No pytest,semantic typecheck,ESLint,web/native build,browser click,credential creation,provider call or DB mutation executed now.

Fresh safe checks:ZIP CRC/hash+workspace file comparison,AST structure/source syntax parsing (Python read/parse and95TS/TSX parse0diagnostics),literal route/index metadata comparison,and local DB hello/listCollections/listIndexes. These are NOT a new558-test pass,not end-to-end proof,and not production validation. Exact tools/commands/artifacts are retained in this folder.

## Limitations,approval and completion gate

All static inventoried routes/actions/API/models/indexes are exposed for review,but not every runtime branch/button/business operation has passing current evidence. Read-only constraint prevents registration/order/refund/upload/import/app-state writes and unknown side-effect UI actions. Actual provider/native/production resources are absent/unverified;no guesses substituted. Dependency advisories,full XSS/IDOR fuzzing,load abuse,DB record integrity and all device/operational paths remain unverified or blocked. FulloriginalTask1 evidence is sufficient for OWNER REVIEW of findings/inventories/limitations,not unconditional acceptance or production readiness. Final status **REVIEW PENDING** until owner personally reviews/approves. Do not start Task2 or fixes.
''';(E/'PHASE_1_TASK_1_MASTER_AUDIT_REPORT.md').write_text(master)
# Full acceptance matrix,including user's granular audit request.
checklist='# PHASE 1 TASK 1 — Final Checklist\n\n'+intro+'| Requirement | Evidence | Status | Remaining action | Approval status |\n|---|---|---|---|---|\n'
items=[
 ('Original:current app/screens/navigation/frontend/backend/API/database/auth inspection','Master + fullscreen/API/DB inventories','PARTIALLY VERIFIED','Owner reviews source/runtime scope;fullruntime not proved'),
 ('Original:which buttons/workflows really work','579bindings +17historical browserchecks + workflow tables','PARTIALLY VERIFIED','Disposable behavior tests for unexercised controls;no sourceexistence=working claim'),
 ('Original:Grocery,online/offline shops,Restaurants,HomeServices features','Master workflow maps;services+Restaurant+catalog APIs','PARTIALLY VERIFIED','Verify current merchant/provider/operational scenarios'),
 ('Original:duplicates/errors/incomplete work','0duplicateAPI;intentional aliases;UI-01/UI-02;gap register','PARTIALLY VERIFIED','Review dynamic routes/allUI branch behavior'),
 ('Original:read-only first,no fixes without approval','Protected hashes,Git before/after;AUDIT_PROGRESS','VERIFIED','Maintain preservation;fixesnotstarted'),
 ('Workspace/branch/HEAD/Git modified/untracked/ignored','workspace-provenance;git-status-before/after/ignored','VERIFIED','Remote latest stillUNVERIFIED'),
 ('Checkpoint/handover/roadmap/recovery inventory and preservation','existing-document-inventory;protected hashes','VERIFIED','No existing checkpoint change'),
 ('Master ZIP CRC/hash and workspace/ZIP differences','workspace-provenance.json;62differences','VERIFIED','Do not confuse snapshot with current remote/source'),
 ('Architecture/routes/models/service boundaries','Master;179APIs/60models/95modules','VERIFIED','Static inventory only;coupling is not refactor authorization'),
 ('Every screen route/render/action/API/loading-empty-error/nav','Complete screen report + JSON','PARTIALLY VERIFIED','Render/allbutton runtime mostlyUNVERIFIED'),
 ('APIrequest/response/dependencies/roles/validation/errors','API/model inventory;security findings','PARTIALLY VERIFIED','Plain dict contracts/error branches require approved tests'),
 ('Order/product/stock/seller/admin/import/payment/refund/notifications','Master maps/API inventory;historical resultindex','PARTIALLY VERIFIED','No current statechanging operations'),
 ('Database collections/indexes/unique/ref/transactions/validation','52metadata/67matched/27unique;sourcehelpers','PARTIALLY VERIFIED','No data scan/transaction write;0validators review'),
 ('Backup/restore and production DB security','scripts+historical drill;securityreport','BLOCKED','Need actualproduction grants/TLS/retention/recovery evidence'),
 ('Authregistration/login/password/token/reset/session/roles','8security findings;sourcefunctions','PARTIALLY VERIFIED','Highresetatomicity andsessions require review'),
 ('Customer browse/search/cart/variants/checkout/COD/order/help/cancel/repeat/replacement/refund','Mastercustomer table;API/screens','PARTIALLY VERIFIED','Guestlifecycle/replacement/provider/devicegaps'),
 ('Sellerregistration/approval/product/price/stock/order/adminaudit','Masteroperations table;APIdependency coverage','PARTIALLY VERIFIED','Actualworkflow mutations notperformed'),
 ('Restaurantmenu/orders/cart/themes/refunds/modeisolation','MasterRestaurantmap;stores/shell/routes','PARTIALLY VERIFIED','Native/provider/coverage lifecycle blocked'),
 ('Delivery onboarding/approval/assignment/status/provider','Deliverysource+gapG04','BLOCKED','Adapters/identity/jobassignment missing orblocked'),
 ('SecurityIDOR/roles/rate/CORS/secrets/uploads/formulas/prices/refunds/session/logs/DB/dependencies','Securityreport8items;sourceevidence','PARTIALLY VERIFIED','Productioncontrols/exploitability/dependency advisoryscan unverified'),
 ('Integration source/config/offline/runtime/provider classification','Masterintegration table','PARTIALLY VERIFIED','External provider evidence notfound;do not promote mocks'),
 ('Testconfiguration/safety andexistingvsfreshscope','Tests notexecuted;onlysafeparsers/metadata','VERIFIED','No dangerous suite authorized;do notrunhealth/init'),
 ('Seven requiredreports/manifest anddurable auditcheckpoint','Thisfolder7namedreports +AUDIT_PROGRESS','VERIFIED','Owner reviewscontent;creationdoesnotcomplete acceptance'),
 ('Noapplication/source/UI/API/config/dependency/DB/Githistory modifications','Finalhash/statusverification','VERIFIED','Existing checkpoints/ZIP/patch unchanged'),
 ('FinalstatusREVIEWPENDING;Task2/fixesnotstarted','Master/checklist/AUDIT_PROGRESS','REVIEW REQUIRED','Wait for explicitowner approval'),
]
for name,ev,status,next in items:checklist+=f'| {name} | {ev} | {status} | {next} | Audit authorized;acceptance/fix/Task2 approval PENDING |\n'
checklist+='\nNo blanket Task1 COMPLETE declaration. Enough bounded audit evidence is available for owner review;unexecuted runtime/production/provider checks remain documented. Existing five canonical checkpoints are preserved byte-for-byte;the current durable progress/resume instruction is in AUDIT_PROGRESS.md here.\n';(E/'PHASE_1_TASK_1_FINAL_CHECKLIST.md').write_text(checklist)
# Append meaningful new audit checkpoint only,do not mutate inherited trackers.
with (E/'AUDIT_PROGRESS.md').open('a') as f:f.write(f'\n{T}:Six required Markdown reports saved with53routes/layouts,579bindings,179API/60models,67index/52livecollection metadata inventories,eight source security review items and16gap rows. No fixes/tests/builds/provider calls/DBwrites/source changes. Next:verify every report link/hash and protection baseline,write manifest. FinalstatusREVIEWPENDING;Task2notstarted.\n')
print('Saved six required Markdown reports;security1HIGH/5MEDIUM/2LOW;final REVIEW PENDING.')
