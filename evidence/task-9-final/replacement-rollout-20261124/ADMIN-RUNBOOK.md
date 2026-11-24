# Admin legacy migration enrollment

## Before rollout

Use an authorized Admin account and obtain explicit authorization for the environment and the specific Grocery or Restaurant case IDs. Verify the approved deployment includes the migration lifecycle patch and subsequent enrollment review patch. Use the existing operational backup and restore process for the order, notification, support and financial audit collections. Record a rollout owner and the review window. This runbook authorizes no enrollment by itself.

## Review and enroll

1. In Admin → Food support, select the order mode and enter the existing order ID and replacement case ID.
2. Select **Review legacy migration eligibility**. This read-only check shows the selected offer counts and the reason for exclusion or ambiguity. Use **Load legacy migration status** for campaign-wide counts of previously recorded cases. Ambiguous records are a subset of campaign exclusions. A selected-offer check does not scan other orders.
3. Enroll only a case shown as eligible and within the approved list. Route ambiguous records to Admin/COME-IN Assist. Leave excluded and already-enrolled records alone.
4. Review the customer notice. The existing offer stays on its old terms for 24 hours from the saved notice. Activation rechecks eligibility and starts a fresh 15-minute expiry only when the migrated offer and activation notice are saved successfully.
5. Select **Confirm enrollment and notify customer**. The server requires explicit confirmation and rechecks eligibility inside the existing transaction. The campaign view should show the enrollment in grace. Verify the audit includes the Admin ID, case and order IDs, timestamp, confirmation, notice time and grace deadline.
6. After grace, reconcile every approved case to migrated, excluded or pending retry. For migrated cases, compare the recorded activation time with the expiry and verify the additional notice. Keep excluded cases in review. Repeating a confirmed request for the same case returns its existing record.

## Recovery

- If confirmation times out, reload the selected case and campaign status before retrying. Do not start a new campaign or resend notices manually. Enrollment is idempotent by case.
- If activation fails, inspect recent events and the recorded failure. The worker delays retries while preserving the original offer and rolling back partial activation and notices. Keep the campaign evidence and resolve the underlying store failure.
- To halt rollout, stop new enrollment immediately. If pending activations also need a pause, coordinate with the deployment operator to stop the migration processor on all workers using the existing deployment controls. Do not edit deadlines or delete audit records. Reconcile existing customer notices and grace deadlines before resuming. Keep timed offers on a compatible deployment until they resolve.
- Never use payment or refund tools as migration recovery. Escalate any payment discrepancy through established Assist procedures.

No live cases were reviewed, enrolled or migrated during this verification.
