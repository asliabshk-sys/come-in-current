# Distinct-Password Concurrency Validation Addendum

COME-IN SEC-01 scoped correction — recorded 2026-11-19T16:21:00.956753+00:00 UTC.

**Result: PASS — the two strengthened existing cases pass after the fix and fail before it.** This addendum closes a specific review gap:the original focused concurrency contenders used one shared synthetic password,so the test did not independently prove that the persisted credential belonged to the successful request. Each v2contender now supplies a distinct synthetic password,with differing bytes before bcrypt's72-byte boundary. The persisted hash is verified against every contender without writing password values to artifacts.

## Preservation and scope

All v1runner,reports,JSON/XML/logs,checkpoint and hash manifest remain byte-identical;all ten recorded v1artifact hashes were rechecked. The new evidence lives only in this subdirectory. No application source/configuration/API/schema/UI or old evidence was changed by this focused-test agent. Production/customer/provider operations and database drops:zero.

Only `concurrency_two` and `concurrency_many` assertions/password fixtures were strengthened. The other18case bodies are unchanged. `main` additionally records explicit selectedcase arguments;the CLI supports running only the two relevant existing IDs. No78-case regression or original30-case security suite was repeated for this addendum. Both selected before/after runs use exactly the same v2runner bytes.

## Exact commands

Working directory: `/workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/distinct-password-concurrency`.

```sh
/workspace/come-in-tools/py311/bin/python -B sec01_focused_regression_v2.py --stage before --source /workspace/come-in-current/evidence/phase-1-task-1-owner-review/sec01-fix-20261119T213810+0530/before/backend/server.py --cases SEC01-06 SEC01-07 > focused-before.log 2>&1
/workspace/come-in-tools/py311/bin/python -B sec01_focused_regression_v2.py --stage after --source /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py --cases SEC01-06 SEC01-07 > focused-after.log 2>&1
```

Before:0PASS/2FAIL/0ERROR/0SKIP,exit1. After:2PASS/0FAIL/0ERROR/0SKIP,exit0. Same intended assertions;no suppression or expected-failure marking.

- Before source SHA-256: `a1e340dc58e2e10e9ed5283ef02220251edf3be8e2f88193becd406aaa3778db`.
- After source SHA-256: `70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07`.
- Identical v2runner SHA-256: `523d84f49dfa6072059378752f0ca6326f99e0cee511ba58556f4adca9dd7afa`.
- Unchanged transaction helper SHA-256: `b22cfd46e59d405cdaabf7585f6ec0a68a298cae718c8aea70f369bbfa06ba30`.

## Stronger winner/loser assertions

| Existing case | Before | After | Strict credential check |
| --- | --- | --- | --- |
| SEC01-06 | FAIL | PASS | Two successful preflight reads synchronize;exactlyone call succeeds,one raises existing400,and only the successful contender's password authenticates. |
| SEC01-07 | FAIL | PASS | Three separate eight-way rounds;eachhasone successful call,seven400rejections,and only its successful contender's password authenticates. |

Across the after run:26contender calls,4successes and22invalid-token400exceptions. The stored credential matches all4actualsuccessful requests at their respective round checkpoints;all22losing credentials fail authentication. These are function-level existing400exceptions,not a new HTTPtransport test.

The before run stops SEC01-07 at its first failing round;it does not claim three completed baseline rounds. Its sanitized observations retain multiple successful responses while only the final persisted credential authenticates,showing why different contender passwords improve the evidence.

Sanitized after observations(no password values):

```json
{
  "two_way_after": {
    "contenders": 2,
    "synchronized_preflight_reads": 2,
    "accepted": 1,
    "rejected400": 1,
    "successful_contender_indices": [
      0
    ],
    "authenticating_contender_indices": [
      0
    ],
    "stored_hash_matches_only_successful_contender": true
  },
  "eight_way_after_rounds": [
    {
      "round": 1,
      "contenders": 8,
      "accepted": 1,
      "rejected400": 7,
      "successful_contender_indices": [
        0
      ],
      "authenticating_contender_indices": [
        0
      ],
      "stored_hash_matches_only_successful_contender": true
    },
    {
      "round": 2,
      "contenders": 8,
      "accepted": 1,
      "rejected400": 7,
      "successful_contender_indices": [
        6
      ],
      "authenticating_contender_indices": [
        6
      ],
      "stored_hash_matches_only_successful_contender": true
    },
    {
      "round": 3,
      "contenders": 8,
      "accepted": 1,
      "rejected400": 7,
      "successful_contender_indices": [
        0
      ],
      "authenticating_contender_indices": [
        0
      ],
      "stored_hash_matches_only_successful_contender": true
    }
  ]
}
```

## Real Mongo boundary and retained evidence

Same actual AST-extracted reset/model/hash functions and unchanged existing transaction helper as the v1focused suite. Operations use real Motor sessions and the verified localhost`rs0`PRIMARY. Throttle remains an isolated no-op for this scoped suite;it does not modify/adjudicate other security findings. No .env,production credentials,SMTP/payment/refund/provider integration or global failpoints.

New before database: `comein_sec01_focused_before_20261119t161909z_192ba489`;new after database: `comein_sec01_focused_after_20261119t161932z_435beff1`. Both retained,no drops. Source bytes stayed unchanged during both tests.

Artifacts: [runner](sec01_focused_regression_v2.py), [beforeJSON](focused-before.json), [beforeJUnit](focused-before.xml), [beforelog](focused-before.log), [afterJSON](focused-after.json), [afterJUnit](focused-after.xml), [afterlog](focused-after.log), [summary](distinct-password-concurrency-summary.json), [checkpoint](SEC01_DISTINCT_CONCURRENCY_CHECKPOINT.json), [hashmanifest](distinct-artifact-hashes.json).

The two cases supersede the weaker concurrency evidence within the existing20-case focused suite;do not inflate the canonical denominator to22or aggregate the20-case suite twice. All v1artifacts remain preserved as an auditable earlier attempt. No test operation remains running or interrupted. Parent incorporates this frozen addendum into the final source-preservation/mastermanifest package;owner review/approval remains pending.
