# Task 9 final checkpoint

Initial audit on 23 November 2026 confirmed clean work and GitHub HEAD `6ab5d8ad98568df50c088965487de0fd2d1e991b`. The existing register accounts for 50 policies.

The verified initial audit commit is `bd7db0614ce8427ab2694487cfe9a73e0c71940c`. Restore the tested application change by applying `patches/task9-final-contract-binding.patch` after `patches/task9-closure-evidence-gates.patch`. Changed retained source files are `backend/server.py` and `backend/tests/test_task9_restaurant_replacement.py`. No transport, schema or write capability was added. Task 8, Task 21 and the original archive have no direct diff.

Final disposition is **PARTIALLY VERIFIED**. See the [50-policy execution matrix](final-campaign-20261123/POLICY-EXECUTION-MATRIX.md), [approval handoff](TASK-9-APPROVAL-HANDOFF.md), and [fresh evidence](TASK-9-TEST-EVIDENCE.md).

The implementation milestone was independently verified at `08888cae3489c8e3a5508545a29b3ca40e37c54a` on GitHub. Final regression after the corrected test fixture recorded 707 passes and one external object-storage skip. The closing evidence commit contains the full logs.

### Approval-readiness checkpoint

Baseline `06ab688c4c2474600b1fbe9cc851115756351b38` matched GitHub `work`. Apply `patches/task9-approval-stage-regression.patch` after the final contract binding patch. It changes only `backend/tests/test_task9_restaurant_replacement.py`. Existing funding and execution gates remain in force. [Dashboard](approval-readiness-20261123/APPROVAL-DASHBOARD.md)

### Coupon funding and channels — 23 November 2026

T9-41–43 remain **PARTIALLY VERIFIED**. Existing COME-IN-funded Grocery cash controls passed fresh tests including release rollback, wrong-order release, paid-order denial and Admin reconciliation after restart. Commercial expansion awaits explicit approval. [Decision record](coupon-funding-20261123/OWNER-DECISION.md) · [Tests and commands](coupon-funding-20261123/TESTS.md)

### Advertisement compensation — 23 November 2026

Advertisement compensation remains **PARTIALLY VERIFIED**. Campaign status and audit writes are atomic, identical status replays are deduplicated, and inactive campaigns cannot record events. Compensation eligibility and execution remain disabled pending explicit approval. [Audit](advertisement-compensation-20261123/AUDIT.md) · [Owner decisions](advertisement-compensation-20261123/OWNER-DECISION.md) · [Tests](advertisement-compensation-20261123/TESTS.md)

### Delivery Partner Allocation — 23 November 2026

Delivery Partner Allocation remains **PARTIALLY VERIFIED**, and T9-30 settlement remains **BLOCKED**. Existing onboarding and Admin fee controls passed; no order assignment or partner payable is enabled. [Audit](delivery-partner-allocation-20261123/AUDIT.md) · [Owner decisions](delivery-partner-allocation-20261123/OWNER-DECISION.md) · [Tests](delivery-partner-allocation-20261123/TESTS.md)
