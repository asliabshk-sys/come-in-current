# Task 4 Git baseline and verification method

- `git fetch origin work`, `git status --porcelain=v2 --branch --ignored`, `git rev-list --left-right --count HEAD...origin/work` and `git ls-remote origin refs/heads/work` verified the clean start on 784dd21fa7395029a8a78674b1fe8327d9318dcb with zero ahead/behind.
- The Task 4 evidence and restoration change are saved in the commit introducing this file. Use the commit log and GitHub branch query to verify its identity. After the push, use `git fetch origin work`, `git status --porcelain=v2 --branch`, and compare `git rev-parse HEAD` to `git ls-remote origin refs/heads/work`.
