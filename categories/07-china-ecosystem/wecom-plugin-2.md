> https://github.com/11haonb/wecom-plugin

# WeCom OpenClaw Plugin (95 stars)

## Problem & Solution
OpenClaw lacks native integration with WeCom (Enterprise WeChat), making it impossible to remotely control Agents through enterprise communication tools. This plugin enables bidirectional communication via the WeCom application interface, allowing users to send messages through WeCom to control PC browsers and execute AI tasks.

## Key Features
- **Bidirectional message channel** — Send messages via WeCom, AI processes and returns responses, supporting remote browser control
- **Rich media support** — Supports sending and receiving images, voice, video, and files
- **Tool call integration** — AI can execute 100+ built-in tools, triggered via WeCom tasks
- **Callback server** — Built-in webhook server for handling WeCom message push, supporting Token and AES encryption verification
- **TypeScript implementation** — Node.js 18+ + TypeScript, complete type safety and documentation support
- **Quick configuration** — Configure enterprise ID, Secret, Agent ID, and other credentials via `~/.openclaw/openclaw.json`

<!-- lastCommit: 6a7050b -->
