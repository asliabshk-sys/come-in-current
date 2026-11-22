# SEC-01 Independent Design and Diff Review

Recorded 2026-11-19T21:41:20.449828+05:30 (Asia/Kolkata).

Current server SHA-256: `70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`. Existing transaction helper SHA-256: `b22cfd46e59d405cdaabf7585f6ec0a68a298cae718c8aea70f369bbfa06ba30`.

**Result: PASS — bounded static design/diff review only.** Runtime fix acceptance and owner approval are not inferred.

| Area | Status | Evidence |
| --- | --- | --- |
| Scope | PASS | Only reset_password changes among434top-level ASTnodes;imports/helper/models/routes outside it remain unchanged. |
| Fast invalid/replayed path | PASS | Original unused/unexpired preflight and400response precede bcrypt;this remains an optimization,not an authorization/claim guarantee. |
| Conditional claim | PASS | find_one_and_update filters original_id,digest,usedFalse andfresh expiry then marks used within the supplied session. Installed Motor/PyMongo return_document defaultsFalse(BEFORE). |
| Account binding | PASS | Target account ID comes from claimed token document,not client input or stale preflight account data. |
| Atomic account write | PASS | users.update_one uses the same session;matched_count must equal1or raisesHTTP400,causing transaction abort/token rollback. |
| Concurrency | PASS | Both contenders write the same token document;one can commit,other aborts/retries and must fail the used/expiry condition. Runtime proof remains the test owner responsibility. |
| Failure/retry | PASS | Password and used marker share one transaction;callback failure rolls both back. Existing helper manages TransientTransactionError whole-callback retry and UnknownTransactionCommitResult commit-only retry. |
| Retry-safe hash/time | PASS | bcrypt hash computed once outside callback;fresh now computed inside each callback retry,rechecking token expiry. |
| No unsafe fallback | PASS | No sequential/no-transaction fallback added. Unsupported transaction environments fail rather than accept partial writes. |
| Response compatibility | PASS | Successful reset dict and existing invalid/expired400response remain;no endpoint/model/schema/UI changes. |
| Other findings | PASS | SMTP,JWT/session,rate-limit,bcrypt,admin behavior source nodes remain byte-equivalent in AST;no fixes to other findings. |

Only `reset_password` changes among434top-level ASTnodes. No protected source was modified by this reviewer;no application tests or DB operations were run. The source change is performed by the parent under the owner authorization.

The missing-user check is part of requiring the claimed token and password write to succeed together. The SMTP configuration defect,JWT revocation,rate limit,bcrypt and admin findings remain outside the patch.

A final unrecoverable/uncertain commit can still produce a transport error;the acceptance criterion is coupled durable state and no duplicate overwrite,not accepting a reused token or fabricating an idempotent success response.

Runtime tests should force both preflight reads before claiming,inject failures on both sides of the user write,exercise transient transaction/unknown commit handling,and recheck expiry/replay. Do not place a two-party barrier after successful transactional claims,which can deadlock behind Mongo write conflict.

Task1remains under owner review;this report does not approve or close it.

## Independent focused runtime-evidence review

Recorded 2026-11-19T21:51:15.906745+05:30 (Asia/Kolkata).

**PASS — saved runner/assertions/receipts inspected independently; no tests rerun by this reviewer.**

| Evidence | Before | After |
| --- | --- | --- |
| Twenty focused cases | 10 PASS / 10 FAIL | 20 PASS / 0 FAIL |
| Strengthened distinct-password cases06/07 | 0 PASS / 2 FAIL | 2 PASS / 0 FAIL |

JSON and XML totals agree. Source and runner hashes bind each before/after execution; all after receipts match current server SHA-256 `70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`.

The wrappers forward actual Motor sessions. Strict fault assertions inspect the real records after transaction abort, require both password and token unchanged, then test a clean retry and replay rejection. Unknown-commit injection first performs the real commit, then raises a labelled acknowledgement error; the after receipt requires two commit calls with one callback, one token write and one user write. Transient failure separately requires callback retry with exactly one prepared hash.

Concurrency holds preflight reads, not successful transactional claims. The stronger two-way case has one success and one exact invalid-reset400; each of three eight-way rounds has one success and seven exact400responses. In every round, the stored hash authenticates only the request that actually succeeded. Distinct synthetic passwords remain below72UTF-8bytes, so the unrelated bcrypt finding does not contaminate the assertion.

The stronger cases are refinements of existing06/07, not two additional unique focused cases. V1 artifacts remain preserved. The old30 compatibility harness diff was also inspected; failure instrumentation follows the changed operation order without weakening the original no-partial-state invariant.

Limits: focused auth-rate control is stubbed only in the harness; the broader old30 suite covers the unchanged rate behavior. These are actual function/model + real disposable Mongo tests, not fullHTTP/middleware or actual network-outage/standalone-server tests. No runtime result closes other security findings or grants owner approval.

**Review frozen. No protected source/report/checkpoint was modified by this reviewer; only this new review document and its JSON were appended.**
