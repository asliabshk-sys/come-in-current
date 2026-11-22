# COME-IN iOS validation

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

**PARTIAL: source checks PASS; native binary/device validation BLOCKED.**

- Official Razorpay module/podspec discovered by Expo autolinking. Existing bundle ID and URL scheme preserved. iOS Hermes bundle export PASS, not an IPA/native compile.
- Generated development and production plist both contain the CHAND microphone usage description. Production ATS disallows arbitrary loads; production config requires an HTTPS non-loopback backend URL without URL credentials. Test/dev retains existing local-network defaults.
- Secure storage, camera/audio plugins and route navigation retained. Native permissions, audio formats, system interruption, checkout return and app process death remain unverified.
- Linux host has no macOS, Xcode/xcodebuild, CocoaPods, simulator, Apple signing credentials, registered device or physical iPhone. No native iOS build/device test executed.

Evidence: [ios-autolink-plain.json](evidence/resume-20261118/ios-autolink-plain.json), [native-config-prod.json](evidence/resume-20261118/native-config-prod.json), [native-validation.json](evidence/resume-20261118/native-validation.json), [native-bundles.log](evidence/resume-20261118/native-bundles.log).

Next developer/owner action: on an owned macOS/Xcode host, verify identifier ownership, install existing pinned dependencies with Yarn, provision CocoaPods and an appropriate DEVELOPMENT signing team/device, run `COMEIN_BUILD_ENV=test yarn expo run:ios`. Validate both modes and payment success/fail/cancel/interruption/return on simulator where supported and physical iPhone. Check microphone/camera grant/deny/revoke and secure session restore. No production signing/distribution authorized.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
