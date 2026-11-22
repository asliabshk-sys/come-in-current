# Android / iOS Native Validation Report

Project: COME-IN. Current audit time: 2026-11-19T14:14:11.601290+05:30 (Asia/Kolkata). Repository `/workspace/come-in-current`,branch `work`,HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a` (root verified). Application extraction `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115` is outsideGit andcontains inherited uncommitted work;the HEAD alone doesnot identify these source bytes. Source hashes and prior-input hashes are in [native-provider-validation.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/native-provider-validation.json>).

This workstream changed only NEW iteration evidence/reports. No source,configuration,environment,dependency,originalreport,checkpoint,ZIP or Git history changes. No native project generation,packageinstall,productionoperation,provider call,payment orrefund. Existing prior inventory was reused;179API/60model inventory was not regenerated. The previous27-entry manifest remains untouched. No Task2 started.

## Executed checks and current results

| ID | Validation | Status | Evidence boundary |
| --- | --- | --- | --- |
| NATIVE-01 | Current native host/toolchain inventory | PASS | Executed read-only platform/tool/path inspection;PASS is inventory success,not build readiness. |
| NATIVE-02 | Android Razorpay autolink metadata | PASS | Fresh command exit0 resolves RazorpayPackage/codegen metadata;not compilation or runtime linking. |
| NATIVE-03 | iOS Razorpay autolink metadata | PASS | Fresh command exit0 resolves installed3.0.0podspec;not pod installation or runtime linking. |
| NATIVE-04 | Android native debug build | BLOCKED | No javac,Android SDK/build-tools/sdkmanager/Gradle or configured SDK path;no build attempted. |
| NATIVE-05 | Android emulator/device runtime workflows | BLOCKED | No adb/emulator/KVM/USB device evidence or compiled build. |
| NATIVE-06 | iOS native debug build | BLOCKED | Linux,no macOS/Xcode/xcrun/CocoaPods or generatediOSproject;no build attempted. |
| NATIVE-07 | iOS simulator/device runtime workflows | BLOCKED | No authorized Apple build host/simulator/device/binary/signing evidence. |
| NATIVE-08 | Android actual TEST payment success/failure/cancel/resume | BLOCKED | Requires native debug build/device and authorized actual provider TEST setup. |
| NATIVE-09 | iOS actual TEST payment success/failure/cancel/resume | BLOCKED | Requires native debug build/device and authorized actual provider TEST setup. |

| Command | Exit | Output |
| --- | --- | --- |
| java -version | 0 | [java-version.stdout](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/java-version.stdout>) [java-version.stderr](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/java-version.stderr>) |
| node node_modules/expo-modules-autolinking/bin/expo-modules-autolinking.js react-native-config --platform android --json | 0 | [android-autolinking-current.stdout](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/android-autolinking-current.stdout>) [android-autolinking-current.stderr](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/android-autolinking-current.stderr>) |
| node node_modules/expo-modules-autolinking/bin/expo-modules-autolinking.js react-native-config --platform ios --json | 0 | [ios-autolinking-current.stdout](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/ios-autolinking-current.stdout>) [ios-autolinking-current.stderr](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/ios-autolinking-current.stderr>) |

The Java command reports OpenJDK runtime21.0.13. `javac` is absent;runtime presence is not a complete JDK. Android SDK environment bindings and inspected conventionalSDKpaths are absent;`sdkmanager`,`adb`,`emulator`,`gradle`,`/dev/kvm` and`/dev/bus/usb` are absent. No emulator/device was enumerated viaADB becauseADB is unavailable. No macOS,Xcode,xcrun,CocoaPods or Apple simulator/device evidence exists in this Linuxhost. These are fresh observations,not a re-labeling of the old failed build logs.

Android andiOS autolink query exits0prove **metadata discovery only**:Android resolves`com.razorpay.rn.RazorpayPackage` and`RNRazorpayCheckoutSpec`;iOS resolves theinstalled3.0.0podspec. A generated CMakepath inmetadata doesnot prove thatfileexists/codegencompiled. NoJNI/Java/Objective-C/Swift binary linked or launched. No JSbundle/webbuild was counted as a nativebuild.

## Source configuration inspected

| Area | Observed source evidence | Limit |
| --- | --- | --- |
| Expo/RN/native wrapper | InstalledExpo58.0.17,ReactNative0.88.0,react-native-razorpay3.0.0;dependency versions match package declarations. | Package metadata and peer ranges do not prove this combination compiles or works ondevices. |
| Android applicationID /iOS bundleID | [app.json](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app.json>) declares com.emergent.doorstepmarketplace.eulkc9 forboth. | No generatedmergedmanifest,Info.plist or compiledbundle examined. |
| Scheme/return navigation | app.json scheme frontend;sharedpaymentcomponent refreshesonAppStateactive;nativeadapterusesSDKpromise. | No observeddeeplink/resume/cold-start/crash logs;nativeSDK callback behavior unverified. |
| Microphone/camera/photos | Expoimagepicker/audio configdeclaresusage text;withReleaseSafetyforcesNSMicrophoneUsageDescription. | No actualpermissionprompt,denial/background/lifecycle test. |
| Networksecurity | [app.config.js](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/app.config.js>) requirespubliccredential-freeHTTPSbackendURL forproduction;[withReleaseSafety.js](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/plugins/withReleaseSafety.js>) declaresAndroidcleartextfalse/iOSATSarbitraryloadsfalse inproduction. | Staticdeclarations,not finalgeneratedmanifest/Info.plist or actualproductionHTTPSaudit. |
| Android SDK dependency | [build.gradle](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/node_modules/react-native-razorpay/android/build.gradle>) declarescom.razorpay:checkout:1.6.41 andinheritsappSDKvalueswithmodulefallbacks. | Effectiveappcompile/min/targetSDKandtransitiveartifactresolution notbuilt. |
| iOS SDK dependency | [react-native-razorpay.podspec](</workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/node_modules/react-native-razorpay/react-native-razorpay.podspec>) declaresrazorpay-pod andpodspecminimumiOS10.0. | NoPodfile.lock/resolvedSDKversion/effectiveExpodeploymenttarget or CocoaPodsinstallation proof. |
| Build architecture | ManagedExpoapp hasnoandroid/iosdirectory,eas.json,orinstalledexpo-dev-client. | No customnativebinary exists here. expo-dev-clientabsence is not byitself proofExpo run debug is impossible;ExpoGo doesnot include Razorpay. |

## Minimum closure procedure — NOT EXECUTED

1. Native developer provisions an authorized Android host with the appropriate JDK/compiler,AndroidSDK/platforms/buildtools/platformtools and an emulator or physicaldevice. Usean isolatedsourcecopy boundtothereportedhashes;do notgeneratefiles intheprotectedextraction. No paidresource orproductionrelease signing isauthorized.
2. Configure a reachable **non-production TEST backend** overHTTPS via secure environmentvariables. Preserve theexistingYarn1.22.22/lockfile conventions. In theisolatedfrontend,run`COMEIN_BUILD_ENV=test EXPO_PUBLIC_BACKEND_URL="$COMEIN_TEST_BACKEND_HTTPS_URL" node node_modules/expo/bin/cli run:android --variant debug --device`. This commandis a futureprocedure,not executed evidence. If using a customExpo developmentclient,its dependency/configuration mustbe approved/provisioned separately;ExpoGo isinsufficient.
3. Capture Gradle command/version,fullnativebuildlog,APKhash,sourcehashes,effectiveAndroidmanifest/permissions/networkconfig,autolink output,`adb devices -l` anddevice/OSdetails. Install/launch only theauthorizeddebugbuild,then capturebounded`adb logcat` filteredtoappPID,withnosensitiveinputs.
4. OnanauthorizedmacOS/Xcode/CocoaPodshost,prepare thesameisolatedsourcecopy andsecureTESTbackendbinding. Run`COMEIN_BUILD_ENV=test EXPO_PUBLIC_BACKEND_URL="$COMEIN_TEST_BACKEND_HTTPS_URL" node node_modules/expo/bin/cli run:ios --configuration Debug --device`. Simulator testing doesnotreplacephysicaliPhonetesting. Anydevice-specificdebugsigningrequiresitsauthorizeddeveloperconfiguration;nofakecertificates orproductiondistribution.
5. Capture Xcode/CocoaPodversions,resolvedPodfile.lock,app/buildhashes,buildlog,finalInfo.plist,simulator/deviceidentity andredactedcrash/consolelogs.
6. Executeapp launch/login/logout/permissions/navigation/CHAND/Grocery/Restaurantcart-checkout flows onbothplatforms. With genuineapprovedRazorpayTESTresources,verify success,failure,cancel,background/resume,networkinterruption,duplicatecallback,delayedcapture andreturnnavigation. Checkserverstate,notfrontendmessages alone. PreserveuserpoliciesandUI. Recordexactplatform/source/providerreferences withoutsecrets.

Closure requires successfulcompileddebugbinaries **and** requiredruntime/devicecaseevidence. CurrentAndroid/iOSbuilds anddevicevalidation remainBLOCKED;no successfulnativebuild/devicevalidation isclaimed.
