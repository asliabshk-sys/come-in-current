# ESLint warning review — 2026-11-17T01:22:06.760646-08:00

Fresh direct configured ESLint: **0 errors, 42 warnings**, exit 0. No rules disabled, no warning suppressed, and no frontend source changed in this session. Warning review is classification, not a claim that all runtime edge cases passed.

| Rule | Count | Classification |
| --- | ---: | --- |
| unused-eslint-disable-directive | 1 | 1 generated .expo/types/router.d.ts directive. Do not hand-edit generated routing declarations. |
| @typescript-eslint/no-unused-vars | 18 | 18 unused imports/variables: maintainability/dead-code cleanup; no demonstrated runtime failure. |
| import/no-duplicates | 2 | 2 duplicate module-import style warnings; consolidate only in scoped cleanup. |
| @typescript-eslint/array-type | 10 | 10 equivalent Array<T>/T[] style advisories; no runtime behavior change required. |
| react-hooks/exhaustive-deps | 9 | 9 dependency advisories: one unnecessary dependency, eight missing dependency notices. Review below; no automatic dependency-array edits because of request-loop/reset risks. |
| no-unused-vars | 2 | 2 intentionally unused caught-error bindings in command-guard helpers; rename/remove bindings in scoped cleanup if desired. |

## Dependency review

- `app/chand.tsx:191`: Unnecessary lang dependency recomputes memoized suggestions. Low risk; locale remains represented by t. No capability success implied.
- `app/checkout.tsx:88`: Shop IDs/mixed/demo flags are captured by an effect keyed to the cart fingerprint. Do not blindly add the newly allocated shopIds array: it can trigger repeated fetches. Review memoized primitive identity and test live/demo transitions before changing.
- `app/restaurant/[id].tsx:12`: local is a static restaurant lookup derived from route id; id already triggers the effect. Review whether the catalogue can change for a fixed id before changing dependencies.
- `app/restaurant/checkout.tsx:72`: The effect checks user presence but is keyed by user.id; profile/form prefill is separate. Test sign-in/profile transitions before including full user object and changing refetch behavior.
- `app/restaurant/dashboard.tsx:13`: Callback reads selected presence/id while keyed by selected.id. Test refresh and selection stability before adding an object dependency that may cause reload loops.
- `app/restaurant/orders/index.tsx:51`: Callback reads user presence while keyed by user.id and role. Review auth transition behavior; no current failed runtime evidence.
- `app/services.tsx:21`: Effect captures the per-render dashboard loader and keys on user.id. Stabilize loader deliberately before adding it as a dependency; otherwise requests can repeat each render.
- `src/components/MeasuredQuantityPicker.tsx:45`: Translation function captured in delayed request error handling. Potential stale translated error when locale changes during an otherwise valid quote; quantity/product/error dependencies already govern quote request. Needs locale-transition coverage.
- `src/restaurant/useDiscoveryAddress.ts:64`: Focus callback checks user presence and is keyed by id. Review authentication/focus transitions; avoid unnecessary address reload/reset from broad object dependencies.

## Complete warning inventory

| File:line | Rule | Message |
| --- | --- | --- |
| .expo/types/router.d.ts:1 | unused-eslint-disable-directive | Unused eslint-disable directive (no problems were reported). |
| app/(tabs)/index.tsx:24 | @typescript-eslint/no-unused-vars | 'Alert' is defined but never used. |
| app/+not-found.tsx:4 | @typescript-eslint/no-unused-vars | 'StyleSheet' is defined but never used. |
| app/auth.tsx:14 | @typescript-eslint/no-unused-vars | 'StyleSheet' is defined but never used. |
| app/become-seller.tsx:13 | @typescript-eslint/no-unused-vars | 'StyleSheet' is defined but never used. |
| app/chand.tsx:5 | import/no-duplicates | '/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/node_modules/expo-router/build/index.js' imported multiple times. |
| app/chand.tsx:7 | import/no-duplicates | '/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/node_modules/expo-router/build/index.js' imported multiple times. |
| app/chand.tsx:98 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/chand.tsx:103 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/chand.tsx:104 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/chand.tsx:105 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/chand.tsx:106 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/chand.tsx:191 | react-hooks/exhaustive-deps | React Hook useMemo has an unnecessary dependency: 'lang'. Either exclude it or remove the dependency array. |
| app/checkout.tsx:88 | react-hooks/exhaustive-deps | React Hook useEffect has missing dependencies: 'hasDemoItems', 'hasMixedShops', and 'shopIds'. Either include them or remove the dependency array. |
| app/delivery-partner.tsx:3 | @typescript-eslint/no-unused-vars | 'Alert' is defined but never used. |
| app/referral-dashboard.tsx:4 | @typescript-eslint/no-unused-vars | 'Alert' is defined but never used. |
| app/referral.tsx:4 | @typescript-eslint/no-unused-vars | 'StyleSheet' is defined but never used. |
| app/referral.tsx:13 | @typescript-eslint/no-unused-vars | 'user' is assigned a value but never used. |
| app/restaurant/[id].tsx:12 | react-hooks/exhaustive-deps | React Hook useEffect has a missing dependency: 'local'. Either include it or remove the dependency array. |
| app/restaurant/cart.tsx:1 | @typescript-eslint/no-unused-vars | 'useEffect' is defined but never used. |
| app/restaurant/categories.tsx:2 | @typescript-eslint/no-unused-vars | 'View' is defined but never used. |
| app/restaurant/categories.tsx:3 | @typescript-eslint/no-unused-vars | 'RESTAURANTS' is defined but never used. |
| app/restaurant/checkout.tsx:72 | react-hooks/exhaustive-deps | React Hook useEffect has a missing dependency: 'user'. Either include it or remove the dependency array. |
| app/restaurant/dashboard.tsx:13 | react-hooks/exhaustive-deps | React Hook useCallback has a missing dependency: 'selected'. Either include it or remove the dependency array. |
| app/restaurant/orders/index.tsx:19 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/restaurant/orders/index.tsx:51 | react-hooks/exhaustive-deps | React Hook useCallback has a missing dependency: 'user'. Either include it or remove the dependency array. |
| app/seller/products.tsx:63 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| app/seller/products.tsx:304 | @typescript-eslint/no-unused-vars | 'saved' is assigned a value but never used. |
| app/services.tsx:13 | @typescript-eslint/no-unused-vars | 'CATEGORIES' is assigned a value but never used. |
| app/services.tsx:21 | react-hooks/exhaustive-deps | React Hook useEffect has a missing dependency: 'loadDashboard'. Either include it or remove the dependency array. |
| app/shop/[id].tsx:5 | @typescript-eslint/no-unused-vars | 'useMemo' is defined but never used. |
| app/shop/[id].tsx:6 | @typescript-eslint/no-unused-vars | 'Platform' is defined but never used. |
| app/shops.tsx:17 | @typescript-eslint/no-unused-vars | 'filterShops' is defined but never used. |
| scripts/cmd-guard/modes.js:45 | no-unused-vars | 'e' is defined but never used. Allowed unused caught errors must match /^_/u. |
| scripts/cmd-guard/rules.js:36 | no-unused-vars | 'e' is defined but never used. Allowed unused caught errors must match /^_/u. |
| src/components/MeasuredQuantityPicker.tsx:45 | react-hooks/exhaustive-deps | React Hook useEffect has a missing dependency: 't'. Either include it or remove the dependency array. |
| src/components/ProductCard.tsx:3 | @typescript-eslint/no-unused-vars | 'StyleSheet' is defined but never used. |
| src/components/QuantityStepper.tsx:3 | @typescript-eslint/no-unused-vars | 'StyleSheet' is defined but never used. |
| src/components/SellerMeasuredFields.tsx:17 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| src/data/catalog.ts:367 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| src/lib/chand-party-planner.ts:88 | @typescript-eslint/array-type | Array type using 'Array<T>' is forbidden. Use 'T[]' instead. |
| src/restaurant/useDiscoveryAddress.ts:64 | react-hooks/exhaustive-deps | React Hook useCallback has a missing dependency: 'user'. Either include it or remove the dependency array. |
