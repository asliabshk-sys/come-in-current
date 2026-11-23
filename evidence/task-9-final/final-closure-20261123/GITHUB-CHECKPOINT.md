# GitHub checkpoint

Branch `work`, repository `asliabshk-sys/come-in-current`. Verified baseline and staged checkpoints:

| Milestone | Local and independently queried GitHub work SHA at verification |
| --- | --- |
| Prompt 6 baseline | `6c27683d17a96402490d27b889ed180bc904c0c3` |
| Stage 7 CA packet | `6579d0a6ec6b6462addcff89274b45551b8ab168` |
| Stage 8 partial policy and invoice consistency | `bc5bd1fab71b5620c6ef657a5a893a6547adff66` |
| Stage 9 replacement expiry decision | `0669dceb3500c50d8728d0fec81756049cb9820b` |
| Stage 10 blocked and deferred register | `0abaa8fe4521424777b5fb57beec1485b905deb2` |
| Stage 11 integration | `520766af41cfa2cb88442346841e4f692217d3f0` |

Stage 12 is the commit containing this file. Verify its self-reference with `git log -1 --format=%H -- evidence/task-9-final/final-closure-20261123/GITHUB-CHECKPOINT.md`. Compare local HEAD and origin/work with `git ls-remote origin refs/heads/work`, check `git rev-list --left-right --count HEAD...origin/work`, and confirm `git status --short` is empty.
