# Latest external-validation checkpoint — 2026-11-18T05:41:49.811034-08:00

**NOT READY — EXTERNAL VALIDATION REMAINS.** Actual Android/iOS native command attempts are BLOCKED by missing toolchains/devices. Actual Razorpay TEST payment/webhook/refund BLOCKED by missing issued TEST bindings and egress. Production security/configuration BLOCKED by missing actual infrastructure evidence. New verified upload MIME-spoof defect fixed;25 focused tests and12 local HTTP checks PASS. Prior558PASS6SKIP,70livePASS,78focusedPASS,TypeScript0 andESLint0errors10warnings are retained HISTORICAL evidence,not rerun. No UI/product/payment-policy changes or production/publish operations.

See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) for exact10-gate matrix,commands,results,provider TEST procedure and next actions. Evidence: `evidence/external-validation-20261118T133459Z/`.

---
## Previous report retained

# COME-IN final regression report

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

| Check | Exact result | Evidence |
|---|---|---|
| Final full offline/backend selection | 558 PASS / 0 FAIL / 6 SKIPPED;2 dependency deprecation warnings,32.19s | backend-final-v2.log/xml |
| Final live backend/Grocery/Restaurant/auth/Mongo | 70 PASS / 0 FAIL / 0 SKIPPED,9.33s | live-regression-final.log/xml |
| Focused payment/webhook/refund | 78 PASS / 0 FAIL / 0 SKIPPED,8.27s;8 dependency/lifespan warnings | payment-local.log/xml |
| Final affected local integration + security | 7 PASS / 0 FAIL / 0 SKIPPED,5.57s | affected-local-final.log/xml |
| Security/tracking focused | 17 PASS / 0 FAIL / 0 SKIPPED,1.74s | security-tracking-final.log/xml |
| Frontend planner/native adapter | 11 assertions PASS / 5 mocked SDK checks PASS | frontend-planner.log; frontend-native-contract.log |
| TypeScript | 0 errors,exit0 | typecheck.log |
| ESLint | 0 errors / 10 warnings,exit0 | eslint.json |
| Web export | PASS exit0 | web-build.log |
| Android+iOS JS export | Both Hermes bundles PASS exit0,not native binaries | native-bundles.log |
| Native config/autolink | 5 source/config checks PASS,not compiled module proof | native-validation.json |
| Production URL/guard | 9 PASS / 0 FAIL | config-and-guard-check.log |
| Home/CHAND browser | 5 PASS,0 page errors | home-chand-browser.json |
| Authenticated browser | 12 PASS,0 page errors: real customer/seller/Restaurant-owner/admin login +2 routes per role | browser-roles-v2.json |
| Mongo health | PRIMARY rs0 Mongo7.0.45;transaction commit/abort PASS;67 expected indexes,no missing | mongo-health-final.json |

Counts overlap across focused/full runs; do not sum them as unique tests. Four skips are optional missing pypdf/openpyxl/Pillow/PyMuPDF. Two local integration skips in offline selection passed under explicit local opt-in separately. Legacy backend_test.py not executed/countable as passed; current70-test runtime suites cover the current API. Prior backup/restore6 checks and financial5 checks retained from release-completion-20261117T094751Z and not rerun unnecessarily.

Failed/corrected evidence preserved: initial offline551PASS/2staleFAIL/6SKIP; stronger architecture contracts24PASS; v2 offline553PASS/6SKIP before5 new security tests. Race reproductions4FAIL and upload allocation reproduction1FAIL before fixes. A final intermediate run557PASS/1format-contractFAIL/6SKIP was corrected by retaining original dictionary formatting (assertion unchanged); final558PASS/6SKIP. First role-browser run timed out during the service transition; stable-service rerun12PASS. No checks disabled or suppressions added.

All42 prior ESLint warnings reviewed:32 safe warnings removed in inherited partial cleanup (imports/variables/array style/duplicate imports/caught binding); one referenced catch variable was mistakenly removed and restored this resume. Ten retained diagnostics:9 hook-dependency warnings and1 generated Expo unused directive. No generated declaration edited; no rules disabled. Hook changes would affect request lifetimes and need separate scoped behavior validation. Complete current diagnostics follow.

| File:line | Rule | Severity | Diagnostic |
|---|---|---|---|
| frontend/.expo/types/router.d.ts:1 | unused-eslint-disable-directive | 1 (warning) | Unused eslint-disable directive (no problems were reported). |
| frontend/app/chand.tsx:190 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useMemo has an unnecessary dependency: 'lang'. Either exclude it or remove the dependency array. |
| frontend/app/checkout.tsx:88 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useEffect has missing dependencies: 'hasDemoItems', 'hasMixedShops', and 'shopIds'. Either include them or remove the dependency array. |
| frontend/app/restaurant/[id].tsx:12 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useEffect has a missing dependency: 'local'. Either include it or remove the dependency array. |
| frontend/app/restaurant/checkout.tsx:75 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useEffect has a missing dependency: 'user'. Either include it or remove the dependency array. |
| frontend/app/restaurant/dashboard.tsx:13 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useCallback has a missing dependency: 'selected'. Either include it or remove the dependency array. |
| frontend/app/restaurant/orders/index.tsx:51 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useCallback has a missing dependency: 'user'. Either include it or remove the dependency array. |
| frontend/app/services.tsx:20 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useEffect has a missing dependency: 'loadDashboard'. Either include it or remove the dependency array. |
| frontend/src/components/MeasuredQuantityPicker.tsx:45 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useEffect has a missing dependency: 't'. Either include it or remove the dependency array. |
| frontend/src/restaurant/useDiscoveryAddress.ts:64 | react-hooks/exhaustive-deps | 1 (warning) | React Hook useCallback has a missing dependency: 'user'. Either include it or remove the dependency array. |

Exact commands: [COMMANDS.md](evidence/resume-20261118/COMMANDS.md). Test result index: [test-results-summary.json](evidence/resume-20261118/test-results-summary.json).
