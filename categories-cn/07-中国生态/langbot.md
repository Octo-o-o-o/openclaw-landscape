> https://github.com/langbot-app/LangBot

# LangBot (15574 stars)

## Problem & Solution

LangBot 旨在解决将 AI 助手和 Agent 与多个即时通讯（IM）平台集成的复杂性。它提供了一个生产级的开发平台，用于构建具备代理能力的 IM 机器人，并采用统一的架构设计。

## Key Features

- **多平台支持** — 集成 Discord、Slack、LINE、Telegram、微信、飞书、钉钉、QQ 等。
- **模型不可知** — 支持 OpenAI、Claude、Gemini、DeepSeek、Dify 以及本地大模型。
- **Agent 编排** — 提供知识库编排功能和高度可扩展的插件系统。
- **OpenClaw 替代方案** — 可作为轻量级的 OpenClaw 运行时替代方案进行集成。

## Core Architecture

该系统采用模块化插件架构，将 IM 平台连接器与核心 AI 路由引擎解耦。这种设计使得在不更改底层机器人基础设施的情况下，能够无缝切换不同的大语言模型。

## Tech Stack

- Python, FastAPI, SQLAlchemy, LangChain

<!-- lastCommit: 8bd6442965bd1c5187a726e3ec11d7605a25b2fc -->
