# Task 9 financial policy framework

Baseline GitHub Work commit `788702c945c58e08b580f808fbd087ceca2f9f79`. Apply `patches/task9-financial-policy-framework.patch` after the approved financial policies patch. Forward and reverse patch checks passed.

- Collection and refund decisions use server-side amounts, a matching customer decision, Admin authorization, an immutable audit record and a transactional in-app notification. A positive collection quote is revalidated when the customer accepts. Review can result in rejection or approval pending execution. Existing payment references are preserved. The route does not call any provider or mark execution complete.
- Admin can assign a historical tax case to an active, independently verified account with the dedicated professional role. Professionals can see and decide only their assigned cases, through the restricted queue on the existing Admin route. The server audits assignment and access. A separate Admin still reviews the professional decision. No statutory document generator or automatic tax correction was introduced.
- Admin can save validated draft configurations for six coupon categories and reward campaigns. Drafts include funding, budget, per-customer caps, eligibility, validity and terms. Submission replays reuse an identical draft, and the audit is written in the same transaction. Drafts have no checkout effect. The suite checks concurrent duplicate drafting and invalid budgets. It does not exercise redemption, budget spending, or exhaustion because no active redemption path is connected.
- Existing finalized order accounting, seller payout controls, membership reporting, referral attribution, and reward protection remain. Delivery partner payout and new recognition for advertising and other revenue were outside the safe execution scope without authoritative inputs and approvals.

Changed source is `backend/server.py`, the Restaurant Task 9 integration test, database inventory contract, Admin support, CHAND, the shared replacement component and the auth role type. One new configuration collection, `financial_policy_drafts`, separates draft policy from financial transactions and uses MongoDB's built-in identifier uniqueness only. Existing collections, indexes and issued documents remain intact. Task 8, Task 21 and the Master ZIP were preserved.

**Task 9 — PARTIALLY COMPLETE.** [Decision register](DECISION_REGISTER.md)

## Verification

[Focused tests](focused.log) · [Full regression](full.log) · [TypeScript](typescript.log) · [ESLint](lint.log) · [Expo export](expo.log) · [Chromium](browser.log) · [Browser script](browser-smoke.py)

Native Android, iOS and genuine Razorpay TEST payment, webhook and refund checks are deferred.

Final verification recorded 61 focused passes and 695 full backend passes with zero failures. The sole skip was the external object-storage check. TypeScript, targeted ESLint, Expo web export and the Chromium flows passed.
