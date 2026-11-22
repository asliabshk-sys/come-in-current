# Changed files and reasons

1. `backend/server.py` — SEC-02–SEC-09 minimum corrections plus safe SMTP configuration handling and configured-admin session revocation.
2. `backend/.env.example` — empty placeholder/documentation for explicitly owned trusted proxy CIDRs; no secret or real configuration.
3. `backend/tests/backend_test.py` — legacy fixtures aligned to required current contracts; assertions remain strict.
4. `backend/tests/test_mongo_portability_tool.py` — inventory count 51→52 and explicit `security_locks` assertion after authorized control collection.
5. `frontend/app/checkout.tsx` — complete primitive dependencies for eligibility.
6. `frontend/app/services.tsx` — prevent stale account response overwrite.
7. `frontend/src/restaurant/useDiscoveryAddress.ts` — post-await lifecycle guard and primitive account dependency.

Final SHA-256 values are recorded in the master manifest. No schema migration, UI redesign, route redesign or unrelated refactor was performed.
