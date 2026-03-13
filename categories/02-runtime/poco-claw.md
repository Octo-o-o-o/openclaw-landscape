> https://github.com/poco-ai/poco-claw

# Poco-Claw (1,131 stars)

## Problem & Solution

Poco-Claw addresses the security and usability issues of OpenClaw. Traditional OpenClaw executes commands on the host machine, posing security risks; the CLI interface has a high barrier for non-technical users; and it lacks mobile support and IM integration. Poco provides a more polished Web UI, built-in sandbox runtime, IM integration (DingTalk/Telegram), mobile support, and intelligent memory (mem0), all powered by a Claude Code Agent underneath.

## Key Features

- **Security Sandbox**: All tasks run in isolated containers — installing dependencies, modifying files, and executing commands do not affect the host environment
- **Rich UI**: Plan Mode, session queue, session termination, project management, file upload, Artifacts view (HTML/PDF/Markdown/Xmind/Excalidraw/Drawio), Playback view (command I/O/browser sessions/MCP tool calls)
- **Native Claude Code Experience**: Slash Commands, Plan Mode, AskQuestion, MCP & Skills, built-in browser, GitHub repository integration
- **Background Execution + Scheduled Triggers**: Agents can run continuously in the cloud even after closing the browser, with scheduled task support
- **Multi-device Interaction**: Mobile support, IM integration (DingTalk/Telegram), push notifications, event subscriptions
- **Intelligent Memory (mem0)**: Remembers user preferences, project context, and interaction history to provide personalized assistance
