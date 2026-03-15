> https://github.com/langbot-app/LangBot

# LangBot (15574 stars)

## Problem & Solution

LangBot is designed to solve the complexities of integrating AI assistants and agents with multiple instant messaging platforms. It provides a production-grade platform for building agentic IM bots with a unified architecture.

## Key Features

- **Multi-Platform Support** — Integrates with Discord, Slack, LINE, Telegram, WeChat, Feishu, DingTalk, QQ, and more.
- **Model Agnostic** — Supports OpenAI, Claude, Gemini, DeepSeek, Dify, and local models.
- **Agent Orchestration** — Features knowledge base orchestration and an extensible plugin system.
- **OpenClaw Alternative** — Can be integrated as a lightweight OpenClaw runtime alternative.

## Core Architecture

The system utilizes a modular plugin architecture that decouples the IM platform connectors from the core AI routing engine. This allows seamless swapping of language models without changing the underlying bot infrastructure.

## Tech Stack

- Python, FastAPI, SQLAlchemy, LangChain

<!-- lastCommit: 8bd6442965bd1c5187a726e3ec11d7605a25b2fc -->
