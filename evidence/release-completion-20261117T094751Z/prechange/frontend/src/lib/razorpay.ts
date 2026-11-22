import { useEffect, useState } from "react";
import { Platform } from "react-native";

import { api } from "@/src/lib/api";

// Task 17: Razorpay Standard Checkout for Grocery. Only the public key ID ever reaches the client.
export type RazorpayIntent = { key_id: string; gateway_order_id: string; amount: number; currency: string; order_ref: string; prefill?: { name?: string; contact?: string } };
export type RazorpayResult = { razorpay_order_id: string; razorpay_payment_id: string; razorpay_signature: string };
export type GroceryPaymentConfig = { razorpay_enabled: boolean; razorpay_key_id: string | null; mode: "test" | "live" | null };

export const razorpaySupported = () => Platform.OS === "web" && typeof window !== "undefined";

export function useGroceryPaymentConfig(): GroceryPaymentConfig | null {
  const [config, setConfig] = useState<GroceryPaymentConfig | null>(null);
  useEffect(() => {
    let active = true;
    api.get<GroceryPaymentConfig>("/grocery/payments/config", false)
      .then((c) => { if (active) setConfig(c); })
      .catch(() => { if (active) setConfig({ razorpay_enabled: false, razorpay_key_id: null, mode: null }); });
    return () => { active = false; };
  }, []);
  return config;
}

let scriptPromise: Promise<void> | null = null;
function loadCheckoutScript(): Promise<void> {
  if ((window as any).Razorpay) return Promise.resolve();
  if (!scriptPromise) {
    scriptPromise = new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = "https://checkout.razorpay.com/v1/checkout.js";
      s.async = true;
      s.onload = () => resolve();
      s.onerror = () => { scriptPromise = null; reject(new Error("Could not load the payment window. Check your connection and try again.")); };
      document.body.appendChild(s);
    });
  }
  return scriptPromise;
}

export async function openRazorpay(intent: RazorpayIntent): Promise<RazorpayResult> {
  if (!razorpaySupported()) throw new Error("Online payment currently works in the web app. The Android/iOS app needs a native payment build first.");
  await loadCheckoutScript();
  return new Promise((resolve, reject) => {
    const rz = new (window as any).Razorpay({
      key: intent.key_id, order_id: intent.gateway_order_id, amount: intent.amount, currency: intent.currency,
      name: "COME-IN", description: `Order ${intent.order_ref}`, prefill: intent.prefill,
      handler: (r: RazorpayResult) => resolve(r),
      modal: { ondismiss: () => reject(new Error("Payment window closed. No payment was confirmed.")) },
    });
    rz.on("payment.failed", (r: any) => reject(new Error(r?.error?.description || "Payment failed. No payment was confirmed.")));
    rz.open();
  });
}
