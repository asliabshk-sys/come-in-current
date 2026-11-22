# Task 4 source inventory

205 literal method/path declarations mapped from `backend/server.py`. No duplicate exact method/path pairs. Dynamic registration and full navigation behavior are outside this static count.

| Method | Route | Handler | Line |
|---|---|---|---:|
| GET | `/` | `root` | 705 |
| POST | `/status` | `create_status_check` | 723 |
| GET | `/status` | `list_status_checks` | 730 |
| POST | `/auth/register` | `register` | 967 |
| POST | `/auth/login` | `login` | 1002 |
| GET | `/referrals/me` | `referral_dashboard` | 1016 |
| POST | `/referrals/home-banner-claim` | `claim_first_home_referral_banner` | 1042 |
| GET | `/referral/validate` | `validate_referral` | 1058 |
| GET | `/referral` | `open_referral` | 1065 |
| GET | `/admin/referrals` | `admin_referrals` | 1075 |
| PATCH | `/admin/referrals/{referral_id}/review` | `admin_review_referral` | 1082 |
| PATCH | `/admin/referral-rewards/{reward_id}` | `admin_update_referral_reward` | 1129 |
| GET | `/auth/me` | `me` | 1174 |
| PATCH | `/auth/me` | `update_me` | 1184 |
| POST | `/auth/password/forgot` | `forgot_password` | 1282 |
| POST | `/auth/password/reset` | `reset_password` | 1298 |
| POST | `/uploads/image` | `upload_image` | 1374 |
| POST | `/advertisements` | `create_advertisement` | 1454 |
| GET | `/advertisements/mine` | `my_advertisements` | 1471 |
| POST | `/advertisements/{advertisement_id}/poster` | `upload_advertisement_poster` | 1476 |
| POST | `/advertisements/{advertisement_id}/chand-review` | `review_advertisement_with_chand` | 1506 |
| GET | `/admin/advertisements` | `admin_advertisements` | 1520 |
| PATCH | `/admin/advertisements/{advertisement_id}` | `decide_advertisement` | 1525 |
| POST | `/owner/advertisements/{advertisement_id}/publish` | `owner_publish_advertisement` | 1535 |
| GET | `/advertisements/active` | `active_advertisements` | 1553 |
| GET | `/shops/{shop_id}/membership` | `shop_membership` | 1599 |
| GET | `/shops/{shop_id}/membership/history` | `membership_history` | 1607 |
| POST | `/shops/{shop_id}/membership/purchase` | `request_membership` | 1618 |
| POST | `/shops/{shop_id}/membership/payment-intent` | `create_membership_payment_intent` | 1649 |
| POST | `/shops/{shop_id}/membership/payment-verify` | `verify_membership_payment` | 1696 |
| PATCH | `/admin/memberships/{membership_id}` | `admin_membership_decision` | 1778 |
| POST | `/shops/{shop_id}/membership/refunds` | `request_membership_refund` | 1876 |
| GET | `/shops/{shop_id}/membership/refunds` | `seller_membership_refunds` | 1918 |
| GET | `/admin/membership-refunds` | `admin_membership_refunds` | 1925 |
| GET | `/admin/membership-refunds/{payment_id}` | `membership_refund_details` | 1940 |
| PATCH | `/admin/membership-refunds/{payment_id}` | `decide_membership_refund` | 1970 |
| POST | `/admin/membership-refunds/{payment_id}/{operation}` | `execute_membership_refund` | 2100 |
| POST | `/admin/membership-outages` | `record_membership_outage` | 2135 |
| GET | `/admin/memberships` | `admin_memberships` | 2167 |
| GET | `/shops/{shop_id}/membership/analytics` | `seller_membership_analytics` | 2211 |
| GET | `/admin/memberships/report` | `admin_membership_report` | 2222 |
| POST | `/catalog/premium-events` | `premium_display_event` | 2307 |
| POST | `/advertisements/{advertisement_id}/events/{event_type}` | `track_advertisement_event` | 2343 |
| GET | `/uploads/{storage_path:path}` | `serve_upload` | 2359 |
| POST | `/shops` | `create_shop` | 2396 |
| GET | `/shops/mine` | `my_shop` | 2425 |
| PATCH | `/shops/{shop_id}` | `update_shop` | 2433 |
| PATCH | `/shops/{shop_id}/availability` | `set_shop_availability` | 2448 |
| GET | `/shops` | `list_shops` | 2463 |
| GET | `/shops/{shop_id}` | `get_shop` | 2500 |
| POST | `/chand/feedback` | `submit_chand_feedback` | 2545 |
| GET | `/chand/feedback/mine` | `my_chand_feedback` | 2572 |
| GET | `/admin/chand/feedback` | `admin_chand_feedback` | 2577 |
| GET | `/admin/chand/feedback/summary` | `admin_chand_feedback_summary` | 2582 |
| PATCH | `/admin/chand/feedback/{feedback_id}` | `admin_update_chand_feedback` | 2593 |
| POST | `/assistant/context` | `assistant_context` | 2608 |
| GET | `/assistant/health` | `assistant_health` | 2820 |
| POST | `/assistant/vision` | `assistant_vision` | 2839 |
| POST | `/admin/master-products` | `create_master_product` | 3013 |
| GET | `/catalog/master-products` | `search_master_products` | 3034 |
| POST | `/shops/{shop_id}/master-products/{master_product_id}/link` | `link_master_product` | 3047 |
| POST | `/shops/{shop_id}/products` | `create_product` | 3085 |
| POST | `/shops/{shop_id}/catalogue-import/jobs` | `create_catalogue_import_job` | 3151 |
| GET | `/shops/{shop_id}/catalogue-import/jobs/{job_id}` | `get_catalogue_import_job` | 3240 |
| GET | `/shops/{shop_id}/catalogue-import/jobs` | `list_catalogue_import_jobs` | 3291 |
| GET | `/shops/{shop_id}/catalogue-import/categories` | `list_catalogue_import_categories` | 3299 |
| PATCH | `/shops/{shop_id}/catalogue-import/jobs/{job_id}/records/{record_index}` | `edit_catalogue_import_record` | 3309 |
| POST | `/shops/{shop_id}/catalogue-import/jobs/{job_id}/records/{record_index}/approve` | `approve_catalogue_import_record` | 3333 |
| POST | `/shops/{shop_id}/catalogue-import/jobs/{job_id}/records/{record_index}/reject` | `reject_catalogue_import_record` | 3353 |
| POST | `/shops/{shop_id}/catalogue-import/jobs/{job_id}/bulk-approve` | `bulk_approve_catalogue_import_records` | 3369 |
| POST | `/shops/{shop_id}/catalogue-import/jobs/{job_id}/confirm-apply` | `confirm_catalogue_import_apply` | 3544 |
| POST | `/shops/{shop_id}/products/import` | `import_shop_products` | 3582 |
| GET | `/shops/{shop_id}/products/import-template` | `shop_product_import_template` | 3821 |
| GET | `/admin/catalog-import-history` | `admin_catalog_import_history` | 3833 |
| GET | `/admin/catalog-price-audit` | `admin_catalog_price_audit` | 3839 |
| GET | `/catalog/price-comparison` | `compare_master_product_prices` | 3845 |
| GET | `/admin/retail-price-import/template` | `retail_price_import_template` | 3920 |
| POST | `/admin/retail-price-import` | `admin_retail_price_import` | 3926 |
| GET | `/catalog/retail-prices` | `public_retail_prices` | 4023 |
| GET | `/admin/retail-price-import/history` | `admin_retail_price_import_history` | 4035 |
| GET | `/shops/{shop_id}/products` | `list_shop_products` | 4041 |
| GET | `/catalog/products` | `list_catalog_products` | 4114 |
| GET | `/catalog/search` | `search_catalog` | 4140 |
| PATCH | `/products/{product_id}` | `update_product` | 4172 |
| DELETE | `/products/{product_id}` | `delete_product` | 4216 |
| POST | `/grocery/measured-price` | `measured_price` | 4415 |
| POST | `/grocery/quotes` | `create_grocery_quote` | 4425 |
| POST | `/orders` | `create_order` | 4469 |
| POST | `/orders/{order_id}/confirm-upi-payment` | `confirm_grocery_upi_payment` | 4651 |
| GET | `/orders/mine` | `my_orders` | 4679 |
| POST | `/orders/{order_id}/cancel` | `cancel_grocery_order` | 4755 |
| GET | `/shops/{shop_id}/orders` | `shop_orders` | 4766 |
| PATCH | `/orders/{order_id}/status` | `update_order_status` | 4774 |
| GET | `/orders/{order_id}` | `get_grocery_order_details` | 4867 |
| GET | `/orders/{order_id}/tracking` | `get_order_tracking` | 4876 |
| POST | `/orders/{order_id}/tracking/location` | `update_order_tracking_location` | 4898 |
| POST | `/requests/anything` | `submit_request_anything` | 4933 |
| GET | `/requests/anything/mine` | `my_requests_anything` | 4953 |
| POST | `/requests/assist` | `submit_agent_assist` | 4959 |
| GET | `/admin/announcements` | `admin_announcements` | 5002 |
| POST | `/admin/announcements` | `create_announcement` | 5008 |
| PATCH | `/admin/announcements/{announcement_id}` | `set_announcement_active` | 5017 |
| GET | `/admin/dashboard` | `admin_dashboard` | 5061 |
| GET | `/announcements/active` | `active_announcements` | 5087 |
| GET | `/admin/users` | `admin_users` | 5104 |
| PATCH | `/admin/users/{user_id}/role` | `admin_update_user_role` | 5110 |
| GET | `/admin/shops` | `admin_shops` | 5159 |
| PATCH | `/admin/shops/{shop_id}/status` | `admin_set_shop_status` | 5169 |
| GET | `/admin/orders` | `admin_orders` | 5182 |
| POST | `/earnings/orders/{kind}/{order_id}/cash-collected` | `confirm_manual_cash_collection` | 5330 |
| GET | `/admin/earnings` | `admin_earnings` | 5386 |
| GET | `/admin/earnings/ledger` | `admin_earnings_ledger` | 5420 |
| GET | `/admin/earnings/transactions` | `admin_earnings_transactions` | 5431 |
| GET | `/earnings/mine` | `shopkeeper_earnings` | 5458 |
| GET | `/admin/earnings/bank-account` | `admin_platform_bank_account` | 5555 |
| PUT | `/admin/earnings/bank-account` | `save_admin_platform_bank_account` | 5560 |
| GET | `/shops/{shop_id}/bank-account` | `get_shop_bank_account` | 5565 |
| PUT | `/shops/{shop_id}/bank-account` | `save_shop_bank_account` | 5572 |
| GET | `/restaurants/{restaurant_id}/bank-account` | `get_restaurant_bank_account` | 5579 |
| PUT | `/restaurants/{restaurant_id}/bank-account` | `save_restaurant_bank_account` | 5586 |
| PATCH | `/admin/financial-policy/{kind}/{entity_id}` | `admin_set_financial_policy` | 5593 |
| GET | `/admin/earnings/settlements` | `admin_settlement_list` | 5605 |
| POST | `/shops/{shop_id}/settlements` | `request_shop_settlement` | 5612 |
| POST | `/restaurants/{restaurant_id}/settlements` | `request_restaurant_settlement` | 5660 |
| PATCH | `/admin/earnings/settlements/{settlement_id}` | `admin_settlement_decision` | 5700 |
| GET | `/admin/requests/anything` | `admin_requests_anything` | 5732 |
| GET | `/admin/requests/assist` | `admin_agent_assist` | 5738 |
| PATCH | `/admin/requests/anything/{req_id}/status` | `admin_update_request` | 5749 |
| PATCH | `/admin/requests/assist/{req_id}/status` | `admin_update_assist` | 5771 |
| GET | `/restaurants` | `list_restaurants` | 5916 |
| GET | `/restaurants/mine` | `my_restaurants` | 5938 |
| POST | `/restaurants` | `create_restaurant` | 5942 |
| GET | `/restaurants/{restaurant_id}` | `restaurant_detail` | 5956 |
| GET | `/restaurants/{restaurant_id}/serviceability` | `restaurant_delivery_serviceability` | 5963 |
| PATCH | `/restaurants/{restaurant_id}` | `update_restaurant` | 5973 |
| PATCH | `/restaurants/{restaurant_id}/availability` | `restaurant_availability` | 5985 |
| GET | `/restaurants/{restaurant_id}/menu` | `restaurant_menu` | 5997 |
| POST | `/restaurants/{restaurant_id}/menu` | `create_menu_item` | 6009 |
| PATCH | `/restaurants/{restaurant_id}/menu/{item_id}` | `update_menu_item` | 6019 |
| DELETE | `/restaurants/{restaurant_id}/menu/{item_id}` | `delete_menu_item` | 6031 |
| GET | `/addresses` | `list_addresses` | 6040 |
| POST | `/addresses` | `create_address` | 6044 |
| PATCH | `/addresses/{address_id}` | `update_address` | 6054 |
| DELETE | `/addresses/{address_id}` | `delete_address` | 6066 |
| GET | `/restaurant/cart` | `get_restaurant_cart` | 6077 |
| PUT | `/restaurant/cart` | `save_restaurant_cart` | 6096 |
| DELETE | `/restaurant/cart` | `clear_restaurant_cart` | 6111 |
| POST | `/restaurant/orders` | `create_restaurant_order` | 6116 |
| GET | `/restaurant/orders/mine` | `my_restaurant_orders` | 6189 |
| GET | `/restaurants/{restaurant_id}/orders` | `restaurant_orders` | 6196 |
| PATCH | `/restaurant/orders/{order_id}/status` | `update_restaurant_order_status` | 6201 |
| POST | `/restaurant/orders/{order_id}/cancel` | `cancel_restaurant_order` | 6235 |
| GET | `/restaurant/payments/config` | `restaurant_payment_config` | 6249 |
| POST | `/restaurant/orders/{order_id}/payment-intent` | `create_restaurant_payment_intent` | 6255 |
| POST | `/restaurant/orders/{order_id}/payment-retry` | `retry_restaurant_payment` | 6288 |
| POST | `/restaurant/payments/verify` | `verify_restaurant_payment` | 6305 |
| POST | `/restaurant/payments/razorpay-webhook` | `razorpay_webhook` | 6618 |
| POST | `/restaurants/{restaurant_id}/reviews` | `create_restaurant_review` | 6730 |
| POST | `/restaurant/support` | `create_restaurant_support` | 6751 |
| GET | `/restaurant/support/mine` | `my_restaurant_support` | 6781 |
| GET | `/seller/support` | `seller_order_support` | 6785 |
| PATCH | `/seller/support/{ticket_id}` | `seller_update_order_support` | 6807 |
| GET | `/admin/restaurant/support` | `admin_restaurant_support` | 6859 |
| PATCH | `/admin/restaurant/support/{ticket_id}` | `admin_update_restaurant_support` | 6863 |
| POST | `/admin/restaurant/orders/{order_id}/refund` | `admin_refund_restaurant_order` | 6951 |
| GET | `/admin/restaurant/orders` | `admin_restaurant_orders` | 7073 |
| GET | `/admin/restaurants` | `admin_restaurants` | 7077 |
| PATCH | `/admin/restaurants/{restaurant_id}/status` | `admin_restaurant_status` | 7081 |
| GET | `/home-services/fee-policy` | `get_home_service_fee_policy` | 7254 |
| PATCH | `/admin/home-services/fee-policy` | `set_home_service_fee_policy` | 7259 |
| GET | `/home-services/providers` | `list_service_providers` | 7296 |
| GET | `/home-services/providers/mine` | `my_service_provider` | 7311 |
| POST | `/home-services/providers` | `register_service_provider` | 7316 |
| PATCH | `/home-services/providers/{provider_id}` | `update_service_provider` | 7327 |
| PATCH | `/home-services/providers/{provider_id}/photo` | `update_service_provider_photo` | 7340 |
| POST | `/home-services/appointments` | `create_service_appointment` | 7356 |
| GET | `/home-services/appointments/mine` | `my_service_appointments` | 7385 |
| GET | `/home-services/appointments/provider` | `provider_service_appointments` | 7389 |
| PATCH | `/home-services/appointments/{appointment_id}/status` | `update_service_appointment` | 7401 |
| GET | `/admin/home-services/providers` | `admin_service_providers` | 7444 |
| PATCH | `/admin/home-services/providers/{provider_id}/approval` | `admin_approve_service_provider` | 7452 |
| POST | `/admin/grocery/orders/{order_id}/refund` | `admin_refund_grocery_order` | 7554 |
| GET | `/admin/grocery/refunds` | `admin_grocery_refunds` | 7624 |
| GET | `/grocery/payments/config` | `grocery_payment_config` | 7632 |
| POST | `/orders/{order_id}/payment-intent` | `create_grocery_payment_intent` | 7648 |
| POST | `/grocery/payments/verify` | `verify_grocery_payment` | 7771 |
| GET | `/notifications/mine` | `my_notifications` | 7927 |
| GET | `/notifications/unread-count` | `my_unread_notifications` | 7934 |
| POST | `/notifications/read-all` | `read_all_notifications` | 7939 |
| POST | `/notifications/{notification_id}/read` | `read_notification` | 7945 |
| GET | `/products/{product_id}/restock-alert` | `restock_alert_status` | 7954 |
| POST | `/products/{product_id}/restock-alert` | `subscribe_restock_alert` | 7959 |
| DELETE | `/products/{product_id}/restock-alert` | `unsubscribe_restock_alert` | 7968 |
| GET | `/delivery-partner/provider-status` | `delivery_partner_provider_status` | 8068 |
| POST | `/delivery-partner/otp/request` | `delivery_partner_otp_request` | 8080 |
| POST | `/delivery-partner/otp/verify` | `delivery_partner_otp_verify` | 8089 |
| POST | `/delivery-partner/identity/start` | `delivery_partner_identity_start` | 8094 |
| PUT | `/delivery-partner/application` | `save_delivery_partner_application` | 8099 |
| POST | `/delivery-partner/application/submit` | `submit_delivery_partner_application` | 8173 |
| GET | `/delivery-partner/application/mine` | `my_delivery_partner_application` | 8202 |
| GET | `/delivery-partner/referral` | `delivery_partner_referral` | 8210 |
| GET | `/delivery-partner/admin/applications` | `admin_delivery_partner_applications` | 8219 |
| GET | `/delivery-partner/admin/applications/{application_id}` | `admin_delivery_partner_application_detail` | 8226 |
| PATCH | `/delivery-partner/admin/applications/{application_id}` | `admin_decide_delivery_partner_application` | 8240 |
| GET | `/delivery-partner/access` | `delivery_partner_access` | 8298 |

## Expo route modules

- `frontend/app/(tabs)/_layout.tsx`
- `frontend/app/(tabs)/account.tsx`
- `frontend/app/(tabs)/cart.tsx`
- `frontend/app/(tabs)/categories.tsx`
- `frontend/app/(tabs)/index.tsx`
- `frontend/app/(tabs)/search.tsx`
- `frontend/app/+html.tsx`
- `frontend/app/+not-found.tsx`
- `frontend/app/_layout.tsx`
- `frontend/app/addresses.tsx`
- `frontend/app/admin-delivery-partners.tsx`
- `frontend/app/admin-earnings.tsx`
- `frontend/app/admin-memberships.tsx`
- `frontend/app/admin.tsx`
- `frontend/app/auth.tsx`
- `frontend/app/become-seller.tsx`
- `frontend/app/category/[slug].tsx`
- `frontend/app/chand.tsx`
- `frontend/app/checkout.tsx`
- `frontend/app/delivery-address.tsx`
- `frontend/app/delivery-partner.tsx`
- `frontend/app/index.tsx`
- `frontend/app/language.tsx`
- `frontend/app/notifications.tsx`
- `frontend/app/order-tracking.tsx`
- `frontend/app/orders.tsx`
- `frontend/app/password-reset.tsx`
- `frontend/app/payment-methods.tsx`
- `frontend/app/product/[id].tsx`
- `frontend/app/referral-dashboard.tsx`
- `frontend/app/referral.tsx`
- `frontend/app/request.tsx`
- `frontend/app/restaurant/[id].tsx`
- `frontend/app/restaurant/account.tsx`
- `frontend/app/restaurant/addresses.tsx`
- `frontend/app/restaurant/cart.tsx`
- `frontend/app/restaurant/categories.tsx`
- `frontend/app/restaurant/checkout.tsx`
- `frontend/app/restaurant/dashboard.tsx`
- `frontend/app/restaurant/index.tsx`
- `frontend/app/restaurant/menu.tsx`
- `frontend/app/restaurant/order-confirmation.tsx`
- `frontend/app/restaurant/orders/[id].tsx`
- `frontend/app/restaurant/orders/index.tsx`
- `frontend/app/restaurant/search.tsx`
- `frontend/app/restaurant/support.tsx`
- `frontend/app/retail-prices.tsx`
- `frontend/app/seller/advertisements.tsx`
- `frontend/app/seller/dashboard.tsx`
- `frontend/app/seller/help.tsx`
- `frontend/app/seller/membership.tsx`
- `frontend/app/seller/orders.tsx`
- `frontend/app/seller/products.tsx`
- `frontend/app/seller/support.tsx`
- `frontend/app/seller-earnings.tsx`
- `frontend/app/services.tsx`
- `frontend/app/shop/[id].tsx`
- `frontend/app/shops.tsx`
