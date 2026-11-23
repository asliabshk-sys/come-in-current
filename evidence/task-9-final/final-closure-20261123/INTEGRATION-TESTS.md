# Stage 11 — seven-area integration verification

Fresh runs from the retained app using the [disposable fixture setup](../approval-readiness-20261123/COMMANDS.md). Full API used loopback 8280 with `comein_disposable_task9_final_closure`. Expo browser used API 8283, web 8089, and `comein_disposable_t9_closing_browser`. The first two preview runtime suites were run before other files to preserve their fixture sequence.

```bash
docker exec --user mongodb comein-premium-regression prlimit --pid 1 --nofile=16384:16384
python -m uvicorn server:app --host 127.0.0.1 --port 8280 --no-access-log
python backend/tests/seed_preview_test_accounts.py
mapfile -t tests < <(rg --files backend/tests | rg '/(test_.*|backend_test)\.py$' | rg -v '(test_preview_runtime_e2e|test_batch_5task_runtime)\.py$' | sort)
python -m pytest -q -n 0 --tb=short -rs backend/tests/test_preview_runtime_e2e.py backend/tests/test_batch_5task_runtime.py "${tests[@]}"
evidence=/workspace/come-in-current/evidence/task-9-final
for area in coupon-funding advertisement-compensation delivery-partner-allocation rewards-referral-reversal partial-cod-refund; do
  python "$evidence/$area-20261123/restart.py"
done
sed 's/8262/8282/g;s/comein_disposable_t9_approval_restart/comein_disposable_t9_final_restart/g' "$evidence/approval-readiness-20261123/restart.py" >/tmp/t9-stage11-collection.py
python /tmp/t9-stage11-collection.py
python "$evidence/final-closure-20261123/invoice-restart.py"
cd frontend
./node_modules/.bin/tsc --noEmit
./node_modules/.bin/eslint app/admin.tsx app/admin-earnings.tsx app/seller/advertisements.tsx
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8283 CI=1 ./node_modules/.bin/expo export --platform web --output-dir /tmp/t9-stage11-web
```

Run [browser.py](browser.py) with Playwright, PyMongo and requests against the exported app served by [spa.py](spa.py). External HTTPS is blocked in the browser harness.

| Area | Executed local interactions |
| --- | --- |
| Coupons | Budget race, expiry in final checkout, wrong-order reconciliation, eligible cancellation and one-time release. |
| Ads | Poster-only storage fixture, CHAND/publication gate, expired events, booking limits and evidence, removed campaign and no compensation. |
| Delivery | Scoped approval/access, existing rates and no sales-commission configuration, fee snapshot and malformed evidence without partner payable. |
| Rewards | Attribution, qualification, distinct order linkage, concurrent issuance, order invalidation, rollback and credit preservation. |
| Incremental collection | Stable offline intent preparation, observed mock responses, signature/quote/mismatch rejections and restart. |
| Partial/COD refund | Supported capture and cumulative refund safeguards, COD audit and ledger atomicity, payout-disabled review and replay. |
| Invoice | Original-linked draft, separate approvals, changed professional/Admin snapshot rejection and no duplicate draft after restart. |

Cross-policy cases remain limited to the existing authorized flows. Paid coupon refund allocation, new partner assignment/payable, real incremental collection, actual refund execution, and statutory issuance lack approval or deferred evidence.

**Results**. Full backend **707 passed, 0 failed, 1 skipped** with nine framework/dependency warnings. The single skip was unavailable external object storage at `backend/tests/backend_test.py:397`. No environment-blocked local checks and no pre-existing test failure observed. TypeScript, targeted ESLint and Expo export exited 0. Seven Chromium scenarios and 16 restart checks passed. No genuine external validation or real financial transaction occurred.

[Full](stage-11-full.log) · [Restart](stage-11-restart.log) · [Browser](stage-11-browser.log) · [TypeScript](stage-11-typescript.log) · [ESLint](stage-11-eslint.log) · [Expo](stage-11-expo.log)
