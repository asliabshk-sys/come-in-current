# Local verification commands

Run from the retained extracted app using its existing synthetic preview accounts, loopback replica set and disposable databases. Full API ran on port 8240 using `comein_disposable_task9_closure`. Chromium used web port 8086, API 8241, and `comein_disposable_t9_closure_browser`. Restart used port 8242 and `comein_disposable_t9_closure_restart`. Follow the [fixture setup](../local-policy-20261123/COMMANDS.md).

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_referral*.py backend/tests/test_financial*.py backend/tests/test_grocery_refund*.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py backend/tests/test_restaurant_refund_webhook_transaction_offline.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
python /workspace/come-in-current/evidence/task-9-final/closure-evidence-20261123/restart.py
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/admin-earnings.tsx app/seller/advertisements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8241 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/task9-closure-web
```

Chromium reused [the reconciliation browser harness](../reconciliation-controls-20261123/browser.py) with 8085 replaced by 8086, 8231 by 8241, and the browser database name updated. External HTTPS is blocked in that harness.
