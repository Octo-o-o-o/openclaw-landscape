# OpenClaw Master Skills

## 基本信息

- **项目名称**: openclaw-master-skills
- **GitHub**: https://github.com/LeoYeAI/openclaw-master-skills
- **Stars**: 1,391
- **语言**: Python
- **许可证**: MIT License
- **创建时间**: 2026-03-02
- **最后更新**: 2026-03-11
- **维护者**: LeoYeAI / MyClaw.ai
- **技能数量**: 164 个（README 中标注 127+）

## 问题与解决方案

### 核心问题

1. **技能分散难发现** — OpenClaw 生态中优质技能分散在 skills.sh、GitHub、ClaWHub 等多个平台，用户难以发现和评估
2. **质量参差不齐** — 社区贡献的技能缺乏统一的质量标准和审核机制
3. **缺乏分类索引** — 没有统一的技能目录和分类体系，用户无法快速定位所需技能
4. **更新不及时** — 用户需要手动追踪多个来源的技能更新

### 解决方案

**策展式技能仓库** — 通过自动化脚本每周扫描三大来源（skills.sh 排行榜、GitHub `openclaw-skill` 标签、ClaWHub 最新发布），经过验证、测试后合并到统一仓库，提供：

- **统一入口** — 单一仓库集中管理所有优质技能
- **质量保证** — 每个技能必须包含有效的 `SKILL.md`、清晰的用途说明、无硬编码凭证、可在标准 OpenClaw 上运行
- **分类索引** — 提供表格式技能索引，包含技能名称、描述、分类、来源、添加时间
- **自动更新** — 每周一自动更新 CHANGELOG.md，用户可订阅获取最新技能
- **便捷安装** — 支持 `clawhub install openclaw-master-skills` 一键安装，或手动复制到 `~/.openclaw/workspace/skills/`

## 核心架构

### 技能收集流程

```
┌─────────────────────────────────────────────────────────────┐
│                    Weekly Collection Cycle                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Data Sources (3 channels)        │
        ├─────────────────────────────────────────┤
        │  1. skills.sh (leaderboard top skills)  │
        │  2. GitHub (repos tagged openclaw-skill)│
        │  3. ClaWHub (latest published skills)   │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │      Validation & Quality Check          │
        ├─────────────────────────────────────────┤
        │  • SKILL.md format validation           │
        │  • Clear purpose statement check        │
        │  • No hardcoded credentials scan        │
        │  • Standard OpenClaw compatibility test │
        └─────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Merge & Organize                 │
        ├─────────────────────────────────────────┤
        │  • Copy to skills/<skill-name>/         │
        │  • Update README.md index table         │
        │  • Generate CHANGELOG.md entry          │
        │  • Commit & push to main branch         │
        └─────────────────────────────────────────┘
```

### 目录结构

```
openclaw-master-skills/
├── README.md                    # 主索引（8 种语言版本）
├── CHANGELOG.md                 # 每周更新日志
├── RELEASES.md                  # 版本发布记录
├── SKILL.md                     # 仓库本身的技能定义
├── scripts/
│   └── collect.sh               # 自动收集脚本
└── skills/                      # 164 个技能目录
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
    ├── expo-*                   # 15+ Expo 相关技能
    ├── git-commit/
    ├── mcp-builder/
    ├── next-*                   # Next.js 相关技能
    ├── openclaw-guardian/
    ├── react-*                  # React 相关技能
    ├── shopify-seo-optimizer/
    ├── skill-creator/
    ├── swarmclaw/
    ├── test-driven-development/
    ├── vue-*                    # 10+ Vue 相关技能
    └── ...
```

### 技能分类

从索引表可以看出技能覆盖以下领域：

1. **开发工具类** — git-commit, chrome-devtools, systematic-debugging, test-driven-development
2. **前端框架** — next-*, expo-*, react-*, vue-*, nuxt, vite, vitepress
3. **架构设计** — architecture-patterns, microservices-patterns, api-design-principles
4. **AI 工程** — ai-prompt-generator, prompt-engineering-patterns, rag-implementation, mcp-builder
5. **营销增长** — copywriting, seo-audit, content-strategy, email-sequence, paid-ads
6. **电商工具** — amazon-price-tracker, ebay-product-research, shopify-seo-optimizer
7. **社交媒体** — tiktok-viral-predictor, weibo-trending-bot, youtube-auto-captions
8. **内容处理** — clean-content-fetch, document-parser, pdf, docx, pptx, xlsx
9. **浏览器自动化** — browser-use, playwright 集成
10. **Agent 管理** — agent-governance, swarmclaw, openclaw-guardian, miniade-agent-lifecycle-manager

## 关键特性

### 1. 多语言支持

README 提供 8 种语言版本：
- English (README.md)
- 中文 (README.zh-CN.md)
- Français (README.fr.md)
- Deutsch (README.de.md)
- Русский (README.ru.md)
- 日本語 (README.ja.md)
- Italiano (README.it.md)
- Español (README.es.md)

### 2. 自动化收集与更新

`scripts/collect.sh` 实现每周自动化流程：
- 扫描三大数据源
- 验证技能格式和质量
- 自动合并到仓库
- 生成 CHANGELOG 条目
- 推送到 GitHub

### 3. 便捷安装方式

**方式一：通过 ClaWHub**
```bash
clawhub install openclaw-master-skills
```

**方式二：手动安装**
```bash
git clone https://github.com/LeoYeAI/openclaw-master-skills.git
cp -r openclaw-master-skills/skills/<skill-name> ~/.openclaw/workspace/skills/
```

### 4. 质量审核标准

每个技能必须满足：
- 包含有效的 `SKILL.md` 文件
- 清晰的用途说明（when to use）
- 无硬编码凭证（no hardcoded credentials）
- 可在标准 OpenClaw 上运行（works on standard OpenClaw）

### 5. 社区贡献机制

支持两种提交方式：
1. 提交 Issue（使用 Submit Skill 模板）
2. 直接提交 Pull Request（在 `skills/` 下添加技能文件夹）

### 6. 品牌背书

由 **MyClaw.ai** 驱动 — 一个为每个用户提供专属服务器运行的 AI 个人助手平台。OpenClaw Master Skills 是其策展的、每周更新的生态最佳技能集合。
# ClawButler Skill Descriptor (CBSD)
skill:
  id: "shopify-seo-optimizer"
  name: "Shopify SEO Optimi
  version: "1.0.0"
  platforms:
    - openclaw: "skills/shopify-seo-optimizer"
    - dify: "tools/shopify-seo"
    - langraph: "nodes/seo-optimizer"
  capabilities:
    - read_shopify_products
    - update_product_metadata
    - generate_seo_content
  mcp_tools:
    - shopify_get_products
    - shopify_update_product
  security:
    requires_approval: true
    allowed_scopes: ["read:products", "write:products"]
```

### 3. 自动化更新与通知

**借鉴点**：每周自动更新机制可以应用到 ClawButler 的 **Config Safety V2** 和 **Verified Templates V2.5**：

- **模板更新检测** — 定期扫描已安装模板的上游版本，检测更新
- **兼容性分析** — 自动分析新版本与当前环境的兼容性（依赖版本、API 变更）
- **升级建议** — 生成升级报告，标注破坏性变更（breaking changes）和推荐升级路径
- **一键升级** — 提供 `clawbutler template upgrade <template-id>` 命令，支持 dry-run 预览

**实现示例**：
```bash
# ClawButler 模板管理命令
clawbutler template list                    # 列出已安装模板
clawbutler template search "seo"            # 搜索模板
clawbutler template install shopify-seo     # 安装模板
clawbutler template upgrade --check         # 检查可用更新
clawbutler template upgrade shopify-seo --dry-run  # 预览升级
clawbutler template upgrade shopify-seo     # 执行升级
```

### 4. 社区贡献与生态建设

**借鉴点**：OpenClaw MasteSkills 的社区贡献机制可以启发 ClawButler 的 **生态建设策略**：

- **贡献者激励** — 建立贡献者排行榜，优质模板作者获得 "Verified Contributor" 徽章
- **模板市场** — 允许企业发布付费模板（类似 Dify 的 DSL 市场），ClawButler 抽取平台费
- **认证计划** — 推出 "ClawButler Certified Template" 认证，通过认证的模板获得官方推荐
- **文档标准** — 制定模板文档规范（README、CHANGELOG、示例配置），提高模板可用性

### 5. 多语言国际化

**借鉴点**：8 种语言的 README 展示了国际化的重要性，ClawButler 可以：

- **文档国际化** — 核心文档提供中英双语版本（已部分实现）
- **UI 国际化** — Web 界面已支持 zh-CN / en-US（1424 keys each），可扩展到更多语言
- **模板国际化** — 模板描述支持多语言，用户可以按语言筛选
- **社区本地化** — 建立不同语言的社区频道（Discord、微信群、Telegram），降低非英语用户的参与门槛

### 6. 技能组合与工作流
借鉴点**：164 个技能的组合可以形成复杂工作流，ClawButler 的 **Runbook** 功能可以：

- **技能编排** — 将多个技能组合成 Runbook（例如：`clean-content-fetch` → `document-parser` → `ai-prompt-generator` → `copywriting`）
- **跨平台调度** — Runbook 可以调用不同平台的 Agent（OpenClaw 技能 + Dify 工具 + LangGraph 节点）
- **条件分支** — 根据技能执行结果选择不同路径（类似 LangGraph 的条件边）
- **错误处理** — 技能失败时自动重试或回退到备用技能

**实现示例**：
```yaml
# ClawButler Runbook: SEO Content Pipeline
runbook:
  name: "SEO Content Pipeline"
  version: "1.0.0"
  steps:
    - id: "fetch_content"
      skill: "clean-content-fetch"
      platform: "openclaw"
      input:
        url: "{{ input.url }}"
    - id: "parse_document"
      skill: "document-parser"
      platform: "openclaw"
      input:
        content: "{{ steps.fetch_content.output }}"
    - id: "generate_seo"
      skill: "shopify-seo-optimizer"
      platform: "dify"
      input:
        product_data: "{{ steps.parse_document.output }}"
    - id: "review"
      skill: "copywriting"
      platform: "openclaw"
      input:
        draft: "{{ steps.generate_seo.output }}"
  error_handling:
    retry: 3
    fallback: "notify_admin"
```

### 7. 技能发现与推荐

**借鉴点**：技能索引表提供了良好的发现体验，ClawButler 可以：

- **智能推荐** — 根据用户的 Agent 配置和使用历史，推荐相关技能和模板
- **依赖分析** — 分析技能之间的依赖关系（例如 `expo-tailwind-setup` 依赖 `expo-building-native-ui`），自动安装依赖
- **使用统计** — 展示技能的使用频率、成功率、平均执行时间，帮助用户选择可靠的技能
- **相似技能对比** — 提供同类技能的对比表（功能、性能、维护状态），帮助用户做出选择

## 总结

OpenClaw Master Skills 是一个 **策展式技能仓库**，通过自动化收集、质量审核、统一索引，解决了 OpenClaw 生态中技能分散、质量参差不齐的问题。其核心价值在于：

1. **降低发现成本** — 用户无需在多个平台搜索，一个仓库即可获取所有优质技能
2. **保证质量** — 统一的审核标准确保技能可用性和安全性
3. **持续更新** — 每周自动更新，用户始终能获取最新技能
4. **便捷安装** — 一键安装，降低使用门槛

对 ClawButler 而言，可以借鉴其 **策展机制、质量标准、自动化流程、社区贡献模式**，建立跨平台的 Agent 模板和技能市场，提升用户体验和生态活力。
