# Local verification

Use the existing extracted application with both Task 9 patches applied, a disposable MongoDB replica set, fixture-only credentials and `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`. The loopback API used port 8109 and database `comein_disposable_task9_close`. Seed API fixtures with `python backend/tests/seed_preview_test_accounts.py`. Set the API environment URLs to `http://127.0.0.1:8109`.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9{_grocery_replacement,_restaurant_replacement,_order_actions_contract}.py backend/tests/test_task8_restaurant_repeat.py backend/tests/test_task11_live_order_tracking_contract.py backend/tests/test_task24_repeat_order_contract.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint --max-warnings 0 src/components/GroceryOrderReplacements.tsx app/notifications.tsx app/restaurant/dashboard.tsx 'app/restaurant/orders/[id].tsx'
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8109 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/task9-final-web
```

Full regression included the retained optional catalogue parser dependencies on `PYTHONPATH`. Serve the Expo export on the allowed `http://localhost:8081` origin with an SPA index fallback. Run `python browser-smoke.py` with Chromium, Playwright, PyMongo and requests against the disposable instance.
