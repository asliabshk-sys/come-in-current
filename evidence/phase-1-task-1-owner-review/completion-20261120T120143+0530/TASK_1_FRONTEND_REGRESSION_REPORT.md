# Frontend regression report

- `yarn typecheck`: PASS, 0 TypeScript errors.
- `EXPO_NO_TELEMETRY=1 yarn lint`: PASS.
- `EXPO_NO_TELEMETRY=1 EXPO_PUBLIC_BACKEND_URL=http://127.0.0.1:8000 yarn build:web`: PASS.
- Lifecycle harness: 3 PASS — checkout eligibility refresh, account-scoped services responses, account-scoped persisted address completion.
- CHAND party planner: 11 assertions PASS.

The first Expo lint/build attempts failed before execution because Expo attempted to create an unwritable telemetry directory. The no-telemetry reruns passed and are the final evidence. JSX/UI markup, theme, colors and navigation were unchanged. Android/iOS validation was not run.
