# Verification

Use the retained checkout and isolated Mongo replica set database `comein_disposable_task9_framework_final` with loopback API port 8150. Set `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`, use only fixture credentials and run `python backend/tests/seed_preview_test_accounts.py` before runtime regression. Optional catalogue parser dependencies were included on the test path.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_financial*.py backend/tests/test_grocery_refund*.py backend/tests/test_mongo_portability_tool.py backend/tests/test_task19_seller_admin_workflows_contract.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/chand.tsx src/components/GroceryOrderReplacements.tsx src/store/auth.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8150 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9framework-web
```

Serve the export on the existing local `http://localhost:8081` origin with an SPA fallback. Run `python browser-smoke.py` with Chromium, Playwright, PyMongo and requests. The first full run caught two integration contracts. Admin endpoints now explicitly require Admin, and the database inventory verifies the new draft collection. No prior authorization assertion was changed.
