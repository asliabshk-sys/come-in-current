# T9-12 verification

Tests used synthetic customers and merchants, the retained loopback MongoDB replica set and isolated fixture databases. API transport used local FastAPI or in-process ASGI. Browser checks ran the Expo export with a loopback API. No real payments, refunds, or payout execution occurred. Native, genuine Razorpay and external storage validation remain separate.

## Commands

```bash
python -m pytest -q -n 0 --tb=short backend/tests/test_task9_*.py backend/tests/test_referral_task9_review_integration.py
python -m uvicorn server:app --host 127.0.0.1 --port 8292
python backend/tests/seed_preview_test_accounts.py
mapfile -t suites < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 -ra --tb=short backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${suites[@]}"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx src/components/GroceryOrderReplacements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8293 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t912-web
```

For Chromium, start the exported app with the existing SPA server on port 8294 and FastAPI on 8293. Use disposable database `comein_disposable_t912_browser`, set the API CORS origin to the loopback web origin, and seed preview accounts. Run [browser.py](browser.py) with Chromium, Playwright, PyMongo and requests. The harness aborts external HTTPS requests.

## Coverage

- Grocery and Restaurant independently exercise offer creation and notification, expiry constraints and audit, expiry lockout, concurrent withdrawal, confirmation after Admin makes a quote stale, recalculation, paid pending review and duplicate submission.
- Both modes exercise the pre-preparation boundary, locked acceptance, readiness hold, resolved-ticket Admin closure, dispatch mutation rejection and order-linked customer support.
- Both modes use a controlled server clock and persistent Mongo fixtures to verify 24-hour grace, 15-minute activation, eligibility exclusions, state changes during grace, rollback after failed notification persistence, delayed retry and idempotent enrollment and worker replay.
- The focused suite also retains the existing financial-review, refund and collection contracts, customer ownership checks, frontend source contracts and referral cases.


## Results

| Check | Pass | Fail | Skip | Blocked |
| --- | ---: | ---: | ---: | ---: |
| Focused Task 9, including Grocery and Restaurant | 25 | 0 | 0 | 0 |
| Full serial backend regression | 707 | 0 | 1 | 0 |
| Playwright Chromium scenarios | 4 | 0 | 0 | 0 |
| TypeScript, targeted ESLint and Expo web export | 3 | 0 | 0 | 0 |
| Forward and reverse recovery patch applicability | 2 | 0 | 0 | 0 |

Focused counts overlap the full backend run. The full run took 112.44 seconds and reported 11 framework or dependency warnings. The focused run reported nine such warnings. The single skip was unavailable external object storage at `backend/tests/backend_test.py:397`.

Chromium verified an Admin expiry adjustment with persisted duration, a legacy enrollment visible in Admin with pending grace, and customer withdrawal and confirmed removal through each mode's real screen and local API. Early browser harness attempts failed due to the backend interpreter lacking Playwright and initial auth setup defects. The final harness used the installed Chromium and Playwright and signed in through the UI. All final scenarios passed.

Physical Android/iOS, genuine Razorpay operations, and live rollout of legacy records were not tested in this phase.
