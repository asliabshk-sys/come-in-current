# T9-12 verification

Local tests used synthetic users and a disposable loopback MongoDB replica set. The existing fixture initially failed with a WiredTiger open-file limit. The fresh replica set used a 16,384 open-file limit. No payment-provider or real financial execution was used.

| Check | Command | Result |
| --- | --- | --- |
| Task 9 | `python -m pytest -q -ra --tb=short backend/tests/test_task9_*.py backend/tests/test_referral_task9_review_integration.py` | 25 passed, 0 failed, 0 skipped. 18 test dependency and FastAPI deprecation warnings. |
| TypeScript | `./node_modules/.bin/tsc --noEmit` | Passed |
| Targeted ESLint | `./node_modules/.bin/eslint app/admin.tsx src/components/GroceryOrderReplacements.tsx` | Passed |
| Expo web export | `EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9-expiry-web` | Passed with the local API URL. The first attempt failed because Expo telemetry could not create its home directory. |
| Source recovery patch | `patch -p1 --dry-run` against the captured base and `git apply --check -R` against the updated source | Both passed |

Task 9 fixtures exercise Grocery and Restaurant pricing and payment review, one active option, successful availability timing, failed in-app delivery rollback, late response rejection, concurrent expiry and declines, Assist fallback, admin permission/range checks and deadline audit. Existing integration assertions protect original order and payment records and validate current stock and tax/financial calculations.

The first full-run invocation used repository-default parallel pytest workers. The API suites share state and require preview fixtures and users to exist first. It recorded 672 passed, 11 failed, 23 setup errors and 2 skips. The corrected serial invocation follows the prior checkpoint sequence, with preview runtime tests first. The replacement run used the seeded disposable API on port 8291 and these commands, with the same local-only test environment as the focused run.

```bash
python -m uvicorn server:app --host 127.0.0.1 --port 8291
python backend/tests/seed_preview_test_accounts.py
mapfile -t suites < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 -ra --tb=short backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${suites[@]}"
```

The serial full backend regression passed **707 tests**, with **0 failures** and **1 skip** in 101.68 seconds. The skip was the external object-storage check at `backend/tests/backend_test.py:397`. Pytest reported 11 dependency and framework warnings. Implementation commit `8b6716488b5082803ab74d4adca6af890e703b63` was independently verified on GitHub before this evidence update.

Native validation, actual Razorpay TEST payments/refunds/webhooks and external notification delivery remain deferred.
