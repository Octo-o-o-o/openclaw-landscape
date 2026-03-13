> https://github.com/xianyu110/awesome-openclaw-tutorial

# xianyu110/awesome-openclaw-tutorial

## Basic Information

- **GitHub**: https://github.com/xianyu110/awesome-openclaw-tutorial
- **Stars**: 2,179
- **Language**: Shell
- **Created**: 2026-02-10
- **Last Updated**: 2026-03-11
- **Description**: The most comprehensive Chinese tutorial for OpenClaw from scratch, covering installation, configuration, practical cases, and troubleshooting guides (GitHub edition)
- **Topics**: openclaw, openclaw-skills
- **Total Word Count**: Approximately 418,000 words (15 chapters + 14 appendices + 1 security guide)

## Problem & Solution

### Core Problems

OpenClaw, as a powerful AI Agent platform, has the following pain points:

1. **Steep learning curve**: Official documentation is primarily in English, Chinese resources are scarce, making it difficult for Chinese users to get started
2. **Complex configuration**: Involves API Keys, Profiles, Skills, MCP, Gateway, and other multi-layer configurations that can overwhelm beginners
3. **Version upgrade pitfalls**: For example, version 2026.3.2 separated tool permissions from chat capabilities, changing the default profile to `messaging` (chat-only mode), causing AI to "go silent" after upgrading
4. **Lack of practical cases**: No end-to-end cases for real-world scenarios, leaving users unsure how to apply OpenClaw to actual work
5. **Missing troubleshooting guides**: Users frequently encounter permissions, configuration, and compatibility issues without systematic troubleshooting references

### Solution

awesome-openclaw-tutorial provides a complete Chinese learning system:

1. **Systematic tutorials**: 15 chapters covering the full path from installation to advanced applications
   - Basics (Chapters 1-3): Introduction, installation, quick start
   - Core Features (Chapters 4-7): File management, knowledge management, schedule management, automation workflows
   - Advanced (Chapters 8-11): Skills extensions, multi-platform integration, API integration, advanced configuration
   - Practical (Chapters 12-15): Personal productivity, advanced automation, creative applications, solopreneur cases

2. **14 appendices**: Covering topics such as configuration file structure, API Key configuration, Skills ecosystem, and search guides

3. **Security guide**: A dedicated security configuration chapter (99-security-guide.md) covering permission management, data security, and network security

4. **70+ practical cases**: Scenario-based cases ready for direct application, such as automated report generation, knowledge base construction, smart schedule reminders, etc.

5. **Version upgrade guides**: Detailed migration guides for breaking changes in key versions like 2026.3.2 and 2026.3.7

6. **Rich illustrations**: 50+ configuration screenshots to lower the comprehension barrier

7. **Continuous updates**: Project status marked as "complete, under continuous optimization," with redundant content removed to improve quality

## Core Architecture

### Tutorial Structure

```
awesome-openclaw-tutorial/
├── docs/
│   ├── 01-basics/                    # Basics
│   │   ├── 01-introduction.md        # OpenClaw Introduction
│   │   ├── 02-installation.md        # Installation Guide
│   │   └── 03-quick-start.md         # Quick Start
│   ├── 02-core-features/             # Core Features
│   │   ├── 04-file-management.md     # File Management
│   │   ├── 05-knowledge-management.md # Knowledge Management
│   │   ├── 06-schedule-management.md  # Schedule Management
│   │   └── 07-automation-workflow.md  # Automation Workflows
│   ├── 03-advanced/                  # Advanced
│   │   ├── 08-skills-extension.md    # Skills Extensions
│   │   ├── 09-multi-platform-integration.md # Multi-Platform Integration
│   │   ├── 10-api-integration.md     # API Integration
│   │   ├── 11-advanced-configuration.md # Advanced Configuration
│   │   └── 99-security-guide.md      # Security Guide
│   ├── 04-practical-cases/           # Practical Cases
│   │   ├── 12-personal-productivity.md # Personal Productivity
│   │   ├── 13-advanced-automation.md   # Advanced Automation
│   │   ├── 14-creative-applications.md # Creative Applications
│   │   └── 15-solo-entrepreneur-cases.md # Solopreneur Cases
│   ├── api-key-config-guide.md       # API Key Configuration Guide
│   ├── config-file-structure.md      # Configuration File Structure
│   ├── skills-ecosystem.md           # Skills Ecosystem
│   └── search-guide.md               # Search Guide
├── appendix/                         # Appendices (14 topics)
├── openclaw-manager/                 # OpenClaw Manager Tool
├── scripts/                          # Helper Scripts
├── search.json                       # Search Index
└── README.md                         # Project Homepage
```

### Tech Stack

- **Document format**: Markdown
- **Static site generator**: Jekyll (GitHub Pages)
- **Search functionality**: Custom JSON index + frontend search
- **Version control**: Git + GitHub
- **Helper tools**: Shell scripts (e.g., `update-version-to-2026.3.2.sh`)

### Content Organization Principles

1. **Progressive learning path**: From basics to advanced, from theory to practice
2. **Scenario-driven**: Each chapter is oriented around real-world application scenarios rather than simple feature listings
3. **Pitfall-first approach**: Provides "Important Notes" and "Common Errors" at critical configuration points
4. **Version-aware**: Clearly annotates version differences and provides upgrade guides
5. **Searchable**: Provides a full-text search index for quick problem location

## Key Features

### 1. Version Upgrade Guides

**2026.3.7 Breaking Change**:
- Gateway authentication now requires explicitly setting `gateway.auth.mode`
- Must explicitly choose `token` or `password` authentication mode
- If upgrading from an older version without configured authentication, Gateway will refuse to start

**Quick Fix**:
```bash
# Set token authentication
openclaw config set gateway.auth.mode token
openclaw config set gateway.auth.token "your-secret-token"

# Restart Gateway
openclaw gateway restart
```

**2026.3.2 Breaking Change**:
- Tool permissions and chat capabilities were separated; default profile changed to `messaging` (chat-only mode)
- After upgrading, OpenClaw can only chat but cannot perform tasks (file management, command execution, and all other tool functions become disabled)

**5 Profile Types**:
| Profile | Description |
|---------|-------------|
| `messaging` | Can only send messages and manage sessions (chat only, no actions) |
| `default` | Default toolset (without command execution) |
| `coding` | Programming-related tools |
| `full` | Complete toolset including command execution (**recommended**) |
| `custom` | Custom toolset |

**Quick Fix**:
```bash
# Method 1: Switch via command line
openclaw config set profile full

# Method 2: Edit configuration file
# ~/.openclaw/openclaw.json
{
  "profile": "full"
}
```

### 2. Configuration File Structure Guide

The tutorial provides a complete configuration file structure reference (`docs/config-file-structure.md`) covering:

- **Core configuration**: `~/.openclaw/openclaw.json`
  - `profile`: Tool permission configuration
  - `model`: Default model configuration
  - `gateway`: Gateway configuration (authentication, port, CORS)
  - `skills`: Skills configuration
  - `mcp`: MCP server configuration
  - `extensions`: Extension plugin configuration

- **API Key configuration**: `~/.openclaw/api-keys.json`
  - Supports multiple LLM providers (OpenAI / Anthropic / Google / Azure / Chinese providers)
  - Supports multiple API Keys (load balancing, failover)

- **Skills configuration**: `~/.openclaw/skills/`
  - One directory per Skill
  - `skill.json`: Skill metadata
  - `AGENTS.md`: Skill usage instructions

- **MCP configuration**: `~/.openclaw/mcp-servers.json`
  - MCP server registration
  - Tool/resource/prompt mapping

### 3. Skills Ecosystem

The tutorial provides a complete introduction to the Skills ecosystem (`docs/skills-ecosystem.md`), including:

- **Official Skills**: Skills maintained by the OpenClaw team
  - `agent-browser`: Browser automation
  - `agent-memory`: Long-term memory
  - `agent-scheduler`: Scheduled tasks
  - `agent-search`: Web search

- **Community Skills**: Skills contributed by the community
  - Database operations
  - File processing
  - API integration
  - Notification push

- **Custom Skills**: How to develop your own Skills
  - Skill structure
  - Tool definitions
  - Permission management
  - Testing and publishing

### 4. Multi-Platform Integration

The tutorial details OpenClaw's integration with other platforms (Chapter 9):

- **IM platforms**: DingTalk, WeCom, QQ, Feishu (Lark) (via openclaw-china)
- **Knowledge bases**: Notion, Yuque, Feishu Docs
- **Project management**: Jira, Trello, Asana
- **Code hosting**: GitHub, GitLab, Gitee
- **Cloud storage**: Alibaba Cloud OSS, Tencent Cloud COS, AWS S3

### 5. API Integration

The tutorial provides a complete guide to API integration (Chapter 10):

- **RESTful API**: How to call external APIs via HTTP requests
- **GraphQL API**: How to query GraphQL endpoints
- **WebSocket**: How to establish real-time connections
- **Webhook**: How to receive external event notifications
- **Authentication methods**: API Key / OAuth 2.0 / JWT

### 6. Practical Cases

The tutorial provides 70+ practical cases covering:

**Personal Productivity (Chapter 12)**:
- Automated daily/weekly report generation
- Smart email classification and replies
- Automatic meeting minutes organization
- Automated knowledge base construction

**Advanced Automation (Chapter 13)**:
- Multi-step workflow orchestration
- Conditional branching and loops
- Error handling and retries
- Parallel task execution

**Creative Applications (Chapter 14)**:
- AI art generation (Midjourney / Stable Diffusion integration)
- Content creation (articles, video scripts, social media copy)
- Data visualization
- Interactive story generation

**Solopreneur Cases (Chapter 15)**:
- Independent developer workflows
- Content creator operation automation
- Online course production
- E-commerce operations assistant

### 7. Security Guide

The tutorial provides a dedicated security guide (`docs/03-advanced/99-security-guide.md`) covering:

- **Permission management**: Profile configuration, tool whitelisting, file system access control
- **Data security**: API Key protection, sensitive data encryption, log anonymization
- **Network security**: Gateway authentication, HTTPS configuration, CORS policies
- **Audit logging**: Operation records, anomaly detection, compliance requirements

### 8. Search Functionality

The tutorial provides full-text search functionality (`search.md` + `search.json`):

- **Search index**: Auto-generated JSON index containing titles, content, and keywords from all chapters
- **Frontend search**: JavaScript-based client-side search, no backend required
- **Search guide**: How to use the search feature effectively (`docs/search-guide.md`)

### 9. OpenClaw Manager

The tutorial provides an OpenClaw management tool (`openclaw-manager/`) for:

- **One-click installation**: Automatically installs OpenClaw and commonly used Skills
- **Configuration management**: Graphical configuration editor
- **Version management**: Version checking, upgrading, and rollback
- **Health checks**: Service status monitoring and log viewing

<!-- lastCommit: 6a7050b -->
