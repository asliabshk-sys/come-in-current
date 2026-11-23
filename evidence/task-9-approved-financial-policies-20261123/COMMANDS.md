# Verification commands

Use the existing source with the approved-policy patch applied and an isolated replica-set database. Enable existing local integration fixtures with `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`. Seed runtime fixtures through `python backend/tests/seed_preview_test_accounts.py`. The final full regression used disposable MongoDB database `comein_disposable_task9_policy_final` and loopback port 8130. Browser export and rehearsal used disposable database `comein_disposable_task9_policy`, API port 8129 and the configured web origin `http://localhost:8081` with SPA fallback.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_financial*.py backend/tests/test_task8_restaurant_repeat.py backend/tests/test_grocery_refund*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/chand.tsx src/components/GroceryOrderReplacements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8129 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9policy-web
```

Use the retained optional parser dependencies for full regression and Chromium, Playwright, PyMongo and requests for the browser script. Browser Admin login requires the seeded synthetic Admin account. An initial test run exposed an indentation error and a replay assertion that compared timestamps before and after BSON precision normalization. The final test compares stored replays and separately verifies the recorded decisions. An initial TypeScript pass exposed an optional-state narrowing error in the Admin screen, corrected before the final checks.
