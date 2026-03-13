> https://github.com/VoltAgent/awesome-openclaw-skills

# VoltAgent/awesome-openclaw-skills

## Basic Information

- **GitHub Stars**: 34,650
- **Project URL**: https://github.com/VoltAgent/awesome-openclaw-skills
- **Positioning**: A curated directory of the OpenClaw skill ecosystem, filtering and categorizing 5,490+ community-built skills from the official ClawHub skill registry
- **Maintainer**: VoltAgent team

## Problem & Solution

### Core Problem

1. **Skill discovery is difficult** — The official OpenClaw skill registry (ClawHub) contains thousands of skills but lacks effective categorization and filtering mechanisms, making it hard for users to find skills that meet their needs
2. **Ecosystem fragmentation** — Community-contributed skills vary in quality, with no unified display and evaluation standards
3. **Unclear use cases** — Users are unsure which specific scenarios OpenClaw can be applied to, lacking a source of inspiration

### Solution

**awesome-openclaw-skills provides a curated skill directory system**:

1. **Classification system** — Organizes 5,490+ skills into 30+ functional categories:
   - AI & LLMs (197 skills)
   - Browser & Automation
   - Coding Agents & IDEs
   - DevOps & Cloud
   - Git & GitHub
   - Communication (Slack, Discord, Email, etc.)
   - Data & Analytics
   - Marketing & Sales
   - Health & Fitness
   - Gaming
   - And more

2. **Quick installation** — Provides two installation methods:
   ```bash
   # ClawHub CLI one-click install
   clawhub install <skill-slug>

   # Manual installation (copy to skills directory)
   ~/.openclaw/skills/  # Global
   ~/workspace/.openclaw/skills/  # Workspace-level
   ```

3. **Skill metadata display** — Each skill entry includes:
   - Skill name and slug
   - Short description
   - GitHub link (pointing to official skill repository)
   - Author information

4. **Inspiration library** — Helps users understand OpenClaw application scenarios by showcasing real community use cases

## Core Architecture

### Directory Structure

```
awesome-openclaw-skills/
├── README.md                    # Main entry point with table of contents and installation instructions
├── categories/                  # Category directory
│   ├── ai-and-llms.md          # AI and LLM related skills
│   ├── browser-and-automation.md
│   ├── coding-agents-and-ides.md
│   ├── communication.md
│   ├── devops-and-cloud.md
│   ├── git-and-github.md
│   ├── data-and-analytics.md
│   ├── marketing-and-sales.md
│   ├── health-and-fitness.md
│   ├── gaming.md
│   └── ... (30+ category files)
├── CONTRIBUTING.md              # Contribution guide
└── LICENSE
```

### Skill Classification Logic

**30+ functional categories** covering major application scenarios in the OpenClaw ecosystem:

1. **Developer Tools**:
   - Coding Agents & IDEs
   - Git & GitHub
   - DevOps & Cloud
   - CLI Utilities

2. **Productivity Tools**:
   - Browser & Automation
   - Notes & PKM (Personal Knowledge Management)
   - Calendar & Scheduling
   - PDF & Documents

3. **Communication & Collaboration**:
   - Communication (Slack, Discord, Telegram, Email)
   - Social Media

4. **AI Capability Extensions**:
   - AI & LLMs (197 skills)
   - Image & Video Generation
   - Voice & Audio

5. **Vertical Domains**:
   - Marketing & Sales
   - Health & Fitness
   - Gaming
   - Finance & Crypto

6. **Platform Integrations**:
   - Apple Apps & Services
   - iOS & macOS Development
   - Media & Streaming

### Skill Entry Format

Each skill entry follows a unified format:

```markdown
- [skill-slug](https://github.com/openclaw/skills/tree/main/skills/author/skill-slug/SKILL.md) - Skill description
```

Example (AI & LLMs category):

```markdown
- [agent-memory](https://github.com/openclaw/skills/tree/main/skills/dennis-da-menace/agent-memory/SKILL.md) - Persistent memory system for AI agents.
- [agent-orchestrator](https://github.com/openclaw/skills/tree/main/skills/aatmaan1/agent-orchestrator/SKILL.md) - Meta-agent skill for orchestrating complex tasks.
- [claude-usage-checker](https://github.com/openclaw/skills/tree/main/skills/aligurelli/claude-usage-checker/SKILL.md) - Check Claude Code / Claude Max usage limits.
```

## Key Features

### 1. Curation Strategy

- **Trusted sources** — All skills come from the official OpenClaw skill registry (ClawHub), verified by the community
- **Continuous updates** — Automatically syncs the latest skills from ClawHub via GitHub Actions
- **Quality filtering** — While containing 5,490+ skills, the categorization and descriptions help users quickly assess quality

### 2. Classification System

**30+ functional categories**, each containing dozens to hundreds of skills:

- **AI & LLMs** (197) — Agent orchestration, multi-model switching, memory systems, prompt optimization
- **Browser & Automation** — Web automation, data scraping, form filling
- **Coding Agents & IDEs** — Code generation, refactoring, testing, documentation generation
- **Communication** — Slack, Discord, Telegram, Email, WhatsApp integrations
- **DevOps & Cloud** — Docker, Kubernetes, AWS, GCP, Azure management
- **Git & GitHub** — PR review, Issue management, commit automation

### 3. Installation Convenience

**ClawHub CLI one-click install**:

```bash
clawhub install <skill-slug>
```

**Manual installation** (supports global and workspace-level):

| Location | Path |
|----------|------|
| Global | `~/.openclaw/skills/` |
| Workspace | `~/workspace/.openclaw/skills/` |

### 4. Community-Driven

- **Open contributions** — Provides CONTRIBUTING.md to guide community contributions of new skills
- **Discord community** — Active community with engaged members
- **Continuous maintenance** — Recent updates show the project remains active

### 5. Skill Examples (AI & LLMs Category)

**Agent Orchestration & Collaboration**:
- `agent-orchestrator` — Meta-Agent skill for orchestrating complex tasks
- `agent-registry` — Agent discovery system supporting token-efficient Agent collaboration
- `agent-autonomy-kit` — Lets Agents stop waiting for prompts and run autonomously

**Memory & Context Management**:
- `agent-memory` — Persistent memory system
- `context-gatekeeper` — Keeps token-friendly by summarizing recent conversations

**Multi-Model Support**:
- `communicate` — Launch local or Hugging Face models directly from chat
- `bunni-persona` — Multi-persona and model switching toolkit

**Security & Monitoring**:
- `agent-sentinel` — Operational circuit breaker for Agents
- `claude-usage-checker` — Check Claude Code / Claude Max usage limits

## Summary

VoltAgent/awesome-openclaw-skills is a key piece of infrastructure in the OpenClaw ecosystem. By curating and categorizing 5,490+ skills, it addresses the problems of skill discovery and ecosystem fragmentation. Its core value lies in:

1. **Template library design reference** — Classification system, metadata standards, installation mechanisms
2. **Ecosystem building strategy** — Open community, contribution workflows, quality verification
3. **Capability mapping foundation** — Cross-platform skill mapping, capability routing
4. **Cost & auditing** — Skill cost tracking, permission management, sandbox testing
5. **Automation scenarios** — Runbook templates, workflow orchestration
