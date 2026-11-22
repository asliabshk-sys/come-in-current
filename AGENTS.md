# COME-IN continuation rules

Read COME_IN_LIVE_CHECKPOINT.md, COME_IN_MASTER_TASK_TRACKER.md,
COME_IN_DECISIONS_AND_BLOCKERS.md, COME_IN_SESSION_LOG.md and
COME_IN_NEXT_SESSION_RESUME_PROMPT.md before work. Inspect Git status/branch/HEAD.
The application is retained at /workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115;
this checkout stores its original ZIP and canonical continuation checkpoints.
Use the existing isolated checkout; do not create worktrees unless requested.
Preserve application architecture, UI/theme/navigation/Restaurant Mode and user work.
Follow the phase gate in the live checkpoint; never treat historical tests as new execution.
After meaningful progress and before stopping, update all four checkpoint/tracker/log/blocker
files and the resume prompt, verify their saved contents, and report their paths.
Do not store secrets in evidence/checkpoints. Never auto-commit, push, deploy or publish.
Retain previous logs; use new run-specific evidence filenames and disposable local DBs.
MongoDB's retained container needs this correction after every start, BEFORE index work:
`docker exec --user mongodb comein-onboarding-mongo prlimit --pid 1 --nofile=16384:16384`.
The observed inherited soft nofile=1024 caused WiredTiger failure during index creation;
the existing hard limit is 16384. Do not delete databases to work around this limit.
