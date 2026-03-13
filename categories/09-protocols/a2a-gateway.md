> https://github.com/win4r/a2a-gateway

# openclaw-a2a-gateway (162 stars)

## Problem & Solution

OpenClaw Agents on different servers cannot communicate directly due to the lack of a standardized inter-Agent communication protocol. This plugin implements the A2A (Agent-to-Agent) v0.3.0 protocol, providing JSON-RPC + REST endpoints, Agent Card publishing, Bearer Token authentication, and end-to-end support for A2A Part types (TextPart, FilePart, DataPart), enabling cross-server Agent communication.

## Key Features

- **A2A v0.3.0 Protocol Implementation** — JSON-RPC + REST endpoints with `/.well-known/agent-card.json` Agent Card publishing (backward compatible with `/.well-known/agent.json` legacy format)
- **Bearer Token Authentication** — Secure authentication for inter-Agent communication
- **A2A Part Type Support** — End-to-end handling of TextPart (text), FilePart (URI + base64), and DataPart (structured JSON)
- **`a2a_send_file` Agent Tool** — Agents can programmatically send files to Peer Agents
- **Zero-Configuration Quick Start** — Default Agent Card (`name: "OpenClaw A2A Gateway"`, `skills: [chat]`), ready to install and load without manual configuration
- **Peer Management** — Configure Peer Agent URLs and authentication info, supports Tailscale/LAN/public IP
- **Inbound Message Routing** — Routes A2A messages to OpenClaw Agents and returns responses

<!-- lastCommit: 6a7050b -->
