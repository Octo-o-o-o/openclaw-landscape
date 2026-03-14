> https://github.com/mengjian-github/openclaw101

# OpenClaw 101 — 7-Day Learning Path & Resource Aggregation Site

## Basic Information

- **GitHub**: https://github.com/mengjian-github/openclaw101
- **Stars**: 2,011
- **Online Access**: https://openclaw101.dev
- **Author**: Xiao Mo (Mengjian AI Programming)
- **Positioning**: An open-source OpenClaw Chinese resource aggregation site and learning path guide

## Problem & Solution

### Core Pain Points

1. **Scattered Chinese resources** — OpenClaw's official documentation is primarily in English, while Chinese tutorials are scattered across Alibaba Cloud, Tencent Cloud, Bilibili, CSDN, cnblogs, and other platforms, making it difficult for beginners to learn systematically
2. **Unclear learning path** — From understanding OpenClaw to actual deployment, platform integration, and skill development, there is no structured progression guide
3. **Uneven resource quality** — Community tutorials vary in quality, lacking authoritative curation and categorization
4. **Missing scenario-based skill recommendations** — Users don't know which skills to install for specific scenarios (e.g., enterprise collaboration, personal assistant, content creation)

### Solution

OpenClaw 101 addresses these issues through:

1. **Resource aggregation** — Curates 35+ quality tutorials from platforms including Alibaba Cloud, Tencent Cloud, DigitalOcean, Hostinger, Codecademy, IBM Think, Bilibili, Reddit, and more
2. **7-day learning path** — Provides a structured learning guide from zero to advanced (linked to a Feishu/Lark knowledge base)
3. **Category filtering system** — Content organized into 9 major categories (official resources, getting started, platform integration, skill development, video tutorials, deep-dive articles, tools & plugins, cloud platform deployment, use cases & scenarios)
4. **Bilingual support** — Curates both Chinese and English resources with language filtering
5. **Skill recommendations** — Recommends AI skills by scenario (enterprise collaboration, personal assistant, developer tools, content creation, etc.)
6. **Featured picks** — Marks `featured` resources to help beginners quickly find the best starting tutorials

## Core Architecture

### Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Deployment**: Cloudflare Pages
- **Data management**: Static TypeScript data files (`src/data/resources.ts`)

### Project Structure

```
src/
├── app/
│   ├── page.tsx              # Homepage (English)
│   ├── zh/page.tsx           # Homepage (Chinese)
│   ├── resources/page.tsx    # Resource aggregation page
│   ├── layout.tsx            # Global layout
│   └── globals.css           # Global styles
├── components/
│   ├── Hero.tsx              # Hero banner
│   ├── WhatIs.tsx            # OpenClaw introduction
│   ├── LearningPath.tsx      # 7-day learning path
│   ├── Skills.tsx            # Skill recommendations
│   ├── ResourcesSection.tsx  # Homepage featured resources
│   ├── Community.tsx         # Community & contributions
│   ├── Navbar.tsx            # Navigation bar
│   ├── Footer.tsx            # Footer
│   └── LanguageSwitcher.tsx  # Language toggle
└── data/
    └── resources.ts          # All resource data (core data source)
```

### Data Model

```typescript
interface Resource {
  title: string;           // Resource title
  desc: string;            // One-line description
  url: string;             // Resource link
  source: string;          // Source name (Alibaba Cloud, Tencent Cloud, etc.)
  sourceIcon?: string;     // Source icon (optional)
  lang: 'zh' | 'en';       // Language
  category: ResourceCategory;  // Category
  featured?: boolean;      // Whether featured
  tags?: string[];         // Tags
}

type ResourceCategory =
  | 'official'              // Official resources
  | 'getting-started'       // Getting started
  | 'channel-integration'   // Platform integration
  | 'skill-dev'             // Skill development
  | 'video'                 // Video tutorials
  | 'deep-dive'             // Deep-dive articles
  | 'tools'                 // Tools & plugins
  | 'cloud-deploy'          // Cloud platform deployment
  | 'use-cases';            // Use cases & scenarios
```

### Resource Category System

| Category | Icon | Chinese Label | English Label | Color |
|----------|------|---------------|---------------|-------|
| official | Book | Official Resources | Official | blue |
| getting-started | Flag | Getting Started | Getting Started | green |
| channel-integration | Phone | Platform Integration | Channels | purple |
| skill-dev | Puzzle | Skill Development | Skills | orange |
| video | Camera | Video Tutorials | Videos | red |
| deep-dive | Microscope | Deep-Dive Articles | Deep Dives | indigo |
| tools | Wrench | Tools & Plugins | Tools | teal |
| cloud-deploy | Cloud | Cloud Deployment | Cloud Deploy | sky |
| use-cases | Lightbulb | Use Cases & Scenarios | Use Cases | amber |

## Key Features

### 1. Resource Aggregation & Filtering

- **35+ quality resources** — Covering official documentation, cloud platform tutorials, community blogs, and video tutorials
- **Multi-dimensional filtering** — Filter by category, language, and keywords for quick discovery
- **Source attribution** — Clearly labels resource sources (Alibaba Cloud, Tencent Cloud, DigitalOcean, Bilibili, etc.)
- **Featured picks** — `featured` markers help beginners quickly find the best entry path

### 2. 7-Day Learning Path

Links to a Feishu (Lark) knowledge base, providing a structured learning guide:
- Day 1: Get to know OpenClaw
- Day 2-3: Deployment and configuration
- Day 4-5: Platform integration (Feishu/Lark, DingTalk, WeCom, Telegram)
- Day 6: Skill development
- Day 7: Advanced topics and optimization

### 3. Scenario-Based Skill Recommendations

Recommends skills by use case:
- **Enterprise collaboration** — Feishu (Lark), DingTalk, WeCom integration
- **Personal assistant** — Schedule management, reminders, notes
- **Developer tools** — GitHub integration, code review
- **Content creation** — Copywriting generation, image editing

### 4. Bilingual Support

- Curates both Chinese and English resources
- Language filtering functionality
- Chinese/English interface switching

### 5. Cloud Platform Deployment Tutorial Aggregation

Focuses on curating one-click cloud deployment tutorials:
- **Alibaba Cloud** — Lightweight application server one-click deployment, DingTalk/WeCom integration
- **Tencent Cloud** — Lighthouse one-click deployment, Feishu (Lark)/WeCom integration
- **DigitalOcean** — One-Click Deploy
- **Hostinger** — VPS deployment tutorial

### 6. Community Contribution Mechanism

- Open source repository, PRs welcome
- Clear contribution guidelines (how to add new resources)
- Issue tracking and feature suggestions

<!-- lastCommit: 1d3a9c3 -->
