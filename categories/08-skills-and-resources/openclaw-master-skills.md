> https://github.com/LeoYeAI/openclaw-master-skills

# OpenClaw Master Skills

## Basic Information

- **Project name**: openclaw-master-skills
- **GitHub**: https://github.com/LeoYeAI/openclaw-master-skills
- **Stars**: 1,391
- **Language**: Python
- **License**: MIT License
- **Created**: 2026-03-02
- **Last updated**: 2026-03-11
- **Maintainer**: LeoYeAI / MyClaw.ai
- **Skill count**: 164 (README lists 127+)

## Problem & Solution

### Core Problem

1. **Skills are scattered and hard to discover** — Quality skills in the OpenClaw ecosystem are scattered across skills.sh, GitHub, ClaWHub, and other platforms, making it difficult for users to discover and evaluate them
2. **Inconsistent quality** — Community-contributed skills lack unified quality standards and review mechanisms
3. **No categorized index** — There is no unified skill directory or classification system, making it impossible for users to quickly locate needed skills
4. **Slow updates** — Users need to manually track skill updates across multiple sources

### Solution

**Curated skill repository** — Through automated scripts that weekly scan three major sources (skills.sh leaderboard, GitHub `openclaw-skill` tag, ClaWHub latest releases), skills are verified, tested, and then merged into a unified repository, providing:

- **Unified entry point** — A single repository centrally manages all quality skills
- **Quality assurance** — Each skill must include a valid `SKILL.md`, clear purpose statement, no hardcoded credentials, and must run on standard OpenClaw
- **Categorized index** — Provides a tabular skill index with skill name, description, category, source, and date added
- **Automated updates** — CHANGELOG.md is automatically updated every Monday; users can subscribe for the latest skills
- **Easy installation** — Supports `clawhub install openclaw-master-skills` for one-click installation, or manual copy to `~/.openclaw/workspace/skills/`

## Core Architecture

### Skill Collection Process

```
┌─────────────────────────────────────────────────────────────┐
│                    Weekly Collection Cycle                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              v
        ┌─────────────────────────────────────────┐
        │         Data Sources (3 channels)        │
        ├─────────────────────────────────────────┤
        │  1. skills.sh (leaderboard top skills)  │
        │  2. GitHub (repos tagged openclaw-skill)│
        │  3. ClaWHub (latest published skills)   │
        └─────────────────────────────────────────┘
                              │
                              v
        ┌─────────────────────────────────────────┐
        │      Validation & Quality Check          │
        ├─────────────────────────────────────────┤
        │  • SKILL.md format validation           │
        │  • Clear purpose statement check        │
        │  • No hardcoded credentials scan        │
        │  • Standard OpenClaw compatibility test │
        └─────────────────────────────────────────┘
                              │
                              v
        ┌─────────────────────────────────────────┐
        │         Merge & Organize                 │
        ├─────────────────────────────────────────┤
        │  • Copy to skills/<skill-name>/         │
        │  • Update README.md index table         │
        │  • Generate CHANGELOG.md entry          │
        │  • Commit & push to main branch         │
        └─────────────────────────────────────────┘
```

### Directory Structure

```
openclaw-master-skills/
├── README.md                    # Main index (8 language versions)
├── CHANGELOG.md                 # Weekly update log
├── RELEASES.md                  # Version release records
├── SKILL.md                     # Skill definition for the repo itself
├── scripts/
│   └── collect.sh               # Automated collection script
└── skills/                      # 164 skill directories
    ├── ab-test-setup/
    ├── add-educational-comments/
    ├── agent-governance/
    ├── ai-prompt-generator/
    ├── amazon-price-tracker/
    ├── api-design-principles/
    ├── architecture-blueprint-generator/
    ├── browser-use/
    ├── chrome-devtools/
    ├── clean-content-fetch/
    ├── code-exemplars-blueprint-generator/
    ├── document-parser/
    ├── expo-*                   # 15+ Expo-related skills
    ├── git-commit/
    ├── mcp-builder/
    ├── next-*                   # Next.js-related skills
    ├── openclaw-guardian/
    ├── react-*                  # React-related skills
    ├── shopify-seo-optimizer/
    ├── skill-creator/
    ├── swarmclaw/
    ├── test-driven-development/
    ├── vue-*                    # 10+ Vue-related skills
    └── ...
```

### Skill Categories

The index table reveals skills covering the following domains:

1. **Development Tools** — git-commit, chrome-devtools, systematic-debugging, test-driven-development
2. **Frontend Frameworks** — next-*, expo-*, react-*, vue-*, nuxt, vite, vitepress
3. **Architecture Design** — architecture-patterns, microservices-patterns, api-design-principles
4. **AI Engineering** — ai-prompt-generator, prompt-engineering-patterns, rag-implementation, mcp-builder
5. **Marketing & Growth** — copywriting, seo-audit, content-strategy, email-sequence, paid-ads
6. **E-commerce Tools** — amazon-price-tracker, ebay-product-research, shopify-seo-optimizer
7. **Social Media** — tiktok-viral-predictor, weibo-trending-bot, youtube-auto-captions
8. **Content Processing** — clean-content-fetch, document-parser, pdf, docx, pptx, xlsx
9. **Browser Automation** — browser-use, playwright integration
10. **Agent Management** — agent-governance, swarmclaw, openclaw-guardian, miniade-agent-lifecycle-manager

## Key Features

### 1. Multi-Language Support

README is available in 8 language versions:
- English (README.md)
- Chinese (README.zh-CN.md)
- French (README.fr.md)
- German (README.de.md)
- Russian (README.ru.md)
- Japanese (README.ja.md)
- Italian (README.it.md)
- Spanish (README.es.md)

### 2. Automated Collection & Updates

`scripts/collect.sh` implements the weekly automation pipeline:
- Scans three data sources
- Validates skill format and quality
- Automatically merges into the repository
- Generates CHANGELOG entries
- Pushes to GitHub

### 3. Convenient Installation Methods

**Method 1: Via ClaWHub**
```bash
clawhub install openclaw-master-skills
```

**Method 2: Manual installation**
```bash
git clone https://github.com/LeoYeAI/openclaw-master-skills.git
cp -r openclaw-master-skills/skills/<skill-name> ~/.openclaw/workspace/skills/
```

### 4. Quality Review Standards

Each skill must meet:
- Contains a valid `SKILL.md` file
- Clear purpose statement (when to use)
- No hardcoded credentials
- Works on standard OpenClaw

### 5. Community Contribution Mechanism

Supports two submission methods:
1. Submit an Issue (using the Submit Skill template)
2. Submit a Pull Request directly (adding a skill folder under `skills/`)

### 6. Brand Endorsement

Powered by **MyClaw.ai** — an AI personal assistant platform that runs a dedicated server for each user. OpenClaw Master Skills is its curated, weekly-updated collection of the best skills in the ecosystem.

## Summary

OpenClaw Master Skills is a **curated skill repository** that solves the problems of scattered skills and inconsistent quality in the OpenClaw ecosystem through automated collection, quality review, and a unified index. Its core value lies in:

1. **Reducing discovery cost** — Users no longer need to search across multiple platforms; one repository provides all quality skills
2. **Ensuring quality** — Unified review standards ensure skill usability and security
3. **Continuous updates** — Weekly automatic updates ensure users always have access to the latest skills
4. **Easy installation** — One-click installation lowers the barrier to use

<!-- lastCommit: 6a7050b -->
