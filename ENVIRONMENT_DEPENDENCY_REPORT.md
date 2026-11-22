# COME-IN environment dependencies

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

- Running: retained MongoDB7.0.45 rs0 PRIMARY port27018, FastAPI8001 restarted with final source, Expo web3000. Health commit/abort and all67 indexes pass. Existing data/container preserved; no DB/collection drop/reset. Stored nofile workaround reapplied after restart.
- Reused existing Python3.11 venv, Yarn1.22.22, Expo58/RN0.88, browser Chromium/Playwright. No packages installed this resume. Previous session installed official Razorpay3.0.0 and necessary httpx0.28.1 test dependency; lockfile/requirements-test preserved.
- Native blockers detailed in platform reports. Existing generated JavaScript exports are retained under /workspace/come-in-tools; logs and metadata are durable evidence, not native binaries.
- Optional pypdf/openpyxl/Pillow/PyMuPDF unavailable:4 backend feature tests skipped. No optional libraries installed just to inflate a pass count. Two opt-in payment tests skip in offline selection but pass separately with explicit local opt-in.
- Razorpay key ID, key secret, webhook secret and RAZORPAY_MODE absent in local env/process. AI/SMTP provider bindings also absent. Delivery verification adapters and real notifications remain unconfigured as historically documented. Actual provider egress/delivery remains unverified. No secrets printed or requested in chat.
- Production infrastructure was not inspected/configured: TLS ingress, trusted CORS origins, dedicated strong secrets, least-privilege authenticated MongoDB, backup retention/RPO/RTO and provider bindings remain owner/developer release gates. Isolated backup/restore passed in prior recorded evidence; production recovery SLA is not established by that drill.

Evidence: [environment-status.json](evidence/resume-20261118/environment-status.json), [native-validation.json](evidence/resume-20261118/native-validation.json), [mongo-health-final.json](evidence/resume-20261118/mongo-health-final.json).

Safe TEST configuration on an owned backend only: set APP_ENV=test, RAZORPAY_MODE=test, RAZORPAY_KEY_ID to an issued TEST public ID, RAZORPAY_KEY_SECRET and RAZORPAY_WEBHOOK_SECRET via local environment/secure secret bindings. Enable Grocery online payments only when merchant capability and that TEST setup are verified. Never expose secret variables as EXPO_PUBLIC_*; never infer LIVE/TEST mode. For native production config inspection set COMEIN_BUILD_ENV=production with the real approved HTTPS backend URL; do not build/distribute production here.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
