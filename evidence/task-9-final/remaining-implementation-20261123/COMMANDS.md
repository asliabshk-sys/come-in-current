# Remaining implementation verification

Use the retained application, synthetic credentials, loopback API port 8200 and disposable replica-set database `comein_disposable_task9_remaining`. Enable `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`, seed synthetic preview accounts, and include the retained optional catalogue parser dependencies on the full test path.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_financial*.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_referral*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/checkout.tsx app/admin.tsx app/seller/advertisements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8200 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9remain-web
```

Serve the export on `http://localhost:8081` with an SPA fallback. Run `browser.py` with Playwright, Chromium, requests and PyMongo. The [restart script](../../task-9-policy-audit-20261123/restart-audit.py) tests draft and pending review reload and replay on its own disposable database.
