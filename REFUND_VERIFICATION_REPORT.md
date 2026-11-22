# COME-IN refund verification

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

**Source/local integration PASS within existing policy; real settlement BLOCKED.**

Grocery full refunds are admin-only, require a cancelled order and linked captured Razorpay INR payment with exact server amount. COD/manual methods and active/delivered orders are excluded. Atomic claim/request audit and provider-history reconciliation prevent concurrent/duplicate requests. Ambiguous provider outcome is refund_uncertain and is never blindly replayed. Observed partial refunds are reconciled, but partial initiation is rejected because no approved partial-refund policy exists. Full reversal ledger entries are idempotent; late failed provider events cannot downgrade processed money. Customer summaries and admin queue API expose status; no UI redesign.

Restaurant existing refund eligibility/full-only policy retained. Shared webhook dispatch refuses ambiguous cross-mode payment identity. Final security review additionally fixed customer cancellation/retry overwriting a concurrently paid/accepted Restaurant order.

78 focused payment/refund/webhook tests PASS; final7 affected integration/security tests PASS. Tests include real JWT authorization/401/403, Mongo rollback via validator failure, concurrent provider mock invoked once, duplicate requests, timeout uncertainty, partial observation, duplicate refund events and late failure. No actual settlement or provider API operation performed. Evidence: [payment-local.log](evidence/resume-20261118/payment-local.log), [affected-local-final.log](evidence/resume-20261118/affected-local-final.log), [security-races-before.log](evidence/resume-20261118/security-races-before.log), [security-tracking-final.log](evidence/resume-20261118/security-tracking-final.log).

An uncertain/creating intent or refund is deliberately fail-closed; an administrator must reconcile the original provider reference before permitting any further financial action. Do not clear claims and blindly retry.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
