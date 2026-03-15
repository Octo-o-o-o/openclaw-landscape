> https://github.com/freema/openclaw-mcp

# openclaw-mcp (67 stars)

## Problem & Solution

Claude.ai users cannot directly communicate with self-hosted OpenClaw instances, relying solely on messaging channels (WhatsApp/Telegram). openclaw-mcp establishes a secure bridge between Claude.ai and self-hosted OpenClaw via the MCP protocol and OAuth2 authentication, enabling "AI assistant orchestrating AI assistant" capabilities (Claude.ai delegates tasks to OpenClaw, which invokes Claude Code for execution).

## Key Features

- **OAuth2 Secure Authentication** — Supports `MCP_CLIENT_ID` / `MCP_CLIENT_SECRET` / `MCP_ISSUER_URL` three-parameter authentication to prevent unauthorized access
- **Dual Transport Mode** — Local stdio mode (Claude Desktop) and remote SSE mode (Claude.ai), switchable via the `--transport` parameter
- **Docker One-Click Deployment** — Provides the `ghcr.io/freema/openclaw-mcp` image with version pinning support (e.g., `:1.1.0`) and `read_only` container security hardening
- **Reverse Proxy Compatibility** — Requires `MCP_ISSUER_URL` to be set to a public HTTPS URL, preventing OAuth metadata from exposing `http://localhost:3000` and causing authentication failures
- **Precise CORS Control** — Restricts cross-origin request origins via `CORS_ORIGINS=https://claude.ai` to prevent CSRF attacks
- **Configurable Timeout** — `OPENCLAW_TIMEOUT_MS` parameter supports long-running tasks (default 300 seconds), accommodating time-consuming operations like Claude Code

<!-- lastCommit: 576ad0734cc0d5feb83b008983346b500f7f0afe -->
