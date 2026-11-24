# Razorpay TEST verification

**Provider-backed tests are BLOCKED.** The app environment had no Razorpay mode, public key, private key or webhook secret set. The retained source has example configuration only. Values were not printed or saved. No request went to Razorpay and no financial transaction occurred.

Provision a nonproduction deployment with `APP_ENV=test`, `RAZORPAY_MODE=test`, a server-side `RAZORPAY_KEY_ID` from the TEST dashboard, the matching server-side `RAZORPAY_KEY_SECRET`, and `RAZORPAY_WEBHOOK_SECRET` matching the TEST webhook configuration. Supply these through the authorized secret store. Configure a reachable nonproduction webhook endpoint and use synthetic orders and documented Razorpay TEST instruments. Production configuration and actual customer instruments are outside scope.

With those prerequisites, record TEST order creation, success and failure, signed webhook processing and replay, refund request and confirmation where supported, and stale payment-state rejection. Reconcile each provider transaction and local audit against the same synthetic order. The replacement-specific flow remains pending review for protected paid orders and must not start unsupported charges or refunds.

Offline suites exercise the environment boundary, webhook validation, replay/idempotency, refund and replacement collection safeguards. These results do not establish provider connectivity or a successful TEST payment.
