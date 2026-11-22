# COME-IN Task 2 — Execution Checklist

**Task:** Theme and Design / official app icon integration
**Started:** 22 November 2026 (Asia/Kolkata)
**Starting Git commit:** `3aa855ac9913a1b7c1b3c8c535c569f477c42f01`
**Status:** APPROVED — owner approved completed local scope on 22 November 2026; deferred validation remains separate.

## Scope and restrictions

- Preserve the existing yellow/forest-green/pale-mint design system, navigation, Grocery Mode, Restaurant Mode, CHAND behavior, APIs, authentication and backend.
- Use only the owner-reference icon artwork already present in the retained source. Do not recreate, substitute or redesign it.
- Fix only a confirmed UI/theme/icon defect. No defect has been confirmed in the first static audit.
- Do not begin Task 3, deploy, use production data/credentials, or represent a source/config check as native-device validation.

## Milestones

- [x] Recover `origin/work`; branch/remote starting SHA matched and worktree was clean.
- [x] Locate owner-reference artwork and verify byte identity of icon derivatives.
- [x] Inspect Expo Android/iOS/web icon configuration and adaptive-icon requirements.
- [x] Complete initial static UI/theme route audit.
- [x] Run direct local TypeScript, ESLint and Expo configuration checks.
- [x] Inspect available frontend test/visual-regression evidence and run only safe relevant checks.
- [x] Finalize Task 2 audit/report, remaining limitations and owner-review checklist.
- [x] Save final checkpoint, commit/push and remote-verify (`e738824`).
- [x] Owner approved the completed local scope on 22 November 2026; see `docs/TASK_2_OWNER_APPROVAL_RECORD_20261122.md`.
- [ ] Native Android/iOS and full runtime visual validation — explicitly deferred to final project-wide testing.
- [ ] Task 3 authorization — required separately; Task 3 must not start automatically.

## Current verification result

- Official icon asset and its Android adaptive/web derivatives are byte-identical: SHA-256 `9373ba8487c00eedd3bfa5a449fbc803582ca5663165aad85f88172baf6ca72f`.
- `app.json` maps the official asset to Expo `icon`, Android `adaptiveIcon.foregroundImage`, and web `favicon`. iOS inherits Expo `icon`.
- Direct local `tsc --noEmit`: PASS (0 errors).
- Direct local `eslint .`: PASS (0 errors, 7 warnings). Warnings are existing hook-dependency advisories and were not suppressed or changed.
- `expo config --type public` with CI/telemetry disabled: PASS; resolved Android, iOS and web icon paths. It is a source/configuration result, not a native build/device result.

See `evidence/task-2-theme-icon-20261122/TASK_2_ICON_AND_UI_AUDIT_REPORT.md` for evidence, limitations and the audit inventory.

Final evidence: `evidence/task-2-theme-icon-20261122/TASK_2_FINAL_REPORT.md`. Fresh web export passed; static inventory covered 53 route/layout files and had 0 parse diagnostics; CHAND planner passed 11 assertions. No Task 2 application source change was justified or made.
