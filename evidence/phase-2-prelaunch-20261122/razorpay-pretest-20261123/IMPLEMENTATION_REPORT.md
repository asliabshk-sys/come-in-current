# Razorpay local pre-test milestone — 23 November 2026 (IST)

Base: `work` at `ee627805b7f0c102f935315c242a11884a61a4fb`. The application was reconstructed from the November 22 sanitized archive and the tracked Task 3, Phase 2 foundation and Premium completion patches. Apply `patches/razorpay-pretest.patch` last. Forward and reverse dry runs passed. No earlier patch, archive or evidence was replaced.

## Changes

- Grocery and Restaurant callback verification checks the signature even on the paid/idempotent path. A rejected callback makes no change to the payment record, including during a concurrent valid capture. Non-ASCII signatures are rejected and signature/identifier lengths are bounded. The signed webhook also rejects non-ASCII signatures before comparison.
- Grocery and Restaurant callbacks use the existing captured-payment association validator. It requires matching order and payment associations, INR, captured state and the exact integer amount against the persisted order. The order creation response validator is shared by Grocery, Restaurant and Membership. New intents claim only orders that still await the correct payment state. Existing order amounts are unchanged. ₹299 remains specific to Membership.
- The shared Grocery/Restaurant payment UI serializes Pay and Cancel and checks that the verification response identifies the same paid order. Seller Membership serializes request and payment taps, requires the confirmed record to match its intent and refreshes after an interrupted verification. Existing activation, renewal, exposure, advertisement and CHAND behavior was preserved.
- Source delta covers `backend/server.py`, four backend regression files (three source contracts and the local HTTP harness), `frontend/src/components/GroceryOnlinePayment.tsx`, and the seller membership route. Existing endpoints, Mongo collections, transaction code and refund policy were reused. No dependency or migration was added.

## Verification layers

1. **Automated contracts and units.** Existing source contracts now follow the shared validation boundary. Coverage includes transaction retry, test/live configuration boundaries, strict webhook envelopes, callback security and refund rules.
2. **Mock gateway and frontend.** Razorpay calls returned deterministic in-process payloads or timeouts. The Chromium test intercepts application API requests and supplies a fake Checkout SDK. All three flows exercised dismissal, decline, same-tick Pay taps, duplicate SDK callbacks, failed server verification, retry and a confirmed server response. The native adapter mock suite also ran.
3. **Local integration.** Existing HTTP webhook/refund and membership tests ran on a loopback disposable MongoDB 7 replica set. The HTTP harness adds authenticated Grocery and Restaurant verification, cross-account rejection, missing/malformed/altered signatures, amount/currency/association mismatches, authorized/failed captures, timeouts, concurrent callbacks and one persisted payment/order transition. Existing local tests cover signed duplicate delivery, replay, out-of-order events, late capture/refund review, Grocery/Restaurant refund authorization and reconciliation, and Membership purchase, activation and state transitions.
4. **Genuine Razorpay TEST gateway and production.** Deferred. No Razorpay network request, real transaction, refund, webhook delivery or settlement occurred. The project has no implemented Membership refund policy. A business decision is needed before adding one.

## Commands

Use a disposable app database with `APP_ENV=test`, loopback MongoDB and synthetic auth/test configuration. Use the existing browser and backend test dependencies. Start the local FastAPI app, set the preview/test base URL to its loopback origin, and seed synthetic preview accounts with `backend/tests/seed_preview_test_accounts.py`. Keep local configuration out of Git.

- Focused command: `python -m pytest -q -n 0 --tb=short` over `test_payment_webhook_local_integration.py`, `test_grocery_refund_local_integration.py`, `test_premium_membership_integration.py`, `test_payment_environment_boundary.py`, `test_webhook_envelope_security.py`, `test_final_payment_transition_races.py`, `test_transaction_commit_retry.py`, `test_restaurant_refund_webhook_transaction_offline.py`, `test_step1_final_refund_admin_offline.py`, `test_functional_blockers_regression.py`, `test_shared_system_integration_contract.py`, and `test_task10_payment_refund_notification_contract.py` under `backend/tests`. Enable the existing `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1` opt-in.
- Full command: `python -m pytest -q -n 0 --tb=short -rs`, with `backend/tests/test_preview_runtime_e2e.py` and `backend/tests/test_batch_5task_runtime.py` first, then the sorted `test_*.py` and `backend_test.py` files excluding those first two. Serial order preserves the legacy fixtures' shared state.
- Frontend commands from `frontend/`: `tsc --noEmit`, targeted `eslint src/components/GroceryOnlinePayment.tsx app/seller/membership.tsx`, `node scripts/test-native-payment.cjs`, and `expo export --platform web`. Build with a loopback fixture API URL. Serve the export locally with SPA fallback and run [browser-checkout.py](browser-checkout.py) using Playwright and Chromium. It intercepts the fixture API and blocks external HTTPS requests.

## Deferred final phase

Each row is **DEFERRED — REQUIRES AUTHORIZED EXTERNAL TEST ENVIRONMENT**.

| Validation | Required access or configuration |
|---|---|
| Genuine Razorpay TEST payment | Authorized Razorpay TEST account, TEST key ID/secret, test-mode isolated backend and permitted gateway access. Only key ID goes to the client. |
| Genuine Razorpay TEST webhook delivery | Razorpay TEST dashboard, reachable HTTPS webhook URL, TEST webhook signing secret and appropriate event subscriptions. |
| Genuine Razorpay TEST refund | Authorized TEST dashboard/API access and a captured TEST transaction eligible for refund. |
| Production payment transaction | Approved production environment, authorized production credentials in secure configuration, approved transaction and release controls. |
| Real settlement | Approved live transaction and reconciliation access to settlement reports and the authorized finance account. |
| Production webhook configuration | Authorized production dashboard, verified HTTPS ingress, securely configured production webhook secret and event subscriptions. |
| Android payment acceptance | Signed development build with native Razorpay module, compatible physical Android device and authorized TEST gateway setup. |
| iOS payment acceptance | Signed development build, Apple provisioning access, compatible physical iOS device and authorized TEST gateway setup. |
| Production rollout and live customer acceptance | Release authorization, production configuration, monitoring, rollback plan and verified support/reconciliation procedures. |

## Final results

| Evidence | Result |
|---|---|
| [Focused backend](focused-backend.log) | 94 passed, zero failed, zero skipped |
| [Full backend](full-backend-regression.log) | 683 passed, zero failed, five skipped |
| [Browser Checkout mocks](mock-browser.log) | Grocery, Restaurant and Membership passed |
| [Frontend and restoration](frontend.log) | TypeScript, targeted ESLint, five mocked native checks, Expo web export and patch restoration passed |

The full suite skipped one object-storage check because storage was unavailable and four unrelated catalogue-import checks because optional PDF, spreadsheet and imaging libraries were absent. The initial full run found four source contracts that expected validation inline or the old UI success condition. Those assertions were updated to check the shared validator and the stricter success condition, and the final suite passed. The Git commit introducing this report is the verified milestone.
