"""Read-only native/toolchain and Razorpay configuration evidence;no providers called."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import ast
import hashlib
import json
import os
import platform
import shutil

OUT=Path(__file__).resolve().parent
APP=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115')
REPO=Path('/workspace/come-in-current')
PREVIOUS=REPO/'evidence/phase-1-task-1-owner-review/iteration-2026-11-18T072632-0800'
NOW=datetime.now(ZoneInfo('Asia/Kolkata')).isoformat()
HEAD='a223290a8866a1ebeaac982f546491fdc197ae7a'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def link(p,line=None,label=None):
    p=Path(p)
    return f'[{label or p.name}](<{p}{":"+str(line) if line else ""}>)'

def table(headers,rows):
    clean=lambda v:str(v).replace('|','\\|').replace('\n','<br>')
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(clean(v) for v in r)+' |' for r in rows])+'\n'

def env_presence(p):
    """Never return or store credential values;boolean presence metadata only."""
    selected={'APP_ENV','ENVIRONMENT','RAZORPAY_MODE','RAZORPAY_KEY_ID','RAZORPAY_KEY_SECRET','RAZORPAY_WEBHOOK_SECRET'}
    result={k:{'declared':False,'nonempty':False} for k in sorted(selected)}
    if p.exists():
        for line in p.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith('#') and '=' in line:
                k,v=line.split('=',1);k=k.strip()
                if k in selected:
                    result[k]={'declared':True,'nonempty':bool(v.strip().strip('"').strip("'"))}
    return {'path':str(p),'exists':p.exists(),'key_presence_only':result}

inputs=[]
for name in ['FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md','FINAL_SECURITY_VALIDATION_REPORT.md','FINAL_NAVIGATION_AND_API_INVENTORY.md','FINAL_PRESERVATION_VERIFICATION.md','FINAL_OWNER_DECISION_READINESS.md','FINAL_REVIEW_MANIFEST.json','ITERATION_CHECKPOINT.md']:
    p=PREVIOUS/name;s=p.read_text();inputs.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read':True})
source_paths=[
 'frontend/package.json','frontend/app.json','frontend/app.config.js','frontend/plugins/withReleaseSafety.js',
 'frontend/src/lib/razorpay.ts','frontend/src/lib/razorpay-checkout.ts','frontend/src/lib/razorpay-checkout.native.ts',
 'frontend/src/components/GroceryOnlinePayment.tsx','frontend/app/checkout.tsx','frontend/app/restaurant/checkout.tsx',
 'backend/payment_config.py','backend/payment_webhook.py','backend/refund_rules.py','backend/security_config.py','backend/server.py','backend/.env.example',
 'frontend/node_modules/react-native-razorpay/package.json','frontend/node_modules/react-native-razorpay/react-native-razorpay.podspec',
 'frontend/node_modules/react-native-razorpay/android/build.gradle']
sources=[{'path':str(APP/n),'sha256':sha(APP/n),'bytes':(APP/n).stat().st_size} for n in source_paths]
tools={n:shutil.which(n) for n in ['java','javac','gradle','adb','emulator','sdkmanager','xcodebuild','xcrun','pod','eas','node','yarn']}
env_names=['JAVA_HOME','ANDROID_HOME','ANDROID_SDK_ROOT','DEVELOPER_DIR','EXPO_TOKEN','EAS_ACCESS_TOKEN',
 'APP_ENV','ENVIRONMENT','RAZORPAY_MODE','RAZORPAY_KEY_ID','RAZORPAY_KEY_SECRET','RAZORPAY_WEBHOOK_SECRET']
process_presence={n:bool(os.environ.get(n)) for n in env_names}
paths=[Path('/dev/kvm'),Path('/dev/bus/usb'),Path('/opt/android-sdk'),Path('/usr/local/android-sdk'),Path.home()/'Android/Sdk',Path('/Applications/Xcode.app'),APP/'frontend/android',APP/'frontend/ios',APP/'frontend/eas.json']
path_presence={str(p):p.exists() for p in paths}
binding_presence=[env_presence(APP/'backend/.env'),env_presence(APP/'frontend/.env')]
commands=json.loads((OUT/'native-current-command-results.json').read_text())
assert len(commands)==3 and all(c['exit_code']==0 for c in commands)
assert commands[1]['razorpay_dependency_detected'] and commands[2]['razorpay_dependency_detected']
versions={}
for name in ['expo','react-native','react-native-razorpay','expo-dev-client']:
    p=APP/'frontend/node_modules'/name/'package.json'
    versions[name]=json.loads(p.read_text()).get('version') if p.exists() else None
symbols={n.name:{'line':n.lineno,'end_line':n.end_lineno} for n in ast.parse((APP/'backend/server.py').read_text()).body if isinstance(n,(ast.AsyncFunctionDef,ast.FunctionDef))}

native_checks=[
 {'id':'NATIVE-01','validation':'Current native host/toolchain inventory','status':'PASS','scope':'Executed read-only platform/tool/path inspection;PASS is inventory success,not build readiness.'},
 {'id':'NATIVE-02','validation':'Android Razorpay autolink metadata','status':'PASS','scope':'Fresh command exit0 resolves RazorpayPackage/codegen metadata;not compilation or runtime linking.'},
 {'id':'NATIVE-03','validation':'iOS Razorpay autolink metadata','status':'PASS','scope':'Fresh command exit0 resolves installed3.0.0podspec;not pod installation or runtime linking.'},
 {'id':'NATIVE-04','validation':'Android native debug build','status':'BLOCKED','scope':'No javac,Android SDK/build-tools/sdkmanager/Gradle or configured SDK path;no build attempted.'},
 {'id':'NATIVE-05','validation':'Android emulator/device runtime workflows','status':'BLOCKED','scope':'No adb/emulator/KVM/USB device evidence or compiled build.'},
 {'id':'NATIVE-06','validation':'iOS native debug build','status':'BLOCKED','scope':'Linux,no macOS/Xcode/xcrun/CocoaPods or generatediOSproject;no build attempted.'},
 {'id':'NATIVE-07','validation':'iOS simulator/device runtime workflows','status':'BLOCKED','scope':'No authorized Apple build host/simulator/device/binary/signing evidence.'},
 {'id':'NATIVE-08','validation':'Android actual TEST payment success/failure/cancel/resume','status':'BLOCKED','scope':'Requires native debug build/device and authorized actual provider TEST setup.'},
 {'id':'NATIVE-09','validation':'iOS actual TEST payment success/failure/cancel/resume','status':'BLOCKED','scope':'Requires native debug build/device and authorized actual provider TEST setup.'},
]
provider_checks=[
 {'id':'PROVIDER-01','validation':'Current TEST binding presence inspection','status':'PASS','scope':'Presence-only inspection succeeded;allthree backend key/secret values empty andmodeabsent. Not payment verification.'},
 {'id':'PROVIDER-02','validation':'Actual Razorpay TEST payment order creation','status':'BLOCKED','scope':'No explicitly configured nonempty TEST keypair/mode or authorized TEST account.'},
 {'id':'PROVIDER-03','validation':'Actual TEST checkout success/failure/pending/reconciliation','status':'BLOCKED','scope':'Missing TEST account/credentials/native/web checkout interaction and source-bound provider records.'},
 {'id':'PROVIDER-04','validation':'Actual provider webhook delivery/duplicate/retry validation','status':'BLOCKED','scope':'No configured webhook secret,owned reachable HTTPS TEST endpoint or provider delivery records.'},
 {'id':'PROVIDER-05','validation':'Actual TEST refund creation/status/duplicate/refund webhook','status':'BLOCKED','scope':'No eligible genuine TEST captured payment/provider account or refund/delivery evidence.'},
 {'id':'PROVIDER-06','validation':'Actual provider payment/refund database consistency','status':'BLOCKED','scope':'No genuine provider event/transaction records to reconcile against isolated appDB.'},
]
matrix=[
 ['Environment/key separation','backend/payment_config.py:14','Explicitmode,matchingkeyprefix and production/environment consistency checks declared;no silent key-mode switch.','Source inspected;functional results belong to regression evidence.'],
 ['Grocery server payment intent','backend/server.py:'+str(symbols['create_grocery_payment_intent']['line']),'Authenticated owner scope,server order total/INR,existing-intent reuse,atomic claim anduncertain state on provider error.','No actual provider order created.'],
 ['Restaurant server payment intent','backend/server.py:'+str(symbols['create_restaurant_payment_intent']['line']),'Customer ownership,pending-online eligibility,server total/INR,reuse andintentclaim.','No actual provider order created.'],
 ['Callback verification inbothmodes','backend/server.py:'+str(symbols['verify_restaurant_payment']['line'])+' / '+str(symbols['verify_grocery_payment']['line']),'HMAC check andprovider GET require capturedstatus,matchingpayment/order IDs,exact amount/INR beforeDBpaidtransition.','No callback or providerGETexecuted bythis workstream.'],
 ['Raw webhook signature andevents','backend/server.py:'+str(symbols['razorpay_webhook']['line']),'HMAC over raw requestbody,eventID/bodyhash duplicate check,explicitcaptured/failed/refundevents,recordafterprocessing.','Genuine delivery/retries remainBLOCKED;upstream requestsize limit stillunverified.'],
 ['Grocery refund','backend/server.py:'+str(symbols['admin_refund_grocery_order']['line'])+';backend/refund_rules.py:22','Admin-only,verifiedcaptured online/cancelled eligibility,full amount only,requestID duplicateprotection,transactional claim,providerhistorycheck anduncertain/reconciliation states.','CODdoesnotenterproviderrefund;partial policy notinvented or changed.'],
 ['Restaurant refund','backend/server.py:'+str(symbols['admin_refund_restaurant_order']['line']),'Admin dependency,verifiedpaidlinkedpayment,eligibleamount consistency,transactional claim,providerhistorychecks andpending/uncertain/finalstateguard.','Existingfullrefundbehaviorretained;actualprovideracceptance/settlement unverified.'],
 ['Native checkout and lifecycle','frontend/src/lib/razorpay-checkout.native.ts:5;frontend/src/components/GroceryOnlinePayment.tsx:16','Runtime nativemoduleguard,SDK.open,duplicate-windowguard,cancellationmessages;sharedcomponentrefreshesonAppStateactive andasksbackendtoverifycallback.','Source/metadata only;Android/iOSinterruption,returnnavigation,crashesandSDKcallbackbehavior notexercised.'],
 ['Web checkout','frontend/src/lib/razorpay-checkout.ts:4','Official checkoutscript URL,successcallback,dismiss/failurehandling;backendremainsauthoritative.','No web providerpayment or checkoutscriptrequest made.']]

data={'project':'COME-IN','timestamp_Asia_Kolkata':NOW,'repository':str(REPO),'branch':'work','HEAD':HEAD,
 'application_extraction':str(APP),'source_tree_is_git_HEAD':False,
 'scope':'Current native prerequisites/autolink metadata and source/payment TEST-readiness audit. No app builds,devices,providers or configuration changes.',
 'prior_inputs':inputs,'source_hashes':sources,'platform':{'system':platform.system(),'machine':platform.machine(),'release':platform.release()},
 'tools':tools,'path_presence':path_presence,'environment_presence_only':process_presence,'binding_presence_only':binding_presence,
 'installed_package_versions':versions,'native_command_results':commands,'native_checks':native_checks,'provider_checks':provider_checks,
 'payment_source_matrix':matrix,'provider_calls_executed':0,'native_builds_executed':0,'device_tests_executed':0,
 'native_projects_generated':0,'production_credentials_used':False,'secrets_printed_or_written':False,'packages_installed':False,'protected_files_modified':False,
 'payment_mock_tests_executed_in_this_workstream':0,'mock_tests_owner':'Root/current_regression agent;results are separate from real provider acceptance.',
 'final_native_status':'BLOCKED','final_actual_provider_status':'BLOCKED','Task2_started':False}
(OUT/'native-provider-validation.json').write_text(json.dumps(data,indent=2)+'\n')

common=f'''Project: COME-IN. Current audit time: {NOW} (Asia/Kolkata). Repository `{REPO}`,branch `work`,HEAD `{HEAD}` (root verified). Application extraction `{APP}` is outsideGit andcontains inherited uncommitted work;the HEAD alone doesnot identify these source bytes. Source hashes and prior-input hashes are in {link(OUT/'native-provider-validation.json')}.

This workstream changed only NEW iteration evidence/reports. No source,configuration,environment,dependency,originalreport,checkpoint,ZIP or Git history changes. No native project generation,packageinstall,productionoperation,provider call,payment orrefund. Existing prior inventory was reused;179API/60model inventory was not regenerated. The previous27-entry manifest remains untouched. No Task2 started.

'''
native='# Android / iOS Native Validation Report\n\n'+common
native+='## Executed checks and current results\n\n'+table(['ID','Validation','Status','Evidence boundary'],[[c['id'],c['validation'],c['status'],c['scope']] for c in native_checks])
native+='\n'+table(['Command','Exit','Output'],[[' '.join(c['command']),c['exit_code'],link(OUT/c['stdout_artifact'])+' '+link(OUT/c['stderr_artifact'])] for c in commands])
native+=f'''
The Java command reports OpenJDK runtime21.0.13. `javac` is absent;runtime presence is not a complete JDK. Android SDK environment bindings and inspected conventionalSDKpaths are absent;`sdkmanager`,`adb`,`emulator`,`gradle`,`/dev/kvm` and`/dev/bus/usb` are absent. No emulator/device was enumerated viaADB becauseADB is unavailable. No macOS,Xcode,xcrun,CocoaPods or Apple simulator/device evidence exists in this Linuxhost. These are fresh observations,not a re-labeling of the old failed build logs.

Android andiOS autolink query exits0prove **metadata discovery only**:Android resolves`com.razorpay.rn.RazorpayPackage` and`RNRazorpayCheckoutSpec`;iOS resolves theinstalled3.0.0podspec. A generated CMakepath inmetadata doesnot prove thatfileexists/codegencompiled. NoJNI/Java/Objective-C/Swift binary linked or launched. No JSbundle/webbuild was counted as a nativebuild.

## Source configuration inspected

'''
native+=table(['Area','Observed source evidence','Limit'],[
 ['Expo/RN/native wrapper','InstalledExpo58.0.17,ReactNative0.88.0,react-native-razorpay3.0.0;dependency versions match package declarations.','Package metadata and peer ranges do not prove this combination compiles or works ondevices.'],
 ['Android applicationID /iOS bundleID',link(APP/'frontend/app.json')+' declares com.emergent.doorstepmarketplace.eulkc9 forboth.','No generatedmergedmanifest,Info.plist or compiledbundle examined.'],
 ['Scheme/return navigation','app.json scheme frontend;sharedpaymentcomponent refreshesonAppStateactive;nativeadapterusesSDKpromise.','No observeddeeplink/resume/cold-start/crash logs;nativeSDK callback behavior unverified.'],
 ['Microphone/camera/photos','Expoimagepicker/audio configdeclaresusage text;withReleaseSafetyforcesNSMicrophoneUsageDescription.','No actualpermissionprompt,denial/background/lifecycle test.'],
 ['Networksecurity',link(APP/'frontend/app.config.js')+' requirespubliccredential-freeHTTPSbackendURL forproduction;'+link(APP/'frontend/plugins/withReleaseSafety.js')+' declaresAndroidcleartextfalse/iOSATSarbitraryloadsfalse inproduction.','Staticdeclarations,not finalgeneratedmanifest/Info.plist or actualproductionHTTPSaudit.'],
 ['Android SDK dependency',link(APP/'frontend/node_modules/react-native-razorpay/android/build.gradle')+' declarescom.razorpay:checkout:1.6.41 andinheritsappSDKvalueswithmodulefallbacks.','Effectiveappcompile/min/targetSDKandtransitiveartifactresolution notbuilt.'],
 ['iOS SDK dependency',link(APP/'frontend/node_modules/react-native-razorpay/react-native-razorpay.podspec')+' declaresrazorpay-pod andpodspecminimumiOS10.0.','NoPodfile.lock/resolvedSDKversion/effectiveExpodeploymenttarget or CocoaPodsinstallation proof.'],
 ['Build architecture','ManagedExpoapp hasnoandroid/iosdirectory,eas.json,orinstalledexpo-dev-client.','No customnativebinary exists here. expo-dev-clientabsence is not byitself proofExpo run debug is impossible;ExpoGo doesnot include Razorpay.']])
native+='\n## Minimum closure procedure — NOT EXECUTED\n\n'
native+='''1. Native developer provisions an authorized Android host with the appropriate JDK/compiler,AndroidSDK/platforms/buildtools/platformtools and an emulator or physicaldevice. Usean isolatedsourcecopy boundtothereportedhashes;do notgeneratefiles intheprotectedextraction. No paidresource orproductionrelease signing isauthorized.
2. Configure a reachable **non-production TEST backend** overHTTPS via secure environmentvariables. Preserve theexistingYarn1.22.22/lockfile conventions. In theisolatedfrontend,run`COMEIN_BUILD_ENV=test EXPO_PUBLIC_BACKEND_URL="$COMEIN_TEST_BACKEND_HTTPS_URL" node node_modules/expo/bin/cli run:android --variant debug --device`. This commandis a futureprocedure,not executed evidence. If using a customExpo developmentclient,its dependency/configuration mustbe approved/provisioned separately;ExpoGo isinsufficient.
3. Capture Gradle command/version,fullnativebuildlog,APKhash,sourcehashes,effectiveAndroidmanifest/permissions/networkconfig,autolink output,`adb devices -l` anddevice/OSdetails. Install/launch only theauthorizeddebugbuild,then capturebounded`adb logcat` filteredtoappPID,withnosensitiveinputs.
4. OnanauthorizedmacOS/Xcode/CocoaPodshost,prepare thesameisolatedsourcecopy andsecureTESTbackendbinding. Run`COMEIN_BUILD_ENV=test EXPO_PUBLIC_BACKEND_URL="$COMEIN_TEST_BACKEND_HTTPS_URL" node node_modules/expo/bin/cli run:ios --configuration Debug --device`. Simulator testing doesnotreplacephysicaliPhonetesting. Anydevice-specificdebugsigningrequiresitsauthorizeddeveloperconfiguration;nofakecertificates orproductiondistribution.
5. Capture Xcode/CocoaPodversions,resolvedPodfile.lock,app/buildhashes,buildlog,finalInfo.plist,simulator/deviceidentity andredactedcrash/consolelogs.
6. Executeapp launch/login/logout/permissions/navigation/CHAND/Grocery/Restaurantcart-checkout flows onbothplatforms. With genuineapprovedRazorpayTESTresources,verify success,failure,cancel,background/resume,networkinterruption,duplicatecallback,delayedcapture andreturnnavigation. Checkserverstate,notfrontendmessages alone. PreserveuserpoliciesandUI. Recordexactplatform/source/providerreferences withoutsecrets.

Closure requires successfulcompileddebugbinaries **and** requiredruntime/devicecaseevidence. CurrentAndroid/iOSbuilds anddevicevalidation remainBLOCKED;no successfulnativebuild/devicevalidation isclaimed.
'''
(OUT/'ANDROID_IOS_NATIVE_VALIDATION_REPORT.md').write_text(native)

payment='# Razorpay TEST Payment / Refund Validation Report\n\n'+common
payment+='## Current provider gate\n\n**Actual Razorpay TEST payment,webhook andrefund validation:BLOCKED.** No provider calls were made. No mock/local test is represented as genuineprovider evidence.\n\n'
payment+=table(['ID','Validation','Status','Evidence / blocker'],[[c['id'],c['validation'],c['status'],c['scope']] for c in provider_checks])
payment+='\n## Fresh configuration presence evidence\n\nThe current process has no nonemptyRAZORPAY_MODE/KEY_ID/KEY_SECRET/WEBHOOK_SECRET bindings. A presence-only read of theexistinglocalbackend.env foundKEY_ID,KEY_SECRET andWEBHOOK_SECRET declaredbutempty,andnoRAZORPAY_MODE declaration. Values were not emitted or copied. Frontend.env contains no Razorpay secretbindings. A template orSDKexample is not an issuedtestcredential andwasnotused. The configuredtestaccount,keypair,webhooksecret,ownedHTTPSdeliveryendpoint andsettlement records required for actualvalidation are unavailable. No provider networkprobe was necessary orperformed oncecredentialabsence wasestablished;network reachability is NOT RUN inthisworkstream.\n\n'
payment+='## Existing architecture and both modes\n\n'+table(['Control / flow','Source reference','What source declares','Verification boundary'],matrix)
payment+='\nThe native andwebadapters sharebackendintentcreationandverification viaGroceryOnlinePayment(kind). Callbackdata doesnotdirectlymarktheorderpaid;thecomponentwaitsforserververifiedresponse andrefreshesonAppStateactive. Servercalls toprovider are outsideDB-onlytransactioncallbacks. EventIDs,payloadhashchecks anduniqueindexdeclarations support retry-safedesign;onlyexecutedtests/actualdelivery can establish behavior under specificraces. The broad regression workstream owns local/mock payment/refund tests;those results mustremain labeledoffline/mock/local andcannotclose theactualprovider gate. This workstreamranzero paymentmocktests toavoidduplicating that evidence.\n\n'
payment+='## Pending genuine TEST procedure — no live payments/refunds\n\n'
payment+='''1. The provider/developer custodian securely binds officialissuedTESTcredentials and webhooksecret to an isolatedbackend/testDB (neverchat,source,fixture orreport). Set`APP_ENV=test` and`RAZORPAY_MODE=test`;theKEY_ID must be anissued`rzp_test_` key. KeepKEY_SECRET andWEBHOOK_SECRET server-only. NeverloadLIVEcredentials. Useexisting.env.example variable names andfailclosedvalidation;do notfallbackbetweenmodes.
2. Prepare theauthorizedTESTuser/shop/Restaurantproducts andsource-boundisolatedDB. Capture testsource/environment/commands andpublicconfigurationflags withoutsecretvalues. ConfigureanownedreachableHTTPSwebhook for`/api/restaurant/payments/razorpay-webhook`;thisexistingroute handlesbothorderkinds. SetproviderTESTevents`payment.captured`,`payment.failed`,`refund.processed`,`refund.failed` andretainproviderdeliveryIDs/timestamps.
3. Through theexistingGrocerycustomerflow,createanonlineorder andrequest`POST /api/orders/{order_id}/payment-intent`. ThroughRestaurantflow,request`POST /api/restaurant/orders/{order_id}/payment-intent`. Recordserver-authoritativeamount/INR/providerorderID/orderownership. Repeatsmustnotcreateuncontrolledduplicateintents. UseonlyofficialTESTCheckoutscenariosonwebandnativeauthorizedbuilds;neverusegenuinecustomerpaymentdetails.
4. Submitprovider-returnedcallbackvia`POST /api/grocery/payments/verify` or`POST /api/restaurant/payments/verify`. RetainredactedHTTPstatus/response andproviderTESTpaymententity IDs/status/amount/currency/orderlinks. ConfirmserverGETtoRazorpaycapturedstatus andatomicorder/paymentstate beforeclaimingpaid. Testfailure,pending,cancel,interruptedUI,duplicatecallback,invalidsignature,amount/currency/order mismatch,delayedcapture andlatecaptureaftercancellation. No frontend-onlysuccessqualifies.
5. Delivergenuineprovidersignedwebhooks;retainproviderdeliveryrecords,rawbodyhash,eventID andapplicationauditstate withoutsharedsecrets. Verifycaptured/failed/refundevents,duplicateanddelayed/out-of-orderdelivery,retryaftertemporaryDBfailure,unknown/invalidpayload,invalidsignature andeventID/bodyidentityconflicts inisolatedresources. LocallycreatedHMACrequests areseparate simulatedevidence,not realproviderdelivery.
6. ForaneligiblegenuineTESTcaptureonly,anapprovedadminuses`POST /api/admin/grocery/orders/{order_id}/refund` (request_id,reason,optionalamount_paise peractualschema) or`POST /api/admin/restaurant/orders/{order_id}/refund`. Followexistingfull-eligible-refundpolicy;Grocerypartialreturns/eligibilitymustnotbeinvented. Verifyproviderhistorybeforerefund,state transitions,duplicate/adminauthorization,same-paymentbounds,pending/failure/timeoutreconciliation,signedrefundwebhooks andeventualTESTproviderstatus. CODordersmustneverinvokeRazorpayrefunds. Do notresubmituncertainrefunds untilproviderreconciliation;neverinitiateactualcustomerrefunds.
7. Recordprovider-issuedTESTorder/payment/refund/eventIDs withtimestamps,platform/source/buildhashes,commands,redactedlogs,isolatedDBbefore/afterstate andfinalreconciliation. Separatelocal/mockedcases,genuineTESTtransactions,genuinedelivery andphysicaldeviceresults. Neverclaimactualbanksettlement frommock orTESTsimulation;documentproviderTESTstatussemantics andanyremainingrealproductionoperationalreview separately.

The requiredexternalaction belongs to theproviderintegrationcustodian/owner/native-developer. No credentialrequestinchat,installation,externalconfiguration,payment/refundrequest orproductionoperation was performed by thisaudit. No sourcefix isauthorized ormade.
'''
(OUT/'RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md').write_text(payment)
print(json.dumps({'native_checks':len(native_checks),'provider_checks':len(provider_checks),'metadata_commands':3,
 'actual_native_builds':0,'actual_device_tests':0,'provider_calls':0,'native_status':'BLOCKED','actual_provider_status':'BLOCKED'}))
