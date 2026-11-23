# CA evidence index

- Retained `backend/server.py`: `_replacement_original_financials`, `_invoice_review_snapshot`, `_replacement_financial_review_details`, and `create_replacement_invoice_correction_draft`.
- Retained `backend/refund_rules.py`: captured amount and refund-event arithmetic.
- [Prior tax snapshot and approval controls](../closure-evidence-20261123/IMPLEMENTATION.md)
- [COD reconciliation and refund evidence](../partial-cod-refund-20261123/AUDIT.md)
- [Existing approval handoff](../TASK-9-APPROVAL-HANDOFF.md)
- [Fresh local invoice review check](focused.log), command `python -m pytest -q -n 0 --tb=short backend/tests/test_task9_restaurant_replacement.py` from retained source with disposable MongoDB.
