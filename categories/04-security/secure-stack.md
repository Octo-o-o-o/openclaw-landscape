> https://github.com/yi-john-huang/secure-stack

# OpenClaw Secure Stack (N/A stars)

## Problem & Solution
Self-hosted OpenClaw faces security risks including malicious skills, prompt injection, unauthorized access, and data leakage. Secure Stack wraps an unmodified OpenClaw instance behind a reverse proxy, providing authentication, skill scanning, prompt injection mitigation, pre-execution governance, webhook integration, network isolation, and full audit logging.

## Key Features
- **Multi-Stage Security Pipeline** -- Auth Middleware (Bearer token constant-time comparison) -> Governance (tool call intent classification, policy validation, human approval) -> Sanitizer (prompt injection pattern scanning) -> OpenClaw -> Response Scanner (indirect injection detection) -> Audit Log
- **Webhook Security Relay** -- Telegram/WhatsApp messages are forwarded after signature verification, rate limiting, replay protection, and size checks, supporting HMAC-SHA256 and secret tokens
- **Plugin Hook System** -- TypeScript plugins (`prompt-guard`) run inside OpenClaw, intercepting indirect injection in tool results (`tool_result_persist` hook) and high-risk tool calls (`before_tool_call` hook)
- **Offline Skill Scanning** -- tree-sitter AST analysis detects dangerous APIs (eval, child_process), network exfiltration (fetch, http), filesystem abuse (writeFile, rmSync), isolated to SQLite
- **DNS Whitelisting** -- CoreDNS blocks outbound traffic from skills to non-approved domains
- **One-Click Deployment** -- Docker Compose + Caddy auto HTTPS, `install.sh` auto-installs the `prompt-guard` plugin

<!-- lastCommit: 6a7050b -->
