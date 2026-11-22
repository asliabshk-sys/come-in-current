# COME-IN — Owner Review Master Report

Review time: 2026-11-18T07:17:41.372443-08:00 (UTC−08). Repository `/workspace/come-in-current`, branch `work`, HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a`: all match the expected identity. Application source is `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115`, outside the Git checkout.

**Final decision: REVIEW PENDING.** This is an evidence review for the owner, not personal owner approval, task closure or production readiness. Original reports, manifests, checkpoints, ZIP, source and configuration are preserved. Only this NEW review folder was written. No application tests, DB queries/writes, browser actions, provider calls, attacks, installs or service changes were performed in this review. Task 2 and implementation were not started.

## Overall review result

All seven audit reports were independently inspected against current source, saved metadata, historical XMLs, manifests and preservation evidence. Independent reviewers checked frontend, backend/security and DB/history; the primary reviewer reconciled scope, provenance, contradictions and the final decision.

**93 material claim-units: 47 VERIFIED, 30 PARTIALLY VERIFIED, 6 UNVERIFIED, 3 CONTRADICTED and 7 BLOCKED.** This denominator is explicit in the ledger. It is not a completion percentage or a count of working screens/tests. Source patterns and their severity/closure claims are separate units.

## What was independently verified

- Exact workspace, `work` branch and required HEAD. The extraction is outside Git; no assumption was made about current remote `main` because no fetch was performed.
- All six original Markdown report hashes/sizes and all 31 supporting hashes/sizes match the original audit manifest. The original JSON manifest is separately hashed by this review.
- All 8,150 files covered by the original preservation baseline still match current bytes. This proves covered-file identity, not the excluded-file history or every action taken in the earlier session.
- Frontend: 53 app files, 95 scoped app/src modules, 579 explicit event attributes, including 391 `onPress` attributes. Saved row/handler multisets match current source. All 108 selected literal route candidates resolve to existing file/group candidates.
- Backend: 179 explicit route decorators, 60 Pydantic classes and 292 declared fields match. No duplicate method plus literal path was found in the inspected router. Only four endpoints explicitly declare `response_model`; other responses are not thereby proven broken or accepted.
- Database evidence: 67 current index declarations, 27 unique declarations and a strict 67/67 match against the saved 52-collection/119-index snapshot. The saved snapshot has 52 false validator flags. No fresh DB query was performed in this review.
- Historical evidence: all 39 unique XMLs exist and their indexed suite attributes match. Actual testcase arithmetic supports the selected historical 558 passed/6 skipped, 70 passed, 78 passed and 25 passed. Ten failed-run XMLs and one zero-test artifact also remain visible. These are not fresh tests or independent non-overlapping totals.
- Original ZIP: 5,484,042 bytes; SHA-256 `3233dcd9c8f1997b06035fd5cd7b458ab511658faf25e184044b17aec624d28c`; fresh read-only CRC PASS. Byte comparison reproduces 62 changed existing archive members in the extraction.

## Important discrepancies

1. **Overbroad preservation wording — CONTRADICTED.** Master report line 19 claims all inherited report/history files were protected. The baseline has 8,128 app files, 20 root files and two patches, but zero root/evidence files, including zero of the 39 historical XMLs. This is a coverage discrepancy, not evidence that any excluded file changed. Current review hashes cannot be backdated to the audit.
2. **Special-file public-path fields — CONTRADICTED as URL semantics.** The screen table assigns `/_layout`, `+html` and `+not-found` file-derived paths to special files. They are not ordinary public URLs. The original table does identify file kinds, but the “public path” field needs explicit qualification. No dead application route was demonstrated.
3. **SEC-01 related-test relevance — CONTRADICTED.** The named `test_functional_blockers_regression.py` file has no password-reset coverage. Existing reset-route existence assertions elsewhere do not verify one-time atomic consumption. The original report correctly says concurrency is untested; the wrong citation does not invalidate the source finding or close HIGH risk.

## Important coverage and provenance gaps

- Branch-aware analysis finds 113 literal navigation leaves, not just the 108 selected checks. Five omitted branches at Home `index.tsx:102`, `notifications.tsx:42` and `orders.tsx:193` all reference existing paths. Five `href` attributes and 14 dynamic router arguments are outside those checks. `auth.tsx:64` forwards dynamic `next`; allowed-target behavior remains unverified, not a proven redirect exploit.
- The API inventory captures annotations but omits endpoint defaults and `Query` constraints. The “all signatures” statement is stronger than the data, although API/model counts are correct. `server.py:3643` provides a concrete omitted `kind` pattern/default.
- GET is not automatically read-only: referral validation can insert `referral_link_events`, and `/referrals/me` can persist a referral code. A future safe-runtime plan needs transitive side-effect classification. No such GET request was issued here.
- The DB snapshot has no capture-specific timestamp or raw `hello`/collection validator options. False flags support only “no nonempty validator observed in those 52 local snapshot entries,” not current, global or production absence.
- Historical XML paths and suite attributes were captured, but original XML hashes and complete source/command/environment run bindings were not. This review records current XML hashes for future integrity, not retrospective attestation.
- Actual environment files, dependency trees and inherited root/evidence were outside the original baseline. Covered-file preservation is verified; an unlimited all-configuration/history claim is not independently established.

## Security review

All eight source patterns are supported. The reported total—one HIGH, five MEDIUM and two LOW—is correct, but impact/severity and closure remain conditional on policies, deployment mitigations and missing isolated evidence. No attack or fix was performed.

**HIGH SEC-01 remains OPEN:** reset token lookup, password update and token marking are separate operations without a shared transaction/conditional claim. High-priority review is defensible for account recovery integrity, but arbitrary unauthenticated takeover was not demonstrated and a valid token/flow is a prerequisite. Personal owner disposition and separately approved evidence are still required.

The seven other findings concern revocation policy, forwarded-IP trust, throttle atomicity, public diagnostic writes, bcrypt byte handling, synchronous HTTP in async routes and webhook buffering limits. Full source/report references, impact, severity justification and remaining evidence are in SECURITY_FINDINGS_REVIEW.md.

## Runtime and external limits

Bindings are not working buttons. The historical 17 browser checks are limited web login/render/navigation evidence, not every workflow, error state, permission or native checkout. JS exports and autolink discovery are not native binary/device evidence. Local Mongo/mocked-provider/signed-event tests do not establish actual Razorpay TEST payments, provider webhook delivery, refund settlement or other external deliveries. Production TLS, CORS, secrets, DB roles, retention/RPO/RTO, ingress and logging remain blocked without authorized infrastructure evidence. No production readiness claim is made.

## Decision and next action

**Final review decision and recommendation: REVIEW PENDING.** Counts and much source evidence are sound. The unresolved HIGH disposition, coverage/provenance qualifications and missing runtime/external evidence prevent automatic closure or final owner approval. Twenty evidence/decision gaps are recorded; they are not twenty new canonical tasks.

The six required review outputs and supporting notes are in this NEW folder. Before/after Git status and final preservation verification are recorded by the review manifest. All original reports, the original manifest, checkpoints, source, configuration, ZIP and Git history were left unchanged.

**STOP:** wait for personal owner review and explicit approval of any further scope. Do not implement fixes, start Task 2, install anything, change configuration or deploy. No application test/build/service/DB/provider operation was started by this review.
