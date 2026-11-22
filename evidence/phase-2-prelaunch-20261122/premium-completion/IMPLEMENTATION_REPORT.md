# Premium Membership implementation and verification

Implementation baseline: GitHub `work` at `e536f52e08bbe760ba7750b19f6f4e6b293d5976`. The source, regression changes, and tests are saved in `patches/premium-membership-completion.patch`, alongside the existing archive and patches. The Git commit introducing this report contains the tested application delta. The source tree was recovered by applying the patches below in order.

```sh
unzip archives/COME-IN-COMPLETE-MASTER-SOURCE-20261122-current-state-sanitized.zip -d "$COMEIN_SOURCE"
cd "$COMEIN_SOURCE"
patch -p1 < "$COMEIN_REPO/patches/task3-seller-dashboard-overview.patch"
patch -p1 < "$COMEIN_REPO/patches/phase2-advertisement-foundation.patch"
patch -p1 < "$COMEIN_REPO/patches/premium-membership-completion.patch"
```

The previously tracked archive and patches are unchanged. The archive still excludes environment templates. Verification used local public templates, prepared dependencies, synthetic accounts, and a disposable MongoDB 7 replica set.

## Application changes

- **Seller membership and payments.** The existing membership screen opens Razorpay Standard Checkout through the shared web/native adapter and sends the callback to the existing scoped verification route. The screen also exposes refresh, dates, remaining days, eligibility to renew, recent history and measured exposure. The pending state survives interruption. The signed Razorpay webhook can confirm a capture when the browser or app does not return. Activation still requires the admin decision after verification. Price and duration remain ₹299 and 30 days.
- **Lifecycle security.** Shop-scoped transactions serialize purchase/renewal and activation against the existing shop document. Concurrent requests converge on one pending record. Membership status transitions and their audit writes commit together. Gateway intent creation is claimed conditionally before calling Razorpay. An uncertain provider outcome requires reconciliation before another intent. Confirmation checks the owned order, exact IDs, captured status, INR and integer 29900 paise. Both callback and webhook converge on one confirmation. An active membership cannot be activated twice or renewed until it is no longer entitled.
- **Search.** The catalog uses a bounded query, approved shops, real availability and stock, and the existing catalogue import approval checks. Exact normalized shop names return shop results first. Relevant Premium inventory precedes ordinary inventory. Category and offset/limit filters are supported. The Premium tier uses relevance, ₹10 price bands, and distance bands when supplied. Shops within comparable bands rotate using the preceding 14 days of measured impressions and a daily deterministic tie-break. No rating or distance is generated for a shop with missing data.
- **Home, Grocery and shop browsing.** Existing catalog surfaces use a gold border and a Premium label. The featured feed reserves its first positions for at most two distinct Premium shops and keeps ordinary products near the top. The shop directory consumes the same entitlement query. Premium presentation is independent of advertising publication. Home impressions require both horizontal and vertical viewport visibility. Search and category use list viewability.
- **Exposure and analytics.** A fetch can issue an eligible opportunity and a short-lived, signed, customer-bound display token. It cannot record an impression. Authenticated customer events are deduplicated per UTC day, shop, surface and event kind. Engagement requires an impression, and ingestion rechecks shop approval, product ownership/availability and membership eligibility. The opportunity records placement and prior impressions with no raw search text. Revenue is based on distinct verified capture IDs. Admin reporting supports shop/date filters and paged per-shop breakdowns. Seller history and metrics enforce shop ownership. The public catalog contains presentation metadata only.
- **Customer-first offer selection.** Comparable catalog offers are filtered by quantity in stock and configured fulfillment. Verified coordinates and a configured delivery radius can exclude out-of-range offers. Total cost, price, and known distance precede Premium as a tie-break. Customers choose an offer. The selected-shop checkout, quote, inventory reservation and transaction flow remain the authority for placing the order.
- **Compatibility correction.** The prior advertisement destination pattern used a lookahead unsupported by Pydantic's configured regex engine and prevented application import. The equivalent allowlist pattern now validates on startup and still forbids a second leading slash. Advertisement approval and publication checks were preserved.

## API, persistence and source files

- Added `GET /catalog/search`, `POST /catalog/premium-events`, and seller `GET /shops/{shop_id}/membership/history` and `/analytics`.
- Preserved the existing catalog-array response, optionally enriched by surface/category. Added a presentation field to the public shop directory and optional fulfillment, quantity and paired coordinates to existing price comparison. Extended existing membership summaries and admin pagination/report filters. The signed Razorpay webhook has a membership capture branch.
- Added a shop history index, unique sparse gateway order/payment indexes, and one `premium_exposure` collection with ranking and reporting indexes and 367-day TTL. Mongo portability validation covers 81 indexes and 58 collections. Review duplicate historical gateway IDs before applying the unique indexes to an existing environment. No production migration was executed.
- Backend changes are in `backend/server.py`, `backend/premium_exposure.py`, and the test files listed in the patch. Frontend changes are in existing Home, Search, Grocery category, product detail, shop directory, seller membership and admin membership routes, and their shared product, catalog, exposure and cart modules. No new dependencies were added to the project.

## Validation

- [Focused backend output](focused-backend.log) records **61 passed**, including membership and advertisement contracts, Mongo portability, signed local webhooks, and Grocery refunds. The membership integration test uses HTTP against the FastAPI app, a disposable real MongoDB replica set, and in-process Razorpay doubles. It covers authorization, payment mismatches, duplicate deliveries, concurrent transitions, rollback, renewal, expiry, suspension, cancellation, analytics, search, and offer ranking.
- [Full backend output](full-backend-regression.log) records **683 passed, five skipped, zero failed**. Legacy preview suites that share fixture state ran serially with the preview bootstrap first. An earlier run was interrupted after the disposable MongoDB hit its inherited file-descriptor limit. The final run used the project-documented 16384 limit.
- [Frontend and restore output](frontend-and-restore.log) records TypeScript, targeted ESLint, Expo web export, and forward and reverse patch checks.
- [Chromium output](chromium-smoke.log) records **five smoke checks** against the local build and API. Cases include Premium-first search, exact shop lookup, Grocery badge/ordinary visibility, and both membership dashboards.

## Remaining validation and data limitations

- Genuine Razorpay TEST provider order, payment and webhook delivery remain deferred. Use authorized TEST configuration only. Native application binaries and physical devices were outside the local run. No production transaction, deployment, credentials or data were used.
- Signed-in customer display telemetry is an application measurement. Anonymous traffic, pre-rollout history, live ETA, and membership-attributable orders or completed orders are unavailable. Revenue is gross verified capture, with no membership refund integration claimed. A privileged seller/account cannot issue customer tokens. A signed-in customer with a valid issued token can submit a client display event within the daily cap, so telemetry does not prove human attention.
- Backend eligibility changes take effect on the next read and on event submission. Open Home, Grocery/category and shop-directory screens refresh every 30 seconds and on focus. An already loaded Search page refreshes on focus or query change. Search and offer comparison use location only when explicitly available. The existing Grocery location selector supplies text, and address-specific delivery estimates or reliability data are not inferred.
- Payment-intent timeout or unconfirmed creation is held for reconciliation. Local tests do not exercise Razorpay's response-time or delivery behavior. No Premium allocation or sales guarantee is offered.
