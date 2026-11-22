# SEC-01–SEC-09 final dispositions

| ID | Finding | Correction | Fresh evidence | Status |
|---|---|---|---|---|
| SEC-01 HIGH | Reset token concurrency/partial write | Existing atomic claim+password transaction preserved | 20 focused + 2 distinct concurrency PASS | FIXED |
| SEC-02 MEDIUM | Password-change JWT revocation | Per-account signed password version; reset increments atomically | auth suite 25 PASS | FIXED |
| SEC-03 MEDIUM | Forwarded-IP trust | Explicit owned proxy CIDRs; malformed/universal trust fails closed | rate/proxy 27 PASS | FIXED |
| SEC-04 MEDIUM | Non-atomic auth throttles | Transactional capped IP+subject reservation; success releases captured login buckets | rate/proxy 27 PASS | FIXED |
| SEC-05 MEDIUM | Anonymous diagnostics writes/reads | Admin dependency; bounded input; public health unchanged | roles 27 PASS | FIXED |
| SEC-06 MEDIUM | bcrypt >72-byte alias | Versioned full-input prehash; short legacy hashes retained; ambiguous long legacy requires reset | auth suite 25 PASS | FIXED |
| SEC-07 MEDIUM | Blocking provider HTTP in async handlers | Existing requests calls offloaded; state ownership preserved | local mock 30 PASS | FIXED LOCALLY |
| SEC-08 LOW | Unbounded webhook raw body | 1 MiB declared/stream cap before HMAC/JSON/DB | local mock 30 PASS | FIXED LOCALLY |
| SEC-09 MEDIUM | Concurrent last-admin demotion | Shared transactional security lock and fresh role/count checks | roles 27 PASS | FIXED |

Configured-admin password rotation now uses compare-and-set and increments password version. SMTP port parsing/range failure is safely contained and undelivered reset digests are removed. Actual SMTP/provider delivery is not claimed.
