> https://github.com/microclaw/microclaw

# MicroClaw

| Field | Value |
|-------|-------|
| Repository | [microclaw/microclaw](https://github.com/microclaw/microclaw) |
| Stars | 558 |
| Language | Rust |
| License | MIT |
| Last Active | 2026-03 (actively developed) |

## Introduction

MicroClaw is an Agentic AI assistant built with Rust, inspired by NanoClaw, focused on providing intelligent Agent capabilities within chat platforms. It supports multiple chat platforms (Telegram, Discord, Slack, Feishu, IRC) and multiple LLM providers, with full tool execution capabilities.

## Core Features

- **Agentic Tool Use** — bash commands, file read/write/edit, glob search, regex grep, persistent memory
- **Session Resumption** — Complete conversation state (including tool interactions) persists across messages
- **Context Compression** — Automatically summarizes old messages when sessions become too long
- **Sub-Agents** — Can spawn parallel sub-Agents to handle independent subtasks
- **Skills System** — Extensible skills system, compatible with the Anthropic Skills format
- **Plan & Execute** — TODO tool for decomposing complex tasks
- **Web Search** — Search and web page parsing via DuckDuckGo
- **Scheduled Tasks** — Supports cron-based recurring and one-time scheduled tasks
- **Persistent Memory** — Global, Bot-level, and chat-level AGENTS.md
- **MCP Integration** — Playwright MCP Bridge for browser automation
- **ACP Server** — Can run as an Agent Client Protocol server
- **Message Chunking** — Automatically splits long messages according to platform limits

## Supported Platforms

Telegram / Discord / Slack / Feishu / IRC

## Tool List

bash, read_file, write_file, edit_file, glob, grep, read_memory, write_memory, web_search, web_fetch, send_message, schedule_task, sessions_spawn, subagents series, activate_skill, todo_read/write, etc.

## Technical Architecture

- Platform-extensible architecture: shared Agent loop + tool system + storage layer, with platform adapters handling channel-specific logic
- Docker sandbox support
- Each message triggers an Agentic loop, up to 100 iterations

<!-- lastCommit: 9f6f3b7 -->
