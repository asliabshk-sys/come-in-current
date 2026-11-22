import { useEffect, useState } from 'react';
import { Pressable, Text, TextInput, View, ActivityIndicator } from 'react-native';
import { useRouter } from 'expo-router';
import { readRestaurantCart, writeRestaurantCart } from '@/src/restaurant/cart';
import { RestaurantPage, rs } from '@/src/restaurant/RestaurantPage';
import { restaurantTheme as t } from '@/src/restaurant/theme';
import { createLiveOrder } from '@/src/restaurant/api';
import { api } from '@/src/lib/api';
import { useAuth } from '@/src/store/auth';

type SavedAddress = {
  id: string;
  label: string;
  recipient_name: string;
  phone: string;
  address_line: string;
  city: string;
  state: string;
  pincode: string;
  is_default: boolean;
};

function formatAddress(address: SavedAddress) {
  return [address.address_line, address.city, address.state, address.pincode].filter(Boolean).join(', ');
}

export default function RestaurantCheckout() {
  const router = useRouter();
  const { user } = useAuth();
  const [contactName, setContactName] = useState(user?.name || '');
  const [contactPhone, setContactPhone] = useState(user?.phone || '');
  const [fulfillment, setFulfillment] = useState<'delivery' | 'pickup'>('delivery');
  const [restaurantPaymentMethods, setRestaurantPaymentMethods] = useState<string[]>([]);
  const [paymentMethod, setPaymentMethod] = useState<'cod' | 'pickup'>('cod');
  const [address, setAddress] = useState('');
  const [addressId, setAddressId] = useState('');
  const [savedAddresses, setSavedAddresses] = useState<SavedAddress[]>([]);
  const [addressesLoading, setAddressesLoading] = useState(Boolean(user));
  const [addressNotice, setAddressNotice] = useState('');
  const [notice, setNotice] = useState('');
  const [busy, setBusy] = useState(false);
  const [idempotencyKey] = useState(() => `restaurant-${Date.now()}-${Math.random().toString(36).slice(2, 12)}`);

  const [addressUser, setAddressUser] = useState(user?.id);
  if (addressUser !== user?.id) {
    setAddressUser(user?.id);
    if (user) {
      setContactName((current) => current || user.name || '');
      setContactPhone((current) => current || user.phone || '');
      setAddressesLoading(true); setAddressNotice('');
    }
  }
  useEffect(() => {
    if (!user) return;
    let active = true;
    api.get<SavedAddress[]>('/addresses')
      .then((rows) => {
        if (!active) return;
        const safeRows = Array.isArray(rows) ? rows : [];
        setSavedAddresses(safeRows);
        const fallback = safeRows.find((item) => item.is_default) || safeRows[0];
        const selected = fallback;
        setAddressId(selected?.id || '');
        setAddress(selected ? formatAddress(selected) : '');
        if (safeRows.length === 0) setAddressNotice('No saved addresses yet. Add one to reuse the same address in Shopping and Restaurant Mode.');
      })
      .catch((error: any) => {
        if (active) setAddressNotice(error?.message || 'Saved addresses could not be loaded. Retry or open the shared address book. Manual checkout addresses are not accepted.');
      })
      .finally(() => { if (active) setAddressesLoading(false); });
    return () => { active = false; };
  }, [user?.id]);

  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const lines = await readRestaurantCart();
        const restaurantIds = Array.from(new Set(lines.map((line) => line.restaurantId)));
        if (restaurantIds.length !== 1) return;
        const restaurant = await api.get<any>(`/restaurants/${encodeURIComponent(restaurantIds[0])}`, false);
        if (!active) return;
        const methods = Array.isArray(restaurant.payment_methods) ? restaurant.payment_methods : ['cod', 'pickup'];
        setRestaurantPaymentMethods(methods);
        setFulfillment((current) => !restaurant.delivery_available && restaurant.pickup_available ? 'pickup' : current);
        setPaymentMethod(methods.includes('cod') ? 'cod' : 'pickup');
      } catch { if (active) setRestaurantPaymentMethods([]); }
    })();
    return () => { active = false; };
  }, []);

  async function placeOrder() {
    setNotice('');
    setBusy(true);
    try {
      const lines = await readRestaurantCart();
      if (!lines.length) {
        setNotice('Your cart is empty. Add an item first.');
        return;
      }
      if (!lines.every((line) => line.isLive)) {
        setNotice('These are development sample items, not a live restaurant menu. No order was created. Add items from an approved live restaurant before checkout.');
        return;
      }
      if (new Set(lines.map((line) => line.restaurantId)).size !== 1) {
        setNotice('A restaurant cart can contain items from only one restaurant. Remove items from other restaurants before checkout.');
        return;
      }
      if (!user) {
        setNotice('Please sign in to your existing COME-IN account before placing an order.');
        router.push({ pathname: '/auth', params: { next: '/restaurant/checkout' } } as never);
        return;
      }
      if (fulfillment === 'delivery' && !addressId) {
        setNotice('Choose a valid saved address from the shared address book before delivery checkout.');
        router.push('/addresses' as never);
        return;
      }
      if (!contactName.trim() || !contactPhone.trim()) {
        setNotice('Enter your contact name and phone.');
        return;
      }
      const restaurantId = lines[0].restaurantId;
      const restaurant = await api.get<any>(`/restaurants/${encodeURIComponent(restaurantId)}`, false);
      const enabledMethods = Array.isArray(restaurant.payment_methods) ? restaurant.payment_methods : ['cod', 'pickup'];
      setRestaurantPaymentMethods(enabledMethods);
      const chosenMethod = paymentMethod === 'cod' && enabledMethods.includes('cod') ? 'cod' : fulfillment === 'pickup' && paymentMethod === 'pickup' && enabledMethods.includes('pickup') ? 'pickup' : fulfillment === 'pickup' && enabledMethods.includes('pickup') ? 'pickup' : fulfillment === 'delivery' && enabledMethods.includes('cod') ? 'cod' : null;
      if (!chosenMethod) { setNotice('This restaurant has no supported payment method selected for this checkout. Ask the restaurant to enable COD or pay-at-pickup.'); return; }
      if (fulfillment === 'delivery') {
        const selectedSavedAddress = savedAddresses.find((item) => item.id === addressId);
        const pincodeMatch = (selectedSavedAddress?.pincode || '').match(/\b[1-9][0-9]{5}\b/g);
        const pincode = pincodeMatch?.[pincodeMatch.length - 1];
        if (!pincode) {
          setNotice('The selected saved address needs a valid six-digit pincode. Update it in the shared address book.');
          router.push('/addresses' as never);
          return;
        }
        const coverage = await api.get<{ serviceable: boolean; status: string; reason: string }>(
          `/restaurants/${encodeURIComponent(restaurantId)}/serviceability?pincode=${encodeURIComponent(pincode)}`,
          false,
        );
        if (!coverage.serviceable) {
          setNotice(coverage.reason || 'Delivery coverage could not be confirmed. Choose pickup or contact the restaurant.');
          return;
        }
      }
      const order = await createLiveOrder({
        restaurant_id: restaurantId,
        items: lines.map((line) => ({
          menu_item_id: line.itemId,
          quantity: line.quantity,
          variant_id: line.variantId,
          add_on_ids: line.addOnIds || [],
          instructions: line.instructions || '',
        })),
        address_id: fulfillment === 'delivery' && addressId ? addressId : undefined,
        contact_name: contactName.trim(),
        contact_phone: contactPhone.trim(),
        fulfillment,
        payment_method: chosenMethod,
        notes: '',
        idempotency_key: idempotencyKey,
      });
      await writeRestaurantCart([]);
      router.replace({ pathname: '/restaurant/order-confirmation', params: { id: order.id, ref: order.ref, mode: 'live', status: order.status } } as never);
    } catch (error: any) {
      setNotice(error?.message || 'Could not submit the order. Your cart has been preserved; check the order history before retrying if the connection failed.');
    } finally {
      setBusy(false);
    }
  }

  return (
    <RestaurantPage title="Restaurant checkout" subtitle="Uses your shared COME-IN account and saved addresses">
      <View style={rs.card}>
        <Text style={rs.heading}>Account</Text>
        <Text style={rs.muted}>{user ? `Signed in as ${user.name} · ${user.email}` : 'Sign in with your existing COME-IN account. No separate restaurant account is needed for customers.'}</Text>
        {!user ? <Pressable style={rs.chip} onPress={() => router.push({ pathname: '/auth', params: { next: '/restaurant/checkout' } } as never)}><Text style={rs.chipText}>Sign in</Text></Pressable> : null}

        <Text style={rs.heading}>Contact name</Text>
        <TextInput value={contactName} onChangeText={setContactName} placeholder={user?.name || 'Your name'} placeholderTextColor={t.textMuted} style={rs.input} />
        <Text style={rs.heading}>Contact phone</Text>
        <TextInput value={contactPhone} onChangeText={setContactPhone} placeholder={user?.phone || 'Phone number'} keyboardType="phone-pad" placeholderTextColor={t.textMuted} style={rs.input} />

        <Text style={rs.heading}>Fulfilment</Text>
        <View style={rs.row}>
          <Pressable style={[rs.chip, fulfillment === 'delivery' && rs.chipActive]} onPress={() => setFulfillment('delivery')}><Text style={[rs.chipText, fulfillment === 'delivery' && rs.chipTextActive]}>Delivery</Text></Pressable>
          <Pressable style={[rs.chip, fulfillment === 'pickup' && rs.chipActive]} onPress={() => setFulfillment('pickup')}><Text style={[rs.chipText, fulfillment === 'pickup' && rs.chipTextActive]}>Pickup</Text></Pressable>
        </View>

        {fulfillment === 'delivery' ? <>
          <Text style={rs.heading}>Delivery address</Text>
          {addressesLoading ? <ActivityIndicator color={t.primary} /> : null}
          {savedAddresses.map((saved) => <Pressable key={saved.id} style={[rs.chip, addressId === saved.id && rs.chipActive]} onPress={() => { setAddressId(saved.id); setAddress(formatAddress(saved)); }}><Text style={[rs.chipText, addressId === saved.id && rs.chipTextActive]}>{saved.label}{saved.is_default ? ' · Default' : ''}: {formatAddress(saved)}</Text></Pressable>)}
          <Text style={rs.muted}>{addressId ? `Selected saved address: ${address}` : 'Select an existing saved address below or add one in the shared address book. A manually typed address cannot be used for checkout.'}</Text>
          <View style={rs.row}>
            <Pressable style={rs.chip} onPress={() => router.push('/addresses' as never)}><Text style={rs.chipText}>Manage shared saved addresses</Text></Pressable>
            <Pressable style={rs.chip} onPress={() => router.push('/delivery-address' as never)}><Text style={rs.chipText}>Set current location</Text></Pressable>
          </View>
          <Text style={rs.muted}>The selected saved address is revalidated against your account by the backend. Current location is optional; GPS access is requested only when you choose it, and coordinates are not a postal address. Delivery is confirmed only when the backend has an explicitly configured verified pincode coverage list for this restaurant. If coverage is missing or the pincode is outside that list, checkout is blocked; choosing an address alone never confirms eligibility.</Text>
          {addressNotice ? <Text style={rs.muted}>{addressNotice}</Text> : null}
        </> : <Text style={rs.muted}>Pickup uses the restaurant&#39;s supported pickup option; no delivery address is required.</Text>}

        <Text style={rs.heading}>Payment</Text>
        {restaurantPaymentMethods.includes('cod') ? <Pressable style={[rs.chip,paymentMethod==='cod'&&rs.chipActive]} onPress={()=>setPaymentMethod('cod')}><Text style={[rs.chipText,paymentMethod==='cod'&&rs.chipTextActive]}>Cash on Delivery</Text></Pressable> : null}
        {fulfillment==='pickup' && restaurantPaymentMethods.includes('pickup') ? <Pressable style={[rs.chip,paymentMethod==='pickup'&&rs.chipActive]} onPress={()=>setPaymentMethod('pickup')}><Text style={[rs.chipText,paymentMethod==='pickup'&&rs.chipTextActive]}>Pay at Pickup</Text></Pressable> : null}
        <Text style={rs.muted}>Only the selected restaurant&#39;s enabled COD and pay-at-pickup methods are offered here. Online payment is not offered in this UI (Razorpay needs a customer-facing payment screen) until a customer-facing payment screen is connected. The backend validates the selected method and authoritative prices. No payment is taken or inferred as successful by this screen.</Text>
        <Pressable disabled={busy} style={[rs.button, busy && { opacity: 0.6 }]} onPress={placeOrder}><Text style={rs.buttonText}>{busy ? 'Submitting…' : 'Place order'}</Text></Pressable>
        {notice ? <Text style={{ color: t.error, fontSize: 12 }}>{notice}</Text> : null}
      </View>
    </RestaurantPage>
  );
}
