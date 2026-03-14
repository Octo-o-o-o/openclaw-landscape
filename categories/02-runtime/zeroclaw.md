> https://github.com/zeroclaw-labs/zeroclaw

# ZeroClaw

## Basic Info

- **GitHub**: https://github.com/zeroclaw-labs/zeroclaw
- **Stars**: 25,853
- **Language**: Rust
- **License**: MIT OR Apache-2.0
- **Website**: https://zeroclawlabs.ai
- **Community**: X (@zeroclawlabs), Telegram, Reddit (r/zeroclawlabs), Facebook

## Problem & Solution

### Core Problems

1. **Excessive resource overhead**: OpenClaw (TypeScript) requires >1GB RAM + Node.js runtime (~390MB), startup time exceeds 500 seconds on low-end hardware
2. **High deployment cost**: OpenClaw recommends Mac mini ($599) or high-spec Linux server; edge devices and low-cost hardware cannot run it
3. **Architecture lock-in**: Existing Agent frameworks typically bind to specific LLM providers, messaging channels, or tool ecosystems, resulting in high migration costs
4. **Insufficient security**: Lacks sandbox isolation, workspace restrictions, pairing authentication, and other enterprise-grade security mechanisms
5. **Slow cold starts**: Interpreted language runtimes have high startup latency, impacting CLI and daemon experience

### ZeroClaw's Solution

**Extreme Lightweight Design**:
- Single binary file (~8.8MB), no runtime dependencies
- Memory usage <5MB (release build)
- Cold start <10ms (0.8GHz core)
- Runs on $10 hardware (Raspberry Pi Zero, Orange Pi, etc.)

**Trait-driven Architecture**:
- All subsystems are Trait interfaces: Provider, Channel, Memory, Tool, Observer, RuntimeAdapter, SecurityPolicy
- Switch implementations with zero code changes (configuration file hot-reload)
- Supports custom endpoints (OpenAI-compatible / Anthropic-compatible)

**Security-first Design**:
- Gateway pairing authentication (one-time pairing code -> bearer token)
- Sandbox runtime (Docker isolation + resource limits)
- Workspace scoping (workspace_only mode + path whitelist)
- Command whitelist / blacklist
- Encrypted key storage (local key file)

**Full-stack Memory System** (no external dependencies):
- Vector database: SQLite BLOB + cosine similarity search
- Keyword search: FTS5 virtual tables + BM25 scoring
- Hybrid retrieval: Custom weighted merge function
- Embedding cache: LRU eviction strategy
- Supports PostgreSQL / Lucid / Markdown / None backends

## Core Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      ZeroClaw Runtime                        │
├─────────────────────────────────────────────────────────────┤
│  Trait Layer (all subsystems are pluggable interfaces)       │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │ Provider │ Channel  │  Memory  │   Tool   │ Observer │  │
│  │  (LLM)   │ (Messaging)│ (Storage)│ (Capabilities)│ (Monitoring)│  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │ Runtime  │ Security │ Identity │  Tunnel  │Heartbeat │  │
│  │ Adapter  │  Policy  │  Config  │          │  Engine  │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
├─────────────────────────────────────────────────────────────┤
│  Core Services                                               │
│  • Agent Loop (single-shot / interactive mode)               │
│  • Gateway (Webhook server, port 42617)                      │
│  • Daemon (long-running autonomous runtime)                  │
│  • Service Manager (systemd / OpenRC)                        │
├─────────────────────────────────────────────────────────────┤
│  Storage Layer                                               │
│  • SQLite (hybrid search: vector + FTS5)                     │
│  • PostgreSQL (remote memory backend)                        │
│  • Markdown (filesystem persistence)                         │
│  • Lucid (external memory bridge)                            │
└─────────────────────────────────────────────────────────────┘
```

### Key Design Patterns

**1. Trait-driven Pluggable Architecture**

Each subsystem is defined as a Rust Trait, with implementations dynamically selected via configuration at runtime:

```toml
[memory]
backend = "sqlite"  # Options: sqlite, postgres, lucid, markdown, none

[runtime]
kind = "native"     # Options: native, docker

[tunnel]
provider = "none"   # Options: none, cloudflare, tailscale, ngrok, custom
```

**2. Subscription Authentication (Subscription Auth)**

Supports OpenAI Codex OAuth and Claude Code subscription tokens:

```bash
# OAuth device code flow (headless servers)
zeroclaw auth login --provider openai-codex --device-code

# Multi-account profiles
zeroclaw auth use --provider openai-codex --profile work
```

- Storage file: `~/.zeroclaw/auth-profiles.json` (encrypted)
- Encryption key: `~/.zeroclaw/.secret_key`
- Profile ID format: `<provider>:<profile_name>`

**3. Hybrid Memory Search Engine**

Fully self-developed, zero external dependencies (no Pinecone / Elasticsearch / LangChain):

| Layer | Implementation |
|-------|---------------|
| Vector Database | SQLite BLOB + cosine similarity |
| Keyword Search | FTS5 virtual tables + BM25 |
| Hybrid Merge | Custom weighted function (`vector.rs`) |
| Embedding Generation | `EmbeddingProvider` trait (OpenAI / custom / noop) |
| Chunking Strategy | Line-based Markdown chunking + heading preservation |
| Cache | SQLite `embedding_cache` table + LRU eviction |

**4. Secure Sandbox Runtime**

```toml
[autonomy]
level = "supervised"  # readonly / supervised / full
workspace_only = true
allowed_commands = ["git", "npm", "cargo", "ls", "cat", "grep"]
forbidden_paths = ["/etc", "/root", "/proc", "/sys", "~/.ssh"]

[runtime.docker]
image = "alpine:3.20"
network = "none"
memory_limit_mb = 512
cpu_limit = 1.0
read_only_rootfs = true
```

**5. Gateway Pairing Authentication**

```
1. Client requests pairing code: GET /pair
2. Server generates one-time code (6-digit number)
3. Client submits pairing code: POST /pair (X-Pairing-Code header)
4. Server verifies and returns bearer token
5. Subsequent requests carry token: Authorization: Bearer <token>
```

## Key Features

### 1. Multi-channel Support (Channel Trait)

15+ built-in messaging channels:
- **Instant Messaging**: Telegram, Discord, Slack, Mattermost, Matrix, Signal, WhatsApp
- **Enterprise Collaboration**: Lark (Feishu), DingTalk, QQ
- **Legacy Protocols**: Email, IRC, Webhook
- **Emerging Protocols**: Nostr, Linq
- **Mobile**: iMessage (macOS)

Configuration example (Telegram):

```toml
[channels_config.telegram]
bot_token = "123456:ABC-DEF..."
allowed_chat_ids = [123456789, -1001234567890]
```

### 2. Multi-model Providers (Provider Trait)

Supports 20+ LLM providers:
- **Mainstream**: OpenAI, Anthropic, Google (Gemini), OpenRouter, Groq
- **Local**: Ollama, llama.cpp server
- **Subscription**: OpenAI Codex (ChatGPT), Claude Code
- **Custom**: OpenAI-compatible / Anthropic-compatible endpoints

```toml
default_provider = "openrouter"
default_model = "anthropic/claude-sonnet-4-6"

# Custom endpoints
# default_provider = "custom:https://your-api.com"
# default_provider = "anthropic-custom:https://your-api.com"
```

### 3. Skills System (Skills)

- TOML manifest + SKILL.md instructions
- Community skill packs (open-skills, disabled by default)
- Built-in security audit (blocks symlinks, script files, unsafe Markdown links, high-risk shell payloads)

```bash
zeroclaw skills list
zeroclaw skills install <source>
zeroclaw skills audit <source_or_name>
```

### 4. Heartbeat Tasks (Heartbeat)

Periodic autonomous task execution:

```toml
[heartbeat]
enabled = true
interval_minutes = 30
message = "Check London time"
target = "telegram"
to = "123456789"
```

Or use a `HEARTBEAT.md` file to define the task list.

### 5. Integration Ecosystem (Integrations)

70+ integrations across 9 categories:
- Communication (Telegram, Discord, Slack, Email, WhatsApp)
- Productivity (Todoist, Notion, Google Calendar)
- Development (GitHub, GitLab, Jira, Linear)
- Data (PostgreSQL, Redis, S3)
- Monitoring (Prometheus, Grafana)
- Payments (Stripe, PayPal)
- AI (Composio - 1000+ OAuth apps, optionally enabled)

```bash
zeroclaw integrations info Telegram
```

### 6. AIEOS Identity Specification

Supports [AIEOS v1.1](https://aieos.org) (AI Entity Object Specification) for standardized identity:

```toml
[identity]
format = "aieos"
aieos_path = "identity.json"
```

Or inline JSON:

```toml
[identity]
format = "aieos"
aieos_inline = '''
{
  "identity": {"names": {"first": "Nova"}},
  "psychology": {"neural_matrix": {"creativity": 0.9}},
  "linguistics": {"text_style": {"formality_level": 0.2}},
  "motivations": {"core_drive": "Push boundaries"},
  "capabilities": {"skills": [{"name": "Rust engineering"}]}
}
'''
```

### 7. Browser Tool (Optionally Enabled)

```toml
[browser]
enabled = true
allowed_domains = ["docs.rs"]
backend = "agent_browser"  # agent_browser / rust_native / computer_use / auto
native_headless = true
native_webdriver_url = "http://127.0.0.1:9515"
```

Three backends:
- **agent_browser**: Default, lightweight
- **rust_native**: Requires WebDriver (chromedriver / selenium)
- **computer_use**: External sidecar HTTP endpoint (mouse/keyboard control)

### 8. Migration Tool

Migrate memory from OpenClaw:

```bash
zeroclaw migrate openclaw --dry-run
zeroclaw migrate openclaw
```

### 9. Service Management

Supports systemd (user-level) and OpenRC (system-level):

```bash
# Linux (systemd, no sudo required)
zeroclaw service install
zeroclaw service start

# Alpine (OpenRC, requires sudo)
sudo zeroclaw service install
sudo rc-update add zeroclaw default
sudo rc-service zeroclaw start
```

### 10. One-click Installation

```bash
# Recommended: Clone and run locally
git clone https://github.com/zeroclaw-labs/zeroclaw.git
cd zeroclaw
./install.sh

# Optional: Install system dependencies + Rust
./install.sh --install-system-deps --install-rust

# Optional: Prefer prebuilt binaries (low RAM/disk hosts)
./install.sh --prefer-prebuilt

# Optional: Binary-only install (no source build fallback)
./install.sh --prebuilt-only

# Optional: Run onboarding at the same time
./install.sh --onboard --api-key "sk-..." --provider openrouter

# Remote one-click install (review before running in production)
curl -fsSL https://raw.githubusercontent.com/zeroclaw-labs/zeroclaw/main/install.sh | bash
```

<!-- lastCommit: 06f65fb -->
