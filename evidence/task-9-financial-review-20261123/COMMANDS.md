# Verification commands

Use the existing extracted app, a disposable loopback MongoDB replica set database, synthetic fixtures and the existing test-only environment. The API used port 8119. Set `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1` to enable local transaction coverage. Seed the preview accounts with `python backend/tests/seed_preview_test_accounts.py`.

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9*.py backend/tests/test_financial*.py backend/tests/test_task8_restaurant_repeat.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8119 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9fin-web
```

The full run included the retained optional parser libraries on `PYTHONPATH`. Serve the export at the configured local origin `http://localhost:8081` with an SPA fallback. Run `python browser-smoke.py` with Chromium, Playwright, PyMongo, requests, and the seeded synthetic Admin account. The first browser fixture attempted to insert a second order without a distinct idempotency key. The successful rerun uses a unique fixture key and leaves the existing database index intact.
