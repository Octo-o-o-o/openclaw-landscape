> https://github.com/cloudflare/moltworker

# cloudflare/moltworker

## Basic Info

- **GitHub**: https://github.com/cloudflare/moltworker
- **Stars**: 9,558
- **Language**: TypeScript
- **Created**: 2026-01-27
- **Last Updated**: 2026-03-11
- **Description**: Run OpenClaw (formerly Moltbot/Clawdbot) personal AI assistant on Cloudflare Workers

## Problem & Solution

### Core Problems

1. **High self-hosting barrier**: Traditional AI assistants require users to maintain servers, handle operations (process management, logs, backups, security updates)
2. **Unpredictable costs**: 24/7 VPS or cloud instances are expensive with low resource utilization
3. **Slow cold starts**: Containerized deployments have long cold start times (1-2 minutes), impacting user experience
4. **Difficult data persistence**: How to save conversation history, configuration, and paired devices in stateless container environments

### Solution

**Serverless containerized deployment**: Package OpenClaw as a Docker image running in Cloudflare Sandbox containers, leveraging Cloudflare Workers' global edge network to achieve:

1. **Zero-ops deployment**: One-click deployment to Cloudflare Workers, no server management required
2. **Pay-per-use billing**: Containers can be configured to sleep after idle (`SANDBOX_SLEEP_AFTER`), reducing costs to ~$5-6/month (running only 4 hours/day)
3. **Global acceleration**: Leverages Cloudflare's CDN network for low-latency access worldwide
4. **R2 persistence**: Configuration and conversation history persist across container restarts via R2 object storage (auto-backup every 5 minutes)
5. **Multi-layer authentication**: Cloudflare Access (admin auth) + Gateway Token (Control UI access) + Device Pairing (device pairing) — three layers of security

## Core Architecture

### Tech Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    Cloudflare Workers                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Hono Web Framework                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐     │   │
│  │  │ Admin UI   │  │  API       │  │  Debug     │     │   │
│  │  │ (/_admin/) │  │  (/api/*)  │  │  (/debug/*) │     │   │
│  │  └────────────┘  └────────────┘  └────────────┘     │   │
│  │                                                      │   │
│  │  ┌────────────────────────────────────────────────┐ │   │
│  │  │     Cloudflare Access JWT Middleware          │ │   │
│  │  └────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Cloudflare Sandbox Container                 │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │  OpenClaw Gateway (Node.js 22 + pnpm)         │  │   │
│  │  │  - WebSocket Server (ws://localhost:18789)    │  │   │
│  │  │  - HTTP API                                    │  │   │
│  │  │  - Device Pairing                              │  │   │
│  │  │  - Multi-channel Support                       │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  │                                                        │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │  Skills (Browser Automation, Custom Tools)     │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              R2 Object Storage                       │   │
│  │  - Config Backup (every 5 min)                      │   │
│  │  - Conversation History                             │   │
│  │  - Paired Devices                                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Browser Rendering (CDP Shim)                 │   │
│  │  - Headless Chrome for Web Automation               │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  Anthropic / OpenAI    │
              │  (via AI Gateway)      │
              └────────────────────────┘
```

### Key Components

1. **Worker Layer (TypeScript + Hono)**
   - `src/index.ts`: Main application entry point, route mounting
   - `src/auth/`: Cloudflare Access JWT authentication (JWKS verification, middleware)
   - `src/gateway/`: OpenClaw process management (startup, environment variables, R2 mounting, backup sync)
   - `src/routes/`: API routes (device management, gateway control, debug endpoints)
   - `src/client/`: React admin interface (device pairing, R2 status, gateway restart)

2. **Container Layer (Docker + OpenClaw)**
   - Base image: `cloudflare/sandbox:0.7.0`
   - Node.js 22 + pnpm + OpenClaw 2026.2.3
   - Startup script: `start-openclaw.sh` (R2 restore -> start gateway -> scheduled backup)
   - Pre-installed skills: `skills/cloudflare-browser` (CDP client, screenshots, video recording)

3. **Persistence Layer (R2 + rclone)**
   - Restore configuration from R2 to `/root/.openclaw` on startup
   - Auto-sync to R2 every 5 minutes during runtime
   - Admin interface provides a "Backup Now" button

4. **Authentication Layer (Three-tier Protection)**
   - **Cloudflare Access**: Protects `/_admin/`, `/api/*`, `/debug/*` routes via JWT verification
   - **Gateway Token**: Accessing Control UI requires a `?token=` query parameter
   - **Device Pairing**: New devices must be explicitly approved via the admin interface

### Deployment Flow

```bash
# 1. Install dependencies
npm install

# 2. Configure AI provider (choose one)
npx wrangler secret put ANTHROPIC_API_KEY
# Or use Cloudflare AI Gateway
npx wrangler secret put CLOUDFLARE_AI_GATEWAY_API_KEY
npx wrangler secret put CF_AI_GATEWAY_ACCOUNT_ID
npx wrangler secret put CF_AI_GATEWAY_GATEWAY_ID

# 3. Generate and set Gateway Token
export MOLTBOT_GATEWAY_TOKEN=$(openssl rand -hex 32)
echo "$MOLTBOT_GATEWAY_TOKEN" | npx wrangler secret put MOLTBOT_GATEWAY_TOKEN

# 4. Deploy
npm run deploy

# 5. Configure Cloudflare Access (protect admin interface)
# Enable Cloudflare Access in Workers & Pages dashboard
npx wrangler secret put CF_ACCESS_TEAM_DOMAIN
npx wrangler secret put CF_ACCESS_AUD

# 6. Configure R2 persistence (optional but recommended)
npx wrangler secret put R2_ACCESS_KEY_ID
npx wrangler secret put R2_SECRET_ACCESS_KEY
npx wrangler secret put CF_ACCOUNT_ID
```

## Key Features

### 1. Serverless Container Orchestration

- **Durable Objects**: Each Worker binds to a Sandbox Durable Object, ensuring single-instance operation
- **Container Lifecycle Management**:
  - Default `SANDBOX_SLEEP_AFTER=never` (never sleep, recommended for production)
  - Configurable idle timeout (e.g., `10m`, `1h`) to reduce costs
  - Cold start time 1-2 minutes, subsequent requests respond quickly
- **Process Monitoring**: Starts OpenClaw via `sandbox.startProcess()`, auto-restarts failed processes

### 2. R2 Persistence Strategy

**Backup/Restore Pattern** (simplified design, no OpenClaw code modifications required):

```bash
# Restore on startup
if [ -d /mnt/r2/.openclaw ]; then
  cp -r /mnt/r2/.openclaw /root/
fi

# Scheduled backup during runtime (every 5 minutes)
while true; do
  sleep 300
  rclone sync /root/.openclaw r2:moltbot-data/.openclaw
done
```

**Advantages**:
- Conversation history, paired devices, and configuration files persist across container restarts
- Admin interface displays last backup time, supports manual backup triggering
- Runs without R2 credentials (uses temporary storage)

### 3. Multi-layer Authentication System

| Layer | Scope | Auth Method | Purpose |
|-------|-------|-------------|---------|
| Cloudflare Access | `/_admin/*`, `/api/*`, `/debug/*` | JWT (JWKS verification) | Admin identity verification |
| Gateway Token | Control UI (`/?token=`) | Query parameter | Prevent unauthorized access |
| Device Pairing | All devices (browser, CLI, chat platforms) | Pairing code + admin approval | Device-level access control |

**Local Development Mode**: Set `DEV_MODE=true` to skip Cloudflare Access authentication and enable `allowInsecureAuth` (bypass device pairing)

### 4. Browser Automation (CDP Shim)

Leverages Cloudflare Browser Rendering to provide Chrome DevTools Protocol endpoints:

```typescript
// Endpoints
GET  /cdp/json/version          // Browser version info
GET  /cdp/json/list             // Available targets list
GET  /cdp/json/new              // Create new target
WS   /cdp/devtools/browser/{id} // CDP WebSocket connection

// Authentication: All endpoints require ?secret=<CDP_SECRET>
```

**Pre-installed Skills**:
- `cloudflare-browser/scripts/screenshot.js`: Web page screenshots
- `cloudflare-browser/scripts/video.js`: Multi-page video recording
- `cloudflare-browser/scripts/cdp-client.js`: Reusable CDP client library

### 5. AI Gateway Integration

**Native Cloudflare AI Gateway support** (caching, rate limiting, analytics, cost tracking):

```bash
# Configure AI Gateway (takes priority over direct API keys)
npx wrangler secret put CLOUDFLARE_AI_GATEWAY_API_KEY  # Upstream provider API key
npx wrangler secret put CF_AI_GATEWAY_ACCOUNT_ID
npx wrangler secret put CF_AI_GATEWAY_GATEWAY_ID

# Optional: Override default model (default: Claude Sonnet 4.5)
npx wrangler secret put CF_AI_GATEWAY_MODEL
# Example: workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast
```

**Supported Providers**:
- Workers AI (Unified Billing, no separate API key required)
- Anthropic, OpenAI, Groq, etc. (API key forwarded via gateway)

### 6. Admin Interface Features

Access `/_admin/` (requires Cloudflare Access authentication):

- **R2 Storage Status**: Displays whether R2 is configured, last backup time, "Backup Now" button
- **Gateway Control**: Restart OpenClaw gateway process
- **Device Pairing**:
  - View pending approval device list
  - Individual or batch approval
  - View paired devices

### 7. Debug Endpoints

Accessible when `DEBUG_ROUTES=true` is enabled (requires Cloudflare Access):

```
GET /debug/processes              # List all processes in the container
GET /debug/logs?id=<process_id>   # Get logs for a specific process
GET /debug/version                # Container and OpenClaw version info
```

### 8. Cost Optimization

**Standard configuration cost estimate** (`standard-1` instance: 1/2 vCPU, 4 GiB memory, 8 GB disk):

| Resource | Monthly Usage (24/7) | Free Tier | Overage | Approx. Cost |
|----------|---------------------|-----------|---------|--------------|
| Memory | 2,920 GiB-hrs | 25 GiB-hrs | 2,895 GiB-hrs | ~$26/month |
| CPU (10% utilization) | ~2,190 vCPU-min | 375 vCPU-min | ~1,815 vCPU-min | ~$2/month |
| Disk | 5,840 GB-hrs | 200 GB-hrs | 5,640 GB-hrs | ~$1.50/month |
| Workers Paid Plan | - | - | - | $5/month |
| **Total** | - | - | - | **~$34.50/month** |

**Optimization Strategies**:
- Configure `SANDBOX_SLEEP_AFTER=10m` to sleep when idle
- Running only 4 hours/day can reduce costs to ~$5-6/month (plus $5 plan fee)
- Choose smaller instances (`lite`: 256 MiB/$0.50/month) or larger instances (`standard-4`: 12 GiB)

<!-- lastCommit: aa5f75b -->
