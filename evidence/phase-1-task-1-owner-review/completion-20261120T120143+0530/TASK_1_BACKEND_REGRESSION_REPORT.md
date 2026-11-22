# Backend regression report

## Final source-bound runs

| Suite | Result |
|---|---|
| Offline backend/contracts, guarded | 578 PASS, 2 SKIPPED |
| Legacy isolated HTTP/Mongo | 23 PASS, 1 SKIPPED |
| SEC-01 focused | 20 PASS |
| SEC-01 distinct concurrency | 2 PASS |
| Auth/JWT/bcrypt/SMTP | 25 PASS |
| Proxy/rate limiting | 27 PASS |
| Role/diagnostics | 27 PASS |
| Payment/webhook local mocks | 30 PASS |

The offline suite initially found one legitimate inventory expectation after adding the `security_locks` control collection (52 vs 51). The test was corrected to assert 52 and explicitly require `security_locks`; the complete rerun passed 578/2.

A broad unscoped attempt is retained separately: 560 PASS, 26 SKIP, 17 ERROR from absent preview server, /app frontend path and import environment. It was not a source regression and is not included in final totals.

Skipped: two environment/opt-in cases in offline scope; one external object-storage case in legacy scope. No production DB/provider was used; disposable databases were retained.
