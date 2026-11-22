# SEC-05 / SEC-09 isolated candidate correction report

COME-IN Phase1 Task1. Recorded 2026-11-20T12:11:24.328512+05:30 (Asia/Kolkata). Production source remains owned by the parent merge workflow;this workstream changed only a new isolated candidate and new evidence.

**Same27tests:before10PASS/17FAIL/0ERROR/0SKIP → candidate27PASS/0FAIL/0ERROR/0SKIP.** Both source hashes and the identical runner hash were checked against JSON and JUnit. The tests write only retained unique disposable loopbackMongoDB databases;no production/customer data,provider/native execution,global failpoint or database drop.

## SEC-05 — MEDIUM — candidate PASS

Original finding:anonymous `/api/status` POST accepted unbounded diagnostic names and shared GET exposed the feed. Candidate keeps both routes and response shape but uses existing `require_role("admin")` for each. Anonymous receives401;customer/shopkeeper/delivery partner403. Existing public `/api/` health remains200/read-only. Admin status create/read remain200. `StatusCheckCreate.client_name` now requires1..256characters;missing/empty/257characters reject422before storage. Response `StatusCheck` remains unchanged,so a prior300-character stored record still reads successfully for an admin. No old diagnostic rows are deleted or truncated.

This is the owner-authorized minimum security boundary;no diagnostic UI or business route is removed. Retention and upstream ingress policies are not newly certified by these tests. ASGI identity is supplied through a clearly synthetic authentication dependency;the actual source role dependency and handler/model bodies execute. Full JWT/production-ingress acceptance belongs to root integration/security work.

## SEC-09 — MEDIUM — candidate PASS

Before-source count-then-write race is now reproduced on realMongoDB,not merely a collection double. Tests hold old nontransactional count reads before writes;two/four already privileged admins then cross-demote each other and leave zero admins. This remains a controlled local schedule with synthetic accounts,not a production attack or privilege escalation.

Candidate initializes a dedicated `security_locks` control document `_id="admin-role-mutations",version=0` safely. A duplicate initial-upsert race is tolerated only when the expected guard record exists. Inside the unchanged `run_transaction` helper it first increments that shared guard,then rereads the actor as a currentadmin,reads the target,checks last-admin count,writes the role and reads the response using the same session. A competing transaction must retry on the shared document;merely wrapping independent user documents/counts in snapshot transactions would not suffice.

The current actor check rejects an already-demoted in-flight actor403. Existing self-demotion409,target404,legitimate customer→shopkeeper updates and customer→admin promotions remain. All response password fields stay excluded. User data/schema is not migrated;one related metadata collection/document is added with the implicit unique `_id` index. A deployment using restrictive collection grants must grant this normal control-document access;no production permission/configuration was changed here.

Both two-admin and four-admin tests run with the guard initially absent and already present. After candidate execution every cohort retains at least one admin;no generic500or duplicate-upsert failure occurs. A fault after the real user write rolls back user role and guard version;clean retry succeeds. Transaction-session unavailability fails closed. Tests do not barrier the transactional count read,because correct serialization would deadlock such a test;the invariant and actual persisted roles are checked after all concurrent calls instead.

## Exact candidate delta and evidence

- `server.candidate.py`:full isolated source copy,only `StatusCheckCreate`, `create_status_check`, `list_status_checks`, `admin_update_user_role` differ.
- `SEC05_SEC09_CANDIDATE.patch`:complete source patch for parent review/sequential merge.
- `candidate-metadata.json`:AST-node scope;noimports changed;SEC-01reset function unchanged.
- `roles-before.json/xml/log`, `roles-after.json/xml/log`:all27cases,commands,timestamps,source/runner hashes,real-Mongo observations and54retained database names.
- `SEC05_SEC09_RESULTS.json`:machine-readable final summary.
- `validate_roles_diagnostics.py`:same executable intended-invariant runner for both source states.

Before sourceSHA256:`70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`.

Candidate sourceSHA256:`f054bfb4a25004ac334514ef6c67fa47cd800715a2df0919dc6c85c9e1b3fbcf`.

RunnerSHA256:`a64b60a947f0edb8c5208e8924f9652bf32d7c4da1f31fad1e0521ebac9f1186`.

No original reports/checkpoints/ZIPs,application source,other security finding,UI/schema migration,dependency or Git history was modified by this workstream. Android,iOSand actualRazorpayvalidation remainDEFERREDand were not executed.

Next:parent merges the four-node candidate,then reruns actual-source integration/regression. Candidate success alone is not Task1owner approval or a claim production has already changed. No tests remain running.
