> https://github.com/DingTalk-Real-AI/connector

# DingTalk OpenClaw Connector (1,604 stars)

## Problem & Solution
Solves the integration problem where DingTalk enterprise users cannot directly use OpenClaw Gateway. By connecting DingTalk bots and DEAP Agents to OpenClaw Gateway via Stream mode, it supports AI Card streaming responses, session persistence, and rich media messages, enabling enterprise users to seamlessly use AI Agent capabilities within DingTalk.

## Core Architecture
- **Stream WebSocket connection** — DingTalk messages are pushed to the Connector via Stream mode, requiring no public IP or webhook configuration
- **HTTP SSE streaming forwarding** — The Connector calls the Gateway `/v1/chat/completions` endpoint, converting SSE chunks in real-time to the DingTalk AI Card streaming API
- **Session and memory isolation** — Maintains separate sessions and memory for direct messages/group chats/group-level contexts, with configurable cross-session memory sharing
- **Multi-Agent routing** — A single Connector instance can connect to multiple Agents, with different DingTalk bots bound to different Agents for role-based task distribution

## Key Features
- **AI Card streaming responses** — Typewriter-effect real-time display of AI replies for improved user experience
- **Rich media support** — Receives JPEG/PNG images, parses .docx/.pdf/.xlsx file attachments, and sends audio messages
- **DingTalk Document API** — Supports creating, appending to, searching, and listing DingTalk documents for knowledge base integration
- **Async mode** — Immediately acknowledges user messages, processes tasks in the background, and proactively pushes results; suitable for time-consuming tasks
- **Markdown table conversion** — Automatically converts Markdown tables to DingTalk-compatible text format
