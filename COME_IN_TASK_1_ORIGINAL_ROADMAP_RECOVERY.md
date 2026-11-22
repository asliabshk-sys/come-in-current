# COME-IN — Phase 1, Task 1: Original Roadmap Recovery & Verification

Investigation completed 2026-11-18T06:20:36.257369-08:00 (UTC−08). **COMPLETE — bounded read-only investigation and reporting.** This does not mean an original30-task roadmap was recovered,any implementation task is complete,or the app is release-ready. Phase1/Task2 is NOT STARTED;user review/approval required. This recovery task is a separate audit assignment,not a rename of canonical roadmap Task1.

## 1. Executive Summary

- **Original30-task roadmap: NOT FOUND within the searched records.** Do not infer that it never existed outside available records.
- **22-main-task roadmap: SOURCE VERIFIED(document).** The strongest available roadmap explicitly says22 and prohibits automatic expansion beyond22. Its Restaurant Mode addendum explicitly says it is not a23rd main task.
- Later implementation reports numbered23,24,25 exist;an earlier reconciliation document explicitly calls their numbering separate from the approved roadmap. Those labels are preserved verbatim;no task renumbered,merged or renamed here.
- Task26 and27 references/details: **NOT FOUND** in the available project documents,source/report names,spreadsheet,Git records or archive. The user's recollection that numbering reached27 remains UNVERIFIED.
- Tasks28,29,30: **TASK DETAILS NOT RECOVERED**. No names invented.
- One actual application ZIP found;5,484,042bytes,SHA256 and CRC verified read-only. Earlier ZIPs are referenced in historical reports but their original bytes are not available here.

## 2. Active Workspace and Repository Identification

- Active cwd `/workspace`;actual Git checkout `/workspace/come-in-current`,repository `asliabshk-sys/come-in-current`.
- Suggested `/workspaces/come-in-current` is not the active path. `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115` is the retained application extraction outside Git,not a separate app Git checkout.
- Branch `work`;HEAD `a223290a8866a1ebeaac982f546491fdc197ae7a` (`Upload verified COME-IN Master Source ZIP`). Two reachable commits:initial README `0396a15` and source ZIP upload `a223290`,both15Nov2026. This is not the original full development Git history.
- Existing untracked checkpoint/report/evidence/patch additions preserved. Original README is stale (says source not uploaded);the actual archive and later upload commit establish available source presence. No README edit made.
- No source/API/auth/UI/theme/navigation/DB/service/provider configuration change,no tests/builds rerun,no external/production access,no commit/push/deploy/publish. Only requested report,investigation evidence and root five checkpoint documents updated.

## 3. Documents and Records Searched

Search scope:available project checkout and extracted app including `project-reports/`,`project-reports/memory/`,`reports/audit/previous-handoff-package-2026-11-12/PROJECT_HISTORY/ADDITIONAL_LIBRARY_ARTIFACTS/`,`MASTER_BACKUP_EVIDENCE/HISTORICAL_DOCUMENT_VERSIONS/`,root Markdown/JSON/XLSX trackers,existing root checkpoints/readiness/regression/session logs,test-output artifacts and all reachable Git history. Also checked available `/mnt/data`,`/workspaces`,`/tmp` for surfaced project records/archives. Original absent paths in historical reports were not treated as current files. No remote account/private chat/Drive history or unavailable original attachments were queried.

Read/scanned **925 project files** (Markdown/JSON/text/log/XML/CSV/HTML plus relevant code references and one XLSX). Dependency trees,caches,.git objects,runtime DB files,uploads and secret `.env` contents were excluded. No PDF roadmap was present. Task-number search supports spaced/underscored/compact Task23..30 forms;spreadsheet cells parsed with stdlib ZIP/XML including shared strings. No optional parser packages installed.

Key records:

- [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md)
- [COME_IN_MASTER_TASK_TRACKER.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/COME_IN_MASTER_TASK_TRACKER.md), [COME_IN_MASTER_TASK_TRACKER.json](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/COME_IN_MASTER_TASK_TRACKER.json), [COME_IN_MASTER_TASK_TRACKER.xlsx](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/COME_IN_MASTER_TASK_TRACKER.xlsx)
- [MASTER_TASK_TRACKER.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/MASTER_TASK_TRACKER.md) —14Nov continuation view,not a new original roadmap.
- Historical tracker copies in both MongoDB Step1/Phase2 backup document folders and previous handoff package.
- Original numbered reports Task10..25,especially Task23/24 and the three Task25 audit/design/implementation-decision reports.
- [MASTER_BACKUP_EVIDENCE/SOURCE_CONSOLIDATION_REPORT.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/MASTER_BACKUP_EVIDENCE/SOURCE_CONSOLIDATION_REPORT.md) and PROJECT_MANIFEST.json for archive provenance/limitations.
- All five root checkpoint documents plus COME_IN_RELEASE_READINESS.md,FINAL_REGRESSION_REPORT.md,EXTERNAL_VALIDATION_REPORT.md;latest prior report dated18Nov2026 05:41:49−08.

Complete file paths/hashes:[searched-file-manifest.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/searched-file-manifest.json). Detailed number hits:[exhaustive-numbering-hits.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/exhaustive-numbering-hits.json). Spreadsheet cells:[tracker-spreadsheet-rows.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/tracker-spreadsheet-rows.json). A hit is a reference,not a distinct task or proof of completion. Counts include duplicated historical copies.

## 4. Original Roadmap Found

Strongest available candidate is `/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md`. Heading: **COME-IN APP — MASTER PROJECT PROMPT**,subtitle **Project Memory •22 Main Tasks •Restaurant Mode •Safety •Next Steps**. Lines59/61 begin the22-task list;Task1..22 are explicit headings. Rule15 expressly forbids automatic expansion beyond22. Section4 says Restaurant Mode is not a23rd main task.

This is **SOURCE VERIFIED(original-document artifact)**,not proof that the author first drafted it here or that no older30-task plan ever existed. Base document has no reliable creation timestamp;18Oct2026 evidence appendices give an available dated bound,not original authorship. Its current app copy exactly matches the ZIP member. Roadmap SHA256:`702adc3c8648443c0fb4e3e35ce2b84304c27f89b4bf852011cfec69081b6ece`. ZIP member timestamps describe packaging,not first authorship.

Original Restaurant Mode/theme-switch addendum records parent tasks **2,3,4,6,7,10,14,17,18** and explicitly keeps Restaurant Mode within those tasks;it is not a new main-task number. This is documentary scope,not current feature verification.

Definition of evidence labels used below:
- **SOURCE VERIFIED**:definition/reference found directly in available document/source. Here this generally means document verification,not current behavior verification.
- **HISTORICAL REPORT**:older status/implementation/test claim;not revalidated by running app/tests.
- **TEST EVIDENCE FOUND**:persisted test report/result artifact found;scope/date preserved,not freshly executed.
- **NOT FOUND**:absent within explicit search scope.
- **CONFLICTING RECORDS**:different labels/statuses/numbering retained without choosing a new merged task.
- **UNVERIFIED**:insufficient evidence for the particular claim.

## 5. Recovered Original Task List

Original names and numbering below are unchanged. The detailed descriptions are copied from the recovered roadmap;the table statuses are historical Markdown/JSON tracker claims,not this audit's implementation verdict.

| Original # | Exact original name | Phase | Historical MD / JSON status |
|---:|---|---|---|
Full verbatim definitions and all recovered tracker fields: [recovered-original-tasks.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/recovered-original-tasks.json) (including nested historical verification fields).

| 1 | Existing Project Audit | Phase 1 — Audit | **COMPLETED** / COMPLETED |
| 2 | Theme and Design | Phase 2 — Design और Customer Experience | **COMPLETED** / COMPLETED |
| 3 | Home Screen and Navigation | Phase 2 — Design और Customer Experience | **COMPLETED** / COMPLETED |
| 4 | Categories and Catalog | Phase 3 — Product Catalog और Shopping | **COMPLETED** / COMPLETED |
| 5 | Quantity, Variants and Units | Phase 3 — Product Catalog और Shopping | **COMPLETED** / PARTIAL |
| 6 | Search and Filters | Phase 3 — Product Catalog और Shopping | **COMPLETED** / COMPLETED |
| 7 | Cart and Checkout | Phase 4 — Cart और Orders | **COMPLETED** / COMPLETED |
| 8 | Repeat Order | Phase 4 — Cart और Orders | **COMPLETED** / COMPLETED |
| 9 | Out-of-Stock Replacement | Phase 4 — Cart और Orders | **COMPLETED** / COMPLETED |
| 10 | Live Tracking | Phase 5 — Delivery और Customer Support | **COMPLETED** / COMPLETED |
| 11 | Order Help and Refund Status | Phase 5 — Delivery और Customer Support | **PARTIAL** / PARTIAL |
| 12 | Excel/CSV Price and Stock Import | Phase 6 — Seller Tools और Data | **COMPLETED** / COMPLETED |
| 13 | Login and Account | Phase 7 — Accounts और Operations | **COMPLETED** / COMPLETED |
| 14 | Seller/Shop/Restaurant Panel | Phase 7 — Accounts और Operations | **COMPLETED** / COMPLETED |
| 15 | Admin Panel | Phase 7 — Accounts और Operations | **COMPLETED** / COMPLETED |
| 16 | Backend, Database and Security | Phase 8 — Backend, Security और Payments | **PARTIAL** / PARTIAL |
| 17 | Payments and Notifications | Phase 8 — Backend, Security और Payments | **PARTIAL** / PARTIAL |
| 18 | Testing and Bug Fixes | Phase 9 — Testing और Launch | **PARTIAL** / PARTIAL |
| 19 | Production Build and Launch | Phase 9 — Testing और Launch | **BLOCKED** / BLOCKED |
| 20 | Smart Notification System | Phase 10 — Advanced Features | **PARTIAL** / PARTIAL |
| 21 | Smart Price Comparison | Phase 10 — Advanced Features | **PARTIAL** / PARTIAL |
| 22 | Home Services Logo/Icon and Tile Integration | Phase 10 — Advanced Features | **COMPLETED** / COMPLETED |

### Original Task 1: Existing Project Audit

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:63);phase **Phase 1 — Audit**.

Original description/subtasks:

- वर्तमान ऐप, स्क्रीन, navigation, frontend/backend, API, database और authentication की जाँच।

- कौन-से बटन और workflows वास्तव में काम करते हैं, जाँचें।

- Grocery, online/offline shops, restaurants और Home Services के मौजूदा फीचर पहचानें।

- duplicate routes/components, errors और अधूरे काम नोट करें।

- पहले read-only audit करें; बिना अनुमति fixes न करें।

**HISTORICAL REPORT — tracker evidence:** historical audit reports; ZIP re-imported and inspected 2026-11-11

Markdown tracker implementation/evidence field: Historical audit reports; uploaded ZIP extracted and inspected 2026-11-11.

Markdown remaining/dependency field: No new audit required unless source changes.

XLSX implementation evidence: Historical audit reports; uploaded ZIP integrity and project-root inspection completed in this handover.. Remaining/subtasks: No new audit unless source changes.. XLSX reported status: COMPLETED. Reported tests: ZIP integrity PASS; 362 project files extracted.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 2: Theme and Design

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:77);phase **Phase 2 — Design और Customer Experience**.

Original description/subtasks:

- साफ़, consistent, mobile-friendly डिज़ाइन।

- मुख्य shopping theme: Yellow + Forest Green + Pale Mint।

- rounded cards, readable text, subtle shadows और consistent spacing।

**HISTORICAL REPORT — tracker evidence:** THEME_* reports; UI preserved; missing style keys fixed (no visual redesign)

Markdown tracker implementation/evidence field: Existing THEME reports; UI preserved; prior missing style keys fixed.

Markdown remaining/dependency field: No redesign; visual/device verification remains separate.

XLSX implementation evidence: Existing theme and styling source preserved; earlier theme reports retained.. Remaining/subtasks: No redesign; full visual/device recheck remains separate.. XLSX reported status: COMPLETED. Reported tests: Historical theme reports; no UI redesign in this batch.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 3: Home Screen and Navigation

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:85);phase **Phase 2 — Design और Customer Experience**.

Original description/subtasks:

- Home screen, category entry points और bottom navigation।

- Online Shops, Offline Shops, Restaurants और Home Services तक स्पष्ट पहुँच।

- सेक्शन बदलने और वापस आने का आसान रास्ता।

**HISTORICAL REPORT — tracker evidence:** app/(tabs)/index.tsx renders (screenshot); bell now opens notifications

Markdown tracker implementation/evidence field: Home and navigation source; BATCH-02 reports notification bell/unread badge UI E2E.

Markdown remaining/dependency field: Full device check pending.

XLSX implementation evidence: Home/navigation source and notification bell wiring present.. Remaining/subtasks: Full real-device check pending.. XLSX reported status: COMPLETED. Reported tests: Historical screenshot/UI E2E report.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 4: Categories and Catalog

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:95);phase **Phase 3 — Product Catalog और Shopping**.

Original description/subtasks:

- Grocery, daily essentials, local shops और restaurant/food categories व menu/catalog।

- मौजूदा data model audit करें।

**HISTORICAL REPORT — tracker evidence:** catalog reports; /api/catalog/products PASS in runtime e2e

Markdown tracker implementation/evidence field: Catalog reports; /api/catalog/products PASS in historical runtime E2E.

Markdown remaining/dependency field: Not rerun in Iteration 3.

XLSX implementation evidence: Catalog API and category source present.. Remaining/subtasks: Not rerun in Iteration 3.. XLSX reported status: COMPLETED. Reported tests: Historical runtime E2E: catalog endpoint PASS.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 5: Quantity, Variants and Units

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:101);phase **Phase 3 — Product Catalog और Shopping**.

Original description/subtasks:

- product size, weight, quantity, variants और unit selection।

- जहाँ लागू हो, price per unit स्पष्ट करें।

**HISTORICAL REPORT — tracker evidence:** Authoritative baseline hashes verified; baseline manifest 595/595 PASS; 43 focused Task 5-related tests PASS/0 FAIL; compileall PASS; no application source changes.

Markdown tracker implementation/evidence field: 2026-11-11 Emergent live run on MongoDB 7.0.45 replica set: T5-MONGO-01..07, measured Repeat Order E2E and transaction-backed CSV import apply/rollback 9/9 PASS; Expo Customer + Seller Preview PASS; full backend regression 415 PASS / 0 FAIL / 23 skipped.

Markdown remaining/dependency field: Open low finding F-1: concurrent checkout losers get 503 (WriteConflict) instead of 409 — no oversell. Native device and Razorpay online payment out of scope.

XLSX implementation evidence: Phase 4 source remains preserved; no application source changes. This resumption reverified baseline ZIP/Excel hashes and manifest; reran 43 focused Task 5-related tests and backend compileall successfully.. Remaining/subtasks: None for the Emergent preview scope. Open low-severity finding F-1: concurrent checkout losers get 503 (WriteConflict) instead of 409 — no oversell. Native device runtime and Razorpay online payment not in scope (not configured).. XLSX reported status: COMPLETED. Reported tests: 2026-11-11 LIVE: T5-MONGO-01..07 PASS (9/9 incl. measured Repeat Order E2E + transaction-backed CSV import apply/invalid/duplicate/rollback, run twice); Expo Customer + Seller Preview PASS (testing agent iteration_1); full backend regression serial 415 PASS / 0 FAIL / 23 skipped.. Dependencies/blockers: None in Emergent preview. External: Razorpay TEST keys for online payment; native device for APK checks.. Runtime verified that batch: Yes.

JSON remaining: Seven MongoDB transaction scenarios; Seller/Customer Preview; measured Repeat Order E2E; transaction-backed CSV/Excel import apply.;blockers: No local MongoDB runtime/drivers or authorized disposable endpoint; no pinned Yarn/Expo dependencies or non-production frontend .env. Corepack registry DNS failure EAI_AGAIN..

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 6: Search and Filters

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:107);phase **Phase 3 — Product Catalog और Shopping**.

Original description/subtasks:

- products, shops, restaurants और food items की खोज।

- relevant filters, जैसे category, veg/non-veg, cuisine और availability जहाँ डेटा उपलब्ध हो।

- price comparison के नियम Task 21 से जुड़ें।

**HISTORICAL REPORT — tracker evidence:** earlier reports; not re-tested in this batch

Markdown tracker implementation/evidence field: Earlier Task 6 implementation and test reports preserved.

Markdown remaining/dependency field: Not rerun in this batch.

XLSX implementation evidence: Search/filter source and earlier task report preserved.. Remaining/subtasks: Not rerun in this batch.. XLSX reported status: COMPLETED. Reported tests: Historical implementation evidence.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 7: Cart and Checkout

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:117);phase **Phase 4 — Cart और Orders**.

Original description/subtasks:

- सुरक्षित cart, price/stock revalidation और checkout।

- Restaurant cart और grocery/shop cart अलग रहें; गलती से mix न हों।

- checkout, delivery fee और order summary स्पष्ट हों।

**HISTORICAL REPORT — tracker evidence:** Checkout crash fixed (fulfillment TDZ). Quote -> confirm -> COD/pickup orders PASS in UI and API; quote reuse rejected

Markdown tracker implementation/evidence field: Checkout quote/idempotency source; historical COD/pickup UI/API tests; Iteration 3 fixes empty-cart and unavailable-fulfillment messaging.

Markdown remaining/dependency field: No Expo runtime in current environment.

XLSX implementation evidence: Server quote, idempotency, COD/pickup checkout source preserved; checkout messaging improved.. Remaining/subtasks: Expo runtime and broader checkout regressions pending.. XLSX reported status: COMPLETED. Reported tests: Current source contracts included in 43-pass focused batch.. Dependencies/blockers: Expo runtime. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 8: Repeat Order

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:125);phase **Phase 4 — Cart और Orders**.

Original description/subtasks:

- पहले के order से items दोबारा चुनना; current price और stock फिर जाँचना।

**HISTORICAL REPORT — tracker evidence:** earlier TASK24 report; measured repeat extension NOT TESTED in this batch

Markdown tracker implementation/evidence field: Earlier TASK24 report and existing repeat-order source.

Markdown remaining/dependency field: Measured repeat-order extension not fully verified.

XLSX implementation evidence: Repeat-order source and earlier TASK24 report preserved.. Remaining/subtasks: Measured repeat-order extension not fully verified.. XLSX reported status: COMPLETED. Reported tests: Historical task report; not rerun in this batch.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 9: Out-of-Stock Replacement

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:129);phase **Phase 4 — Cart और Orders**.

Original description/subtasks:

- item unavailable होने पर replacement या removal का विकल्प।

- अनुमति के बिना अनचाहा replacement न करें।

**HISTORICAL REPORT — tracker evidence:** earlier TASK25 report; not re-tested

Markdown tracker implementation/evidence field: Earlier TASK25 report and existing source.

Markdown remaining/dependency field: Not rerun in this batch.

XLSX implementation evidence: Out-of-stock replacement source and earlier TASK25 report preserved.. Remaining/subtasks: Not rerun in this batch.. XLSX reported status: COMPLETED. Reported tests: Historical task report.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 10: Live Tracking

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:137);phase **Phase 5 — Delivery और Customer Support**.

Original description/subtasks:

- वास्तविक data/integration होने पर order status/tracking।

- live tracking का दावा तभी करें जब सच में काम करे।

- शुरुआत में restaurant अपनी delivery संभाल सकता है, यदि arrangement स्पष्ट हो।

**HISTORICAL REPORT — tracker evidence:** /api/orders/{id}/tracking PASS in runtime e2e

Markdown tracker implementation/evidence field: Historical /api/orders/{id}/tracking runtime E2E report.

Markdown remaining/dependency field: Not rerun in this batch.

XLSX implementation evidence: Tracking endpoint/source and prior runtime report preserved.. Remaining/subtasks: Not rerun in this batch.. XLSX reported status: COMPLETED. Reported tests: Historical tracking E2E PASS.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 11: Order Help and Refund Status

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:145);phase **Phase 5 — Delivery और Customer Support**.

Original description/subtasks:

- order issue, cancellation/help और refund status।

- Shop Call Assistance subtask: shop का phone connect न हो तो ग्राहक Come-In agent/representative से दुकान पर जाकर बात करवाने का अनुरोध कर सके। Operational व्यवस्था पहले तय करनी होगी।

**HISTORICAL REPORT — tracker evidence:** Restaurant Admin refund route has paise cap, provider history, CAS claim and reconciliation safeguards; Grocery refund summary states are offline-tested; in-app notification routes exist.

Markdown tracker implementation/evidence field: Restaurant Admin refund safeguards retained; Grocery refund summary states and in-app notification routes have offline coverage.

Markdown remaining/dependency field: Automatic Grocery refunds, refund-specific notifications and live customer/seller/admin status synchronization remain pending.

XLSX implementation evidence: Restaurant Admin refund route retains paise cap, provider history, CAS claim and reconciliation safeguards; Grocery refund summary states are offline-tested; in-app notification routes exist.. Remaining/subtasks: Automatic Grocery provider refunds; live provider/DB lifecycle; customer/seller/admin live refund status synchronization; refund-specific notifications and reconciliation.. XLSX reported status: PARTIAL. Reported tests: Grocery refund summary + Restaurant refund safeguards covered by offline contracts; no live provider/DB.. Dependencies/blockers: Disposable DB + approved Razorpay TEST/mock provider.. Runtime verified that batch: No.

JSON remaining: Automatic Grocery provider refunds, live provider/DB lifecycle, customer/seller/admin live refund status synchronization, refund-specific notification behavior and reconciliation remain pending.;blockers: —.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 12: Excel/CSV Price and Stock Import

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:153);phase **Phase 6 — Seller Tools और Data**.

Original description/subtasks:

- shops के लिए products, price और stock upload/update।

- importer schema audit करें।

- stable product ID से update करें; duplicates न बनाएँ।

- invalid prices, missing names, invalid stock और wrong columns पर errors दिखाएँ।

- पहले test/staging में जाँचें; production data पर बिना अनुमति परीक्षण न करें।

**HISTORICAL REPORT — tracker evidence:** earlier reports; import confirm dialogs now work on web (Alert shim). Measured CSV columns NOT TESTED

Markdown tracker implementation/evidence field: Earlier reports; import confirmation dialog source fix; Task 5 measured CSV parser/model now has offline coverage.

Markdown remaining/dependency field: Transaction-backed measured import apply remains pending with disposable MongoDB verification.

XLSX implementation evidence: Earlier reports and import confirmation dialog source fix; Task 5 measured CSV parser/model now has offline coverage.. Remaining/subtasks: Transaction-backed measured import apply remains pending with disposable MongoDB verification.. XLSX reported status: COMPLETED. Reported tests: Historical Task 12 evidence plus Task 5 actual parser/model offline tests; no live DB apply test.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 13: Login and Account

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:167);phase **Phase 7 — Accounts और Operations**.

Original description/subtasks:

- सुरक्षित login/account, profile और order history।

- mode बदलने पर login/account न खोएँ।

**HISTORICAL REPORT — tracker evidence:** login/register/me PASS; brute-force rate limit added (Task 16)

Markdown tracker implementation/evidence field: Historical login/register/me and rate-limit test reports.

Markdown remaining/dependency field: OTP login not implemented; outside existing verified scope.

XLSX implementation evidence: Login/register/me source and rate-limiting reports preserved.. Remaining/subtasks: OTP login not implemented; email/password remains current auth flow.. XLSX reported status: COMPLETED. Reported tests: Historical runtime/security test evidence.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 14: Seller/Shop/Restaurant Panel

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:173);phase **Phase 7 — Accounts और Operations**.

Original description/subtasks:

- shop panel में products, prices, availability और orders।

- restaurant partners के लिए menu, item prices, availability और food orders।

- मौजूदा सुविधा को reuse करें।

**HISTORICAL REPORT — tracker evidence:** seller products JSX syntax error fixed; seller orders + status change PASS; header overflow fixed

Markdown tracker implementation/evidence field: Existing seller/restaurant/admin panel source; BATCH-02 seller form and order UI E2E report.

Markdown remaining/dependency field: Task 5 measured seller UI runtime still separately pending.

XLSX implementation evidence: Seller/shop/restaurant panels retained; seller UI source exists.. Remaining/subtasks: Task 5 measured seller UI runtime remains a separate pending gate.. XLSX reported status: COMPLETED. Reported tests: Historical seller UI E2E report.. Dependencies/blockers: Expo runtime. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 15: Admin Panel

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:181);phase **Phase 7 — Accounts और Operations**.

Original description/subtasks:

- admin controls, shop/restaurant management, catalog, orders और announcements।

- role permissions जाँचें।

**HISTORICAL REPORT — tracker evidence:** New /api/admin/dashboard + Overview tab, Referrals tab exposed, announcement edit (validated PATCH), web confirm dialogs fixed; RBAC 401/403 tests PASS; UI E2E PASS

Markdown tracker implementation/evidence field: Admin dashboard/referrals/announcement edit/RBAC source and historical UI/API tests; Iteration 3 improves refund feedback.

Markdown remaining/dependency field: No full admin runtime retest in current environment.

XLSX implementation evidence: Admin dashboard/referrals/announcement/RBAC source retained; refund feedback improved.. Remaining/subtasks: Full admin runtime not available here.. XLSX reported status: COMPLETED. Reported tests: Historical admin E2E + current admin TSX syntax transpile.. Dependencies/blockers: Expo runtime. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 16: Backend, Database and Security

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:189);phase **Phase 8 — Backend, Security और Payments**.

Original description/subtasks:

- authentication, authorization, validation, secrets, API access और database rules audit।

- sensitive keys frontend/public repository में न हों।

- user/order data और permissions सुरक्षित हों।

- backup/restore strategy जाँचें; बिना test के backup को recoverable न बताएं।

**HISTORICAL REPORT — tracker evidence:** Production CORS guard rejects missing/wildcard origins in production; auth/RBAC and password reset source contracts pass. Password reset email depends on SMTP.

Markdown tracker implementation/evidence field: Security headers/rate limits retained; production CORS guard rejects missing/wildcard origins in production; password-reset/RBAC source contracts pass.

Markdown remaining/dependency field: Phone OTP inactive; no logout-all/all-session revocation endpoint found; SMTP delivery, restore drill, external audit and deployed CORS verification pending.

XLSX implementation evidence: Production CORS guard rejects missing/wildcard origins in production; auth/RBAC and password-reset source contracts pass. Password-reset email depends on SMTP.. Remaining/subtasks: Phone OTP inactive/unconfigured; no logout-all endpoint/server-side all-session revocation found; SMTP delivery, restore drill, deployed CORS verification and external security audit remain pending.. XLSX reported status: PARTIAL. Reported tests: Production CORS contract tests PASS; auth/RBAC/password-reset source contracts PASS; no deployed config/SMTP/OTP/logout-all runtime.. Dependencies/blockers: SMTP/OTP config, disposable DB, deployment config and external audit.. Runtime verified that batch: No.

JSON remaining: Phone OTP is not active/configured; no logout-all endpoint/server-side all-session revocation was found. SMTP delivery, restore drill, deployed production CORS verification and external security audit remain pending.;blockers: —.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 17: Payments and Notifications

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:199);phase **Phase 8 — Backend, Security और Payments**.

Original description/subtasks:

- payment status, order status, settlement और refunds।

- provider terms के अनुसार gateway fees समझें।

- push/in-app notifications और backend integration।

- paid integrations या production activation से पहले अनुमति लें।

**HISTORICAL REPORT — tracker evidence:** Grocery Razorpay gate requires explicit enablement and both server-side keys; offline feature-gate contracts pass. Restaurant refund/payment source safeguards retained.

Markdown tracker implementation/evidence field: Razorpay source remains gated; new offline tests verify explicit Grocery feature flag and both server-side keys are required.

Markdown remaining/dependency field: No TEST keys/provider calls; native payment sheet and automatic Grocery refunds pending; push requires Firebase/native build.

XLSX implementation evidence: Grocery Razorpay gate requires explicit enablement and both server-side keys; offline feature-gate contracts pass. Restaurant payment/refund source safeguards retained.. Remaining/subtasks: No Razorpay TEST provider calls, native payment sheet/build, live payment/cancellation/refund/webhook synchronization or push-provider verification.. XLSX reported status: PARTIAL. Reported tests: Feature gate and offline payment/refund contracts PASS; provider not called.. Dependencies/blockers: Owner-approved TEST credentials + native build + disposable DB/mock provider.. Runtime verified that batch: No.

JSON remaining: No Razorpay TEST credentials/provider calls, native payment sheet/build, live payment/cancellation/refund/webhook synchronization or push-provider verification.;blockers: —.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 18: Testing and Bug Fixes

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:211);phase **Phase 9 — Testing और Launch**.

Original description/subtasks:

- customer, seller, restaurant, admin और order workflows test करें।

- UI, navigation, API, database और errors जाँचें।

- fix के बाद retest करें।

- read-only audit के दौरान बिना अनुमति implementation न करें।

**HISTORICAL REPORT — tracker evidence:** All 24 prior offline source-contract failures individually reconciled; 333/333 pass across 52 offline test files; focused 63 pass; Python compileall PASS; 89 TS/TSX syntax transpiles with 0 diagnostics.

Markdown tracker implementation/evidence field: QA reconciliation: 63 focused tests and 333/333 broad offline tests pass; Python compileall PASS; 89 TS/TSX syntax transpiles with 0 diagnostics.

Markdown remaining/dependency field: Full backend collection, semantic typecheck, web build, Expo/MongoDB/provider/native tests remain blocked; 24 prior failures were reconciled.

XLSX implementation evidence: All 24 prior offline source-contract failures individually reconciled; 333/333 pass across 52 offline files; focused 63 pass; Python compileall PASS; 89 TS/TSX syntax transpiles with 0 diagnostics.. Remaining/subtasks: Full backend runtime collection blocked by 3 missing /app/frontend/.env collection errors; typecheck blocked by missing node_modules/expo base config; web build blocked by missing Expo CLI; MongoDB/provider/device runtime pending.. XLSX reported status: PARTIAL. Reported tests: 52-file offline suite 333 PASS/0 FAIL; focused 63 PASS/0 FAIL; compileall PASS; TS syntax 89/0; full runtime/typecheck/build blocked.. Dependencies/blockers: Preview env, Expo dependencies/CLI, MongoDB replica set, Razorpay TEST and device.. Runtime verified that batch: No.

JSON remaining: Full backend runtime collection blocked by 3 missing /app/frontend/.env collection errors; typecheck blocked by missing node_modules/expo base config; web build blocked by missing Expo CLI; MongoDB/provider/device runtime pending.;blockers: —.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 19: Production Build and Launch

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:221);phase **Phase 9 — Testing और Launch**.

Original description/subtasks:

- production readiness, configuration, secrets, backup, monitoring और deployment checklist।

- deployment, paid resources या irreversible actions से पहले मेरी स्पष्ट अनुमति।

- recurring costs पहले बताएँ।

**HISTORICAL REPORT — tracker evidence:** NOT FOUND

Markdown tracker implementation/evidence field: Not started by owner instruction.

Markdown remaining/dependency field: Needs explicit owner approval, production secrets, deployment and cost approval.

XLSX implementation evidence: No production build or launch performed.. Remaining/subtasks: Requires explicit owner approval, production secrets, deployment and cost approval.. XLSX reported status: BLOCKED. Reported tests: Blocked by owner policy.. Dependencies/blockers: Owner approval + production setup. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 20: Smart Notification System

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:231);phase **Phase 10 — Advanced Features**.

Original description/subtasks:

- push और in-app notification center।

- order status, offers/promotions, price changes, restocks और app announcements।

- admin announcement approval/targeting और sensible frequency।

- app बंद होने पर push के लिए provider setup, user permission और backend integration जरूरी।

- test के बिना working न बताएं।

**HISTORICAL REPORT — tracker evidence:** In-app notification center, read/read-all and unread-count endpoints remain present; offline contracts distinguish in-app from unconfigured native push.

Markdown tracker implementation/evidence field: In-app notification center, unread count, read/read-all and scoped notifications historically tested.

Markdown remaining/dependency field: Push delivery not configured; Firebase config and native build needed.

XLSX implementation evidence: In-app notification center, read/read-all and unread-count endpoints remain present; offline contracts distinguish in-app from unconfigured native push.. Remaining/subtasks: Native push delivery and token registration/refresh require Firebase configuration and native build.. XLSX reported status: PARTIAL. Reported tests: In-app notification source contracts PASS; push provider explicitly not configured.. Dependencies/blockers: Firebase configuration + native build.. Runtime verified that batch: No.

JSON remaining: Native push delivery and token registration/refresh require Firebase configuration and native build.;blockers: —.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 21: Smart Price Comparison

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:243);phase **Phase 10 — Advanced Features**.

Original description/subtasks:

- एक ही product की अलग-अलग shops में तुलना।

- सही match: brand, pack size, weight, unit और variant।

- उपलब्ध matching offers में सबसे कम verified price पहले highlight करें; अन्य offers भी दिखाएँ।

- stock, distance/delivery और last-updated time तभी दिखाएँ जब वास्तविक data उपलब्ध हो।

- checkout पर price और stock फिर verify करें।

- local shops के Excel/CSV data का उपयोग।

- third-party retailer live API/feed के लिए अनुमति और वास्तविक access जरूरी है; केवल registration से access न मानें।

- external data sources की licensing/access जाँचें; reference data को actual local shop price न कहें।

**HISTORICAL REPORT — tracker evidence:** Price-comparison source and exact master-variant/approved in-stock offer contracts retained; no runtime claim.

Markdown tracker implementation/evidence field: Comparison UI styles and customer shopping workflow source preserved.

Markdown remaining/dependency field: Linked-master comparison endpoint runtime test and distance data pending.

XLSX implementation evidence: Price-comparison source and exact master-variant/approved in-stock offer contracts retained; no runtime claim.. Remaining/subtasks: Live linked-master comparison endpoint and trusted distance/location data remain unverified.. XLSX reported status: PARTIAL. Reported tests: Offline source contracts PASS; live endpoint and distance data not tested.. Dependencies/blockers: Catalog master linkage + trusted location/distance source.. Runtime verified that batch: No.

JSON remaining: Live linked-master comparison endpoint and trusted distance/location data remain unverified.;blockers: —.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

### Original Task 22: Home Services Logo/Icon and Tile Integration

**SOURCE VERIFIED(definition)**: [project-reports/memory/COME-IN-MASTER-ROADMAP.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md:261);phase **Phase 10 — Advanced Features**.

Original description/subtasks:

- Home screen पर Home Services tile/icon को मुख्य theme से match करें।

- पहले जाँचें कि existing Home Services flow/destination है या नहीं।

- working flow हो तो reuse करें; duplicate न बनाएँ।

- flow न हो तो gap बताकर implementation से पहले अनुमति लें।

**HISTORICAL REPORT — tracker evidence:** home-services-card tile visible on Home

Markdown tracker implementation/evidence field: Existing report and home-services tile source/evidence.

Markdown remaining/dependency field: No new work required.

XLSX implementation evidence: Home Services tile/icon source and historical evidence retained.. Remaining/subtasks: No new work required.. XLSX reported status: COMPLETED. Reported tests: Historical home tile evidence.. Dependencies/blockers: —. Runtime verified that batch: No.

Related source files:original roadmap does not give a per-task file manifest. Recorded paths,when provided by trackers/reports,are retained in the quoted evidence above and structured task JSON;no source-to-task mapping is invented. Current implementation status is **UNVERIFIED by this investigation**.

## 6. Tasks 23–27 Historical References

These are later implementation-report labels,not additional canonical main tasks. Names are document titles,not replacements for original roadmap names.

| Historical label | Exact recovered report title | Record/status/test claim | Classification |
|---:|---|---|---|
|23|Customer Order Tracking Audit & Targeted Fix Report|COME-IN-TASK23-ORDER-TRACKING-REPORT-2026-10-30.md;claims COMPLETE—TRACKING VERIFIED AT SOURCE LEVEL;33 passed0.83s,explicitly no running authenticated API/Mongo test.|SOURCE VERIFIED(document);HISTORICAL REPORT(result)|
|24|Repeat Order Audit & Targeted Fix Report|COME-IN-TASK24-REPEAT-ORDER-REPORT-2026-10-30.md;claims COMPLETE—REORDER VERIFIED AT SOURCE LEVEL;66 passed0.60s.|SOURCE VERIFIED(document);HISTORICAL REPORT(result)|
|25|Out-of-Stock Replacement Audit Report|COME-IN-TASK25-REPLACEMENT-REPORT-2026-10-30.md;INCOMPLETE—ISSUES REMAIN;no replacement implementation in this pass.|SOURCE VERIFIED(document);HISTORICAL REPORT|
|25|Customer-approved Order Replacement Design Review|COME-IN-TASK25-REPLACEMENT-DESIGN-REVIEW-2026-10-30.md;DESIGN REVIEW READY—IMPLEMENTATION PAUSED FOR BUSINESS/PAYMENT DECISIONS.|SOURCE VERIFIED(document);CONFLICTING RECORDS vs completed canonical tracker|
|25|Replacement Implementation Decision Report|COME-IN-TASK25-REPLACEMENT-IMPLEMENTATION-REPORT-2026-10-30.md;INCOMPLETE—PAYMENT/REFUND SAFETY BLOCKER;source unchanged.|SOURCE VERIFIED(document);HISTORICAL REPORT|
|26|TASK DETAILS NOT RECOVERED|No qualifying available document/source filename/task-number match.|NOT FOUND|
|27|TASK DETAILS NOT RECOVERED|No qualifying available document/source filename/task-number match;user recollection not enough to assign a name.|NOT FOUND;UNVERIFIED recollection|

Historical Task23 report:[project-reports/COME-IN-TASK23-ORDER-TRACKING-REPORT-2026-10-30.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/COME-IN-TASK23-ORDER-TRACKING-REPORT-2026-10-30.md). Recorded source/test paths: `backend/integrations/order_notifications.py`, `backend/server.py`, `backend/tests/test_delivery_tracking_contract.py`, `backend/tests/test_task11_live_order_tracking_contract.py`, `backend/tests/test_task19_seller_admin_workflows_contract.py`, `backend/tests/test_task23_order_tracking_authorization_contract.py`, `backend/tests/test_task9_order_actions_contract.py`, `frontend/app/checkout.tsx`, `frontend/app/order-tracking.tsx`, `frontend/app/orders.tsx`, `frontend/app/restaurant/order-confirmation.tsx`, `frontend/app/restaurant/orders/[id].tsx`. File-reference presence is not runtime verification.

Historical Task24 report:[project-reports/COME-IN-TASK24-REPEAT-ORDER-REPORT-2026-10-30.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/COME-IN-TASK24-REPEAT-ORDER-REPORT-2026-10-30.md). Recorded source/test paths: `backend/server.py`, `backend/tests/test_grocery_checkout_security_contract.py`, `backend/tests/test_shopping_cart_variants_contract.py`, `backend/tests/test_task24_repeat_order_contract.py`, `backend/tests/test_task9_order_actions_contract.py`, `frontend/app/(tabs)/cart.tsx`, `frontend/app/checkout.tsx`, `frontend/app/order-tracking.tsx`, `frontend/app/orders.tsx`, `frontend/app/restaurant/cart.tsx`, `frontend/app/restaurant/checkout.tsx`, `frontend/app/restaurant/orders/[id].tsx`, `frontend/src/data/catalog.ts`, `frontend/src/data/useCatalogProducts.ts`, `frontend/src/store/cart.tsx`. File-reference presence is not runtime verification.

Historical Task25 report:[project-reports/COME-IN-TASK25-REPLACEMENT-REPORT-2026-10-30.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/COME-IN-TASK25-REPLACEMENT-REPORT-2026-10-30.md). Recorded source/test paths: `backend/server.py`, `backend/tests/test_task9_order_actions_contract.py`, `frontend/app/(tabs)/cart.tsx`, `frontend/app/chand.tsx`, `frontend/app/orders.tsx`, `frontend/src/store/cart.tsx`. File-reference presence is not runtime verification.

Task23 scope:tracking authorization/current role and live Restaurant ownership;Task24 scope:aggregate repeated product/variant rows,current catalog price/stock/availability and checkout freshness;Task25 scope:customer-approved replacement design,stock/price/refund/additional-payment constraints and business approval. Detailed original report bodies remain intact. Restaurant and Grocery restrictions in those historical reports are not new policies in this audit.

## 7. Tasks 28–30 Recovery Results

| Number | Result | Evidence classification |
|---:|---|---|
|28|**TASK DETAILS NOT RECOVERED**|NOT FOUND within available project/ZIP/tracker/spreadsheet/Git scope|
|29|**TASK DETAILS NOT RECOVERED**|NOT FOUND within same scope|
|30|**TASK DETAILS NOT RECOVERED**|NOT FOUND within same scope|

No placeholder features or speculative task names created. No recovered30-task count asserted. Task26/27 likewise unrecovered. Original owner notes/chat exports/older absent archives may contain more records;their absence here is not evidence of nonexistence.

## 8. Duplicate / Conflicting Task References

- Canonical Task10=Live Tracking;later Task10 report=Payments/Refunds/Notifications. Canonical Task11=Order Help and Refund Status;later Task11 report=Live Order Tracking.
- Canonical Task17=Payments and Notifications;later reports15–17 divide Razorpay checkout,native integration plan and build feasibility.
- Canonical Task18=Testing and Bug Fixes;later Task18=Cart Variants,Stock,Checkout.
- Canonical Task19=Production Build and Launch;later Task19=Seller/Admin Workflows.
- Canonical Task20=Smart Notification System;later Task20=Product Catalog,Variants,Stock.
- Canonical Task21=Smart Price Comparison;later Task21=Customer Shopping/Buy Now. Do not count a customer-shopping report as completed price comparison.
- Canonical Task22=Home Services Logo/Icon and Tile Integration;later Task22=Checkout Audit.
- Later Task23/24/25 reference tracking/repeat/replacement while original roadmap already defines those scopes under10/8/9. This is a recorded overlap,not a renumbering performed now.
- Main tracker summary14COMPLETED/7PARTIAL/1BLOCKED puts Task5 in PARTIAL,but its Markdown row says COMPLETED;JSON Task5 and spreadsheet retain PARTIAL/older provisioning states. The14Nov continuation tracker explicitly acknowledges this conflict. No status overwritten.
- Canonical Task9 COMPLETED in trackers vsTask25 audit/design/decision documents INCOMPLETE/implementation paused. Chronology/scope may explain parts,but current replacement acceptance is not proven by a tracker label;**CONFLICTING RECORDS** retained.
- Canonical Task5 name also has later parenthetical Fixed-Pack+Loose/Measured extensions;original base name kept unchanged in recovered list. Later tracker Task22 shortens its name;original full name retained.

Existing reconciliation (not authored by this audit):
[reports/audit/previous-handoff-package-2026-11-12/PROJECT_HISTORY/ADDITIONAL_LIBRARY_ARTIFACTS/COME_IN_MASTER_TASK_TRACKER.md](/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/reports/audit/previous-handoff-package-2026-11-12/PROJECT_HISTORY/ADDITIONAL_LIBRARY_ARTIFACTS/COME_IN_MASTER_TASK_TRACKER.md:45). It explicitly distinguishes implementation-report numbering;its original mapping table is preserved,not merged into this report's canonical numbering.

## 9. Historical Completion Claims

Recovered tracker summary claims14COMPLETED,7PARTIAL,1BLOCKED,total22. Markdown rows/status updates and JSON/XLSX are not perfectly synchronized;do not recompute current completion percentage from those claims. Task23/24 report only source-level verification;Task25 reports no safe completed replacement implementation.18Nov continuation reports much newer local regression/payment/source work but still BLOCKED native/provider/production gates. None of these histories supplies an original30-task roadmap or makes Task26–30 recoverable.

No app implementation is re-audited in this task. “SOURCE VERIFIED” for a roadmap definition does not upgrade historical implementation to current PASS. Tests were not rerun.

## 10. Test Evidence Found

- Task23 report records33 source-contract tests passed in0.83s,not API/Mongo E2E. Task24 records66 source-contract tests passed in0.60s. These result statements are HISTORICAL REPORT evidence;fresh execution not claimed.
- Original XLSX/JSON trackers contain per-task verification strings retained in Section5/structured recovery JSON;several say historical/runtime-not-verified.
- Persisted JUnit/log artifacts exist under root evidence:18Nov backend-final-v2.xml has564 cases=558PASS6SKIP,live-regression-final.xml70PASS,payment-local.xml78PASS. Other focused/local/native-adapter/browser logs are indexed. Found XML includes Task23/24 named source-contract cases;their interpretation must stay tied to that test's scope,not whole-task acceptance.
- Latest external-validation evidence:25 focused upload checks and12 localHTTP checks passed after an8-failure reproduction. These are release/security histories,not roadmap recovery tests.
- Actual tests executed THIS investigation:none. Only read-only ZIP CRC/hash and document consistency checks executed. No TypeScript/ESLint/backend/browser/native/provider suites rerun.

Detailed existing-result index:[existing-test-evidence-index.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/existing-test-evidence-index.json). Counts overlap across histories;do not sum as unique tasks/tests.

## 11. ZIP Backup Inventory and Integrity

- Available ZIP:`/workspace/come-in-current/COME-IN-COMPLETE-MASTER-SOURCE-20261115.zip`;size **5,484,042bytes**;SHA256 **`3233dcd9c8f1997b06035fd5cd7b458ab511658faf25e184044b17aec624d28c`**;read-only `zipfile.ZipFile.testzip()` **PASS**,bad member=None;646members/646regular files.
- Classification:**complete available application-source consolidation**,not only a helper/transfer bundle:frontend+backend+scripts+infra+docs/reports present. This does not prove all original workspace/history/production data are included. Packaging report explicitly disclaims complete original workspace/Git history.
- Roadmap/tracker/report/history matching ZIP member paths:266;full list in [archive-inventory.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/archive-inventory.json). Eight roadmap/tracker members compared against current app copies;all preserved matches recorded in [archived-roadmap-provenance.json](/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z/archived-roadmap-provenance.json). No extraction/replacement/write to ZIP performed.

Important archived roadmap/tracker members:
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/COME_IN_MASTER_TASK_TRACKER.json` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/COME_IN_MASTER_TASK_TRACKER.md` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/COME_IN_MASTER_TASK_TRACKER.xlsx` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/MASTER_BACKUP_EVIDENCE/HISTORICAL_DOCUMENT_VERSIONS/COME-IN-MONGODB-PHASE2-WORK/COME_IN_MASTER_TASK_TRACKER.md` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/MASTER_BACKUP_EVIDENCE/HISTORICAL_DOCUMENT_VERSIONS/COME-IN-MONGODB-STEP1-DEV-20261115/COME_IN_MASTER_TASK_TRACKER.md` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/MASTER_TASK_TRACKER.md` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/project-reports/memory/COME-IN-MASTER-ROADMAP.md` —current copy byte match:True.
- `COME-IN-COMPLETE-MASTER-SOURCE-20261115/reports/audit/previous-handoff-package-2026-11-12/PROJECT_HISTORY/ADDITIONAL_LIBRARY_ARTIFACTS/COME_IN_MASTER_TASK_TRACKER.md` —current copy byte match:True.

Historical-only ZIP references (bytes unavailable in current search scope,so integrity/size/checksum claims below are NOT freshly verified):

| Historical ZIP name | Recorded information / source | Current classification |
|---|---|---|
|COME-IN-MASTER-COMPLETE-TASK5-MONGODB_2026-11-11 2.zip|Tracker primary-source SHA256 `9d871f9f04551017a5322a275ddbd63a353f2ed24d13be9cd57831d9c27738f6`|HISTORICAL REPORT;original ZIP NOT FOUND|
|COME-IN-MONGODB-STEP1-FINAL-SOURCE-CHECKPOINT-20261115.zip|Consolidation report SHA256 `5f7253bb61d5d6ebd9e404ba9f9ab7e159082cb43cae123c22c47926ad910071`,620 source files reportedly copied|HISTORICAL REPORT;original ZIP NOT FOUND|
|COME-IN-TASK23-POST-CHANGE-20261030T081012Z.zip|Referenced by Task25 baseline audit;prior CRC claim|HISTORICAL REPORT;original ZIP NOT FOUND|
|COME-IN-TASK24-POST-CHANGE-20261030T082300Z.zip|Task25 design report records4,132,820bytes,SHA256 `95ff21fc79742836cc4eb67a7751fb26eecb7b8b1580d658099a0004cebc68bd`,prior CRC PASS|HISTORICAL REPORT;original ZIP NOT FOUND|
|COME-IN-FINAL-PREVIEW-READINESS-2026-10-18.zip|Roadmap dated evidence appendix candidate source|HISTORICAL REPORT;original ZIP NOT FOUND|

These are selected provenance references,not an assertion that they are all historical archives ever created. No absent ZIP labeled newest/authoritative by filename alone. Available Nov15 consolidation is the uploaded source snapshot;strongest roadmap-definition evidence is its actual22-task document,not package naming.

## 12. Missing Records and Unresolved Questions

- No original30-task list,Task26/27 definition,orTask28–30 names/descriptions recovered.
- Full original development history/earlier Codex workspace/private chat/export and referenced original historical ZIPs unavailable. This bounds completeness of recovery,not project functionality.
- Undated roadmap base cannot be authenticated as earliest-ever original. Its explicit22-task structure is verified;creation date/authoring provenance is UNVERIFIED.
- Current completion of conflicting canonicalTask5/9 and other tasks needs a later separately authorized reconciliation,not this read-only task.
- Earliest clearly date-labelled available reports:15Oct2026 `REPLIT_PREVIEW_READINESS_REPORT_2026-10-15.md` and `SHOPPING_THEME_FINAL_VERIFICATION_2026-10-15.md` (the latter explicitlyDate15Oct). This is the earliest demonstrably dated document in the scanned filename inventory,not earliest-ever project activity. Roadmap base may be older but is undated.
- Latest pre-investigation substantive report:18Nov2026 `EXTERNAL_VALIDATION_REPORT.md`,05:41:49.811034−08,with five continuation checkpoint updates. Latest original packaged consolidation:15Nov2026. Latest Git upload commit:15Nov2026. Filesystem/ZIP packaging timestamps are not used as original roadmap authorship proof.

## 13. Evidence-Based Conclusion

**Original30-task roadmap found? No,NOT FOUND in available scope. Original document main-task count?22.22-task list found?Yes,SOURCE VERIFIED.**

**23–27?**23=Customer Order Tracking Audit & Targeted Fix;24=Repeat Order Audit & Targeted Fix;25=Replacement audit/design/implementation decision (multiple titles/statuses preserved);26/27=TASK DETAILS NOT RECOVERED. **28–30?TASK DETAILS NOT RECOVERED.**

**Duplicates/conflicts?Yes:**separate implementation numbers,reused scope,unsynchronized tracker statuses. No merge/renumber/rename performed. **Oldest/newest?**Dated available reports15Oct/latest pre-audit external report18Nov;original roadmap creation time unknown. **Strongest original-roadmap evidence?**Archived byte-matching `project-reports/memory/COME-IN-MASTER-ROADMAP.md`,explicit22-task rule,list and Restaurant subtask restriction.

**Enough information for Phase1/Task2?**Enough for a user-approved next verification based on the recovered22-task definition and explicit unknowns. Not enough to assert30 tasks or verify missing26–30. Task2's exact scope is not supplied in this request and must not be invented. This investigation is COMPLETE only within the documented search boundary;missing original records remain NOT FOUND,not “recovered”.

## 14. Recommended Next Step: Phase 1, Task 2

Stop for user review of this report. If the user approves,follow their specified Task2 scope;preserve recovered numbering and keep historical claims separate from implementation/test verification. If30-task provenance is required,the needed artifact is an original owner roadmap/chat export or an absent historical archive containing actual task definitions—not new inferred features. **Task2 has NOT been started.**

Evidence directory:/workspace/come-in-current/evidence/roadmap-recovery-20261118T141512Z. All five checkpoint documents updated with a documentation-only recovery entry and read-verified. Original app/source/ZIP/patch protected hashes checked;no source/runtime operation. Commands used:rg file/text discovery,Git status/branch/log,stdlib file/hash/JSON/XML/XLSX reading and ZIP.testzip (no extraction). No install/build/test/provider/DB/service operation performed.
