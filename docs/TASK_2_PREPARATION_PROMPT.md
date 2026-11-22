# COME-IN — Canonical Task 2 Preparation Prompt (Do Not Execute Until Authorized)

Repository: `asliabshk-sys/come-in-current`
Branch: `work`
Prerequisite: the owner has explicitly approved Phase 1 / Task 1 and separately authorized this Task 2 execution.

First fetch `origin/work`, inspect the five checkpoint files plus `docs/COME_IN_MASTER_TASK_BOARD.md`, and verify that local `HEAD` equals `origin/work`. Preserve all existing changes. Do not begin if Task 1 is still `REVIEW PENDING`.

**Task 2 — Theme and Design**

Original objective: maintain a clean, consistent, mobile-friendly UI using the established yellow, forest-green and pale-mint shopping theme, rounded cards, readable text, subtle shadows and consistent spacing.

Allowed scope: inventory the existing design-system/theme sources; identify concrete approved visual consistency or accessibility defects; make the smallest necessary visual corrections; test only affected UI surfaces; preserve CHAND, Restaurant Mode, Grocery Mode, existing navigation and business behavior.

Excluded: redesigning screens, changing product decisions, backend/API/auth/database work, native Android/iOS validation, Razorpay TEST/provider work, production deployment, and dependency/framework upgrades without separate approval.

Required evidence: exact source paths and rationale for each change, before/after screenshots or reproducible UI evidence when available, focused regression output, preserved external-validation limitations, updated checkpoints/handover/task board, reviewed diff without secrets, commit and non-force push to `origin/work`, then fetch and verify zero ahead/behind plus a clean tree.

Stop and request direction if the proposed change would alter navigation, business workflow, Restaurant Mode, payment behavior, authentication, public API, database schema, or requires unavailable device/provider/production resources.
