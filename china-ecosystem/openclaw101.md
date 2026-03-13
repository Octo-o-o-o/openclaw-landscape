# OpenClaw 101 — 7天学习路径与资源聚合站

## 基本信息

- **GitHub**: https://github.com/mengjian-github/openclaw101
- **Stars**: 2,011
- **在线访问**: https://openclaw101.dev
- **作者**: 小墨（孟健AI编程）
- **定位**: 开源的 OpenClaw 中文资源聚合站与学习路径指南

## 问题与解决方案

### 核心痛点

1. **中文资源分散** — OpenClaw 官方文档以英文为主，中文教程散落在阿里云、腾讯云、B站、CSDN、博客园等平台，新手难以系统化学习
2. **学习路径不清晰** — 从认识 OpenClaw 到实际部署、接入平台、开发技能，缺乏结构化的进阶指南
3. **资源质量参差不齐** — 社区教程质量不一，缺少权威筛选和分类
4. **场景化技能推荐缺失** — 用户不知道针对特定场景（如企业协作、个人助理、内容创作）应该安装哪些技能

### 解决方案

OpenClaw 101 通过以下方式解决上述问题：

1. **资源聚合** — 收录 35+ 篇来自阿里云、腾讯云、DigitalOcean、Hostinger、Codecademy、IBM Think、B站、Reddit 等平台的优质教程
2. **7天学习路径** — 提供从零基础到进阶的系统化学习指南（链接飞书知识库）
3. **分类筛选系统** — 按 9 大类别（官方资源、入门部署、平台接入、技能开发、视频教程、深度文章、工具插件、云平台部署、玩法场景）组织内容
4. **中英双语支持** — 同时收录中文和英文资源，支持语言筛选
5. **技能推荐** — 按场景分类推荐 AI 技能（企业协作、个人助理、开发工具、内容创作等）
6. **精选推荐** — 标记 `featured` 资源，帮助新手快速找到最佳入门教程

## 核心架构

### 技术栈

- **框架**: Next.js 14 (App Router)
- **语言**: TypeScript
- **样式**: Tailwind CSS
- **部署**: Cloudflare Pages
- **数据管理**: 静态 TypeScript 数据文件（`src/data/resources.ts`）

### 项目结构

```
src/
├── app/
│   ├── page.tsx              # 首页（英文）
│   ├── zh/page.tsx           # 首页（中文）
│   ├── resources/page.tsx    # 资源聚合页
│   ├── layout.tsx            # 全局布局
│   └── globals.css           # 全局样式
├── components/
│   ├── Hero.tsx              # 首屏 Banner
│   ├── WhatIs.tsx            # OpenClaw 介绍
│   ├── LearningPath.tsx      # 7天学习路径
│   ├── Skills.tsx            # 技能推荐
│   ├── ResourcesSection.tsx  # 首页资源精选
│   ├── Community.tsx         # 社区与贡献
│   ├── Navbar.tsx            # 导航栏
│   ├── Footer.tsx            # 页脚
│   └── LanguageSwitcher.tsx  # 语言切换
└── data/
    └── resources.ts          # 📚 所有资源数据（核心数据源）
```

### 数据模型

```typescript
interface Resource {
  title: string;           // 资源标题
  desc: string;            // 一句话描述
  url: string;             // 资源链接
  source: string;          // 来源名称（阿里云、腾讯云等）
  sourceIcon?: string;     // 来源图标（可选）
  lang: 'zh' | 'en';       // 语言
  category: ResourceCategory;  // 分类
  featured?: boolean;      // 是否推荐
  tags?: string[];         // 标签
}

type ResourceCategory =
  | 'official'              // 官方资源
  | 'getting-started'       // 入门部署
  | 'channel-integration'   // 平台接入
  | 'skill-dev'             // 技能开发
  | 'video'                 // 视频教程
  | 'deep-dive'             // 深度文章
  | 'tools'                 // 工具与插件
  | 'cloud-deploy'          // 云平台部署
  | 'use-cases';            // 玩法与场景
```

### 资源分类体系

| 分类 | 图标 | 中文标签 | 英文标签 | 颜色 |
|------|------|----------|----------|------|
| official | 📖 | 官方资源 | Official | blue |
| getting-started | 🏁 | 入门部署 | Getting Started | green |
| channel-integration | 📱 | 平台接入 | Channels | purple |
| skill-dev | 🧩 | 技能开发 | Skills | orange |
| video | 📹 | 视频教程 | Videos | red |
| deep-dive | 🔬 | 深度文章 | Deep Dives | indigo |
| tools | 🔧 | 工具与插件 | Tools | teal |
| cloud-deploy | ☁️ | 云平台部署 | Cloud Deploy | sky |
| use-cases | 💡 | 玩法与场景 | Use Cases | amber |

## 关键特性

### 1. 资源聚合与筛选

- **35+ 优质资源** — 覆盖官方文档、云平台教程、社区博客、视频教程
- **多维度筛选** — 按分类、语言、关键词快速定位
- **来源标注** — 清晰标注资源来源（阿里云、腾讯云、DigitalOcean、B站等）
- **精选推荐** — `featured` 标记帮助新手快速找到最佳入门路径

### 2. 7天学习路径

链接飞书知识库，提供结构化学习指南：
- Day 1: 认识 OpenClaw
- Day 2-3: 部署与配置
- Day 4-5: 平台接入（飞书、钉钉、企业微信、Telegram）
- Day 6: 技能开发
- Day 7: 进阶与优化

### 3. 场景化技能推荐

按使用场景推荐技能：
- **企业协作** — 飞书、钉钉、企业微信接入
- **个人助理** — 日程管理、提醒、笔记
- **开发工具** — GitHub 集成、代码审查
- **内容创作** — 文案生成、图片编辑

### 4. 中英双语支持

- 同时收录中文和英文资源
- 语言筛选功能
- 中英文界面切换

### 5. 云平台部署教程聚合

重点收录云平台一键部署教程：
- **阿里云** — 轻量应用服务器一键部署，钉钉/企业微信接入
- **腾讯云** — Lighthouse 一键部署，飞书/企业微信接入
- **DigitalOcean** — One-Click Deploy
- **Hostinger** — VPS 部署教程

### 6. 社区贡献机制

- 开源仓库，欢迎 PR
- 清晰的贡献指南（如何添加新资源）
- Issue 跟踪与功能建议
## 总结

OpenClaw 101 是一个优秀的 **资源聚合与学习路径** 项目，通过系统化的内容组织和场景化的推荐，降低了 OpenClaw 的学习门槛。ClawButler 可以借鉴其思路，建立 **Agent 生态资源聚合站**、**场景化模板推荐**、**交互式 Onboarding**，提升用户体验和社区活跃度。
