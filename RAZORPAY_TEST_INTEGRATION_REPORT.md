# Razorpay TEST integration / platform architecture (Step2 audit)

| Layer/platform | Current implementation | Required completion |
| --- | --- | --- |
| Grocery web | Standard Checkout JS, backend intent and verify, shared signed webhook | Mode enforcement, robust event audit; actual TEST delivery blocked on credentials/network |
| Restaurant web | Backend intents/verify/admin refund; customer checkout currently COD/pickup only | Reuse payment helper without UI redesign; preserve existing methods |
| Android / iOS | Helper explicitly rejects non-web; no native Razorpay dependency | Official compatible module + development build, lifecycle reconciliation; builds/devices/signing unavailable |
| Backend | Amount/currency/capture checks, transactional DB helpers, idempotency and full Restaurant refund safeguards | Central mode configuration, typed payload rejection and duplicate body identity, eligible Grocery refund path |

No real provider operation was performed. Missing credentials/network/device gates remain BLOCKED, not source-pass substitutions. Existing complete/full-refund policy is preserved; no new arbitrary partial-refund policy.


## Final resume verification — 2026-11-18T05:29:47.952268-08:00

78 focused local/mock tests PASS;7 final affected local/security tests PASS. Actual TEST keys/webhook secret/mode absent; no provider API, transaction, refund or provider delivery executed. Official native SDK installed/autolink-discovered; both JS exports pass but native binaries/devices remain blocked. See WEBHOOK_VERIFICATION_REPORT.md, REFUND_VERIFICATION_REPORT.md, platform reports and FINAL_REGRESSION_REPORT.md.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
