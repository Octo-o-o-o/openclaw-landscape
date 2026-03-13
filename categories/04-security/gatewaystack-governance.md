> https://github.com/davidcrowe/gatewaystack-governance

# GatewayStack Governance (5 stars)

## Problem & Solution
OpenClaw's tool calls lack a governance layer -- Agents can directly execute dangerous operations (reading SSH keys, running arbitrary commands) with no identity checks, rate limiting, or audit trails. GatewayStack Governance intercepts every tool call at the process level, enforcing five governance checks.

## Key Features
- **Five Core Checks** -- Identity (Agent ID mapped to governance identity) -> Scope (deny-by-default tool whitelist) -> Rate Limiting (sliding window limits) -> Injection Detection (40+ attack pattern scanning) -> Audit Logging (append-only JSONL)
- **Process-Level Interception** -- Via OpenClaw's `before_tool_call` event hook, Agents cannot bypass or skip checks
- **Three Optional Features** -- Output DLP (PII scanning and redaction), Escalation (human approval workflows), Behavioral Monitoring (anomaly detection)
- **GatewayStack Ecosystem Integration** -- Uses `@gatewaystack/transformabl-core` (DLP) and `@gatewaystack/limitabl-core` (behavioral monitoring)
- **Zero-Configuration Core** -- Core checks work without configuration; optional features are enabled via `policy.json`
- **One-Click Installation** -- `openclaw plugins install @gatewaystack/gatewaystack-governance`
