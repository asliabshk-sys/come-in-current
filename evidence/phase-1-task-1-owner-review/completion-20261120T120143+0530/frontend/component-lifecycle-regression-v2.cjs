/* Execute the actual TSX component functions with isolated hook/API doubles.
 * No browser, native modules, backend, provider, storage file or real account I/O.
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const crypto = require('crypto');
const ts = require('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend/node_modules/typescript');
const sourceDir = process.argv[2];
const out = process.argv[3];
if (!sourceDir || !out) throw new Error('Usage: node component-lifecycle-regression.cjs SOURCE_DIR RESULT_JSON');
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const same = (a, b) => a && b && a.length === b.length && a.every((x, i) => Object.is(x, b[i]));
const noop = () => {};
function assert(value, message) { if (!value) throw new Error(message); }
function deferred() { let resolve;const promise = new Promise(r => { resolve = r; });return { promise, resolve }; }

class Hooks {
  constructor(kind) {
    this.kind = kind;this.slots = [];this.index = 0;this.pending = new Map();this.dirty = false;
    this.user = null;this.gets = [];this.storageGets = [];this.cartSource = 'catalog';this.tree = null;
    this.router = { back: noop, push: noop, replace: noop };
    this.cartActions = { clear: noop, clearBuyNow: noop };
    this.react = {
      useState: initial => {
        const index = this.index++;
        if (!this.slots[index]) {
          const slot = { value: typeof initial === 'function' ? initial() : initial };
          slot.set = update => {const next = typeof update === 'function' ? update(slot.value) : update;if (!Object.is(next, slot.value)) {slot.value = next;this.dirty = true;}};
          this.slots[index] = slot;
        }
        return [this.slots[index].value, this.slots[index].set];
      },
      useRef: initial => {const i = this.index++;if (!this.slots[i]) this.slots[i] = { current: initial };return this.slots[i];},
      useCallback: (fn, deps) => this.memo(() => fn, deps),
      useMemo: (fn, deps) => this.memo(fn, deps),
      useEffect: (fn, deps) => {
        const i = this.index++;const old = this.slots[i];
        if (!old || !same(old.deps, deps)) {
          this.slots[i] = { deps, cleanup: old?.cleanup };
          this.pending.set(i, fn);
        }
      },
    };
    const ui = new Proxy({ StyleSheet: { hairlineWidth: 1, create: x => x }, Platform: { OS: 'web' } }, {
      get: (target, prop) => prop in target ? target[prop] : String(prop),
    });
    const api = {
      get: url => {
        const entry = { url, account: this.user?.id || null };this.gets.push(entry);
        if ((this.kind === 'services' && url !== '/home-services/providers') || this.kind === 'discovery') {entry.deferred = deferred();return entry.deferred.promise;}
        if (url.startsWith('/shops/')) return Promise.resolve({ name: 'Fixture shop', delivery_available: true, pickup_available: false, payment_methods: ['cod'] });
        return Promise.resolve([]);
      },
      post: () => Promise.resolve({ quote_token: 'synthetic-quote', items: [], total: 100, subtotal: 100, delivery_fee: 0, currency: 'INR' }),
      patch: () => Promise.resolve({}),upload: () => Promise.resolve({}),
    };
    const colors = new Proxy({}, { get: () => '#123456' });
    const modules = {
      react: this.react,
      'react/jsx-runtime': { jsx: (type, props, key) => ({ type, props, key }), jsxs: (type, props, key) => ({ type, props, key }), Fragment: 'Fragment' },
      'react-native': ui,
      '@react-native-vector-icons/feather': { __esModule: true, default: 'Feather' },
      'expo-router': { useRouter: () => this.router, useLocalSearchParams: () => ({}), useFocusEffect: fn => this.react.useEffect(fn, [fn]) },
      'expo-linking': { openURL: () => Promise.resolve() },
      'react-native-safe-area-context': { useSafeAreaInsets: () => ({ top: 0, bottom: 0, left: 0, right: 0 }) },
      '@/src/lib/api': { api },
      '@/src/store/auth': { useAuth: () => ({ user: this.user }) },
      '@/src/components/GroceryOnlinePayment': { GroceryOnlinePayment: 'GroceryOnlinePayment' },
      '@/src/lib/razorpay': { useGroceryPaymentConfig: () => ({ razorpay_enabled: false }) },
      '@/src/store/cart': { DELIVERY_FEE: 20, DELIVERY_FEE_THRESHOLD: 499, useCart: () => ({ ...this.cartActions, cartLines: [{ product: { id: 'same-product', shopId: 'fixture-shop', source: this.cartSource, name: 'Fixture', price: 100 }, qty: 1 }], subtotal: 100, deliveryFee: 0, unresolvedKeys: [], buyNowLine: null }) },
      '@/src/lib/measure': { lineAmount: (p, qty) => p.price * qty, formatAmount: (_p, amount) => String(amount), isMeasured: () => false },
      '@/src/utils/storage': { storage: { getItem: (_key, fallback) => {if (this.kind !== 'discovery') return Promise.resolve(fallback);const d=deferred();this.storageGets.push({account:this.user?.id,deferred:d});return d.promise;}, setItem: () => Promise.resolve() } },
      '@/src/store/location': { useLocationCtx: () => ({ location: 'Set delivery location' }) },
      '@/src/theme': { makeStyles: fn => () => fn(colors), useTheme: () => ({ colors }), radius: { pill: 20, md: 12, lg: 20 }, spacing: { sm: 8, md: 12, lg: 20, xl: 24, xxl: 32 } },
      '@/src/utils/alert': { Alert: { alert: noop } },
    };
    this.require = name => { if (!(name in modules)) throw new Error('Unreviewed module import: ' + name);return modules[name]; };
  }
  memo(fn, deps) {const i = this.index++;if (!this.slots[i] || !same(this.slots[i].deps, deps)) this.slots[i] = { value: fn(), deps };return this.slots[i].value;}
  load(relative, exportName = 'default') {
    const file = path.join(sourceDir, relative);const source = fs.readFileSync(file, 'utf8');
    this.sourceFile = file;this.sourceSHA256 = sha(source);
    const compiled = ts.transpileModule(source, { compilerOptions: { jsx: ts.JsxEmit.ReactJSX, module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } });
    const module = { exports: {} };
    vm.runInNewContext(compiled.outputText, { module, exports: module.exports, require: this.require, console, setTimeout, clearTimeout, URL, Date, Math, Promise, encodeURIComponent }, { filename: file });
    this.component = module.exports[exportName];
  }
  render() {
    let rounds = 0;
    do {this.dirty = false;this.index = 0;this.tree = this.component();if (++rounds > 12) throw new Error('Unbounded render loop');} while (this.dirty);
    return this.tree;
  }
  flushEffects() {const pending = [...this.pending];this.pending.clear();for (const [i, fn] of pending) {this.slots[i].cleanup?.();this.slots[i].cleanup = fn();}}
  async settle() {for (let i = 0; i < 12; i++) await Promise.resolve();}
  resolveDashboard(account) {
    for (const entry of this.gets) {
      if (entry.account !== account || !entry.deferred) continue;
      entry.deferred.resolve(entry.url.endsWith('/providers/mine')
        ? { id: account + '-provider', full_name: 'PRIVATE_' + account, phone: 'fixture-phone', service_area: 'fixture-area', tasks: [], payment_preferences: [] }
        : [{ id: account + '-appointment', ref: 'PRIVATE_' + account, status: 'pending', appointment_at: '2026-11-20T10:00:00Z' }]);
    }
  }
}

(async () => {
  const cases = [];
  for (const [id, invariant, fn] of [
    ['FE-LIFECYCLE-01', 'Checkout re-evaluates live/demo eligibility even when its cart fingerprint stays identical', async () => {
      const h = new Hooks('checkout');h.load('app/checkout.tsx');h.render();h.flushEffects();await h.settle();
      assert(h.gets.filter(x => x.url.startsWith('/shops/')).length === 0, 'Demo cart unexpectedly fetched shop eligibility');
      h.cartSource = 'live';h.render();h.flushEffects();await h.settle();
      assert(h.gets.filter(x => x.url.startsWith('/shops/')).length === 1, 'Live cart with unchanged id/qty/shop failed to fetch current shop options');
      return { source: h.sourceFile, source_SHA256: h.sourceSHA256, shop_fetches: h.gets.filter(x => x.url.startsWith('/shops/')).length };
    }],
    ['FE-LIFECYCLE-02', 'An old account dashboard response cannot overwrite the currently signed-in account dashboard', async () => {
      const h = new Hooks('services');h.load('app/services.tsx');h.user = { id: 'ACCOUNT_A', role: 'customer' };h.render();h.flushEffects();
      h.user = { id: 'ACCOUNT_B', role: 'customer' };h.render();h.flushEffects();
      h.resolveDashboard('ACCOUNT_B');await h.settle();h.render();
      assert(JSON.stringify(h.tree).includes('PRIVATE_ACCOUNT_B'), 'Current account dashboard failed to render its own response');
      h.resolveDashboard('ACCOUNT_A');await h.settle();h.render();
      assert(!JSON.stringify(h.tree).includes('PRIVATE_ACCOUNT_A'), 'Stale prior-account response appeared in the current account dashboard');
      assert(JSON.stringify(h.tree).includes('PRIVATE_ACCOUNT_B'), 'Prior-account response replaced the current account data');
      return { source: h.sourceFile, source_SHA256: h.sourceSHA256, no_account_data_in_result: true };
    }],
    ['FE-LIFECYCLE-03', 'Persisted address lookup from an old account cannot overwrite the active account selection after an await', async () => {
      const h = new Hooks('discovery');h.load('src/restaurant/useDiscoveryAddress.ts', 'useDiscoveryAddress');
      const address = account => [{id:account+'-address',label:'Fixture',address_line:'Synthetic fixture only',city:'Fixture',state:'Fixture',pincode:'110001',is_default:true}];
      h.user = {id:'ACCOUNT_A',role:'customer'};h.render();h.flushEffects();
      h.gets.find(x=>x.account==='ACCOUNT_A').deferred.resolve(address('ACCOUNT_A'));await h.settle();
      assert(h.storageGets.some(x=>x.account==='ACCOUNT_A'), 'Old account storage await was not reached');
      h.user = {id:'ACCOUNT_B',role:'customer'};h.render();h.flushEffects();
      h.gets.find(x=>x.account==='ACCOUNT_B').deferred.resolve(address('ACCOUNT_B'));await h.settle();
      h.storageGets.find(x=>x.account==='ACCOUNT_B').deferred.resolve('ACCOUNT_B-address');await h.settle();h.render();
      assert(h.tree.selectedAddressId==='ACCOUNT_B-address', 'Current account address selection failed');
      h.storageGets.find(x=>x.account==='ACCOUNT_A').deferred.resolve('ACCOUNT_A-address');await h.settle();h.render();
      assert(h.tree.selectedAddressId==='ACCOUNT_B-address', 'Old account storage completion overwrote the active account address selection');
      return {source:h.sourceFile,source_SHA256:h.sourceSHA256,no_private_account_data_in_result:true};
    }],
  ]) {
    try {cases.push({ id, invariant, status: 'PASS', evidence: await fn() });}
    catch (e) {cases.push({ id, invariant, status: 'FAIL', failure: e.message });}
  }
  const result = { recorded_UTC: new Date().toISOString(), command: process.argv, source_directory: sourceDir, scope: 'Actual TSX transpilation/component functions with isolated React-hook/API doubles;not a browser/backend/native/provider acceptance test.', counts: { PASS: cases.filter(x => x.status === 'PASS').length, FAIL: cases.filter(x => x.status === 'FAIL').length, ERROR: 0, SKIPPED: 0 }, cases, safety: { production_accounts: false, API_calls: 0, native_modules: 0, provider_calls: 0, source_modified: false } };
  fs.writeFileSync(out, JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({ counts: result.counts, cases: cases.map(({ id, status, failure }) => ({ id, status, failure })) }));
  process.exitCode = result.counts.FAIL ? 1 : 0;
})().catch(error => { console.error(error.stack);process.exitCode = 2; });
