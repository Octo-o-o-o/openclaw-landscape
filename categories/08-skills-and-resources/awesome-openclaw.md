> https://github.com/SamurAIGPT/awesome-openclaw

# SamurAIGPT/awesome-openclaw

## Basic Information

- **Stars**: 778
- **URL**: https://github.com/SamurAIGPT/awesome-openclaw
- **License**: CC0 1.0 (Public Domain)
- **Type**: Resource list (Awesome List)
- **Author**: Anil Chandra Naidu Matcha (@matchaman11)

## Problem & Solution

### Core Problem

The OpenClaw ecosystem is evolving rapidly, with community projects, tools, tutorials, and articles scattered across various platforms, making it difficult for users:

1. **Scattered resources**: Community projects, skills, tutorials, and articles are spread across GitHub, Medium, YouTube, and other platforms
2. **Information overload**: A large number of new projects and articles are published daily, making it hard to filter for quality resources
3. **Lack of categorization**: Resources are not systematically categorized, making it difficult to quickly find what you need
4. **Slow updates**: Official documentation updates lag behind the faster-moving community resources
5. **Poor beginner-friendliness**: Lacks a complete learning path from beginner to advanced

### Solution

awesome-openclaw is a **curated OpenClaw resource list** providing:

- **700+ community skills**: ClawHub official skill store
- **12+ messaging platform integrations**: WhatsApp, Telegram, Discord, Slack, etc.
- **50+ external service integrations**: GitHub, Gmail, Spotify, Obsidian, etc.
- **13,000+ MCP servers**: Model Context Protocol ecosystem
- **Community project categories**: Web clients, deployment tools, memory systems, enterprise solutions, etc.
- **Tutorials and articles**: Complete learning path from beginner to advanced
- **Security resources**: Best practices, security tools, known risks

## Core Architecture

### Resource Classification System

```
awesome-openclaw/
├── Official Resources
│   ├── OpenClaw Website
│   ├── GitHub Repository (150k+ stars)
│   ├── Official Documentation
│   ├── ClawHub (Skill Store)
│   └── Release Notes
├── Quick Start
│   ├── Installation Guide
│   ├── First Configuration
│   └── Web Dashboard
├── Installation Guides
│   ├── Official Guide
│   ├── Platform Guides (macOS/Linux/Windows/Docker/Cloud)
│   └── Hosted Services (OctoClaw, SlackClaw)
├── Skills and Plugins
│   ├── Skill Registries (ClawHub, AgentFund, ClawdTalk, etc.)
│   ├── Popular Skills (LinkedIn, X/Twitter, etc.)
│   ├── Skill Categories (Productivity, Development, Smart Home, etc.)
│   └── Plugin Development
├── Integrations
│   ├── Messaging Platforms (12+)
│   └── External Services (50+)
├── MCP Support
│   ├── MCP Resources
│   └── MCP Server List
├── Tutorials and Guides
│   ├── Beginner Tutorials
│   └── Advanced Tutorials
├── Articles and News
│   ├── Origins and History
│   ├── Industry Coverage
│   └── Security Analysis
├── Community
│   ├── Official Channels
│   ├── Events (ClawCon)
│   └── Creators
├── Community Projects
│   ├── Web Clients and UI
│   ├── Deployment and Infrastructure
│   ├── Memory and Storage
│   ├── Enterprise Solutions
│   ├── China IM Integrations
│   ├── Monitoring and Tools
│   ├── Trading and Finance
│   ├── Development Workflows
│   ├── Content and Publishing
│   ├── Marketplaces
│   └── Other
├── Alternatives and Comparisons
│   ├── Alternatives List
│   └── Comparison Resources
├── Security
│   ├── Best Practices
│   ├── Security Tools
│   ├── Security Resources
│   └── Known Risks
└── FAQ
```

### Data Structure

**Tabular resource list**:

```markdown
| Project | Stars | Description |
|---------|-------|-------------|
| [clawterm](https://github.com/nicholaschen/clawterm) | - | Terminal-based OpenClaw client |
| [MobileClaw](https://github.com/wende/mobileclaw) | NEW | Mobile-first PWA client for OpenClaw |
```

**Categorized list**:

```markdown
### Beginner

| Tutorial | Source | Description |
|----------|--------|-------------|
| [What is OpenClaw?](https://medium.com/@gemQueenx/...) | Medium | Setup + Features guide |
```

## Key Features

### 1. Community Project Categories (200+ projects)

#### Web Clients and UI (7)

| Project | Stars | Description |
|---------|-------|-------------|
| **MobileClaw** | NEW | Mobile-first PWA client with real-time tool calls, inline diffs, sub-Agent activity streams |
| **Nerve** | NEW | Self-hosted web cockpit with real-time streaming, reasoning blocks, voice I/O, sub-Agent session monitoring |
| **SwarmClaw** | NEW | Self-hosted AI Agent orchestration dashboard with multi-provider support and task scheduling |
| **PinchChat** | - | Open-source webchat UI with ChatGPT-style interface and real-time tool call visualization |
| **webclaw** | 155+ | Fast, minimalist OpenClaw web client |

#### Deployment and Infrastructure (10)

| Project | Stars | Description |
|---------|-------|-------------|
| **moltworker** | 7.9k | Run OpenClaw on Cloudflare Workers |
| **OpenClaw Easy** | NEW | Zero-config OpenClaw desktop app (macOS/Windows), no terminal needed |
| **OpenClawInstaller** | 1.3k | OpenClaw one-click deployment tool |
| **OpenClaw Kit (TurboStarter)** | NEW | Opinionated OpenClaw wrapper starter kit with infrastructure, auth, and billing |
| **MimiClaw** | NEW | Run OpenClaw on a $5 ESP32-S3 chip, no Linux or Node.js required |
| **openclaw-self-healing** | NEW | 4-layer autonomous self-healing system with Claude Code as emergency doctor |
| **OctoClaw** | NEW | Fully managed OpenClaw hosting (German Hetzner), GDPR compliant |
| **SlackClaw** | NEW | Managed OpenClaw deployment designed for Slack workspaces |
| **PhoneClaw** | NEW | Automate all Android phone apps |
| **LightClaw** | NEW | Lightweight OpenClaw-inspired Python Agent core |

#### Memory and Storage (4)

| Project | Stars | Description |
|---------|-------|-------------|
| **memU** | 8k | Persistent memory layer for proactive Agents |
| **Agent Second Brain** | 152 | Complete second brain system: voice notes to Telegram to Obsidian vault + Todoist tasks |
| **clawmem** | - | Vector-based memory for OpenClaw |
| **soul-upload.com** | - | Encrypted backup storage for OpenClaw workspace artifacts (SOUL.md, MEMORY.md, etc.) |

#### Enterprise Solutions (3)

| Project | Stars | Description |
|---------|-------|-------------|
| **archestra** | 2.8k | Enterprise-grade OpenClaw with RBAC |
| **openclaw-saml** | - | SAML authentication for OpenClaw |
| **claw-audit** | - | Audit logging and compliance tools |

#### China IM Integrations (5)

| Project | Stars | Description |
|---------|-------|-------------|
| **openclaw-dingtalk** | 500+ | DingTalk integration |
| **openclaw-feishu** | 400+ | Feishu/Lark integration |
| **openclaw-wechat** | 600+ | WeChat integration |
| **openclaw-qq** | 300+ | QQ integration |
| **openclaw-wework** | 200+ | WeCom (Enterprise WeChat) integration |

#### Monitoring and Tools (6)

| Project | Stars | Description |
|---------|-------|-------------|
| **Manifest** | 3.3k | Real-time cost observability for OpenClaw Agents |
| **crabwalk** | 683 | Real-time companion monitor for OpenClaw |
| **opik-openclaw** | 50 | Trace-level observability OpenClaw plugin for Opik |
| **AgentPulse** | NEW | Real-time LLM cost tracking and observability |
| **WatchClaw** | NEW | Autonomous security/ops hardening layer for OpenClaw deployments |

### 2. MCP Support (13,000+ servers)

**MCP Resources**:

- **MCP Adapter Plugin**: Exposes MCP tools as native Agent tools
- **Native MCP Support Issue**: Feature discussion
- **MCP Server PR**: Server support implementation

**Curated MCP Servers**:

| Server | Description |
|--------|-------------|
| `https://api.anchorbrowser.io/mcp` | Cloud browser platform for AI Agents |
| **AI Image Generator & Editor** | Generate professional AI images via unified interface, 1,300+ curated prompts |
| **ecap-security-auditor** | Vulnerability scanning |
| **glin-profanity-mcp** | Profanity detection |
| **AnChain.AI Data MCP** | AML compliance |
| **skillsync-mcp** | Secure gated skill manager for Claude Code |
| **meyhem-search** | Agent-native search with feedback-driven ranking |
| **wavestreamer** | AI prediction platform |
| **defi-mcp** | DeFi MCP server, 12 tools |
| **x-twitter-scraper** | X API and Twitter scraping skill, 40+ tools |

### 3. Tutorials and Guides

#### Beginner Tutorials (4)

| Tutorial | Source | Description |
|----------|--------|-------------|
| [What is OpenClaw?](https://medium.com/@gemQueenx/...) | Medium | Setup + features guide |
| [OpenClaw for Developers](https://dev.to/mechcloud_academy/...) | DEV.to | Developer guide |
| [What is OpenClaw?](https://www.digitalocean.com/...) | DigitalOcean | Comprehensive explainer |
| [Complete Installation Guide](https://www.aifreeapi.com/...) | AI Free API | WhatsApp, Telegram, Discord setup |

#### Advanced Tutorials (3)

| Tutorial | Source | Description |
|----------|--------|-------------|
| [GitHub PR Review Automation](https://zenvanriel.nl/...) | Blog | Automated code review |
| [Creating AI Agent Workforce](https://o-mega.ai/...) | o-mega | Ultimate workforce guide |
| [Pre-Launch Checklist](https://habr.com/...) | Habr | Security and configuration checklist |

### 4. Security Resources

#### Best Practices

- Run OpenClaw in a sandbox environment to limit blast radius
- Restrict file system access to only necessary directories
- Store API keys in environment variables — never hardcode them
- Keep OpenClaw updated to the latest version
- Review skills before installing from third-party sources
- Never expose OpenClaw instances to the public internet

#### Security Tools

| Project | Description |
|---------|-------------|
| **aquaman** | Credential isolation proxy — API keys never enter the Agent process |
| **APort Agent Guardrails** | Pre-action authorization for OpenClaw |
| **leashed** | Policy engine, audit logs, and emergency kill switch for AI Agents |

#### Known Risks

- Exposed instances can be hijacked by adversaries
- Prompt injection through malicious content in ingested data
- Misconfigured settings can leak sensitive data or API keys

### 5. Alternatives and Comparisons

| Agent | Type | Best For |
|-------|------|----------|
| **OpenClaw** | Open Source | Personal AI assistant, chat-driven, 12+ messaging platforms |
| **Manus AI** | Proprietary | General-purpose Agent framework |
| **OpenManus** | Open Source | Open-source Manus AI alternative |
| **AutoGPT** | Open Source | Autonomous task execution |
| **Open Interpreter** | Open Source | Terminal-based code execution |
| **Claude Code** | Proprietary | Developer coding assistance |
| **Jan.ai** | Open Source | Privacy-focused, fully offline |
| **Agent Zero** | Open Source | Fully local autonomous Agent |
| **Khoj** | Open Source | Open-source personal AI |
| **eesel AI** | SaaS | Commercial customer service |

## Summary

SamurAIGPT/awesome-openclaw is a **comprehensive aggregator of community resources**, with value in:

1. **Systematic categorization**: 200+ projects organized by function
2. **Continuous updates**: NEW projects are labeled to keep the list fresh
3. **Multi-dimensional**: Projects, tutorials, articles, security, comparisons
4. **Community-driven**: Accepts community contributions for collaborative maintenance

<!-- lastCommit: 45c0a7cce8a19c4261134fbbd5499aa5dcd98a27 -->
