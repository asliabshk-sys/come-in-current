# Replacement expiry implementation audit — 24 November 2026

Starting local and independently queried GitHub work HEAD matched `81fcdbfbc74cc5c47d27bfde46cc1ee7893d0fd7`. The working tree was clean. The owner approved a 15-minute default, configurable Admin bounds, successful customer availability as the start, and sequential Grocery/Restaurant offers.

Existing report routes store ordered candidate options and the reporting timestamp on the order. The current UI displays all options together. Existing rejection ends the proposal; staff can refresh. These behaviors conflict with the required one-at-a-time re-offer progression for newly issued offers. Historical offers and accepted Assist intent require protection. Existing offer decisions may create pending financial reviews without changing money.

The supported durable delivery mechanism is a customer-scoped in-app notification written inside the same Mongo transaction as the order. Start at its successful persistence in that transaction, with the offer and notice visible together on commit. A notification write failure must roll back the offer and deadline. Push is unconfigured. No claim of device receipt will be made.

Use the existing option order with current price, availability, ownership and total checks. Re-offering does not change the order or authorize payment. Exhaustion opens Assist. An explicitly chosen eligible item-removal flow remains separate. Preserve already-issued cases without deadlines and protect accepted, dispatched and financially pending consent from automatic expiry. No retroactive migration is authorized by this increment. Independent manual cancellation remains separate from the expiry and re-offer requirements.

Only 15 minutes is specified initially. Admin must explicitly configure numeric minimum/maximum limits before changing the default or adjusting a live deadline. No commercial bounds have been inferred.
