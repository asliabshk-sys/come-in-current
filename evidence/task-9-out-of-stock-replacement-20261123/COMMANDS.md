# Local verification commands

Use the existing isolated app source with the Task 8 patch applied, then apply the Task 9 patch. Configure temporary fixture-only credentials, a loopback test API, and a disposable MongoDB replica-set database. This run used `comein_disposable_task9_final`, Mongo on port 27018, FastAPI on port 8099 and the existing allowed web origin `http://localhost:8081`. Set `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1` for the fixture-only integration cases. Seed the preview fixtures using `python backend/tests/seed_preview_test_accounts.py`.

```bash
python -m pytest -q -n 0 --tb=short \
  backend/tests/test_task9_grocery_replacement.py \
  backend/tests/test_task9_order_actions_contract.py \
  backend/tests/test_task19_seller_admin_workflows_contract.py \
  backend/tests/test_task8_restaurant_repeat.py \
  backend/tests/test_task24_repeat_order_contract.py

mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"

cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/order-tracking.tsx app/seller/orders.tsx src/components/GroceryOrderReplacements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8099 CI=1 \
  ./node_modules/.bin/expo export --platform web --output-dir /tmp/task9-web
```

Serve the export on port 8081 with an SPA index fallback. Run `python browser-smoke.py` with Chromium, Playwright, requests and PyMongo installed.

The initial full run found two existing source-contract failures because the status compare-and-update had been factored through a new variable. The final code keeps that update for existing transitions and uses the additional atomic case check for ready. The initial lint run rejected ref use through a render callback. The final UI uses disabled buttons and the transaction provides duplicate protection. The first export needed Expo telemetry disabled for this sandbox. The first browser run used a disallowed test origin and was rerun at the configured local origin. No provider was contacted.

Rerun the optional parser module with its retained test dependencies on `PYTHONPATH` using `python -m pytest -q -n 0 --tb=short -rs backend/tests/test_universal_catalogue_import_engine.py`.
