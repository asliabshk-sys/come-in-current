# COME-IN Android validation

Updated 2026-11-18T05:29:47.952268-08:00. Repository /workspace/come-in-current; app /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115; branch work, HEAD a223290a8866a1ebeaac982f546491fdc197ae7a. Source/platform/config checks are distinct from real provider/device validation. No LIVE keys, real payment/refund, production DB, paid infrastructure, commit/push/deploy/publish.

**PARTIAL: source checks PASS; native binary/device validation BLOCKED.**

- Expo58.0.17/RN0.88.0 and official react-native-razorpay3.0.0 preserved. Android module discovered by Expo autolinking; discovery is not native linking/compilation proof.
- Existing package ID `com.emergent.doorstepmarketplace.eulkc9` and `frontend` URL scheme unchanged. Owner must confirm identifier ownership and TEST development-build signing.
- Generated manifest checked; production sets `android:usesCleartextTraffic=false`. Development network behavior preserved. Permissions include Internet, microphone and image selection; grant/deny/revoke behavior is not device-tested.
- Android Hermes bundle PASS; mocked adapter success/cancel/failure/concurrent-checkout tests PASS. AppState refresh and server confirmation are implemented; process death, external wallet/UPI return and duplicate callbacks still require device tests.
- This Linux host has Java runtime only. Missing javac/JDK, Android SDK/sdkmanager/platform/build-tools/NDK, Gradle, adb, emulator/physical device. No APK/AAB build or emulator/device test executed.
- Installed RN defaults: minSdk24, target36, compile37, buildTools37.0.0, NDK27.1.12297006. No SDK download or paid cloud build attempted.

Evidence: [android-autolink-plain.json](evidence/resume-20261118/android-autolink-plain.json), [native-validation.json](evidence/resume-20261118/native-validation.json), [native-config-prod.json](evidence/resume-20261118/native-config-prod.json), [native-bundles.log](evidence/resume-20261118/native-bundles.log).

Next developer action: provision a compatible JDK and the recorded SDK/build-tools/NDK on an owned native build host; preserve this source/lockfile, use Yarn1.22.22, run `COMEIN_BUILD_ENV=test yarn expo run:android` for a development build (not Expo Go), then use a configured reachable TEST backend. Verify success/fail/cancel, background/resume/process-kill, delayed webhook, retry and both modes on emulator and physical device. Do not distribute/sign a production build. SDK compatibility remains unproven until compilation succeeds.


## External validation update — 2026-11-18T05:41:49.811034-08:00
See [EXTERNAL_VALIDATION_REPORT.md](EXTERNAL_VALIDATION_REPORT.md) and `evidence/external-validation-20261118T133459Z/`. Native commands attempted in isolated scratch:Android prebuild succeeds then SDK/adb unavailable;iOS Linux refused;both native/device gates BLOCKED. Actual provider TEST now authorized by user but credentials,webhook and egress absent;no real provider flow executed. Production audit stays BLOCKED. General upload empty/MIME-spoof reproduced8FAIL then fixed;25focusedPASS and12localHTTPPASS,no external storage call. Earlier regression counts remain historical and were not rerun.
