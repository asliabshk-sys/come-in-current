# T9-12 rollout verification

Baseline `1c8cddd41a719501df4d973f2f901d097e69f882` matched local and GitHub `work` before edits. The existing Admin button performed review and enrollment in one write. The operational patch adds a read-only Admin preview, a distinct confirmation action, a required confirmation flag on the existing enrollment POST and confirmation evidence in the existing audit. The preview classifies each selected offer as eligible, excluded, ambiguous or already enrolled. The campaign summary includes previously recorded ambiguous exclusions. Activation and notification logic are reused.

Apply `patches/task9-legacy-enrollment-review.patch` after `patches/task9-replacement-lifecycle.patch`. No schema migration is needed. The patch changes the existing server, Admin panel and two focused replacement suites. Browser coverage extends the existing [Playwright harness](../replacement-lifecycle-20261124/browser.py).

| Verification | Result |
| --- | --- |
| Grocery and Restaurant Admin preview | PASS. Both tests verify role access, classification of eligible, excluded and ambiguous fixtures, no preview writes, 24-hour grace and 15-minute activation policy. |
| Confirmation, audit and worker | PASS. Missing confirmation is rejected. Authorized enrollment retains existing audit and retry behavior. Disposable fixtures verify concurrent duplicate prevention, notification rollback, no partial activation, original offer history and expiry from successful activation. |
| Focused Task 9 | PASS. 25 passed, 0 failed, 0 skipped. Includes separate Grocery and Restaurant replacement scenarios. |
| Offline payment and refund safeguards | PASS. 49 passed, 0 failed, 0 skipped. No provider-backed operation was used. |
| Persisted enrollment audit | PASS. Verified explicit confirmation, Admin/case/order IDs, timestamps, a 24-hour interval and one grace notice in the disposable browser database. |
| Full serial backend regression | PASS. 707 passed, 0 failed, 1 skipped (unavailable object storage at `backend/tests/backend_test.py:397`). Pytest reported 11 framework or dependency warnings in 120.03 seconds. |
| Frontend | PASS. TypeScript, targeted ESLint and Expo web export. |
| Chromium | PASS. Five scenarios cover individual expiry adjustment, read-only eligibility preview, separate enrollment, Grocery withdrawal/removal and Restaurant withdrawal/removal. |
| Native iOS and Android | BLOCKED. See [native verification](NATIVE-VERIFICATION.md). |
| Genuine Razorpay TEST | BLOCKED. See [TEST verification](RAZORPAY-TEST.md). |
| Live Admin enrollment | NOT TESTED. No live records were accessed or enrolled. See the [Admin runbook and recovery procedure](ADMIN-RUNBOOK.md). |

The local suites and web harness used synthetic orders, a disposable loopback MongoDB replica set and a local API. No real charge, refund or settlement was made. Test counts overlap the full regression.

## Commands

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_*.py backend/tests/test_referral_task9_review_integration.py
python -m pytest -q -n 0 --tb=short backend/tests/test_payment_environment_boundary.py backend/tests/test_webhook_envelope_security.py backend/tests/test_payment_webhook_local_integration.py backend/tests/test_grocery_refund_local_integration.py backend/tests/test_restaurant_refund_webhook_transaction_offline.py backend/tests/test_task9_collection_adapter.py
mapfile -t suites < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 -ra --tb=short backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${suites[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx src/components/GroceryOrderReplacements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8293 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9ops-web
```

For the browser harness, serve the exported SPA at loopback 8294 with the API at loopback 8293 and synthetic preview accounts. Set the disposable DB name to `comein_disposable_t9ops_browser`. The regression used the seeded loopback API at 8292 with an independent disposable database. Payment variables remained unset in both environments. Forward and reverse recovery patch checks passed.
