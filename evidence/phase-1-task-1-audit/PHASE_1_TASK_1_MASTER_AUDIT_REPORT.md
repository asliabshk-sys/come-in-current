# PHASE 1 TASK 1 — Master Existing Project Audit

Audit timestamp: 2026-11-18T06:59:35.322181-08:00 (UTC−08). **Final status: REVIEW PENDING.** Canonical Phase1/Task1=Existing Project Audit under the recovered22-task roadmap. Roadmap Recovery is preserved and is not proof that this application audit passed. No canonical task added/renamed/merged/renumbered. Task2/implementation NOT STARTED. Only files in `/workspace/come-in-current/evidence/phase-1-task-1-audit` are created/updated. Existing source,ZIP,patches and all five checkpoints are protected unchanged.

Evidence labels: **SOURCE VERIFIED**=located in current code/document;**STATICALLY VERIFIED**=read-only parser/structural check;**TEST EVIDENCE FOUND**=persisted result with date/scope,not freshly run;**RUNTIME VERIFIED**=only the specified actual runtime observation;**EXTERNAL INTEGRATION VERIFIED**=requires real external provider evidence (none newly established);**HISTORICAL REPORT ONLY**,**NOT FOUND**,**UNVERIFIED**,**BLOCKED** retain their narrow meaning.

Allowed item statuses: VERIFIED,PARTIALLY VERIFIED,NOT IMPLEMENTED,NOT FOUND,HISTORICAL CLAIM ONLY,UNVERIFIED,BLOCKED,REVIEW REQUIRED. A VERIFIED inventory/declaration is not VERIFIED business behavior. Owner approval for audit acceptance/fixes/Task2 remains pending.

## Executive summary

**REVIEW PENDING — inventory/source investigation completed for owner review;whole-application runtime/security acceptance is NOT claimed.** Reviewed95frontend TS/TSX modules,53app route/layout files,579JSX event bindings,108literal navigation targets,179API registrations,60Pydantic models,67index declarations and51source collection references. Fresh read-only local Mongo metadata:52collections/119indexes,all67declarations matched,0collection validators. No application records read or database writes.0application tests,provider calls,UI clicks/builds/install/config changes performed. Existing39JUnit result artifacts indexed as historical evidence.

Security review records1HIGH,5MEDIUM,2LOW items,all REVIEW REQUIRED,no exploit or fix. Source and persisted test artifacts show substantial shopping/Restaurant/admin/provider-boundary work;actual native devices,provider deliveries and production configuration remain BLOCKED/UNVERIFIED.

## Workspace, Git, ZIP and preservation

Cwd/workspace `/workspace`;repository `/workspace/come-in-current`,origin GitHub asliabshk-sys/come-in-current,branch work,HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. App is extracted at `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`,outside Git. Suggested/workspaces path is not active. Local Git tracks README+source ZIP,not the complete current app diff.62archived members differ in current tree;new files/continuation changes also exist and are captured in patches/continuation.patch. A differing timestamp/name is not a remote-authority proof. Remote main was not fetched,so latest remote comparison is UNVERIFIED. No checkout/reset/rebase/clean/restore/commit/push performed.

Available master ZIP:5,484,042bytes,SHA256 `3233dcd9c8f1997b06035fd5cd7b458ab511658faf25e184044b17aec624d28c`,read-onlyCRC PASS. Original Roadmap Recovery SHA256 preserved as baseline;canonical roadmap defines22 tasks. Existing five checkpoints,all inherited report/history/source/ZIP/patch files were hash-protected and are not edited. Current audit checkpoint is AUDIT_PROGRESS.md inside this new evidence folder to respect latest preservation/no-overwrite instruction. Before/after Git status and hashes are retained;the only expected new Git addition is this audit folder.

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
