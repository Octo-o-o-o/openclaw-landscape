> https://github.com/clawdotnet/openclaw.net

# OpenClaw.NET (84 stars)

## Problem & Solution
OpenClaw is natively based on Node.js/TypeScript and lacks native support in the .NET ecosystem. OpenClaw.NET provides a complete .NET implementation (with NativeAOT support), including Gateway + Agent Runtime, supporting C# native tools and Node.js plugin bridging.

## Key Features
- **Dual Runtime Modes** — `aot` mode (trim-safe, low memory) and `jit` mode (extension bridging, dynamic plugins), configured via `OpenClaw:Runtime:Mode`
- **Layered Startup Architecture** — Bootstrap (config loading, validation) -> Composition (service registration) -> Profiles (runtime selection) -> Pipeline (middleware, endpoints)
- **Multi-client Support** — Web UI (`/chat`), WebSocket (`/ws`), CLI (`OpenClaw.Cli`), Desktop Companion (`OpenClaw.Companion`)
- **Webhook Channels** — Inbound message handling for Telegram, Twilio, WhatsApp, and generic webhooks
- **18+ Native Tools** — File operations, shell execution, web search, and more implemented natively in C#, with better performance than Node.js bridging
- **Hardened Security Configuration** — Provides dev/staging/prod three-tier security configuration templates, supports `--doctor` mode for configuration validation
