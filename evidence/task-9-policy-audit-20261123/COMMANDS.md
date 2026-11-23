# Task 9 policy audit commands

Use the retained source, the Task 9 continuation patches in order and isolated test MongoDB databases. Use fixture-only credentials from the local test environment and enable local integration with `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`. The main API ran on loopback 8160 with `comein_disposable_task9_audit`. Seed preview data using `python backend/tests/seed_preview_test_accounts.py`. Optional catalogue parsers were on the full test path.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_grocery_refund*.py backend/tests/test_financial*.py backend/tests/test_referral*.py backend/tests/test_task8_restaurant_repeat.py backend/tests/test_task21*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/chand.tsx app/order-tracking.tsx app/seller/orders.tsx src/components/GroceryOrderReplacements.tsx src/store/auth.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8160 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9audit-web
```

Serve the export on `http://localhost:8081` with an SPA index fallback. Run `python browser-smoke.py` with Chromium, Playwright, PyMongo and requests. Run `python restart-audit.py` from the retained app source with its backend on the Python path. That script starts and stops two API processes on isolated port 8161 using a separate disposable database.
