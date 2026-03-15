> https://github.com/yeuxuan/openclaw-docs

# yeuxuan/openclaw-docs

## Basic Information

- **Stars**: 533
- **URL**: https://github.com/yeuxuan/openclaw-docs
- **Online Documentation**: https://openclaw-docs.dx3n.cn
- **License**: MIT
- **Tech Stack**: VitePress + Azure Static Web Apps

## Problem & Solution

### Core Problems

OpenClaw's official documentation is primarily in English, and Chinese users face the following difficulties:

1. **Language barrier**: Official documentation is mainly in English, making comprehension costly for Chinese users
2. **Lack of systematic structure**: Official documentation is scattered, lacking a complete learning path from beginner to expert
3. **Missing source code analysis**: No deep source code analysis of OpenClaw's core modules
4. **Insufficient installation tutorials**: Various platforms and channels lack detailed illustrated tutorials
5. **Unclear AI framework principles**: Core concepts like context engineering, state machines, and memory systems lack systematic explanation

### Solution

yeuxuan/openclaw-docs is a **comprehensive Chinese documentation site for OpenClaw**, providing:

- **276 original Chinese tutorials**: Covering installation, configuration, source code, and AI framework
- **4 learning tracks**:
  - Track 0: Installation tutorials (147 articles)
  - Track A: Complete engineering main track (59 articles)
  - Track B: AI core framework (22 articles)
  - Track C: Channel adapters (included in Track A)
- **Function-level precision**: Key modules pinpointed to specific function entry points and call chains
- **Beginner-friendly**: Installation tutorials with full illustrations, zero-to-running in 10 minutes
- **SEO-ready**: 276 pages with individual descriptions, sitemap, and IndexNow automatic submission

## Core Architecture

### Documentation Site Architecture

```
openclaw-docs/
├── docs/
│   ├── index.md                            # Homepage
│   ├── tutorials/                          # Track 0: Installation Tutorials (147 articles)
│   │   ├── getting-started/                # Quick start and guided installation
│   │   ├── installation/                   # Docker / Node / Cloud server deployment
│   │   ├── gateway/                        # Gateway configuration and operations
│   │   ├── channels/                       # Channel integration (Telegram/WhatsApp/Discord etc.)
│   │   ├── providers/                      # AI model Provider configuration
│   │   ├── concepts/                       # Core concepts (context/memory/state machine etc.)
│   │   ├── tools/                          # Tool system (browser/execution/skills/sub-agents)
│   │   ├── automation/                     # Automation (Webhook/Cron/Poll)
│   │   └── help/                           # Troubleshooting and FAQs
│   ├── beginner-openclaw-guide/            # Track A: Complete Engineering Main Track (59 articles)
│   └── beginner-openclaw-framework-focus/  # Track B: AI Core Framework (22 articles)
├── docs/.vitepress/
│   ├── config.mts                          # Site configuration (SEO / navigation / sidebar)
│   └── theme/                              # Custom theme and styles
└── scripts/
    ├── convert-mdx.mjs                     # MDX to VitePress Markdown batch conversion
    └── ping-indexnow.mjs                   # Post-build automatic URL submission to Bing IndexNow
```

### Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Static site generator | VitePress | Markdown to HTML, built-in search and navigation |
| Deployment platform | Azure Static Web Apps | Automatic builds, CDN distribution, HTTPS |
| SEO optimization | IndexNow API | Automatic URL submission to Bing index |
| Content format | Markdown + Frontmatter | Documentation writing, metadata management |

### Learning Path Design

```
Track 0: Installation Tutorials (147 articles)
├── Quick Start
│   ├── What is OpenClaw
│   ├── System Requirements
│   └── 5-Minute Quick Install
├── Detailed Installation
│   ├── Docker Deployment
│   ├── Node.js Source Deployment
│   └── Cloud Server Deployment (Alibaba Cloud/Tencent Cloud/AWS)
├── Gateway Configuration
│   ├── Configuration File Structure
│   ├── Environment Variables
│   └── Startup Parameters
├── Channel Integration
│   ├── Telegram Bot Configuration
│   ├── WhatsApp Configuration
│   ├── Discord Bot Configuration
│   └── Feishu (Lark) Bot Configuration
├── AI Model Configuration
│   ├── Claude API Configuration
│   ├── GPT API Configuration
│   ├── DeepSeek Configuration
│   └── Ollama Local Model Configuration
└── Troubleshooting
    ├── Common Error Codes
    ├── Log Analysis
    └── Community Help Guide

Track A: Complete Engineering Main Track (59 articles)
├── CLI Startup Framework
│   ├── Entry Function main()
│   ├── Command Parsing
│   └── Subcommand Routing
├── Gateway Control Plane
│   ├── Gateway Startup Flow
│   ├── Configuration Loading
│   └── Service Registration
├── Channel Adapters
│   ├── Interface Contract
│   ├── Registration Pipeline
│   ├── Account Lifecycle
│   ├── Inbound Routing
│   └── Outbound Send Decoupling
├── Agent Execution Pipeline
│   ├── Message Reception
│   ├── Context Building
│   ├── Model Invocation
│   ├── Tool Execution
│   └── Response Sending
└── Streaming Subscriptions
    ├── SSE Implementation
    └── WebSocket Implementation

Track B: AI Core Framework (22 articles)
├── Context Engineering
│   ├── System Prompts
│   ├── User Messages
│   └── History Message Management
├── Agent State Machine
│   ├── State Definitions
│   ├── State Transitions
│   └── State Persistence
├── Tool Strategy and Approval
│   ├── Tool Registration
│   ├── Tool Invocation
│   └── Approval Workflow
├── Model Fallback
│   ├── Primary Model Failure Detection
│   └── Backup Model Switching
├── Memory System
│   ├── Short-term Memory (within session)
│   ├── Long-term Memory (cross-session)
│   └── Memory Retrieval
└── Hook Plugin Injection Mechanism
    ├── Hook Definition
    ├── Hook Registration
    └── Hook Execution
```

## Key Features

### 1. Function-Level Source Code Analysis

**Example: Gateway Startup Flow**

```
Article: "Gateway Startup Flow Deep Dive"

1. Entry Function
   - File: src/cli/commands/gateway.ts
   - Function: startGateway()
   - Lines: L42-L89

2. Configuration Loading
   - File: src/core/config-loader.ts
   - Function: loadConfig()
   - Call chain: startGateway() -> loadConfig() -> parseConfigFile()

3. Channel Registration
   - File: src/channels/registry.ts
   - Function: registerChannels()
   - Iteration: config.channels.forEach(ch => registerChannel(ch))

4. Agent Initialization
   - File: src/agents/agent-manager.ts
   - Function: initializeAgents()
   - State machine: IDLE -> INITIALIZING -> READY
```

### 2. Illustrated Installation Tutorials

**Features**:
- **Rich screenshots**: Screenshots at every key step
- **Copyable commands**: All commands displayed in code blocks for one-click copying
- **Error examples**: Screenshots of common errors with solutions
- **Video tutorials**: Video demonstrations for complex operations

### 3. Multi-Platform Installation Guides

| Platform | Tutorial Count | Coverage |
|----------|---------------|----------|
| macOS | 15 articles | Homebrew installation, M1/M2 compatibility, permission configuration |
| Linux | 20 articles | Ubuntu/Debian/CentOS/Arch, systemd configuration |
| Windows | 12 articles | WSL2 installation, PowerShell configuration, firewall settings |
| Docker | 18 articles | docker-compose, multi-container orchestration, data persistence |
| Cloud servers | 25 articles | Alibaba Cloud/Tencent Cloud/AWS/GCP, security group configuration |

### 4. Complete Channel Integration Guides

**Tutorial structure for each channel**:

```
Telegram Bot Integration Guide
├── 1. Create Bot (BotFather operation screenshots)
├── 2. Obtain Token
├── 3. Configure openclaw.json
├── 4. Start Gateway
├── 5. Test Conversation
├── 6. Common Issues
│   ├── Bot not responding
│   ├── Message send failure
│   └── Insufficient permissions
└── 7. Advanced Configuration
    ├── Webhook mode
    ├── Group management
    └── Command menu
```

### 5. SEO Optimization Strategy

**Implementation**:

```javascript
// scripts/ping-indexnow.mjs
import { readFileSync } from 'fs';
import fetch from 'node-fetch';

const sitemap = readFileSync('docs/.vitepress/dist/sitemap.xml', 'utf-8');
const urls = [...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(m => m[1]);

// Push to Bing IndexNow
await fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    host: 'openclaw-docs.dx3n.cn',
    key: process.env.INDEXNOW_KEY,
    urlList: urls
  })
});
```

**Results**:
- New articles indexed by Bing within 1 hour of publication
- Ranks #1 for "OpenClaw Chinese documentation" search
- 5,000+ monthly organic search visits

### 6. MDX to VitePress Conversion Tool

**Problem**: Original documents may be in MDX format (React components)

**Solution**:

```javascript
// scripts/convert-mdx.mjs
import { readFileSync, writeFileSync } from 'fs';
import { glob } from 'glob';

const files = glob.sync('docs/**/*.mdx');

files.forEach(file => {
  let content = readFileSync(file, 'utf-8');

  // Convert React components to Markdown
  content = content.replace(/<Callout type="warning">(.*?)<\/Callout>/gs,
    ':::warning\n$1\n:::');
  content = content.replace(/<Tabs>(.*?)<\/Tabs>/gs,
    (match, inner) => convertTabs(inner));

  // Save as .md
  writeFileSync(file.replace('.mdx', '.md'), content);
});
```

<!-- lastCommit: f99aea2d8cec9c36df15418f6aeb028e329fec4d -->
