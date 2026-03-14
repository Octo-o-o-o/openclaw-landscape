> https://github.com/hesamsheikh/awesome-openclaw-usecases

# Awesome OpenClaw Use Cases

## Basic Information

- **GitHub**: https://github.com/hesamsheikh/awesome-openclaw-usecases
- **Stars**: 23,013
- **Maintainer**: Hesam Sheikh (@Hesamation)
- **Community**: Discord (Open Source AI Builders)
- **Use case count**: 36+
- **Categories**: Social Media, Creative & Building, Infrastructure & DevOps, Productivity, Research & Learning, Finance & Trading

## Problem & Solution

### Core Problem

**OpenClaw adoption bottleneck**: Users do not lack skills — what they lack is **discovering specific ways OpenClaw can improve their lives**.

- Official documentation focuses on technical implementation, lacking scenario-based use cases
- Users do not know what real-world problems OpenClaw can solve
- Community best practices are scattered across Discord / Reddit / X and difficult to search
- New users face a steep learning curve, lacking reproducible templates

### Solution

**Community-driven use case library**: Collects real user OpenClaw usage scenarios, providing reproducible configuration templates and implementation guides.

- **Authenticity**: Only accepts use cases that have been verified to run for at least one day
- **Actionability**: Each use case includes pain points, implementation approach, configuration examples, and required skills
- **Security warnings**: Clearly labels security risks of third-party skills and dependencies
- **Clear categorization**: Organized into 6 major categories by application scenario for easy discovery

## Core Architecture

### Use Case Classification System

```
awesome-openclaw-usecases/
├── usecases/
│   ├── Social Media (4)
│   │   ├── daily-reddit-digest.md
│   │   ├── daily-youtube-digest.md
│   │   ├── x-account-analysis.md
│   │   └── multi-source-tech-news-digest.md
│   │
│   ├── Creative & Building (5)
│   │   ├── overnight-mini-app-builder.md
│   │   ├── youtube-content-pipeline.md
│   │   ├── content-factory.md
│   │   ├── autonomous-game-dev-pipeline.md
│   │   └── podcast-production-pipeline.md
│   │
│   ├── Infrastructure & DevOps (2)
│   │   ├── n8n-workflow-orchestration.md
│   │   └── self-healing-home-server.md
│   │
│   ├── Productivity (18)
│   │   ├── autonomous-project-management.md
│   │   ├── multi-channel-customer-service.md
│   │   ├── phone-based-personal-assistant.md
│   │   ├── inbox-declutter.md
│   │   ├── personal-crm.md
│   │   ├── health-symptom-tracker.md
│   │   ├── multi-channel-assistant.md
│   │   ├── project-state-management.md
│   │   ├── dynamic-dashboard.md
│   │   ├── todoist-task-manager.md
│   │   ├── family-calendar-household-assistant.md
│   │   ├── multi-agent-team.md
│   │   ├── aionui-cowork-desktop.md
│   │   ├── custom-morning-brief.md
│   │   ├── meeting-notes-action-items.md
│   │   ├── habit-tracker-accountability-coach.md
│   │   ├── second-brain.md
│   │   └── event-guest-confirmation.md
│   │
│   ├── Research & Learning (5)
│   │   ├── earnings-tracker.md
│   │   ├── knowledge-base-rag.md
│   │   ├── market-research-product-factory.md
│   │   ├── pre-build-idea-validator.md
│   │   └── semantic-memory-search.md
│   │
│   └── Finance & Trading (1)
│       └── polymarket-autopilot.md
│
├── README.md (English)
├── README_CN.md (Chinese)
├── README_KR.md (Korean)
└── CONTRIBUTING.md
```

### Use Case Document Structure

Each use case follows a unified template:

```markdown
# [Use Case Name]

## Pain Point
Describes the specific problem the user faces

## What It Does
Core capability list of the solution

## How It Works
1. Step 1
2. Step 2
3. ...

## Skills You Need
- skill_name_1
- skill_name_2

## Setup
### AGENTS.md / SOUL.md / config.toml examples
```toml
[configuration content]
```

## Example Output
Actual running result screenshots or text

## Tips & Gotchas
- Common issues
- Best practices
```

## Key Features

### 1. Social Media Automation

#### Daily Reddit Digest
- **Pain point**: Subscribed to multiple subreddits, information overload, unable to filter high-quality content
- **Solution**: Automatically scrapes and summarizes based on user preferences (keywords, minimum upvotes, exclusion patterns)
- **Skills**: `reddit_search`, `memory_save`, `schedule`
- **Output**: Daily digest email or Telegram message

#### Daily YouTube Digest
- **Pain point**: Subscribed to too many channels, missing important videos
- **Solution**: Scrapes new videos from subscribed channels, generates summaries (title, duration, key points)
- **Skills**: `youtube_search`, `youtube_transcript`, `schedule`

#### Multi-Source Tech News Digest
- **Pain point**: Tech news is scattered across RSS, Twitter/X, GitHub, HN; manual aggregation is time-consuming
- **Solution**: Automatically aggregates from 109+ sources, quality scoring, natural language queries
- **Skills**: `rss_fetch`, `twitter_search`, `github_trending`, `web_search`
- **Highlight**: Supports natural language filtering ("Show me AI infra news from last 7 days")

### 2. Creative & Building

#### Overnight Mini-App Builder (Goal-Driven Autonomous Tasks)
- **Pain point**: Many ideas but little execution; lacking automated task decomposition and execution
- **Solution**: User brainstorms goals, Agent auto-generates, schedules, and completes daily tasks (including building surprise mini-apps)
- **Skills**: `sessions_spawn`, `file_write`, `shell_execute`, `git_commit`
- **Example**: User says "Build a habit tracker", Agent generates an MVP overnight and deploys it

#### Autonomous Game Dev Pipeline
- **Pain point**: Educational game development cycles are long, requiring coordination of backlog, implementation, testing, documentation, and Git commits
- **Solution**: Full lifecycle management from backlog selection to implementation, registration, documentation, and Git commits, enforcing a "Bugs First" strategy
- **Skills**: `file_read`, `file_write`, `shell_execute`, `git_commit`, `sessions_spawn`
- **Highlight**: Multi-Agent parallel work (dev Agent, test Agent, docs Agent)

#### Podcast Production Pipeline
- **Pain point**: Podcast production requires guest research, outline writing, show notes, and social media promotion — manual operation is time-consuming
- **Solution**: Automates the entire process (topic to guest research to outline to show notes to social media assets)
- **Skills**: `web_search`, `file_write`, `memory_save`

### 3. Infrastructure & DevOps

#### n8n Workflow Orchestration
- **Pain point**: Agents directly calling APIs requires managing credentials, with high security risks
- **Solution**: Agent delegates to n8n workflows via Webhooks; credentials are managed by n8n, never touched by the Agent
- **Skills**: `http_request` (calling n8n webhook)
- **Advantages**: Visual workflows, credential isolation, lockable integrations

#### Self-Healing Home Server
- **Pain point**: Home server failures (NAS, Pi-hole, Home Assistant) require manual SSH fixes
- **Solution**: Resident infrastructure Agent with SSH access, automated cron tasks, and self-healing capabilities
- **Skills**: `shell_execute`, `ssh_execute`, `schedule`, `memory_recall`
- **Example**: Detects Docker container stopped, auto-restarts, logs the event, sends Telegram notification

### 4. Productivity

#### Autonomous Project Management
- **Pain point**: Traditional orchestrator patterns become bottlenecks, with the main Agent acting as a traffic cop
- **Solution**: Decentralized coordination where sub-Agents work autonomously through a shared `STATE.yaml` file
- **Core pattern**:
  ```yaml
  # STATE.yaml
  tasks:
    - id: homepage-hero
      status: in_progress
      owner: pm-frontend
    - id: api-auth
      status: done
      owner: pm-backend
    - id: content-migration
      status: blocked
      blocked_by: api-auth
  ```
- **Skills**: `sessions_spawn`, `sessions_send`, `file_read`, `file_write`, `git_commit`
- **Advantages**: Parallel execution, no orchestration overhead, self-documenting

#### Multi-Agent Specialized Team
- **Pain point**: A single Agent has limited context window and cannot simultaneously handle strategy, development, marketing, and business analysis
- **Solution**: Multiple specialized Agents (Milo for strategy, Josh for business, Marketing, Dev), shared memory, controlled via a single Telegram group
- **Configuration example**:
  ```text
  ## SOUL.md — Milo (Strategy Lead)
  Model: Claude Opus
  Channel: Telegram (responds to @milo)
  Daily tasks:
  - 8:00 AM: Review overnight agent activity
  - 6:00 PM: End-of-day recap
  ```
- **Skills**: `memory_save`, `memory_recall`, `schedule`, `telegram_send`

#### Phone-Based Personal Assistant
- **Pain point**: Cannot use a keyboard while driving or cooking; needs a hands-free voice assistant
- **Solution**: Access OpenClaw via phone call, voice queries for calendar, Jira, web search
- **Skills**: `voice_call`, `calendar_read`, `jira_search`, `web_search`
- **Implementation**: Twilio / Vonage + OpenClaw webhook

#### Second Brain
- **Pain point**: Ideas, notes, and links are scattered across multiple tools, hard to retrieve
- **Solution**: Send any content to a Bot for automatic saving, search all memories via a custom Next.js dashboard
- **Skills**: `memory_save`, `memory_recall`, `semantic_search`
- **Highlight**: Hybrid retrieval with vector search + keyword search

#### Event Guest Confirmation
- **Pain point**: Manually calling each event guest to confirm attendance is time-consuming and error-prone
- **Solution**: AI voice calls each guest on the list, confirms attendance, collects notes, generates a summary report
- **Skills**: `voice_call`, `memory_save`, `file_write`
- **Implementation**: Bland.ai / Vapi.ai + OpenClaw

### 5. Research & Learning

#### Personal Knowledge Base (RAG)
- **Pain point**: Bookmarked articles, tweets, and URLs cannot be semantically retrieved
- **Solution**: Drag and drop URLs/tweets into chat, automatically builds a searchable knowledge base
- **Skills**: `web_scrape`, `memory_save`, `semantic_search`
- **Technology**: RAG (Retrieval-Augmented Generation)

#### Market Research & Product Factory
- **Pain point**: Not knowing users' real pain points, blindly developing products
- **Solution**: Uses the "Last 30 Days" skill to mine real pain points from Reddit and X, OpenClaw builds the MVP
- **Skills**: `reddit_search`, `twitter_search`, `file_write`, `shell_execute`
- **Process**: Pain point mining, demand validation, MVP development, user testing

#### Pre-Build Idea Validator
- **Pain point**: Not knowing whether the market is already saturated before development
- **Solution**: Automatically scans GitHub, HN, npm, PyPI, Product Hunt; stops if crowded, continues if whitespace
- **Skills**: `github_search`, `npm_search`, `pypi_search`, `web_search`
- **Output**: Competitive analysis report + recommendation (continue / stop / differentiate)

#### Semantic Memory Search
- **Pain point**: OpenClaw's Markdown memory files only support keyword search
- **Solution**: Adds vector-driven semantic search to memory files with hybrid retrieval and automatic syncing
- **Skills**: `memory_recall`, `semantic_search`, `embedding_generate`
- **Technology**: Vector database (Pinecone / Weaviate / Qdrant) + hybrid retrieval

### 6. Finance & Trading

#### Polymarket Autopilot
- **Pain point**: Manual prediction market trading is time-consuming, lacking backtesting and strategy analysis
- **Solution**: Automated paper trading, backtesting, strategy analysis, daily performance reports
- **Skills**: `http_request` (Polymarket API), `memory_save`, `schedule`
- **Note**: Paper trading only; cryptocurrency-related use cases are not accepted

## Summary

The core value of awesome-openclaw-usecases lies in **scenario-based use cases** + **community-driven** + **reproducible templates**. The most valuable takeaways include:

1. **Use-case-driven product design**: Establish a Use Cases Gallery, categorized by industry/role
2. **Template marketplace**: Community contributions + security audits + official certification
3. **Multi-Agent collaboration patterns**: Decentralized coordination (STATE.yaml) + specialized teams (shared memory)
4. **State management patterns**: Runbook state files + parallel execution + real-time display
5. **Self-healing infrastructure**: Self-Healing trigger types + automated remediation
6. **Multi-channel integration**: Voice Channel + Customer Service Router
7. **Knowledge base & RAG**: Semantic search + hybrid retrieval + audit log search
8. **Market research & validation**: Pre-deployment market scanning + competitive analysis
9. **Security warning mechanism**: Security badges + audit reports + pre-deployment warnings
10. **Contribution guidelines**: Demo videos + security audits + community voting

<!-- lastCommit: 4914bfc -->
