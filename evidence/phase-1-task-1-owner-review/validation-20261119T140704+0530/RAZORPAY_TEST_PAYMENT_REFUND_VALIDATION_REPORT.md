# Razorpay TEST Payment / Refund Validation Report

Project: COME-IN. Current audit time: 2026-11-19T14:14:11.601290+05:30 (Asia/Kolkata). Repository `/workspace/come-in-current`,branch `work`,HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a` (root verified). Application extraction `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115` is outsideGit andcontains inherited uncommitted work;the HEAD alone doesnot identify these source bytes. Source hashes and prior-input hashes are in [native-provider-validation.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/native-provider-validation.json>).

This workstream changed only NEW iteration evidence/reports. No source,configuration,environment,dependency,originalreport,checkpoint,ZIP or Git history changes. No native project generation,packageinstall,productionoperation,provider call,payment orrefund. Existing prior inventory was reused;179API/60model inventory was not regenerated. The previous27-entry manifest remains untouched. No Task2 started.

## Current provider gate

**Actual Razorpay TEST payment,webhook andrefund validation:BLOCKED.** No provider calls were made. No mock/local test is represented as genuineprovider evidence.

| ID | Validation | Status | Evidence / blocker |
| --- | --- | --- | --- |
| PROVIDER-01 | Current TEST binding presence inspection | PASS | Presence-only inspection succeeded;allthree backend key/secret values empty andmodeabsent. Not payment verification. |
| PROVIDER-02 | Actual Razorpay TEST payment order creation | BLOCKED | No explicitly configured nonempty TEST keypair/mode or authorized TEST account. |
| PROVIDER-03 | Actual TEST checkout success/failure/pending/reconciliation | BLOCKED | Missing TEST account/credentials/native/web checkout interaction and source-bound provider records. |
| PROVIDER-04 | Actual provider webhook delivery/duplicate/retry validation | BLOCKED | No configured webhook secret,owned reachable HTTPS TEST endpoint or provider delivery records. |
| PROVIDER-05 | Actual TEST refund creation/status/duplicate/refund webhook | BLOCKED | No eligible genuine TEST captured payment/provider account or refund/delivery evidence. |
| PROVIDER-06 | Actual provider payment/refund database consistency | BLOCKED | No genuine provider event/transaction records to reconcile against isolated appDB. |

## Fresh configuration presence evidence

The current process has no nonemptyRAZORPAY_MODE/KEY_ID/KEY_SECRET/WEBHOOK_SECRET bindings. A presence-only read of theexistinglocalbackend.env foundKEY_ID,KEY_SECRET andWEBHOOK_SECRET declaredbutempty,andnoRAZORPAY_MODE declaration. Values were not emitted or copied. Frontend.env contains no Razorpay secretbindings. A template orSDKexample is not an issuedtestcredential andwasnotused. The configuredtestaccount,keypair,webhooksecret,ownedHTTPSdeliveryendpoint andsettlement records required for actualvalidation are unavailable. No provider networkprobe was necessary orperformed oncecredentialabsence wasestablished;network reachability is NOT RUN inthisworkstream.

## Existing architecture and both modes

| Control / flow | Source reference | What source declares | Verification boundary |
| --- | --- | --- | --- |
| Environment/key separation | backend/payment_config.py:14 | Explicitmode,matchingkeyprefix and production/environment consistency checks declared;no silent key-mode switch. | Source inspected;functional results belong to regression evidence. |
| Grocery server payment intent | backend/server.py:6348 | Authenticated owner scope,server order total/INR,existing-intent reuse,atomic claim anduncertain state on provider error. | No actual provider order created. |
| Restaurant server payment intent | backend/server.py:4990 | Customer ownership,pending-online eligibility,server total/INR,reuse andintentclaim. | No actual provider order created. |
| Callback verification inbothmodes | backend/server.py:5041 / 6470 | HMAC check andprovider GET require capturedstatus,matchingpayment/order IDs,exact amount/INR beforeDBpaidtransition. | No callback or providerGETexecuted bythis workstream. |
| Raw webhook signature andevents | backend/server.py:5362 | HMAC over raw requestbody,eventID/bodyhash duplicate check,explicitcaptured/failed/refundevents,recordafterprocessing. | Genuine delivery/retries remainBLOCKED;upstream requestsize limit stillunverified. |
| Grocery refund | backend/server.py:6254;backend/refund_rules.py:22 | Admin-only,verifiedcaptured online/cancelled eligibility,full amount only,requestID duplicateprotection,transactional claim,providerhistorycheck anduncertain/reconciliation states. | CODdoesnotenterproviderrefund;partial policy notinvented or changed. |
| Restaurant refund | backend/server.py:5670 | Admin dependency,verifiedpaidlinkedpayment,eligibleamount consistency,transactional claim,providerhistorychecks andpending/uncertain/finalstateguard. | Existingfullrefundbehaviorretained;actualprovideracceptance/settlement unverified. |
| Native checkout and lifecycle | frontend/src/lib/razorpay-checkout.native.ts:5;frontend/src/components/GroceryOnlinePayment.tsx:16 | Runtime nativemoduleguard,SDK.open,duplicate-windowguard,cancellationmessages;sharedcomponentrefreshesonAppStateactive andasksbackendtoverifycallback. | Source/metadata only;Android/iOSinterruption,returnnavigation,crashesandSDKcallbackbehavior notexercised. |
| Web checkout | frontend/src/lib/razorpay-checkout.ts:4 | Official checkoutscript URL,successcallback,dismiss/failurehandling;backendremainsauthoritative. | No web providerpayment or checkoutscriptrequest made. |

The native andwebadapters sharebackendintentcreationandverification viaGroceryOnlinePayment(kind). Callbackdata doesnotdirectlymarktheorderpaid;thecomponentwaitsforserververifiedresponse andrefreshesonAppStateactive. Servercalls toprovider are outsideDB-onlytransactioncallbacks. EventIDs,payloadhashchecks anduniqueindexdeclarations support retry-safedesign;onlyexecutedtests/actualdelivery can establish behavior under specificraces. The broad regression workstream owns local/mock payment/refund tests;those results mustremain labeledoffline/mock/local andcannotclose theactualprovider gate. This workstreamranzero paymentmocktests toavoidduplicating that evidence.

## Pending genuine TEST procedure — no live payments/refunds

1. The provider/developer custodian securely binds officialissuedTESTcredentials and webhooksecret to an isolatedbackend/testDB (neverchat,source,fixture orreport). Set`APP_ENV=test` and`RAZORPAY_MODE=test`;theKEY_ID must be anissued`rzp_test_` key. KeepKEY_SECRET andWEBHOOK_SECRET server-only. NeverloadLIVEcredentials. Useexisting.env.example variable names andfailclosedvalidation;do notfallbackbetweenmodes.
2. Prepare theauthorizedTESTuser/shop/Restaurantproducts andsource-boundisolatedDB. Capture testsource/environment/commands andpublicconfigurationflags withoutsecretvalues. ConfigureanownedreachableHTTPSwebhook for`/api/restaurant/payments/razorpay-webhook`;thisexistingroute handlesbothorderkinds. SetproviderTESTevents`payment.captured`,`payment.failed`,`refund.processed`,`refund.failed` andretainproviderdeliveryIDs/timestamps.
3. Through theexistingGrocerycustomerflow,createanonlineorder andrequest`POST /api/orders/{order_id}/payment-intent`. ThroughRestaurantflow,request`POST /api/restaurant/orders/{order_id}/payment-intent`. Recordserver-authoritativeamount/INR/providerorderID/orderownership. Repeatsmustnotcreateuncontrolledduplicateintents. UseonlyofficialTESTCheckoutscenariosonwebandnativeauthorizedbuilds;neverusegenuinecustomerpaymentdetails.
4. Submitprovider-returnedcallbackvia`POST /api/grocery/payments/verify` or`POST /api/restaurant/payments/verify`. RetainredactedHTTPstatus/response andproviderTESTpaymententity IDs/status/amount/currency/orderlinks. ConfirmserverGETtoRazorpaycapturedstatus andatomicorder/paymentstate beforeclaimingpaid. Testfailure,pending,cancel,interruptedUI,duplicatecallback,invalidsignature,amount/currency/order mismatch,delayedcapture andlatecaptureaftercancellation. No frontend-onlysuccessqualifies.
5. Delivergenuineprovidersignedwebhooks;retainproviderdeliveryrecords,rawbodyhash,eventID andapplicationauditstate withoutsharedsecrets. Verifycaptured/failed/refundevents,duplicateanddelayed/out-of-orderdelivery,retryaftertemporaryDBfailure,unknown/invalidpayload,invalidsignature andeventID/bodyidentityconflicts inisolatedresources. LocallycreatedHMACrequests areseparate simulatedevidence,not realproviderdelivery.
6. ForaneligiblegenuineTESTcaptureonly,anapprovedadminuses`POST /api/admin/grocery/orders/{order_id}/refund` (request_id,reason,optionalamount_paise peractualschema) or`POST /api/admin/restaurant/orders/{order_id}/refund`. Followexistingfull-eligible-refundpolicy;Grocerypartialreturns/eligibilitymustnotbeinvented. Verifyproviderhistorybeforerefund,state transitions,duplicate/adminauthorization,same-paymentbounds,pending/failure/timeoutreconciliation,signedrefundwebhooks andeventualTESTproviderstatus. CODordersmustneverinvokeRazorpayrefunds. Do notresubmituncertainrefunds untilproviderreconciliation;neverinitiateactualcustomerrefunds.
7. Recordprovider-issuedTESTorder/payment/refund/eventIDs withtimestamps,platform/source/buildhashes,commands,redactedlogs,isolatedDBbefore/afterstate andfinalreconciliation. Separatelocal/mockedcases,genuineTESTtransactions,genuinedelivery andphysicaldeviceresults. Neverclaimactualbanksettlement frommock orTESTsimulation;documentproviderTESTstatussemantics andanyremainingrealproductionoperationalreview separately.

The requiredexternalaction belongs to theproviderintegrationcustodian/owner/native-developer. No credentialrequestinchat,installation,externalconfiguration,payment/refundrequest orproductionoperation was performed by thisaudit. No sourcefix isauthorized ormade.
