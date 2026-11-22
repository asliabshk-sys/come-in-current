import { useCallback, useState } from 'react';
import { useFocusEffect } from 'expo-router';
import { api } from '@/src/lib/api';
import { useAuth } from '@/src/store/auth';
import { useLocationCtx } from '@/src/store/location';
import { storage } from '@/src/utils/storage';

export type DiscoveryAddress = {
  id: string;
  label: string;
  address_line: string;
  city: string;
  state: string;
  pincode: string;
  is_default: boolean;
};

export function validIndianPincode(value: unknown): string | undefined {
  const pin = String(value ?? '').trim();
  return /^[1-9][0-9]{5}$/.test(pin) ? pin : undefined;
}

export function pincodeFromLocationText(value: string): string | undefined {
  const matches = value.match(/\b[1-9][0-9]{5}\b/g);
  return matches?.length ? validIndianPincode(matches[matches.length - 1]) : undefined;
}

const SELECTED_ADDRESS_KEY = '@comein_restaurant_discovery_address_v1';

export function useDiscoveryAddress() {
  const { user } = useAuth();
  const discoveryUserId = user?.id;
  const { location } = useLocationCtx();
  const [addresses, setAddresses] = useState<DiscoveryAddress[]>([]);
  const [selectedAddressId, setSelectedAddressId] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useFocusEffect(useCallback(() => {
    let active = true;
    if (!discoveryUserId) {
      setAddresses([]);
      setSelectedAddressId('');
      setError('Sign in to use your saved delivery addresses for restaurant discovery.');
      return () => { active = false; };
    }
    setLoading(true);
    setError('');
    api.get<DiscoveryAddress[]>('/addresses')
      .then(async (rows) => {
        if (!active) return;
        const safeRows = Array.isArray(rows) ? rows : [];
        setAddresses(safeRows);
        let persistedId = '';
        try { persistedId = (await storage.getItem<string>(SELECTED_ADDRESS_KEY, '')) ?? ''; } catch { /* fall back to the account default */ }
        if (!active) return;
        setSelectedAddressId((current) => safeRows.some((row) => row.id === current)
          ? current
          : (safeRows.find((row) => row.id === persistedId) || safeRows.find((row) => row.is_default) || safeRows[0])?.id || '');
        if (!safeRows.length) setError('No saved addresses found. Add an address with a valid pincode to filter restaurant delivery coverage.');
        else if (!safeRows.some((row) => validIndianPincode(row.pincode))) setError('A valid pincode is missing from your saved addresses. Update an address before filtering delivery coverage.');
      })
      .catch((e: any) => { if (active) setError(e?.message || 'Saved addresses could not be loaded. Check your connection and retry.'); })
      .finally(() => { if (active) setLoading(false); });
    return () => { active = false; };
  }, [discoveryUserId]));

  const chooseAddress = useCallback((id: string) => {
    setSelectedAddressId(id);
    void storage.setItem(SELECTED_ADDRESS_KEY, id);
  }, []);

  const selectedAddress = addresses.find((row) => row.id === selectedAddressId);
  const sharedLocationPincode = pincodeFromLocationText(location);
  const savedAddressPincode = validIndianPincode(selectedAddress?.pincode);
  const selectedPincode = savedAddressPincode || sharedLocationPincode;
  const pincodeSource = savedAddressPincode ? (selectedAddress?.label || 'Saved address') : sharedLocationPincode ? 'Shared current location/address' : 'Saved address';

  return { addresses, selectedAddressId, setSelectedAddressId: chooseAddress, selectedAddress, selectedPincode, pincodeSource, loading, error, hasSharedLocationText: Boolean(sharedLocationPincode && !savedAddressPincode) };
}
