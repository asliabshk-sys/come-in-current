# Task 9 external approval packet

| Dependency | Who signs or runs it | Exact evidence required | Current technical state |
| --- | --- | --- | --- |
| CA guidance, T9-46 | Assigned verified CA or tax professional | Case-specific written treatment, original reference, correction type and approved financial/tax values. | Internal preflight preserves the review snapshot. |
| Numbering and issuance, T9-48 | Authorized statutory issuer and separate Admin after CA review | Issuer identity, applicable sequence scope and format, issuance/reversal rules and approval references. | Internal draft only. Statutory number allocation and issuance remain disabled. |
| Razorpay TEST, T9-20, T9-23–26, T9-50 | Payment integration owner and authorized TEST operator | Separately authorized sandbox session, approved collection/refund rules, linked order/capture/refund records, signed webhook replay and independently confirmed TEST outcomes. | Local adapter and fixtures passed. No external execution. Use authorized secret configuration without entering credentials in this record. |
| Object storage regression | Infrastructure owner and test operator | Disposable storage namespace with authorized test access. Run object create/read/cleanup and supply redacted output for the skipped case. | External object storage remains unavailable in the local suite. |
| Android/iOS, T9-50 | Release owner and authorized device tester | Approved test builds on physical Android/iOS, scoped fixture accounts and recorded checkout, replacement and failure behavior. | Chromium evidence is available. Physical device validation remains deferred. |

- Policy or dependency ____________________
- Evidence reference, environment and date ____________________
- Authorized validator or professional signature ____________________
- Result and outstanding conditions ____________________

For T9-36, the identity/fraud integration owner must provide authorized evidence of referral attribution and validated fraud signals, including false-positive handling for shared households. Supply a redacted fixture report and sign the same record above. The local referral safeguards remain in force.
