"""Pure helpers for safe, bounded provider refund accounting.

Amounts in provider refund records are integer paise. Failed refunds do not
consume the captured amount; pending and completed refunds do.
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def amount_to_paise(value) -> int:
    try:
        amount = Decimal(str(value))
        if not amount.is_finite() or amount <= 0:
            raise InvalidOperation
        paise = int((amount * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        if paise <= 0:
            raise InvalidOperation
        return paise
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("Invalid eligible refund amount") from None


def summarize_provider_refunds(refunds, eligible_paise: int) -> dict:
    if isinstance(eligible_paise, bool) or not isinstance(eligible_paise, int) or eligible_paise <= 0:
        raise ValueError("Invalid eligible refund amount")
    if not isinstance(refunds, (list, tuple)):
        raise ValueError("Invalid provider refund list")

    seen = set()
    consumed_paise = 0
    pending_paise = 0
    completed_paise = 0
    normalized = []

    for refund in refunds:
        if not isinstance(refund, dict):
            raise ValueError("Invalid provider refund record")
        refund_id = refund.get("id") or refund.get("refund_id")
        status = str(refund.get("status") or "").lower()
        amount = refund.get("amount")
        if not isinstance(refund_id, str) or not refund_id or refund_id in seen:
            raise ValueError("Missing or duplicate provider refund ID")
        seen.add(refund_id)
        if status not in {"pending", "processed", "refunded", "failed"}:
            raise ValueError("Unknown provider refund status")
        if isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid provider refund amount")
        normalized.append({"id": refund_id, "status": status, "amount": amount})
        if status == "failed":
            continue
        consumed_paise += amount
        if status == "pending":
            pending_paise += amount
        else:
            completed_paise += amount

    if consumed_paise > eligible_paise:
        raise ValueError("Provider refunds exceed the eligible captured amount")

    if consumed_paise == 0:
        state = "not_refunded"
    elif pending_paise:
        state = "refund_pending"
    elif consumed_paise == eligible_paise:
        state = "refunded"
    else:
        state = "partially_refunded"

    return {
        "eligible_paise": eligible_paise,
        "consumed_paise": consumed_paise,
        "pending_paise": pending_paise,
        "completed_paise": completed_paise,
        "remaining_paise": eligible_paise - consumed_paise,
        "status": state,
        "refunds": normalized,
    }
