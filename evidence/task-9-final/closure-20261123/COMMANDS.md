# Closure verification commands

The retained application ran on loopback port 8180 using isolated MongoDB database `comein_disposable_task9_closure`. Configure fixture-only credentials and `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`. Seed synthetic preview accounts with `python backend/tests/seed_preview_test_accounts.py`.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_referral*.py backend/tests/test_grocery_refund*.py backend/tests/test_financial*.py backend/tests/test_task8_restaurant_repeat.py backend/tests/test_task21*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/chand.tsx 'app/(tabs)/cart.tsx' src/store/cart.tsx src/components/GroceryOrderReplacements.tsx app/referral-dashboard.tsx app/notifications.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8180 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9close-web
```

Include retained optional catalogue dependencies on the full test path. Serve the export on the configured `http://localhost:8081` origin with SPA fallback. Run the two Chromium scripts using Playwright, requests and PyMongo, and run the [restart script](../../task-9-policy-audit-20261123/restart-audit.py) from the retained app. The first focused attempt had a synthetic database name beyond MongoDB's namespace limit. The final script shortens the fixture name and retains all assertions.
