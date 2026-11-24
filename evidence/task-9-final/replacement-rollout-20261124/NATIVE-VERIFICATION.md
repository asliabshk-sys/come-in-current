# Native device verification

| Target | Result | Environment evidence and prerequisite |
| --- | --- | --- |
| iOS | BLOCKED | Linux workspace, no Xcode or `xcrun`, and no connected iOS device or simulator. Provide a signed Expo-compatible development build on a connected iPhone or a macOS/Xcode simulator with access to the isolated API. |
| Android | BLOCKED | No `adb`, Android SDK/emulator, `/dev/kvm`, connected device or APK in the retained workspace. Provide an Expo-compatible development build on a connected authorized Android device or a working emulator with API access. |
| Expo development build network reachability from either native target | NOT TESTED | Supply the device-routable isolated HTTPS backend URL through `EXPO_PUBLIC_BACKEND_URL` and verify it from each target. Loopback web connectivity was exercised separately. |

On each target, use synthetic orders and run Grocery and Restaurant independently. Create an offer and check its in-app notice, deadline display, expiry and Admin adjustment. Withdraw and confirm item removal and the revised total. Check that acceptance, packing/preparation and dispatch protect the order and keep Assist reachable. Repeat across background/resume and app restart, interrupt the network during a decision, and verify retry, duplicate protection, and customer-visible errors. Record OS, device/build, API environment and results. Chromium evidence applies only to web.
