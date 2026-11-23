# Local verification commands

Run from the retained extracted app using its existing synthetic preview accounts, loopback replica set and disposable databases. Full API ran on port 8253 using `comein_disposable_task9_last2`. Chromium used web port 8087, API 8251, and `comein_disposable_t9_last_browser`. Restart used port 8252 and `comein_disposable_t9_last_restart`. Follow the [fixture setup](../local-policy-20261123/COMMANDS.md).

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_referral*.py backend/tests/test_financial*.py backend/tests/test_grocery_refund*.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_restaurant_refund_webhook_transaction_offline.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
python /workspace/come-in-current/evidence/task-9-final/final-campaign-20261123/restart.py
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/admin-earnings.tsx app/seller/advertisements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8251 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9-last-web
```

Run the [Chromium harness](browser.py) with the disposable web and API listeners above. External HTTPS is blocked in that harness.
