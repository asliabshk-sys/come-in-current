# Verification commands

Run from the retained extracted app with synthetic preview accounts and disposable local MongoDB. Full runtime API used loopback port 8220. Chromium used API port 8221 and the exported web app served on localhost port 8084 via SPA fallback. Test environment and API setup follow the previous [commands](../local-policy-20261123/COMMANDS.md).

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
python /workspace/come-in-current/evidence/task-9-policy-audit-20261123/restart-audit.py
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/seller/advertisements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8221 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9-campaign-web
```

Chromium reused [browser.py](../local-policy-20261123/browser.py) with updated fixture ports and database name `comein_disposable_t9_campaign_browser`. Browser tests blocked external HTTPS requests. The restart check used its existing separate disposable database.

Expanded focused selection: `python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_referral*.py backend/tests/test_financial*.py backend/tests/test_grocery_refund*.py backend/tests/test_task4_storage_advertisement_integration.py backend/tests/test_phase2_advertisement_contract.py`.
