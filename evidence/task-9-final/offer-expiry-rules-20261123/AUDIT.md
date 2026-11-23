# Offer expiry rules — scoped audit

**Overall: PARTIALLY VERIFIED.** GitHub work and local HEAD initially matched `ba5d4059777ea01f737332d35d4bebe1f55b3878`. T9-12 replacement-offer expiry and independent cancellation remain **NOT IMPLEMENTED** pending owner decisions. Existing dated coupon, advertisement and membership windows are separate controls.

| Area | Status | Findings |
| --- | --- | --- |
| A. Dates and terms | VERIFIED | Promotion drafts require dates with offsets and expiry strictly after start. Advertisement dates now require offsets, an ordered window and the existing maximum of 90 days. UTC timestamps retain the same instant. Accepted commercial terms and historic data were preserved. No default duration was added. |
| B. Server time | PARTIALLY VERIFIED | Backend uses server time for eligibility, with inclusive start and exclusive end. Offset normalization and exact coupon boundary were verified. Client time affects local quote presentation only and cannot grant eligibility. Distributed clock skew and device-specific daylight-saving display were not tested. |
| C. Checkout enforcement | VERIFIED | Existing Grocery coupons are rechecked in quote and final checkout. The budget write independently checks the active date window. At the cutoff, checkout rejects the stale quote and rolls back. Existing UI prompts for a fresh quote and total review. No alternate total is applied silently. |
| D. Cart and delayed payment | PARTIALLY VERIFIED | Cart/open quotes carry no reservation of coupon validity. A pre-expiry quote cannot commit an expired redemption. Grocery coupons are supported only in approved cash channels. Online pending/delayed-payment coupons, offer stacking and replacement-offer deadlines remain outside the approved flow. |
| E. Pause, resume and closure | VERIFIED | Pausing does not change dates, valid campaigns can resume, expired or closed coupons cannot resume. Scheduled date filters control availability. Restart preserves paused status and rejects resume beyond the stored deadline. |
| F. Coupon and promotion expiry | VERIFIED | Existing campaign/customer caps, one-time budget consumption, refund review and eligible unpaid cancellation release were preserved. Release after expiry does not reactivate the campaign. |
| G. Ads and membership | PARTIALLY VERIFIED | Ad publication and resume require an unexpired window, existing CHAND evidence and designated Admin approval. Active filtering and UTC serialization apply to scheduled and expired ads. Membership eligibility tests cover the original expiry gate and retained search/placement checks. Extensions and device display were not added. |
| H. Audit and notices | PARTIALLY VERIFIED | Existing pause/resume/closure and redemption audit remain in force. Checkout presents a re-quote error. No scheduled expiry event or expiry reminder was added. |
| I. Database and recovery | PARTIALLY VERIFIED | A forced expiry at spend time rolls back order, stock, quote claim and audit. Existing competing-checkout and duplicate-redemption tests passed. Restart preserved the paused campaign, reconciliation, and single eligible cancellation release. No new background expiry processing or storage rewrite. |

**DEFERRED — POST ALL APP TASKS**. Physical Android/iOS, genuine Razorpay TEST payment/webhook/refund validation and external provider validation. No money or credits moved.
