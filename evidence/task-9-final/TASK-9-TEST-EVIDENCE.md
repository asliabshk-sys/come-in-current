# Task 9 final test evidence

| Test | Result | Output |
| --- | --- | --- |
| Focused replacement, refund, financial, referral, Task 8 and Task 21 | 61 passed, 0 failed, 0 skipped | [Focused](focused.log) |
| Full backend | 695 passed, 0 failed, 1 skipped | [Full](full.log) |
| TypeScript | Passed | [TypeScript](typescript.log) |
| Targeted ESLint | Passed | [ESLint](lint.log) |
| Expo web export | Passed | [Expo](expo.log) |
| Chromium cart | Live pack replacement, repeated click, measured-option guard, unrelated line and persisted reload passed | [Cart output](cart.log), [script](cart-smoke.py) |
| Chromium replacement | Five scenarios passed, including quote for a cheaper paid item and Admin approval pending execution | [Browser output](browser.log), [script](browser-smoke.py) |
| FastAPI process restart | Draft, pending collection review and its audit reloaded. Replay issued no payment and created no duplicate audit entry. | [Restart](restart.log), [script](../task-9-policy-audit-20261123/restart-audit.py) |

Full suite skip was the existing external object-storage check in `backend/tests/backend_test.py:397`. Native Android and iOS and genuine Razorpay TEST payment, webhook and refund execution remain deferred. Mongo-backed cases used synthetic orders and disposable databases. Checkout coupon consumption and partner payout cannot be exercised without the unimplemented or blocked policies listed in the final register. Local review evidence is not payment-provider confirmation.

## Commands

Use the retained source and replica set on loopback. Main API used port 8170 and disposable `comein_disposable_task9_final_scope`. Enable existing local fixture transaction tests with `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1` and seed preview accounts with `python backend/tests/seed_preview_test_accounts.py`. Full regression included the retained optional catalogue parsers on the Python path.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_grocery_refund*.py backend/tests/test_financial*.py backend/tests/test_referral*.py backend/tests/test_task8_restaurant_repeat.py backend/tests/test_task21*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/chand.tsx 'app/(tabs)/cart.tsx' src/store/cart.tsx src/components/GroceryOrderReplacements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8170 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9final-web
```

Serve the export on the configured `http://localhost:8081` origin with SPA index fallback. Run the two browser scripts with Playwright, Chromium, PyMongo and requests. Run the previous audit's restart script against the updated source to reproduce the process reload test.

## Closure increment

| Test | Result | Output |
| --- | --- | --- |
| Focused regression | 63 passed, 0 failed, 0 skipped | [Focused](closure-20261123/focused.log) |
| Full backend | 697 passed, 0 failed, 1 skipped | [Full](closure-20261123/full.log) |
| TypeScript, targeted ESLint, Expo web export | Passed | [TypeScript](closure-20261123/typescript.log), [ESLint](closure-20261123/lint.log), [Expo](closure-20261123/expo.log) |
| Chromium | Seven scenarios passed, including the referral notification and cart persistence | [Browser](closure-20261123/browser.log), [Cart](closure-20261123/cart.log) |
| Policy restart and replay | Draft and pending collection review survived restart. No duplicate audit or payment on replay. | [Restart](closure-20261123/restart.log) |

The sole skip was the existing external object-storage test. Fresh referral tests covered concurrent approvals at the reward threshold, transaction rollback, self-referral and duplicate attribution denial, distinct shared-household accounts, cancelled or refunded eligibility safeguards, and single-credit and notification behavior. No new coupon activation, payout, statutory issuance or genuine provider work was run. [Commands](closure-20261123/COMMANDS.md)

## Payout and campaign policy increment

- **65 focused passed** with no failures or skips. Coverage includes schedule versions and processing boundaries, zero commission, concurrent duplicate payout references, CSV authorization, campaign price acceptance, budget caps and replay, private funding information and coupon draft funding validation. [Focused evidence](business-policy-20261123/focused.log)
- **699 backend passed**, zero failures, **one skip** for unavailable external object storage. [Full output](business-policy-20261123/full.log)
- TypeScript, targeted ESLint, Expo export, two Chromium workflows and process restart/replay passed. [TypeScript](business-policy-20261123/typescript.log) · [ESLint](business-policy-20261123/lint.log) · [Expo](business-policy-20261123/expo.log) · [Chromium](business-policy-20261123/browser.log) · [Restart](business-policy-20261123/restart.log)
- No real payout, genuine provider validation, or coupon checkout redemption was executed. [Commands](business-policy-20261123/COMMANDS.md)

## Grocery coupon and ad delivery increment

- **49 focused passed**, with no failures or skips. Covered real Mongo transaction rollback after stock decrement, two customers competing for the final funded coupon, cancellation and repeated requests, expired coupon, draft activation access, fixed campaign area filtering and measured report ownership. [Focused output](remaining-implementation-20261123/focused.log)
- **700 full backend passed, 0 failed, 1 skipped** for unavailable external object storage. [Full output](remaining-implementation-20261123/full.log)
- TypeScript, targeted ESLint, Expo export, four Chromium scenarios and restart/replay passed. Chromium covered Admin activation and seller report. Cash coupon order submission, retry and cancellation were exercised through the HTTP/Mongo tests. [TypeScript](remaining-implementation-20261123/typescript.log) · [ESLint](remaining-implementation-20261123/lint.log) · [Expo](remaining-implementation-20261123/expo.log) · [Chromium](remaining-implementation-20261123/browser.log) · [Restart](remaining-implementation-20261123/restart.log)
- Native Android/iOS and genuine Razorpay TEST payment, refund and webhook validation remain deferred. [Commands](remaining-implementation-20261123/COMMANDS.md)

## Local campaign lifecycle milestone

Coupon and ad milestone focused result was **3 passed, 0 failed, 0 skipped** using test_task9_coupon_checkout.py and test_task9_business_policy.py. [Focused log](local-policy-20261123/coupon-ad-focused.log).

## Local financial reconciliation and lifecycle increment

- **66 focused passed, 0 failed, 0 skipped, 7 warnings.** Includes paused checkout and replay, ended shortfall and excess, reward availability after qualifying-order refund, two-party invoice approval, concurrent draft replay and immutable invoice linkage. [Focused output](local-policy-20261123/focused.log)
- **700 full backend passed, 0 failed, 1 skipped, 9 warnings.** The existing skip was external object storage unavailable. Warnings are existing FastAPI lifecycle, multipart and parser deprecations. [Full output](local-policy-20261123/full.log)
- TypeScript, targeted ESLint, Expo export, five Chromium scenarios, and process restart/replay passed. Browser validation covered Admin campaign pause, not statutory issuance. [TypeScript](local-policy-20261123/typescript.log) · [ESLint](local-policy-20261123/lint.log) · [Expo](local-policy-20261123/expo.log) · [Chromium](local-policy-20261123/browser.log) · [Restart](local-policy-20261123/restart.log)
- Genuine provider, native-device, object storage, CHAND provider and statutory external checks remain deferred or blocked as documented. [Commands](local-policy-20261123/COMMANDS.md)

### Review consistency campaign

| Check | Result | Evidence |
| --- | --- | --- |
| Task 9 focused | 17 passed, 0 failed, 0 skipped, 7 warnings | [Focused](review-consistency-20261123/focused.log) |
| Expanded financial/advertisement tests | 66 passed, 0 failed, 0 skipped, 7 warnings | [Integrated](review-consistency-20261123/integrated.log) |
| Full backend | 700 passed, 0 failed, 1 skipped, 9 warnings | [Full](review-consistency-20261123/full.log) |
| TypeScript and targeted ESLint | Both passed | [TypeScript](review-consistency-20261123/typescript.log), [ESLint](review-consistency-20261123/eslint.log) |
| Expo web | Exported successfully | [Expo](review-consistency-20261123/expo.log) |
| Chromium | Five passed | [Browser](review-consistency-20261123/browser.log) |
| FastAPI restart and replay | Three passed | [Restart](review-consistency-20261123/restart.log) |

Full backend skipped external object storage at `backend/tests/backend_test.py:397`. Python warnings are FastAPI event-hook and catalogue dependency deprecations. Chromium and restart were executed separately using disposable databases. [Commands](review-consistency-20261123/COMMANDS.md)

### Seven-area reconciliation

Task 9 focused HTTP and MongoDB suite recorded **17 passed, 0 failed, 0 skipped, 7 warnings**. Coverage includes coupon reconciliation after concurrent spending and cancellation, canonical advertisement event identity, closed campaign review concurrency and permissions, linked payment review evidence, reward ledger isolation and invoice readiness. [Focused log](reconciliation-controls-20261123/focused.log) · [Commands](reconciliation-controls-20261123/COMMANDS.md)

| Verification | Result | Evidence |
| --- | --- | --- |
| Expanded financial, referral, advertisement, mock gateway and webhook checks | 75 passed, 0 failed, 0 skipped, 7 warnings | [Expanded log](reconciliation-controls-20261123/integrated.log) |
| Full backend regression | 700 passed, 0 failed, 1 skipped, 9 warnings | [Full log](reconciliation-controls-20261123/full.log) |
| TypeScript, targeted ESLint, Expo web export | All passed | [Types](reconciliation-controls-20261123/typescript.log) · [Lint](reconciliation-controls-20261123/eslint.log) · [Expo](reconciliation-controls-20261123/expo.log) |
| Chromium | Seven scenarios passed | [Browser log](reconciliation-controls-20261123/browser.log) |
| FastAPI restart with disposable MongoDB | Four assertions groups passed, including ad review replay and collection contract persistence | [Restart log](reconciliation-controls-20261123/restart.log) |

The full-suite skip at `backend/tests/backend_test.py:397` was unavailable external object storage. Warnings cover FastAPI lifecycle hooks and catalogue dependencies. The initial focused run had two failures. The advertisement review now returns the canonical persisted timestamp consistently and the reward fixture assertion counts entries at the correct stage. Both were resolved in the final focused and full runs. [Initial focused log](reconciliation-controls-20261123/focused-initial.log)

The release gate continues to defer physical Android/iOS, genuine Razorpay TEST payments, webhooks and refunds, authentic settlement confirmation, and statutory issuance.

### Closure evidence gates

The focused HTTP, MongoDB and local provider adapter run recorded **24 passed, 0 failed, 0 skipped, 7 warnings**. It covers misattributed coupon audit data, concurrent ad and payment reviews, provider-link and refund conflicts, unsigned/invalid events, customer-scoped reward evidence, matched COD confirmation audit, and changed invoice snapshots. [Focused output](closure-evidence-20261123/focused.log) · [Commands](closure-evidence-20261123/COMMANDS.md)

| Check | Result | Evidence |
| --- | --- | --- |
| Expanded local integration and mock suite | 82 passed, 0 failed, 0 skipped, 7 warnings | [Expanded](closure-evidence-20261123/integrated.log) |
| Full backend regression | 707 passed, 0 failed, 1 skipped, 9 warnings | [Full](closure-evidence-20261123/full.log) |
| TypeScript, targeted ESLint and Expo export | Passed | [Types](closure-evidence-20261123/typescript.log) · [Lint](closure-evidence-20261123/eslint.log) · [Expo](closure-evidence-20261123/expo.log) |
| Chromium | Seven scenarios passed | [Browser](closure-evidence-20261123/browser.log) |
| FastAPI restart and replay | Five assertion groups passed, including revalidating the same persisted provider preview with execution disabled | [Restart](closure-evidence-20261123/restart.log) |
| Source checkpoint | Forward dry-run and reverse apply check passed | [Patch](../../patches/task9-closure-evidence-gates.patch) |

The only regression skip was external object storage at `backend/tests/backend_test.py:397`. Warnings were Python framework and catalogue dependency deprecations. All payment records and signatures used for the new adapter tests were fixtures. Real payments, provider transport, native device testing, and statutory issuance remain deferred or blocked.

### Final execution campaign

Fresh focused run: **24 passed, 0 failed, 0 skipped, 7 warnings**. Initial run: **23 passed, 1 failed**. The new fixture reused the original item identifier's variable name and affected a later case. The corrected fixture kept all assertions. [Focused](final-campaign-20261123/focused.log) · [Initial output](final-campaign-20261123/focused-initial.log) · [Commands](final-campaign-20261123/COMMANDS.md)

| Check | Fresh result | Evidence |
| --- | --- | --- |
| Expanded Task 9, financial, referral, ad and refund contracts | 82 passed, 0 failed, 0 skipped, 7 warnings | [Expanded](final-campaign-20261123/integrated.log) |
| TypeScript, targeted ESLint, Expo web export | Passed | [Types](final-campaign-20261123/typescript.log) · [Lint](final-campaign-20261123/eslint.log) · [Expo](final-campaign-20261123/expo.log) |
| Chromium | 7 scenarios passed | [Browser](final-campaign-20261123/browser.log) |
| FastAPI restart and replay | 5 checks passed | [Restart](final-campaign-20261123/restart.log) |

The initial expanded and full runs encountered the same fixture shadowing error as the focused run. Their counts were 81 passed and 1 failed, and 706 passed, 1 failed and 1 skipped, respectively. [Initial expanded](final-campaign-20261123/integrated-initial.log) · [Initial full](final-campaign-20261123/full-initial.log)

The corrected full backend regression recorded **707 passed, 0 failed, 1 skipped, 9 warnings**. The skip at `backend/tests/backend_test.py:397` was unavailable external object storage. Warnings were framework and optional catalogue dependency deprecations. [Final full output](final-campaign-20261123/full.log)

### Approval readiness rerun

| Check | Result | Evidence |
| --- | --- | --- |
| Focused | 24 passed, 0 failed, 0 skipped, 7 warnings | [Log](approval-readiness-20261123/focused.log) |
| Expanded transaction, financial, payment/refund and authorization | 82 passed, 0 failed, 0 skipped, 7 warnings | [Log](approval-readiness-20261123/expanded.log) |
| Full backend | 707 passed, 0 failed, 1 skipped, 9 warnings | [Log](approval-readiness-20261123/full.log) |
| TypeScript, targeted ESLint, Expo export | Passed | [Types](approval-readiness-20261123/typescript.log) · [Lint](approval-readiness-20261123/eslint.log) · [Expo](approval-readiness-20261123/expo.log) |
| Chromium and restart/persistence | 7 scenarios and 5 checks passed | [Chromium](approval-readiness-20261123/browser.log) · [Restart](approval-readiness-20261123/restart.log) |

External object storage was unavailable at `backend/tests/backend_test.py:397`. Python warnings cover framework and catalogue dependency deprecations. All financial evidence was local or synthetic. [Commands](approval-readiness-20261123/COMMANDS.md)

### Coupon funding and channels — 23 November 2026

T9-41–43 remain **PARTIALLY VERIFIED**. Existing COME-IN-funded Grocery cash controls passed fresh tests including release rollback, wrong-order release, paid-order denial and Admin reconciliation after restart. Commercial expansion awaits explicit approval. [Decision record](coupon-funding-20261123/OWNER-DECISION.md) · [Tests and commands](coupon-funding-20261123/TESTS.md)

### Advertisement compensation — 23 November 2026

Advertisement compensation remains **PARTIALLY VERIFIED**. Campaign status and audit writes are atomic, identical status replays are deduplicated, and inactive campaigns cannot record events. Compensation eligibility and execution remain disabled pending explicit approval. [Audit](advertisement-compensation-20261123/AUDIT.md) · [Owner decisions](advertisement-compensation-20261123/OWNER-DECISION.md) · [Tests](advertisement-compensation-20261123/TESTS.md)

### Delivery Partner Allocation — 23 November 2026

Delivery Partner Allocation remains **PARTIALLY VERIFIED**, and T9-30 settlement remains **BLOCKED**. Existing onboarding and Admin fee controls passed; no order assignment or partner payable is enabled. [Audit](delivery-partner-allocation-20261123/AUDIT.md) · [Owner decisions](delivery-partner-allocation-20261123/OWNER-DECISION.md) · [Tests](delivery-partner-allocation-20261123/TESTS.md)

### Rewards and referral reversal — 23 November 2026

Rewards and Referral Reversal remains **PARTIALLY VERIFIED**. Distinct qualifying referral, order and customer links are rechecked, and reward transitions record old/new state. Existing credits were preserved. External identity and reversal policies remain open. [Audit](rewards-referral-reversal-20261123/AUDIT.md) · [Owner decision](rewards-referral-reversal-20261123/OWNER-DECISION.md) · [Tests](rewards-referral-reversal-20261123/TESTS.md)
