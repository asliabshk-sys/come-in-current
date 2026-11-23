# Coupon funding and channels — decision record

**T9-41, T9-42 and T9-43 remain partially verified.** This is a proposal pending signature. The existing authorization covers nonstacking coupons funded 100% by COME-IN for signed-in Grocery cash checkout. It includes configured campaign dates, audience, shop/product/category eligibility, minimum eligible spend, campaign and customer limits, and eligible unpaid cancellation release when the campaign explicitly opts in.

| Decision | Existing rule and recommendation | Exact approval required for expansion |
| --- | --- | --- |
| Funding ownership | Keep COME-IN as the sole enabled funder. Draft seller and advertiser shares are configuration only. | Identify legal payer and campaign per share, specify a total of 10,000 basis points, who backs unpaid funding, when liability starts, invoice evidence and settlement owner. Require signed funding parties and finance confirmation. |
| Channels | Keep Grocery COD and supported cash-at-shop/pickup. Restaurant, online redemption and coupon stacking stay disabled. | Specify eligible modes, fulfillment, payment methods, customer audience, merchant/product scope, terms, and reservation-to-spend timing per channel. For online payment define failure, expiry, capture and idempotent restoration. |
| Limits | Keep server-enforced campaign budget, discount cap, per-customer budget, redemption limits and validity. Open quotes currently consume no campaign funds. | Supply approved budget, benefit type and values, per-order/customer and redemption caps, dates, any pending reservation expiry and exhaustion behavior. |
| Refund and cancellation costs | Restore an opted-in eligible unpaid Grocery cancellation exactly once. Keep paid refunds and partial returns under review. Preserve accepted benefits under existing rules. | State which funder bears each cost, allocation by refunded item and amount, whether any balance is restored, and what evidence and approvals are needed. Specify merchant/platform treatment, customer notice and reversal idempotency. |
| Pause and close | Pause blocks checkout with an equivalent open quote; active can resume inside the valid window. Closure is terminal. Prior receipts and eligible unpaid releases remain available. | Confirm existing behavior or specify exact treatment of already accepted orders, open quotes and any future online reservations. Define who may approve lifecycle changes and the required audit reason. |

**Impact**. Keeping the current scope preserves existing customer discounts and budget controls. Expansion would introduce financial posting, settlement and support obligations. No new liability or automatic refund policy follows from this record.

**Tests following approval**. Cover funding ownership and caps, mode and payment eligibility, concurrency, failure after spending or release, partial and full refunds, duplicate provider events, pause/close races, immutable reconciliation and restart.

- Decision(s), approved wording and exclusions ____________________
- Campaign/funding agreement reference and effective date ____________________
- Owner name, signature and date ____________________
- Finance and funding party co-approval, if applicable ____________________
