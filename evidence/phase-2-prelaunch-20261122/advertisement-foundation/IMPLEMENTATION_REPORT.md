# Phase 2 — Advertisement Foundation

**Status:** IN PROGRESS — first implemented, locally verified vertical slice.

## Implemented

- Seller-owned campaign drafts with bounded title, destination, placement, and a maximum 90-day campaign window.
- A dedicated advertisement-poster upload path. It verifies authenticated ownership, MIME/signature consistency, a 2 MB maximum, and bounded raster dimensions before object storage.
- Restricted CHAND metadata review abstraction. If the provider is not configured, it returns `NOT_CONFIGURED` and the campaign stays unpublished; it never fabricates a safe decision.
- Final publication is designated-owner-only, requires a completed `safe` CHAND recommendation and the exact reviewed poster SHA-256, and is auditable. Ordinary administrators may reject, pause, or remove campaigns but cannot publish them.
- Public active-campaign endpoint, authenticated daily impression/click de-duplication, and Mongo index declarations.
- Seller Account entry and native/web poster-selection UI. This is the only new image-upload entry point introduced by this milestone.

## Source patch

`patches/phase2-advertisement-foundation.patch` applies cleanly to the verified Phase 2 baseline and reverses cleanly from the isolated implementation checkout.

## Fresh checks

| Command | Result |
|---|---|
| `PYTHONPATH=backend /workspace/come-in-tools/py311/bin/python -m pytest -q backend/tests/test_phase2_advertisement_contract.py backend/tests/test_catalogue_chand_adapter.py` | PASS — 10 passed |
| `./frontend/node_modules/.bin/tsc -p frontend/tsconfig.json --noEmit` | PASS — 0 TypeScript errors |
| `cd frontend && ./node_modules/.bin/eslint app/seller/advertisements.tsx 'app/(tabs)/account.tsx' src/lib/api.ts` | PASS — 0 errors/warnings |
| `patch --dry-run --forward ...phase2-advertisement-foundation.patch` and reverse dry-run | PASS |
| `expo export --platform web` | BLOCKED in this isolated environment: Expo attempted to create `/home/agent/.expo`, which is unavailable to the sandbox. This is an environment failure, not a successful export claim. |

## Explicit limitations / next work

- No CHAND provider credential was used. Real provider review remains deferred until owner-configured credentials and authorized validation exist.
- The deployment must set `ADVERTISEMENT_OWNER_EMAIL` to the designated owner-admin account before any campaign can be published. Without it, publication is safely forbidden.
- No native Android/iOS or real user/device validation was performed.
- The legacy general image-upload route and existing customer CHAND vision UI predate this work. They conflict with the new Phase 2 application-wide “advertisement-only image upload” policy and require an explicit compatibility/migration decision before disabling them; they were not silently broken in this slice.
- Membership, pricing, verification, delivery performance, complaints, analytics, and admin UI integrations remain Phase 2 work in progress.
