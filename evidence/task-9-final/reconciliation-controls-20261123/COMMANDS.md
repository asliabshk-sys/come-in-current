# Verification commands

Run from the retained extracted app using the project fixture environment, local replica set and synthetic preview accounts. Full API used port 8232 and disposable database `comein_disposable_task9_final_regression`. Chromium used port 8231 with Expo web served on localhost port 8085 with SPA fallback and database `comein_disposable_t9_final_browser`. Refer to the earlier [fixture setup](../local-policy-20261123/COMMANDS.md).

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_referral*.py backend/tests/test_financial*.py backend/tests/test_grocery_refund*.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_restaurant_refund_webhook_transaction_offline.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
python /workspace/come-in-current/evidence/task-9-policy-audit-20261123/restart-audit.py
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/admin-earnings.tsx app/seller/advertisements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8231 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9-final-web
```

Run [browser.py](browser.py) with Chromium, Playwright, PyMongo and requests against the fixture web/API processes. It blocks external HTTPS. A synthetic database setup marks the fixture campaign ended before the browser exercises final reconciliation. Publication and resume authorization are exercised by the API integration test separately.
