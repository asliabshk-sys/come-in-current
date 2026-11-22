# COME-IN webhook verification

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

**Source/local integration PASS; actual Razorpay delivery BLOCKED.**

Raw-body HMAC with constant-time comparison, mode-specific server secret, signed JSON/schema checks, provider event-ID requirement, payload-hash identity conflict detection, duplicate receipt uniqueness and post-processing receipt recording are implemented. Payment/order/amount/currency are validated before capture. Transactions protect order/payment state; paid/processed outcomes survive delayed failure. Unknown valid events are audited as ignored. Failed event receipt after financial commit was injected; retry repaired the audit receipt without replaying payment effects. Grocery partial/full refund events and duplicate/late-failed events were exercised through local signed HTTP.

Tests use in-memory local signing material, HTTP ASGI, real isolated retained MongoDB and forbidden/mocked outbound provider calls. This is not actual provider webhook delivery. Focused selection78PASS, final affected integration/security selection7PASS. Evidence: [payment-local.log](evidence/resume-20261118/payment-local.log), [affected-local-final.log](evidence/resume-20261118/affected-local-final.log).

Real TEST delivery requires secure backend-only TEST key/secret/mode and webhook secret, an owned reachable HTTPS endpoint `/api/restaurant/payments/razorpay-webhook`, matching TEST provider subscriptions for payment.captured/payment.failed/refund.processed/refund.failed where supported, and owner/provider delivery verification. Never put secrets in chat or frontend. Do not send actual payment/refund requests in this session.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
