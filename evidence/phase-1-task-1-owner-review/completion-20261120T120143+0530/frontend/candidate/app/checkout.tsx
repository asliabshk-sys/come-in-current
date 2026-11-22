// Customer checkout — per-shop COD, pickup/cash-at-shop and UPI intent.
// Direct UPI payment is not marked paid until the shopkeeper verifies receipt.
import Feather from "@react-native-vector-icons/feather";
import { useFocusEffect, useRouter } from "expo-router";
import { useCallback, useEffect, useState } from "react";
import {
  ActivityIndicator,
  KeyboardAvoidingView,
  Linking,
  Platform,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { api } from "@/src/lib/api";
import { useAuth } from "@/src/store/auth";
import { GroceryOnlinePayment } from "@/src/components/GroceryOnlinePayment";
import { useGroceryPaymentConfig } from "@/src/lib/razorpay";
import { DELIVERY_FEE, DELIVERY_FEE_THRESHOLD, useCart } from "@/src/store/cart";
import { formatAmount, isMeasured, lineAmount } from "@/src/lib/measure";
import { storage } from "@/src/utils/storage";
import { useLocationCtx } from "@/src/store/location";
import { makeStyles, radius, spacing, useTheme } from "@/src/theme";

const DEFAULT_LOCATION = "Set delivery location";
const GUEST_SESSION_KEY = "@comein_grocery_guest_session_v1";
const IDEMPOTENCY_KEY_STORAGE = "@comein_grocery_idempotency_v1";
const makeOpaqueLocalKey = () => `${Date.now().toString(36)}-${Math.random().toString(36).slice(2)}-${Math.random().toString(36).slice(2)}-${Math.random().toString(36).slice(2)}`;
type GroceryQuote = { quote_token: string; expires_at: string; items: any[]; subtotal: number; delivery_fee: number; reward_discount?: number; total: number; currency: string; fulfillment?: "delivery" | "pickup" };

export default function CheckoutScreen() {
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const styles = useStyles();
  const { colors } = useTheme();
  const { user } = useAuth();
  const { cartLines, subtotal: cartSubtotal, deliveryFee: cartDeliveryFee, clear, clearBuyNow, unresolvedKeys, buyNowLine } = useCart();
  // Clear a temporary Buy Now line whenever checkout is abandoned by any navigation path,
  // including Android hardware Back and iOS swipe-back (not only the visible Back button).
  useFocusEffect(useCallback(() => () => clearBuyNow(), [clearBuyNow]));
  const checkoutLines = buyNowLine ? [buyNowLine] : cartLines;
  const checkoutUnresolvedKeys = buyNowLine ? [] : unresolvedKeys;
  const subtotal = buyNowLine ? checkoutLines.reduce((sum, line) => sum + lineAmount(line.product, line.qty), 0) : cartSubtotal;
  const deliveryFee = buyNowLine ? (subtotal === 0 || subtotal >= DELIVERY_FEE_THRESHOLD ? 0 : DELIVERY_FEE) : cartDeliveryFee;
  const { location } = useLocationCtx();

  const [name, setName] = useState(user?.name || "");
  const [phone, setPhone] = useState(user?.phone || "");
  const [address, setAddress] = useState(location === DEFAULT_LOCATION ? "" : location);
  const [notes, setNotes] = useState("");
  const [paymentMethod, setPaymentMethod] = useState<"cod" | "upi" | "cash_shop" | "pickup" | "online_razorpay">("cod");
  const paymentConfig = useGroceryPaymentConfig();
  const [fulfillment, setFulfillment] = useState<"delivery" | "pickup">("delivery");
  const total = subtotal + (fulfillment === "pickup" ? 0 : deliveryFee);
  const [shopOptions, setShopOptions] = useState<{ delivery: boolean; pickup: boolean; name: string; paymentMethods: string[]; publicUpi?: string; loadFailed?: boolean } | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [placed, setPlaced] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [quote, setQuote] = useState<GroceryQuote | null>(null);
  const [rewardBalance, setRewardBalance] = useState(0);
  const [useRewards, setUseRewards] = useState(false);
  const [guestSession, setGuestSession] = useState("");
  const [idempotencyKey, setIdempotencyKey] = useState("");
  const shopIds = Array.from(new Set(checkoutLines.map((line) => line.product.shopId).filter(Boolean)));
  const hasMixedShops = shopIds.length > 1;
  const hasDemoItems = checkoutLines.some((line) => line.product.source !== "live");
  const guestHeaders = { "X-Comein-Guest-Session": guestSession };
  const cartFingerprint = JSON.stringify(checkoutLines.map((line) => ({ id: line.product.id, variant: line.variant?.id || null, qty: line.qty, shop: line.product.shopId || null })));

  const optionsShopId = shopIds[0];
  useEffect(() => {
    let active = true;
    const shopId = optionsShopId;
    if (!shopId || hasDemoItems || hasMixedShops) return () => { active = false; };
    api.get<{ delivery_available?: boolean; pickup_available?: boolean; name?: string; payment_methods?: string[]; public_upi?: string }>(`/shops/${encodeURIComponent(shopId)}`, false).then((shop) => {
      if (!active) return;
      const options = { delivery: Boolean(shop.delivery_available), pickup: Boolean(shop.pickup_available), name: String(shop.name || "Selected shop"), paymentMethods: Array.isArray(shop.payment_methods) ? shop.payment_methods : ["cod"], publicUpi: typeof shop.public_upi === "string" ? shop.public_upi : undefined };
      setShopOptions(options);
      const available = options.paymentMethods.filter((method) => method === "cod" || method === "upi" && Boolean(options.publicUpi) || method === "cash_shop" && options.pickup || method === "pickup" && options.pickup);
      setPaymentMethod((current) => available.includes(current) || current === "online_razorpay" ? current : (available[0] as "cod" | "upi" | "cash_shop" | "pickup") || "cod");
      setFulfillment((current) => current === "delivery" && !options.delivery && options.pickup ? "pickup" : current === "pickup" && !options.pickup && options.delivery ? "delivery" : current);
    }).catch(() => { if (active) setShopOptions({ delivery: false, pickup: false, name: "Selected shop", paymentMethods: [], loadFailed: true }); });
    return () => { active = false; };
  }, [cartFingerprint, optionsShopId, hasDemoItems, hasMixedShops]);

  useEffect(() => {
    let active = true;
    (async () => {
      let session = await storage.getItem<string>(GUEST_SESSION_KEY, "");
      if (!session || session.length < 24) {
        session = makeOpaqueLocalKey() + makeOpaqueLocalKey();
        await storage.setItem(GUEST_SESSION_KEY, session);
      }
      if (active) setGuestSession(session);
    })();
    return () => { active = false; };
  }, []);

  useEffect(() => {
    let active = true;
    if (user?.role !== "customer") return () => { active = false; };
    api.get<any>("/referrals/me").then((data) => { if (active) setRewardBalance(Math.max(0, Number(data.available_balance || 0))); }).catch(() => { if (active) setRewardBalance(0); });
    return () => { active = false; };
  }, [user?.id, user?.role]);

  const onlineAvailable = Boolean(paymentConfig?.razorpay_enabled && user && shopOptions?.paymentMethods.includes("online_razorpay"));
  const paymentAvailable = paymentMethod === "online_razorpay" ? onlineAvailable : Boolean(shopOptions && (paymentMethod === "cod" && shopOptions.paymentMethods.includes("cod") || paymentMethod === "upi" && shopOptions.paymentMethods.includes("upi") && Boolean(shopOptions.publicUpi) || (paymentMethod === "cash_shop" || paymentMethod === "pickup") && shopOptions.pickup && (shopOptions.paymentMethods.includes(paymentMethod) || paymentMethod === "pickup" && shopOptions.paymentMethods.includes("cash_shop"))));
  const canPlace = Boolean(name.trim() && phone.trim() && (fulfillment === "pickup" || address.trim()) && checkoutLines.length > 0 && !hasMixedShops && !hasDemoItems && checkoutUnresolvedKeys.length === 0 && guestSession && idempotencyKey && shopIds.length === 1 && shopOptions && shopOptions[fulfillment] && paymentAvailable);
  useEffect(() => {
    let active = true;
    (async () => {
      let key = "";
      try {
        const raw = await storage.getItem<string>(IDEMPOTENCY_KEY_STORAGE, "");
        if (raw) {
          const saved = JSON.parse(raw);
          if (saved?.fingerprint === cartFingerprint && typeof saved?.key === "string") key = saved.key;
        }
      } catch {}
      if (!key) {
        key = makeOpaqueLocalKey() + makeOpaqueLocalKey();
        try { await storage.setItem(IDEMPOTENCY_KEY_STORAGE, JSON.stringify({ fingerprint: cartFingerprint, key })); } catch {}
      }
      if (active) setIdempotencyKey(key);
    })();
    return () => { active = false; };
  }, [cartFingerprint]);
  const checkoutKey = `${cartFingerprint}:${fulfillment}`;
  const [previousCheckoutKey, setPreviousCheckoutKey] = useState(checkoutKey);
  if (previousCheckoutKey !== checkoutKey) {
    setPreviousCheckoutKey(checkoutKey);
    setQuote(null);
  }
  const [previousCartFingerprint, setPreviousCartFingerprint] = useState(cartFingerprint);
  if (previousCartFingerprint !== cartFingerprint) {
    setPreviousCartFingerprint(cartFingerprint);
    setShopOptions(null);
  }

  const rewardUserKey = `${user?.id || ""}:${user?.role || ""}`;
  const [previousRewardUserKey, setPreviousRewardUserKey] = useState(rewardUserKey);
  if (previousRewardUserKey !== rewardUserKey) {
    setPreviousRewardUserKey(rewardUserKey);
    if (user?.role !== "customer") { setRewardBalance(0); setUseRewards(false); }
  }

  const place = async () => {
    setError(null);
    if (!canPlace) {
      setError(hasMixedShops ? "Checkout is limited to one shop. Return to your cart and remove items from other shops." : hasDemoItems ? "Demo preview items cannot be ordered. Remove them from your cart." : checkoutUnresolvedKeys.length ? "Please remove or resolve older saved cart items before checkout." : !shopOptions ? "Checking this shop's pickup and delivery options…" : !shopOptions[fulfillment] ? "This shop does not support the selected fulfillment option." : !paymentAvailable ? "Choose a payment method enabled and configured by this shop." : "Please complete the required contact and fulfillment details and use live catalog products.");
      return;
    }
    setSubmitting(true);
    try {
      if (!quote) {
        const created = await api.post<GroceryQuote>("/grocery/quotes", {
          items: checkoutLines.map((line) => ({ product_id: line.product.id, variant_id: line.variant?.id, qty: line.qty })),
          fulfillment,
          use_rewards: useRewards,
        }, true, guestHeaders);
        setQuote(created);
        setError("Review the server-confirmed prices below, then confirm to place your order. Quote expires in 10 minutes.");
        return;
      }
      if (Date.parse(quote.expires_at) <= Date.now()) {
        setQuote(null);
        setError("Your quote expired. Create a new quote and review the current prices.");
        return;
      }
      const order = await api.post<any>("/orders", {
        items: quote.items.map((line) => ({ product_id: line.product_id, variant_id: line.variant_id, name: line.name, unit: line.unit, price: line.price, qty: line.qty, shop_id: line.shop_id })),
        quote_token: quote.quote_token,
        idempotency_key: idempotencyKey,
        confirm_price_changes: true,
        shop_id: quote.items[0]?.shop_id,
        delivery_address: fulfillment === "delivery" ? address : "",
        fulfillment,
        customer_name: name,
        customer_phone: phone,
        notes,
        payment_method: paymentMethod,
      }, true, guestHeaders);
      if (buyNowLine) clearBuyNow();
      else clear();
      await storage.removeItem(IDEMPOTENCY_KEY_STORAGE);
      setIdempotencyKey("");
      setPlaced(order);
    } catch (e: any) {
      const detail = e?.detail;
      if (detail?.updated_quote) {
        setQuote(detail.updated_quote as GroceryQuote);
        setError("The price changed after your last quote. Review the updated amounts below and confirm again.");
      } else if (detail?.code === "quote_expired" || detail?.code === "quote_invalid" || detail?.code === "quote_changed" || detail?.code === "stale_quote" || detail?.code === "stock_changed" || detail?.code === "insufficient_stock") {
        setQuote(null);
        setError(detail?.message || e?.message || "Quote needs to be refreshed.");
      } else {
        setError(detail?.message || e?.message || "Could not place order. Your cart has been preserved.");
      }
    } finally {
      setSubmitting(false);
    }
  };

  if (placed) {
    return (
      <View style={styles.success}>
        <View style={styles.sIcon}><Feather name="check" size={32} color={colors.onBrandPrimary} /></View>
        <Text style={styles.sTitle}>{placed.payment_status === "paid_by_rewards" ? "Order placed — covered by rewards" : placed.payment_method === "upi" || placed.payment_status === "razorpay_pending" ? "Order created — payment pending" : "Order placed!"}</Text>
        <Text style={styles.sSub}>Reference <Text style={{ fontWeight: "800" }}>{placed.ref}</Text></Text>
        {placed.payment_status === "paid_by_rewards" ? <Text style={styles.sSub}>Your approved referral rewards covered the order total. No additional payment is due.</Text> : placed.payment_method === "upi" ? <>
          <Text style={styles.sSub}>Pay ₹{Number(placed.total).toFixed(2)} to the shop&#39;s UPI ID. The order stays pending until the shopkeeper verifies receipt.</Text>
          <Pressable testID="pay-upi-btn" onPress={() => { if (placed.payment_uri) Linking.openURL(placed.payment_uri).catch(() => setError("Could not open a UPI app. Copy the shop UPI ID from the shop page and pay manually; the order remains unpaid until the shop verifies receipt.")); }} style={styles.primary}>
            <Text style={styles.primaryText}>Pay with UPI app</Text>
          </Pressable>
          {error ? <Text style={styles.errorText}>{error}</Text> : null}
        </> : placed.payment_method === "online_razorpay" ? <>
          <Text style={styles.sSub} testID="online-payment-status">{placed.payment_status === "paid" ? `Paid ₹${Number(placed.total).toFixed(2)} online — verified by the server.` : "Complete the online payment below. The shop sees the order only after the server verifies payment."}</Text>
          <GroceryOnlinePayment order={placed} onChange={setPlaced} />
        </> : <Text style={styles.sSub}>{placed.payment_method === "cod" ? (placed.fulfillment === "pickup" ? `Pay ₹${placed.total} when collecting` : `Pay ₹${placed.total} on delivery`) : `Pay ₹${placed.total} at the shop`}</Text>}
        <Pressable testID="success-home" onPress={() => router.replace("/(tabs)")} style={styles.primary}>
          <Text style={styles.primaryText}>Keep shopping</Text>
        </Pressable>
        <Pressable testID="success-orders" onPress={() => router.replace("/orders")}>
          <Text style={{ color: colors.brandPrimary, fontWeight: "700", marginTop: spacing.md }}>Track my orders</Text>
        </Pressable>
      </View>
    );
  }

  return (
    <KeyboardAvoidingView style={styles.root} behavior={Platform.OS === "ios" ? "padding" : undefined}>
      <View style={[styles.header, { paddingTop: insets.top + spacing.sm }]}>
        <Pressable onPress={() => { if (buyNowLine) clearBuyNow(); router.back(); }} style={styles.iconBtn}><Feather name="arrow-left" size={20} color={colors.onSurface} /></Pressable>
        <Text style={styles.title}>Checkout</Text>
      </View>
      <ScrollView contentContainerStyle={{ padding: spacing.lg, paddingBottom: 160 }} keyboardShouldPersistTaps="handled">
        <SectionTitle text="Fulfillment" />
        {shopOptions && <Text style={styles.pmSub}>{shopOptions.name}</Text>}
        {checkoutLines.length > 0 && !shopOptions ? <Text style={styles.pmSub} testID="fulfillment-options-loading">Checking this shop&#39;s delivery and pickup availability…</Text> : null}
        <View style={{ flexDirection: "row", gap: spacing.sm }}>
          {shopOptions?.delivery && <Pressable testID="fulfillment-delivery" onPress={() => setFulfillment("delivery")} style={[styles.pmRow, { flex: 1 }, fulfillment === "delivery" && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}><Feather name="truck" size={16} color={colors.brandPrimary} /><Text style={styles.pmTitle}>Delivery</Text></Pressable>}
          {shopOptions?.pickup && <Pressable testID="fulfillment-pickup" onPress={() => setFulfillment("pickup")} style={[styles.pmRow, { flex: 1 }, fulfillment === "pickup" && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}><Feather name="map-pin" size={16} color={colors.brandPrimary} /><Text style={styles.pmTitle}>Pickup</Text></Pressable>}
        </View>
        {shopOptions?.loadFailed ? <Text style={styles.errorText} testID="fulfillment-options-error">Could not load this shop&#39;s delivery and pickup options. Check your connection and return to the cart to retry.</Text> : null}
        {shopOptions && !shopOptions.loadFailed && !shopOptions.delivery && !shopOptions.pickup ? <Text style={styles.errorText} testID="fulfillment-unavailable">This shop currently offers neither delivery nor pickup. Please contact the shop before placing an order.</Text> : null}
        {fulfillment === "delivery" && shopOptions?.delivery ? <>
          <SectionTitle text="Delivery details" />
          <Field testID="co-address" label="Delivery address" value={address} onChange={setAddress} multiline />
        </> : fulfillment === "pickup" && shopOptions?.pickup ? <Text style={styles.pmSub}>Collect your order from the shop&#39;s listed location. No delivery service is assumed.</Text> : null}
        <Field testID="co-name" label="Full name" value={name} onChange={setName} />
        <Field testID="co-phone" label="Phone number" value={phone} onChange={setPhone} keyboardType="phone-pad" />
        <Field testID="co-notes" label="Notes for shop (optional)" value={notes} onChange={setNotes} multiline />

        <SectionTitle text="Payment" />
        {shopOptions?.paymentMethods.includes("cod") ? <Pressable testID="pm-cod" onPress={() => setPaymentMethod("cod")} style={[styles.pmRow, paymentMethod === "cod" && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}>
          <Feather name="dollar-sign" size={16} color={colors.brandPrimary} />
          <View style={{ flex: 1 }}><Text style={styles.pmTitle}>Cash on Delivery</Text><Text style={styles.pmSub}>Pay in cash when your delivery arrives.</Text></View>
          <Feather name={paymentMethod === "cod" ? "check-circle" : "circle"} size={18} color={paymentMethod === "cod" ? colors.brandPrimary : colors.muted} />
        </Pressable> : null}
        {shopOptions?.paymentMethods.includes("upi") && shopOptions.publicUpi ? <Pressable testID="pm-upi" onPress={() => setPaymentMethod("upi")} style={[styles.pmRow, paymentMethod === "upi" && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}>
          <Feather name="smartphone" size={16} color={colors.brandPrimary} />
          <View style={{ flex: 1 }}><Text style={styles.pmTitle}>UPI</Text><Text style={styles.pmSub}>{shopOptions.publicUpi} · opens your UPI app; shopkeeper must verify receipt.</Text></View>
          <Feather name={paymentMethod === "upi" ? "check-circle" : "circle"} size={18} color={paymentMethod === "upi" ? colors.brandPrimary : colors.muted} />
        </Pressable> : null}
        {fulfillment === "pickup" && (shopOptions?.paymentMethods.includes("cash_shop") || shopOptions?.paymentMethods.includes("pickup")) ? <Pressable testID="pm-cash-shop" onPress={() => setPaymentMethod(shopOptions.paymentMethods.includes("cash_shop") ? "cash_shop" : "pickup")} style={[styles.pmRow, (paymentMethod === "cash_shop" || paymentMethod === "pickup") && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}>
          <Feather name="map-pin" size={16} color={colors.brandPrimary} /><View style={{ flex: 1 }}><Text style={styles.pmTitle}>Cash at Shop / Pickup</Text><Text style={styles.pmSub}>Pay in person when collecting your order.</Text></View>
          <Feather name={(paymentMethod === "cash_shop" || paymentMethod === "pickup") ? "check-circle" : "circle"} size={18} color={(paymentMethod === "cash_shop" || paymentMethod === "pickup") ? colors.brandPrimary : colors.muted} />
        </Pressable> : null}
        {onlineAvailable ? <Pressable testID="pm-online-razorpay" onPress={() => setPaymentMethod("online_razorpay")} style={[styles.pmRow, paymentMethod === "online_razorpay" && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}>
          <Feather name="credit-card" size={16} color={colors.brandPrimary} /><View style={{ flex: 1 }}><Text style={styles.pmTitle}>Pay online (Razorpay){paymentConfig?.mode === "test" ? " · TEST MODE" : ""}</Text><Text style={styles.pmSub}>Card, UPI or netbanking. Paid only after the server verifies the payment with Razorpay.</Text></View>
          <Feather name={paymentMethod === "online_razorpay" ? "check-circle" : "circle"} size={18} color={paymentMethod === "online_razorpay" ? colors.brandPrimary : colors.muted} />
        </Pressable> : null}
        {checkoutLines.length > 0 && shopOptions && !shopOptions.loadFailed && !onlineAvailable && !shopOptions.paymentMethods.some((method) => method === "cod" || method === "upi" && Boolean(shopOptions.publicUpi) || (method === "cash_shop" || method === "pickup") && shopOptions.pickup) ? <Text style={styles.pmSub} testID="no-supported-payment">This shop has no payment method enabled and configured for this checkout. Contact the shop owner; do not place the order.</Text> : null}
        {paymentMethod === "upi" ? <Text style={styles.pmSub}>UPI payment is initiated in your UPI app. COME-IN does not automatically receive bank confirmation; the shopkeeper must verify the actual credit before accepting the order as paid. Never share your UPI PIN or OTP.</Text> : null}

        {user?.role === "customer" && rewardBalance > 0 ? <Pressable testID="checkout-use-referral-rewards" onPress={() => { setUseRewards((current) => !current); setQuote(null); }} style={[styles.pmRow, useRewards && { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary }]}><Feather name="gift" size={18} color={colors.brandPrimary} /><View style={{ flex: 1 }}><Text style={styles.pmTitle}>Use Referral Rewards</Text><Text style={styles.pmSub}>Available balance ₹{rewardBalance.toFixed(2)} · {useRewards ? "Will apply to the next server quote" : "Use approved rewards on this order"}</Text></View><Feather name={useRewards ? "check-circle" : "circle"} size={18} color={useRewards ? colors.brandPrimary : colors.muted} /></Pressable> : null}
        <SectionTitle text={quote ? "Server-confirmed quote" : "Order summary"} />
        {quote && <Text style={styles.errorText}>Quote expires: {new Date(quote.expires_at).toLocaleTimeString()}</Text>}
        <View style={styles.bill}>
          {(quote?.items || checkoutLines.map((l) => ({ product_id: l.product.id, name: l.product.name, unit: l.product.unit, price: l.product.price, qty: l.qty, variant_id: l.variant?.id, ...(isMeasured(l.product) ? { line_total: lineAmount(l.product, l.qty), quantity_label: formatAmount(l.product, l.qty) } : {}) }))).map((l: any, index: number) => (
            <View key={`${l.product_id}-${l.variant_id || "base"}-${index}`} style={styles.billLine} testID={`checkout-line-${index}`}>
              <Text style={styles.billName}>{l.quantity_label ? `${l.quantity_label} × ${l.name} (₹${l.price}/${l.unit})` : `${l.qty} × ${l.name} ${l.unit ? `(${l.unit})` : ""}`}</Text>
              <Text style={styles.billValue}>₹{(l.line_total != null ? Number(l.line_total) : Number(l.price) * Number(l.qty)).toFixed(2)}</Text>
            </View>
          ))}
          <View style={styles.billLine}><Text style={styles.billName}>Items subtotal</Text><Text style={styles.billValue}>₹{quote?.subtotal ?? subtotal}</Text></View>
          <View style={styles.billLine}><Text style={styles.billName}>{fulfillment === "pickup" ? "Pickup" : "Delivery"}</Text><Text style={styles.billValue}>{fulfillment === "pickup" ? "At shop" : (quote?.delivery_fee ?? deliveryFee) === 0 ? "FREE" : `₹${quote?.delivery_fee ?? deliveryFee}`}</Text></View>
          {Number(quote?.reward_discount || 0) > 0 ? <View style={styles.billLine}><Text style={styles.billName}>Referral rewards</Text><Text style={styles.billValue}>−₹{Number(quote?.reward_discount || 0).toFixed(2)}</Text></View> : null}
          <View style={styles.divider} />
          <View style={styles.billLine}><Text style={[styles.billName, { fontWeight: "800", color: colors.onSurface }]}>To pay</Text><Text style={[styles.billValue, { fontWeight: "800", fontSize: 16 }]}>₹{quote?.total ?? total}</Text></View>
        </View>

        {error && <Text style={styles.errorText}>{error}</Text>}
      </ScrollView>

      <View style={[styles.cta, { paddingBottom: insets.bottom + spacing.sm }]}>
        <Pressable
          testID="place-order-btn"
          disabled={!canPlace || submitting}
          onPress={place}
          style={[styles.primary, (!canPlace || submitting) && { opacity: 0.5 }]}
        >
          {submitting ? <ActivityIndicator color={colors.onBrandPrimary} /> : (
            <Text style={styles.primaryText}>
              {submitting ? "Please wait…" : quote ? `Confirm and place · ₹${quote.total}` : checkoutLines.length === 0 ? "Your cart is empty" : `Review quote · ₹${total}`}
            </Text>
          )}
        </Pressable>
      </View>
    </KeyboardAvoidingView>
  );
}

function SectionTitle({ text }: { text: string }) {
  const styles = useStyles();
  return <Text style={styles.sectionTitle}>{text}</Text>;
}

function Field({ testID, label, value, onChange, multiline, keyboardType }: any) {
  const styles = useStyles();
  const { colors } = useTheme();
  return (
    <View>
      <Text style={styles.label}>{label}</Text>
      <View style={[styles.inputWrap, multiline && { alignItems: "flex-start" }]}>
        <TextInput testID={testID} value={value} onChangeText={onChange} placeholderTextColor={colors.muted} style={[styles.input, multiline && { minHeight: 60 }]} multiline={multiline} keyboardType={keyboardType} />
      </View>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  header: { flexDirection: "row", alignItems: "center", gap: spacing.md, paddingHorizontal: spacing.lg, paddingBottom: spacing.sm, backgroundColor: colors.surface, borderBottomWidth: StyleSheet.hairlineWidth, borderBottomColor: colors.border },
  iconBtn: { width: 36, height: 36, borderRadius: 18, backgroundColor: colors.surfaceTertiary, alignItems: "center", justifyContent: "center" },
  title: { fontSize: 18, fontWeight: "800", color: colors.onSurface },
  sectionTitle: { marginTop: spacing.lg, marginBottom: spacing.sm, fontSize: 12, fontWeight: "800", letterSpacing: 0.5, color: colors.muted },
  label: { marginTop: spacing.sm, marginBottom: 6, fontSize: 12, fontWeight: "700", color: colors.onSurfaceSecondary },
  inputWrap: { backgroundColor: colors.surfaceTertiary, borderRadius: radius.md, paddingHorizontal: spacing.md, paddingVertical: Platform.OS === "ios" ? 12 : 8 },
  input: { fontSize: 14, color: colors.onSurface, padding: 0 },
  pmRow: { flexDirection: "row", alignItems: "center", gap: spacing.md, borderWidth: 1, borderColor: colors.border, borderRadius: radius.md, padding: spacing.md, marginTop: spacing.sm },
  pmTitle: { fontSize: 14, fontWeight: "700", color: colors.onSurface },
  pmSub: { fontSize: 11, color: colors.muted, marginTop: 2 },
  bill: { marginTop: spacing.sm, backgroundColor: colors.surface, borderRadius: radius.md, borderWidth: 1, borderColor: colors.border, padding: spacing.md, gap: 4 },
  billLine: { flexDirection: "row", justifyContent: "space-between", paddingVertical: 4 },
  billName: { fontSize: 13, color: colors.onSurfaceSecondary },
  billValue: { fontSize: 13, color: colors.onSurface, fontWeight: "600" },
  divider: { height: StyleSheet.hairlineWidth, backgroundColor: colors.divider, marginVertical: 4 },
  cta: { position: "absolute", left: 0, right: 0, bottom: 0, paddingHorizontal: spacing.lg, paddingTop: spacing.md, backgroundColor: colors.surface, borderTopWidth: 1, borderTopColor: colors.border },
  primary: { backgroundColor: colors.brandPrimary, paddingVertical: 14, borderRadius: radius.md, alignItems: "center" },
  primaryText: { color: colors.onBrandPrimary, fontWeight: "800", fontSize: 15 },
  errorText: { color: colors.error, fontSize: 12, marginTop: spacing.md },
  success: { flex: 1, backgroundColor: colors.surface, alignItems: "center", justifyContent: "center", padding: spacing.xl, gap: spacing.sm },
  sIcon: { width: 72, height: 72, borderRadius: 36, backgroundColor: colors.brandPrimary, alignItems: "center", justifyContent: "center", marginBottom: spacing.md },
  sTitle: { fontSize: 20, fontWeight: "800", color: colors.onSurface },
  sSub: { fontSize: 13, color: colors.muted },
}));
