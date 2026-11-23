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
