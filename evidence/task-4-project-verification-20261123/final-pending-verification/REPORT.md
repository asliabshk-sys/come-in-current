# Task 4 final pending-work verification — 23 November 2026 IST

Verified starting state: `asliabshk-sys/come-in-current`, branch `work`, local HEAD and fetched/advertised remote `f32bf68e3691865c8be9fb9cdf7b709d1d690d27`, clean tree and 0/0 ahead/behind. Continued from the previously restored source with its public templates.

## Corrected local defects

- Advertisement poster URLs were returned but the generic download route checked only general file records. The same route now resolves the current campaign poster. Before publication, only the seller who owns the campaign and administrators can fetch it. Anonymous delivery requires an active approved campaign and matching approval hash. Replacement or removal hides old references. The response rechecks the served bytes against the campaign hash.
- Poster replacement, CHAND review and owner publication now compare campaign state and poster identity when saving. A review that becomes stale during replacement returns a conflict, and an owner can publish only the poster covered by the completed safe recommendation. Existing pending recommendations without a recorded hash need re-review. CHAND remains advisory and metadata-only.
- The current storage adapter maps provider failures and invalid object references to controlled HTTP errors. It retains the single stale-key retry. General file upload/retrieval uses the existing access and soft-deletion model. The local integration test exercises the real API and Mongo layer with an in-process storage fixture. No provider was added. The adapter has no physical deletion operation.

Apply `patches/task4-storage-advertisement-verification.patch` after the public-template restoration patch. Forward and reverse checks passed. No UI, theme, navigation, approved task scope or payment/refund policy was changed.

## Fresh verification and exact invocations

Backend ran with `APP_ENV=test`, disposable loopback Mongo replica-set database, local fixture accounts, and `COMEIN_RUN_LOCAL_PAYMENT_TESTS=1`. FastAPI was served at 127.0.0.1:18330. No external payment, storage, AI or production request was used for the new integration and browser fixtures.

| Suite | Command | Result |
|---|---|---|
| Full backend | `python -m pytest -q -n 0 --tb=short -rs`, preview runtime and batch runtime first, then sorted remaining `test_*.py` and `backend_test.py` | **686 passed, 0 failed, 5 skipped**. [Log](full-backend.log) |
| Changed-module focused | `python -m pytest -q -n 0 --tb=short` on `test_task4_storage_advertisement_integration.py`, `test_phase2_advertisement_contract.py`, `test_image_upload_type_boundary.py`, `test_upload_allocation_bound.py`, `test_chand_shopping_integration_contract.py` | **32 passed**. [Log](focused.log) |
| Payment, membership, refund, CHAND and catalog contracts | `python -m pytest -q -n 0 --tb=short` on `test_{premium_membership_integration,membership_refund_policy,payment_webhook_local_integration,grocery_refund_local_integration,restaurant_refund_webhook_transaction_offline,payment_environment_boundary,webhook_envelope_security,chand_media_contract,chand_localization_contract,shopping_catalog_contract}.py` | **61 passed**. [Log](payments.log) |
| Optional parser | With separately installed optional parser dependencies, `python -m pytest -q -n 0 -rs --tb=short backend/tests/test_universal_catalogue_import_engine.py` | **21 passed**, including the four parser cases skipped in the full run. [Log](catalogue.log) |
| Source and build | `python -m compileall -q backend scripts`; from frontend `tsc --noEmit`, targeted `eslint --max-warnings 0` for Search, CHAND, seller ads/membership and admin membership/shared checkout components, `expo config --type public`, `expo export --platform web`, native mock and planner scripts | All passed. 205 literal API pairs, zero duplicate pairs, no customer transcription or Expo Audio restoration. Five native adapter mocks and 11 planner assertions passed. [Frontend](frontend.log) · [Source](source-contracts.log) |
| Chromium | `python` on Task 4 `test-checkout-browser.py` with local fixture origins, prior refund browser harness with local origin substitutions, and local FastAPI/Chromium discovery and role smoke suite | Three mocked checkout flows, two refund fixture flows and five local API checks passed. [Payments](payment-browser.log) · [Refund](refund-browser.log) · [Local API](runtime-browser.log) |

The remaining skip, `backend/tests/backend_test.py::test_image_upload`, requires the external Emergent storage binding. With no authorized binding, startup reports uploads disabled and the external path returns HTTP 503. A successful local mock is recorded separately. [Startup](server.log)

[Exact pending and external dispositions](PENDING_ITEMS.md) cover native devices, genuine Razorpay, production, policy/legal review, and separate module scope. Task 3 remains complete, approved and closed. This project-wide verification does not close canonical Task 4 — Categories and Catalog. Production rollout remains blocked.
