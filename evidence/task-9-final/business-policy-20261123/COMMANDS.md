# Verification commands

Use a fixture-only environment, loopback replica-set MongoDB and the retained app source. Final backend regression ran on port 8191 with database `comein_disposable_task9_biz_final`. Browser and Expo used port 8190 and `comein_disposable_task9_biz`. Enable `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1` and seed `backend/tests/seed_preview_test_accounts.py`. Include retained optional catalogue parser dependencies on the test path.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_financial*.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_grocery_refund*.py backend/tests/test_referral*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin-earnings.tsx app/seller-earnings.tsx app/seller/advertisements.tsx src/lib/api.ts
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8190 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9biz-web
```

Serve the export on the configured local origin `http://localhost:8081` with SPA fallback. Run `browser.py` with Playwright, Chromium, PyMongo and requests. The previous [restart script](../../task-9-policy-audit-20261123/restart-audit.py) was rerun against the current source. A first command used a nonexistent advertisement test glob and collected nothing. Final commands name the existing advertisement modules explicitly.
