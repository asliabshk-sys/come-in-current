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

The first full-run invocation used repository-default parallel pytest workers. The API suites share state and require preview fixtures and users to exist first. It recorded 672 passed, 11 failed, 23 setup errors and 2 skips. The corrected serial invocation follows the prior checkpoint sequence, with preview runtime tests first. Results are recorded in the regression follow-up.

Native validation, actual Razorpay TEST payments/refunds/webhooks and external notification delivery remain deferred.
