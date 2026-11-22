# Reproducible executed commands (2026-11-18 resume)

Working app root: /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115
Python: /workspace/come-in-tools/py311/bin/python; Yarn: /workspace/come-in-tools/yarn/node_modules/.bin/yarn.
No new packages installed.

## Backend offline/full regression (cwd backend)
Set PYTHONPATH to app root plus app/backend, then:
python -m pytest tests -q --ignore=tests/test_preview_runtime_e2e.py --ignore=tests/test_batch_5task_runtime.py --ignore=tests/test_iter_notifications_admin_measured.py --ignore=tests/test_task5_live_mongo_transactions.py --ignore=tests/backend_test.py --junitxml=/workspace/come-in-current/evidence/resume-20261118/backend-final-v2.xml
The four runtime suites above ran separately against the explicit disposable local backend; legacy backend_test.py was not run (older auth contract), not counted as passed.

## Live regression
python /workspace/come-in-current/evidence/resume-20261118/live-runner-final.py
Runner reads retained local test credentials outside the repo, asserts disposable DB, seeds only local test accounts, then runs the four existing live modules with -n0. No real provider calls.

## Payment focused (cwd backend, PYTHONPATH as above)
COMEIN_RUN_LOCAL_PAYMENT_TESTS=1 python -m pytest tests/test_payment_environment_boundary.py tests/test_webhook_envelope_security.py tests/test_payment_webhook_local_integration.py tests/test_grocery_refund_local_integration.py tests/test_grocery_refund_eligibility.py tests/test_restaurant_refund_webhook_transaction_offline.py tests/test_step1_final_refund_admin_offline.py tests/test_task18_refund_safety_iteration3.py -q
Final affected run: same local opt-in with test_payment_webhook_local_integration.py test_grocery_refund_local_integration.py test_final_payment_transition_races.py test_upload_allocation_bound.py.

## Frontend (cwd frontend)
yarn typecheck
./node_modules/.bin/eslint . --format json --no-cache
node scripts/test-chand-party-planner.cjs
node scripts/test-native-payment.cjs
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /workspace/come-in-tools/web-release-20261118
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 ./node_modules/.bin/expo export --platform android --platform ios --output-dir /workspace/come-in-tools/native-bundles-20261118
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 ./node_modules/.bin/expo config --type introspect --json
COMEIN_BUILD_ENV=production EXPO_PUBLIC_BACKEND_URL=https://validation.invalid EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 ./node_modules/.bin/expo config --type introspect --json
./node_modules/.bin/expo-modules-autolinking react-native-config --platform android --json
./node_modules/.bin/expo-modules-autolinking react-native-config --platform ios --json

## Browser/config/guard (safe local scripts)
node /workspace/come-in-current/evidence/resume-20261118/browser-home-chand.cjs
node /workspace/come-in-current/evidence/resume-20261118/browser-roles-v2.cjs
node /workspace/come-in-current/evidence/resume-20261118/config-and-guard-check.cjs

## Preservation
python /workspace/come-in-tools/release-save-patch.py
cd APP_ROOT && git apply --reverse --check /workspace/come-in-current/patches/continuation.patch
Do not rerun the backup/restore scripts against their already-existing targets; retained prior drill evidence is sufficient.
