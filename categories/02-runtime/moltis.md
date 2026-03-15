> https://github.com/moltis-org/moltis

# Moltis (2,077 stars)

## Problem & Solution

Moltis addresses the security and auditability issues of OpenClaw. Traditional OpenClaw (TypeScript + Node.js, ~430K LoC) carries supply chain attack risks, memory safety concerns, and complex runtime dependencies. Moltis rewrites it in Rust with single-binary deployment, zero `unsafe` code, sandboxed isolated execution, a core of only ~5K LoC (Agent loop + model layer), full stack ~124K LoC, 3,100+ tests, and independently auditable code.

## Key Features

- **Memory Safety**: Rust ownership system + zero `unsafe` code (disabled at workspace level, optional only for FFI), eliminating memory vulnerabilities
- **Sandbox Isolation**: Docker + Apple Container dual-layer sandbox, per-session isolation, commands never execute on the host machine
- **Single-binary Deployment**: No Node.js, no npm, no runtime dependencies — 44MB single file, supports Mac Mini/Raspberry Pi/self-hosted servers
- **Auditable Architecture**: Core Agent loop ~5K LoC, 46 modular crates (~196K LoC), independently auditable, 3,100+ tests
- **Full-featured Built-in**: Voice (15+ providers), memory, scheduling, Telegram/Discord/WhatsApp, browser automation, MCP server, Hooks (15 event types)
- **Security by Design**: Secrets wrapped with `secrecy::Secret` (zeroed on drop), tool output sanitization, SSRF protection, Origin verification, Hook interception

<!-- lastCommit: 55d5543c9a73a21348f453980cd3f0aab308ca35 -->
