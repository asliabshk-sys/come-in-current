# Test Provenance and Reproduction Report

Project: COME-IN. Recorded 2026-11-19T21:25:29.696010+05:30 (Asia/Kolkata). **REVIEW PENDING.** This provenance workstream executed no tests, database queries, network calls or source/configuration changes. It independently read all39 historical XML artifacts and39 matching logs, then reconciled actual finalized fresh receipts from the designated validation agents. Existing reports/checkpoints remain preserved.

## Recovered source identity and preservation

Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`. The application is the extracted, locally changed tree at `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`. **The repository HEAD does not identify that outside-Git application.** Current per-file input hashes and explicit source/runtime receipts bind this validation.

Read all six latest final reports, `ITERATION_CHECKPOINT.md` and the20-gap ledger from `iteration-2026-11-18T072632-0800` before continuing. Baselines are distinct:8150old audit paths,8476initial owner review,8504next review,8533current validation. The old8150map contains8128app+20root+2patch paths and no root/evidence files. The additional326/28/29paths belong to later captures. Actual secret `.env` files, dependency trees, Git internals and selected caches/uploads are excluded. Current hashes cannot establish past excluded-file integrity.

The current captured app subset contains8128files. Canonical captured path→SHA256 map fingerprint: `0a5b35edec8b855ab065e045cda15d3dcd43ccdf098c05a522025e1606bd31d8`. Method:SHA256 of sorted compact JSON using app-relative paths and captured hashes from [preservation-baseline.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/preservation-baseline.json>). This is a present capture, never an original17/18Nov execution attestation.

## Historical evidence boundary

All39 XML/log pairs were fully read. Their currently observed hashes still match this workstream's initial capture; suite attributes match the old audit index. Ten XMLs contain failures and one contains zero cases. **Zero cases is not a successful test run.** Repeated selections overlap; do not sum historical rows as unique coverage. XML timestamps/hostnames are self-reported stored fields rather than trusted process attestations.

None of39matching logs records the exact original pytest invocation. Candidate command documents/runners are identified per artifact below; their current existence does not establish the exact original process, source, network target or environment. Original per-run source content hashes and complete execution/isolation receipts remain missing. Current XML/log hashes are not backdated.

## Complete39-artifact result index

T=actualtestcasecount;P=nonfailed/nonerrored/nonskipped;F=failure;E=error;S=skip. AllrowsareHISTORICAL,notfreshresults.

| # | Artifact | Suite timestamp | T/P/F/E/S | Matching log | Available command evidence |
|---:|---|---|---|---|---|
| 1 | [session-20261117/frontend-group-regression.xml](/workspace/come-in-current/evidence/session-20261117/frontend-group-regression.xml) | 2026-11-17T08:49:58.304638+00:00 | 63/63/0/0/0 | [frontend-group-regression.log](/workspace/come-in-current/evidence/session-20261117/frontend-group-regression.log) | exact invocation NOT FOUND |
| 2 | [session-20261117/transaction-regression.xml](/workspace/come-in-current/evidence/session-20261117/transaction-regression.xml) | 2026-11-17T08:44:44.935425+00:00 | 52/51/1/0/0 | [transaction-regression.log](/workspace/come-in-current/evidence/session-20261117/transaction-regression.log) | exact invocation NOT FOUND |
| 3 | [session-20261117/release-offline.xml](/workspace/come-in-current/evidence/session-20261117/release-offline.xml) | 2026-11-17T09:00:25.345305+00:00 | 505/496/5/0/4 | [release-offline.log](/workspace/come-in-current/evidence/session-20261117/release-offline.log) | exact invocation NOT FOUND |
| 4 | [session-20261117/frontend-effects-regression.xml](/workspace/come-in-current/evidence/session-20261117/frontend-effects-regression.xml) | 2026-11-17T08:58:28.605813+00:00 | 107/107/0/0/0 | [frontend-effects-regression.log](/workspace/come-in-current/evidence/session-20261117/frontend-effects-regression.log) | exact invocation NOT FOUND |
| 5 | [session-20261117/seller-support-contract-final.xml](/workspace/come-in-current/evidence/session-20261117/seller-support-contract-final.xml) | 2026-11-17T09:05:04.600192+00:00 | 5/5/0/0/0 | [seller-support-contract-final.log](/workspace/come-in-current/evidence/session-20261117/seller-support-contract-final.log) | exact invocation NOT FOUND |
| 6 | [session-20261117/state-group-regression.xml](/workspace/come-in-current/evidence/session-20261117/state-group-regression.xml) | 2026-11-17T08:53:01.253335+00:00 | 45/45/0/0/0 | [state-group-regression.log](/workspace/come-in-current/evidence/session-20261117/state-group-regression.log) | exact invocation NOT FOUND |
| 7 | [session-20261117/live-after-fix.xml](/workspace/come-in-current/evidence/session-20261117/live-after-fix.xml) | 2026-11-17T08:46:06.225606+00:00 | 70/70/0/0/0 | [live-after-fix.log](/workspace/come-in-current/evidence/session-20261117/live-after-fix.log) | exact invocation NOT FOUND |
| 8 | [session-20261117/release-offline-final.xml](/workspace/come-in-current/evidence/session-20261117/release-offline-final.xml) | 2026-11-17T09:03:00.046180+00:00 | 505/497/4/0/4 | [release-offline-final.log](/workspace/come-in-current/evidence/session-20261117/release-offline-final.log) | exact invocation NOT FOUND |
| 9 | [session-20261117/transaction-regression-v2.xml](/workspace/come-in-current/evidence/session-20261117/transaction-regression-v2.xml) | 2026-11-17T08:45:09.556386+00:00 | 52/52/0/0/0 | [transaction-regression-v2.log](/workspace/come-in-current/evidence/session-20261117/transaction-regression-v2.log) | exact invocation NOT FOUND |
| 10 | [session-20261117/remaining-runtime.xml](/workspace/come-in-current/evidence/session-20261117/remaining-runtime.xml) | 2026-11-17T08:34:11.054102+00:00 | 61/61/0/0/0 | [remaining-runtime.log](/workspace/come-in-current/evidence/session-20261117/remaining-runtime.log) | exact invocation NOT FOUND |
| 11 | [session-20261117/auth-contract-correction.xml](/workspace/come-in-current/evidence/session-20261117/auth-contract-correction.xml) | 2026-11-17T09:01:56.741822+00:00 | 9/9/0/0/0 | [auth-contract-correction.log](/workspace/come-in-current/evidence/session-20261117/auth-contract-correction.log) | exact invocation NOT FOUND |
| 12 | [release-completion-20261117T094751Z/step3-tests.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step3-tests.xml) | 2026-11-17T09:54:32.373710+00:00 | 30/30/0/0/0 | [step3-tests.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step3-tests.log) | exact invocation NOT FOUND |
| 13 | [release-completion-20261117T094751Z/step9-payment-v2.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment-v2.xml) | 2026-11-17T10:20:57.816035+00:00 | 78/78/0/0/0 | [step9-payment-v2.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment-v2.log) | exact invocation NOT FOUND |
| 14 | [release-completion-20261117T094751Z/step5-tests.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests.xml) | 2026-11-17T10:10:34.571365+00:00 | 0/0/0/0/0 | [step5-tests.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests.log) | exact invocation NOT FOUND |
| 15 | [release-completion-20261117T094751Z/step4-tests-v2.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests-v2.xml) | 2026-11-17T10:00:06.714995+00:00 | 48/48/0/0/0 | [step4-tests-v2.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests-v2.log) | exact invocation NOT FOUND |
| 16 | [release-completion-20261117T094751Z/step1-live.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step1-live.xml) | 2026-11-17T09:48:07.463618+00:00 | 70/70/0/0/0 | [step1-live.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step1-live.log) | runner script found |
| 17 | [release-completion-20261117T094751Z/step9-payment.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment.xml) | 2026-11-17T10:20:33.399228+00:00 | 78/76/2/0/0 | [step9-payment.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment.log) | exact invocation NOT FOUND |
| 18 | [release-completion-20261117T094751Z/step5-tests-v2.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests-v2.xml) | 2026-11-17T10:10:53.981523+00:00 | 50/50/0/0/0 | [step5-tests-v2.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests-v2.log) | exact invocation NOT FOUND |
| 19 | [release-completion-20261117T094751Z/step4-final.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-final.xml) | 2026-11-17T10:03:25.232767+00:00 | 62/62/0/0/0 | [step4-final.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-final.log) | exact invocation NOT FOUND |
| 20 | [release-completion-20261117T094751Z/step4-tests.xml](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests.xml) | 2026-11-17T09:59:30.429540+00:00 | 48/47/1/0/0 | [step4-tests.log](/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests.log) | exact invocation NOT FOUND |
| 21 | [regression-fixes-20261117T091345Z/three-failures-after.xml](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-after.xml) | 2026-11-17T09:15:24.609966+00:00 | 3/3/0/0/0 | [three-failures-after.log](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-after.log) | exact invocation NOT FOUND |
| 22 | [regression-fixes-20261117T091345Z/csv-focused.xml](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/csv-focused.xml) | 2026-11-17T09:14:24.008321+00:00 | 8/8/0/0/0 | [csv-focused.log](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/csv-focused.log) | exact invocation NOT FOUND |
| 23 | [regression-fixes-20261117T091345Z/three-failures-before.xml](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-before.xml) | 2026-11-17T09:13:46.165158+00:00 | 3/0/3/0/0 | [three-failures-before.log](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-before.log) | exact invocation NOT FOUND |
| 24 | [regression-fixes-20261117T091345Z/relevant-regression.xml](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/relevant-regression.xml) | 2026-11-17T09:17:07.795784+00:00 | 96/92/0/0/4 | [relevant-regression.log](/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/relevant-regression.log) | exact invocation NOT FOUND |
| 25 | [external-validation-20261118T133459Z/upload-types-before.xml](/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-types-before.xml) | 2026-11-18T13:36:52.433912+00:00 | 8/0/8/0/0 | [upload-types-before.log](/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-types-before.log) | historical command documentation found |
| 26 | [external-validation-20261118T133459Z/upload-security-after.xml](/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-security-after.xml) | 2026-11-18T13:37:38.548339+00:00 | 25/25/0/0/0 | [upload-security-after.log](/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-security-after.log) | historical command documentation found |
| 27 | [resume-20261118/security-races-before.xml](/workspace/come-in-current/evidence/resume-20261118/security-races-before.xml) | 2026-11-18T13:22:31.668987+00:00 | 4/0/4/0/0 | [security-races-before.log](/workspace/come-in-current/evidence/resume-20261118/security-races-before.log) | historical command documentation found |
| 28 | [resume-20261118/backend-final.xml](/workspace/come-in-current/evidence/resume-20261118/backend-final.xml) | 2026-11-18T13:23:45.698295+00:00 | 564/557/1/0/6 | [backend-final.log](/workspace/come-in-current/evidence/resume-20261118/backend-final.log) | historical command documentation found |
| 29 | [resume-20261118/payment-local.xml](/workspace/come-in-current/evidence/resume-20261118/payment-local.xml) | 2026-11-18T13:20:26.013737+00:00 | 78/78/0/0/0 | [payment-local.log](/workspace/come-in-current/evidence/resume-20261118/payment-local.log) | historical command documentation found |
| 30 | [resume-20261118/backend-full.xml](/workspace/come-in-current/evidence/resume-20261118/backend-full.xml) | 2026-11-18T13:18:58.261920+00:00 | 559/551/2/0/6 | [backend-full.log](/workspace/come-in-current/evidence/resume-20261118/backend-full.log) | historical command documentation found |
| 31 | [resume-20261118/contract-focused.xml](/workspace/come-in-current/evidence/resume-20261118/contract-focused.xml) | 2026-11-18T13:20:06.480649+00:00 | 24/24/0/0/0 | [contract-focused.log](/workspace/come-in-current/evidence/resume-20261118/contract-focused.log) | historical command documentation found |
| 32 | [resume-20261118/backend-final-v2.xml](/workspace/come-in-current/evidence/resume-20261118/backend-final-v2.xml) | 2026-11-18T13:25:23.275822+00:00 | 564/558/0/0/6 | [backend-final-v2.log](/workspace/come-in-current/evidence/resume-20261118/backend-final-v2.log) | historical command documentation found |
| 33 | [resume-20261118/security-races-after.xml](/workspace/come-in-current/evidence/resume-20261118/security-races-after.xml) | 2026-11-18T13:23:10.051980+00:00 | 28/28/0/0/0 | [security-races-after.log](/workspace/come-in-current/evidence/resume-20261118/security-races-after.log) | historical command documentation found |
| 34 | [resume-20261118/security-final-focused.xml](/workspace/come-in-current/evidence/resume-20261118/security-final-focused.xml) | 2026-11-18T13:23:44.317153+00:00 | 5/5/0/0/0 | [security-final-focused.log](/workspace/come-in-current/evidence/resume-20261118/security-final-focused.log) | historical command documentation found |
| 35 | [resume-20261118/security-tracking-final.xml](/workspace/come-in-current/evidence/resume-20261118/security-tracking-final.xml) | 2026-11-18T13:24:54.575700+00:00 | 17/17/0/0/0 | [security-tracking-final.log](/workspace/come-in-current/evidence/resume-20261118/security-tracking-final.log) | historical command documentation found |
| 36 | [resume-20261118/live-regression.xml](/workspace/come-in-current/evidence/resume-20261118/live-regression.xml) | 2026-11-18T13:20:25.773575+00:00 | 70/70/0/0/0 | [live-regression.log](/workspace/come-in-current/evidence/resume-20261118/live-regression.log) | runner script found |
| 37 | [resume-20261118/affected-local-final.xml](/workspace/come-in-current/evidence/resume-20261118/affected-local-final.xml) | 2026-11-18T13:25:23.245605+00:00 | 7/7/0/0/0 | [affected-local-final.log](/workspace/come-in-current/evidence/resume-20261118/affected-local-final.log) | historical command documentation found |
| 38 | [resume-20261118/live-regression-final.xml](/workspace/come-in-current/evidence/resume-20261118/live-regression-final.xml) | 2026-11-18T13:25:37.302305+00:00 | 70/70/0/0/0 | [live-regression-final.log](/workspace/come-in-current/evidence/resume-20261118/live-regression-final.log) | runner script found |
| 39 | [resume-20261118/backend-full-v2.xml](/workspace/come-in-current/evidence/resume-20261118/backend-full-v2.xml) | 2026-11-18T13:20:38.725101+00:00 | 559/553/0/0/6 | [backend-full-v2.log](/workspace/come-in-current/evidence/resume-20261118/backend-full-v2.log) | historical command documentation found |

## Per-artifact provenance,failures,skips and reproduction limits

### H01 — frontend-group-regression.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/frontend-group-regression.xml`;currentSHA256:`3659aa064aa2e98d1a07292206f42b058ecb32f86d332124428f85a09e6f60a1`.
- Log:`/workspace/come-in-current/evidence/session-20261117/frontend-group-regression.log`;currentSHA256:`42589bdf8f01eb5b98dc44eb445a763e443df6573d111c26755e21bed8dc18c7`;142bytes fullyread.
- Actual counts:T63/P63/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:49:58.304638+00:00", "hostname": "bca3ee959444", "time": "3.078"}].
- Modules:test_chand_feedback_contract, test_chand_media_contract, test_chand_shopping_integration_contract, test_delivery_tracking_contract, test_grocery_checkout_security_contract, test_master_catalog_seller_ui_contract, test_task12_customer_support_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H02 — transaction-regression.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/transaction-regression.xml`;currentSHA256:`fc702faeca5972e27918f5226b879a79fce6983db6c5f24f764f1541f6493826`.
- Log:`/workspace/come-in-current/evidence/session-20261117/transaction-regression.log`;currentSHA256:`e5f594d50c202c874e03ead95416469e7dd59fc47f5704fb6be7c4cdbe4d8d78`;5781bytes fullyread.
- Actual counts:T52/P51/F1/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:44:44.935425+00:00", "hostname": "bca3ee959444", "time": "3.733"}].
- Modules:test_catalogue_transaction_apply_offline, test_grocery_capture_transaction_offline, test_mongo_transactions, test_restaurant_capture_transaction_offline, test_restaurant_refund_webhook_transaction_offline, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_transaction_commit_retry. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw1] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_transaction_commit_retry::test_unknown_commit_retry_stops_at_transaction_budget.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H03 — release-offline.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/release-offline.xml`;currentSHA256:`140a797f97882168ba3f7e72a785510634f148013bd2ad16539a75561f2263d7`.
- Log:`/workspace/come-in-current/evidence/session-20261117/release-offline.log`;currentSHA256:`5609bb48056dfe58364e5d55e8b70e06c36bd03c33a31c99f746ab19f343dbc3`;6664bytes fullyread.
- Actual counts:T505/P496/F5/E0/S4;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:00:25.345305+00:00", "hostname": "bca3ee959444", "time": "34.803"}].
- Modules:test_assistant_context_contract, test_catalog_import_security_contract, test_catalog_reference_minimum, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_catalogue_validator_migration, test_chand_demo_contract, test_chand_feedback_contract, test_chand_localization_contract, test_chand_media_contract, test_chand_ollama_provider_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_directory_only_category_contract, test_financial_rules, test_financial_security_contract, test_frontend_contracts, test_functional_blockers_regression, test_grocery_capture_transaction_offline, test_grocery_checkout_security_contract, test_grocery_pay_at_shop_status_contract, test_home_services_remaining_contract, test_master_catalog_api_contract, test_master_catalog_seller_ui_contract, test_mongo_backup_safety_offline, test_mongo_config, test_mongo_portability_tool, test_mongo_transactions, test_online_shop_product_listing_contract, test_p0_payment_checkout_completion, test_p0_restaurant_delivery_panel, test_provider_adapter_contracts, test_referral_implementation_contract, test_referral_rules, test_restaurant_api_contract, test_restaurant_capture_transaction_offline, test_restaurant_pricing, test_restaurant_refund_webhook_transaction_offline, test_restaurant_serviceability, test_role_security_retail_import_contract, test_shared_system_integration_contract, test_shop_registration_browse_entrypoints, test_shopping_cart_variants_contract, test_shopping_catalog_contract, test_shopping_rewards_redemption_contract, test_standard_ui_image_shop_cta_contract, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_step1_final_restore_index_profile_offline, test_targeted_tasks_9_12_15_18_21, test_task10_payment_refund_notification_contract, test_task11_grocery_refund_status_contract, test_task11_live_order_tracking_contract, test_task12_customer_support_contract, test_task13_seller_support_status_contract, test_task14_seller_support_ui_contract, test_task16_production_cors_contract, test_task17_grocery_payment_gate_contract, test_task18_refund_safety_iteration3, test_task19_seller_admin_workflows_contract, test_task20_product_catalog_variants_stock_contract, test_task21_customer_shopping_workflow_contract, test_task22_checkout_audit_contract, test_task23_order_tracking_authorization_contract, test_task24_repeat_order_contract, test_task5_customer_measured_shopping_contract, test_task5_measured_import_contract, test_task5_task7_ui_implementation_contract, test_task9_order_actions_contract, test_transaction_commit_retry, test_universal_catalogue_import_engine. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw1] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw0] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_frontend_contracts::test_auth_persistence_failure_is_not_silently_accepted; tests.test_frontend_contracts::test_shopping_home_theme_contract_and_separate_mode_routes; tests.test_frontend_contracts::test_bakery_has_no_fabricated_sample_inventory_and_voice_is_honest; tests.test_shared_system_integration_contract::test_shared_logout_clears_the_same_token_and_existing_roles_remain_authoritative; tests.test_universal_catalogue_import_engine::test_csv_formula_like_cells_are_preserved_as_untrusted_source_text.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H04 — frontend-effects-regression.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/frontend-effects-regression.xml`;currentSHA256:`03c233bdd178dbfdbd31584e5085e08b63510cc74e9b87f63cc6ab00566767c4`.
- Log:`/workspace/come-in-current/evidence/session-20261117/frontend-effects-regression.log`;currentSHA256:`93bbe45923664ebe7df2d162ba804f824d6da48e7db4a8a1814e2b3f847c9856`;223bytes fullyread.
- Actual counts:T107/P107/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:58:28.605813+00:00", "hostname": "bca3ee959444", "time": "5.637"}].
- Modules:test_chand_feedback_contract, test_chand_media_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_grocery_checkout_security_contract, test_master_catalog_seller_ui_contract, test_referral_implementation_contract, test_restaurant_api_contract, test_shopping_cart_variants_contract, test_task12_customer_support_contract, test_task5_customer_measured_shopping_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H05 — seller-support-contract-final.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/seller-support-contract-final.xml`;currentSHA256:`5d5ad560bfb6792ca63411d014f015913baaf2f7a353e591d58db345bf896784`.
- Log:`/workspace/come-in-current/evidence/session-20261117/seller-support-contract-final.log`;currentSHA256:`0da81eb5221a91ae10b1d11c39b5ab799c36f4233370b45cdb1a79aacb339a21`;141bytes fullyread.
- Actual counts:T5/P5/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:05:04.600192+00:00", "hostname": "bca3ee959444", "time": "0.494"}].
- Modules:test_task14_seller_support_ui_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H06 — state-group-regression.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/state-group-regression.xml`;currentSHA256:`6853f233f83b16626f3c71bc607c0279d878c195776daf6864d1376862ff233e`.
- Log:`/workspace/come-in-current/evidence/session-20261117/state-group-regression.log`;currentSHA256:`1d3b6ccf644af6a8e53e58a5b63fac1be71f00f2f8ca0a4ab2bb9ebb51105ada`;142bytes fullyread.
- Actual counts:T45/P45/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:53:01.253335+00:00", "hostname": "bca3ee959444", "time": "1.866"}].
- Modules:test_chand_shopping_integration_contract, test_grocery_checkout_security_contract, test_shopping_cart_variants_contract, test_task5_customer_measured_shopping_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H07 — live-after-fix.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/live-after-fix.xml`;currentSHA256:`f367042785cb34f972c0ac2b36b5b4c924dcb87ac6b4e6b310ce2afb895fd32b`.
- Log:`/workspace/come-in-current/evidence/session-20261117/live-after-fix.log`;currentSHA256:`e772c9ca02d2503df2ef6a0c76be97a17e8eb8fb603b5936a76d3bac9734dfd4`;99bytes fullyread.
- Actual counts:T70/P70/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:46:06.225606+00:00", "hostname": "bca3ee959444", "time": "9.642"}].
- Modules:test_batch_5task_runtime, test_iter_notifications_admin_measured, test_preview_runtime_e2e, test_task5_live_mongo_transactions. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H08 — release-offline-final.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/release-offline-final.xml`;currentSHA256:`cee43f2fd0e14447f9959dbe0ea449a373dc67c8dea4c8cef2bd3bd6175e3e9e`.
- Log:`/workspace/come-in-current/evidence/session-20261117/release-offline-final.log`;currentSHA256:`b2b4dd07cb37ae17ac1a40158420e506db936882b396f1be46bc525766bcf1cb`;5650bytes fullyread.
- Actual counts:T505/P497/F4/E0/S4;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:03:00.046180+00:00", "hostname": "bca3ee959444", "time": "45.930"}].
- Modules:test_assistant_context_contract, test_catalog_import_security_contract, test_catalog_reference_minimum, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_catalogue_validator_migration, test_chand_demo_contract, test_chand_feedback_contract, test_chand_localization_contract, test_chand_media_contract, test_chand_ollama_provider_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_directory_only_category_contract, test_financial_rules, test_financial_security_contract, test_frontend_contracts, test_functional_blockers_regression, test_grocery_capture_transaction_offline, test_grocery_checkout_security_contract, test_grocery_pay_at_shop_status_contract, test_home_services_remaining_contract, test_master_catalog_api_contract, test_master_catalog_seller_ui_contract, test_mongo_backup_safety_offline, test_mongo_config, test_mongo_portability_tool, test_mongo_transactions, test_online_shop_product_listing_contract, test_p0_payment_checkout_completion, test_p0_restaurant_delivery_panel, test_provider_adapter_contracts, test_referral_implementation_contract, test_referral_rules, test_restaurant_api_contract, test_restaurant_capture_transaction_offline, test_restaurant_pricing, test_restaurant_refund_webhook_transaction_offline, test_restaurant_serviceability, test_role_security_retail_import_contract, test_shared_system_integration_contract, test_shop_registration_browse_entrypoints, test_shopping_cart_variants_contract, test_shopping_catalog_contract, test_shopping_rewards_redemption_contract, test_standard_ui_image_shop_cta_contract, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_step1_final_restore_index_profile_offline, test_targeted_tasks_9_12_15_18_21, test_task10_payment_refund_notification_contract, test_task11_grocery_refund_status_contract, test_task11_live_order_tracking_contract, test_task12_customer_support_contract, test_task13_seller_support_status_contract, test_task14_seller_support_ui_contract, test_task16_production_cors_contract, test_task17_grocery_payment_gate_contract, test_task18_refund_safety_iteration3, test_task19_seller_admin_workflows_contract, test_task20_product_catalog_variants_stock_contract, test_task21_customer_shopping_workflow_contract, test_task22_checkout_audit_contract, test_task23_order_tracking_authorization_contract, test_task24_repeat_order_contract, test_task5_customer_measured_shopping_contract, test_task5_measured_import_contract, test_task5_task7_ui_implementation_contract, test_task9_order_actions_contract, test_transaction_commit_retry, test_universal_catalogue_import_engine. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw0] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw1] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_frontend_contracts::test_shopping_home_theme_contract_and_separate_mode_routes; tests.test_frontend_contracts::test_bakery_has_no_fabricated_sample_inventory_and_voice_is_honest; tests.test_universal_catalogue_import_engine::test_csv_formula_like_cells_are_preserved_as_untrusted_source_text; tests.test_task14_seller_support_ui_contract::test_seller_account_navigation_exposes_support_for_shopkeeper_and_restaurant_roles.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H09 — transaction-regression-v2.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/transaction-regression-v2.xml`;currentSHA256:`5454680de27a9b8cec742eb473722a9571a085b38c9cab80ed3e51140769e4bc`.
- Log:`/workspace/come-in-current/evidence/session-20261117/transaction-regression-v2.log`;currentSHA256:`475e6c08e4d48b5ff44d1a367ee943497153dead960c5995c2ec395ac2423efc`;665bytes fullyread.
- Actual counts:T52/P52/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:45:09.556386+00:00", "hostname": "bca3ee959444", "time": "5.120"}].
- Modules:test_catalogue_transaction_apply_offline, test_grocery_capture_transaction_offline, test_mongo_transactions, test_restaurant_capture_transaction_offline, test_restaurant_refund_webhook_transaction_offline, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_transaction_commit_retry. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H10 — remaining-runtime.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/remaining-runtime.xml`;currentSHA256:`87eca641c9ce12708b55b296149b53ca6fc0c8669537bc9d36eda90dc85b634d`.
- Log:`/workspace/come-in-current/evidence/session-20261117/remaining-runtime.log`;currentSHA256:`f621fae538be45e680631ebeeff68dd3b63860b5d2c204f2e6a68b993a9de097`;99bytes fullyread.
- Actual counts:T61/P61/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T08:34:11.054102+00:00", "hostname": "bca3ee959444", "time": "5.592"}].
- Modules:test_batch_5task_runtime, test_iter_notifications_admin_measured, test_preview_runtime_e2e. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H11 — auth-contract-correction.xml

- XML path:`/workspace/come-in-current/evidence/session-20261117/auth-contract-correction.xml`;currentSHA256:`eb82a0acb4848c58d600c6dd6b04e03cd8db96145bec7c0ab2970ab30a4de46b`.
- Log:`/workspace/come-in-current/evidence/session-20261117/auth-contract-correction.log`;currentSHA256:`4e9d76a81cd5571a0842be3d94b51347cd364d2245a9980dbb5ad399d19ac81c`;141bytes fullyread.
- Actual counts:T9/P9/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:01:56.741822+00:00", "hostname": "bca3ee959444", "time": "1.880"}].
- Modules:test_frontend_contracts, test_shared_system_integration_contract, test_task12_customer_support_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H12 — step3-tests.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step3-tests.xml`;currentSHA256:`d5f646a021c24df23a76b964473d26476a3f247f7017f324b17b6cccd140191d`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step3-tests.log`;currentSHA256:`47ad9afc7dff678e6e71b1aec3da3746c38d5be5584e96d326b41043f386f061`;596bytes fullyread.
- Actual counts:T30/P30/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:54:32.373710+00:00", "hostname": "bca3ee959444", "time": "2.439"}].
- Modules:test_functional_blockers_regression, test_payment_environment_boundary, test_task17_grocery_payment_gate_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H13 — step9-payment-v2.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment-v2.xml`;currentSHA256:`7b2362e8287b6f8a620bc11ed67c05cceec4c88619a9a7e1e6575c6cb0be374d`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment-v2.log`;currentSHA256:`5df416f5b28e0f894230c771c6d42922b2ab155dbc4752f32f9cc6f7ada4ab73`;2816bytes fullyread.
- Actual counts:T78/P78/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T10:20:57.816035+00:00", "hostname": "bca3ee959444", "time": "7.495"}].
- Modules:test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_payment_environment_boundary, test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_step1_final_refund_admin_offline, test_task18_refund_safety_iteration3, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H14 — step5-tests.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests.xml`;currentSHA256:`75158bad5f8ba207355d9f58a6c31aa4946cb4a3f1cf1ec3f5c4406bf5eb6303`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests.log`;currentSHA256:`e82b4de6dc240b308d9ec7293368fa30c6e11e9752f8d2c84471817f99be020f`;87bytes fullyread.
- Actual counts:T0/P0/F0/E0/S0;status:ZERO TESTS;NOT A PASS RUN.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T10:10:34.571365+00:00", "hostname": "bca3ee959444", "time": "0.008"}].
- Modules:NOT FOUND;zero-testartifact. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H15 — step4-tests-v2.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests-v2.xml`;currentSHA256:`02102ae671b9463770780a6b7391f8065742bd2e656a2d5b1f5619e07b6dabda`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests-v2.log`;currentSHA256:`a36246a65174bf43f875e189bcd119ca35ba3edb00f246e632d717c1af55eaf8`;2607bytes fullyread.
- Actual counts:T48/P48/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T10:00:06.714995+00:00", "hostname": "bca3ee959444", "time": "8.761"}].
- Modules:test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_shared_system_integration_contract, test_task10_payment_refund_notification_contract, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H16 — step1-live.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step1-live.xml`;currentSHA256:`cdf984b0b591dda55a6b2ea3845e6843131090e574b59e320495801cd2b27286`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step1-live.log`;currentSHA256:`6a4e5321d0918790a4bdb97138ca9e0321d8277eb1450f7250e94f0700f05ec2`;99bytes fullyread.
- Actual counts:T70/P70/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:48:07.463618+00:00", "hostname": "bca3ee959444", "time": "9.479"}].
- Modules:test_batch_5task_runtime, test_iter_notifications_admin_measured, test_preview_runtime_e2e, test_task5_live_mongo_transactions. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Recorded candidate runner:step1-live-runner.py launches python -m pytest -n0 -q with4explicit live modules andthis JUnit destination;no contemporaneous process/source/environment receipt. References:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step1-live-runner.py`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H17 — step9-payment.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment.xml`;currentSHA256:`27c7ab90c8daaf1d5f2f553beb841032fe448f35e0c6761bedad169dc948079d`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step9-payment.log`;currentSHA256:`c01161c6d70721112d7017861a20b1ef72a6a930c7f9c74fef2fd227dd67e828`;4852bytes fullyread.
- Actual counts:T78/P76/F2/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T10:20:33.399228+00:00", "hostname": "bca3ee959444", "time": "4.447"}].
- Modules:test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_payment_environment_boundary, test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_step1_final_refund_admin_offline, test_task18_refund_safety_iteration3, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw1] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios; tests.test_grocery_refund_local_integration::test_local_grocery_refund_authorization_accounting_and_retry.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H18 — step5-tests-v2.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests-v2.xml`;currentSHA256:`575c2e1211728fea32e78a300ef4319bb9f405aceabde7ce78bbfdd79f3a760a`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step5-tests-v2.log`;currentSHA256:`9e6cdbfc066cc7f6d053ef1706d8cd1c0e347a498a41d1396d8612d2bfb09096`;2625bytes fullyread.
- Actual counts:T50/P50/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T10:10:53.981523+00:00", "hostname": "bca3ee959444", "time": "7.727"}].
- Modules:test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_step1_final_refund_admin_offline, test_task11_grocery_refund_status_contract, test_task18_refund_safety_iteration3. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H19 — step4-final.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-final.xml`;currentSHA256:`dbe8429e0f760e2489571c75783cad952204d5805ae1547efc0b52778e66483c`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-final.log`;currentSHA256:`d3f533dc7c4ab388674d8739ef295628da6cc85d3925dc01f397f9afb6839e72`;2607bytes fullyread.
- Actual counts:T62/P62/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T10:03:25.232767+00:00", "hostname": "bca3ee959444", "time": "5.565"}].
- Modules:test_payment_environment_boundary, test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_shared_system_integration_contract, test_task10_payment_refund_notification_contract, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H20 — step4-tests.xml

- XML path:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests.xml`;currentSHA256:`4129c08d91e2176bc01a7a7726efa091e39bcaca7bf4b6429c17e29f59d149ee`.
- Log:`/workspace/come-in-current/evidence/release-completion-20261117T094751Z/step4-tests.log`;currentSHA256:`078f9596af2a5a3c2e1ac63d3abcaddb56c6bfd0ebd06d359cc9f495be2c454d`;9825bytes fullyread.
- Actual counts:T48/P47/F1/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:59:30.429540+00:00", "hostname": "bca3ee959444", "time": "4.625"}].
- Modules:test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_shared_system_integration_contract, test_task10_payment_refund_notification_contract, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H21 — three-failures-after.xml

- XML path:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-after.xml`;currentSHA256:`fb48f614b43fde1d3607ff9b6d8514295d406baf07d2629793918945fbdab880`.
- Log:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-after.log`;currentSHA256:`f21802e5e24571b06b077e416af1539fdce6ad55b407e03af6af45b03968cb3b`;98bytes fullyread.
- Actual counts:T3/P3/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:15:24.609966+00:00", "hostname": "bca3ee959444", "time": "0.077"}].
- Modules:test_frontend_contracts, test_universal_catalogue_import_engine. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H22 — csv-focused.xml

- XML path:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/csv-focused.xml`;currentSHA256:`a3c4031e9235813c72d590a856e2d91d843b838ed4290a64d643544421aa07b9`.
- Log:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/csv-focused.log`;currentSHA256:`7675a80b671dcea752b95232e2c5608b37bcf5a445a4010666219f75dd8a44d7`;113bytes fullyread.
- Actual counts:T8/P8/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:14:24.008321+00:00", "hostname": "bca3ee959444", "time": "0.068"}].
- Modules:test_universal_catalogue_import_engine. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H23 — three-failures-before.xml

- XML path:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-before.xml`;currentSHA256:`2a7bfbb5abd96645bf505427349d710aca75026dce955f601c56f9453576fc89`.
- Log:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/three-failures-before.log`;currentSHA256:`21a366d80b5de68343c22c344660f3e0105736ce38bb3d809a30e7f7e4b57917`;3311bytes fullyread.
- Actual counts:T3/P0/F3/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:13:46.165158+00:00", "hostname": "bca3ee959444", "time": "0.057"}].
- Modules:test_frontend_contracts, test_universal_catalogue_import_engine. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_universal_catalogue_import_engine::test_csv_formula_like_cells_are_preserved_as_untrusted_source_text; tests.test_frontend_contracts::test_shopping_home_theme_contract_and_separate_mode_routes; tests.test_frontend_contracts::test_bakery_has_no_fabricated_sample_inventory_and_voice_is_honest.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H24 — relevant-regression.xml

- XML path:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/relevant-regression.xml`;currentSHA256:`b49002aa2c9ee4475c06dd72b6754e39fc01e060e070a65eb77ab4022bf2ab40`.
- Log:`/workspace/come-in-current/evidence/regression-fixes-20261117T091345Z/relevant-regression.log`;currentSHA256:`e135c611b6f63e99a2be20fb60b40f2f7465b7d636027dde2db5ad2abc486c36`;756bytes fullyread.
- Actual counts:T96/P92/F0/E0/S4;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-17T09:17:07.795784+00:00", "hostname": "bca3ee959444", "time": "3.637"}].
- Modules:test_catalog_import_security_contract, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_chand_demo_contract, test_chand_media_contract, test_chand_shopping_integration_contract, test_frontend_contracts, test_universal_catalogue_import_engine. Current module presence is NOT a historical-sourcebinding.
- Command evidence:NOT FOUND:matching log has no recorded exact invocation;testcase module coverage is available but not original command/source/environment attestation..
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H25 — upload-types-before.xml

- XML path:`/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-types-before.xml`;currentSHA256:`e880146295adae5e6e24874a64bea1f2ef61aec8e0e4f39d2665381acec271e3`.
- Log:`/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-types-before.log`;currentSHA256:`537d915ab0b2a1fe7cc1502dcc3ca738bdc246738e87c3e59cb08a968fa9af52`;7036bytes fullyread.
- Actual counts:T8/P0/F8/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:36:52.433912+00:00", "hostname": "4fa0f8dc6b53", "time": "1.783"}].
- Modules:test_image_upload_type_boundary. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available historical external-validation report records source-test selection for before/after upload checks;not a per-process signed execution/source/environment receipt. References:`/workspace/come-in-current/EXTERNAL_VALIDATION_REPORT.md`.
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw0] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/jpeg]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/png]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/gif]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/webp]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/jpeg]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/png]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/gif]; tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/webp].
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H26 — upload-security-after.xml

- XML path:`/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-security-after.xml`;currentSHA256:`f171157678f722b030bb12e97612cd29e7a3787b67d6b8dcf1627eda15a02d4c`.
- Log:`/workspace/come-in-current/evidence/external-validation-20261118T133459Z/upload-security-after.log`;currentSHA256:`9624060a0c4cb5c0e8f4db5533f697e17afb1782212b3804bd9c8a7044e4db96`;665bytes fullyread.
- Actual counts:T25/P25/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:37:38.548339+00:00", "hostname": "4fa0f8dc6b53", "time": "3.071"}].
- Modules:test_catalog_import_security_contract, test_image_upload_type_boundary, test_upload_allocation_bound. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available historical external-validation report records source-test selection for before/after upload checks;not a per-process signed execution/source/environment receipt. References:`/workspace/come-in-current/EXTERNAL_VALIDATION_REPORT.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H27 — security-races-before.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/security-races-before.xml`;currentSHA256:`a5823d72863f9e395701315e26859655a9ca72aa2f8dff95d320d2a1094686f9`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/security-races-before.log`;currentSHA256:`1f9f45cbbb54915671cd45a2eba98204eb142f878c05520e1de02184c2a38e9d`;9518bytes fullyread.
- Actual counts:T4/P0/F4/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:22:31.668987+00:00", "hostname": "4fa0f8dc6b53", "time": "1.533"}].
- Modules:test_final_payment_transition_races. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw0] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_final_payment_transition_races::test_customer_transition_cannot_overwrite_concurrent_final_state[concurrent0-cancel_restaurant_order]; tests.test_final_payment_transition_races::test_customer_transition_cannot_overwrite_concurrent_final_state[concurrent0-retry_restaurant_payment]; tests.test_final_payment_transition_races::test_customer_transition_cannot_overwrite_concurrent_final_state[concurrent1-cancel_restaurant_order]; tests.test_final_payment_transition_races::test_customer_transition_cannot_overwrite_concurrent_final_state[concurrent1-retry_restaurant_payment].
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H28 — backend-final.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/backend-final.xml`;currentSHA256:`039d4c3f0ddc4a0741ede271ccb71b0a8eb9315b7c13577ad1516b73d0efedbc`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/backend-final.log`;currentSHA256:`f56e61ac93b47f6d658fd5eb7122660325fb1349e359c91657d658f5102618a7`;2223bytes fullyread.
- Actual counts:T564/P557/F1/E0/S6;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:23:45.698295+00:00", "hostname": "4fa0f8dc6b53", "time": "31.268"}].
- Modules:test_assistant_context_contract, test_catalog_import_security_contract, test_catalog_reference_minimum, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_catalogue_validator_migration, test_chand_demo_contract, test_chand_feedback_contract, test_chand_localization_contract, test_chand_media_contract, test_chand_ollama_provider_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_directory_only_category_contract, test_final_payment_transition_races, test_financial_rules, test_financial_security_contract, test_frontend_contracts, test_functional_blockers_regression, test_grocery_capture_transaction_offline, test_grocery_checkout_security_contract, test_grocery_pay_at_shop_status_contract, test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_home_services_remaining_contract, test_master_catalog_api_contract, test_master_catalog_seller_ui_contract, test_mongo_backup_safety_offline, test_mongo_config, test_mongo_portability_tool, test_mongo_transactions, test_online_shop_product_listing_contract, test_p0_payment_checkout_completion, test_p0_restaurant_delivery_panel, test_payment_environment_boundary, test_payment_webhook_local_integration, test_provider_adapter_contracts, test_referral_implementation_contract, test_referral_rules, test_restaurant_api_contract, test_restaurant_capture_transaction_offline, test_restaurant_pricing, test_restaurant_refund_webhook_transaction_offline, test_restaurant_serviceability, test_role_security_retail_import_contract, test_shared_system_integration_contract, test_shop_registration_browse_entrypoints, test_shopping_cart_variants_contract, test_shopping_catalog_contract, test_shopping_rewards_redemption_contract, test_standard_ui_image_shop_cta_contract, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_step1_final_restore_index_profile_offline, test_targeted_tasks_9_12_15_18_21, test_task10_payment_refund_notification_contract, test_task11_grocery_refund_status_contract, test_task11_live_order_tracking_contract, test_task12_customer_support_contract, test_task13_seller_support_status_contract, test_task14_seller_support_ui_contract, test_task16_production_cors_contract, test_task17_grocery_payment_gate_contract, test_task18_refund_safety_iteration3, test_task19_seller_admin_workflows_contract, test_task20_product_catalog_variants_stock_contract, test_task21_customer_shopping_workflow_contract, test_task22_checkout_audit_contract, test_task23_order_tracking_authorization_contract, test_task24_repeat_order_contract, test_task5_customer_measured_shopping_contract, test_task5_measured_import_contract, test_task5_task7_ui_implementation_contract, test_task9_order_actions_contract, test_transaction_commit_retry, test_universal_catalogue_import_engine, test_upload_allocation_bound, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw1] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_delivery_tracking_contract::test_customer_cancellation_clears_any_stored_restaurant_delivery_location.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'; tests.test_grocery_refund_local_integration::test_local_grocery_refund_authorization_accounting_and_retry:requires explicit local disposable payment-test opt-in; tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios:requires explicit local disposable payment-test opt-in.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H29 — payment-local.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/payment-local.xml`;currentSHA256:`e59c2522b2ffded9573e5b8f288db83154cbe62e5fd2ea197d05d79e1100d4c9`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/payment-local.log`;currentSHA256:`59d1ec3d26b337be5eb3cd1529e48208b10aaa079b880e7f574243bde001f8e5`;2816bytes fullyread.
- Actual counts:T78/P78/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:20:26.013737+00:00", "hostname": "4fa0f8dc6b53", "time": "8.279"}].
- Modules:test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_payment_environment_boundary, test_payment_webhook_local_integration, test_restaurant_refund_webhook_transaction_offline, test_step1_final_refund_admin_offline, test_task18_refund_safety_iteration3, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H30 — backend-full.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/backend-full.xml`;currentSHA256:`0786bac0b221c114389c016b2ba730f114047a39f743d246a620d258deca291b`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/backend-full.log`;currentSHA256:`e663cdc4aa3b94046be3700065fa2da57252e626dd5421304f0ae0a5f9f709ba`;3223bytes fullyread.
- Actual counts:T559/P551/F2/E0/S6;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:18:58.261920+00:00", "hostname": "4fa0f8dc6b53", "time": "35.620"}].
- Modules:test_assistant_context_contract, test_catalog_import_security_contract, test_catalog_reference_minimum, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_catalogue_validator_migration, test_chand_demo_contract, test_chand_feedback_contract, test_chand_localization_contract, test_chand_media_contract, test_chand_ollama_provider_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_directory_only_category_contract, test_financial_rules, test_financial_security_contract, test_frontend_contracts, test_functional_blockers_regression, test_grocery_capture_transaction_offline, test_grocery_checkout_security_contract, test_grocery_pay_at_shop_status_contract, test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_home_services_remaining_contract, test_master_catalog_api_contract, test_master_catalog_seller_ui_contract, test_mongo_backup_safety_offline, test_mongo_config, test_mongo_portability_tool, test_mongo_transactions, test_online_shop_product_listing_contract, test_p0_payment_checkout_completion, test_p0_restaurant_delivery_panel, test_payment_environment_boundary, test_payment_webhook_local_integration, test_provider_adapter_contracts, test_referral_implementation_contract, test_referral_rules, test_restaurant_api_contract, test_restaurant_capture_transaction_offline, test_restaurant_pricing, test_restaurant_refund_webhook_transaction_offline, test_restaurant_serviceability, test_role_security_retail_import_contract, test_shared_system_integration_contract, test_shop_registration_browse_entrypoints, test_shopping_cart_variants_contract, test_shopping_catalog_contract, test_shopping_rewards_redemption_contract, test_standard_ui_image_shop_cta_contract, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_step1_final_restore_index_profile_offline, test_targeted_tasks_9_12_15_18_21, test_task10_payment_refund_notification_contract, test_task11_grocery_refund_status_contract, test_task11_live_order_tracking_contract, test_task12_customer_support_contract, test_task13_seller_support_status_contract, test_task14_seller_support_ui_contract, test_task16_production_cors_contract, test_task17_grocery_payment_gate_contract, test_task18_refund_safety_iteration3, test_task19_seller_admin_workflows_contract, test_task20_product_catalog_variants_stock_contract, test_task21_customer_shopping_workflow_contract, test_task22_checkout_audit_contract, test_task23_order_tracking_authorization_contract, test_task24_repeat_order_contract, test_task5_customer_measured_shopping_contract, test_task5_measured_import_contract, test_task5_task7_ui_implementation_contract, test_task9_order_actions_contract, test_transaction_commit_retry, test_universal_catalogue_import_engine, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:Python 3.11.18 /workspace/come-in-tools/py311/bin/python; [gw0] linux -- Python 3.11.18 /workspace/come-in-tools/py311/bin/python. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:tests.test_shared_system_integration_contract::test_restaurant_payment_ui_does_not_claim_success_or_call_gateway_without_sdk; tests.test_restaurant_api_contract::test_webhook_event_is_recorded_after_processing_for_retry_safety.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'; tests.test_grocery_refund_local_integration::test_local_grocery_refund_authorization_accounting_and_retry:requires explicit local disposable payment-test opt-in; tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios:requires explicit local disposable payment-test opt-in.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H31 — contract-focused.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/contract-focused.xml`;currentSHA256:`f1846403e7e88e38f253d9e06f3672e7076e9647ffb06fee2568df9d706b787f`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/contract-focused.log`;currentSHA256:`80d00c4a4b99a081a9635b4c60c11a7da6149e29ecd34fd4a25b1d0435a8c932`;142bytes fullyread.
- Actual counts:T24/P24/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:20:06.480649+00:00", "hostname": "4fa0f8dc6b53", "time": "2.650"}].
- Modules:test_restaurant_api_contract, test_shared_system_integration_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H32 — backend-final-v2.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/backend-final-v2.xml`;currentSHA256:`51fb23bdfaf50692e6919c342ad9be0a653b082e986f1ed825deb3706b3a00c2`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/backend-final-v2.log`;currentSHA256:`025499fd2a593440ed591ac4f2d5aecdf662947490d5e66f7dbe7f04de596c05`;1238bytes fullyread.
- Actual counts:T564/P558/F0/E0/S6;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:25:23.275822+00:00", "hostname": "4fa0f8dc6b53", "time": "32.190"}].
- Modules:test_assistant_context_contract, test_catalog_import_security_contract, test_catalog_reference_minimum, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_catalogue_validator_migration, test_chand_demo_contract, test_chand_feedback_contract, test_chand_localization_contract, test_chand_media_contract, test_chand_ollama_provider_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_directory_only_category_contract, test_final_payment_transition_races, test_financial_rules, test_financial_security_contract, test_frontend_contracts, test_functional_blockers_regression, test_grocery_capture_transaction_offline, test_grocery_checkout_security_contract, test_grocery_pay_at_shop_status_contract, test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_home_services_remaining_contract, test_master_catalog_api_contract, test_master_catalog_seller_ui_contract, test_mongo_backup_safety_offline, test_mongo_config, test_mongo_portability_tool, test_mongo_transactions, test_online_shop_product_listing_contract, test_p0_payment_checkout_completion, test_p0_restaurant_delivery_panel, test_payment_environment_boundary, test_payment_webhook_local_integration, test_provider_adapter_contracts, test_referral_implementation_contract, test_referral_rules, test_restaurant_api_contract, test_restaurant_capture_transaction_offline, test_restaurant_pricing, test_restaurant_refund_webhook_transaction_offline, test_restaurant_serviceability, test_role_security_retail_import_contract, test_shared_system_integration_contract, test_shop_registration_browse_entrypoints, test_shopping_cart_variants_contract, test_shopping_catalog_contract, test_shopping_rewards_redemption_contract, test_standard_ui_image_shop_cta_contract, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_step1_final_restore_index_profile_offline, test_targeted_tasks_9_12_15_18_21, test_task10_payment_refund_notification_contract, test_task11_grocery_refund_status_contract, test_task11_live_order_tracking_contract, test_task12_customer_support_contract, test_task13_seller_support_status_contract, test_task14_seller_support_ui_contract, test_task16_production_cors_contract, test_task17_grocery_payment_gate_contract, test_task18_refund_safety_iteration3, test_task19_seller_admin_workflows_contract, test_task20_product_catalog_variants_stock_contract, test_task21_customer_shopping_workflow_contract, test_task22_checkout_audit_contract, test_task23_order_tracking_authorization_contract, test_task24_repeat_order_contract, test_task5_customer_measured_shopping_contract, test_task5_measured_import_contract, test_task5_task7_ui_implementation_contract, test_task9_order_actions_contract, test_transaction_commit_retry, test_universal_catalogue_import_engine, test_upload_allocation_bound, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'; tests.test_grocery_refund_local_integration::test_local_grocery_refund_authorization_accounting_and_retry:requires explicit local disposable payment-test opt-in; tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios:requires explicit local disposable payment-test opt-in.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H33 — security-races-after.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/security-races-after.xml`;currentSHA256:`737878a8f6e366e435dfa466518b3bf5ae12686c9c87acde03cac02793ecee4d`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/security-races-after.log`;currentSHA256:`f14385b2dfd78e1a1d5689573748f094fa3f238d4276b5338200e3185a380344`;665bytes fullyread.
- Actual counts:T28/P28/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:23:10.051980+00:00", "hostname": "4fa0f8dc6b53", "time": "2.685"}].
- Modules:test_final_payment_transition_races, test_restaurant_api_contract, test_shared_system_integration_contract. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H34 — security-final-focused.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/security-final-focused.xml`;currentSHA256:`af87bfce8a43298e8bf3406da36a9fd6a5979f2faab33ee59fb5768d8c92e8a4`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/security-final-focused.log`;currentSHA256:`5862bbff4c5ec7ae428a1cdc5d4368186a7df468d1d45c58398fb67703ac4a8d`;664bytes fullyread.
- Actual counts:T5/P5/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:23:44.317153+00:00", "hostname": "4fa0f8dc6b53", "time": "1.123"}].
- Modules:test_final_payment_transition_races, test_upload_allocation_bound. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H35 — security-tracking-final.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/security-tracking-final.xml`;currentSHA256:`6f6b90e1e7e92cd62dddf92b35b126b1f8d755a7562c80465f6c947d71f79521`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/security-tracking-final.log`;currentSHA256:`beaf7b0ff225b4f375434a36b672b666465f76639224d764055595ee53d7606d`;665bytes fullyread.
- Actual counts:T17/P17/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:24:54.575700+00:00", "hostname": "4fa0f8dc6b53", "time": "1.741"}].
- Modules:test_delivery_tracking_contract, test_final_payment_transition_races, test_upload_allocation_bound. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H36 — live-regression.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/live-regression.xml`;currentSHA256:`3fcec03b36752f0b7b3b08516a3fc8212f55bbf8fd3684acc21e1ed61f4c37eb`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/live-regression.log`;currentSHA256:`7d49005c1bc18ed5d373ac4c552ebc429c72de0e821056485791a5fb11225c43`;99bytes fullyread.
- Actual counts:T70/P70/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:20:25.773575+00:00", "hostname": "4fa0f8dc6b53", "time": "9.625"}].
- Modules:test_batch_5task_runtime, test_iter_notifications_admin_measured, test_preview_runtime_e2e, test_task5_live_mongo_transactions. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Recorded candidate runner launches python -m pytest -n0 -q with4explicit live modules andthis JUnit destination;runtime target/source hash not captured contemporaneously. References:`/workspace/come-in-current/evidence/resume-20261118/live-runner.py`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H37 — affected-local-final.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/affected-local-final.xml`;currentSHA256:`d918bbb7c34881c510dccc9eab14c22c49d972953133816f1cef2b75a9416616`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/affected-local-final.log`;currentSHA256:`9c8fa9e190321dca42feda91d52f5a36d3b27aecbc61e10e25dcaff09f96a194`;2735bytes fullyread.
- Actual counts:T7/P7/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:25:23.245605+00:00", "hostname": "4fa0f8dc6b53", "time": "5.576"}].
- Modules:test_final_payment_transition_races, test_grocery_refund_local_integration, test_payment_webhook_local_integration, test_upload_allocation_bound. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H38 — live-regression-final.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/live-regression-final.xml`;currentSHA256:`ec16a54d1d43efad79c261408ee43a2216a1a92ec3ce0e53d724c2a9c09e990e`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/live-regression-final.log`;currentSHA256:`795097a869bc6d051b83f7ad14d1ff9ab99573d257c0d444cce96c17373ca702`;99bytes fullyread.
- Actual counts:T70/P70/F0/E0/S0;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:25:37.302305+00:00", "hostname": "4fa0f8dc6b53", "time": "9.343"}].
- Modules:test_batch_5task_runtime, test_iter_notifications_admin_measured, test_preview_runtime_e2e, test_task5_live_mongo_transactions. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Recorded candidate runner launches python -m pytest -n0 -q with4explicit live modules andthis JUnit destination;runtime target/source hash not captured contemporaneously. References:`/workspace/come-in-current/evidence/resume-20261118/live-runner-final.py`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:none.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.

### H39 — backend-full-v2.xml

- XML path:`/workspace/come-in-current/evidence/resume-20261118/backend-full-v2.xml`;currentSHA256:`d657160d4a8faffa3959e6d3cd4b36c7715b4f0c92b880538a30d719651ae2d6`.
- Log:`/workspace/come-in-current/evidence/resume-20261118/backend-full-v2.log`;currentSHA256:`948d8b74b78b2ef42ac52d862ea2304213588950ad81f7d792245d41bebdeb66`;1238bytes fullyread.
- Actual counts:T559/P553/F0/E0/S6;status:HISTORICAL RESULT ARTIFACT;NOT FRESH VALIDATION.
- Suite timestamps/hostnames:[{"timestamp": "2026-11-18T13:20:38.725101+00:00", "hostname": "4fa0f8dc6b53", "time": "32.255"}].
- Modules:test_assistant_context_contract, test_catalog_import_security_contract, test_catalog_reference_minimum, test_catalogue_chand_adapter, test_catalogue_import_job_api_contract, test_catalogue_import_workflow_contract, test_catalogue_transaction_apply_offline, test_catalogue_validator_migration, test_chand_demo_contract, test_chand_feedback_contract, test_chand_localization_contract, test_chand_media_contract, test_chand_ollama_provider_contract, test_chand_shopping_integration_contract, test_delivery_partner_onboarding_contract, test_delivery_tracking_contract, test_directory_only_category_contract, test_financial_rules, test_financial_security_contract, test_frontend_contracts, test_functional_blockers_regression, test_grocery_capture_transaction_offline, test_grocery_checkout_security_contract, test_grocery_pay_at_shop_status_contract, test_grocery_refund_eligibility, test_grocery_refund_local_integration, test_home_services_remaining_contract, test_master_catalog_api_contract, test_master_catalog_seller_ui_contract, test_mongo_backup_safety_offline, test_mongo_config, test_mongo_portability_tool, test_mongo_transactions, test_online_shop_product_listing_contract, test_p0_payment_checkout_completion, test_p0_restaurant_delivery_panel, test_payment_environment_boundary, test_payment_webhook_local_integration, test_provider_adapter_contracts, test_referral_implementation_contract, test_referral_rules, test_restaurant_api_contract, test_restaurant_capture_transaction_offline, test_restaurant_pricing, test_restaurant_refund_webhook_transaction_offline, test_restaurant_serviceability, test_role_security_retail_import_contract, test_shared_system_integration_contract, test_shop_registration_browse_entrypoints, test_shopping_cart_variants_contract, test_shopping_catalog_contract, test_shopping_rewards_redemption_contract, test_standard_ui_image_shop_cta_contract, test_step1_final_delivery_partner_transactions_offline, test_step1_final_refund_admin_offline, test_step1_final_restore_index_profile_offline, test_targeted_tasks_9_12_15_18_21, test_task10_payment_refund_notification_contract, test_task11_grocery_refund_status_contract, test_task11_live_order_tracking_contract, test_task12_customer_support_contract, test_task13_seller_support_status_contract, test_task14_seller_support_ui_contract, test_task16_production_cors_contract, test_task17_grocery_payment_gate_contract, test_task18_refund_safety_iteration3, test_task19_seller_admin_workflows_contract, test_task20_product_catalog_variants_stock_contract, test_task21_customer_shopping_workflow_contract, test_task22_checkout_audit_contract, test_task23_order_tracking_authorization_contract, test_task24_repeat_order_contract, test_task5_customer_measured_shopping_contract, test_task5_measured_import_contract, test_task5_task7_ui_implementation_contract, test_task9_order_actions_contract, test_transaction_commit_retry, test_universal_catalogue_import_engine, test_webhook_envelope_security. Current module presence is NOT a historical-sourcebinding.
- Command evidence:Available command documentation:COMMANDS.md records offline exclusions,local payment opt-in andfocused selectors. It is documentation,not a per-run exact original invocation/env/source receipt for every earlier artifact. References:`/workspace/come-in-current/evidence/resume-20261118/COMMANDS.md`.
- Captured environment clues:No Python/platform/version clue in matchinglog. Complete per-run package/dependency/environment fingerprint NOT FOUND. No actual.envvalue inspected/copied.
- Failed cases:none.
- Error cases:none.
- Skipped cases/reasons:tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance:could not import 'pypdf': No module named 'pypdf'; tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available:could not import 'openpyxl': No module named 'openpyxl'; tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields:could not import 'PIL': No module named 'PIL'; tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields:could not import 'fitz': No module named 'fitz'; tests.test_grocery_refund_local_integration::test_local_grocery_refund_authorization_accounting_and_retry:requires explicit local disposable payment-test opt-in; tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios:requires explicit local disposable payment-test opt-in.
- Historical source binding:UNVERIFIED:current repo HEAD identifiesuploadedZIP Gitcheckout,not outsideGit extraction used duringthis run. No per-run current app content hash or complete env fingerprint supplied.


## Fresh executed validation — separate from historical claims

| Validation | Actual result | Evidence and boundary |
|---|---|---|
| Existing offline backend/source contracts |574PASS /0FAIL /6SKIP;exit0 |[backend-offline-result.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-offline-result.json>); Python sockets denied, no dotenv/source edits. |
| Local ASGI + real MongoDB with provider mocks |2PASS /0FAIL /0SKIP;exit0 |[backend-local-result.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-local-result.json>);unique disposable DBs,zero external provider operations. |
| Four existing local HTTP + MongoDB suites |70PASS /0FAIL /0SKIP;exit0 |[backend-live.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-live.xml>);byte-identical test copies,unique synthetic DB,ephemeral loopback server stopped. |
| Additional unchanged legacy localHTTP+Mongo |17PASS /2assertionFAIL /3setupERROR /1SKIP;exit1 |[backend-legacy-result.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-legacy-result.json>);contract/fixture mismatch,genuine unsuccessful run;not automatically a source defect. |
| Current frontend checks |Six command gates PASS;TypeScript0errors;ESLint0errors/10warnings |[frontend-validation.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/frontend-validation.json>);CHAND helper,SDK VM mock,config guard,andactual webexport;no current browser/device acceptance. |
| Final independently reproduced broad security suite |49PASS /1FAIL /0ERROR /0SKIP |[broad-security-reproduced.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduced.xml>);exact command/source/harness receipts;last-admin invariant FAIL with controlled doubles. |
| New reset/model/function + real MongoDB validation |23PASS /7FAIL /0ERROR /0SKIP |[password-reset-results-v2.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/password-reset-results-v2.json>);controlled interleavings/fault injection,offline SMTP;not HTTP/real email or production. |
| Current local DB metadata |PASS for52collections/119indexes/all67source declarations matched |[db-metadata-current.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/db-metadata-current.json>);PRIMARYrs0,Mongo7.0.45,27018loopback;metadata only. |
| Android/iOS autolinking |Both source-resolution commands exit0 |[native-provider-validation.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/native-provider-validation.json>);zero native builds/devices;those gates remainBLOCKED. |
| Actual provider TEST payment/webhook/refund |BLOCKED;zeroactualcalls |[RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/RAZORPAY_TEST_PAYMENT_REFUND_VALIDATION_REPORT.md>);key/secret/webhook empty,mode absent;no genuine delivery/settlement. |

Initial offline/local/live selections totaled646PASS/0FAIL/6SKIP. The separately executed, unchanged legacy suite adds17PASS/2assertionFAIL/3setupERROR/1SKIP. Final existing-regression invocations therefore total663PASS/2FAIL/3ERROR/7SKIP. Two offline opt-in skips subsequently passed;deduplicated outcomes are663PASS/2FAIL/3ERROR/5SKIP. The regression JSON also reports five combined unsuccessful outcomes underFAIL;this report preserves actual JUnit failure/error distinctions. New security runs and heterogeneous frontend/compiler/build checks are outside these totals. Overall current regression gate isFAIL;no test outcome is concealed or reclassified as a pass.

The final reset failures areRESET-10(invalid SMTP-port exception/undelivered token),RESET-16(two same-token concurrent resets accepted),RESET-17(password changed while token remained reusable after injected token-write failure),RESET-18(success with missing target account),RESET-19(pre-reset access JWT remains valid),RESET-27(concurrent limiter overshoot),RESET-30(accepted long-password suffix equivalence at bcrypt72-byte boundary). Security priorities and owner policy decisions must be reviewed;no passing failure-detection check closes a defect.

The first reset harness attempt is retained separately:15PASS/6FAIL/9ERROR;compile inherited the harness future-annotations flag andleftunresolvedEmailStr references. The correctioncompile(dont_inherit=True)matchesactualserverannotationsemantics;finalv2 is23PASS/7FAIL/0ERROR. The firstscriptprecorrectionhashwasnotcaptured andisnotinvented. Firstbroadattempt48PASS/2FAILincludedaninvalidexample.testEmailStrfixture;usingexample.comcorrectsthefixturewithsource/assertionsunchanged. Finalbroadv2is49PASS/1FAIL. Attemptsare notsummed;theseareharnesscorrections,notsourcefixes.

## Additional legacy execution and exact failures

Final receipt:[backend-legacy-result.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-legacy-result.json>);JUnit:[backend-legacy.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-legacy.xml>);log:[backend-legacy.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-legacy.log>). Executed 2026-11-19T15:50:56.838579+00:00–2026-11-19T15:51:01.231148+00:00;byte-identicaltestSHA256`a4e9c990c972790e4f6f6c9fd0aca31d280c3bdac5bc5a0ab9cc56d34d5935b9`;sourcebefore/after unchanged;ephemeralserverstopped;newsyntheticdatabase retained,no database drop/reset. Actualcommand:

```sh
/workspace/come-in-tools/py311/bin/python -m pytest /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/legacy-tests/backend_test.py -q -n 0 -p no:cacheprovider -p backend_local_guard -c /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/pytest.ini --junitxml=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-legacy.xml --basetemp=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-legacy-tmp
```

The duplicate-registration test receives the current409 while its unchanged assertion expects400. Three cases fail during shared product-fixture setup because it omits currently requiredProductIn.description and receives422;the two order-dependent test bodies never reach their order APIcalls. Product-delete creation likewise omits required fields and then assumes anid,raisingKeyError. These are actual unsuccessful assertions/fixtures;they do not by themselves establish faulty current application policy. Image-upload isSKIPPED because unconfigured object storage returns503. No assertion was weakened,no source/configuration was changed,andno currentregressionpassclaimincludes these unsuccessful cases.

## Why the current offline result is574PASS instead of historical558PASS

An independent exact `(classname,name)` comparison of historical `evidence/resume-20261118/backend-final-v2.xml` and current `backend-offline.xml` finds564historical identities and580current identities:all564retained,zero removed,exactly16added. All16are in `tests.test_image_upload_type_boundary`;no other module contributes a new case identity. Both runs have the identical six skipped identities/reasons. Thus558+16=574passes. This is a coverage observation,not evidence that this session changed application source or proof of the historical execution environment. Protected source hashes remain unchanged.

| Added current case identity | Current result |
|---|---|
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/gif]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/jpeg]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/png]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[-image/webp]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/gif]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/jpeg]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/png]` |PASS |
| `tests.test_image_upload_type_boundary::test_declared_image_mime_cannot_store_non_image_bytes[<html>not an image</html>-image/webp]` |PASS |
| `tests.test_image_upload_type_boundary::test_matching_format_headers_preserve_supported_upload_paths[image/gif-GIF89alocal-header-test]` |PASS |
| `tests.test_image_upload_type_boundary::test_matching_format_headers_preserve_supported_upload_paths[image/jpeg-\xff\xd8\xff\xe0local-header-test]` |PASS |
| `tests.test_image_upload_type_boundary::test_matching_format_headers_preserve_supported_upload_paths[image/png-\x89PNG\r\n\x1a\nlocal-header-test]` |PASS |
| `tests.test_image_upload_type_boundary::test_matching_format_headers_preserve_supported_upload_paths[image/webp-RIFF\x04\x00\x00\x00WEBP]` |PASS |
| `tests.test_image_upload_type_boundary::test_mismatched_or_truncated_headers_are_not_stored[image/gif-\xff\xd8\xff]` |PASS |
| `tests.test_image_upload_type_boundary::test_mismatched_or_truncated_headers_are_not_stored[image/jpeg-\x89PNG\r\n\x1a\n]` |PASS |
| `tests.test_image_upload_type_boundary::test_mismatched_or_truncated_headers_are_not_stored[image/png-GIF89a]` |PASS |
| `tests.test_image_upload_type_boundary::test_mismatched_or_truncated_headers_are_not_stored[image/webp-RIFFno-webp]` |PASS |

The six offline skip occurrences are:

| Case | Reason | Final disposition |
|---|---|---|
| `tests.test_grocery_refund_local_integration::test_local_grocery_refund_authorization_accounting_and_retry` |requires explicit local disposable payment-test opt-in |Passed in current local opt-in run |
| `tests.test_payment_webhook_local_integration::test_local_signed_webhook_http_and_transaction_scenarios` |requires explicit local disposable payment-test opt-in |Passed in current local opt-in run |
| `tests.test_universal_catalogue_import_engine::test_pdf_text_adapter_preserves_page_provenance` |could not import 'pypdf': No module named 'pypdf' |Still SKIPPED;optional dependency unavailable |
| `tests.test_universal_catalogue_import_engine::test_xlsx_processes_multiple_sheets_when_openpyxl_available` |could not import 'openpyxl': No module named 'openpyxl' |Still SKIPPED;optional dependency unavailable |
| `tests.test_universal_catalogue_import_engine::test_image_ocr_extracts_visible_text_without_promoting_fields` |could not import 'PIL': No module named 'PIL' |Still SKIPPED;optional dependency unavailable |
| `tests.test_universal_catalogue_import_engine::test_scanned_pdf_uses_optional_ocr_without_promoting_product_fields` |could not import 'fitz': No module named 'fitz' |Still SKIPPED;optional dependency unavailable |

The unchanged legacy `tests/backend_test.py` was subsequently safely executed exactly once after its configuration and existing stale-list were inspected. The stale-list has28entries butzero entries naming this file;it was not legitimate to treat that list as prior documentation for this legacy file. The byte-identicalcopy ran againsta freshloopbackHTTP+MongoDB with dotenvdisabled/networkguard. Final result:17PASS/2assertionFAIL/3setupERROR/1SKIP,exit1. No assertion was rewritten. Details below distinguish current contract mismatch from application defects.

## Actual current commands, runtime and source binding

Current offline execution ran2026-11-19T08:40:05.003614+00:00–2026-11-19T08:40:51.732500+00:00;Python executable `/workspace/come-in-tools/py311/bin/python`,platform `Linux-6.18.57-x86_64-with-glibc2.41`,source/input map113files and`source_changed=[]`. Command:

```sh
/workspace/come-in-tools/py311/bin/python -m pytest tests -q -n 0 -p no:cacheprovider -p backend_network_guard --ignore=tests/test_preview_runtime_e2e.py --ignore=tests/test_batch_5task_runtime.py --ignore=tests/test_iter_notifications_admin_measured.py --ignore=tests/test_task5_live_mongo_transactions.py --ignore=tests/backend_test.py --junitxml=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-offline.xml --basetemp=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-offline-tmp
```

Local execution ran2026-11-19T08:42:54.743700+00:00–2026-11-19T08:43:18.308150+00:00;actual commands:

```sh
/workspace/come-in-tools/py311/bin/python -m pytest tests/test_payment_webhook_local_integration.py tests/test_grocery_refund_local_integration.py -q -n 0 -p no:cacheprovider -p backend_local_guard --junitxml=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-local-payments.xml --basetemp=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-local-payment-tmp
```

```sh
/workspace/come-in-tools/py311/bin/python -m pytest /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/live-tests/test_preview_runtime_e2e.py /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/live-tests/test_batch_5task_runtime.py /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/live-tests/test_iter_notifications_admin_measured.py /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/live-tests/test_task5_live_mongo_transactions.py -q -n 0 -p no:cacheprovider -p backend_local_guard -c /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/pytest.ini --junitxml=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-live.xml --basetemp=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-live-tmp
```

Runners/guards/input-hash maps are retained in [run_backend_regression.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/run_backend_regression.py>), [run_local_backend_validation.py](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/run_local_backend_validation.py>), [backend-regression.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/backend-regression.json>). Local guards allow only the selected loopback Mongo/HTTP destinations;dotenv loaders are disabled;unique synthetic DBs were retained. Tests did perform authorized writes only to new disposable databases. Metadata capture itself read no application records and wrote no data. These are test safeguards rather than deployed security controls.

Frontend commands,non-secret environment,exit codes,logs and95source-file bindings are in [frontend-validation.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/frontend-validation.json>). The web export used existing pinned Yarn/dependencies and95hash-matched scratch source copies;output contains100artifacts. No packages were installed. CHAND stdout says11assertions while source has13top-levelassert call sites;preserve the reported11with this caveat. Five SDK VM scenarios andnineconfig-guard checks are not real UI/native/provider workflows.

Reset validation ran2026-11-19T15:47:42.074742+00:00–2026-11-19T15:47:51.316681+00:00 withPython3.11.18 (main, Oct 26 2026, 14:05:07) [Clang 23.1.3 ]. Recorded package versions:`{"PyJWT": "2.15.1", "bcrypt": "4.1.3", "fastapi": "0.110.1", "motor": "3.7.1", "pydantic": "2.14.3", "pymongo": "4.18.2"}`. Actual unmodified functions/models were AST-extracted and bound by full source/segment hashes;Motor operated on a new retained loopback MongoDB database. Source SHA256before/after=`a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db`. A live HTTP server/middleware,actual SMTP transport and production impact were not tested. The new harness itself is separate evidence,not application source.

## Safe reproduction and remaining provenance

The18NovCOMMANDS.md and saved runners provide candidate historical command paths,not original invocation attestation. Old live runners can seed accounts and target existing historical output files;do not execute them unchanged. Any future reproduction must use a new unique evidence folder,verified disposable database,nonsecret process-only fixtures,offline/loopback guard,newstdout/JUnit paths andinput hashes. Do not overwrite old evidence or repeat successful runs without a relevant change. Current runner output destinations also require new paths before a rerun.

Trusted contemporaneous source/build hashes,command/exitstatus andnonsecret environment/isolation/custody receipts are still required to authenticate decisive historical runs. New localtests do not recover those facts. Currentmetadata supplies a newtimestamp/rawoptions butdoesnot prove the oldsnapshot timing orproduction state. HistoricalMongo8.0.38claims do not match the actual current local7.0.45metadata and are retained as historical.

Native compile/device,actual provider TEST payment/webhook/refund settlement,productionTLS/CORS/DBaccess/secrets/backup controls anduncovered browser/workflow states remain separately open orblocked. Task1isREVIEWPENDING;no source fix,Task2,commit,push,deploy,publish orowner approval occurred. Finalreview requires actual security failure dispositions.

## Canonical security mapping and final disposition

[security-audit.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/security-audit.json>) and[COMPLETE_APPLICATION_SECURITY_AUDIT.md](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/COMPLETE_APPLICATION_SECURITY_AUDIT.md>) retain ninecanonicalfindings:1HIGH,6MEDIUM,2LOW. RESET16/17 mapSEC01HIGH;RESET10/18areLOWsubissuesunderSEC01 ratherthannewIDs. RESET19→SEC02MEDIUM;RESET27→SEC04MEDIUM;RESET30→SEC06LOW. RESET29is helper/sourceobservationunderSEC03;productioningressremainsunverified. SEC09MEDIUMislimitedtocontrolledmodeldoublelast-adminconcurrency,notrealMongoraceorproductionlockoutproof. Thefulloriginalbroadtestshellinvocationwasnotretained;source/harness/segmenthashesandXMLtimestampareavailableandarethecorrectboundedprovenance.

Task1remains**REVIEW PENDING**. CurrentregressionhasactuallegacyFAIL/ERROR,andsecurityvalidationFAIL. Native/device/provider/productiongatesremainBLOCKED. Ownerreviewsandseparatelyauthorizesanysourcefixes;thisworkstreamdoesnotfixorstartTask2. Currentartifactreceipthashesandall20retainedgaps+ninecanonicalsecurityactionsarein[consolidated-action-register.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/consolidated-action-register.json>).

## Final independent broad-security reproduction

[broad-security-reproduction.json](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduction.json>) records a justified independent execution from2026-11-19T15:54:41.894482+00:00to2026-11-19T15:54:42.949221+00:00,exit1. The earlier v2 command was not retained,so the unchanged harness was reproduced once to close the **new command-provenance gap**. This is not an arbitrary repeat and doesnot recover the old invocation. Actual command:

```sh
/workspace/come-in-tools/py311/bin/python -m pytest /workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/test_broad_security_isolated.py -c /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/pytest.ini -n 0 -p no:cacheprovider -q --junitxml=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduced.xml --basetemp=/workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduction-tmp
```

Final outcome49PASS/1FAIL/0ERROR/0SKIP;count these50cases once,not v1+v2+reproduction. Source and harness hashes match the retained input;all sockets denied,in-memory synthetic doubles only,no application-server import/DB/provider activity. [broad-security-reproduced.xml](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduced.xml>) and[broad-security-reproduced.log](</workspace/come-in-current/evidence/phase-1-task-1-owner-review/validation-20261119T140704+0530/broad-security-reproduced.log>) retain the unsuppressed last-admin failure. This reproduction strengthens currentprovenance,not realMongoconcurrency orproductionacceptance.
