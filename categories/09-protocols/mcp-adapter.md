> https://github.com/androidStern/mcp-adapter

# openclaw-mcp-adapter (N/A stars)

## Problem & Solution

Tools provided by MCP (Model Context Protocol) servers cannot be directly invoked by OpenClaw Agents — they need to be wrapped through CLI Skills, adding extra call layers and latency. This plugin automatically connects to MCP servers at OpenClaw startup, discovers and registers their tools as native Agent tools, enabling zero-middleware direct invocation.

## Key Features

- **Auto-Discovery at Startup** — Connects to configured MCP servers when the Gateway starts, automatically discovers and registers all tools as first-class citizen tools
- **Dual Transport Protocol Support** — Supports both stdio (subprocess launch) and HTTP (connect to running servers) transport modes
- **Tool Name Prefixing** — Optional `toolPrefix` configuration to avoid tool name conflicts across multiple servers (e.g., `myserver_toolname`)
- **Sandbox Integration** — Supports adding MCP tools to the sandbox tool whitelist for fine-grained permission control
- **Environment Variable Substitution** — Supports `${VAR}` syntax in configuration for referencing environment variables, enabling secure API key management
- **TypeScript Implementation** — Built with TypeScript, providing type safety and a good developer experience

<!-- lastCommit: 6a7050b -->
