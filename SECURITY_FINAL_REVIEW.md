# COME-IN final scoped security review

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

**Scoped source/local controls PASS after fixes; production security gate BLOCKED pending deployment-specific evidence.** This is source and local test review, not an independent penetration test or production audit.

| Area | Verified scope / result | Evidence |
|---|---|---|
| Authentication/roles | Existing Bearer JWT/type/expiry and DB-backed user roles retained; require_role, shop ownership, customer scoping and delivery boundaries inspected. Existing negative-role/ownership suites and live tests passed. | backend-final-v2.xml; live-regression-final.xml |
| Price/stock/order ownership | Server quote/amount/currency and transactional reservation/rollback/idempotency checked by offline/live suites. | live-regression-final.xml; mongo-health-final.json |
| Payment/refund | Explicit mode/key boundaries, backend provider fetch + signatures, admin refund authorization, duplicate/uncertain financial operations fail closed. No secret frontend response or actual provider request in tests. | payment-local.xml; affected-local-final.xml |
| Webhooks | Raw-body signatures, strict payload/event ID, duplicate/conflict audit and delayed-event safety. Provider delivery unverified. | WEBHOOK_VERIFICATION_REPORT.md |
| Verified race defects | Cancel/retry originally overwrote an order paid/accepted after its initial read.4 deterministic reproductions FAILED before; compare-and-set ownership/status/payment filters now return409 and preserve state. | security-races-before.xml; security-races-after.xml |
| Verified upload allocation defect | General image endpoint originally read all bytes before5MB rejection. Reproduction FAILED before; read now capped at MAX_UPLOAD_BYTES+1, rejecting before object storage. This bounds application read, not ingress multipart spooling. Existing MIME allowlist/random storage paths/path traversal checks preserved. Deep image decoding/object provider behavior is not verified. | upload-bound-before.log; security-final-focused.xml |
| Abuse controls | Existing auth subject/IP windows, assistant/media rate checks and idempotent payment-intent claims inspected. Public endpoint abuse/load and reverse-proxy request-size/rate controls not proven. | server.py _check_auth_rate_limit/_record_auth_attempt; relevant regression tests |
| Secrets/logging | Presence-only env audit; payment config errors sanitized, secrets excluded from settings repr/frontend config. Generic exception log sites reviewed; no real secret-bearing provider request executed. Dedicated production keys, log retention/redaction policy and secure bindings remain external. | environment-status.json; test_payment_environment_boundary.py |
| HTTPS/CORS/DB | Production native ATS/cleartext and HTTPS URL gate passed; backend production CORS explicit-origin guard present. Local DB transactions/indexes pass; production TLS/DB auth/network/roles not audited. | config-and-guard-check.log; native-config-prod.json; mongo-health-final.json |

No security rules weakened. Source fixes: backend/server.py conditional Restaurant transitions and bounded general image upload; command-guard catch binding restored. Auth/UI/product/refund policies preserved. All failures and corrected runs retained. Next owner/developer action is production configuration/security review and isolated native/TEST resource provisioning, not deployment.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
