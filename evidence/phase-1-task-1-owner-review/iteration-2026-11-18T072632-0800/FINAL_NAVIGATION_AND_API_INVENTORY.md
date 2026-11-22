# Final Navigation and API Inventory

Project: COME-IN. Review recorded **2026-11-19T13:59:07.329884+05:30 (Asia/Kolkata)**. This existing dated iteration was opened on 18 November and resumed on 19 November; it is not a new audit restart.

Repository: `/workspace/come-in-current`; branch: `work`; HEAD: `a223290a8866a1ebeaac982f546491fdc197ae7a`. Application extraction: `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115` (outside the Git checkout).

Scope: read-only evidence investigation and NEW documentation only. All seven original audit reports and all six original owner-review reports/manifests were read before this iteration's investigation. Originals are retained verbatim. No application tests, browser actions, database queries/writes, account/token creation, provider calls, installs, configuration changes or implementation were performed. Task 2 was not started. The owner has not approved or closed Task 1.

Classification vocabulary: VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / CONTRADICTED / BLOCKED. Each assessed assertion has one classification. Source correctness, runtime acceptance and owner approval are separate assertions.

## Navigation count reconciliation

Source scope is the previously inventoried95 TS/TSX modules,including53 app route/layout files. The 579 event bindings are occurrences,not 579 working buttons or vulnerabilities. The 108 previously selected literal targets resolve at source level,but did not exhaust conditional leaves. Complete bounded count: **107 unconditional literal/pathname calls +6 leaves of3 two-branch conditional calls =113 literal destination occurrences**. The old 108 set retained the Restaurant leaf at `orders.tsx:193` and omitted the five below. These are destination occurrences,not unique URLs or completed journeys.

Original 108 checks: [navigation-target-checks.json](</workspace/come-in-current/evidence/phase-1-task-1-audit/navigation-target-checks.json>). New predicates,components,source/target hashes and input hashes: [navigation-closure.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/iteration-2026-11-18T072632-0800/navigation-closure.json>). The file-existence/source mapping assertions below are VERIFIED;runtime navigation remains UNVERIFIED.

| Omitted leaf | Source | Exact static condition | Destination / parameters | Existing destination file | Classification |
| --- | --- | --- | --- | --- | --- |
| NAV-OMITTED-1 | [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:102>) | (user) | /notifications | [NotificationsScreen](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:17>) | VERIFIED |
| NAV-OMITTED-2 | [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:102>) | NOT(user) | /orders | [MyOrdersScreen](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:17>) | VERIFIED |
| NAV-OMITTED-3 | [notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:42>) | (n.data?.seller) AND (n.data.order_kind === "restaurant") | /restaurant/dashboard | [RestaurantDashboard](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:10>) | VERIFIED |
| NAV-OMITTED-4 | [notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:42>) | (n.data?.seller) AND NOT(n.data.order_kind === "restaurant") | /seller/orders | [SellerOrdersScreen](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:30>) | VERIFIED |
| NAV-OMITTED-5 | [orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:193>) | NOT(item.kind === "restaurant") | /order-tracking; { pathname: "/order-tracking", params: { id: item.id, kind: "grocery" } } | [OrderTrackingScreen](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/order-tracking.tsx:13>) | VERIFIED |

Home uses truthiness of `user` from useAuth;no extra authorization predicate is inferred. Notification seller branches require `n.data?.seller`;Restaurant additionally requires matchingorder_kind,the other seller branch requires its negation. Notification `open(n)` can POST a read marker and update local state before navigation;it was not invoked. Orders branch uses the item kind,not an extra invented role guard. The already recorded Restaurant alternative is `/restaurant/orders/[id]` with `{id:item.id}`. No id validity or ownership was exercised.

## Href attributes

| ID | Source / expression | Base target / candidate | Classification / scope |
| --- | --- | --- | --- |
| NAV-HREF-1 | [+not-found.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/+not-found.tsx:21>) "/(tabs)" | /(tabs) [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:39>) | VERIFIED; Source mapping only;Redirect/Link not executed and runtime route resolution/parameters not verified. |
| NAV-HREF-2 | [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/index.tsx:4>) "/(tabs)" | /(tabs) [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:39>) | VERIFIED; Source mapping only;Redirect/Link not executed and runtime route resolution/parameters not verified. |
| NAV-HREF-3 | [account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/account.tsx:10>) "/(tabs)/account" | /(tabs)/account [account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:23>) | VERIFIED; Source mapping only;Redirect/Link not executed and runtime route resolution/parameters not verified. |
| NAV-HREF-4 | [addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/addresses.tsx:3>) "/addresses" | /addresses [addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:8>) | VERIFIED; Source mapping only;Redirect/Link not executed and runtime route resolution/parameters not verified. |
| NAV-HREF-5 | [support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/support.tsx:6>) {`/chand?openHelp=1${suffix}` as never} | /chand [chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:146>) | PARTIALLY VERIFIED; Source mapping only;Redirect/Link not executed and runtime route resolution/parameters not verified. {"source": {"path": "/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/support.tsx", "line": 5}, "when_order_id_truthy": "&order_id=${encodeURIComponent(order_id)}&order_kind=${order_kind === \"grocery\" ? \"grocery\" : \"restaurant\"}", "when_order_id_falsy": "empty suffix", "fixed_query": "openHelp=1", "full_source_line": "  const suffix = order_id ? `&order_id=${encodeURIComponent(order_id)}&order_kind=${order_kind === 'grocery' ? 'grocery' : 'restaurant'}` : '';"} |

## Fourteen dynamic router arguments

Source classification includes12 entity-template occurrences,one unbounded auth next,and one finite RestaurantNav route list. Parameter values,encoding,permissions and actual rendering/navigation remain untested.

| ID | Source / argument | Lexical conditions | Route pattern / files | Classification / remaining evidence |
| --- | --- | --- | --- | --- |
| NAV-DYNAMIC-1 | [categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/categories.tsx:41>) `/category/${item.id}` | [] | /category/[slug] [[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:11>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-2 | [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:203>) `/category/${item.id}` | [] | /category/[slug] [[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:11>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-3 | [auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:64>) next as any | [{"kind": "if", "condition": "next && typeof next === \"string\"", "branch": "then/truthy", "line": 64}] | No single static pattern   | UNVERIFIED; next is a route parameter passed through as any after successful authentication;no in-source route allowlist is checked at the navigation call. Whether external/malformed/unauthorized target navigation is possible is UNVERIFIED,not an exploit finding. |
| NAV-DYNAMIC-4 | [[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:48>) `/category/${item.id}` | [] | /category/[slug] [[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:11>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-5 | [chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:399>) `/product/${product.id}` | [{"kind": "if", "condition": "product.variants?.length \|\| isMeasured(product)", "branch": "then/truthy", "line": 398}] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-6 | [notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:43>) `/product/${n.data.product_id}` | [{"kind": "if", "condition": "n.data?.seller", "branch": "else/falsy", "line": 42}, {"kind": "if", "condition": "n.data?.product_id", "branch": "then/truthy", "line": 43}] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-7 | [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:235>) `/product/${listing.id}` | [{"kind": "short-circuit-AND", "condition": "product.source === \"catalog\"", "branch": "truthy required", "line": 229}, {"kind": "conditional-expression", "condition": "matchingLiveListings.length === 0", "branch": "falsy", "line": 232}] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-8 | [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:264>) `/product/${r.id}` | [{"kind": "short-circuit-AND", "condition": "related.length > 0", "branch": "truthy required", "line": 252}] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-9 | [shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:192>) `/shop/${item.id}` | [] | /shop/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:16>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-10 | [ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:34>) `/product/${product.id}` | [{"kind": "if", "condition": "product.source !== \"live\" \|\| hasVariants \|\| measured", "branch": "then/truthy", "line": 34}] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-11 | [ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:46>) `/product/${product.id}` | [] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-12 | [ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:79>) `/product/${product.id}` | [{"kind": "conditional-expression", "condition": "product.source !== \"live\"", "branch": "falsy", "line": 73}, {"kind": "conditional-expression", "condition": "hasVariants", "branch": "truthy", "line": 75}] | /product/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:19>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-13 | [RestaurantCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/restaurant/RestaurantCard.tsx:6>) `/restaurant/${restaurant.id}` as never | [] | /restaurant/[id] [[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:10>)  | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |
| NAV-DYNAMIC-14 | [RestaurantNav.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/restaurant/RestaurantNav.tsx:6>) route as never | [] | No single static pattern  /restaurant: [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:11>); /restaurant/categories: [categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/categories.tsx:10>); /restaurant/search: [search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:11>); /restaurant/cart: [cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:7>); /restaurant/orders: [index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:24>); /restaurant/account: [account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/account.tsx:9>) | PARTIALLY VERIFIED; Parameter validity,entity existence,permissions,encoding,framework URL behavior and actual navigation are not tested. |

`_layout` files compose route trees,`+html` is a document helper and`+not-found` is a fallback. File-derived pseudo-path fields for these are not ordinary navigable-page acceptance. This corrects documentation only;no source route was changed.

## Complete API source inventory:179 registrations

All 179 explicit method/path/function triples match the old inventory. No duplicate method/path pairs were found within the parsed application decorators. This does not inspect dynamic runtime registrations or mounted external apps. Source SHA-256: `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db` for [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py>). No application import,OpenAPI generation,dependency execution or request occurred.

There are387 signature parameters,216 with Python defaults,27 Query parameters across 19 endpoints,and60 BaseModel declarations. Only 4 endpoints declare an explicit response_model. None of these counts proves runtime validity or full ownership/security coverage. Full structured source metadata: [complete-api-inventory.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/iteration-2026-11-18T072632-0800/complete-api-inventory.json>);extractor: [extract-complete-api.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/iteration-2026-11-18T072632-0800/extract-complete-api.py>). Model fields/defaults/validators are preserved in that JSON and summarized after the179rows.

The table preserves exact argument annotations/default expressions,including Query/Body/Form/File/Depends declarations. **Python default presence is not HTTP optionality**:File(...)/Form(...) are required despite Python defaults. Request model constraints,Annotated metadata and manual request reads also matter. No generated OpenAPI requiredness was asserted. Response columns show declared decorators,return annotations,direct exception sites and return expressions. Helper-raised errors,dependency errors,implicit framework422validation,conditional serialization and actual wire contracts are not exhaustively inferred and remain UNVERIFIED.

### API-001 — GET `/api/`

Classification: **VERIFIED — source declarations only**. Function `root`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:669>).

```python
root()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 670, "expression": "{\"service\": \"come-in\", \"status\": \"ok\", \"time\": now_iso()}", "literal_dict_keys": ["service", "status", "time"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-002 — POST `/api/status`

Classification: **VERIFIED — source declarations only**. Function `create_status_check`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:687>).

```python
create_status_check(payload: StatusCheckCreate)
```

Request declarations: StatusCheckCreate. Dependencies: []. Manual request-body reads: [].

Declared response_model: `StatusCheck`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {"response_model": "StatusCheck"}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 690, "expression": "obj", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-003 — GET `/api/status`

Classification: **VERIFIED — source declarations only**. Function `list_status_checks`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:694>).

```python
list_status_checks()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `List[StatusCheck]`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {"response_model": "List[StatusCheck]"}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 696, "expression": "[StatusCheck(**r) for r in rows]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-004 — POST `/api/auth/register`

Classification: **VERIFIED — source declarations only**. Function `register`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:854>).

```python
register(body: RegisterIn, request: Request)
```

Request declarations: RegisterIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `AuthOut`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {"response_model": "AuthOut"}.

Direct HTTPException sites: [{"line": 859, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Email already registered\""}}, {"line": 875, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Could not allocate a unique account/referral code\""}}].

Return expressions (source branches,not a validated schema): [{"line": 885, "expression": "{\"token\": token, \"user\": doc_out(user_doc)}", "literal_dict_keys": ["token", "user"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-005 — POST `/api/auth/login`

Classification: **VERIFIED — source declarations only**. Function `login`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:889>).

```python
login(body: LoginIn, request: Request)
```

Request declarations: LoginIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `AuthOut`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {"response_model": "AuthOut"}.

Direct HTTPException sites: [{"line": 895, "arguments": [], "keywords": {"status_code": "401", "detail": "\"Invalid email or password\""}}].

Return expressions (source branches,not a validated schema): [{"line": 897, "expression": "{\"token\": token, \"user\": doc_out(user)}", "literal_dict_keys": ["token", "user"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-006 — GET `/api/referrals/me`

Classification: **VERIFIED — source declarations only**. Function `referral_dashboard`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:901>).

```python
referral_dashboard(request: Request, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 903, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Referral & Earn is available to customer accounts only\""}}].

Return expressions (source branches,not a validated schema): [{"line": 919, "expression": "{\"referral_code\": code, \"referral_url\": link, \"message\": f\"Join me on COME-IN! Register using my referral link and explore shops, restaurants, products, and services.\\n\\nJoin here: {link}\",\n            \"counts\": statuses, \"eligible_count\": statuses[\"qualified\"], \"target\": REFERRAL_TARGET,\n            \"reward_amount\": REFERRAL_REWARD_INR, \"reward_status\": reward.get(\"status\", \"not_yet_earned\") if reward else \"not_yet_earned\",\n            \"available_balance\": round(balance, 2), \"referrals\": referrals, \"ledger\": ledger,\n            \"payout_integration\": \"manual_admin_review_required\"}", "literal_dict_keys": ["referral_code", "referral_url", "message", "counts", "eligible_count", "target", "reward_amount", "reward_status", "available_balance", "referrals", "ledger", "payout_integration"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-007 — POST `/api/referrals/home-banner-claim`

Classification: **VERIFIED — source declarations only**. Function `claim_first_home_referral_banner`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:927>).

```python
claim_first_home_referral_banner(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 939, "expression": "{\"show_prominent\": result.modified_count == 1}", "literal_dict_keys": ["show_prominent"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 930, "expression": "{\"show_prominent\": False}", "literal_dict_keys": ["show_prominent"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 934, "expression": "{\"show_prominent\": False}", "literal_dict_keys": ["show_prominent"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-008 — GET `/api/referral/validate`

Classification: **VERIFIED — source declarations only**. Function `validate_referral`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:943>).

```python
validate_referral(code: str=Query(min_length=6, max_length=24))
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 946, "expression": "{\"valid\": bool(referrer), \"code\": normalize_referral_code(code)}", "literal_dict_keys": ["valid", "code"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-009 — GET `/api/referral`

Classification: **VERIFIED — source declarations only**. Function `open_referral`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:950>).

```python
open_referral(code: str=Query(min_length=6, max_length=24))
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 956, "expression": "{\"valid\": True, \"code\": code.strip().upper(), \"message\": \"Open COME-IN and register with this referral code. Set PUBLIC_APP_URL for production web/deferred linking.\"}", "literal_dict_keys": ["valid", "code", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 955, "expression": "RedirectResponse(url=f\"{public_url}/referral?code={code.strip().upper()}\", status_code=307)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-010 — GET `/api/admin/referrals`

Classification: **VERIFIED — source declarations only**. Function `admin_referrals`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:960>).

```python
admin_referrals(user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 963, "expression": "{\"referrals\": referrals, \"rewards\": rewards}", "literal_dict_keys": ["referrals", "rewards"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-011 — PATCH `/api/admin/referrals/{referral_id}/review`

Classification: **VERIFIED — source declarations only**. Function `admin_review_referral`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:967>).

```python
admin_review_referral(referral_id: str, body: ReferralReviewIn, user: dict=Depends(require_role('admin')))
```

Request declarations: ReferralReviewIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 969, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Referral not found\""}}, {"line": 1007, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Referral review could not be committed atomically\""}}, {"line": 975, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Referral not found\""}}, {"line": 978, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Referral is not awaiting review\""}}, {"line": 985, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Qualifying order must be at least ₹100, delivered, and free of pending refund/return/dispute flags\""}}, {"line": 987, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Verify the referred customer's contact using an authorized method before approval\""}}, {"line": 989, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Confirm payment and completed refund/return checks before approval\""}}, {"line": 992, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Referral review already processed\""}}, {"line": 981, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Qualifying order reference is invalid\""}}, {"line": 996, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Referral review already processed\""}}, {"line": 1000, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Referral cannot be held from its current state\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1010, "expression": "doc_out(await db.referrals.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-012 — PATCH `/api/admin/referral-rewards/{reward_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_update_referral_reward`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1014>).

```python
admin_update_referral_reward(reward_id: str, body: ReferralRewardDecisionIn, user: dict=Depends(require_role('admin')))
```

Request declarations: ReferralRewardDecisionIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1021, "arguments": [], "keywords": {"status_code": "422", "detail": "\"A verified bank payout reference is required before marking paid\""}}, {"line": 1016, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Reward not found\""}}, {"line": 1054, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Reward update could not be committed atomically; no payout status was intentionally changed\""}}, {"line": 1025, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Reward not found\""}}, {"line": 1027, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Invalid reward status transition\""}}, {"line": 1039, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Reward was concurrently updated\""}}, {"line": 1030, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Reward is missing its ten qualifying order references\""}}, {"line": 1037, "arguments": [], "keywords": {"status_code": "422", "detail": "\"A qualifying order is no longer eligible; reward remains pending verification\""}}, {"line": 1033, "arguments": [], "keywords": {"status_code": "409", "detail": "\"A qualifying order reference is invalid\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1055, "expression": "doc_out(await db.referral_rewards.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-013 — GET `/api/auth/me`

Classification: **VERIFIED — source declarations only**. Function `me`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1059>).

```python
me(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1060, "expression": "user", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-014 — PATCH `/api/auth/me`

Classification: **VERIFIED — source declarations only**. Function `update_me`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1069>).

```python
update_me(body: UpdateProfileIn, user: dict=Depends(get_current_user))
```

Request declarations: UpdateProfileIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1076, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 1072, "expression": "user", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-015 — POST `/api/auth/password/forgot`

Classification: **VERIFIED — source declarations only**. Function `forgot_password`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1107>).

```python
forgot_password(body: ForgotPasswordIn, request: Request)
```

Request declarations: ForgotPasswordIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1120, "expression": "{\"message\":\"If that email is registered and reset email is configured, instructions will be sent.\"}", "literal_dict_keys": ["message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-016 — POST `/api/auth/password/reset`

Classification: **VERIFIED — source declarations only**. Function `reset_password`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1123>).

```python
reset_password(body: ResetPasswordIn, request: Request)
```

Request declarations: ResetPasswordIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1126, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Reset link is invalid or expired\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1130, "expression": "{\"reset\":True,\"message\":\"Password updated. Please sign in again.\"}", "literal_dict_keys": ["reset", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-017 — POST `/api/uploads/image`

Classification: **VERIFIED — source declarations only**. Function `upload_image`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1142>).

```python
upload_image(file: UploadFile=File(...), user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1148, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Only JPEG/PNG/WEBP/GIF images are allowed\""}}, {"line": 1151, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Image too large (max 5 MB)\""}}, {"line": 1161, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Image bytes do not match the declared file type\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1181, "expression": "{\"url\": f\"/api/uploads/{result['path']}\", \"storage_path\": result[\"path\"]}", "literal_dict_keys": ["url", "storage_path"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-018 — GET `/api/uploads/{storage_path:path}`

Classification: **VERIFIED — source declarations only**. Function `serve_upload`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1185>).

```python
serve_upload(storage_path: str)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1187, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Invalid path\""}}, {"line": 1190, "arguments": [], "keywords": {"status_code": "404", "detail": "\"File not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1192, "expression": "Response(content=data, media_type=record.get(\"content_type\") or ct)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-019 — POST `/api/shops`

Classification: **VERIFIED — source declarations only**. Function `create_shop`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1222>).

```python
create_shop(body: ShopIn, user: dict=Depends(get_current_user))
```

Request declarations: ShopIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1225, "arguments": [], "keywords": {"status_code": "403", "detail": "\"This account cannot register a shop\""}}, {"line": 1229, "arguments": [], "keywords": {"status_code": "400", "detail": "\"You already have a shop registered\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1247, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-020 — GET `/api/shops/mine`

Classification: **VERIFIED — source declarations only**. Function `my_shop`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1251>).

```python
my_shop(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1255, "expression": "doc_out(shop)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 1254, "expression": "None", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-021 — PATCH `/api/shops/{shop_id}`

Classification: **VERIFIED — source declarations only**. Function `update_shop`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1259>).

```python
update_shop(shop_id: str, body: ShopIn, user: dict=Depends(get_current_user))
```

Request declarations: ShopIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1266, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-022 — PATCH `/api/shops/{shop_id}/availability`

Classification: **VERIFIED — source declarations only**. Function `set_shop_availability`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1274>).

```python
set_shop_availability(shop_id: str, body: ShopAvailabilityIn, user: dict=Depends(get_current_user))
```

Request declarations: ShopAvailabilityIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1280, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Shop must be approved before going online\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1285, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-023 — GET `/api/shops`

Classification: **VERIFIED — source declarations only**. Function `list_shops`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1289>).

```python
list_shops(type: Optional[str]=None, online: Optional[str]=None, q: Optional[str]=None)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1318, "expression": "rows", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-024 — GET `/api/shops/{shop_id}`

Classification: **VERIFIED — source declarations only**. Function `get_shop`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1322>).

```python
get_shop(shop_id: str)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1326, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Shop not available\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1329, "expression": "public_shop", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-025 — POST `/api/chand/feedback`

Classification: **VERIFIED — source declarations only**. Function `submit_chand_feedback`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1367>).

```python
submit_chand_feedback(body: ChandFeedbackIn, user: dict=Depends(get_current_user))
```

Request declarations: ChandFeedbackIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1375, "arguments": [], "keywords": {"status_code": "429", "detail": "\"Feedback limit reached. Please try again later.\""}}, {"line": 1389, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Feedback request could not be confirmed\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1390, "expression": "doc_out(await db.chand_feedback.find_one({\"_id\": result.inserted_id}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 1371, "expression": "doc_out(existing)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 1388, "expression": "doc_out(existing)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-026 — GET `/api/chand/feedback/mine`

Classification: **VERIFIED — source declarations only**. Function `my_chand_feedback`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1394>).

```python
my_chand_feedback(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1395, "expression": "[doc_out(x) async for x in db.chand_feedback.find({\"user_id\": user[\"id\"]}, {\"user_id\": 0}).sort(\"created_at\", -1).limit(50)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-027 — GET `/api/admin/chand/feedback`

Classification: **VERIFIED — source declarations only**. Function `admin_chand_feedback`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1399>).

```python
admin_chand_feedback(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1400, "expression": "[doc_out(x) async for x in db.chand_feedback.find({}, {\"user_id\": 0}).sort(\"created_at\", -1).limit(500)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-028 — GET `/api/admin/chand/feedback/summary`

Classification: **VERIFIED — source declarations only**. Function `admin_chand_feedback_summary`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1404>).

```python
admin_chand_feedback_summary(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1410, "expression": "[{\"rating\": row.get(\"_id\", {}).get(\"rating\"), \"category\": row.get(\"_id\", {}).get(\"category\"),\n             \"status\": row.get(\"_id\", {}).get(\"status\"), \"count\": int(row.get(\"count\", 0))} for row in rows]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-029 — PATCH `/api/admin/chand/feedback/{feedback_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_update_chand_feedback`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1415>).

```python
admin_update_chand_feedback(feedback_id: str, body: ChandFeedbackStatusIn, _: dict=Depends(require_role('admin')))
```

Request declarations: ChandFeedbackStatusIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1419, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Chand feedback not found\""}}, {"line": 1422, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Invalid Chand feedback status transition\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1426, "expression": "doc_out(updated)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-030 — POST `/api/assistant/context`

Classification: **VERIFIED — source declarations only**. Function `assistant_context`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1430>).

```python
assistant_context(body: AssistantContextIn, request: Request, user: Optional[dict]=Depends(get_current_user_optional))
```

Request declarations: AssistantContextIn. Dependencies: ["get_current_user_optional"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1439, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Enter a search question\""}}, {"line": 1455, "arguments": [], "keywords": {"status_code": "429", "detail": "\"Chand is receiving too many requests. Please wait a minute and try again.\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1604, "expression": "context", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 1471, "expression": "[{field: {\"$regex\": re.escape(term), \"$options\": \"i\"}} for term in terms for field in fields]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-031 — GET `/api/assistant/health`

Classification: **VERIFIED — source declarations only**. Function `assistant_health`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1644>).

```python
assistant_health()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1653, "expression": "{\n        \"provider\": provider if configured else \"not_configured\",\n        \"configured\": configured,\n        \"live_probe\": False,\n        \"message\": \"Configuration is present; provider connectivity has not been tested.\" if configured else \"Configure a supported provider on the backend.\",\n        \"vision_capability\": \"unverified\" if configured else \"not_configured\",\n        \"speech_to_text_configured\": provider == \"openai_compatible\" and bool(base_url and api_key and os.environ.get(\"COMEIN_STT_MODEL\", \"whisper-1\").strip()),\n    }", "literal_dict_keys": ["provider", "configured", "live_probe", "message", "vision_capability", "speech_to_text_configured"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-032 — POST `/api/assistant/transcribe`

Classification: **VERIFIED — source declarations only**. Function `assistant_transcribe`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1664>).

```python
assistant_transcribe(file: UploadFile=File(...), language: Optional[str]=Query(default=None, pattern='^(hi|en)$'), user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1673, "arguments": [], "keywords": {"status_code": "415", "detail": "\"Use a supported audio recording format.\""}}, {"line": 1676, "arguments": [], "keywords": {"status_code": "413", "detail": "\"Audio must be between 1 byte and 12 MB.\""}}, {"line": 1680, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Speech provider is not configured. Voice transcription is unavailable.\""}}, {"line": 1697, "arguments": [], "keywords": {"status_code": "422", "detail": "\"No speech was recognized. Please try again.\""}}, {"line": 1695, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Speech transcription failed. Please try again or type your request.\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1698, "expression": "{\"text\": transcript.strip()[:1000], \"language\": language or \"auto\", \"stored\": False}", "literal_dict_keys": ["text", "language", "stored"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-033 — POST `/api/assistant/vision`

Classification: **VERIFIED — source declarations only**. Function `assistant_vision`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1702>).

```python
assistant_vision(request: Request, file: UploadFile=File(...), language: str=Query(default='en', pattern='^(en|hi|gu|mr|ta|te|bn|pa|kn|ml|or|ur)$'), user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1716, "arguments": [], "keywords": {"status_code": "415", "detail": "\"Upload a JPEG, PNG or WebP product photo.\""}}, {"line": 1719, "arguments": [], "keywords": {"status_code": "413", "detail": "\"Product photos must be no larger than 5 MB.\""}}, {"line": 1726, "arguments": [], "keywords": {"status_code": "415", "detail": "\"The image content does not match its declared format.\""}}, {"line": 1729, "arguments": [], "keywords": {"status_code": "503", "detail": "\"A vision-capable AI provider is not configured.\""}}, {"line": 1759, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Photo recognition failed. Please try another clear photo or type the product name.\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1769, "expression": "catalog", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 1761, "expression": "{\"recognized_text\": \"\", \"products\": [], \"match_status\": \"unclear\", \"image_stored\": False}", "literal_dict_keys": ["recognized_text", "products", "match_status", "image_stored"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-034 — POST `/api/admin/master-products`

Classification: **VERIFIED — source declarations only**. Function `create_master_product`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1876>).

```python
create_master_product(body: MasterProductIn, _: dict=Depends(require_role('admin')))
```

Request declarations: MasterProductIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1880, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Product name cannot be blank\""}}, {"line": 1885, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"duplicate_master_product\", \"message\": \"A matching master product already exists\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 1893, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-035 — GET `/api/catalog/master-products`

Classification: **VERIFIED — source declarations only**. Function `search_master_products`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1897>).

```python
search_master_products(q: str=Query(default='', max_length=120), category_id: Optional[str]=Query(default=None, max_length=40), limit: int=Query(default=30, ge=1, le=100), _: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 1906, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-036 — POST `/api/shops/{shop_id}/master-products/{master_product_id}/link`

Classification: **VERIFIED — source declarations only**. Function `link_master_product`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1910>).

```python
link_master_product(shop_id: str, master_product_id: str, body: MasterLinkIn, user: dict=Depends(get_current_user))
```

Request declarations: MasterLinkIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1919, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Active master product not found\""}}, {"line": 1923, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"invalid_variant\", \"message\": \"Choose a valid master catalog variant\"}"}}, {"line": 1926, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"duplicate_link\", \"message\": \"This master product variant is already linked to your shop\"}"}}, {"line": 1916, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Master product not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 1939, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-037 — POST `/api/shops/{shop_id}/products`

Classification: **VERIFIED — source declarations only**. Function `create_product`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1948>).

```python
create_product(shop_id: str, body: ProductIn, user: dict=Depends(get_current_user))
```

Request declarations: ProductIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 1961, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"duplicate_sku\", \"message\": \"This SKU already exists in your shop\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 1972, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-038 — POST `/api/shops/{shop_id}/catalogue-import/jobs`

Classification: **VERIFIED — source declarations only**. Function `create_catalogue_import_job`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2014>).

```python
create_catalogue_import_job(shop_id: str, files: List[UploadFile]=File(...), user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2027, "arguments": [], "keywords": {"status_code": "413", "detail": "f\"Upload between 1 and {CATALOGUE_IMPORT_MAX_FILES} files\""}}, {"line": 2067, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"catalogue_import_no_supported_files\", \"errors\": errors}"}}].

Return expressions (source branches,not a validated schema): [{"line": 2099, "expression": "{\"job_id\": job_id, \"shop_id\": shop_id, \"status\": status_value, \"files_processed\": len(source_files), \"total_records\": len(staged_records), \"needs_review\": len(staged_records), \"errors\": errors, \"applied\": False}", "literal_dict_keys": ["job_id", "shop_id", "status", "files_processed", "total_records", "needs_review", "errors", "applied"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-039 — GET `/api/shops/{shop_id}/catalogue-import/jobs/{job_id}`

Classification: **VERIFIED — source declarations only**. Function `get_catalogue_import_job`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2103>).

```python
get_catalogue_import_job(shop_id: str, job_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2108, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Catalogue import job not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2109, "expression": "job", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-040 — GET `/api/shops/{shop_id}/catalogue-import/jobs`

Classification: **VERIFIED — source declarations only**. Function `list_catalogue_import_jobs`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2154>).

```python
list_catalogue_import_jobs(shop_id: str, user: dict=Depends(get_current_user), limit: int=Query(default=30, ge=1, le=100))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2158, "expression": "[row async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-041 — GET `/api/shops/{shop_id}/catalogue-import/categories`

Classification: **VERIFIED — source declarations only**. Function `list_catalogue_import_categories`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2162>).

```python
list_catalogue_import_categories(shop_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2168, "expression": "sorted({str(value) for value in (master_ids + shop_ids) if value})", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-042 — PATCH `/api/shops/{shop_id}/catalogue-import/jobs/{job_id}/records/{record_index}`

Classification: **VERIFIED — source declarations only**. Function `edit_catalogue_import_record`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2172>).

```python
edit_catalogue_import_record(shop_id: str, job_id: str, record_index: int, body: dict, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2177, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Import record not found\""}}, {"line": 2180, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This record is already reviewed and cannot be edited\""}}, {"line": 2183, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Only supported product fields may be edited\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2192, "expression": "{\"record_index\": record_index, \"seller_edited_fields\": edited, \"review_status\": \"NEEDS_REVIEW\"}", "literal_dict_keys": ["record_index", "seller_edited_fields", "review_status"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-043 — POST `/api/shops/{shop_id}/catalogue-import/jobs/{job_id}/records/{record_index}/approve`

Classification: **VERIFIED — source declarations only**. Function `approve_catalogue_import_record`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2196>).

```python
approve_catalogue_import_record(shop_id: str, job_id: str, record_index: int, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2201, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Import record not found\""}}, {"line": 2204, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Import job has already been applied\""}}, {"line": 2207, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"record_validation_failed\", \"errors\": errors}"}}].

Return expressions (source branches,not a validated schema): [{"line": 2212, "expression": "{\"record_index\": record_index, \"review_status\": \"APPROVED\"}", "literal_dict_keys": ["record_index", "review_status"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-044 — POST `/api/shops/{shop_id}/catalogue-import/jobs/{job_id}/records/{record_index}/reject`

Classification: **VERIFIED — source declarations only**. Function `reject_catalogue_import_record`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2216>).

```python
reject_catalogue_import_record(shop_id: str, job_id: str, record_index: int, body: dict={}, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2221, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Import record not found\""}}, {"line": 2223, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Import job has already been applied\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2228, "expression": "{\"record_index\": record_index, \"review_status\": \"REJECTED\"}", "literal_dict_keys": ["record_index", "review_status"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-045 — POST `/api/shops/{shop_id}/catalogue-import/jobs/{job_id}/bulk-approve`

Classification: **VERIFIED — source declarations only**. Function `bulk_approve_catalogue_import_records`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2232>).

```python
bulk_approve_catalogue_import_records(shop_id: str, job_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2236, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Import job has already been applied\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2251, "expression": "{\"approved_record_indices\": approved, \"skipped\": skipped, \"approved_count\": len(approved)}", "literal_dict_keys": ["approved_record_indices", "skipped", "approved_count"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-046 — POST `/api/shops/{shop_id}/catalogue-import/jobs/{job_id}/confirm-apply`

Classification: **VERIFIED — source declarations only**. Function `confirm_catalogue_import_apply`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2407>).

```python
confirm_catalogue_import_apply(shop_id: str, job_id: str, body: dict, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2410, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Explicit confirm=true is required\""}}, {"line": 2415, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Only the shop owner can apply catalogue imports\""}}, {"line": 2421, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Import is already processed or requires reconciliation\""}}, {"line": 2430, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Conflicting import record; no Product merge was attempted\""}}, {"line": 2441, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Import transaction not confirmed; reconcile committed job before retrying\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2423, "expression": "await _apply_catalogue_import_job_transactionally(shop_id, job_id, user[\"id\"])", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2420, "expression": "verified", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2429, "expression": "verified", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2439, "expression": "verified", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-047 — POST `/api/shops/{shop_id}/products/import`

Classification: **VERIFIED — source declarations only**. Function `import_shop_products`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2445>).

```python
import_shop_products(shop_id: str, file: UploadFile=File(...), apply: bool=Form(default=False), user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2461, "arguments": [], "keywords": {"status_code": "415", "detail": "\"Upload a .csv, .xlsx, or .xls file\""}}, {"line": 2464, "arguments": [], "keywords": {"status_code": "413", "detail": "\"Import file exceeds the 5 MB limit\""}}, {"line": 2493, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Import file has no data rows\""}}, {"line": 2495, "arguments": [], "keywords": {"status_code": "413", "detail": "\"Import is limited to 5,000 rows per file\""}}, {"line": 2498, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"invalid_import_columns\", \"message\": \"Required columns: name, unit, price, stock, category_id, description\", \"missing\": sorted(required - headers)}"}}, {"line": 2491, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Could not read import file as UTF-8 CSV or Excel\""}}, {"line": 2678, "arguments": [], "keywords": {"status_code": "503", "detail": "{\"code\": \"catalog_import_unavailable\", \"message\": \"The import was not committed because the database could not complete a safe transaction.\"}"}}, {"line": 2472, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"invalid_import_headers\", \"message\": \"CSV column names must be non-empty and unique (case-insensitive).\"}"}}, {"line": 2482, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"invalid_import_headers\", \"message\": \"Excel column names must be non-empty and unique (case-insensitive).\"}"}}, {"line": 2487, "arguments": [], "keywords": {"status_code": "415", "detail": "\"Excel import requires pandas plus openpyxl (.xlsx) or xlrd (.xls); CSV import is available\""}}, {"line": 2634, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"import_listing_changed\", \"message\": f\"Row {row['row']} no longer matches an existing listing. No import changes were committed.\"}"}}, {"line": 2636, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"import_product_identity_conflict\", \"message\": f\"Row {row['row']} brand or pack/unit no longer matches the selected listing. No import changes were committed.\"}"}}, {"line": 2641, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"import_sku_conflict\", \"message\": f\"Row {row['row']} SKU belongs to a different listing. No import changes were committed.\"}"}}, {"line": 2643, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"import_variant_conflict\", \"message\": f\"Row {row['row']} cannot change a master-linked variant unit. No import changes were committed.\"}"}}, {"line": 2645, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"import_measured_variant_conflict\", \"message\": f\"Row {row['row']} cannot make a product with pack variants a measured product. No import changes were committed.\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 2680, "expression": "result", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2572, "expression": "{\"mode\": \"apply\" if apply else \"preview\", \"valid_rows\": len(valid_rows), \"created\": 0, \"updated\": 0, \"skipped\": len(rows) - len(valid_rows), \"errors\": errors, \"applied\": False}", "literal_dict_keys": ["mode", "valid_rows", "created", "updated", "skipped", "errors", "applied"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2615, "expression": "{\"mode\": \"apply\" if apply else \"preview\", \"valid_rows\": len(valid_rows), \"created\": 0, \"updated\": 0, \"skipped\": len(preflight_errors), \"errors\": preflight_errors, \"applied\": False, \"new_products\": new_products, \"price_changes\": price_changes}", "literal_dict_keys": ["mode", "valid_rows", "created", "updated", "skipped", "errors", "applied", "new_products", "price_changes"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2617, "expression": "{\"mode\": \"preview\", \"valid_rows\": len(valid_rows), \"created\": 0, \"updated\": 0, \"skipped\": 0, \"errors\": [], \"applied\": False, \"new_products\": new_products, \"matched_updates\": matched_updates, \"price_changes\": price_changes, \"message\": \"Validation passed. Review changes and re-submit with apply=true to write these rows.\"}", "literal_dict_keys": ["mode", "valid_rows", "created", "updated", "skipped", "errors", "applied", "new_products", "matched_updates", "price_changes", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-048 — GET `/api/shops/{shop_id}/products/import-template`

Classification: **VERIFIED — source declarations only**. Function `shop_product_import_template`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2684>).

```python
shop_product_import_template(shop_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2692, "expression": "Response(content=content, media_type=\"text/csv\", headers={\"Content-Disposition\": \"attachment; filename=come-in-grocery-import-template.csv\"})", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-049 — GET `/api/admin/catalog-import-history`

Classification: **VERIFIED — source declarations only**. Function `admin_catalog_import_history`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2696>).

```python
admin_catalog_import_history(user: dict=Depends(require_role('admin')), limit: int=Query(default=100, ge=1, le=500))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2698, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-050 — GET `/api/admin/catalog-price-audit`

Classification: **VERIFIED — source declarations only**. Function `admin_catalog_price_audit`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2702>).

```python
admin_catalog_price_audit(user: dict=Depends(require_role('admin')), limit: int=Query(default=200, ge=1, le=1000))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2704, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-051 — GET `/api/catalog/price-comparison`

Classification: **VERIFIED — source declarations only**. Function `compare_master_product_prices`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2708>).

```python
compare_master_product_prices(master_product_id: str=Query(min_length=1, max_length=80), variant_id: str=Query(min_length=1, max_length=80), sell_by: Optional[Literal['pack', 'weight', 'volume']]=Query(default=None))
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2720, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Active master product not found\""}}, {"line": 2723, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Master product variant not found\""}}, {"line": 2717, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Master product not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2737, "expression": "{\"master_product_id\": str(master_oid), \"product_name\": master.get(\"name\", \"\"), \"brand\": master.get(\"brand\", \"\"), \"variant_id\": variant_id, \"unit\": MEASURED_SELL_BY[sell_by][1] if measured_mode else variant[\"unit\"], \"sell_by\": sell_by if measured_mode else \"pack\", \"offers\": offers, \"offer_count\": len(offers), \"lowest_price\": offers[0][\"price\"] if offers else None, \"last_updated\": max((o[\"updated_at\"] for o in offers if o.get(\"updated_at\")), default=None)}", "literal_dict_keys": ["master_product_id", "product_name", "brand", "variant_id", "unit", "sell_by", "offers", "offer_count", "lowest_price", "last_updated"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-052 — GET `/api/admin/retail-price-import/template`

Classification: **VERIFIED — source declarations only**. Function `retail_price_import_template`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2760>).

```python
retail_price_import_template(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2762, "expression": "Response(content=content, media_type=\"text/csv\", headers={\"Content-Disposition\": \"attachment; filename=come-in-retail-price-template.csv\"})", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-053 — POST `/api/admin/retail-price-import`

Classification: **VERIFIED — source declarations only**. Function `admin_retail_price_import`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2766>).

```python
admin_retail_price_import(file: UploadFile=File(...), apply: bool=Form(default=False), user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2774, "arguments": [], "keywords": {"status_code": "415", "detail": "\"Upload a .csv, .xlsx, or .xls file\""}}, {"line": 2777, "arguments": [], "keywords": {"status_code": "413", "detail": "\"Import file exceeds the 5 MB limit\""}}, {"line": 2799, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"invalid_retail_import_columns\", \"message\": \"Required columns: retailer, retailer_shop_id, name, price; recommended: sku, category_id, brand, pack_size/unit, stock, last_updated, source_url\", \"missing\": missing}"}}, {"line": 2795, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Could not read import file as UTF-8 CSV or Excel\""}}, {"line": 2858, "arguments": [], "keywords": {"status_code": "503", "detail": "{\"code\": \"retail_import_unavailable\", \"message\": \"Retail import was not committed because the database could not complete a safe transaction.\"}"}}, {"line": 2791, "arguments": [], "keywords": {"status_code": "415", "detail": "\"Excel import requires pandas plus openpyxl (.xlsx) or xlrd (.xls); CSV import is available\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2859, "expression": "{\"mode\": \"apply\", \"valid_rows\": len(normalized_rows), \"created\": created, \"updated\": updated, \"skipped\": 0, \"errors\": [], \"rows\": preview_rows, \"applied\": True, \"imported_at\": imported_at}", "literal_dict_keys": ["mode", "valid_rows", "created", "updated", "skipped", "errors", "rows", "applied", "imported_at"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2836, "expression": "{\"mode\": \"apply\" if apply else \"preview\", \"valid_rows\": len(normalized_rows), \"created\": 0, \"updated\": 0, \"skipped\": len(errors), \"errors\": errors, \"rows\": preview_rows, \"applied\": False}", "literal_dict_keys": ["mode", "valid_rows", "created", "updated", "skipped", "errors", "rows", "applied"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2838, "expression": "{\"mode\": \"preview\", \"valid_rows\": len(normalized_rows), \"created\": 0, \"updated\": 0, \"skipped\": 0, \"errors\": [], \"rows\": preview_rows, \"applied\": False, \"message\": \"Preview only; no retailer price records have been written.\"}", "literal_dict_keys": ["mode", "valid_rows", "created", "updated", "skipped", "errors", "rows", "applied", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-054 — GET `/api/catalog/retail-prices`

Classification: **VERIFIED — source declarations only**. Function `public_retail_prices`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2863>).

```python
public_retail_prices(retailer: Optional[str]=None, q: Optional[str]=None, limit: int=Query(default=100, ge=1, le=500))
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2871, "expression": "[public_doc(row, (\"updated_by\", \"source_filename\")) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-055 — GET `/api/admin/retail-price-import/history`

Classification: **VERIFIED — source declarations only**. Function `admin_retail_price_import_history`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2875>).

```python
admin_retail_price_import_history(_: dict=Depends(require_role('admin')), limit: int=Query(default=100, ge=1, le=500))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2877, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-056 — GET `/api/shops/{shop_id}/products`

Classification: **VERIFIED — source declarations only**. Function `list_shop_products`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2881>).

```python
list_shop_products(shop_id: str, user: Optional[dict]=Depends(get_current_user_optional))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user_optional"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2888, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Shop not available\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2895, "expression": "rows", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-057 — GET `/api/catalog/products`

Classification: **VERIFIED — source declarations only**. Function `list_catalog_products`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2899>).

```python
list_catalog_products()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 2935, "expression": "rows", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 2909, "expression": "[]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-058 — PATCH `/api/products/{product_id}`

Classification: **VERIFIED — source declarations only**. Function `update_product`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2939>).

```python
update_product(product_id: str, body: ProductIn, user: dict=Depends(get_current_user))
```

Request declarations: ProductIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2949, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Product not found\""}}, {"line": 2946, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Product not found\""}}, {"line": 2952, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 2956, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Not your product\""}}, {"line": 2974, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"duplicate_sku\", \"message\": \"This SKU already exists in your shop\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 2979, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-059 — DELETE `/api/products/{product_id}`

Classification: **VERIFIED — source declarations only**. Function `delete_product`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:2983>).

```python
delete_product(product_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 2990, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Product not found\""}}, {"line": 2987, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Product not found\""}}, {"line": 2993, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 2997, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Not your product\""}}].

Return expressions (source branches,not a validated schema): [{"line": 2999, "expression": "{\"deleted\": True}", "literal_dict_keys": ["deleted"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-060 — POST `/api/grocery/measured-price`

Classification: **VERIFIED — source declarations only**. Function `measured_price`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3182>).

```python
measured_price(body: QuoteLineIn)
```

Request declarations: QuoteLineIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3187, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"not_measured\", \"message\": \"This product is sold in fixed packs.\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 3188, "expression": "{\"product_id\": line[\"product_id\"], \"qty\": line[\"qty\"], \"price\": line[\"price\"], \"unit\": line[\"unit\"], \"line_total\": line[\"line_total\"], \"quantity_label\": line[\"quantity_label\"], \"currency\": \"INR\"}", "literal_dict_keys": ["product_id", "qty", "price", "unit", "line_total", "quantity_label", "currency"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-061 — POST `/api/grocery/quotes`

Classification: **VERIFIED — source declarations only**. Function `create_grocery_quote`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3192>).

```python
create_grocery_quote(body: GroceryQuoteIn, request: Request)
```

Request declarations: GroceryQuoteIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3199, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"pickup_unavailable\", \"message\": \"This shop does not currently support pickup.\"}"}}, {"line": 3201, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"delivery_unavailable\", \"message\": \"This shop does not currently support delivery. Choose pickup if available.\"}"}}, {"line": 3206, "arguments": [], "keywords": {"status_code": "401", "detail": "{\"code\": \"reward_login_required\", \"message\": \"Sign in with a customer account to use referral rewards.\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 3215, "expression": "{\"quote_token\": token, \"expires_at\": quote[\"expires_at\"].isoformat(), \"items\": resolved, \"fulfillment\": body.fulfillment, **totals, \"currency\": \"INR\"}", "literal_dict_keys": ["quote_token", "expires_at", "items", "fulfillment", "currency"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-062 — POST `/api/orders`

Classification: **VERIFIED — source declarations only**. Function `create_order`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3236>).

```python
create_order(body: OrderIn, request: Request)
```

Request declarations: OrderIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3241, "arguments": [], "keywords": {"status_code": "400", "detail": "{\"code\": \"quote_required\", \"message\": \"Create a fresh quote before placing a Grocery order\"}"}}, {"line": 3243, "arguments": [], "keywords": {"status_code": "400", "detail": "{\"code\": \"idempotency_required\", \"message\": \"Order retry key is required\"}"}}, {"line": 3250, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"quote_invalid\", \"message\": \"Quote is invalid or belongs to another session. Please review your cart again.\"}"}}, {"line": 3257, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"quote_expired\", \"message\": \"Your quote expired. Review prices again.\"}"}}, {"line": 3259, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"fulfillment_changed\", \"message\": \"Fulfillment choice changed. Request a fresh quote.\"}"}}, {"line": 3266, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"payment_method_disabled\", \"message\": \"This shop does not accept the selected payment method.\"}"}}, {"line": 3268, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"upi_not_configured\", \"message\": \"This shop has not configured a UPI ID.\"}"}}, {"line": 3270, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"pickup_payment_requires_pickup\", \"message\": \"Cash at shop / pay-at-pickup can only be used when pickup is selected.\"}"}}, {"line": 3272, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"payment_method_unavailable\", \"message\": \"This online gateway is not configured for Grocery checkout. Select a supported shop payment method.\"}"}}, {"line": 3279, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"pickup_unavailable\", \"message\": \"This shop no longer supports pickup.\"}"}}, {"line": 3281, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"delivery_unavailable\", \"message\": \"This shop no longer supports delivery.\"}"}}, {"line": 3283, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"delivery_address_required\", \"message\": \"Enter a delivery address.\"}"}}, {"line": 3287, "arguments": [], "keywords": {"status_code": "403", "detail": "{\"code\": \"reward_owner_mismatch\", \"message\": \"Only the customer who created this reward quote can use it.\"}"}}, {"line": 3289, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"reward_balance_changed\", \"message\": \"Your available reward balance changed. Request a fresh quote.\"}"}}, {"line": 3295, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"stock_changed\", \"message\": \"Inventory changed after your quote. No order was placed; review your cart and request a new quote.\"}"}}, {"line": 3305, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"price_changed\", \"message\": \"Prices changed. Review the updated quote and confirm again.\", \"updated_quote\": {\"quote_token\": fresh_token, \"expires_at\": fresh[\"expires_at\"].isoformat(), \"items\": current_lines, \"fulfillment\": body.fulfillment, **current_totals, \"currency\": \"INR\"}}"}}, {"line": 3307, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"shop_mismatch\", \"message\": \"Cart shop changed; please review your cart.\"}"}}, {"line": 3275, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"payment_method_unavailable\", \"message\": \"Online payment is not enabled for Grocery checkout yet. Select another payment method.\"}"}}, {"line": 3277, "arguments": [], "keywords": {"status_code": "403", "detail": "{\"code\": \"online_payment_requires_login\", \"message\": \"Sign in as a customer to pay online.\"}"}}, {"line": 3390, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"duplicate_order_submission\", \"message\": \"This order submission was already processed. Refresh your orders before retrying.\"}"}}, {"line": 3412, "arguments": [], "keywords": {"status_code": "503", "detail": "{\"code\": \"grocery_checkout_unavailable\", \"message\": \"Secure checkout is temporarily unavailable. Your cart has not been intentionally processed; please retry safely.\"}"}}, {"line": 3340, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"payment_method_disabled\", \"message\": \"This shop does not accept the selected payment method.\"}"}}, {"line": 3342, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"upi_settings_changed\", \"message\": \"Shop UPI settings changed during checkout. Review the shop's payment details and try again.\"}"}}, {"line": 3344, "arguments": [], "keywords": {"status_code": "422", "detail": "{\"code\": \"pickup_payment_requires_pickup\", \"message\": \"Cash at shop / pay-at-pickup can only be used when pickup is selected.\"}"}}, {"line": 3346, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"pickup_unavailable\", \"message\": \"This shop no longer supports pickup.\"}"}}, {"line": 3348, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"delivery_unavailable\", \"message\": \"This shop no longer supports delivery.\"}"}}, {"line": 3354, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"stock_changed\", \"message\": \"Inventory changed during checkout. No order was placed; request a new quote.\"}"}}, {"line": 3357, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"quote_changed\", \"message\": \"Price or delivery fee changed. Please request a new quote.\"}"}}, {"line": 3359, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"shop_changed\", \"message\": \"Shop changed. Please request a new quote.\"}"}}, {"line": 3369, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"quote_already_consumed\", \"message\": \"This checkout quote has already been used. Request a fresh quote before placing another order.\"}"}}, {"line": 3372, "arguments": [], "keywords": {"status_code": "409", "detail": "{\"code\": \"insufficient_stock\", \"message\": \"Stock changed while checking out. No order was placed; review your cart.\"}"}}].

Return expressions (source branches,not a validated schema): [{"line": 3414, "expression": "doc_out(order_doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3247, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3381, "expression": "prior_response", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3335, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3389, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3398, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-063 — POST `/api/orders/{order_id}/confirm-upi-payment`

Classification: **VERIFIED — source declarations only**. Function `confirm_grocery_upi_payment`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3418>).

```python
confirm_grocery_upi_payment(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3427, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 3432, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This order is not a direct UPI order\""}}, {"line": 3436, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order is not awaiting UPI confirmation\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3442, "expression": "doc_out(await db.orders.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3434, "expression": "doc_out(order)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-064 — GET `/api/orders/mine`

Classification: **VERIFIED — source declarations only**. Function `my_orders`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3446>).

```python
my_orders(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3448, "expression": "[{**doc_out(r), \"refund_summary\": _refund_summary(r)} async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-065 — POST `/api/orders/{order_id}/cancel`

Classification: **VERIFIED — source declarations only**. Function `cancel_grocery_order`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3522>).

```python
cancel_grocery_order(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3524, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Only the customer who placed this order can cancel it\""}}, {"line": 3528, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3529, "expression": "await _cancel_grocery_order(oid, user, \"Cancelled by customer\")", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-066 — GET `/api/shops/{shop_id}/orders`

Classification: **VERIFIED — source declarations only**. Function `shop_orders`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3533>).

```python
shop_orders(shop_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3537, "expression": "[doc_out(r) async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-067 — PATCH `/api/orders/{order_id}/status`

Classification: **VERIFIED — source declarations only**. Function `update_order_status`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3541>).

```python
update_order_status(order_id: str, body: OrderStatusUpdate, user: dict=Depends(get_current_user))
```

Request declarations: OrderStatusUpdate. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3550, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 3573, "arguments": [], "keywords": {"status_code": "409", "detail": "f\"Invalid order status transition: {order.get('status')} → {body.status}\""}}, {"line": 3584, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order status changed; refresh before trying again\""}}, {"line": 3547, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 3557, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 3562, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Only a new, unaccepted order can be declined\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3590, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3564, "expression": "fresh", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-068 — GET `/api/orders/{order_id}`

Classification: **VERIFIED — source declarations only**. Function `get_grocery_order_details`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3634>).

```python
get_grocery_order_details(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3638, "arguments": [], "keywords": {"status_code": "403", "detail": "\"You are not allowed to view this order\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3639, "expression": "doc_out(order)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-069 — GET `/api/orders/{order_id}/tracking`

Classification: **VERIFIED — source declarations only**. Function `get_order_tracking`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3643>).

```python
get_order_tracking(order_id: str, kind: str=Query(default='grocery', pattern='^(grocery|restaurant|local_shop)$'), user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3646, "arguments": [], "keywords": {"status_code": "403", "detail": "\"You are not allowed to view this order's tracking\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3650, "expression": "{\n        \"order_id\": str(order.get(\"_id\")), \"kind\": kind, \"status\": status_value,\n        \"status_history\": [\n            {\"status\": entry.get(\"status\"), \"at\": entry.get(\"at\"), \"note\": entry.get(\"note\", \"\")}\n            for entry in (order.get(\"status_history\") or [])\n            if isinstance(entry, dict) and entry.get(\"status\") and entry.get(\"at\") is not None\n        ],\n        \"tracking_active\": bool(active and point),\n        \"location\": ({\"latitude\": point.get(\"latitude\"), \"longitude\": point.get(\"longitude\"), \"accuracy_m\": point.get(\"accuracy_m\"), \"updated_at\": point.get(\"updated_at\")} if point else None),\n        \"eta_minutes\": None, \"map_provider\": None,\n        \"message\": \"Live location is not available yet.\" if active and not point else (\"Tracking ended for this order.\" if not active else \"Latest authorized delivery-device location.\"),\n    }", "literal_dict_keys": ["order_id", "kind", "status", "status_history", "tracking_active", "location", "eta_minutes", "map_provider", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-070 — POST `/api/orders/{order_id}/tracking/location`

Classification: **VERIFIED — source declarations only**. Function `update_order_tracking_location`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3665>).

```python
update_order_tracking_location(order_id: str, body: DeliveryLocationUpdateIn, kind: str=Query(default='grocery', pattern='^(grocery|restaurant|local_shop)$'), user: dict=Depends(get_current_user))
```

Request declarations: DeliveryLocationUpdateIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3681, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Location updates are allowed only while a delivery is out for delivery\""}}, {"line": 3690, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order status changed; location update was not saved\""}}, {"line": 3669, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 3679, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Only the authorized order operator can update delivery location\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3691, "expression": "{\"ok\": True, \"updated_at\": point[\"updated_at\"]}", "literal_dict_keys": ["ok", "updated_at"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-071 — POST `/api/requests/anything`

Classification: **VERIFIED — source declarations only**. Function `submit_request_anything`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3700>).

```python
submit_request_anything(body: RequestAnythingIn, request: Request)
```

Request declarations: RequestAnythingIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3716, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-072 — GET `/api/requests/anything/mine`

Classification: **VERIFIED — source declarations only**. Function `my_requests_anything`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3720>).

```python
my_requests_anything(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3722, "expression": "[doc_out(r) async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-073 — POST `/api/requests/assist`

Classification: **VERIFIED — source declarations only**. Function `submit_agent_assist`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3726>).

```python
submit_agent_assist(body: AgentAssistIn, request: Request)
```

Request declarations: AgentAssistIn. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3742, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-074 — GET `/api/admin/announcements`

Classification: **VERIFIED — source declarations only**. Function `admin_announcements`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3769>).

```python
admin_announcements(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3771, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-075 — POST `/api/admin/announcements`

Classification: **VERIFIED — source declarations only**. Function `create_announcement`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3775>).

```python
create_announcement(body: AnnouncementIn, user: dict=Depends(require_role('admin')))
```

Request declarations: AnnouncementIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3780, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-076 — PATCH `/api/admin/announcements/{announcement_id}`

Classification: **VERIFIED — source declarations only**. Function `set_announcement_active`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3784>).

```python
set_announcement_active(announcement_id: str, body: dict, _: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3815, "arguments": [], "keywords": {"status_code": "422", "detail": "\"No editable announcement fields supplied\""}}, {"line": 3823, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Announcement not found\""}}, {"line": 3789, "arguments": [], "keywords": {"status_code": "422", "detail": "\"active must be a boolean\""}}, {"line": 3799, "arguments": [], "keywords": {"status_code": "422", "detail": "\"audience must be all, customers or shopkeepers\""}}, {"line": 3819, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Announcement not found\""}}, {"line": 3795, "arguments": [], "keywords": {"status_code": "422", "detail": "f\"{field} must be {lo}-{hi} characters\""}}, {"line": 3812, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Expiry must be in the future\""}}, {"line": 3809, "arguments": [], "keywords": {"status_code": "422", "detail": "\"expires_at must be an ISO date-time\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3824, "expression": "doc_out(await db.announcements.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-077 — GET `/api/admin/dashboard`

Classification: **VERIFIED — source declarations only**. Function `admin_dashboard`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3828>).

```python
admin_dashboard(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3839, "expression": "{\n        \"users\": {\"total\": sum(users.values()), \"by_role\": users},\n        \"shops\": {\"total\": sum(shops.values()), \"by_status\": shops, \"pending_approval\": shops.get(\"pending\", 0)},\n        \"restaurants\": {\"total\": sum(restaurants.values()), \"by_status\": restaurants, \"pending_approval\": restaurants.get(\"pending\", 0)},\n        \"grocery_orders\": {\"total\": sum(orders.values()), \"by_status\": orders, \"last_24h\": await db.orders.count_documents({\"created_at\": {\"$gte\": since}})},\n        \"restaurant_orders\": {\"total\": sum(food_orders.values()), \"by_status\": food_orders, \"last_24h\": await db.restaurant_orders.count_documents({\"created_at\": {\"$gte\": since}})},\n        \"delivered_grocery_gross_inr\": round(float(revenue[0][\"total\"]) if revenue else 0.0, 2),\n        \"open_support_tickets\": await db.restaurant_support.count_documents({\"status\": {\"$nin\": [\"resolved\", \"closed\"]}}),\n        \"open_requests\": await db.request_anything.count_documents({\"status\": {\"$nin\": [\"completed\", \"cancelled\"]}}),\n        \"active_announcements\": await db.announcements.count_documents({\"active\": True}),\n        \"push_configured\": False,\n    }", "literal_dict_keys": ["users", "shops", "restaurants", "grocery_orders", "restaurant_orders", "delivered_grocery_gross_inr", "open_support_tickets", "open_requests", "active_announcements", "push_configured"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 3832, "expression": "{str(r[\"_id\"]): r[\"n\"] async for r in coll.aggregate([{\"$group\": {\"_id\": f\"${field}\", \"n\": {\"$sum\": 1}}}])}", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-078 — GET `/api/announcements/active`

Classification: **VERIFIED — source declarations only**. Function `active_announcements`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3854>).

```python
active_announcements(user: Optional[dict]=Depends(get_current_user_optional))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user_optional"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3863, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-079 — GET `/api/admin/users`

Classification: **VERIFIED — source declarations only**. Function `admin_users`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3871>).

```python
admin_users(_: dict=Depends(require_role('admin')), limit: int=Query(default=500, ge=1, le=1000))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3873, "expression": "[doc_out(row) async for row in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-080 — PATCH `/api/admin/users/{user_id}/role`

Classification: **VERIFIED — source declarations only**. Function `admin_update_user_role`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3877>).

```python
admin_update_user_role(user_id: str, body: AdminRoleUpdateIn, user: dict=Depends(require_role('admin')))
```

Request declarations: AdminRoleUpdateIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 3880, "arguments": [], "keywords": {"status_code": "409", "detail": "\"You cannot remove your own admin role from this session\""}}, {"line": 3883, "arguments": [], "keywords": {"status_code": "404", "detail": "\"User not found\""}}, {"line": 3887, "arguments": [], "keywords": {"status_code": "409", "detail": "\"The last admin account cannot be demoted\""}}].

Return expressions (source branches,not a validated schema): [{"line": 3890, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-081 — GET `/api/admin/shops`

Classification: **VERIFIED — source declarations only**. Function `admin_shops`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3894>).

```python
admin_shops(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3896, "expression": "[doc_out(r) async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-082 — PATCH `/api/admin/shops/{shop_id}/status`

Classification: **VERIFIED — source declarations only**. Function `admin_set_shop_status`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3904>).

```python
admin_set_shop_status(shop_id: str, body: ShopApprovalIn, _: dict=Depends(require_role('admin')))
```

Request declarations: ShopApprovalIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3913, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-083 — GET `/api/admin/orders`

Classification: **VERIFIED — source declarations only**. Function `admin_orders`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3917>).

```python
admin_orders(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 3919, "expression": "[doc_out(r) async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-084 — POST `/api/earnings/orders/{kind}/{order_id}/cash-collected`

Classification: **VERIFIED — source declarations only**. Function `confirm_manual_cash_collection`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4065>).

```python
confirm_manual_cash_collection(kind: Literal['grocery', 'restaurant'], order_id: str, body: CashCollectionIn, user: dict=Depends(get_current_user))
```

Request declarations: CashCollectionIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4067, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 4069, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Explicit cash collection confirmation is required\""}}, {"line": 4092, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Only unconfirmed cash/COD orders can be manually collected\""}}, {"line": 4094, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Cash collection can only be confirmed after delivery or pickup\""}}, {"line": 4100, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order payment state changed concurrently; refresh and retry\""}}, {"line": 4073, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 4079, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Restaurant order not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4104, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4083, "expression": "doc_out(order)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4099, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-085 — GET `/api/admin/earnings`

Classification: **VERIFIED — source declarations only**. Function `admin_earnings`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4121>).

```python
admin_earnings(start_date: Optional[str]=None, end_date: Optional[str]=None, user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4142, "expression": "{\"selected\": _financial_summary(selected), \"today\": _financial_summary(today_rows), \"current_month\": _financial_summary(month_rows),\n            \"ledger_earnings\": {\"selected\": selected_ledger, \"today\": today_ledger, \"current_month\": month_ledger},\n            \"expenses\": {\"available\": False, \"reason\": \"No supported expense-entry source exists in the current project.\"},\n            \"other_platform_income\": {\"available\": False, \"reason\": \"No other platform-income source is configured.\"},\n            \"timezone\": tz_name, \"selected_range\": {\"start_date\": start_date, \"end_date\": end_date, \"start_utc\": start.isoformat(), \"end_exclusive_utc\": end.isoformat()},\n            \"registrations\": {\"customers\": users_count, \"shopkeepers\": shopkeepers_count, \"new_customers_in_range\": await db.users.count_documents({\"role\": \"customer\", \"created_at\": {\"$gte\": start, \"$lt\": end}}), \"new_shopkeepers_in_range\": await db.users.count_documents({\"role\": \"shopkeeper\", \"created_at\": {\"$gte\": start, \"$lt\": end}})},\n            \"shops\": {\"total\": len(shops) + len(restaurants), \"approved\": sum(1 for x in shops + restaurants if x.get(\"status\") == \"approved\"), \"pending\": sum(1 for x in shops + restaurants if x.get(\"status\") == \"pending\"), \"rejected_or_suspended\": sum(1 for x in shops + restaurants if x.get(\"status\") in {\"rejected\", \"suspended\"}), \"new_in_range\": await db.shops.count_documents({\"created_at\": {\"$gte\": start, \"$lt\": end}}) + await db.restaurants.count_documents({\"created_at\": {\"$gte\": start, \"$lt\": end}})},\n            \"referral_rewards\": {**referral_statuses, \"pending_liability_inr\": round(referral_liability, 2)},\n            \"active_users\": {\"available\": False, \"reason\": \"Reliable activity-event tracking is not configured.\"},\n            \"financial_policy_note\": \"Historical orders without an explicitly configured admin commission/fee policy are shown with unavailable net earnings; gross sales are not platform income.\"}", "literal_dict_keys": ["selected", "today", "current_month", "ledger_earnings", "expenses", "other_platform_income", "timezone", "selected_range", "registrations", "shops", "referral_rewards", "active_users", "financial_policy_note"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-086 — GET `/api/admin/earnings/ledger`

Classification: **VERIFIED — source declarations only**. Function `admin_earnings_ledger`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4155>).

```python
admin_earnings_ledger(start_date: Optional[str]=None, end_date: Optional[str]=None, page: int=Query(default=1, ge=1), page_size: int=Query(default=50, ge=1, le=100), event_type: Optional[str]=None, order_id: Optional[str]=None, user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4162, "expression": "{\"items\": rows, \"page\": page, \"page_size\": page_size, \"total\": total, \"timezone\": tz_name}", "literal_dict_keys": ["items", "page", "page_size", "total", "timezone"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-087 — GET `/api/admin/earnings/transactions`

Classification: **VERIFIED — source declarations only**. Function `admin_earnings_transactions`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4166>).

```python
admin_earnings_transactions(start_date: Optional[str]=None, end_date: Optional[str]=None, page: int=Query(default=1, ge=1), page_size: int=Query(default=50, ge=1, le=100), transaction_type: Optional[str]=None, status_filter: Optional[str]=None, order_id: Optional[str]=None, shop_id: Optional[str]=None, settlement_reference: Optional[str]=None, user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4189, "expression": "{\"items\": page_rows, \"page\": page, \"page_size\": page_size, \"total\": total, \"timezone\": tz_name}", "literal_dict_keys": ["items", "page", "page_size", "total", "timezone"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-088 — GET `/api/earnings/mine`

Classification: **VERIFIED — source declarations only**. Function `shopkeeper_earnings`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4193>).

```python
shopkeeper_earnings(start_date: Optional[str]=None, end_date: Optional[str]=None, shop_id: Optional[str]=None, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4195, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 4201, "arguments": [], "keywords": {"status_code": "403", "detail": "\"You are not authorized for this shop or restaurant\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4249, "expression": "{\"timezone\": tz_name, \"periods\": {\"today\": today_summary, \"this_week\": week_summary, \"this_month\": month_summary}, \"selected_range\": {\"start_date\": start_date, \"end_date\": end_date}, \"shops\": [{\"id\": k, \"type\": v[0], \"name\": v[1].get(\"name\", \"Restaurant\"), \"status\": v[1].get(\"status\")} for k,v in selected_ids.items()],\n            \"summary\": _financial_summary(rows), \"orders\": [{**r, \"customer_name\": r.get(\"customer_name\", \"\"), \"customer_phone\": r.get(\"customer_phone\", \"\"), \"delivery_address\": r.get(\"delivery_address\", \"\")} for r in rows[:200]],\n            \"products_sold\": [{**x, \"sales_amount\": x[\"sales_amount\"]} for x in sold.values()],\n            \"stock\": [{\"product_id\": str(p[\"_id\"]), \"shop_id\": str(p.get(\"shop_id\", \"\")), \"name\": p.get(\"name\", \"Product\"), \"stock\": int(p.get(\"stock\", 0)), \"low_stock\": 0 < int(p.get(\"stock\", 0)) <= 5, \"out_of_stock\": int(p.get(\"stock\", 0)) <= 0, \"variants\": [{\"id\": v.get(\"id\"), \"unit\": v.get(\"unit\"), \"stock\": int(v.get(\"stock\", 0))} for v in p.get(\"variants\", []) if isinstance(v, dict)]} for p in products],\n            \"settlements\": settlements, \"settlement_summary\": {\"paid_amount_inr\": float(settled_amount), \"awaiting_settlement_inr\": float(awaiting_amount), \"paid_count\": sum(1 for x in settlements if x.get(\"status\") == \"paid\"), \"awaiting_count\": sum(1 for x in settlements if x.get(\"status\") in {\"pending_review\", \"approved\", \"processing\"})}, \"bank_account\": selected_bank,\n            \"policy_note\": \"Payable/net earnings remain unavailable when the admin has not configured the actual commission, service-fee and delivery-fee beneficiary policy.\"}", "literal_dict_keys": ["timezone", "periods", "selected_range", "shops", "summary", "orders", "products_sold", "stock", "settlements", "settlement_summary", "bank_account", "policy_note"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4244, "expression": "rr", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-089 — GET `/api/admin/earnings/bank-account`

Classification: **VERIFIED — source declarations only**. Function `admin_platform_bank_account`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4290>).

```python
admin_platform_bank_account(user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4291, "expression": "await _masked_bank_account(\"platform\", \"platform\")", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-090 — PUT `/api/admin/earnings/bank-account`

Classification: **VERIFIED — source declarations only**. Function `save_admin_platform_bank_account`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4295>).

```python
save_admin_platform_bank_account(body: BankAccountIn, user: dict=Depends(require_role('admin')))
```

Request declarations: BankAccountIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4296, "expression": "await _save_bank_account(\"platform\", \"platform\", body, user[\"id\"])", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-091 — GET `/api/shops/{shop_id}/bank-account`

Classification: **VERIFIED — source declarations only**. Function `get_shop_bank_account`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4300>).

```python
get_shop_bank_account(shop_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4303, "expression": "await _masked_bank_account(\"shop\", shop_id)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-092 — PUT `/api/shops/{shop_id}/bank-account`

Classification: **VERIFIED — source declarations only**. Function `save_shop_bank_account`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4307>).

```python
save_shop_bank_account(shop_id: str, body: BankAccountIn, user: dict=Depends(get_current_user))
```

Request declarations: BankAccountIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4310, "expression": "await _save_bank_account(\"shop\", shop_id, body, user[\"id\"])", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-093 — GET `/api/restaurants/{restaurant_id}/bank-account`

Classification: **VERIFIED — source declarations only**. Function `get_restaurant_bank_account`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4314>).

```python
get_restaurant_bank_account(restaurant_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4317, "expression": "await _masked_bank_account(\"restaurant\", restaurant_id)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-094 — PUT `/api/restaurants/{restaurant_id}/bank-account`

Classification: **VERIFIED — source declarations only**. Function `save_restaurant_bank_account`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4321>).

```python
save_restaurant_bank_account(restaurant_id: str, body: BankAccountIn, user: dict=Depends(get_current_user))
```

Request declarations: BankAccountIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4324, "expression": "await _save_bank_account(\"restaurant\", restaurant_id, body, user[\"id\"])", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-095 — PATCH `/api/admin/financial-policy/{kind}/{entity_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_set_financial_policy`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4328>).

```python
admin_set_financial_policy(kind: Literal['shop', 'restaurant'], entity_id: str, body: FinancialPolicyIn, user: dict=Depends(require_role('admin')))
```

Request declarations: FinancialPolicyIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4332, "arguments": [], "keywords": {"status_code": "404", "detail": "f\"{kind.title()} not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4336, "expression": "{\"entity_type\": kind, \"entity_id\": entity_id, **{k: v for k,v in patch.items() if k != \"financial_policy_updated_by\"}}", "literal_dict_keys": ["entity_type", "entity_id"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-096 — GET `/api/admin/earnings/settlements`

Classification: **VERIFIED — source declarations only**. Function `admin_settlement_list`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4340>).

```python
admin_settlement_list(page: int=Query(default=1, ge=1), page_size: int=Query(default=50, ge=1, le=100), user: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4343, "expression": "{\"items\": rows, \"page\": page, \"page_size\": page_size, \"total\": total}", "literal_dict_keys": ["items", "page", "page_size", "total"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-097 — POST `/api/shops/{shop_id}/settlements`

Classification: **VERIFIED — source declarations only**. Function `request_shop_settlement`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4347>).

```python
request_shop_settlement(shop_id: str, body: SettlementRequestIn, user: dict=Depends(get_current_user))
```

Request declarations: SettlementRequestIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4349, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 4363, "arguments": [], "keywords": {"status_code": "409", "detail": "\"No finalized, unallocated payable orders are available. Check the commission policy and order statuses.\""}}, {"line": 4365, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Register a payout bank account before requesting settlement.\""}}, {"line": 4387, "arguments": [], "keywords": {"status_code": "409", "detail": "\"One or more orders are already allocated to another settlement request\""}}, {"line": 4390, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Settlement request could not be committed atomically; no settlement was intentionally created\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4391, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4354, "expression": "doc_out(existing)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4381, "expression": "prior_response", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4374, "expression": "doc_out(prior_doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4386, "expression": "doc_out(prior_doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-098 — POST `/api/restaurants/{restaurant_id}/settlements`

Classification: **VERIFIED — source declarations only**. Function `request_restaurant_settlement`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4395>).

```python
request_restaurant_settlement(restaurant_id: str, body: SettlementRequestIn, user: dict=Depends(get_current_user))
```

Request declarations: SettlementRequestIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4399, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 4403, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Register a payout bank account before requesting settlement.\""}}, {"line": 4410, "arguments": [], "keywords": {"status_code": "409", "detail": "\"No finalized, unallocated payable restaurant orders are available.\""}}, {"line": 4427, "arguments": [], "keywords": {"status_code": "409", "detail": "\"One or more restaurant orders are already allocated to another settlement request\""}}, {"line": 4430, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Settlement request could not be committed atomically; no settlement was intentionally created\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4431, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4401, "expression": "doc_out(existing)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4422, "expression": "prior_response", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4416, "expression": "doc_out(prior_doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4426, "expression": "doc_out(prior_doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-099 — PATCH `/api/admin/earnings/settlements/{settlement_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_settlement_decision`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4435>).

```python
admin_settlement_decision(settlement_id: str, body: SettlementDecisionIn, user: dict=Depends(require_role('admin')))
```

Request declarations: SettlementDecisionIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4438, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Settlement not found\""}}, {"line": 4441, "arguments": [], "keywords": {"status_code": "409", "detail": "f\"Cannot apply {body.decision} to settlement in {row.get('status')} state\""}}, {"line": 4443, "arguments": [], "keywords": {"status_code": "422", "detail": "\"To mark paid, confirm an actual manual bank transfer and provide its bank/provider reference. No transfer provider is configured.\""}}, {"line": 4462, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Settlement state and audit could not be committed atomically\""}}, {"line": 4453, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Settlement state changed concurrently; refresh and retry\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4463, "expression": "doc_out(await db.settlement_requests.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-100 — GET `/api/admin/requests/anything`

Classification: **VERIFIED — source declarations only**. Function `admin_requests_anything`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4467>).

```python
admin_requests_anything(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4469, "expression": "[doc_out(r) async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-101 — GET `/api/admin/requests/assist`

Classification: **VERIFIED — source declarations only**. Function `admin_agent_assist`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4473>).

```python
admin_agent_assist(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4475, "expression": "[doc_out(r) async for r in cursor]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-102 — PATCH `/api/admin/requests/anything/{req_id}/status`

Classification: **VERIFIED — source declarations only**. Function `admin_update_request`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4484>).

```python
admin_update_request(req_id: str, body: RequestStatusIn, _: dict=Depends(require_role('admin')))
```

Request declarations: RequestStatusIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4493, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Request not found\""}}, {"line": 4490, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Request not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4502, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-103 — PATCH `/api/admin/requests/assist/{req_id}/status`

Classification: **VERIFIED — source declarations only**. Function `admin_update_assist`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4506>).

```python
admin_update_assist(req_id: str, body: RequestStatusIn, _: dict=Depends(require_role('admin')))
```

Request declarations: RequestStatusIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4515, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Request not found\""}}, {"line": 4512, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Request not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4524, "expression": "doc_out(fresh)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-104 — GET `/api/restaurants`

Classification: **VERIFIED — source declarations only**. Function `list_restaurants`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4651>).

```python
list_restaurants(q: Optional[str]=None, cuisine: Optional[str]=None, min_rating: Optional[float]=Query(default=None, ge=0, le=5), max_delivery_fee: Optional[float]=Query(default=None, ge=0), available: bool=True, city: Optional[str]=None, pincode: Optional[str]=None)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4668, "arguments": [], "keywords": {"status_code": "422", "detail": "\"A valid six-digit Indian pincode is required\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4670, "expression": "[_restaurant_public(r) for r in rows]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-105 — GET `/api/restaurants/mine`

Classification: **VERIFIED — source declarations only**. Function `my_restaurants`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4673>).

```python
my_restaurants(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4674, "expression": "[doc_out(x) async for x in db.restaurants.find({\"owner_id\": user[\"id\"]}).sort(\"created_at\", -1)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-106 — POST `/api/restaurants`

Classification: **VERIFIED — source declarations only**. Function `create_restaurant`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4677>).

```python
create_restaurant(body: RestaurantIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4679, "arguments": [], "keywords": {"status_code": "403", "detail": "\"This account cannot register a restaurant\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4688, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-107 — GET `/api/restaurants/{restaurant_id}`

Classification: **VERIFIED — source declarations only**. Function `restaurant_detail`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4691>).

```python
restaurant_detail(restaurant_id: str)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4694, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Restaurant is not currently available\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4695, "expression": "_restaurant_public(restaurant)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-108 — GET `/api/restaurants/{restaurant_id}/serviceability`

Classification: **VERIFIED — source declarations only**. Function `restaurant_delivery_serviceability`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4698>).

```python
restaurant_delivery_serviceability(restaurant_id: str, pincode: Optional[str]=None)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4702, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Restaurant is not currently available\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4704, "expression": "{\"restaurant_id\": str(restaurant[\"_id\"]), **result}", "literal_dict_keys": ["restaurant_id"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-109 — PATCH `/api/restaurants/{restaurant_id}`

Classification: **VERIFIED — source declarations only**. Function `update_restaurant`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4708>).

```python
update_restaurant(restaurant_id: str, body: RestaurantIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4717, "expression": "doc_out(await _restaurant_or_404(restaurant_id))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-110 — PATCH `/api/restaurants/{restaurant_id}/availability`

Classification: **VERIFIED — source declarations only**. Function `restaurant_availability`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4720>).

```python
restaurant_availability(restaurant_id: str, body: dict, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4725, "arguments": [], "keywords": {"status_code": "422", "detail": "\"available must be a boolean\""}}, {"line": 4727, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Restaurant must be approved before accepting orders\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4729, "expression": "doc_out(await _restaurant_or_404(restaurant_id))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-111 — GET `/api/restaurants/{restaurant_id}/menu`

Classification: **VERIFIED — source declarations only**. Function `restaurant_menu`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4732>).

```python
restaurant_menu(restaurant_id: str, q: Optional[str]=None, category: Optional[str]=None)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4735, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Restaurant not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4741, "expression": "[doc_out(x) async for x in db.restaurant_menu.find(filt).sort(\"category\", 1).limit(1000)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-112 — POST `/api/restaurants/{restaurant_id}/menu`

Classification: **VERIFIED — source declarations only**. Function `create_menu_item`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4744>).

```python
create_menu_item(restaurant_id: str, body: MenuItemIn, user: dict=Depends(get_current_user))
```

Request declarations: MenuItemIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4751, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-113 — PATCH `/api/restaurants/{restaurant_id}/menu/{item_id}`

Classification: **VERIFIED — source declarations only**. Function `update_menu_item`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4754>).

```python
update_menu_item(restaurant_id: str, item_id: str, body: MenuItemIn, user: dict=Depends(get_current_user))
```

Request declarations: MenuItemIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4759, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Menu item not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4763, "expression": "doc_out(await db.restaurant_menu.find_one({\"_id\": item[\"_id\"]}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-114 — DELETE `/api/restaurants/{restaurant_id}/menu/{item_id}`

Classification: **VERIFIED — source declarations only**. Function `delete_menu_item`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4766>).

```python
delete_menu_item(restaurant_id: str, item_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4771, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Menu item not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4772, "expression": "{\"deleted\": True}", "literal_dict_keys": ["deleted"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-115 — GET `/api/addresses`

Classification: **VERIFIED — source declarations only**. Function `list_addresses`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4775>).

```python
list_addresses(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4776, "expression": "[doc_out(x) async for x in db.addresses.find({\"user_id\": user[\"id\"]}).sort(\"is_default\", -1)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-116 — POST `/api/addresses`

Classification: **VERIFIED — source declarations only**. Function `create_address`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4779>).

```python
create_address(body: AddressIn, user: dict=Depends(get_current_user))
```

Request declarations: AddressIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4786, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-117 — PATCH `/api/addresses/{address_id}`

Classification: **VERIFIED — source declarations only**. Function `update_address`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4789>).

```python
update_address(address_id: str, body: AddressIn, user: dict=Depends(get_current_user))
```

Request declarations: AddressIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4792, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Address not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4798, "expression": "doc_out(await db.addresses.find_one({\"_id\":oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-118 — DELETE `/api/addresses/{address_id}`

Classification: **VERIFIED — source declarations only**. Function `delete_address`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4801>).

```python
delete_address(address_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4804, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Address not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4805, "expression": "{\"deleted\": True}", "literal_dict_keys": ["deleted"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-119 — GET `/api/restaurant/cart`

Classification: **VERIFIED — source declarations only**. Function `get_restaurant_cart`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4812>).

```python
get_restaurant_cart(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4828, "expression": "{\"restaurant_id\":cart.get(\"restaurant_id\"),\"restaurant_name\":restaurant.get(\"name\") if restaurant else None,\"delivery_fee\":float(restaurant.get(\"delivery_fee\",0)) if restaurant else 0,\"tax_rate\":float(restaurant.get(\"tax_rate\",5)) if restaurant else 5,\"items\":output,\"updated_at\":cart.get(\"updated_at\")}", "literal_dict_keys": ["restaurant_id", "restaurant_name", "delivery_fee", "tax_rate", "items", "updated_at"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4814, "expression": "{\"restaurant_id\":None,\"items\":[]}", "literal_dict_keys": ["restaurant_id", "items"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-120 — PUT `/api/restaurant/cart`

Classification: **VERIFIED — source declarations only**. Function `save_restaurant_cart`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4831>).

```python
save_restaurant_cart(body: RestaurantCartIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantCartIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4833, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Restaurant is not accepting orders\""}}, {"line": 4838, "arguments": [], "keywords": {"status_code": "409", "detail": "\"A cart item is no longer available\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4843, "expression": "{\"saved\":True,\"restaurant_id\":body.restaurant_id,\"item_count\":len(validated)}", "literal_dict_keys": ["saved", "restaurant_id", "item_count"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-121 — DELETE `/api/restaurant/cart`

Classification: **VERIFIED — source declarations only**. Function `clear_restaurant_cart`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4846>).

```python
clear_restaurant_cart(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4848, "expression": "{\"cleared\":True}", "literal_dict_keys": ["cleared"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-122 — POST `/api/restaurant/orders`

Classification: **VERIFIED — source declarations only**. Function `create_restaurant_order`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4851>).

```python
create_restaurant_order(body: RestaurantOrderIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantOrderIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4857, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Restaurant is not accepting orders\""}}, {"line": 4859, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Delivery is unavailable; choose pickup if supported\""}}, {"line": 4861, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Pickup is unavailable\""}}, {"line": 4863, "arguments": [], "keywords": {"status_code": "400", "detail": "\"This restaurant does not support the selected payment method\""}}, {"line": 4865, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Pay-at-pickup requires pickup fulfilment\""}}, {"line": 4867, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Online payments are not configured\""}}, {"line": 4875, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Delivery address is required\""}}, {"line": 4908, "arguments": [], "keywords": {"status_code": "400", "detail": "f\"Minimum order is ₹{restaurant.get('min_order',0)}\""}}, {"line": 4872, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Saved address not found\""}}, {"line": 4887, "arguments": [], "keywords": {"status_code": "status_code", "detail": "serviceability[\"reason\"]"}}, {"line": 4892, "arguments": [], "keywords": {"status_code": "409", "detail": "\"A menu item is unavailable; refresh your cart\""}}, {"line": 4897, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Invalid menu add-on\""}}, {"line": 4902, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Invalid menu variant\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4921, "expression": "doc_out(order)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4854, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 4916, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-123 — GET `/api/restaurant/orders/mine`

Classification: **VERIFIED — source declarations only**. Function `my_restaurant_orders`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4924>).

```python
my_restaurant_orders(user: dict=Depends(require_role('customer', 'shopkeeper')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"customer\", \"shopkeeper\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4928, "expression": "[doc_out(x) async for x in db.restaurant_orders.find({\"customer_id\":user[\"id\"]}).sort(\"created_at\",-1).limit(200)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-124 — GET `/api/restaurants/{restaurant_id}/orders`

Classification: **VERIFIED — source declarations only**. Function `restaurant_orders`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4931>).

```python
restaurant_orders(restaurant_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4933, "expression": "[doc_out(x) async for x in db.restaurant_orders.find({\"restaurant_id\":restaurant_id}).sort(\"created_at\",-1).limit(500)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-125 — PATCH `/api/restaurant/orders/{order_id}/status`

Classification: **VERIFIED — source declarations only**. Function `update_restaurant_order_status`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4936>).

```python
update_restaurant_order_status(order_id: str, body: RestaurantStatusIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantStatusIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4939, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 4949, "arguments": [], "keywords": {"status_code": "409", "detail": "f\"Invalid order status transition: {order.get('status')} → {body.status}\""}}, {"line": 4960, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order status changed; refresh before trying again\""}}, {"line": 4942, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shopkeeper role required\""}}, {"line": 4946, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Only this restaurant's owner can update its orders\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4967, "expression": "doc_out(fresh_order)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-126 — POST `/api/restaurant/orders/{order_id}/cancel`

Classification: **VERIFIED — source declarations only**. Function `cancel_restaurant_order`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4970>).

```python
cancel_restaurant_order(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4972, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 4974, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This order can no longer be cancelled online; contact support\""}}, {"line": 4980, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order changed; refresh before cancelling\""}}].

Return expressions (source branches,not a validated schema): [{"line": 4981, "expression": "doc_out(await db.restaurant_orders.find_one({\"_id\":oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-127 — GET `/api/restaurant/payments/config`

Classification: **VERIFIED — source declarations only**. Function `restaurant_payment_config`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4984>).

```python
restaurant_payment_config()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 4987, "expression": "{\"razorpay_enabled\": bool(settings), \"razorpay_key_id\": settings.key_id if settings else None, \"mode\": settings.mode if settings else None, \"supported_methods\": [\"cod\", \"pickup\"] + ([\"razorpay\"] if settings else [])}", "literal_dict_keys": ["razorpay_enabled", "razorpay_key_id", "mode", "supported_methods"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-128 — POST `/api/restaurant/orders/{order_id}/payment-intent`

Classification: **VERIFIED — source declarations only**. Function `create_restaurant_payment_intent`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4990>).

```python
create_restaurant_payment_intent(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 4992, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 4996, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Online payments are not configured. Use COD or pickup payment if the restaurant supports it.\""}}, {"line": 4998, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order is not awaiting online payment\""}}, {"line": 5005, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Existing payment intent does not match the current order total\""}}, {"line": 5018, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Payment gateway is unavailable or returned a mismatched order; no payment was confirmed\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5021, "expression": "{\"gateway\":\"razorpay\",\"key_id\":key_id,\"gateway_order_id\":payload[\"id\"],\"amount\":payload[\"amount\"],\"currency\":payload[\"currency\"],\"order_ref\":order[\"ref\"]}", "literal_dict_keys": ["gateway", "key_id", "gateway_order_id", "amount", "currency", "order_ref"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5006, "expression": "{\"gateway\":\"razorpay\",\"key_id\":key_id,\"gateway_order_id\":existing[\"gateway_order_id\"],\"amount\":int(round(float(existing[\"amount\"])*100)),\"currency\":existing.get(\"currency\",\"INR\"),\"order_ref\":order[\"ref\"]}", "literal_dict_keys": ["gateway", "key_id", "gateway_order_id", "amount", "currency", "order_ref"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-129 — POST `/api/restaurant/orders/{order_id}/payment-retry`

Classification: **VERIFIED — source declarations only**. Function `retry_restaurant_payment`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5024>).

```python
retry_restaurant_payment(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5027, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 5029, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This order is not eligible for online payment retry\""}}, {"line": 5031, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Online payment is not configured\""}}, {"line": 5037, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order changed; refresh before retrying payment\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5038, "expression": "{\"retry_allowed\":True,\"order_id\":str(oid),\"message\":\"Create a new payment intent to retry. No payment has been confirmed.\"}", "literal_dict_keys": ["retry_allowed", "order_id", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-130 — POST `/api/restaurant/payments/verify`

Classification: **VERIFIED — source declarations only**. Function `verify_restaurant_payment`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5041>).

```python
verify_restaurant_payment(body: PaymentVerifyIn, user: dict=Depends(get_current_user))
```

Request declarations: PaymentVerifyIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5043, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 5045, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order is not an online-payment order\""}}, {"line": 5048, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Payment verification is not configured\""}}, {"line": 5050, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Gateway order does not belong to this Come-In order\""}}, {"line": 5052, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Payment amount does not match the order total\""}}, {"line": 5056, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This payment order has already been completed\""}}, {"line": 5058, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order is not awaiting online payment verification\""}}, {"line": 5062, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Payment signature verification failed\""}}, {"line": 5083, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Gateway payment is not captured for the exact order amount and currency\""}}, {"line": 5076, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Payment status could not be confirmed with the gateway; the order remains unpaid\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5088, "expression": "{\"verified\": True, \"order\": doc_out(fresh_order)}", "literal_dict_keys": ["verified", "order"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5055, "expression": "{\"verified\": True, \"order\": doc_out(order)}", "literal_dict_keys": ["verified", "order"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-131 — POST `/api/restaurant/payments/razorpay-webhook`

Classification: **VERIFIED — source declarations only**. Function `razorpay_webhook`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5362>).

```python
razorpay_webhook(request: Request)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [{"line": 5366, "call": "request.body()"}].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5365, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Payment webhook is not configured\""}}, {"line": 5368, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Invalid webhook signature\""}}, {"line": 5373, "arguments": [], "keywords": {"status_code": "400", "detail": "str(exc)"}}, {"line": 5378, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Webhook event identity conflicts with prior data\""}}, {"line": 5410, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Failed payment does not match persisted order\""}}, {"line": 5420, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Provider payment is linked to multiple order kinds; reconcile before refund\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5446, "expression": "{\"received\":True}", "literal_dict_keys": ["received"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5379, "expression": "{\"received\": True, \"duplicate\": True}", "literal_dict_keys": ["received", "duplicate"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5384, "expression": "{\"received\": True, \"order_kind\": \"grocery\"}", "literal_dict_keys": ["received", "order_kind"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-132 — POST `/api/restaurants/{restaurant_id}/reviews`

Classification: **VERIFIED — source declarations only**. Function `create_restaurant_review`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5449>).

```python
create_restaurant_review(restaurant_id: str, body: RestaurantReviewIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantReviewIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5452, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Only customers with a delivered order can review this restaurant\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5460, "expression": "{\"saved\":True,\"rating\":avg,\"review_count\":len(reviews)}", "literal_dict_keys": ["saved", "rating", "review_count"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-133 — POST `/api/restaurant/support`

Classification: **VERIFIED — source declarations only**. Function `create_restaurant_support`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5470>).

```python
create_restaurant_support(body: RestaurantSupportIn, user: dict=Depends(get_current_user))
```

Request declarations: RestaurantSupportIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5480, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found for this account\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5497, "expression": "doc_out(ticket)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5486, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5495, "expression": "doc_out(prior)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-134 — GET `/api/restaurant/support/mine`

Classification: **VERIFIED — source declarations only**. Function `my_restaurant_support`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5500>).

```python
my_restaurant_support(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5501, "expression": "[doc_out(x) async for x in db.restaurant_support.find({\"user_id\":user[\"id\"]}).sort(\"created_at\",-1).limit(200)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-135 — GET `/api/seller/support`

Classification: **VERIFIED — source declarations only**. Function `seller_order_support`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5504>).

```python
seller_order_support(user: dict=Depends(require_role('shopkeeper', 'restaurant')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"shopkeeper\", \"restaurant\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5517, "expression": "[doc_out(x) async for x in db.restaurant_support.find({\"order_id\": {\"$in\": list(owned_order_ids)}}).sort(\"created_at\", -1).limit(500)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 5516, "expression": "[]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-136 — PATCH `/api/seller/support/{ticket_id}`

Classification: **VERIFIED — source declarations only**. Function `seller_update_order_support`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5526>).

```python
seller_update_order_support(ticket_id: str, body: SellerSupportStatusIn, user: dict=Depends(require_role('shopkeeper', 'restaurant')))
```

Request declarations: SellerSupportStatusIn. Dependencies: ["require_role(\"shopkeeper\", \"restaurant\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5535, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Support ticket not found\""}}, {"line": 5539, "arguments": [], "keywords": {"status_code": "403", "detail": "\"This support ticket is not linked to a seller order\""}}, {"line": 5547, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Linked order not found\""}}, {"line": 5560, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Support ticket status changed; refresh before updating\""}}, {"line": 5562, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Invalid support status transition\""}}, {"line": 5570, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Support ticket status changed; refresh before updating\""}}, {"line": 5573, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Support ticket changed; refresh before updating\""}}, {"line": 5544, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Linked order not found\""}}, {"line": 5551, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Support ticket not found for this seller\""}}, {"line": 5555, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Support ticket not found for this seller\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5574, "expression": "doc_out(updated)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-137 — GET `/api/admin/restaurant/support`

Classification: **VERIFIED — source declarations only**. Function `admin_restaurant_support`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5578>).

```python
admin_restaurant_support(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5579, "expression": "[doc_out(x) async for x in db.restaurant_support.find().sort(\"created_at\",-1).limit(1000)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-138 — PATCH `/api/admin/restaurant/support/{ticket_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_update_restaurant_support`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5582>).

```python
admin_update_restaurant_support(ticket_id: str, body: dict, _: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5584, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Invalid support status\""}}, {"line": 5586, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Support ticket not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5589, "expression": "doc_out(await db.restaurant_support.find_one({\"_id\":oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-139 — POST `/api/admin/restaurant/orders/{order_id}/refund`

Classification: **VERIFIED — source declarations only**. Function `admin_refund_restaurant_order`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5670>).

```python
admin_refund_restaurant_order(order_id: str, _: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5674, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Order not found\""}}, {"line": 5676, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Only verified paid orders can be refunded\""}}, {"line": 5679, "arguments": [], "keywords": {"status_code": "409", "detail": "\"No verified online payment is linked to this order\""}}, {"line": 5687, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Captured payment does not match the eligible order amount; manual reconciliation is required\""}}, {"line": 5696, "arguments": [], "keywords": {"status_code": "409", "detail": "\"A refund is already pending, partially refunded, uncertain, or completed; reconcile with the provider before retrying\""}}, {"line": 5701, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Refund gateway is not configured\""}}, {"line": 5743, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Existing manual/provider refund activity was found. No additional refund was sent; reconcile before taking further action.\""}}, {"line": 5685, "arguments": [], "keywords": {"status_code": "409", "detail": "\"The eligible order/payment amount is invalid; manual reconciliation is required\""}}, {"line": 5729, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Existing provider refunds could not be verified. No new refund was sent; manual reconciliation is required.\""}}, {"line": 5773, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Refund outcome is uncertain. Do not retry; reconcile the payment/refund in the provider dashboard first.\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5782, "expression": "{\n        \"refund_requested\": True,\n        \"refund_status\": stored_status,\n        \"refund_id\": refund_id,\n        \"amount_paise\": eligible_paise,\n        \"message\": \"Refund status is recorded from the provider. Only a provider-confirmed completed refund triggers a ledger reversal.\",\n    }", "literal_dict_keys": ["refund_requested", "refund_status", "refund_id", "amount_paise", "message"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-140 — GET `/api/admin/restaurant/orders`

Classification: **VERIFIED — source declarations only**. Function `admin_restaurant_orders`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5792>).

```python
admin_restaurant_orders(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5793, "expression": "[doc_out(x) async for x in db.restaurant_orders.find().sort(\"created_at\",-1).limit(2000)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-141 — GET `/api/admin/restaurants`

Classification: **VERIFIED — source declarations only**. Function `admin_restaurants`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5796>).

```python
admin_restaurants(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5797, "expression": "[doc_out(x) async for x in db.restaurants.find().sort(\"created_at\",-1).limit(1000)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-142 — PATCH `/api/admin/restaurants/{restaurant_id}/status`

Classification: **VERIFIED — source declarations only**. Function `admin_restaurant_status`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5800>).

```python
admin_restaurant_status(restaurant_id: str, body: dict, _: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 5802, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Invalid restaurant status\""}}].

Return expressions (source branches,not a validated schema): [{"line": 5805, "expression": "doc_out(await _restaurant_or_404(restaurant_id))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-143 — GET `/api/home-services/fee-policy`

Classification: **VERIFIED — source declarations only**. Function `get_home_service_fee_policy`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5954>).

```python
get_home_service_fee_policy()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5956, "expression": "{\"mode\": (row or {}).get(\"mode\", \"provider\"), \"fixed_visit_fee\": float((row or {}).get(\"fixed_visit_fee\", 0)), \"currency\": \"INR\"}", "literal_dict_keys": ["mode", "fixed_visit_fee", "currency"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-144 — PATCH `/api/admin/home-services/fee-policy`

Classification: **VERIFIED — source declarations only**. Function `set_home_service_fee_policy`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5959>).

```python
set_home_service_fee_policy(body: HomeServiceFeePolicyIn, _: dict=Depends(require_role('admin')))
```

Request declarations: HomeServiceFeePolicyIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 5962, "expression": "{\"mode\": body.mode, \"fixed_visit_fee\": body.fixed_visit_fee, \"currency\": \"INR\", \"updated_at\": doc[\"updated_at\"]}", "literal_dict_keys": ["mode", "fixed_visit_fee", "currency", "updated_at"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-145 — GET `/api/home-services/providers`

Classification: **VERIFIED — source declarations only**. Function `list_service_providers`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5996>).

```python
list_service_providers(category: Optional[str]=None, q: Optional[str]=None)
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6008, "expression": "[{k:v for k,v in r.items() if k not in {\"owner_id\", \"private_notes\"}} for r in rows]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-146 — GET `/api/home-services/providers/mine`

Classification: **VERIFIED — source declarations only**. Function `my_service_provider`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6011>).

```python
my_service_provider(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6013, "expression": "doc_out(row) if row else None", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-147 — POST `/api/home-services/providers`

Classification: **VERIFIED — source declarations only**. Function `register_service_provider`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6016>).

```python
register_service_provider(body: ServiceProviderIn, user: dict=Depends(get_current_user))
```

Request declarations: ServiceProviderIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6019, "arguments": [], "keywords": {"status_code": "409", "detail": "\"A service-provider profile is already registered for this account\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6024, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-148 — PATCH `/api/home-services/providers/{provider_id}`

Classification: **VERIFIED — source declarations only**. Function `update_service_provider`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6027>).

```python
update_service_provider(provider_id: str, body: ServiceProviderIn, user: dict=Depends(get_current_user))
```

Request declarations: ServiceProviderIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6031, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}, {"line": 6032, "arguments": [], "keywords": {"status_code": "403", "detail": "\"You can only edit your own provider profile\""}}, {"line": 6029, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6034, "expression": "doc_out(await db.service_providers.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-149 — PATCH `/api/home-services/providers/{provider_id}/photo`

Classification: **VERIFIED — source declarations only**. Function `update_service_provider_photo`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6040>).

```python
update_service_provider_photo(provider_id: str, body: ServiceProviderPhotoIn, user: dict=Depends(get_current_user))
```

Request declarations: ServiceProviderPhotoIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6044, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}, {"line": 6045, "arguments": [], "keywords": {"status_code": "403", "detail": "\"You can only change your own provider photo\""}}, {"line": 6042, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}, {"line": 6049, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Photo must be uploaded by your account\""}}, {"line": 6051, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Photo URL must be an uploaded image URL\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6053, "expression": "doc_out(await db.service_providers.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-150 — POST `/api/home-services/appointments`

Classification: **VERIFIED — source declarations only**. Function `create_service_appointment`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6056>).

```python
create_service_appointment(body: ServiceAppointmentIn, user: dict=Depends(get_current_user))
```

Request declarations: ServiceAppointmentIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6060, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider is not currently available\""}}, {"line": 6061, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Appointment time must include timezone\""}}, {"line": 6062, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Choose a future appointment time\""}}, {"line": 6065, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This appointment time is not listed as available\""}}, {"line": 6068, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This provider already has a pending or confirmed booking at that time\""}}, {"line": 6058, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}, {"line": 6073, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This provider already has a pending or confirmed booking at that time\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6082, "expression": "doc_out(doc)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-151 — GET `/api/home-services/appointments/mine`

Classification: **VERIFIED — source declarations only**. Function `my_service_appointments`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6085>).

```python
my_service_appointments(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6086, "expression": "[doc_out(x) async for x in db.service_appointments.find({\"customer_id\": user[\"id\"]}).sort(\"created_at\", -1).limit(200)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-152 — GET `/api/home-services/appointments/provider`

Classification: **VERIFIED — source declarations only**. Function `provider_service_appointments`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6089>).

```python
provider_service_appointments(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6093, "expression": "[doc_out(x) async for x in db.service_appointments.find(filt).sort(\"created_at\", -1).limit(300)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6091, "expression": "[]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-153 — PATCH `/api/home-services/appointments/{appointment_id}/status`

Classification: **VERIFIED — source declarations only**. Function `update_service_appointment`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6101>).

```python
update_service_appointment(appointment_id: str, body: ServiceAppointmentStatusIn, user: dict=Depends(get_current_user))
```

Request declarations: ServiceAppointmentStatusIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6105, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Appointment not found\""}}, {"line": 6112, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Not authorized to update this appointment\""}}, {"line": 6113, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Customers may only cancel their own appointment\""}}, {"line": 6114, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Providers must reject or reschedule rather than cancel customer bookings\""}}, {"line": 6115, "arguments": [], "keywords": {"status_code": "422", "detail": "\"A new appointment time is required\""}}, {"line": 6116, "arguments": [], "keywords": {"status_code": "422", "detail": "\"Rescheduled time must include timezone and be in the future\""}}, {"line": 6117, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This appointment is already closed and cannot be changed\""}}, {"line": 6134, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Appointment changed concurrently; refresh and try again\""}}, {"line": 6103, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Appointment not found\""}}, {"line": 6123, "arguments": [], "keywords": {"status_code": "409", "detail": "\"New time is not listed as available\""}}, {"line": 6128, "arguments": [], "keywords": {"status_code": "409", "detail": "\"The new time slot is already reserved\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6141, "expression": "doc_out(await db.service_appointments.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-154 — GET `/api/admin/home-services/providers`

Classification: **VERIFIED — source declarations only**. Function `admin_service_providers`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6144>).

```python
admin_service_providers(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6145, "expression": "[doc_out(x) async for x in db.service_providers.find().sort(\"created_at\", -1).limit(500)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-155 — PATCH `/api/admin/home-services/providers/{provider_id}/approval`

Classification: **VERIFIED — source declarations only**. Function `admin_approve_service_provider`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6152>).

```python
admin_approve_service_provider(provider_id: str, body: ProviderApprovalIn, _: dict=Depends(require_role('admin')))
```

Request declarations: ProviderApprovalIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6156, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}, {"line": 6154, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Provider not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6158, "expression": "doc_out(await db.service_providers.find_one({\"_id\": oid}))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-156 — POST `/api/admin/grocery/orders/{order_id}/refund`

Classification: **VERIFIED — source declarations only**. Function `admin_refund_grocery_order`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6254>).

```python
admin_refund_grocery_order(order_id: str, body: GroceryRefundIn, user: dict=Depends(require_role('admin')))
```

Request declarations: GroceryRefundIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6256, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Admin access required\""}}, {"line": 6261, "arguments": [], "keywords": {"status_code": "409", "detail": "\"No captured online Grocery payment is eligible\""}}, {"line": 6305, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Existing provider refund found; no second refund was sent\""}}, {"line": 6265, "arguments": [], "keywords": {"status_code": "422 if body.amount_paise is not None else 409", "detail": "str(exc)"}}, {"line": 6272, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Refund records changed\""}}, {"line": 6276, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Refund already requested or requires reconciliation\""}}, {"line": 6301, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Refund history is unverified; no new refund was sent\""}}, {"line": 6319, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Refund outcome uncertain; reconcile before another request\""}}, {"line": 6280, "arguments": [], "keywords": {"status_code": "409", "detail": "str(exc)"}}].

Return expressions (source branches,not a validated schema): [{"line": 6320, "expression": "await _apply_grocery_refund_transactionally(payment[\"_id\"], oid, refund[\"id\"], refund[\"amount\"], refund[\"status\"])", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6287, "expression": "True", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6290, "expression": "{\"duplicate\": True, \"refund_status\": fresh.get(\"refund_status\"), \"provider_request_replayed\": False}", "literal_dict_keys": ["duplicate", "refund_status", "provider_request_replayed"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6274, "expression": "False", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-157 — GET `/api/admin/grocery/refunds`

Classification: **VERIFIED — source declarations only**. Function `admin_grocery_refunds`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6324>).

```python
admin_grocery_refunds(_: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6327, "expression": "[doc_out(row) async for row in db.orders.find(\n        {\"payment_method\": \"online_razorpay\", \"refund_status\": {\"$exists\": True}}, projection).limit(100)]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-158 — GET `/api/grocery/payments/config`

Classification: **VERIFIED — source declarations only**. Function `grocery_payment_config`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6332>).

```python
grocery_payment_config()
```

Request declarations: No directly annotated inventoried model. Dependencies: []. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6334, "expression": "{\"razorpay_enabled\": bool(keys), \"razorpay_key_id\": keys[0] if keys else None, \"mode\": (\"test\" if keys[0].startswith(\"rzp_test_\") else \"live\") if keys else None, \"payment_window_minutes\": GROCERY_PAYMENT_WINDOW_MINUTES}", "literal_dict_keys": ["razorpay_enabled", "razorpay_key_id", "mode", "payment_window_minutes"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-159 — POST `/api/orders/{order_id}/payment-intent`

Classification: **VERIFIED — source declarations only**. Function `create_grocery_payment_intent`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6348>).

```python
create_grocery_payment_intent(order_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6351, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Online payment is not configured. Cancel this order and choose another payment method.\""}}, {"line": 6355, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order is not awaiting online payment\""}}, {"line": 6361, "arguments": [], "keywords": {"status_code": "409", "detail": "\"The payment window expired. The order was cancelled and no payment was taken; please order again.\""}}, {"line": 6367, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Existing payment intent does not match the current order total\""}}, {"line": 6380, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Payment gateway is unavailable or returned a mismatched order; no payment was confirmed\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6383, "expression": "{\"gateway\": \"razorpay\", \"key_id\": key_id, \"gateway_order_id\": payload[\"id\"], \"amount\": amount_paise, \"currency\": \"INR\", \"order_ref\": order[\"ref\"], \"prefill\": prefill}", "literal_dict_keys": ["gateway", "key_id", "gateway_order_id", "amount", "currency", "order_ref", "prefill"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6368, "expression": "{\"gateway\": \"razorpay\", \"key_id\": key_id, \"gateway_order_id\": existing[\"gateway_order_id\"], \"amount\": amount_paise, \"currency\": \"INR\", \"order_ref\": order[\"ref\"], \"prefill\": prefill}", "literal_dict_keys": ["gateway", "key_id", "gateway_order_id", "amount", "currency", "order_ref", "prefill"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-160 — POST `/api/grocery/payments/verify`

Classification: **VERIFIED — source declarations only**. Function `verify_grocery_payment`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6470>).

```python
verify_grocery_payment(body: PaymentVerifyIn, user: dict=Depends(get_current_user))
```

Request declarations: PaymentVerifyIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6473, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Payment verification is not configured\""}}, {"line": 6478, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Gateway order does not belong to this Come-In order\""}}, {"line": 6480, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Payment amount does not match the order total\""}}, {"line": 6484, "arguments": [], "keywords": {"status_code": "409", "detail": "\"This payment order has already been completed\""}}, {"line": 6486, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Order is not awaiting online payment verification\""}}, {"line": 6490, "arguments": [], "keywords": {"status_code": "400", "detail": "\"Payment signature verification failed\""}}, {"line": 6502, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Gateway payment is not captured for the exact order amount and currency\""}}, {"line": 6505, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Payment was captured after this order closed. It is flagged for refund review; contact support.\""}}, {"line": 6498, "arguments": [], "keywords": {"status_code": "502", "detail": "\"Payment status could not be confirmed with the gateway; the order remains unpaid\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6506, "expression": "{\"verified\": True, \"order\": doc_out(fresh)}", "literal_dict_keys": ["verified", "order"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6483, "expression": "{\"verified\": True, \"order\": doc_out(order)}", "literal_dict_keys": ["verified", "order"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-161 — GET `/api/notifications/mine`

Classification: **VERIFIED — source declarations only**. Function `my_notifications`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6628>).

```python
my_notifications(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6631, "expression": "{\"items\": rows, \"unread\": unread, \"push_configured\": False}", "literal_dict_keys": ["items", "unread", "push_configured"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-162 — GET `/api/notifications/unread-count`

Classification: **VERIFIED — source declarations only**. Function `my_unread_notifications`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6635>).

```python
my_unread_notifications(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6636, "expression": "{\"unread\": await db.notifications.count_documents({\"user_id\": user[\"id\"], \"read\": False}), \"push_configured\": False}", "literal_dict_keys": ["unread", "push_configured"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-163 — POST `/api/notifications/read-all`

Classification: **VERIFIED — source declarations only**. Function `read_all_notifications`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6640>).

```python
read_all_notifications(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6642, "expression": "{\"updated\": result.modified_count}", "literal_dict_keys": ["updated"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-164 — POST `/api/notifications/{notification_id}/read`

Classification: **VERIFIED — source declarations only**. Function `read_notification`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6646>).

```python
read_notification(notification_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6650, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Notification not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6651, "expression": "{\"read\": True}", "literal_dict_keys": ["read"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-165 — GET `/api/products/{product_id}/restock-alert`

Classification: **VERIFIED — source declarations only**. Function `restock_alert_status`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6655>).

```python
restock_alert_status(product_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6656, "expression": "{\"subscribed\": bool(await db.restock_alerts.find_one({\"user_id\": user[\"id\"], \"product_id\": product_id, \"active\": True}))}", "literal_dict_keys": ["subscribed"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-166 — POST `/api/products/{product_id}/restock-alert`

Classification: **VERIFIED — source declarations only**. Function `subscribe_restock_alert`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6660>).

```python
subscribe_restock_alert(product_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6663, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Product not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6665, "expression": "{\"subscribed\": True}", "literal_dict_keys": ["subscribed"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-167 — DELETE `/api/products/{product_id}/restock-alert`

Classification: **VERIFIED — source declarations only**. Function `unsubscribe_restock_alert`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6669>).

```python
unsubscribe_restock_alert(product_id: str, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6671, "expression": "{\"subscribed\": False}", "literal_dict_keys": ["subscribed"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-168 — GET `/api/delivery-partner/provider-status`

Classification: **VERIFIED — source declarations only**. Function `delivery_partner_provider_status`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6769>).

```python
delivery_partner_provider_status(_: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6771, "expression": "{\n        \"otp\": \"ADAPTER_PENDING\",\n        \"aadhaar\": \"ADAPTER_PENDING\",\n        \"pan\": \"ADAPTER_PENDING\",\n        \"secure_document_storage\": \"ADAPTER_PENDING\",\n        \"note\": \"Vendor-specific adapters and live verification are not implemented; environment variables alone never enable verification.\",\n    }", "literal_dict_keys": ["otp", "aadhaar", "pan", "secure_document_storage", "note"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-169 — POST `/api/delivery-partner/otp/request`

Classification: **VERIFIED — source declarations only**. Function `delivery_partner_otp_request`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6781>).

```python
delivery_partner_otp_request(request: Request, user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6786, "arguments": [], "keywords": {"status_code": "503", "detail": "\"OTP provider adapter requires vendor-specific integration and verification before activation.\""}}, {"line": 6785, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Authorized OTP provider is not configured. No OTP was sent.\""}}].

Return expressions (source branches,not a validated schema): [].

### API-170 — POST `/api/delivery-partner/otp/verify`

Classification: **VERIFIED — source declarations only**. Function `delivery_partner_otp_verify`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6790>).

```python
delivery_partner_otp_verify(_: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6791, "arguments": [], "keywords": {"status_code": "503", "detail": "\"OTP verification is unavailable until the authorized provider adapter is integrated. No phone was marked verified.\""}}].

Return expressions (source branches,not a validated schema): [].

### API-171 — POST `/api/delivery-partner/identity/start`

Classification: **VERIFIED — source declarations only**. Function `delivery_partner_identity_start`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6795>).

```python
delivery_partner_identity_start(_: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6796, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Authorized Aadhaar/PAN verification providers are not integrated. Do not submit identity numbers or documents here.\""}}].

Return expressions (source branches,not a validated schema): [].

### API-172 — PUT `/api/delivery-partner/application`

Classification: **VERIFIED — source declarations only**. Function `save_delivery_partner_application`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6800>).

```python
save_delivery_partner_application(body: DeliveryPartnerDraftIn, user: dict=Depends(get_current_user))
```

Request declarations: DeliveryPartnerDraftIn. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6802, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Admin accounts cannot apply as delivery partners\""}}, {"line": 6804, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Shop Seller accounts must use their separate seller workflow\""}}, {"line": 6807, "arguments": [], "keywords": {"status_code": "409", "detail": "\"An application already exists; use its status or correction workflow\""}}, {"line": 6838, "arguments": [], "keywords": {"status_code": "409", "detail": "\"An application already exists; use its status or correction workflow\""}}, {"line": 6870, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Application save could not be confirmed; refresh its status before retrying\""}}, {"line": 6854, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Application was modified concurrently\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6862, "expression": "_dp_public(saved)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6865, "expression": "await run_transaction(client, save)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-173 — POST `/api/delivery-partner/application/submit`

Classification: **VERIFIED — source declarations only**. Function `submit_delivery_partner_application`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6874>).

```python
submit_delivery_partner_application(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6880, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Save your application first\""}}, {"line": 6882, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Mobile, Aadhaar, PAN and required documents must be verified by authorized providers before submission\""}}, {"line": 6887, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Application cannot be submitted from its current state\""}}, {"line": 6899, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Application submission could not be confirmed; refresh before retrying\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6891, "expression": "_dp_public(await db.delivery_partner_applications.find_one({\"_id\": app_doc[\"_id\"]}, session=session))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6894, "expression": "await run_transaction(client, submit)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-174 — GET `/api/delivery-partner/application/mine`

Classification: **VERIFIED — source declarations only**. Function `my_delivery_partner_application`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6903>).

```python
my_delivery_partner_application(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6907, "expression": "{**_dp_public(app_doc), \"full_name\": _dp_decrypt(app_doc[\"full_name_enc\"]), \"mobile\": _dp_decrypt(app_doc[\"mobile_enc\"]), \"residential_address\": _dp_decrypt(app_doc[\"residential_address_enc\"]), \"alternate_contact\": _dp_decrypt(app_doc[\"alternate_contact_enc\"])}", "literal_dict_keys": ["full_name", "mobile", "residential_address", "alternate_contact"], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6906, "expression": "None", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-175 — GET `/api/delivery-partner/referral`

Classification: **VERIFIED — source declarations only**. Function `delivery_partner_referral`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6911>).

```python
delivery_partner_referral(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6914, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Save an application before using referrals\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6916, "expression": "{\"code\": app_doc[\"referral_code\"] if approved else None, \"eligible_to_share\": approved, \"reward_status\": \"NOT_CONFIGURED\"}", "literal_dict_keys": ["code", "eligible_to_share", "reward_status"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-176 — GET `/api/delivery-partner/admin/applications`

Classification: **VERIFIED — source declarations only**. Function `admin_delivery_partner_applications`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6920>).

```python
admin_delivery_partner_applications(_: dict=Depends(require_role('admin')), status_filter: Optional[str]=Query(default=None, max_length=40))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [].

Return expressions (source branches,not a validated schema): [{"line": 6923, "expression": "[{\"id\": str(d[\"_id\"]), \"status\": d.get(\"status\"), \"phone_verified\": bool(d.get(\"phone_verified\")), \"aadhaar_verified\": bool(d.get(\"aadhaar_verified\")), \"pan_verified\": bool(d.get(\"pan_verified\")), \"documents_status\": d.get(\"documents_status\"), \"created_at\": d.get(\"created_at\"), \"updated_at\": d.get(\"updated_at\")} for d in docs]", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-177 — GET `/api/delivery-partner/admin/applications/{application_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_delivery_partner_application_detail`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6927>).

```python
admin_delivery_partner_application_detail(application_id: str, admin: dict=Depends(require_role('admin')))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6934, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Application not found\""}}, {"line": 6931, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Application not found\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6937, "expression": "{\"id\": application_id, \"status\": d.get(\"status\"), \"full_name\": _dp_decrypt(d[\"full_name_enc\"]), \"mobile\": _dp_decrypt(d[\"mobile_enc\"]), \"residential_address\": _dp_decrypt(d[\"residential_address_enc\"]), \"alternate_contact\": _dp_decrypt(d[\"alternate_contact_enc\"]), \"phone_verified\": bool(d.get(\"phone_verified\")), \"aadhaar_verified\": bool(d.get(\"aadhaar_verified\")), \"pan_verified\": bool(d.get(\"pan_verified\")), \"documents_status\": d.get(\"documents_status\"), \"created_at\": d.get(\"created_at\"), \"updated_at\": d.get(\"updated_at\")}", "literal_dict_keys": ["id", "status", "full_name", "mobile", "residential_address", "alternate_contact", "phone_verified", "aadhaar_verified", "pan_verified", "documents_status", "created_at", "updated_at"], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-178 — PATCH `/api/delivery-partner/admin/applications/{application_id}`

Classification: **VERIFIED — source declarations only**. Function `admin_decide_delivery_partner_application`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6941>).

```python
admin_decide_delivery_partner_application(application_id: str, body: DeliveryPartnerDecisionIn, admin: dict=Depends(require_role('admin')))
```

Request declarations: DeliveryPartnerDecisionIn. Dependencies: ["require_role(\"admin\")"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 6945, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Application not found\""}}, {"line": 6960, "arguments": [], "keywords": {"status_code": "404", "detail": "\"Application not found\""}}, {"line": 6962, "arguments": [], "keywords": {"status_code": "409", "detail": "f\"Cannot {body.decision} an application in its current state\""}}, {"line": 6967, "arguments": [], "keywords": {"status_code": "409", "detail": "\"All verification requirements must pass before approval or reactivation\""}}, {"line": 6975, "arguments": [], "keywords": {"status_code": "409", "detail": "\"Application state changed during review; refresh before retrying\""}}, {"line": 6995, "arguments": [], "keywords": {"status_code": "503", "detail": "\"Application decision could not be confirmed; refresh before retrying\""}}].

Return expressions (source branches,not a validated schema): [{"line": 6987, "expression": "_dp_public(await db.delivery_partner_applications.find_one({\"_id\": oid}, session=session))", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}, {"line": 6990, "expression": "await run_transaction(client, decide)", "literal_dict_keys": [], "scope": "Static branch expression only;not a validated runtime response schema."}].

### API-179 — GET `/api/delivery-partner/access`

Classification: **VERIFIED — source declarations only**. Function `delivery_partner_access`; [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6999>).

```python
delivery_partner_access(user: dict=Depends(get_current_user))
```

Request declarations: No directly annotated inventoried model. Dependencies: ["get_current_user"]. Manual request-body reads: [].

Declared response_model: `None`;return annotation: `None`;status_code decorator: `None`. Other explicit response declarations: {}.

Direct HTTPException sites: [{"line": 7002, "arguments": [], "keywords": {"status_code": "403", "detail": "\"Delivery Partner access requires an approved and eligible application\""}}].

Return expressions (source branches,not a validated schema): [{"line": 7003, "expression": "{\"eligible\": True, \"role\": \"delivery_partner\", \"application_id\": str(d[\"_id\"])}", "literal_dict_keys": ["eligible", "role", "application_id"], "scope": "Static branch expression only;not a validated runtime response schema."}].

## Sixty model declarations and constraints

Every field annotation/default/Field expression and validator body below is source-only. The set includes request,response and base classes;60 does not mean 60 HTTP request bodies.

### Model `BaseDoc`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:193>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| id | Optional[PyObjectId] | Field(default=None, alias="_id") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:194>) |
| created_at | datetime | Field(default_factory=now_utc) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:195>) |
| updated_at | datetime | Field(default_factory=now_utc) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:196>) |

### Model `RegisterIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:305>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | str | Field(min_length=1, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:306>) |
| email | EmailStr | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:307>) |
| password | str | Field(min_length=6, max_length=128) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:308>) |
| phone | Optional[str] | Field(default=None, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:309>) |
| referral_code | Optional[str] | Field(default=None, min_length=6, max_length=24) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:310>) |

### Model `LoginIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:313>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| email | EmailStr | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:314>) |
| password | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:315>) |

### Model `AuthOut`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:318>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| token | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:319>) |
| user | dict | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:320>) |

### Model `ReferralReviewIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:323>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| decision | Literal["approve", "reject", "hold"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:324>) |
| note | str | Field(default="", max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:325>) |
| contact_verified | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:326>) |
| contact_verification_method | Optional[Literal["email", "phone", "authorized_manual_check"]] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:327>) |
| payment_confirmed | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:328>) |
| refund_return_checks_passed | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:329>) |

### Model `ReferralRewardDecisionIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:332>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| decision | Literal["approve", "reject", "available", "processing", "paid"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:333>) |
| note | str | Field(default="", max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:334>) |
| payout_reference | Optional[str] | Field(default=None, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:335>) |

### Model `BankAccountIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:338>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| account_holder_name | str | Field(min_length=2, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:339>) |
| bank_name | str | Field(min_length=2, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:340>) |
| account_number | str | Field(min_length=8, max_length=20, pattern=r"^[0-9]{8,20}$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:341>) |
| ifsc | str | Field(min_length=11, max_length=11, pattern=r"^[A-Za-z]{4}0[A-Za-z0-9]{6}$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:342>) |

Validator source metadata:

```json
[
  {
    "name": "normalize_ifsc",
    "line": 346,
    "decorators": [
      "field_validator(\"ifsc\")",
      "classmethod"
    ],
    "source": "def normalize_ifsc(cls, value):\n        return value.strip().upper()"
  },
  {
    "name": "trim_nonblank",
    "line": 351,
    "decorators": [
      "field_validator(\"account_holder_name\", \"bank_name\")",
      "classmethod"
    ],
    "source": "def trim_nonblank(cls, value):\n        value = value.strip()\n        if not value:\n            raise ValueError(\"This field is required\")\n        return value"
  }
]
```

### Model `FinancialPolicyIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:358>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| commission_rate_percent | Decimal | Field(ge=0, le=30) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:359>) |
| platform_service_fee_inr | Decimal | Field(default=Decimal("0"), ge=0, le=100000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:360>) |
| delivery_fee_beneficiary | Literal["platform", "shopkeeper", "third_party", "not_applicable"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:361>) |

### Model `SettlementRequestIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:364>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| idempotency_key | str | Field(min_length=16, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:365>) |

### Model `CashCollectionIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:368>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| confirmed | bool | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:369>) |
| note | str | Field(default="Cash received by shop/restaurant owner", max_length=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:370>) |

### Model `SettlementDecisionIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:373>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| decision | Literal["approve", "reject", "processing", "paid", "failed", "reverse"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:374>) |
| note | str | Field(default="", max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:375>) |
| payout_reference | Optional[str] | Field(default=None, max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:376>) |
| manual_payment_confirmed | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:377>) |

### Model `ShopIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:383>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | str | Field(min_length=2, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:384>) |
| tagline | str | Field(default="", max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:385>) |
| description | str | Field(default="", max_length=1200) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:386>) |
| owner_name | str | Field(default="", max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:387>) |
| phone | str | Field(min_length=5, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:388>) |
| alt_phone | Optional[str] | Field(default=None, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:389>) |
| whatsapp | Optional[str] | Field(default=None, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:390>) |
| category_ids | List[str] | Field(default_factory=list) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:391>) |
| area | str | Field(default="", max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:392>) |
| address | str | Field(default="", max_length=400) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:393>) |
| city | str | Field(default="", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:394>) |
| state | str | Field(default="", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:395>) |
| pincode | str | Field(default="", max_length=12) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:396>) |
| latitude | Optional[float] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:397>) |
| longitude | Optional[float] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:398>) |
| hours | str | Field(default="", max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:399>) |
| holidays | List[str] | Field(default_factory=list) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:400>) |
| services | List[str] | Field(default_factory=list) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:401>) |
| delivery_available | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:402>) |
| pickup_available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:403>) |
| delivery_radius_km | Optional[float] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:404>) |
| payment_methods | List[str] | Field(default_factory=lambda: ["cod"], max_length=8) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:405>) |
| public_upi | Optional[str] | Field(default=None, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:406>) |
| shop_type | Literal["online", "offline", "both"] | "offline" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:407>) |
| offline_shop_type | Literal["grocery_kirana", "chicken", "meat", "fish", "momos", "burger", "pizza", "chinese_food", "chaat_golgappa", "other_food"] | "grocery_kirana" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:409>) |
| image_url | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:410>) |
| gallery | List[str] | Field(default_factory=list) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:411>) |
| business_registration | Optional[str] | Field(default=None, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:412>) |

Validator source metadata:

```json
[
  {
    "name": "validate_shop_payment_methods",
    "line": 416,
    "decorators": [
      "field_validator(\"payment_methods\")",
      "classmethod"
    ],
    "source": "def validate_shop_payment_methods(cls, value):\n        allowed = {\"cod\", \"cash_shop\", \"pickup\", \"upi\", \"online_stripe\", \"online_razorpay\"}\n        normalized = list(dict.fromkeys(str(item).strip().lower() for item in value))\n        invalid = set(normalized) - allowed\n        if invalid:\n            raise ValueError(\"Unsupported shop payment method\")\n        if not normalized:\n            raise ValueError(\"At least one supported shop payment method must be enabled\")\n        return normalized"
  },
  {
    "name": "validate_public_upi",
    "line": 428,
    "decorators": [
      "field_validator(\"public_upi\")",
      "classmethod"
    ],
    "source": "def validate_public_upi(cls, value):\n        if value is None or not value.strip():\n            return None\n        candidate = value.strip()\n        if len(candidate) > 80 or \"@\" not in candidate or any(ch.isspace() for ch in candidate):\n            raise ValueError(\"Enter a valid public UPI handle, e.g. shop@upi\")\n        return candidate"
  }
]
```

### Model `ProductVariantIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:440>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| id | str | Field(min_length=1, max_length=80, pattern=r"^[A-Za-z0-9._-]+$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:441>) |
| unit | str | Field(min_length=1, max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:442>) |
| price | float | Field(gt=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:443>) |
| mrp | Optional[float] | Field(default=None, ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:444>) |
| stock | int | Field(default=0, ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:445>) |
| available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:446>) |

Validator source metadata:

```json
[
  {
    "name": "variant_mrp_gte_price",
    "line": 450,
    "decorators": [
      "field_validator(\"mrp\")",
      "classmethod"
    ],
    "source": "def variant_mrp_gte_price(cls, v, info):\n        if v is not None and v < info.data.get(\"price\", 0):\n            raise ValueError(\"Variant MRP cannot be less than selling price\")\n        return v"
  }
]
```

### Model `MeasureIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:461>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| min_qty | int | Field(ge=1, le=MEASURED_QTY_LIMIT) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:462>) |
| max_qty | int | Field(ge=1, le=MEASURED_QTY_LIMIT) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:463>) |
| step | int | Field(ge=1, le=MEASURED_QTY_LIMIT) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:464>) |
| presets | List[int] | Field(default_factory=list, max_length=8) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:465>) |

Validator source metadata:

```json
[
  {
    "name": "check_range",
    "line": 468,
    "decorators": [
      "model_validator(mode=\"after\")"
    ],
    "source": "def check_range(self):\n        if self.min_qty > self.max_qty:\n            raise ValueError(\"Minimum quantity cannot exceed maximum quantity\")\n        for p in self.presets:\n            if p < self.min_qty or p > self.max_qty or (p - self.min_qty) % self.step:\n                raise ValueError(\"Each quick amount must be within min/max and match the step size\")\n        self.presets = sorted(set(self.presets))\n        return self"
  }
]
```

### Model `ProductIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:478>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | str | Field(min_length=1, max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:479>) |
| brand | str | Field(default="", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:480>) |
| unit | str | Field(default="", max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:481>) |
| price | float | Field(gt=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:482>) |
| mrp | Optional[float] | Field(default=None, ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:483>) |
| stock | int | Field(default=0, ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:484>) |
| image_url | Optional[str] | Field(default=None, max_length=2048) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:485>) |
| category_id | str | Field(min_length=1, max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:486>) |
| description | str | Field(min_length=1, max_length=1200) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:487>) |
| sku | Optional[str] | Field(default=None, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:488>) |
| available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:489>) |
| variants | Optional[List[ProductVariantIn]] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:491>) |
| sell_by | Optional[Literal["pack", "weight", "volume"]] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:493>) |
| measure | Optional[MeasureIn] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:494>) |

Validator source metadata:

```json
[
  {
    "name": "check_measured",
    "line": 497,
    "decorators": [
      "model_validator(mode=\"after\")"
    ],
    "source": "def check_measured(self):\n        if self.sell_by in MEASURED_SELL_BY:\n            if not self.measure:\n                raise ValueError(\"Measured products need min, max and step quantities\")\n            if self.variants:\n                raise ValueError(\"Measured products cannot have pack variants\")\n            self.variants = []\n            self.unit = MEASURED_SELL_BY[self.sell_by][1]\n        else:\n            self.measure = None\n        return self"
  },
  {
    "name": "trim_product_text",
    "line": 511,
    "decorators": [
      "field_validator(\"name\", \"category_id\", \"description\", \"unit\", \"brand\")",
      "classmethod"
    ],
    "source": "def trim_product_text(cls, value):\n        # React Native renders descriptions as text (not HTML). Trim user input\n        # here while preserving Hindi/Unicode and literal text safely.\n        return value.strip() if isinstance(value, str) else value"
  },
  {
    "name": "product_name_must_not_be_blank",
    "line": 518,
    "decorators": [
      "field_validator(\"name\")",
      "classmethod"
    ],
    "source": "def product_name_must_not_be_blank(cls, value):\n        if not value:\n            raise ValueError(\"Product name is required\")\n        return value"
  },
  {
    "name": "product_category_must_not_be_blank",
    "line": 525,
    "decorators": [
      "field_validator(\"category_id\")",
      "classmethod"
    ],
    "source": "def product_category_must_not_be_blank(cls, value):\n        if not value:\n            raise ValueError(\"Product category is required\")\n        return value"
  },
  {
    "name": "product_description_must_not_be_blank",
    "line": 532,
    "decorators": [
      "field_validator(\"description\")",
      "classmethod"
    ],
    "source": "def product_description_must_not_be_blank(cls, value):\n        if not value:\n            raise ValueError(\"Product description is required\")\n        return value"
  },
  {
    "name": "mrp_gte_price",
    "line": 539,
    "decorators": [
      "field_validator(\"mrp\")",
      "classmethod"
    ],
    "source": "def mrp_gte_price(cls, v, info):\n        if v is not None and v < info.data.get(\"price\", 0):\n            raise ValueError(\"MRP cannot be less than selling price\")\n        return v"
  },
  {
    "name": "normalize_sku",
    "line": 546,
    "decorators": [
      "field_validator(\"sku\")",
      "classmethod"
    ],
    "source": "def normalize_sku(cls, value):\n        value = value.strip() if value else \"\"\n        return value or None"
  },
  {
    "name": "unique_variant_ids",
    "line": 552,
    "decorators": [
      "field_validator(\"variants\")",
      "classmethod"
    ],
    "source": "def unique_variant_ids(cls, variants):\n        if variants is None:\n            return variants\n        ids = [v.id for v in variants]\n        if len(ids) != len(set(ids)):\n            raise ValueError(\"Variant IDs must be unique within a product\")\n        return variants"
  }
]
```

### Model `CartLine`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:564>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| product_id | str | Field(min_length=1, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:565>) |
| name | str | Field(default="", max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:566>) |
| unit | str | Field(default="", max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:567>) |
| price | Optional[float] | Field(default=None, ge=0) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:568>) |
| qty | int | Field(ge=1, le=MEASURED_QTY_LIMIT) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:569>) |
| image_url | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:570>) |
| shop_id | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:571>) |
| variant_id | Optional[str] | Field(default=None, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:572>) |

### Model `QuoteLineIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:575>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| product_id | str | Field(min_length=1, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:576>) |
| qty | int | Field(ge=1, le=MEASURED_QTY_LIMIT) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:577>) |
| variant_id | Optional[str] | Field(default=None, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:578>) |

### Model `GroceryQuoteIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:581>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| items | List[QuoteLineIn] | Field(min_length=1, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:582>) |
| fulfillment | Literal["delivery", "pickup"] | "delivery" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:583>) |
| use_rewards | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:584>) |

### Model `OrderIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:587>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| items | List[CartLine] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:588>) |
| delivery_address | str | Field(default="", max_length=400) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:589>) |
| fulfillment | Literal["delivery", "pickup"] | "delivery" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:590>) |
| customer_name | str | Field(default="", max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:591>) |
| customer_phone | str | Field(default="", max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:592>) |
| delivery_fee | float | Field(default=0, ge=0) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:594>) |
| payment_method | Literal["cod", "upi", "cash_shop", "pickup", "online_stripe", "online_razorpay"] | "cod" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:595>) |
| notes | str | Field(default="", max_length=400) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:596>) |
| shop_id | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:597>) |
| quote_token | Optional[str] | Field(default=None, min_length=20, max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:598>) |
| idempotency_key | Optional[str] | Field(default=None, min_length=16, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:599>) |
| confirm_price_changes | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:600>) |

Validator source metadata:

```json
[
  {
    "name": "non_empty",
    "line": 604,
    "decorators": [
      "field_validator(\"items\")",
      "classmethod"
    ],
    "source": "def non_empty(cls, v):\n        if not v:\n            raise ValueError(\"Order has no items\")\n        return v"
  }
]
```

### Model `DeliveryLocationUpdateIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:610>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| latitude | float | Field(ge=-90, le=90) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:611>) |
| longitude | float | Field(ge=-180, le=180) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:612>) |
| accuracy_m | Optional[float] | Field(default=None, ge=0, le=100000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:613>) |

Validator source metadata:

```json
[
  {
    "name": "finite_coordinate",
    "line": 617,
    "decorators": [
      "field_validator(\"latitude\", \"longitude\")",
      "classmethod"
    ],
    "source": "def finite_coordinate(cls, value):\n        import math\n        if not math.isfinite(value):\n            raise ValueError(\"Coordinates must be finite numbers\")\n        return value"
  }
]
```

### Model `OrderStatusUpdate`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:624>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal[<br>        "pending", "accepted", "preparing", "ready", "out_for_delivery", "delivered", "cancelled"<br>    ] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:625>) |
| note | str | Field(default="", max_length=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:628>) |

### Model `RequestAnythingIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:634>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| description | str | Field(min_length=1, max_length=1200) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:635>) |
| pickup | str | Field(default="", max_length=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:636>) |
| drop | str | Field(min_length=1, max_length=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:637>) |
| size | str | Field(default="Small", max_length=24) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:638>) |
| quantity | int | Field(default=1, ge=1) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:639>) |
| budget | Optional[float] | Field(default=None, ge=0) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:640>) |
| category | str | Field(default="", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:641>) |
| reference_image_url | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:642>) |
| notes | str | Field(default="", max_length=400) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:643>) |
| customer_name | str | Field(default="", max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:644>) |
| customer_phone | str | Field(default="", max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:645>) |

### Model `AgentAssistIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:648>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| shop_id | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:649>) |
| reason | str | Field(min_length=1, max_length=600) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:650>) |
| preferred_time | str | Field(default="", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:651>) |
| instructions | str | Field(default="", max_length=600) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:652>) |
| customer_name | str | Field(default="", max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:653>) |
| customer_phone | str | Field(default="", max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:654>) |

### Model `StatusCheck`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:676>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| id | str | Field(default_factory=lambda: str(uuid.uuid4())) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:677>) |
| client_name | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:678>) |
| timestamp | datetime | Field(default_factory=now_utc) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:679>) |

### Model `StatusCheckCreate`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:682>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| client_name | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:683>) |

### Model `UpdateProfileIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1063>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | Optional[str] | Field(default=None, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1064>) |
| phone | Optional[str] | Field(default=None, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1065>) |

### Model `ForgotPasswordIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1080>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| email | EmailStr | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1081>) |

### Model `ResetPasswordIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1083>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| token | str | Field(min_length=32, max_length=256) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1084>) |
| new_password | str | Field(min_length=8, max_length=128) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1085>) |

### Model `ShopAvailabilityIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1269>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| online | bool | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1270>) |

### Model `AssistantTurn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1332>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| role | Literal["user", "assistant"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1333>) |
| content | str | Field(min_length=1, max_length=1000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1334>) |

### Model `AssistantContextIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1337>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| query | str | Field(min_length=1, max_length=300) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1338>) |
| language | str | Field(default="en", pattern="^(en\|hi\|gu\|mr\|ta\|te\|bn\|pa\|kn\|ml\|or\|ur)$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1339>) |
| limit | int | Field(default=6, ge=1, le=12) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1340>) |
| history | List[AssistantTurn] | Field(default_factory=list, max_length=8) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1342>) |

### Model `ChandFeedbackIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1345>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| rating | Literal["positive", "negative"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1346>) |
| category | Literal["answer_quality", "product_match", "language", "safety", "other"] | "answer_quality" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1347>) |
| comment | str | Field(default="", max_length=1000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1348>) |
| conversation_ref | str | Field(min_length=8, max_length=80, pattern=r"^[A-Za-z0-9_-]+$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1349>) |
| request_id | str | Field(min_length=8, max_length=100, pattern=r"^[A-Za-z0-9_-]+$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1350>) |

### Model `ChandFeedbackStatusIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1353>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["reviewing", "resolved", "closed"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1354>) |
| resolution_note | str | Field(default="", max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1355>) |

### Model `MasterVariantIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1815>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| id | str | Field(min_length=1, max_length=80, pattern=r"^[A-Za-z0-9._-]+$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1816>) |
| unit | str | Field(min_length=1, max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1817>) |

### Model `MasterProductIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1820>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | str | Field(min_length=1, max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1821>) |
| brand | str | Field(default="", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1822>) |
| category_id | str | Field(min_length=1, max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1823>) |
| source_reference | str | Field(min_length=4, max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1824>) |
| description | str | Field(default="", max_length=1200) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1825>) |
| image_url | Optional[str] | Field(default=None, max_length=1000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1826>) |
| variants | List[MasterVariantIn] | Field(min_length=1, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1827>) |

Validator source metadata:

```json
[
  {
    "name": "source_reference_nonblank",
    "line": 1831,
    "decorators": [
      "field_validator(\"source_reference\")",
      "classmethod"
    ],
    "source": "def source_reference_nonblank(cls, value):\n        value = value.strip()\n        if len(value) < 4:\n            raise ValueError(\"A nonblank source reference is required\")\n        return value"
  },
  {
    "name": "master_variant_ids_unique",
    "line": 1839,
    "decorators": [
      "field_validator(\"variants\")",
      "classmethod"
    ],
    "source": "def master_variant_ids_unique(cls, variants):\n        ids = [v.id for v in variants]\n        if len(ids) != len(set(ids)):\n            raise ValueError(\"Master variant IDs must be unique\")\n        return variants"
  }
]
```

### Model `MasterLinkIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1846>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| variant_id | str | Field(min_length=1, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1847>) |
| price | float | Field(ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1848>) |
| mrp | Optional[float] | Field(default=None, ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1849>) |
| stock | int | Field(default=0, ge=0, le=100000000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1850>) |
| available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1851>) |
| sell_by | Optional[Literal["pack", "weight", "volume"]] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1853>) |
| measure | Optional[MeasureIn] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:1854>) |

Validator source metadata:

```json
[
  {
    "name": "link_mrp_gte_price",
    "line": 1858,
    "decorators": [
      "field_validator(\"mrp\")",
      "classmethod"
    ],
    "source": "def link_mrp_gte_price(cls, v, info):\n        if v is not None and v < info.data.get(\"price\", 0):\n            raise ValueError(\"MRP cannot be less than price\")\n        return v"
  },
  {
    "name": "check_link_measured",
    "line": 1864,
    "decorators": [
      "model_validator(mode=\"after\")"
    ],
    "source": "def check_link_measured(self):\n        if self.sell_by in MEASURED_SELL_BY:\n            if not self.measure:\n                raise ValueError(\"Measured listings need min, max and step quantities\")\n            if self.price <= 0:\n                raise ValueError(\"Measured listings need a price per kg / L greater than 0\")\n        else:\n            self.measure = None\n        return self"
  }
]
```

### Model `AnnouncementIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3750>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| title | str | Field(min_length=3, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3751>) |
| body | str | Field(min_length=3, max_length=1200) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3752>) |
| audience | Literal["all", "customers", "shopkeepers"] | "all" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3753>) |
| active | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3754>) |
| expires_at | Optional[datetime] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3756>) |

Validator source metadata:

```json
[
  {
    "name": "expiry_in_future",
    "line": 3760,
    "decorators": [
      "field_validator(\"expires_at\")",
      "classmethod"
    ],
    "source": "def expiry_in_future(cls, value):\n        if value is not None:\n            value = value if value.tzinfo else value.replace(tzinfo=timezone.utc)\n            if value <= datetime.now(timezone.utc):\n                raise ValueError(\"Expiry must be in the future\")\n        return value"
  }
]
```

### Model `AdminRoleUpdateIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3866>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| role | Literal["customer", "shopkeeper", "admin"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3867>) |

### Model `ShopApprovalIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3899>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["approved", "suspended", "pending"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:3900>) |

### Model `RequestStatusIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4478>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["pending", "assigned", "in_progress", "completed", "cancelled"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4479>) |
| note | str | Field(default="", max_length=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4480>) |

### Model `AddressIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4535>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| label | str | Field(default="Home", min_length=1, max_length=40) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4536>) |
| recipient_name | str | Field(min_length=1, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4537>) |
| phone | str | Field(min_length=5, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4538>) |
| address_line | str | Field(min_length=5, max_length=400) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4539>) |
| city | str | Field(min_length=1, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4540>) |
| state | str | Field(min_length=1, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4541>) |
| pincode | str | Field(min_length=4, max_length=12) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4542>) |
| latitude | Optional[float] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4543>) |
| longitude | Optional[float] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4544>) |
| is_default | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4545>) |

### Model `RestaurantIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4547>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | str | Field(min_length=2, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4548>) |
| description | str | Field(default="", max_length=1600) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4549>) |
| cuisines | List[str] | Field(default_factory=list, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4550>) |
| phone | str | Field(min_length=5, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4551>) |
| address | str | Field(min_length=5, max_length=400) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4552>) |
| city | str | Field(min_length=1, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4553>) |
| image_url | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4554>) |
| delivery_available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4555>) |
| delivery_serviceable_pincodes | Optional[List[str]] | Field(default=None, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4557>) |
| pickup_available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4558>) |
| payment_methods | List[Literal["cod", "pickup", "razorpay"]] | Field(default_factory=lambda: ["cod", "pickup"], max_length=3) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4559>) |
| delivery_fee | float | Field(default=0, ge=0, le=10000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4560>) |
| tax_rate | float | Field(default=5, ge=0, le=30) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4561>) |
| min_order | float | Field(default=0, ge=0) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4562>) |
| estimated_minutes | int | Field(default=35, ge=5, le=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4563>) |

Validator source metadata:

```json
[
  {
    "name": "validate_delivery_serviceable_pincodes",
    "line": 4567,
    "decorators": [
      "field_validator(\"delivery_serviceable_pincodes\")",
      "classmethod"
    ],
    "source": "def validate_delivery_serviceable_pincodes(cls, value):\n        if value is None:\n            return value\n        normalized = []\n        for item in value:\n            pincode = normalize_pincode(item)\n            if not pincode:\n                raise ValueError(\"Delivery coverage must contain valid six-digit Indian pincodes\")\n            if pincode not in normalized:\n                normalized.append(pincode)\n        return normalized"
  }
]
```

### Model `MenuItemIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4579>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| name | str | Field(min_length=1, max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4580>) |
| description | str | Field(default="", max_length=1200) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4581>) |
| category | str | Field(default="Main", max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4582>) |
| price | float | Field(ge=0, le=100000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4583>) |
| image_url | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4584>) |
| available | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4585>) |
| vegetarian | Optional[bool] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4586>) |
| variants | List[dict] | Field(default_factory=list, max_length=30) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4587>) |
| add_ons | List[dict] | Field(default_factory=list, max_length=50) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4588>) |

### Model `RestaurantOrderLineIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4590>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| menu_item_id | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4591>) |
| quantity | int | Field(ge=1, le=99) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4592>) |
| variant_id | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4593>) |
| add_on_ids | List[str] | Field(default_factory=list, max_length=50) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4594>) |
| instructions | str | Field(default="", max_length=300) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4595>) |

### Model `RestaurantOrderIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4597>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| restaurant_id | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4598>) |
| items | List[RestaurantOrderLineIn] | Field(min_length=1, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4599>) |
| address_id | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4600>) |
| delivery_address | Optional[str] | Field(default=None, max_length=700) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4601>) |
| contact_name | str | Field(min_length=1, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4602>) |
| contact_phone | str | Field(min_length=5, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4603>) |
| fulfillment | Literal["delivery", "pickup"] | "delivery" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4604>) |
| payment_method | Literal["cod", "pickup", "razorpay"] | "cod" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4605>) |
| notes | str | Field(default="", max_length=600) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4606>) |
| idempotency_key | str | Field(min_length=8, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4607>) |

### Model `RestaurantStatusIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4609>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["accepted", "rejected", "preparing", "ready", "picked_up", "out_for_delivery", "delivered", "cancelled"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4610>) |
| note | str | Field(default="", max_length=300) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4611>) |

### Model `PaymentVerifyIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4613>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| order_id | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4614>) |
| razorpay_order_id | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4615>) |
| razorpay_payment_id | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4616>) |
| razorpay_signature | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4617>) |

### Model `RestaurantReviewIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4619>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| rating | int | Field(ge=1, le=5) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4620>) |
| comment | str | Field(default="", max_length=1000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4621>) |

### Model `RestaurantCartIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4807>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| restaurant_id | str | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4808>) |
| items | List[RestaurantOrderLineIn] | Field(default_factory=list, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:4809>) |

### Model `RestaurantSupportIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5462>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| order_id | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5463>) |
| order_kind | Literal["grocery", "restaurant"] | "restaurant" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5464>) |
| category | Literal["order", "payment", "refund", "restaurant", "other", "order_late", "wrong_or_missing_item", "damaged_item", "cancellation_help", "payment_issue", "refund_status"] | "order" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5465>) |
| request_id | Optional[str] | Field(default=None, min_length=8, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5466>) |
| message | str | Field(min_length=5, max_length=2000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5467>) |

### Model `SellerSupportStatusIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5520>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["in_progress", "resolved"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5521>) |
| expected_status | Literal["open", "in_progress"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5522>) |

### Model `HomeServiceFeePolicyIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5948>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| mode | Literal["provider", "fixed", "waived"] | "provider" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5949>) |
| fixed_visit_fee | float | Field(default=0, ge=0, le=100000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5950>) |
| currency | Literal["INR"] | "INR" | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5951>) |

### Model `ServiceProviderIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5970>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| full_name | str | Field(min_length=2, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5971>) |
| category | str | Field(min_length=2, max_length=80) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5972>) |
| specializations | List[str] | Field(default_factory=list, max_length=30) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5973>) |
| phone | str | Field(min_length=5, max_length=20) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5974>) |
| photo_url | Optional[str] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5975>) |
| experience_years | int | Field(default=0, ge=0, le=70) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5976>) |
| description | str | Field(default="", max_length=2000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5977>) |
| tasks | List[str] | Field(default_factory=list, max_length=50) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5978>) |
| service_area | str | Field(min_length=2, max_length=240) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5979>) |
| working_hours | str | Field(default="", max_length=160) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5980>) |
| available_slots | List[str] | Field(default_factory=list, max_length=100) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5981>) |
| service_charge | Optional[float] | Field(default=None, ge=0) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5982>) |
| visit_fee | float | Field(default=0, ge=0) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5983>) |
| additional_charges | str | Field(default="", max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5984>) |
| quotation_required | bool | True | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5985>) |
| payment_preferences | List[Literal["cash_after_service", "cash_visit_fee"]] | Field(default_factory=lambda: ["cash_after_service"], max_length=2) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5986>) |

### Model `ServiceAppointmentIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5988>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| provider_id | str | Field(min_length=1, max_length=64) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5989>) |
| requested_service | str | Field(min_length=2, max_length=600) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5990>) |
| appointment_at | datetime | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5991>) |
| address | str | Field(min_length=3, max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5992>) |
| notes | str | Field(default="", max_length=1000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:5993>) |

### Model `ServiceProviderPhotoIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6036>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| photo_url | str | Field(min_length=1, max_length=1000) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6037>) |

### Model `ServiceAppointmentStatusIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6095>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["accepted", "rejected", "rescheduled", "cancelled"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6096>) |
| note | str | Field(default="", max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6097>) |
| rescheduled_at | Optional[datetime] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6098>) |

### Model `ProviderApprovalIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6147>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| status | Literal["approved", "rejected", "suspended"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6148>) |
| is_active | bool | False | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6149>) |

### Model `GroceryRefundIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6180>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| request_id | str | Field(min_length=8, max_length=100, pattern=r"^[A-Za-z0-9_-]+$") | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6181>) |
| reason | str | Field(min_length=3, max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6182>) |
| amount_paise | Optional[int] | Field(default=None, gt=0, strict=True) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6183>) |

### Model `DeliveryPartnerDraftIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6683>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| full_name | str | Field(min_length=2, max_length=120) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6684>) |
| mobile | str | Field(min_length=10, max_length=16) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6685>) |
| residential_address | str | Field(min_length=8, max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6686>) |
| alternate_contact | str | Field(min_length=10, max_length=16) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6687>) |
| consent_identity_verification | bool | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6688>) |
| consent_data_processing | bool | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6689>) |
| consent_declaration | bool | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6690>) |
| referral_code | Optional[str] | Field(default=None, min_length=6, max_length=24) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6691>) |

Validator source metadata:

```json
[
  {
    "name": "normalize_indian_phone",
    "line": 6695,
    "decorators": [
      "field_validator(\"mobile\", \"alternate_contact\")",
      "classmethod"
    ],
    "source": "def normalize_indian_phone(cls, value: str) -> str:\n        digits = re.sub(r\"\\D\", \"\", value)\n        if len(digits) == 12 and digits.startswith(\"91\"):\n            digits = digits[2:]\n        if len(digits) != 10 or digits[0] not in \"6789\":\n            raise ValueError(\"Enter a valid 10-digit Indian mobile number\")\n        return digits"
  },
  {
    "name": "trim_required_text",
    "line": 6705,
    "decorators": [
      "field_validator(\"full_name\", \"residential_address\")",
      "classmethod"
    ],
    "source": "def trim_required_text(cls, value: str) -> str:\n        value = \" \".join(value.split())\n        if not value:\n            raise ValueError(\"This field is required\")\n        return value"
  },
  {
    "name": "validate_consent_and_contacts",
    "line": 6712,
    "decorators": [
      "model_validator(mode=\"after\")"
    ],
    "source": "def validate_consent_and_contacts(self):\n        if self.mobile == self.alternate_contact:\n            raise ValueError(\"Alternate contact must be different from the applicant mobile\")\n        if not (self.consent_identity_verification and self.consent_data_processing and self.consent_declaration):\n            raise ValueError(\"All required consents must be accepted\")\n        return self"
  }
]
```

### Model `DeliveryPartnerDecisionIn`

**VERIFIED — source declarations only**;bases: `BaseModel`;[server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6720>).

| Field | Annotation | Default / constraints | Source line |
| --- | --- | --- | --- |
| decision | Literal["approve", "reject", "correction", "suspend", "reactivate"] | None | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6721>) |
| reason | str | Field(min_length=3, max_length=500) | [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6722>) |

## GET probe side effects — no requests executed

The conservative AST-local call graph inspects81 GET handlers. Three have recognized potential Mongo write paths;all81entries and the analysis are in [get-side-effect-inventory.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/iteration-2026-11-18T072632-0800/get-side-effect-inventory.json>) and [augment-api-effects.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/iteration-2026-11-18T072632-0800/augment-api-effects.py>). The analysis follows local functions and dependency helpers;unresolved dynamic/external effects mean the remaining 78 are **not certified pure**. A potential site is not proof every branch writes.

| GET endpoint | Handler | Potential direct/transitive write | Classification |
| --- | --- | --- | --- |
| /api/referrals/me | [referral_dashboard](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:901>) | db.users.update_one via _ensure_referral_code [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:722>) | VERIFIED — source possibility only |
| /api/referral/validate | [validate_referral](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:943>) | db.referral_link_events.insert_one via validate_referral [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:945>) | VERIFIED — source possibility only |
| /api/delivery-partner/admin/applications/{application_id} | [admin_delivery_partner_application_detail](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6927>) | db.delivery_partner_audit.insert_one via admin_delivery_partner_application_detail [server.py](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py:6936>) | VERIFIED — source possibility only |

No evidence here authorizes a GET probe or marks an API,button,screen,auth boundary or workflow runtime-accepted.
