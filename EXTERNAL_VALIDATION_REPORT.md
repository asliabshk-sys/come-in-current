# COME-IN external validation — 2026-11-18T05:41:49.811034-08:00

**NOT READY — EXTERNAL VALIDATION REMAINS.** Native commands were attempted; no native binary, device run, actual Razorpay TEST transaction/webhook/refund, or production security sign-off succeeded. Safe source defect fixed; no production/customer financial operations, LIVE credentials, production DB changes, paid setup, commit/push/deploy/publish.

Repository /workspace/come-in-current (asliabshk-sys/come-in-current), branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. App /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115 remains outside Git. All inherited work preserved.

| Validation | Final status | Evidence and scope |
|---|---|---|
| MongoDB & Backend | PASS retained/local | Previous70live and Mongo PRIMARY/transaction/67-index evidence preserved; current backend/web GET200. Upload path newly verified. No full suite or DB drill repeated. |
| Android Native Build | BLOCKED | `expo run:android --no-install` in scratch completed native prebuild, then missing SDK path/`spawn adb ENOENT` stopped it. No javac,JDK/SDK/build-tools,Gradle/adb. No APK/AAB/native compile PASS. |
| Android Device Testing | BLOCKED | No emulator/adb,KVM access,USB device bus or attached device. App launch/navigation/login/modes/native checkout/crash checks not executed on device. |
| iOS Native Build | BLOCKED | `expo run:ios --no-install` explicitly refused Linux: macOS required. No Xcode/CocoaPods or native compile. |
| iOS Device Testing | BLOCKED | No iPhone/simulator/macOS host/signing. No device launch/permissions/payment-return evidence. |
| Razorpay Actual TEST Payment | BLOCKED | No issued TEST key ID/secret/mode,0 managed secret/variable bindings; restricted egress excludes api.razorpay.com and checkout.razorpay.com. No provider transaction/order call attempted. |
| Razorpay Webhook | BLOCKED actual | Signed LOCAL HTTP/mock-provider tests historically passed; actual TEST provider delivery not performed. No configured secret,owned public HTTPS endpoint or verified dashboard subscription. |
| Razorpay Refund | BLOCKED actual | Source/local authorization/idempotency/reconciliation evidence retained. No provider TEST refund/settlement performed. |
| Production Security | BLOCKED | Scoped source/local review and confirmed upload fix passed. Actual deployment TLS,DB access controls,edge abuse controls,logs,secret policy and recovery obligations unavailable. |
| Production Configuration | BLOCKED | No identified authorized production deployment/domain/cluster,secure bindings,store identity/signing or retention/RPO/RTO evidence. Never substitute local dev settings. |

## Work actually completed

1. Read all five checkpoints,readiness,regression and platform/security reports; checked full Git status and exact last completed operation. No pending build/test from the previous session was assumed successful.
2. Rechecked available host/resources and safe credential PRESENCE only. Linux/Java runtime present; javac/Android SDK/build-tools/adb/emulator/Gradle,Xcode/CocoaPods/devices absent.0 managed secret/variable bindings;Razorpay egress hosts not allowed. No network policy changed.
3. Verified installed official Razorpay3.0.0 and retained Android/iOS autolink records. Original source/config/lockfiles hashed before work;frontend unchanged. Reused prior Hermes/config/microphone/HTTPS evidence because those files did not change. Autolink discovery is not compiled-module proof.
4. Attempted development commands in `/workspace/come-in-tools/native-external-validation-20261118`, a separate copy with shared existing node_modules. Android native generation succeeded;build stopped before compilation/device access. Generated native files retained ONLY in scratch. Original Expo architecture/package/lockfile unchanged. iOS command rejected Linux. No app/device crash log can exist for an app never launched; exact command errors retained.
5. Reproduced a general image-upload flaw:8 cases accepted empty/HTML bytes under image MIME declarations. Added matching JPEG/PNG/GIF/WebP file signatures before storage. Existing authentication,5MB bounded read,random storage paths and supported format paths preserved. This is a file-header boundary,not full image decoding/malware scanning. No optional image library installed or provider upload executed.
6. New focused regression:25PASS/0FAIL/0SKIP (2 existing dependency warnings),3.07s. Covers16 new upload type cases plus existing allocation/catalogue security checks. Rerun justified only by changed upload validation; no broad558-test rerun.
7. Restarted existing local backend with new source.12 real local HTTP checks PASS:existing local customer authentication,anonymous upload401,8 empty/spoof uploads400 before storage,2 disabled payment-config GETs. No secrets/tokens persisted,no object storage/payment/refund/webhook provider call. First restart attempt met existing port binding; original process stopped and second start succeeded;both logs retained.

## Historical results retained — not freshly executed

Backend558PASS6SKIP;70livePASS;78focused paymentPASS;7final affectedPASS;TypeScript0errors;ESLint0errors/10warnings;frontend planner11/native mock5/browser17 checks;web and Android/iOS JS exports PASS. Full source/device/provider distinctions remain. Four optional parser/OCR skips remain unverified;two local payment opt-ins passed separately previously. No warnings suppressed or old tests weakened. Backup/restore drill and financial consistency evidence retained,not repeated.

## Source-level production audit

| Control | Source evidence / observed status | Real production evidence |
|---|---|---|
| Authentication/roles | server.py JWT type/expiry,DB-backed roles,require_role;shop/customer/Restaurant ownership and delivery guard paths reviewed;prior negative security suites retained. | BLOCKED: no actual production identity/service configuration supplied |
| Price/quantity/stock/concurrency | Server quote and persisted amount/currency,transactional stock rollback,idempotency and protected status writes;historical live evidence retained. | BLOCKED: production cluster/access not inspected |
| Payment/refund forgery/replay | payment_config.py explicit mode/key boundary;signature/provider-fetch match,raw-body webhook HMAC,event ID/hash audit,admin refund eligibility/claim/reconcile. | BLOCKED: actual TEST/provider and production binding evidence missing |
| MongoDB/backup | Existing local replica set remains unchanged;loopback development container is not production security. backup-db.sh keeps URI out of argv and protected config;restore/disposable drill evidence retained. | BLOCKED:authenticated least privilege,TLS,backup schedule,retention,RPO/RTO,restore ownership unknown |
| Secrets/HTTPS/CORS | Presence-only scan;no credentials output. Production CORS explicit-origin guard;native production HTTPS/ATS/cleartext source guard and prior generated checks retained. | BLOCKED:no actual ingress/domain/secret bindings or rotation evidence |
| Abuse/logs | Existing auth IP/subject limits,assistant/media limits and payment-intent claims inspected. No abuse/load exercise or edge configuration changed. Secret-sanitized payment error paths preserved. | BLOCKED:edge rate/body limits,trusted proxy/log redaction/retention not audited |
| Uploads | Confirmed MIME-spoof defect fixed with16 new tests,existing5MB bounded read and401 ownership auth verified locally. Catalogue upload guards unchanged. | BLOCKED:real object storage integration and full image-content processing not verified |

Files inspected include backend/server.py,payment_config.py,payment_webhook.py,security_config.py,refund_rules.py,role/checkout/security tests,scripts/backup-db.sh,restore-db.sh,infra/mongodb/docker-compose.yml,docs/deployment/DEPLOYMENT_NOTES.md,frontend/app.config.js,plugins/withReleaseSafety.js,native adapter/official module metadata and retained autolink/config evidence.

## Files changed and preservation

Source: `backend/server.py`,new `backend/tests/test_image_upload_type_boundary.py`. No frontend/UI/theme/navigation/auth/refund-policy change. All previous code,backups,logs and DBs preserved. Checkpoint/project-checkpoint/readiness/regression/platform/security/provider reports and new evidence updated. Cumulative source patch updated and reverse checked;original tracked source ZIP/README unchanged. Exact current status and source manifests saved in this evidence directory.

## Next safe actions and owners

- Developer/build host: provision a compatible full JDK and Android SDK/platform37/build-tools37.0.0/NDK27.1.12297006 from the pinned RN defaults,then rerun development build in retained scratch. Add emulator or physical Android device;validate both modes,login,checkout,success/fail/cancel,duplicate callbacks,background/process kill/return,permission behavior and crash logs. This environment has no KVM/USB device path;do not claim device PASS after compilation alone.
- Developer/Apple owner: use an owned macOS/Xcode/CocoaPods/iPhone or simulator host,confirm existing bundle-ID ownership/development signing,compile and run the preserved app. No production signing/distribution here. No paid EAS build was invoked.
- Owner/provider: securely bind issued official TEST key ID/secret/webhook secret and explicit TEST mode,allow required TEST provider egress and configure an owned public HTTPS webhook. Then follow TEST procedure below. Latest user authorizes actual official TEST-only flows with authorized test accounts;no additional permission needed for that scope once resources exist. Never ask for keys in chat.
- Production owner/security: supply authorized read-only evidence/access for actual domain/TLS,CORS,DB roles/network/backup schedule,secret bindings/rotation,ingress abuse limits and sanitized logging. Do not deploy or modify production while auditing.

## Safe official Razorpay TEST procedure (BLOCKED until resources exist)

1. In secure backend environment bindings only,set APP_ENV=test,RAZORPAY_MODE=test and provider-issued RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET,RAZORPAY_WEBHOOK_SECRET. Use an isolated nonproduction replica set/test account;do not place secrets in EXPO_PUBLIC variables,source,chat,command arguments or reports. Backend must reject LIVE prefixes in this environment and must not switch modes silently.
2. Confirm sanitized config exposes only public TEST key ID/mode. Enable merchant/payment capabilities only in the isolated TEST deployment. Use backend-created server-authoritative Grocery/Restaurant orders,intents and amounts;preserve existing eligibility and refund policies.
3. On native DEVELOPMENT builds (not Expo Go) and web,use only provider-documented TEST instruments/accounts. Exercise success,failed,cancelled,interrupted checkout,duplicate callback,delayed capture and backend verification;never use real customer/card/bank data. A frontend callback alone must never confirm paid.
4. Configure TEST webhook URL `/api/restaurant/payments/razorpay-webhook` on an owned HTTPS endpoint with the matching secret. Subscribe to supported capture/failure/refund processed/failed events. Verify actual delivery IDs/logs without secrets,invalid raw-body signature rejection,retries/duplicate/out-of-order reconciliation and exact order/amount/currency binding. Simulated signing is not provider delivery.
5. For TEST refunds,use only an eligible TEST-captured payment,authorized admin,existing full-only initiation policy and a unique request ID. Exercise duplicate/failed/uncertain outcomes and observed partial events where provider-supported;never clear uncertain claims to blindly resubmit. COD never goes through Razorpay. Verify TEST provider state and persisted order/payment/refund/ledger consistency.
6. Record sanitized provider TEST order/payment/event/refund references,status,timestamps and platform/device/build evidence. Real-money operations remain prohibited. If any binding/host/device is unavailable,keep that gate BLOCKED instead of substituting mocks.

## Exact commands and evidence

Native scratch cwd `/workspace/come-in-tools/native-external-validation-20261118`:
```
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 COMEIN_BUILD_ENV=test ./node_modules/.bin/expo run:android --no-install
EXPO_NO_TELEMETRY=1 EXPO_OFFLINE=1 CI=1 COMEIN_BUILD_ENV=test ./node_modules/.bin/expo run:ios --no-install
```
Both exit1 due recorded external environment prerequisites;no native compile/device success. Isolated prebuild modified scratch package/native directory only.

Backend cwd `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend` using `/workspace/come-in-tools/py311/bin/python`:
```
python -m pytest tests/test_image_upload_type_boundary.py -q   # BEFORE:8 failed,reproduced defect
python -m pytest tests/test_image_upload_type_boundary.py tests/test_upload_allocation_bound.py tests/test_catalog_import_security_contract.py -q   # AFTER:25 passed
python /workspace/come-in-current/evidence/external-validation-20261118T133459Z/verify-upload-http.py   # 12 local HTTP checks passed
```
Exact JUnit/log artifacts: `evidence/external-validation-20261118T133459Z/upload-types-before.xml`, `upload-security-after.xml`, `upload-http-results.json`;native `android-build-attempt.log`,`ios-build-attempt.log`;safe inventory `resource-inventory.json`,`managed-environment-summary.json`,`native-evidence.json`. No historical suite rerun or fictitious provider/device pass.
