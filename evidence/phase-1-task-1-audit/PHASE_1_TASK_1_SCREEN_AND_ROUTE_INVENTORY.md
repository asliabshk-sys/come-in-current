# PHASE 1 TASK 1 — Screen, Route and Action Inventory

Audit timestamp: 2026-11-18T06:59:35.322181-08:00 (UTC−08). **Final status: REVIEW PENDING.** Canonical Phase1/Task1=Existing Project Audit under the recovered22-task roadmap. Roadmap Recovery is preserved and is not proof that this application audit passed. No canonical task added/renamed/merged/renumbered. Task2/implementation NOT STARTED. Only files in `/workspace/come-in-current/evidence/phase-1-task-1-audit` are created/updated. Existing source,ZIP,patches and all five checkpoints are protected unchanged.

Evidence labels: **SOURCE VERIFIED**=located in current code/document;**STATICALLY VERIFIED**=read-only parser/structural check;**TEST EVIDENCE FOUND**=persisted result with date/scope,not freshly run;**RUNTIME VERIFIED**=only the specified actual runtime observation;**EXTERNAL INTEGRATION VERIFIED**=requires real external provider evidence (none newly established);**HISTORICAL REPORT ONLY**,**NOT FOUND**,**UNVERIFIED**,**BLOCKED** retain their narrow meaning.

Allowed item statuses: VERIFIED,PARTIALLY VERIFIED,NOT IMPLEMENTED,NOT FOUND,HISTORICAL CLAIM ONLY,UNVERIFIED,BLOCKED,REVIEW REQUIRED. A VERIFIED inventory/declaration is not VERIFIED business behavior. Owner approval for audit acceptance/fixes/Task2 remains pending.

## Scope and interpretation

53 app TSX files were read/parsed:2 layouts,1 HTML document and50 page/redirect/not-found entries. Shared modules bring the parsed TS/TSX set to95;0 parser diagnostics is syntax evidence only,not a fresh semantic TypeScript check.579 JSX event bindings across app/shared source are indexed.108 literal router targets resolve to existing route/group/public-path candidates;dynamic runtime navigation remains UNVERIFIED. Zero duplicate FastAPI registrations found separately;frontend aliases/overlapping public paths need framework-aware interpretation.

Every row has SOURCE VERIFIED route/binding evidence and item status PARTIALLY VERIFIED unless it is a static layout/intentional alias. A source file or nonempty callback does not prove rendering,working business actions or all empty/error states. State columns below are lexical source markers,not UI tests. An absent marker may be handled by a child/shared component or a screen with no async operation;it is not automatically a bug. Render evidence covers only the historically exercised pages listed below.

Historical browser evidence18Nov2026:Home/CHAND entry,voice-typing navigation/focus and four mode cards (5checks);real customer/seller/Restaurant-owner/admin UI logins plus/orders,/delivery-partner,/seller/products,/seller/support,/restaurant/dashboard,/restaurant/orders,/admin,/admin-delivery-partners (12checks). Scope:web login/navigation/render only,not every control/native/provider workflow. See root evidence/resume-20261118/home-chand-browser.json and browser-roles-v2.json. These were NOT rerun. No new browser navigation/clicks were performed because arbitrary UI effects may write local/app data.

## Complete app route/layout inventory

| File / source | Logical route;public path | Kind / redirect | Events / direct API calls | Loading / empty / error markers | Render evidence / status |
|---|---|---|---|---|---|
| [frontend/app/(tabs)/_layout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/_layout.tsx:1>) | `/(tabs)/_layout`;`/_layout` | layout/document;redirect=False | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:1>) | `/(tabs)/account`;`/account` | route/layout;redirect=False | 11/0 | 0/1/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:1>) | `/(tabs)/cart`;`/cart` | route/layout;redirect=False | 11/0 | 0/13/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/(tabs)/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/categories.tsx:1>) | `/(tabs)/categories`;`/categories` | route/layout;redirect=False | 2/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:1>) | `/(tabs)/index`;`/` | route/layout;redirect=False | 25/6 | 0/0/2 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/(tabs)/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/search.tsx:1>) | `/(tabs)/search`;`/search` | route/layout;redirect=False | 4/0 | 0/3/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/+html.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/+html.tsx:1>) | `/+html`;`/+html` | layout/document;redirect=False | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/+not-found.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/+not-found.tsx:1>) | `/+not-found`;`/+not-found` | route/layout;redirect=False | 0/0 | 0/1/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/_layout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/_layout.tsx:1>) | `/_layout`;`/_layout` | layout/document;redirect=False | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:1>) | `/addresses`;`/addresses` | route/layout;redirect=False | 4/4 | 0/1/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:1>) | `/admin-delivery-partners`;`/admin-delivery-partners` | route/layout;redirect=False | 9/6 | 2/0/3 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:1>) | `/admin-earnings`;`/admin-earnings` | route/layout;redirect=False | 28/10 | 6/3/7 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:1>) | `/admin`;`/admin` | route/layout;redirect=False | 62/55 | 4/1/27 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:1>) | `/auth`;`/auth` | route/layout;redirect=False | 8/0 | 9/0/5 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:1>) | `/become-seller`;`/become-seller` | route/layout;redirect=False | 40/3 | 11/5/12 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/category/[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:1>) | `/category/[slug]`;`/category/[slug]` | route/layout;redirect=False | 2/0 | 0/5/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:1>) | `/chand`;`/chand` | route/layout;redirect=False | 51/12 | 20/3/21 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:1>) | `/checkout`;`/checkout` | route/layout;redirect=False | 18/8 | 3/2/15 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:1>) | `/delivery-address`;`/delivery-address` | route/layout;redirect=False | 6/0 | 4/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:1>) | `/delivery-partner`;`/delivery-partner` | route/layout;redirect=False | 5/4 | 4/0/4 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/index.tsx:1>) | `/index`;`/` | route/layout;redirect=True | 0/0 | 0/0/0 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/language.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/language.tsx:1>) | `/language`;`/language` | route/layout;redirect=False | 3/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:1>) | `/notifications`;`/notifications` | route/layout;redirect=False | 3/8 | 6/1/6 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/order-tracking.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/order-tracking.tsx:1>) | `/order-tracking`;`/order-tracking` | route/layout;redirect=False | 2/2 | 5/0/5 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:1>) | `/orders`;`/orders` | route/layout;redirect=False | 8/3 | 9/1/8 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:1>) | `/password-reset`;`/password-reset` | route/layout;redirect=False | 6/2 | 2/0/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/payment-methods.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/payment-methods.tsx:1>) | `/payment-methods`;`/payment-methods` | route/layout;redirect=False | 3/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:1>) | `/product/[id]`;`/product/[id]` | route/layout;redirect=False | 12/3 | 1/2/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/referral-dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral-dashboard.tsx:1>) | `/referral-dashboard`;`/referral-dashboard` | route/layout;redirect=False | 4/4 | 4/2/7 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/referral.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral.tsx:1>) | `/referral`;`/referral` | route/layout;redirect=False | 2/3 | 2/0/3 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:1>) | `/request`;`/request` | route/layout;redirect=False | 9/1 | 2/0/4 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:1>) | `/restaurant/[id]`;`/restaurant/[id]` | route/layout;redirect=False | 5/0 | 4/0/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/account.tsx:1>) | `/restaurant/account`;`/restaurant/account` | route/layout;redirect=True | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/addresses.tsx:1>) | `/restaurant/addresses`;`/restaurant/addresses` | route/layout;redirect=True | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:1>) | `/restaurant/cart`;`/restaurant/cart` | route/layout;redirect=False | 5/0 | 1/1/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/categories.tsx:1>) | `/restaurant/categories`;`/restaurant/categories` | route/layout;redirect=False | 2/0 | 0/0/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:1>) | `/restaurant/checkout`;`/restaurant/checkout` | route/layout;redirect=False | 12/7 | 5/2/5 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:1>) | `/restaurant/dashboard`;`/restaurant/dashboard` | route/layout;redirect=False | 26/13 | 4/4/10 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:1>) | `/restaurant/index`;`/restaurant` | route/layout;redirect=False | 5/0 | 1/1/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/menu.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/menu.tsx:1>) | `/restaurant/menu`;`/restaurant/menu` | route/layout;redirect=False | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/order-confirmation.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/order-confirmation.tsx:1>) | `/restaurant/order-confirmation`;`/restaurant/order-confirmation` | route/layout;redirect=False | 2/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:1>) | `/restaurant/orders/[id]`;`/restaurant/orders/[id]` | route/layout;redirect=False | 7/6 | 2/1/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/orders/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:1>) | `/restaurant/orders/index`;`/restaurant/orders` | route/layout;redirect=False | 4/1 | 9/1/5 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:1>) | `/restaurant/search`;`/restaurant/search` | route/layout;redirect=False | 5/0 | 0/1/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/restaurant/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/support.tsx:1>) | `/restaurant/support`;`/restaurant/support` | route/layout;redirect=True | 0/0 | 0/0/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/retail-prices.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/retail-prices.tsx:1>) | `/retail-prices`;`/retail-prices` | route/layout;redirect=False | 2/4 | 4/1/3 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:1>) | `/seller/orders`;`/seller/orders` | route/layout;redirect=False | 6/6 | 4/1/0 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:1>) | `/seller/products`;`/seller/products` | route/layout;redirect=False | 70/18 | 16/4/38 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:1>) | `/seller/support`;`/seller/support` | route/layout;redirect=False | 6/4 | 4/1/15 | TEST EVIDENCE FOUND18Nov(web limited);PARTIALLY VERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:1>) | `/seller-earnings`;`/seller-earnings` | route/layout;redirect=False | 16/9 | 5/4/6 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:1>) | `/services`;`/services` | route/layout;redirect=False | 16/14 | 7/3/9 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:1>) | `/shop/[id]`;`/shop/[id]` | route/layout;redirect=False | 12/3 | 6/5/3 | UNVERIFIED rendering;PARTIALLY VERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:1>) | `/shops`;`/shops` | route/layout;redirect=False | 11/3 | 0/5/1 | UNVERIFIED rendering;PARTIALLY VERIFIED |

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

### `/(tabs)/_layout` — [frontend/app/(tabs)/_layout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/_layout.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/(tabs)/account` — [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.push "/admin" (line39); router.push "/admin-delivery-partners" (line40); router.push "/admin-earnings" (line41); router.push "/become-seller" (line45); router.push "/seller/products" (line50); router.push "/seller/orders" (line51); router.push "/seller/support" (line52); router.push "/seller-earnings" (line53); router.push "/seller/support" (line56); router.push "/(tabs)/cart" (line72); router.push "/orders" (line74); router.push "/referral-dashboard" (line81); router.push "/auth" (line84); router.push "/delivery-partner" (line89); router.push "/addresses" (line94); router.push "/chand" (line96); router.push "/shops" (line97); router.push "/services" (line98); router.push "/language" (line108); router.push "/notifications" (line110); router.push "/payment-methods" (line111); router.push "/chand" (line112); router.push "/auth" (line141); [
              { id: "online", icon: "shopping-bag" as const, label: "Online Shop", go: () => router.push({ pathname: "/become-seller", params: { type: "online" } }) },
              { id: "offline", icon: "home" as const, label: "Offline Shop", go: () => router.push({ pathname: "/become-seller", params: { type: "offline" } }) },
              { id: "restaurant", icon: "coffee" as const, label: "Restaurant", go: () => router.push("/restaurant/dashboard") },
              { id: "home-services", icon: "tool" as const, label: "Home Services", go: () => router.push({ pathname: "/services", params: { openRegistration: "1" } }) },
            ].map (mode) => (
              <Pressable
                key={mode.id}
                testID={`account-add-shop-mode-${mode.id}`}
                accessibilityRole="button"
                onPress={() => { setShopModesOpen(false); mode.go(); }}
                style={[styles.row, { width: "100%", borderWidth: 1, borderColor: colors.border, borderRadius: radius.md, marginTop: spacing.xs, paddingHorizontal: spacing.md }]}
              >
                <View style={styles.rowIcon}><Feather name={mode.icon} size={18} color={colors.brandPrimary} /></View>
                <Text style={[styles.rowLabel, { flex: 1 }]}>{mode.label}</Text>
                <Feather name="chevron-right" size={18} color={colors.muted} />
              </Pressable>
            ) (line201); router.push { pathname: "/become-seller", params: { type: "online" } } (line202); router.push { pathname: "/become-seller", params: { type: "offline" } } (line203); router.push "/restaurant/dashboard" (line204); router.push { pathname: "/services", params: { openRegistration: "1" } } (line205).

State marker lines:{"loading": [], "empty": [71], "error": []}. Handler count:11. Actual working/render status remains scoped as in table.

### `/(tabs)/cart` — [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.replace "/(tabs)" (line54); router.push "/checkout" (line211).

State marker lines:{"loading": [], "empty": [39, 45, 46, 49, 50, 55, 57, 274, 282, 291, 292, 298, 305], "error": []}. Handler count:11. Actual working/render status remains scoped as in table.

### `/(tabs)/categories` — [frontend/app/(tabs)/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/categories.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.push "/services" (line24); router.push `/category/${item.id}` (line41).

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:2. Actual working/render status remains scoped as in table.

### `/(tabs)/index` — [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:1>)

Direct APIs:api.get<{ unread: number }>("/notifications/unread-count").then((r) => { if (active) setUnread(Number(r.unread) || 0); }).catch () => {} (line56); api.get<{ unread: number }>("/notifications/unread-count").then (r) => { if (active) setUnread(Number(r.unread) || 0); } (line56); api.get "/notifications/unread-count" (line56); api.post<{ show_prominent: boolean }>("/referrals/home-banner-claim", {}).then((result) => {
      if (active) setReferralClaim({ userId: user.id, show: Boolean(result.show_prominent) });
    }).catch () => { if (active) setReferralClaim({ userId: user.id, show: false }); } (line62); api.post<{ show_prominent: boolean }>("/referrals/home-banner-claim", {}).then (result) => {
      if (active) setReferralClaim({ userId: user.id, show: Boolean(result.show_prominent) });
    } (line62); api.post "/referrals/home-banner-claim" (line62).

Navigation:router.push "/chand?voice=1" (line96); router.push "/language" (line99); router.push user ? "/notifications" : "/orders" (line102); router.push "/(tabs)/account" (line106); router.push "/(tabs)/search" (line118); router.push "/(tabs)/categories" (line128); router.push "/(tabs)/categories" (line143); router.push "/referral-dashboard" (line178); router.push "/shops?type=online" (line187); router.push "/shops?type=offline" (line188); router.push "/restaurant" (line189); router.push "/services" (line190); router.push "/(tabs)/categories" (line196); router.push `/category/${item.id}` (line203); router.push "/chand" (line239); router.push "/(tabs)/categories" (line268); router.push "/services" (line278); router.push "/services" (line288).

State marker lines:{"loading": [], "empty": [], "error": [56, 64]}. Handler count:25. Actual working/render status remains scoped as in table.

### `/(tabs)/search` — [frontend/app/(tabs)/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/search.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [67, 91, 147], "error": []}. Handler count:4. Actual working/render status remains scoped as in table.

### `/+html` — [frontend/app/+html.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/+html.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/+not-found` — [frontend/app/+not-found.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/+not-found.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [17], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/_layout` — [frontend/app/_layout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/_layout.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/addresses` — [frontend/app/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:1>)

Direct APIs:api.get<Address[]>('/addresses').then(setItems).catch ()=>setMessage('Sign in to save addresses securely to your account.') (line8); api.get<Address[]>('/addresses').then setItems (line8); api.get '/addresses' (line8); api.post '/addresses' (line8).

Navigation:router.back (back) (line8).

State marker lines:{"loading": [], "empty": [8], "error": [8]}. Handler count:4. Actual working/render status remains scoped as in table.

### `/admin-delivery-partners` — [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:1>)

Direct APIs:api.get<QueueItem[]>("/delivery-partner/admin/applications").then(setItems)
      .catch((e: any) => setNotice(e?.message || "Could not load applications."))
      .finally () => setBusy(false) (line16); api.get<QueueItem[]>("/delivery-partner/admin/applications").then(setItems)
      .catch (e: any) => setNotice(e?.message || "Could not load applications.") (line16); api.get<QueueItem[]>("/delivery-partner/admin/applications").then setItems (line16); api.get "/delivery-partner/admin/applications" (line16); api.get `/delivery-partner/admin/applications/${id}` (line21); api.patch `/delivery-partner/admin/applications/${selected.id}` (line22).

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [2, 25], "empty": [], "error": [17, 21, 22]}. Handler count:9. Actual working/render status remains scoped as in table.

### `/admin-earnings` — [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:1>)

Direct APIs:api.get `/admin/earnings${suffix}` (line26); api.get `/admin/earnings/transactions${txSuffix}` (line26); api.get `/admin/earnings/ledger${suffix}` (line26); api.get "/admin/earnings/settlements" (line26); api.get "/admin/earnings/bank-account" (line26); api.get "/admin/shops" (line26); api.get "/admin/restaurants" (line26); api.patch `/admin/financial-policy/${policyKind}/${policyId}` (line34); api.put "/admin/earnings/bank-account" (line35); api.patch `/admin/earnings/settlements/${id}` (line36).

Navigation:router.replace "/(tabs)/account" (line37); router.back (back) (line40).

State marker lines:{"loading": [4, 15, 31, 38, 42, 47], "empty": [47, 48, 49], "error": [31, 32, 34, 35, 36, 42, 47]}. Handler count:28. Actual working/render status remains scoped as in table.

### `/admin` — [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:1>)

Direct APIs:api.get "/admin/users" (line76); api.get "/admin/shops" (line77); api.get "/admin/orders" (line78); api.get "/admin/requests/anything" (line79); api.get "/admin/requests/assist" (line80); api.get "/admin/restaurants" (line81); api.get "/admin/restaurant/orders" (line82); api.get "/admin/restaurant/support" (line83); api.get "/catalog/master-products?limit=100" (line84); api.get "/admin/announcements" (line85); api.get "/home-services/fee-policy" (line86); api.get "/admin/dashboard" (line87); api.get<any[]>("/admin/chand/feedback").then((rows) => {
      if (active) setChandFeedback(rows);
    }).catch (e: any) => { if (active) setAdminNotice(e?.message || "Chand feedback could not be loaded."); } (line98); api.get<any[]>("/admin/chand/feedback").then (rows) => {
      if (active) setChandFeedback(rows);
    } (line98); api.get "/admin/chand/feedback" (line98); api.get<any>("/admin/referrals").then((result) => {
      if (!active) return;
      setReferralRows(result.referrals || []); setReferralRewards(result.rewards || []);
    }).catch (e: any) => { if (active) setAdminNotice(e?.message || "Referral review queue could not be loaded."); } (line107); api.get<any>("/admin/referrals").then (result) => {
      if (!active) return;
      setReferralRows(result.referrals || []); setReferralRewards(result.rewards || []);
    } (line107); api.get "/admin/referrals" (line107); api.patch `/admin/shops/${id}/status` (line139); api.patch `/admin/restaurants/${id}/status` (line144); api.patch `/admin/restaurant/support/${id}` (line149); api.post `/admin/restaurant/orders/${id}/refund` (line155); api.patch `/admin/requests/${kind}/${id}/status` (line172); api.post "/admin/master-products" (line183); api.get `/catalog/master-products?q=${encodeURIComponent(masterQuery)}&limit=100` (line189); api.patch `/admin/users/${u.id}/role` (line264); api.patch `/admin/chand/feedback/${r.id}` (line328); api.patch `/admin/chand/feedback/${r.id}` (line329); api.patch `/admin/chand/feedback/${r.id}` (line330); api.patch "/admin/home-services/fee-policy" (line362); api.patch `/admin/announcements/${editingAnnouncement}` (line378); api.post "/admin/announcements" (line379); api.get "/admin/announcements" (line381); api.patch `/admin/announcements/${announcement.id}` (line386); api.get "/admin/announcements" (line386); api.get "/admin/catalog-import-history" (line397); api.get "/admin/catalog-price-audit" (line397); api.get "/admin/catalog-import-history" (line403); api.get "/admin/catalog-price-audit" (line403); api.get "/admin/referrals" (line427); api.patch `/admin/referrals/${r.id}/review` (line433); api.get "/admin/referrals" (line433); api.patch `/admin/referrals/${r.id}/review` (line434); api.get "/admin/referrals" (line434); api.patch `/admin/referral-rewards/${r.id}` (line441); api.get "/admin/referrals" (line441); api.patch `/admin/referral-rewards/${r.id}` (line442); api.get "/admin/referrals" (line442); api.patch `/admin/referral-rewards/${r.id}` (line443); api.get "/admin/referrals" (line443); api.patch `/admin/referral-rewards/${r.id}` (line443); api.get "/admin/referrals" (line443); api.get "/admin/retail-price-import/history" (line454); api.get "/admin/retail-price-import/history" (line460); api.get `/catalog/master-products?q=${encodeURIComponent(masterQuery)}&limit=100` (line483).

Navigation:router.push "/auth" (line124); router.back (back) (line198); router.push "/admin-earnings" (line258).

State marker lines:{"loading": [7, 70, 117, 136], "empty": [485], "error": [100, 110, 117, 165, 191, 264, 328, 329, 330, 362, 383, 386, 396, 397, 402, 403, 427, 433, 434, 441, 442, 443, 453, 454, 459, 460, 483]}. Handler count:62. Actual working/render status remains scoped as in table.

### `/auth` — [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.replace next as any (line64); router.replace "/(tabs)/account" (line65); router.back (back) (line84); router.push "/password-reset" as never (line174).

State marker lines:{"loading": [8, 43, 48, 57, 69, 160, 162, 164, 165], "empty": [], "error": [44, 47, 56, 66, 67]}. Handler count:8. Actual working/render status remains scoped as in table.

### `/become-seller` — [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:1>)

Direct APIs:api.upload file (line148); api.patch `/shops/${existingId}` (line185); api.post "/shops" (line186).

Navigation:router.push { pathname: "/auth", params: { next: "/become-seller" } } (line110); router.back (back) (line223); router.push "/seller/products" (line396); router.push "/seller/orders" (line397).

State marker lines:{"loading": [6, 82, 84, 102, 115, 118, 146, 153, 240, 241, 386], "empty": [47, 80, 95, 98, 188], "error": [85, 101, 138, 145, 150, 151, 159, 162, 166, 172, 194, 195]}. Handler count:40. Actual working/render status remains scoped as in table.

### `/category/[slug]` — [frontend/app/category/[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.back (back) (line25); router.replace `/category/${item.id}` (line48).

State marker lines:{"loading": [], "empty": [68, 69, 71, 130, 131], "error": []}. Handler count:2. Actual working/render status remains scoped as in table.

### `/chand` — [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:1>)

Direct APIs:api.get<any>("/assistant/health", false).then((health) => {
      if (active) setProviderStatus((current) => current === "live" ? current : health?.configured ? "configured_unverified" : "not_configured");
    }).catch () => { if (active) setProviderStatus((current) => current === "live" ? current : "unavailable"); } (line193); api.get<any>("/assistant/health", false).then (health) => {
      if (active) setProviderStatus((current) => current === "live" ? current : health?.configured ? "configured_unverified" : "not_configured");
    } (line193); api.get "/assistant/health" (line193); api.get "/catalog/products" (line280); api.get "/catalog/products" (line319); api.post "/grocery/measured-price" (line327); api.post "/chand/feedback" (line453); api.get "/orders/mine" (line470); api.get "/restaurant/orders/mine" (line471); api.get "/restaurant/support/mine" (line472); api.post "/restaurant/support" (line531); api.post "/assistant/context" (line553).

Navigation:router.push `/product/${product.id}` (line399); router.back (back) (line576); router.push "/(tabs)/categories" (line788); router.push "/restaurant" (line789); router.push "/services" (line790); router.push "/orders" (line791); router.push "/request" (line792).

State marker lines:{"loading": [8, 211, 235, 271, 277, 278, 301, 380, 381, 486, 490, 499, 613, 646, 701, 710, 751, 784, 845, 846], "empty": [290, 710, 783], "error": [195, 299, 300, 351, 352, 373, 374, 391, 392, 417, 418, 437, 438, 443, 462, 537, 562, 616, 647, 713, 754]}. Handler count:51. Actual working/render status remains scoped as in table.

### `/checkout` — [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:1>)

Direct APIs:api.get<{ delivery_available?: boolean; pickup_available?: boolean; name?: string; payment_methods?: string[]; public_upi?: string }>(`/shops/${encodeURIComponent(shopId)}`, false).then((shop) => {
      if (!active) return;
      const options = { delivery: Boolean(shop.delivery_available), pickup: Boolean(shop.pickup_available), name: String(shop.name || "Selected shop"), paymentMethods: Array.isArray(shop.payment_methods) ? shop.payment_methods : ["cod"], publicUpi: typeof shop.public_upi === "string" ? shop.public_upi : undefined };
      setShopOptions(options);
      const available = options.paymentMethods.filter((method) => method === "cod" || method === "upi" && Boolean(options.publicUpi) || method === "cash_shop" && options.pickup || method === "pickup" && options.pickup);
      setPaymentMethod((current) => available.includes(current) || current === "online_razorpay" ? current : (available[0] as "cod" | "upi" | "cash_shop" | "pickup") || "cod");
      setFulfillment((current) => current === "delivery" && !options.delivery && options.pickup ? "pickup" : current === "pickup" && !options.pickup && options.delivery ? "delivery" : current);
    }).catch () => { if (active) setShopOptions({ delivery: false, pickup: false, name: "Selected shop", paymentMethods: [], loadFailed: true }); } (line79); api.get<{ delivery_available?: boolean; pickup_available?: boolean; name?: string; payment_methods?: string[]; public_upi?: string }>(`/shops/${encodeURIComponent(shopId)}`, false).then (shop) => {
      if (!active) return;
      const options = { delivery: Boolean(shop.delivery_available), pickup: Boolean(shop.pickup_available), name: String(shop.name || "Selected shop"), paymentMethods: Array.isArray(shop.payment_methods) ? shop.payment_methods : ["cod"], publicUpi: typeof shop.public_upi === "string" ? shop.public_upi : undefined };
      setShopOptions(options);
      const available = options.paymentMethods.filter((method) => method === "cod" || method === "upi" && Boolean(options.publicUpi) || method === "cash_shop" && options.pickup || method === "pickup" && options.pickup);
      setPaymentMethod((current) => available.includes(current) || current === "online_razorpay" ? current : (available[0] as "cod" | "upi" | "cash_shop" | "pickup") || "cod");
      setFulfillment((current) => current === "delivery" && !options.delivery && options.pickup ? "pickup" : current === "pickup" && !options.pickup && options.delivery ? "delivery" : current);
    } (line79); api.get `/shops/${encodeURIComponent(shopId)}` (line79); api.get<any>("/referrals/me").then((data) => { if (active) setRewardBalance(Math.max(0, Number(data.available_balance || 0))); }).catch () => { if (active) setRewardBalance(0); } (line106); api.get<any>("/referrals/me").then (data) => { if (active) setRewardBalance(Math.max(0, Number(data.available_balance || 0))); } (line106); api.get "/referrals/me" (line106); api.post "/grocery/quotes" (line160); api.post "/orders" (line174).

Navigation:Linking.openURL(placed.payment_uri).catch () => setError("Could not open a UPI app. Copy the shop UPI ID from the shop page and pay manually; the order remains unpaid until the shop verifies receipt.") (line216); Linking.openURL placed.payment_uri (line216); router.replace "/(tabs)" (line224); router.replace "/orders" (line227); router.back (back) (line237).

State marker lines:{"loading": [7, 243, 307], "empty": [112, 309], "error": [63, 86, 106, 123, 126, 152, 154, 166, 171, 192, 196, 199, 201, 216, 219]}. Handler count:18. Actual working/render status remains scoped as in table.

### `/delivery-address` — [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.back (back) (line70); router.back (back) (line81).

State marker lines:{"loading": [35, 44, 97, 100], "empty": [], "error": []}. Handler count:6. Actual working/render status remains scoped as in table.

### `/delivery-partner` — [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:1>)

Direct APIs:api.get "/delivery-partner/application/mine" (line32); api.get "/delivery-partner/provider-status" (line33); api.put "/delivery-partner/application" (line48); api.post "/delivery-partner/otp/request" (line61).

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [3, 16, 39, 73], "empty": [], "error": [38, 55, 62, 69]}. Handler count:5. Actual working/render status remains scoped as in table.

### `/index` — [frontend/app/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/index.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/language` — [frontend/app/language.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/language.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.back (back) (line20); router.back (back) (line28).

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:3. Actual working/render status remains scoped as in table.

### `/notifications` — [frontend/app/notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:1>)

Direct APIs:api.get<{ items: Notice[] }>("/notifications/mine")
      .then((r) => { setItems(r.items || []); setError(""); })
      .catch((e: any) => setError(e?.message || t("n.loadError")))
      .finally () => setLoading(false) (line29); api.get<{ items: Notice[] }>("/notifications/mine")
      .then((r) => { setItems(r.items || []); setError(""); })
      .catch (e: any) => setError(e?.message || t("n.loadError")) (line29); api.get<{ items: Notice[] }>("/notifications/mine")
      .then (r) => { setItems(r.items || []); setError(""); } (line29); api.get "/notifications/mine" (line29); api.post(`/notifications/${n.id}/read`, {}).catch () => {} (line41); api.post `/notifications/${n.id}/read` (line41); api.post("/notifications/read-all", {}).catch () => {} (line46); api.post "/notifications/read-all" (line46).

Navigation:router.push (n.data.order_kind === "restaurant" ? "/restaurant/dashboard" : "/seller/orders") as never (line42); router.push `/product/${n.data.product_id}` (line43); router.push { pathname: "/order-tracking", params: { id: n.data.order_id, kind: n.data.order_kind || "grocery" } } as never (line44); router.back (back) (line50).

State marker lines:{"loading": [4, 24, 32, 36, 57, 59], "empty": [59], "error": [25, 30, 31, 41, 46, 58]}. Handler count:3. Actual working/render status remains scoped as in table.

### `/order-tracking` — [frontend/app/order-tracking.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/order-tracking.tsx:1>)

Direct APIs:api.get `/orders/${encodeURIComponent(id)}/tracking?kind=${orderKind}` (line27); api.get `/orders/${encodeURIComponent(id)}` (line28).

Navigation:router.back (back) (line41).

State marker lines:{"loading": [4, 22, 34, 45, 46], "empty": [], "error": [23, 30, 31, 33, 46]}. Handler count:2. Actual working/render status remains scoped as in table.

### `/orders` — [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:1>)

Direct APIs:api.get "/orders/mine" (line35); api.get "/restaurant/orders/mine" (line36); api.post `/orders/${encodeURIComponent(order.id)}/cancel` (line154).

Navigation:router.push "/(tabs)/cart" (line147); router.push { pathname: "/auth", params: { next: "/orders" } } (line168); router.back (back) (line179); router.push item.kind === "restaurant" ? { pathname: "/restaurant/orders/[id]", params: { id: item.id } } : { pathname: "/order-tracking", params: { id: item.id, kind: "grocery" } } (line193); router.push { pathname: "/chand", params: { openHelp: "1", order_id: item.id, order_kind: item.kind } } as never (line208).

State marker lines:{"loading": [5, 25, 27, 45, 49, 53, 58, 174, 212], "empty": [188], "error": [28, 43, 44, 49, 53, 157, 158, 187]}. Handler count:8. Actual working/render status remains scoped as in table.

### `/password-reset` — [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:1>)

Direct APIs:api.post '/auth/password/forgot' (line6); api.post '/auth/password/reset' (line6).

Navigation:router.replace '/auth' as never (line6).

State marker lines:{"loading": [2, 6], "empty": [], "error": [6]}. Handler count:6. Actual working/render status remains scoped as in table.

### `/payment-methods` — [frontend/app/payment-methods.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/payment-methods.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.back (back) (line14); router.push "/(tabs)/cart" (line29); router.push "/restaurant/cart" (line30).

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:3. Actual working/render status remains scoped as in table.

### `/product/[id]` — [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:1>)

Direct APIs:api.get<any>(`/catalog/price-comparison?master_product_id=${encodeURIComponent(product.masterProductId)}&variant_id=${encodeURIComponent(product.masterVariantId)}${product.sellBy === "weight" || product.sellBy === "volume" ? `&sell_by=${product.sellBy}` : ""}`, false)
      .then((result) => { if (active) { setComparison(result); setComparisonMessage(""); } })
      .catch () => { if (active) { setComparison(null); setComparisonMessage("Price comparison is currently unavailable. This offer's displayed price is from its own shop listing."); } } (line55); api.get<any>(`/catalog/price-comparison?master_product_id=${encodeURIComponent(product.masterProductId)}&variant_id=${encodeURIComponent(product.masterVariantId)}${product.sellBy === "weight" || product.sellBy === "volume" ? `&sell_by=${product.sellBy}` : ""}`, false)
      .then (result) => { if (active) { setComparison(result); setComparisonMessage(""); } } (line55); api.get `/catalog/price-comparison?master_product_id=${encodeURIComponent(product.masterProductId)}&variant_id=${encodeURIComponent(product.masterVariantId)}${product.sellBy === "weight" || product.sellBy === "volume" ? `&sell_by=${product.sellBy}` : ""}` (line55).

Navigation:router.back (back) (line65); router.push "/checkout" (line107); router.back (back) (line124); router.push "/(tabs)/cart" (line132); router.push `/product/${listing.id}` (line235); router.push `/product/${r.id}` (line264).

State marker lines:{"loading": [47], "empty": [64, 232], "error": [57]}. Handler count:12. Actual working/render status remains scoped as in table.

### `/referral-dashboard` — [frontend/app/referral-dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral-dashboard.tsx:1>)

Direct APIs:api.get<Dashboard>("/referrals/me").then(result=>{setData(result);setError("");}).catch((e:any)=>setError(e?.message||"Could not load Referral & Earn.")).finally ()=>setLoading(false) (line13); api.get<Dashboard>("/referrals/me").then(result=>{setData(result);setError("");}).catch (e:any)=>setError(e?.message||"Could not load Referral & Earn.") (line13); api.get<Dashboard>("/referrals/me").then result=>{setData(result);setError("");} (line13); api.get "/referrals/me" (line13).

Navigation:Linking.openURL `https://wa.me/?text=${encodeURIComponent(data.message)}` (line20); Linking.openURL url (line20); Linking.openURL `https://wa.me/?text=${encodeURIComponent(data.message)}` (line20); router.back (back) (line23).

State marker lines:{"loading": [12, 13, 16, 24], "empty": [32, 33], "error": [12, 13, 16, 18, 19, 20, 24]}. Handler count:4. Actual working/render status remains scoped as in table.

### `/referral` — [frontend/app/referral.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral.tsx:1>)

Direct APIs:api.get<{valid:boolean}>(`/referral/validate?code=${encodeURIComponent(normalized)}`, false).then((r) => { if (active) { setValid(r.valid); if (r.valid) void storage.setItem("comein.pendingReferralCode", normalized); else setError("This referral code is invalid or no longer eligible."); } }).catch (e:any) => { if(active){setValid(false);setError(e?.message || "Could not validate this referral link.");} } (line23); api.get<{valid:boolean}>(`/referral/validate?code=${encodeURIComponent(normalized)}`, false).then (r) => { if (active) { setValid(r.valid); if (r.valid) void storage.setItem("comein.pendingReferralCode", normalized); else setError("This referral code is invalid or no longer eligible."); } } (line23); api.get `/referral/validate?code=${encodeURIComponent(normalized)}` (line23).

Navigation:router.push {pathname:"/auth",params:{mode:"signup",ref:typeof code==="string"?code:""}} (line29); router.push {pathname:"/auth",params:{ref:typeof code==="string"?code:""}} (line30).

State marker lines:{"loading": [4, 28], "empty": [], "error": [14, 19, 23]}. Handler count:2. Actual working/render status remains scoped as in table.

### `/request` — [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:1>)

Direct APIs:api.post "/requests/anything" (line61).

Navigation:router.back (back) (line87); router.push "/delivery-address" (line134); router.back (back) (line250).

State marker lines:{"loading": [5, 225], "empty": [], "error": [41, 58, 74, 75]}. Handler count:9. Actual working/render status remains scoped as in table.

### `/restaurant/[id]` — [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.replace '/restaurant' as never (line16); router.push '/restaurant/cart' as never (line28).

State marker lines:{"loading": [4, 11, 12, 15], "empty": [], "error": [12]}. Handler count:5. Actual working/render status remains scoped as in table.

### `/restaurant/account` — [frontend/app/restaurant/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/account.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/restaurant/addresses` — [frontend/app/restaurant/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/addresses.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/restaurant/cart` — [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.push '/restaurant' as never (line7); router.push '/restaurant/checkout' as never (line7).

State marker lines:{"loading": [7], "empty": [7], "error": []}. Handler count:5. Actual working/render status remains scoped as in table.

### `/restaurant/categories` — [frontend/app/restaurant/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/categories.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.push {pathname:'/restaurant/[id]',params:{id:r.id}} as never (line10).

State marker lines:{"loading": [], "empty": [], "error": [10]}. Handler count:2. Actual working/render status remains scoped as in table.

### `/restaurant/checkout` — [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:1>)

Direct APIs:api.get<SavedAddress[]>('/addresses')
      .then((rows) => {
        if (!active) return;
        const safeRows = Array.isArray(rows) ? rows : [];
        setSavedAddresses(safeRows);
        const fallback = safeRows.find((item) => item.is_default) || safeRows[0];
        const selected = fallback;
        setAddressId(selected?.id || '');
        setAddress(selected ? formatAddress(selected) : '');
        if (safeRows.length === 0) setAddressNotice('No saved addresses yet. Add one to reuse the same address in Shopping and Restaurant Mode.');
      })
      .catch((error: any) => {
        if (active) setAddressNotice(error?.message || 'Saved addresses could not be loaded. Retry or open the shared address book. Manual checkout addresses are not accepted.');
      })
      .finally () => { if (active) setAddressesLoading(false); } (line59); api.get<SavedAddress[]>('/addresses')
      .then((rows) => {
        if (!active) return;
        const safeRows = Array.isArray(rows) ? rows : [];
        setSavedAddresses(safeRows);
        const fallback = safeRows.find((item) => item.is_default) || safeRows[0];
        const selected = fallback;
        setAddressId(selected?.id || '');
        setAddress(selected ? formatAddress(selected) : '');
        if (safeRows.length === 0) setAddressNotice('No saved addresses yet. Add one to reuse the same address in Shopping and Restaurant Mode.');
      })
      .catch (error: any) => {
        if (active) setAddressNotice(error?.message || 'Saved addresses could not be loaded. Retry or open the shared address book. Manual checkout addresses are not accepted.');
      } (line59); api.get<SavedAddress[]>('/addresses')
      .then (rows) => {
        if (!active) return;
        const safeRows = Array.isArray(rows) ? rows : [];
        setSavedAddresses(safeRows);
        const fallback = safeRows.find((item) => item.is_default) || safeRows[0];
        const selected = fallback;
        setAddressId(selected?.id || '');
        setAddress(selected ? formatAddress(selected) : '');
        if (safeRows.length === 0) setAddressNotice('No saved addresses yet. Add one to reuse the same address in Shopping and Restaurant Mode.');
      } (line59); api.get '/addresses' (line59); api.get `/restaurants/${encodeURIComponent(restaurantIds[0])}` (line84); api.get `/restaurants/${encodeURIComponent(restaurantId)}` (line127); api.get `/restaurants/${encodeURIComponent(restaurantId)}/serviceability?pincode=${encodeURIComponent(pincode)}` (line141).

Navigation:router.push { pathname: '/auth', params: { next: '/restaurant/checkout' } } as never (line114); router.push '/addresses' as never (line119); router.push '/addresses' as never (line138); router.replace { pathname: '/restaurant/orders/[id]', params: { id: order.id } } as never (line168); router.replace { pathname: '/restaurant/order-confirmation', params: { id: order.id, ref: order.ref, mode: 'live', status: order.status } } as never (line169); router.push { pathname: '/auth', params: { next: '/restaurant/checkout' } } as never (line182); router.push '/addresses' as never (line201); router.push '/delivery-address' as never (line202).

State marker lines:{"loading": [2, 41, 53, 73, 197], "empty": [68, 101], "error": [70, 71, 90, 170, 171]}. Handler count:12. Actual working/render status remains scoped as in table.

### `/restaurant/dashboard` — [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:1>)

Direct APIs:api.get<any>('/restaurant/payments/config').catch ()=>({razorpay_enabled:false}) (line13); api.get '/restaurant/payments/config' (line13); api.get '/restaurants/mine' (line13); api.get `/restaurants/${current.id}/orders` (line13); api.get `/restaurants/${current.id}/menu` (line13); api.post '/restaurants' (line16); api.patch `/restaurants/${selected.id}` (line17); api.upload file (line18); api.post `/restaurants/${selected.id}/menu` (line19); api.patch `/restaurants/${selected.id}/menu/${item.id}` (line20); api.patch `/restaurants/${selected.id}/menu/${item.id}` (line22); api.patch `/restaurant/orders/${order.id}/status` (line23); api.patch `/restaurants/${selected.id}/availability` (line26).

Navigation:router.replace '/restaurant' as never (line32).

State marker lines:{"loading": [3, 12, 13, 25], "empty": [16, 17, 30, 31], "error": [13, 16, 17, 18, 19, 20, 21, 22, 23, 26]}. Handler count:26. Actual working/render status remains scoped as in table.

### `/restaurant/index` — [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.push '/restaurant/search' as never (line11); router.push '/restaurant/search' as never (line11); router.push {pathname:'/restaurant/categories',params:{cuisine:label}} as never (line11); router.push '/restaurant/search' as never (line11); router.push {pathname:'/restaurant/[id]',params:{id:r.id}} as never (line11).

State marker lines:{"loading": [11], "empty": [11], "error": [11]}. Handler count:5. Actual working/render status remains scoped as in table.

### `/restaurant/menu` — [frontend/app/restaurant/menu.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/menu.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/restaurant/order-confirmation` — [frontend/app/restaurant/order-confirmation.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/order-confirmation.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.replace '/restaurant/orders' as never (line4); router.replace '/restaurant' as never (line4).

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:2. Actual working/render status remains scoped as in table.

### `/restaurant/orders/[id]` — [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:1>)

Direct APIs:api.get<Order[]>('/restaurant/orders/mine').then(rows=>setOrder(rows.find(o=>o.id===id)||null)).catch((e:any)=>setMessage(e?.message||'Sign in to view this order.')).finally ()=>setLoading(false) (line9); api.get<Order[]>('/restaurant/orders/mine').then(rows=>setOrder(rows.find(o=>o.id===id)||null)).catch (e:any)=>setMessage(e?.message||'Sign in to view this order.') (line9); api.get<Order[]>('/restaurant/orders/mine').then rows=>setOrder(rows.find(o=>o.id===id)||null) (line9); api.get '/restaurant/orders/mine' (line9); api.post `/restaurant/orders/${id}/cancel` (line9); api.post `/restaurants/${order.restaurant_id}/reviews` (line9).

Navigation:router.push {pathname:'/order-tracking',params:{id:order.id,kind:'restaurant'}} as never (line9); router.push {pathname:'/restaurant/support',params:{order_id:order.id,order_kind:'restaurant'}} as never (line9).

State marker lines:{"loading": [3, 9], "empty": [9], "error": [9]}. Handler count:7. Actual working/render status remains scoped as in table.

### `/restaurant/orders/index` — [frontend/app/restaurant/orders/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:1>)

Direct APIs:api.get '/restaurant/orders/mine' (line44).

Navigation:router.push { pathname: '/auth', params: { next: '/restaurant/orders' } } as never (line69); router.replace '/restaurant' as never (line93); router.push { pathname: '/restaurant/orders/[id]', params: { id: order.id } } as never (line102).

State marker lines:{"loading": [2, 28, 35, 40, 49, 63, 77, 79, 80], "empty": [89], "error": [29, 41, 46, 47, 82]}. Handler count:4. Actual working/render status remains scoped as in table.

### `/restaurant/search` — [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:router.push {pathname:'/restaurant/[id]',params:{id:r.id}} as never (line11).

State marker lines:{"loading": [], "empty": [11], "error": [11]}. Handler count:5. Actual working/render status remains scoped as in table.

### `/restaurant/support` — [frontend/app/restaurant/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/support.tsx:1>)

Direct APIs:NOT FOUND locally;inspect shared components/hooks or static/redirect behavior.

Navigation:NOT FOUND local router call;may be shared shell/Redirect/links.

State marker lines:{"loading": [], "empty": [], "error": []}. Handler count:0. Actual working/render status remains scoped as in table.

### `/retail-prices` — [frontend/app/retail-prices.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/retail-prices.tsx:1>)

Direct APIs:api.get<RetailOffer[]>("/catalog/retail-prices", false)
      .then((rows) => setOffers(Array.isArray(rows) ? rows : []))
      .catch((e: any) => setError(e?.message || "Retail price data is unavailable."))
      .finally () => setLoading(false) (line42); api.get<RetailOffer[]>("/catalog/retail-prices", false)
      .then((rows) => setOffers(Array.isArray(rows) ? rows : []))
      .catch (e: any) => setError(e?.message || "Retail price data is unavailable.") (line42); api.get<RetailOffer[]>("/catalog/retail-prices", false)
      .then (rows) => setOffers(Array.isArray(rows) ? rows : []) (line42); api.get "/catalog/retail-prices" (line42).

Navigation:router.back (back) (line57).

State marker lines:{"loading": [4, 38, 45, 62], "empty": [62], "error": [39, 44, 62]}. Handler count:2. Actual working/render status remains scoped as in table.

### `/seller/orders` — [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:1>)

Direct APIs:api.get<any>("/shops/mine").then async (s) => {
    setShop(s);
    if (s) {
      const list = await api.get<any[]>(`/shops/${s.id}/orders`);
      setOrders(list);
    }
  
    } (line42); api.get "/shops/mine" (line42); api.get `/shops/${s.id}/orders` (line45); api.post `/orders/${orderId}/confirm-upi-payment` (line53); api.patch `/shops/${shop.id}/availability` (line64); api.patch `/orders/${orderId}/status` (line69).

Navigation:router.push "/auth" (line77); router.back (back) (line93).

State marker lines:{"loading": [6, 38, 59, 81], "empty": [123], "error": []}. Handler count:6. Actual working/render status remains scoped as in table.

### `/seller/products` — [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:1>)

Direct APIs:api.get `/shops/${sid}/products` (line116); api.get<{ id: string; status?: string } | null>("/shops/mine").then(async (s) => {
      if (!s) return;
      setShopId(s.id);
      setShopStatus(s.status || "pending");
      await load(s.id);
    }).catch((e: any) => {
      setError(e?.message || "Could not load your shop products. Check your connection and try again.");
    }).finally () => setLoading(false) (line123); api.get<{ id: string; status?: string } | null>("/shops/mine").then(async (s) => {
      if (!s) return;
      setShopId(s.id);
      setShopStatus(s.status || "pending");
      await load(s.id);
    }).catch (e: any) => {
      setError(e?.message || "Could not load your shop products. Check your connection and try again.");
    } (line123); api.get<{ id: string; status?: string } | null>("/shops/mine").then async (s) => {
      if (!s) return;
      setShopId(s.id);
      setShopStatus(s.status || "pending");
      await load(s.id);
    } (line123); api.get "/shops/mine" (line123); api.get `/catalog/master-products?q=${encodeURIComponent(query)}&limit=50` (line138); api.post `/shops/${shopId}/master-products/${selectedMaster.id}/link` (line177); api.getCatalogueImportJob shopId (line222); api.upload file (line269); api.patch `/products/${editing.id}` (line302); api.post `/shops/${shopId}/products` (line303); api.getCatalogueImportJob(shopId, item.job_id).then(setCatalogueImportJob).catch (e: any) => setError(e?.message || "Could not load import job.") (line382); api.getCatalogueImportJob(shopId, item.job_id).then setCatalogueImportJob (line382); api.getCatalogueImportJob shopId (line382); api.getCatalogueImportJob shopId (line387); api.getCatalogueImportJob shopId (line388); api.getCatalogueImportJob shopId (line389); api.getCatalogueImportJob shopId (line422).

Navigation:router.push "/auth" (line326); router.back (back) (line344).

State marker lines:{"loading": [6, 85, 89, 94, 130, 134, 144, 267, 274, 332, 443, 444, 448, 473, 486, 569], "empty": [46, 191, 448, 575], "error": [90, 118, 128, 129, 140, 184, 200, 209, 210, 211, 219, 225, 226, 227, 239, 243, 244, 251, 257, 260, 262, 271, 272, 282, 286, 290, 294, 296, 306, 307, 317, 318, 382, 415, 416, 417, 422, 423]}. Handler count:70. Actual working/render status remains scoped as in table.

### `/seller/support` — [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:1>)

Direct APIs:api.get<SupportTicket[]>("/seller/support").then((rows) => {
      setTickets(Array.isArray(rows) ? rows : []); setError("");
    }).catch (e: any) => {
      const status = (e as any)?.status;
      setError(status === 401 ? "Your session has expired. Please sign in again." : status === 403 ? "Seller access is not authorized for this account." : e?.message || "Support tickets could not be loaded.");
      throw e;
    } (line45); api.get<SupportTicket[]>("/seller/support").then (rows) => {
      setTickets(Array.isArray(rows) ? rows : []); setError("");
    } (line45); api.get "/seller/support" (line45); api.patch `/seller/support/${encodeURIComponent(ticket.id)}` (line72).

Navigation:router.push "/auth" (line98); router.back (back) (line103).

State marker lines:{"loading": [4, 38, 57, 106], "empty": [111], "error": [41, 46, 47, 49, 57, 62, 69, 78, 83, 84, 86, 88, 89, 91, 124]}. Handler count:6. Actual working/render status remains scoped as in table.

### `/seller-earnings` — [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:1>)

Direct APIs:api.get<any>(`/earnings/mine${suffix}`).then async (result) => {setData(result);const current=(result.shops||[]).find((s:any)=>s.id===selected)||(result.shops||[])[0];if(current&&!selected)setSelected(current.id);if(current){const b=current.type==="restaurant"?await api.get<any>(`/restaurants/${current.id}/bank-account`):await api.get<any>(`/shops/${current.id}/bank-account`);setBankSummary(b);}else setBankSummary(null);
    } (line15); api.get `/earnings/mine${suffix}` (line15); api.get `/restaurants/${current.id}/bank-account` (line15); api.get `/shops/${current.id}/bank-account` (line15); api.put path (line21); api.post settlementPath (line22); api.post(`/earnings/orders/${o.order_kind}/${o.order_id}/cash-collected`,{confirmed:true,note:"Shopkeeper confirmed cash was physically received."}).then(()=>refresh()).catch (e:any)=>setNotice(e?.message||"Cash collection could not be confirmed.") (line32); api.post(`/earnings/orders/${o.order_kind}/${o.order_id}/cash-collected`,{confirmed:true,note:"Shopkeeper confirmed cash was physically received."}).then ()=>refresh() (line32); api.post `/earnings/orders/${o.order_kind}/${o.order_id}/cash-collected` (line32).

Navigation:router.replace "/(tabs)/account" (line23); router.back (back) (line25).

State marker lines:{"loading": [4, 12, 18, 24, 27], "empty": [27, 31, 32, 34], "error": [18, 19, 21, 22, 27, 32]}. Handler count:16. Actual working/render status remains scoped as in table.

### `/services` — [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:1>)

Direct APIs:api.get "/home-services/providers/mine" (line19); api.get "/home-services/appointments/provider" (line19); api.get "/home-services/appointments/mine" (line19); api.get<Provider[]>("/home-services/providers",false).then(setRows).catch(e=>setError(e?.message||"Could not load providers")).finally ()=>setLoading(false) (line24); api.get<Provider[]>("/home-services/providers",false).then(setRows).catch e=>setError(e?.message||"Could not load providers") (line24); api.get<Provider[]>("/home-services/providers",false).then setRows (line24); api.get "/home-services/providers" (line24); api.patch `/home-services/providers/${mine.id}` (line27); api.post "/home-services/providers" (line27); api.post "/home-services/appointments" (line28); api.patch `/home-services/appointments/${a.id}/status` (line29); api.upload file (line30); api.patch `/home-services/providers/${mine.id}/photo` (line30); api.patch `/home-services/appointments/${a.id}/status` (line33).

Navigation:router.back (back) (line31); Linking.openURL(`tel:${p.phone}`).catch ()=>Alert.alert("Calling unavailable","Use a device that supports phone links.") (line37); Linking.openURL `tel:${p.phone}` (line37).

State marker lines:{"loading": [5, 16, 24, 27, 36, 37, 38], "empty": [33, 34, 37], "error": [16, 19, 24, 27, 28, 29, 30, 33, 37]}. Handler count:16. Actual working/render status remains scoped as in table.

### `/shop/[id]` — [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:1>)

Direct APIs:api.get `/shops/${id}` (line39); api.get "/catalog/products" (line41); api.post "/requests/assist" (line128).

Navigation:router.back (back) (line74); Linking.openURL url (line102); router.back (back) (line159).

State marker lines:{"loading": [6, 29, 54, 62, 65, 298], "empty": [242, 243, 245, 475, 480], "error": [51, 104, 140]}. Handler count:12. Actual working/render status remains scoped as in table.

### `/shops` — [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:1>)

Direct APIs:api.get<any[]>("/shops").then((rows) => {
      const normalized: Shop[] = rows.map((s) => ({
        id: s.id,
        name: s.name,
        tagline: s.tagline || "",
        type: (s.shop_type as ShopType) || "offline",
        offlineShopType: (s.offline_shop_type as OfflineShopType) || "grocery_kirana",
        categoryIds: s.category_ids || [],
        area: s.area || "",
        address: s.address || "",
        phone: s.phone || "",
        image: resolveImage(s.image_url) || "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=600&q=80",
        openNow: Boolean(s.online),
        hours: s.hours || "",
        deliveryAvailable: Boolean(s.delivery_available),
        pickupAvailable: Boolean(s.pickup_available),
        productIds: [],
      }));
      setLiveShops(normalized);
    }).catch () => setLiveShops([]) (line46); api.get<any[]>("/shops").then (rows) => {
      const normalized: Shop[] = rows.map((s) => ({
        id: s.id,
        name: s.name,
        tagline: s.tagline || "",
        type: (s.shop_type as ShopType) || "offline",
        offlineShopType: (s.offline_shop_type as OfflineShopType) || "grocery_kirana",
        categoryIds: s.category_ids || [],
        area: s.area || "",
        address: s.address || "",
        phone: s.phone || "",
        image: resolveImage(s.image_url) || "https://images.unsplash.com/photo-1604719312566-8912e9227c6a?w=600&q=80",
        openNow: Boolean(s.online),
        hours: s.hours || "",
        deliveryAvailable: Boolean(s.delivery_available),
        pickupAvailable: Boolean(s.pickup_available),
        productIds: [],
      }));
      setLiveShops(normalized);
    } (line46); api.get "/shops" (line46).

Navigation:router.back (back) (line86); router.push "/retail-prices" (line167); router.push `/shop/${item.id}` (line192).

State marker lines:{"loading": [], "empty": [183, 184, 186, 409, 415], "error": [65]}. Handler count:11. Actual working/render status remains scoped as in table.

## Complete event/button binding index

Entries include onPress and input/modal change events;only binding presence is verified. Full original handler expressions are in JSON;the table gives a readable prefix,not an execution verdict.

| File:line | Event | Source handler prefix | Status |
|---|---|---|---|
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:133>) | onPress | logout | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:141>) | onPress | () => router.push("/auth") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:157>) | onPress | r.onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:192>) | onRequestClose | () => setShopModesOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:194>) | onPress | () => setShopModesOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:195>) | onPress | () => {} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:211>) | onPress | () => { setShopModesOpen(false); mode.go(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:219>) | onPress | () => setShopModesOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:230>) | onRequestClose | () => setSignInOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:232>) | onPress | () => setSignInOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/account.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/account.tsx:243>) | onPress | () => setSignInOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:51>) | onPress | () => removeKey(key) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:54>) | onPress | () => router.replace("/(tabs)") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:76>) | onPress | clear | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:104>) | onPress | () => removeKey(key) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:114>) | onError | () => setFailedImages((current) => ({ ...current, [line.key]: true })) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:137>) | onAdd | () => increment(line.product.id, line.variant?.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:138>) | onInc | () => {<br>                        if (isMeasured(line.product)) {<br>                          if (stepUp(line.product, line.qty) === line.qty) { setQuantityNotice((current) => ({ ...current, [li… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:157>) | onDec | () => { setQuantityNotice((current) => { const next = { ...current }; delete next[line.key]; return next; }); decrement(line.product.id, line.variant?.id); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:160>) | onPress | () => remove(line.product.id, line.variant?.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:174>) | onPress | () => replaceLine(line.product.id, line.variant?.id, candidate, variant?.id, line.qty) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/cart.tsx:211>) | onPress | () => router.push("/checkout") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/categories.tsx:24>) | onPress | () => router.push("/services") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/categories.tsx:41>) | onPress | () => router.push(`/category/${item.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:96>) | onPress | () => router.push("/chand?voice=1") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:99>) | onPress | () => router.push("/language") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:102>) | onPress | () => router.push(user ? "/notifications" : "/orders") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:106>) | onPress | () => router.push("/(tabs)/account") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:118>) | onPress | () => router.push("/(tabs)/search") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:128>) | onPress | () => router.push("/(tabs)/categories") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:143>) | onPress | () => router.push("/(tabs)/categories") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:178>) | onPress | () => router.push("/referral-dashboard") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:187>) | onPress | () => router.push("/shops?type=online") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:188>) | onPress | () => router.push("/shops?type=offline") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:189>) | onPress | () => router.push("/restaurant") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:190>) | onPress | () => router.push("/services") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:196>) | onSeeAll | () => router.push("/(tabs)/categories") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:203>) | onPress | () => router.push(`/category/${item.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:226>) | onPress | () => setLocModalOpen(true) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:239>) | onPress | () => router.push("/chand") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:268>) | onSeeAll | () => router.push("/(tabs)/categories") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:278>) | onSeeAll | () => router.push("/services") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:288>) | onPress | () => router.push("/services") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:312>) | onRequestClose | () => setLocModalOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:314>) | onPress | () => setLocModalOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:322>) | onChangeText | setLocInput | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:330>) | onPress | () => {<br>              setLocation(locInput);<br>              setLocModalOpen(false);<br>            } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:359>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/index.tsx:378>) | onPress | onSeeAll | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/search.tsx:51>) | onChangeText | setQuery | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/search.tsx:59>) | onPress | () => setQuery("") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/search.tsx:74>) | onPress | () => setQuery(s) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/(tabs)/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/(tabs)/search.tsx:107>) | onScrollBeginDrag | Keyboard.dismiss | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:8>) | onPress | ()=>router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:8>) | onChangeText | setter | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:8>) | onPress | save | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/addresses.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/addresses.tsx:8>) | onPress | ()=>remove(a.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:25>) | onPress | () => open(item.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:26>) | onChangeText | setReason | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:27>) | onPress | () => decide("approve") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:27>) | onPress | () => decide("reject") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:27>) | onPress | () => decide("correction") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:27>) | onPress | () => decide("suspend") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:27>) | onPress | () => decide("reactivate") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:27>) | onPress | () => setSelected(null) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-delivery-partners.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-delivery-partners.tsx:31>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:37>) | onPress | ()=>router.replace("/(tabs)/account") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:40>) | onPress | ()=>router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:40>) | onPress | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:41>) | onRefresh | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:42>) | onChangeText | setStartDate | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:42>) | onChangeText | setEndDate | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:42>) | onPress | ()=>{setLoading(true);load().catch((e:any)=>setNotice(e?.message\|\|"Failed")).finally(()=>setLoading(false));} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:45>) | onPress | ()=>choosePolicy(entity) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:45>) | onChangeText | setCommissionRate | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:45>) | onChangeText | setServiceFee | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:45>) | onPress | ()=>setDeliveryBeneficiary(v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:45>) | onPress | savePolicy | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:46>) | onChangeText | setHolder | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:46>) | onChangeText | setBankName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:46>) | onChangeText | setAccount | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:46>) | onChangeText | setIfsc | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:46>) | onPress | saveBank | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:47>) | onChangeText | setTransactionOrderId | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:47>) | onChangeText | setTransactionShopId | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:47>) | onChangeText | setTransactionStatus | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:47>) | onChangeText | setTransactionType | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:47>) | onChangeText | setSettlementReference | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:47>) | onPress | ()=>{setLoading(true);load().catch((e:any)=>setNotice(e?.message\|\|"Failed")).finally(()=>setLoading(false));} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:49>) | onPress | ()=>decision(s.id,"approve") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:49>) | onPress | ()=>decision(s.id,"reject") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:49>) | onChangeText | setPayoutRef | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:49>) | onPress | ()=>decision(s.id,"processing") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin-earnings.tsx:49>) | onPress | ()=>Alert.alert("Confirm actual transfer", "Only continue after a real bank transfer has been completed and its reference checked.",[{text:"Cancel",style:"cancel"},{text:"Confirm transfer",o… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:124>) | onPress | () => router.push("/auth") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:198>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:225>) | onPress | () => setTab(t.k as Tab) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:233>) | onRefresh | async () => { setRefreshing(true); await load(); setRefreshing(false); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:249>) | onPress | () => setTab(target as Tab) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:258>) | onPress | () => router.push("/admin-earnings") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:264>) | onPress | async () => { Alert.alert("Change user role", `Set ${u.email} to ${role}? This changes server-authorized access.`, [{text:"Cancel",style:"cancel"},{text:"Confirm",onPress:async()=>{try{await… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:274>) | onPress | () => setShopStatus(s.id, "approved") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:275>) | onPress | () => setShopStatus(s.id, "suspended") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:276>) | onPress | () => setShopStatus(s.id, "pending") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:293>) | onPress | () => setRestaurantStatus(r.id, "approved") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:294>) | onPress | () => setRestaurantStatus(r.id, "suspended") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:295>) | onPress | () => setRestaurantStatus(r.id, "pending") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:306>) | onPress | () => requestRefund(o.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:315>) | onPress | () => setSupportStatus(r.id, "in_progress") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:316>) | onPress | () => setSupportStatus(r.id, "resolved") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:317>) | onPress | () => setSupportStatus(r.id, "closed") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:328>) | onPress | async () => { try { await api.patch(`/admin/chand/feedback/${r.id}`, { status: "reviewing", resolution_note: "" }); setChandFeedback((rows) => rows.map((x) => x.id === r.id ? { ...x, status:… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:329>) | onPress | async () => { try { await api.patch(`/admin/chand/feedback/${r.id}`, { status: "resolved", resolution_note: "Reviewed by admin" }); setChandFeedback((rows) => rows.map((x) => x.id === r.id ?… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:330>) | onPress | async () => { try { await api.patch(`/admin/chand/feedback/${r.id}`, { status: "closed", resolution_note: "Closed by admin" }); setChandFeedback((rows) => rows.map((x) => x.id === r.id ? { .… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:340>) | onPress | () => setReqStatus("anything", r.id, "assigned") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:341>) | onPress | () => setReqStatus("anything", r.id, "completed") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:342>) | onPress | () => setReqStatus("anything", r.id, "cancelled") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:352>) | onPress | () => setReqStatus("assist", r.id, "assigned") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:353>) | onPress | () => setReqStatus("assist", r.id, "completed") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:360>) | onPress | () => setHomeFeeMode(value) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:361>) | onChangeText | setHomeFixedFee | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:362>) | onPress | async () => { const fee=Number(homeFixedFee); if (!Number.isFinite(fee)\|\|fee<0\|\|fee>100000) { setAdminNotice("Enter a valid fee between ₹0 and ₹100,000."); return; } try { await api.patch("/… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:366>) | onChangeText | setAnnouncementTitle | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:367>) | onChangeText | setAnnouncementBody | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:369>) | onPress | () => setAnnouncementAudience(audience) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:371>) | onChangeText | setAnnouncementDays | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:372>) | onPress | async () => {<br>            if (announcementTitle.trim().length < 3 \|\| announcementBody.trim().length < 3) { setAdminNotice("Enter an announcement title and message."); return; }<br>            c… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:385>) | onPress | () => { setEditingAnnouncement(null); setAnnouncementTitle(""); setAnnouncementBody(""); setAnnouncementDays(""); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:386>) | onPress | () => { setEditingAnnouncement(announcement.id); setAnnouncementTitle(announcement.title \|\| ""); setAnnouncementBody(announcement.body \|\| ""); setAnnouncementAudience(announcement.audience \|… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:386>) | onPress | async () => { try { await api.patch(`/admin/announcements/${announcement.id}`, { active: !announcement.active }); setAnnouncements(await api.get<any[]>("/admin/announcements")); } catch (e: … (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:393>) | onPress | () => { setImportShopId(shop.id); setImportPreview(null); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:396>) | onPress | async () => { if (!importShopId) { setAdminNotice("Select a store first."); return; } try { const blob = await api.downloadShopImportTemplate(importShopId); if (typeof document === "undefine… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:397>) | onPress | async () => { setImportBusy(true); try { const [h,a] = await Promise.all([api.get<any[]>("/admin/catalog-import-history"),api.get<any[]>("/admin/catalog-price-audit")]); setImportHistory(h);… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:402>) | onPress | async () => { if(!importShopId \|\| !importFile){setAdminNotice("Select a store and a CSV/XLS/XLSX file first.");return;} setImportBusy(true);setImportPreview(null);try{const result=await api.… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:403>) | onPress | () => { if(!importShopId\|\|!importFile\|\|!importPreview\|\|importPreview.errors?.length\|\|!importPreview.valid_rows){setAdminNotice("Run a successful preview with no errors before confirming impo… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:427>) | onPress | async()=>{try{const result=await api.get<any>("/admin/referrals");setReferralRows(result.referrals\|\|[]);setReferralRewards(result.rewards\|\|[]);setAdminNotice("Referral queue refreshed.");}ca… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:433>) | onPress | ()=>Alert.alert("Verify referral eligibility", "Only continue if you have independently verified customer contact, confirmed payment, and completed refund/return and fraud checks.", [{text:"… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:434>) | onPress | ()=>Alert.alert("Reject referral", "Reject this referral qualification?", [{text:"Cancel",style:"cancel"},{text:"Reject",style:"destructive",onPress:async()=>{try{await api.patch(`/admin/ref… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:441>) | onPress | ()=>Alert.alert("Approve reward", "Approve the single ₹500 reward only after validating all 10 qualified referrals and fraud review.", [{text:"Cancel",style:"cancel"},{text:"Approve reward",… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:442>) | onPress | async()=>{try{await api.patch(`/admin/referral-rewards/${r.id}`,{decision:"available",note:"Reward cleared for use."});const result=await api.get<any>("/admin/referrals");setReferralRewards(… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:443>) | onChangeText | setReferralPayoutReference | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:443>) | onPress | async()=>{try{await api.patch(`/admin/referral-rewards/${r.id}`,{decision:"processing",note:"Manual payout processing started."});const result=await api.get<any>("/admin/referrals");setRefer… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:443>) | onPress | async()=>{if(!referralPayoutReference.trim()){setAdminNotice("Enter a verified bank payout reference first.");return;}try{await api.patch(`/admin/referral-rewards/${r.id}`,{decision:"paid",n… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:453>) | onPress | async () => { try { const blob = await api.downloadRetailPriceImportTemplate(); if (typeof document === "undefined" \|\| typeof URL === "undefined") { setAdminNotice("Template download is supp… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:454>) | onPress | async () => { setImportBusy(true); try { setRetailHistory(await api.get<any[]>("/admin/retail-price-import/history")); setAdminNotice("Retail import history refreshed."); } catch(e:any) { se… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:459>) | onPress | async()=>{ if(!retailFile){setAdminNotice("Choose a retailer CSV/XLS/XLSX file first.");return;} setImportBusy(true);setRetailPreview(null);try{const result=await api.importRetailPrices(reta… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:460>) | onPress | ()=>{if(!retailFile\|\|!retailPreview\|\|retailPreview.errors?.length\|\|!retailPreview.valid_rows){setAdminNotice("Run a successful preview with no errors before confirming.");return;} Alert.aler… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:476>) | onChangeText | setMasterName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:477>) | onChangeText | setMasterBrand | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:478>) | onChangeText | setMasterCategory | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:479>) | onChangeText | setMasterUnit | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:480>) | onChangeText | setMasterSource | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:481>) | onPress | () => { void createMasterProduct(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:482>) | onChangeText | setMasterQuery | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:483>) | onPress | async () => { try { setMasterProducts(await api.get<any[]>(`/catalog/master-products?q=${encodeURIComponent(masterQuery)}&limit=100`)); } catch (e: any) { setAdminNotice(e?.message \|\| "Catal… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/admin.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/admin.tsx:498>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:84>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:110>) | onChangeText | setName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:121>) | onChangeText | setEmail | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:134>) | onChangeText | setPhone | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:146>) | onChangeText | setPassword | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:161>) | onPress | submit | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:174>) | onPress | () => router.push("/password-reset" as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/auth.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/auth.tsx:181>) | onPress | () => setMode(mode === "signin" ? "signup" : "signin") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:110>) | onPress | () => router.push({ pathname: "/auth", params: { next: "/become-seller" } }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:223>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:238>) | onPress | pickLogo | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:259>) | onChange | onFile | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:265>) | onChange | (v) => field("name", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:266>) | onChange | (v) => field("owner_name", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:267>) | onChange | (v) => field("tagline", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:272>) | onChange | (v) => field("description", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:275>) | onChange | (v) => field("business_registration", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:278>) | onChange | (v) => field("phone", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:279>) | onChange | (v) => field("alt_phone", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:280>) | onChange | (v) => field("whatsapp", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:283>) | onChange | (v) => field("area", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:284>) | onChange | (v) => field("address", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:287>) | onChange | (v) => field("city", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:290>) | onChange | (v) => field("state", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:293>) | onChange | (v) => field("pincode", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:298>) | onChange | (v) => field("latitude", v ? Number(v) : undefined) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:301>) | onChange | (v) => field("longitude", v ? Number(v) : undefined) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:317>) | onChange | (v) => field("shop_type", v as Shop["shop_type"]) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:326>) | onPress | () => field("offline_shop_type", value) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:331>) | onChange | (v) => field("hours", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:336>) | onChange | (v) => field("delivery_radius_km", v ? Number(v) : undefined) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:343>) | onChange | (v) => field("delivery_available", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:349>) | onChange | (v) => field("pickup_available", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:355>) | onToggle | togglePayment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:356>) | onToggle | togglePayment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:357>) | onToggle | togglePayment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:358>) | onToggle | togglePayment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:359>) | onToggle | togglePayment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:362>) | onChange | (v) => field("public_upi", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:382>) | onPress | submit | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:396>) | onPress | () => router.push("/seller/products") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:397>) | onPress | () => router.push("/seller/orders") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:412>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:450>) | onChangeText | onChange | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:477>) | onValueChange | onChange | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:501>) | onPress | () => onChange(o.value) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:542>) | onPress | () => onToggle(code) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/become-seller.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/become-seller.tsx:571>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/category/[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:25>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/category/[slug].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/category/[slug].tsx:48>) | onPress | () => router.replace(`/category/${item.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:576>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:591>) | onPress | () => setRole(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:602>) | onPress | () => void chooseProductPhoto("camera") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:603>) | onPress | () => void chooseProductPhoto("gallery") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:608>) | onPress | () => void searchPhotoCatalog() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:609>) | onPress | () => void chooseProductPhoto("gallery") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:610>) | onPress | () => { setPhotoAsset(null); setPhotoMatches([]); setPhotoClues(""); setPhotoNotice(""); setPhotoError(""); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:619>) | onPress | () => confirmPhotoProduct(product) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:633>) | onPress | () => addToPlan(product) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:634>) | onPress | () => addToPlan(product, variant.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:649>) | onPress | () => void send(retryQuery) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:661>) | onPress | () => substitutePartyLine(line) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:662>) | onPress | () => setPlanItems((rows) => rows.map((row) => row.product.id === line.product.id && row.variantId === line.variantId ? { ...row, quantity: Math.max(min, row.quantity - step), verifiedTotal:… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:664>) | onPress | () => setPlanItems((rows) => rows.map((row) => row.product.id === line.product.id && row.variantId === line.variantId ? { ...row, quantity: Math.min(row.quantity + step, max), verifiedTotal:… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:665>) | onPress | () => setPlanItems((rows) => rows.filter((row) => !(row.product.id === line.product.id && row.variantId === line.variantId))) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:670>) | onPress | () => void transferPlanToCart() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:678>) | onPress | () => setFeedbackRating("positive") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:679>) | onPress | () => setFeedbackRating("negative") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:681>) | onChangeText | setFeedbackComment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:682>) | onPress | () => void submitChandFeedback() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:689>) | onPress | openHelp | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:702>) | onPress | () => { setSelectedOrder(o); setSupportCategory(o.refund_status ? "refund" : "order"); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:711>) | onPress | () => setSupportCategory(cat as any) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:712>) | onChangeText | setSupportMessage | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:719>) | onPress | () => setConfirmSupport(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:720>) | onPress | () => void submitSupport() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:724>) | onPress | () => void loadHelpData() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:725>) | onPress | () => { setSupportRequestId((current) => current \|\| `support-${Date.now()}-${Math.random().toString(36).slice(2, 12)}`); setConfirmSupport(true); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:736>) | onPress | () => send(suggestion) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:742>) | onPress | () => setVoiceLanguage(value) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:746>) | onPress | () => void startVoiceRecording() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:747>) | onPress | () => void stopAndTranscribeVoice() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:748>) | onPress | () => void cancelVoiceRecording() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:757>) | onChangeText | setDraft | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:757>) | onSubmitEditing | () => send() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:758>) | onPress | () => { setVoiceTypingHint(true); messageInputRef.current?.focus(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:761>) | onPress | () => send() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:768>) | onPress | () => { setPartyOccasion(occasion); setPartyServing(PARTY_OCCASION_SERVING_ASSUMPTIONS[occasion]); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:771>) | onChangeText | (value) => setPartyGuests(value.replace(/[^0-9]/g, "").slice(0, 3)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:772>) | onChangeText | (value) => setPartyBudget(value.replace(/[^0-9]/g, "").slice(0, 6)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:776>) | onChangeText | (v) => setPartyServing((a) => ({ ...a, snacksGramsPerGuest: Number(v.replace(/[^0-9]/g, "")) })) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:777>) | onChangeText | (v) => setPartyServing((a) => ({ ...a, drinksMlPerGuest: Number(v.replace(/[^0-9]/g, "")) })) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:780>) | onChangeText | (v) => setPartyServing((a) => ({ ...a, bakeryPiecesPerGuest: Number(v.replace(/[^0-9]/g, "")) })) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:781>) | onChangeText | (v) => setPartyServing((a) => ({ ...a, fruitGramsPerGuest: Number(v.replace(/[^0-9]/g, "")) })) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:784>) | onPress | () => void generatePartyPlan() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:787>) | onPress | () => setPartyOpen((open) => !open) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:788>) | onPress | () => router.push("/(tabs)/categories") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:789>) | onPress | () => router.push("/restaurant") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:790>) | onPress | () => router.push("/services") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:791>) | onPress | () => router.push("/orders") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/chand.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/chand.tsx:792>) | onPress | () => router.push("/request") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:216>) | onPress | () => { if (placed.payment_uri) Linking.openURL(placed.payment_uri).catch(() => setError("Could not open a UPI app. Copy the shop UPI ID from the shop page and pay manually; the order remain… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:222>) | onChange | setPlaced | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:224>) | onPress | () => router.replace("/(tabs)") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:227>) | onPress | () => router.replace("/orders") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:237>) | onPress | () => { if (buyNowLine) clearBuyNow(); router.back(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:245>) | onPress | () => setFulfillment("delivery") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:246>) | onPress | () => setFulfillment("pickup") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:252>) | onChange | setAddress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:254>) | onChange | setName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:255>) | onChange | setPhone | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:256>) | onChange | setNotes | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:259>) | onPress | () => setPaymentMethod("cod") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:264>) | onPress | () => setPaymentMethod("upi") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:269>) | onPress | () => setPaymentMethod(shopOptions.paymentMethods.includes("cash_shop") ? "cash_shop" : "pickup") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:273>) | onPress | () => setPaymentMethod("online_razorpay") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:280>) | onPress | () => { setUseRewards((current) => !current); setQuote(null); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:304>) | onPress | place | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/checkout.tsx:330>) | onChangeText | onChange | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:81>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:97>) | onPress | requestCurrentLocation | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:112>) | onChangeText | setInput | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:118>) | onSubmitEditing | handleSave | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:128>) | onPress | () => setInput(q.value) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-address.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-address.tsx:158>) | onPress | handleSave | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:78>) | onChangeText | setter | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:87>) | onPress | startOtp | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:96>) | onPress | () => setConsent(!consent) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:97>) | onPress | saveDraft | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/delivery-partner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/delivery-partner.tsx:98>) | onPress | shareReferral | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/language.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/language.tsx:28>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/language.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/language.tsx:53>) | onPress | () => setSelected(opt.code) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/language.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/language.tsx:86>) | onPress | handleSave | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:50>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:53>) | onPress | readAll | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/notifications.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/notifications.tsx:61>) | onPress | () => void open(n) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/order-tracking.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/order-tracking.tsx:41>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/order-tracking.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/order-tracking.tsx:46>) | onPress | () => { setLoading(true); void load(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:168>) | onPress | () => router.push({ pathname: "/auth", params: { next: "/orders" } }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:179>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:181>) | onPress | () => void loadOrders() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:193>) | onPress | () => router.push(item.kind === "restaurant" ? { pathname: "/restaurant/orders/[id]", params: { id: item.id } } : { pathname: "/order-tracking", params: { id: item.id, kind: "grocery" } }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:206>) | onChange | (updated) => setOrders((current) => current.map((row) => row.id === item.id && row.kind === "grocery" ? { ...row, ...updated, kind: "grocery" } : row)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:208>) | onPress | () => router.push({ pathname: "/chand", params: { openHelp: "1", order_id: item.id, order_kind: item.kind } } as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:212>) | onPress | () => repeatOrder(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/orders.tsx:215>) | onPress | () => void cancelOrder(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:6>) | onChangeText | setEmail | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:6>) | onPress | request | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:6>) | onChangeText | setToken | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:6>) | onChangeText | setPassword | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:6>) | onPress | reset | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/password-reset.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/password-reset.tsx:6>) | onPress | ()=>router.replace('/auth' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/payment-methods.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/payment-methods.tsx:14>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/payment-methods.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/payment-methods.tsx:29>) | onPress | () => router.push("/(tabs)/cart") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/payment-methods.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/payment-methods.tsx:30>) | onPress | () => router.push("/restaurant/cart") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:65>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:124>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:132>) | onPress | () => router.push("/(tabs)/cart") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:144>) | onError | () => setImageFailed(true) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:163>) | onSave | (amount) => setAmount(product, amount) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:180>) | onPress | () => { setSelectedVariantId(variant.id); setCartMessage(""); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:235>) | onPress | () => router.push(`/product/${listing.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:264>) | onPress | () => router.push(`/product/${r.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:296>) | onAdd | measured ? () => { addProduct(product); setCartMessage(""); } : addSelectedToCart | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:297>) | onInc | measured ? () => { increment(product.id, undefined, product); setCartMessage(""); } : incrementSelected | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:298>) | onDec | () => { decrement(product.id, selectedVariant?.id); setCartMessage(""); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/product/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/product/[id].tsx:302>) | onPress | buyNow | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/referral-dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral-dashboard.tsx:23>) | onPress | ()=>router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/referral-dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral-dashboard.tsx:26>) | onPress | ()=>void copy() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/referral-dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral-dashboard.tsx:27>) | onPress | ()=>void share() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/referral-dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral-dashboard.tsx:28>) | onPress | ()=>void whatsapp() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/referral.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral.tsx:29>) | onPress | () => router.push({pathname:"/auth",params:{mode:"signup",ref:typeof code==="string"?code:""}}) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/referral.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/referral.tsx:30>) | onPress | () => router.push({pathname:"/auth",params:{ref:typeof code==="string"?code:""}}) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:87>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:113>) | onChangeText | setPickup | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:126>) | onChangeText | setDrop | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:134>) | onPress | () => router.push("/delivery-address") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:152>) | onChangeText | setDesc | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:168>) | onPress | () => setSize(s) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:204>) | onChangeText | setCustomerPhone | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:218>) | onPress | submit | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/request.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/request.tsx:248>) | onPress | () => {<br>                setSubmitted(false);<br>                router.back();<br>              } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:16>) | onPress | ()=>router.replace('/restaurant' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:24>) | onPress | ()=>setVariantChoice(prev=>({...prev,[item.id]:v.id})) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:25>) | onPress | ()=>setAddonChoice(prev=>({...prev,[item.id]:checked?(prev[item.id]\|\|[]).filter(x=>x!==a.id):[...(prev[item.id]\|\|[]),a.id]})) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:26>) | onPress | ()=>add(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/[id].tsx:28>) | onPress | ()=>router.push('/restaurant/cart' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:7>) | onPress | ()=>router.push('/restaurant' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:7>) | onPress | ()=>update(row.quantity===1?lines.filter(x=>x.itemId!==row.itemId):lines.map(x=>x.itemId===row.itemId?{...x,quantity:x.quantity-1}:x)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:7>) | onPress | ()=>update(lines.map(x=>x.itemId===row.itemId?{...x,quantity:x.quantity+1}:x)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:7>) | onPress | ()=>update(lines.filter(x=>x.itemId!==row.itemId)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/cart.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/cart.tsx:7>) | onPress | ()=>router.push('/restaurant/checkout' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/categories.tsx:10>) | onPress | ()=>setCuisine(c) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/categories.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/categories.tsx:10>) | onPress | ()=>router.push({pathname:'/restaurant/[id]',params:{id:r.id}} as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:182>) | onPress | () => router.push({ pathname: '/auth', params: { next: '/restaurant/checkout' } } as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:185>) | onChangeText | setContactName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:187>) | onChangeText | setContactPhone | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:191>) | onPress | () => setFulfillment('delivery') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:192>) | onPress | () => setFulfillment('pickup') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:198>) | onPress | () => { setAddressId(saved.id); setAddress(formatAddress(saved)); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:201>) | onPress | () => router.push('/addresses' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:202>) | onPress | () => router.push('/delivery-address' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:209>) | onPress | ()=>setPaymentMethod('cod') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:210>) | onPress | ()=>setPaymentMethod('pickup') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:211>) | onPress | ()=>setPaymentMethod('razorpay') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/checkout.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/checkout.tsx:213>) | onPress | placeOrder | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:26>) | onPress | ()=>{setSelected(r);setName(r.name\|\|'');setPhone(r.phone\|\|'');setAddress(r.address\|\|'');setCity(r.city\|\|'');setDescription(r.description\|\|'');setCuisines((r.cuisines\|\|[]).join(', '));setImag… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:26>) | onPress | async()=>{try{const updated=await api.patch<R>(`/restaurants/${selected.id}/availability`,{available:!selected.available});setSelected(updated);setRestaurants(prev=>prev.map(r=>r.id===update… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:27>) | onChangeText | setter | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:27>) | onPress | ()=>togglePaymentMethod(m.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:27>) | onChange | uploadLogo | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:27>) | onPress | ()=>imageInput.current?.click() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:27>) | onPress | updateProfile | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:28>) | onChange | uploadLogo | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:28>) | onPress | ()=>imageInput.current?.click() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:28>) | onChangeText | setter | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:28>) | onPress | ()=>togglePaymentMethod(m.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:28>) | onPress | create | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:29>) | onChangeText | setItemName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:29>) | onChangeText | setItemPrice | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:29>) | onPress | addItem | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:30>) | onChangeText | v=>setPriceDrafts(prev=>({...prev,[item.id]:v})) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:30>) | onPress | ()=>updatePrice(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:30>) | onPress | ()=>toggleItem(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:30>) | onPress | ()=>deleteItem(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:31>) | onPress | ()=>setStatus(o,'accepted') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:31>) | onPress | ()=>setStatus(o,'rejected') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:31>) | onPress | ()=>setStatus(o,'preparing') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:31>) | onPress | ()=>setStatus(o,'ready') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:31>) | onPress | ()=>setStatus(o,o.fulfillment==='pickup'?'picked_up':'out_for_delivery') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:31>) | onPress | ()=>setStatus(o,'delivered') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/dashboard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/dashboard.tsx:32>) | onPress | ()=>router.replace('/restaurant' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:11>) | onPress | ()=>router.push('/restaurant/search' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:11>) | onPress | ()=>router.push('/restaurant/search' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:11>) | onPress | ()=>router.push({pathname:'/restaurant/categories',params:{cuisine:label}} as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:11>) | onPress | ()=>router.push('/restaurant/search' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/index.tsx:11>) | onPress | ()=>router.push({pathname:'/restaurant/[id]',params:{id:r.id}} as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/order-confirmation.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/order-confirmation.tsx:4>) | onPress | ()=>router.replace('/restaurant/orders' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/order-confirmation.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/order-confirmation.tsx:4>) | onPress | ()=>router.replace('/restaurant' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onChange | setOrder | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onPress | ()=>router.push({pathname:'/order-tracking',params:{id:order.id,kind:'restaurant'}} as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onPress | cancel | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onPress | ()=>setRating(n) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onChangeText | setComment | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onPress | review | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/[id].tsx:9>) | onPress | ()=>{if(order) router.push({pathname:'/restaurant/support',params:{order_id:order.id,order_kind:'restaurant'}} as never)} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:69>) | onPress | () => router.push({ pathname: '/auth', params: { next: '/restaurant/orders' } } as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:85>) | onPress | () => { void loadOrders(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:93>) | onPress | () => router.replace('/restaurant' as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/orders/index.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/orders/index.tsx:102>) | onPress | () => router.push({ pathname: '/restaurant/orders/[id]', params: { id: order.id } } as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:11>) | onChangeText | setQ | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:11>) | onPress | ()=>setQ('') | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:11>) | onPress | ()=>setRatingOnly(v=>!v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:11>) | onPress | ()=>setLowFeeOnly(v=>!v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/restaurant/search.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/restaurant/search.tsx:11>) | onPress | ()=>router.push({pathname:'/restaurant/[id]',params:{id:r.id}} as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/retail-prices.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/retail-prices.tsx:57>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/retail-prices.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/retail-prices.tsx:60>) | onChangeText | setQuery | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:77>) | onPress | () => router.push("/auth") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:93>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:106>) | onValueChange | toggleAvailability | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:121>) | onRefresh | async () => { setRefreshing(true); await load(); setRefreshing(false); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:138>) | onPress | () => confirmUpiPayment(item.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/orders.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/orders.tsx:142>) | onPress | () => advance(item.id, a.next) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:326>) | onPress | () => router.push("/auth") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:344>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:351>) | onPress | openMasterCatalog | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:355>) | onPress | openNew | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:360>) | onPress | () => { void downloadImportTemplate(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:363>) | onPress | () => importRef.current?.click() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:366>) | onPress | () => catalogueImportRef.current?.click() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:370>) | onChange | (e: any) => e.target.files?.[0] && previewImport(e.target.files[0]) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:372>) | onChange | (e: any) => e.target.files?.length && uploadUniversalCatalogue(Array.from(e.target.files)) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:382>) | onPress | () => { if (!shopId) return; void api.getCatalogueImportJob(shopId, item.job_id).then(setCatalogueImportJob).catch((e: any) => setError(e?.message \|\| "Could not load import job.")); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:398>) | onChangeText | (v) => updateDraft("name", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:399>) | onChangeText | (v) => updateDraft("brand", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:400>) | onChangeText | (v) => updateDraft("price", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:401>) | onChangeText | (v) => updateDraft("mrp", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:402>) | onChangeText | (v) => updateDraft("stock", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:404>) | onPress | () => updateDraft("category_id", category.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:405>) | onChangeText | (v) => updateDraft("category_id", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:406>) | onChangeText | (v) => updateDraft("unit", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:407>) | onChangeText | (v) => updateDraft("sku", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:408>) | onChangeText | (v) => updateDraft("barcode", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:409>) | onChangeText | (v) => updateDraft("sell_by", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:410>) | onChangeText | (v) => updateDraft("min_qty", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:411>) | onChangeText | (v) => updateDraft("step", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:412>) | onChangeText | (v) => updateDraft("max_qty", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:413>) | onChangeText | (v) => updateDraft("description", v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:415>) | onPress | () => { void saveDraft().catch((e: any) => setError(e?.message \|\| "Could not save record edits.")); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:416>) | onPress | () => { void (async () => { if (Object.keys(record.seller_edited_fields \|\| {}).length) await saveDraft(); await approve(); })().catch((e: any) => setError(e?.message \|\| "Record approval fail… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:417>) | onPress | () => { void reject().catch((e: any) => setError(e?.message \|\| "Record rejection failed.")); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:422>) | onPress | () => { if (!shopId) return; void api.bulkApproveCatalogueImportJob(shopId, catalogueImportJob.job_id).then(() => api.getCatalogueImportJob(shopId, catalogueImportJob.job_id)).then(setCatalo… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:423>) | onPress | () => { if (!shopId) return; void api.confirmCatalogueImportApply(shopId, catalogueImportJob.job_id).then((r) => setError(r.message)).catch((e: any) => setError(e?.message \|\| "Apply confirma… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:426>) | onPress | () => setCatalogueImportJob(null) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:433>) | onPress | () => { void applyImport(); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:434>) | onPress | () => { setImportFile(null); setImportReport(null); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:442>) | onChange | setMasterQuery | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:443>) | onPress | searchMasterCatalog | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:450>) | onPress | () => { setSelectedMaster(item); setSelectedVariantId(item.variants?.[0]?.id \|\| ""); setLinkPrice(""); setLinkMrp(""); setLinkStock("0"); setLinkAvailable(true); setLinkSellBy("pack"); setLi… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:462>) | onPress | () => setSelectedVariantId(variant.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:467>) | onChange | (next) => { setLinkSellBy(next.sell_by); setLinkMeasure(next.measure); if (next.stock !== undefined) setLinkStock(String(next.stock)); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:468>) | onChange | setLinkPrice | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:469>) | onChange | setLinkMrp | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:470>) | onChange | setLinkStock | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:471>) | onValueChange | setLinkAvailable | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:472>) | onPress | linkMasterProduct | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:477>) | onPress | () => { setMasterOpen(false); setMasterError(null); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:484>) | onPress | () => fileRef.current?.click() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:494>) | onChange | (e: any) => e.target.files?.[0] && uploadImage(e.target.files[0]) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:498>) | onChange | setSuggestionQuery | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:502>) | onPress | () => setEditing({ ...editing, name: item.name, category_id: item.category_id, brand: "", unit: "", price: 0, mrp: undefined, stock: 0, image_url: undefined, available: true }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:507>) | onChange | (v) => setEditing({ ...editing, name: v }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:508>) | onChange | (v) => setEditing({ ...editing, brand: v }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:509>) | onChange | (v) => setEditing({ ...editing, unit: v }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:510>) | onChange | (next) => setEditing({ ...editing, ...next, stock: next.stock ?? editing.stock }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:513>) | onChange | (v) => setEditing({ ...editing, price: Number(v) \|\| 0 }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:516>) | onChange | (v) => setEditing({ ...editing, mrp: v ? Number(v) : undefined }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:519>) | onChange | (v) => setEditing({ ...editing, stock: Number(v) \|\| 0 }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:528>) | onPress | () => setEditing({ ...editing, category_id: c.id }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:536>) | onPress | () => setEditing({ ...editing, variants: [...(editing.variants \|\| []), { id: `pack-${Date.now()}`, unit: "", price: 0, stock: 0, available: true }] }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:542>) | onChange | (v) => setEditing({ ...editing, variants: (editing.variants \|\| []).map((x, i) => i === index ? { ...x, unit: v } : x) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:544>) | onChange | (v) => setEditing({ ...editing, variants: (editing.variants \|\| []).map((x, i) => i === index ? { ...x, price: Number(v) \|\| 0 } : x) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:545>) | onChange | (v) => setEditing({ ...editing, variants: (editing.variants \|\| []).map((x, i) => i === index ? { ...x, mrp: v ? Number(v) : undefined } : x) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:546>) | onChange | (v) => setEditing({ ...editing, variants: (editing.variants \|\| []).map((x, i) => i === index ? { ...x, stock: Math.max(0, Number(v) \|\| 0) } : x) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:548>) | onValueChange | (v) => setEditing({ ...editing, variants: (editing.variants \|\| []).map((x, i) => i === index ? { ...x, available: v } : x) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:549>) | onPress | () => setEditing({ ...editing, variants: (editing.variants \|\| []).filter((_, i) => i !== index) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:556>) | onChange | (v) => setEditing({ ...editing, description: v }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:562>) | onValueChange | (v) => setEditing({ ...editing, available: v }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:567>) | onPress | close | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:568>) | onPress | save | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:587>) | onPress | () => openEdit(p) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:588>) | onPress | () => remove(p) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/products.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/products.tsx:614>) | onChangeText | onChange | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:98>) | onPress | () => router.push("/auth") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:103>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:109>) | onRefresh | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:111>) | onPress | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:120>) | onPress | () => void updateStatus(item) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller/support.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller/support.tsx:124>) | onPress | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:23>) | onPress | ()=>router.replace("/(tabs)/account") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:25>) | onPress | ()=>router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:25>) | onPress | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:26>) | onRefresh | refresh | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:27>) | onPress | ()=>{setSelected(s.id);} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:27>) | onChangeText | setStartDate | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:27>) | onChangeText | setEndDate | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:27>) | onPress | ()=>{setLoading(true);load().catch((e:any)=>setNotice(e?.message\|\|"Failed")).finally(()=>setLoading(false));} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:32>) | onPress | ()=>{api.post(`/earnings/orders/${o.order_kind}/${o.order_id}/cash-collected`,{confirmed:true,note:"Shopkeeper confirmed cash was physically received."}).then(()=>refresh()).catch((e:any)=>s… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:33>) | onChangeText | setHolder | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:33>) | onChangeText | setBankName | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:33>) | onChangeText | setAccount | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:33>) | onChangeText | setIfsc | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:33>) | onPress | saveBank | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:34>) | onChangeText | setSettlementKey | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/seller-earnings.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/seller-earnings.tsx:34>) | onPress | requestSettlement | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:26>) | onChangeText | set | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:31>) | onPress | ()=>router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:33>) | onPress | async()=>{try{await api.patch(`/home-services/appointments/${a.id}/status`,{status:"cancelled",note:"Cancelled by customer"});loadDashboard();}catch(e:any){Alert.alert("Cancellation failed",… (full JSON) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:34>) | onChange | uploadProviderPhoto | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:34>) | onPress | ()=>fileInputRef.current?.click() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:34>) | onPress | ()=>updateAppointment(a,"accepted") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:34>) | onPress | ()=>updateAppointment(a,"rejected") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:34>) | onPress | ()=>updateAppointment(a,"rescheduled",reschedule[a.id]) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:35>) | onPress | ()=>setRegister(v=>!v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:36>) | onPress | ()=>setCashAfterService(v=>!v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:36>) | onPress | ()=>setCashVisitFee(v=>!v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:36>) | onPress | registerProvider | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:37>) | onPress | ()=>Linking.openURL(`tel:${p.phone}`).catch(()=>Alert.alert("Calling unavailable","Use a device that supports phone links.")) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:37>) | onPress | ()=>{setSelected(p);setService("");setDate("");setAddress("");} | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:38>) | onPress | book | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/services.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/services.tsx:38>) | onPress | ()=>setSelected(null) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:74>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:159>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:211>) | onPress | callShop | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:215>) | onPress | waShop | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:221>) | onPress | directions | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:225>) | onPress | () => setAssistOpen(true) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:274>) | onRequestClose | () => setAssistOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:275>) | onPress | () => setAssistOpen(false) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:276>) | onStartShouldSetResponder | () => true | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:284>) | onChangeText | setAssistReason | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:293>) | onChangeText | setAssistPhone | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shop/[id].tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shop/[id].tsx:297>) | onPress | submitAssist | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:86>) | onPress | () => router.back() | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:101>) | onChangeText | setQuery | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:107>) | onPress | () => setQuery("") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:118>) | onPress | () => setTab(key) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:143>) | onPress | () => setOfflineShopType(value as OfflineShopType \| "all") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:152>) | onPress | () => setOpenNowOnly((v) => !v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:159>) | onPress | () => setDeliveryOnly((v) => !v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:167>) | onPress | () => router.push("/retail-prices") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:192>) | onPress | () => router.push(`/shop/${item.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:218>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/app/shops.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app/shops.tsx:245>) | onPress | onPress | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/AnnouncementBanner.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/AnnouncementBanner.tsx:40>) | onPress | () => setHidden((h) => [...h, a.id]) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/GroceryOnlinePayment.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/GroceryOnlinePayment.tsx:60>) | onPress | pay | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/GroceryOnlinePayment.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/GroceryOnlinePayment.tsx:61>) | onPress | cancel | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/MeasuredQuantityPicker.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/MeasuredQuantityPicker.tsx:64>) | onPress | () => { setCustom(""); setMessage(""); setAmount(p); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/MeasuredQuantityPicker.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/MeasuredQuantityPicker.tsx:72>) | onChangeText | applyCustom | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/MeasuredQuantityPicker.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/MeasuredQuantityPicker.tsx:78>) | onPress | save | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:46>) | onPress | () => router.push(`/product/${product.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:50>) | onError | () => setImageFailed(true) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:79>) | onPress | () => router.push(`/product/${product.id}`) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:89>) | onAdd | () => addProduct(product) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:90>) | onInc | () => increment(product.id, undefined, product) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:91>) | onDec | () => decrement(product.id) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/ProductCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/ProductCard.tsx:95>) | onPress | buyNow | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/QuantityStepper.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/QuantityStepper.tsx:30>) | onPress | () => {<br>          haptic();<br>          onAdd();<br>        } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/QuantityStepper.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/QuantityStepper.tsx:51>) | onPress | () => {<br>          haptic();<br>          onDec();<br>        } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/QuantityStepper.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/QuantityStepper.tsx:63>) | onPress | () => {<br>          haptic();<br>          onInc();<br>        } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/RestockAlertButton.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/RestockAlertButton.tsx:37>) | onPress | toggle | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:36>) | onPress | () => onChange({ sell_by: o.id, measure: o.id === "pack" ? null : m }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:44>) | onChange | (v: string) => { setStockText(v); const n = Number(v); if (Number.isFinite(n) && n >= 0) onChange({ sell_by: sellBy, measure: m, stock: Math.round(n * 1000) }); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:46>) | onChange | (v: string) => set({ min_qty: num(v) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:47>) | onChange | (v: string) => set({ max_qty: num(v) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:48>) | onChange | (v: string) => set({ step: num(v) }) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:50>) | onChange | (v: string) => { setPresetText(v); set({ presets: v.split(",").map((x) => num(x)).filter((x) => x > 0).slice(0, 8) }); } | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/SellerMeasuredFields.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/SellerMeasuredFields.tsx:63>) | onChangeText | onChange | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/error-boundary.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/error-boundary.tsx:58>) | onPress | handleReload | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/components/error-boundary.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/components/error-boundary.tsx:66>) | onPress | () => setShowDetails((v) => !v) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/restaurant/RestaurantCard.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/restaurant/RestaurantCard.tsx:6>) | onPress | ()=>router.push(`/restaurant/${restaurant.id}` as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/restaurant/RestaurantModeShell.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/restaurant/RestaurantModeShell.tsx:41>) | onPress | () => router.replace("/(tabs)") | SOURCE VERIFIED binding;runtime UNVERIFIED |
| [frontend/src/restaurant/RestaurantNav.tsx](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/src/restaurant/RestaurantNav.tsx:6>) | onPress | ()=>router.push(route as never) | SOURCE VERIFIED binding;runtime UNVERIFIED |
