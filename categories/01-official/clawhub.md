# openclaw/clawhub

## 基本信息

- **GitHub 仓库**: https://github.com/openclaw/clawhub
- **Stars**: 5,292
- **官方网站**: https://clawhub.ai
- **姊妹站点**: https://onlycrabs.ai (SOUL.md 注册中心)
- **创建时间**: 2026-01-03
- **最后更新**: 2026-03-11
- **主要语言**: TypeScript
- **仓库大小**: 2,622 KB

## 问题与解决方案

### 核心问题

OpenClaw 生态系统面临的核心问题是 **Agent 技能（Skills）的分发、版本管理和发现**。随着 AI Agent 能力的扩展，需要一个标准化的方式来：

1. **发布和共享技能**：开发者需要一个中心化的平台来发布他们为 Agent 开发的技能包
2. **版本控制**：技能需要语义化版本管理、变更日志和回滚能力
3. **依赖声明**：技能需要明确声明运行时依赖（环境变量、二进制工具、配置文件）
4. **安全审核**：需要对上传的技能进行安全扫描和内容审核，防止恶意代码
5. **可发现性**：用户需要通过语义搜索（而非关键词）快速找到所需技能
6. **CLI 友好**：技能的安装、更新、同步需要通过命令行工具无缝完成

### 解决方案

ClawHub 提供了一个 **公共技能注册中心**（类似 npm、PyPI），具备以下核心能力：

- **基于文本的技能包格式**：每个技能是一个包含 `SKILL.md`（必需）和支持文件的文件夹
- **语义化版本 + 标签系统**：每次发布创建新版本，支持 `latest` 等标签指针
- **向量搜索**：使用 OpenAI embeddings + Convex 向量索引实现语义搜索
- **GitHub OAuth 认证**：通过 GitHub 账号登录，14 天账号年龄门槛防止滥用
- **自动化安全扫描**：静态分析技能代码，检测元数据不匹配、可疑行为
- **审核机制**：用户举报、自动隐藏（>3 举报）、版主/管理员审核流程
- **CLI 工具**：`clawhub` 命令行工具支持 `install`、`update`、`publish`、`sync` 等操作
- **GitHub 备份**：通过 GitHub App 自动备份所有技能到 `clawdbot/skills` 仓库

## 核心架构

### 技术栈

- **前端**: TanStack Start (React + Vite/Nitro) - 现代化 SPA 框架
- **后端**: Convex - 无服务器数据库 + 文件存储 + HTTP Actions
- **认证**: Convex Auth + GitHub OAuth
- **搜索**: OpenAI `text-embedding-3-small` + Convex 向量索引
- **CLI**: Bun + TypeScript，发布为 `clawhub` npm 包
- **共享层**: `clawhub-schema` 包定义 API 路由和类型
- **测试**: Vitest 4，目标覆盖率 ≥70%
- **代码质量**: Biome + Oxlint（类型感知）

### 数据模型

#### 核心实体

1. **User（用户）**
   - `authId`（Convex Auth 提供）
   - `handle`（GitHub 用户名）
   - `role`: `admin | moderator | user`
   - `avatarUrl`、`name`、`bio`
   - `githubCreatedAt`（用于 14 天账号年龄门槛）

2. **Skill（技能）**
   - `slug`（唯一标识符）
   - `displayName`、`summary`
   - `ownerUserId`
   - `latestVersionId`、`latestTagVersionId`
   - `tags` 映射：`{ tag -> versionId }`
   - `badges`：`redactionApproved`、`highlighted`、`official`、`deprecated`
   - `moderationStatus`: `active | hidden | removed`
   - `moderationFlags`、`moderationReason`
   - `stats`：`downloads`、`stars`、`versions`、`comments`

3. **SkillVersion（技能版本）**
   - `skillId`、`version`（semver）
   - `changelog`（必需）
   - `files`：`[{ path, size, storageId, sha256 }]`
   - `parsed`（从 SKILL.md frontmatter 提取的元数据）
   - `embeddingId`（向量搜索）
   - `softDeletedAt`（软删除）

4. **Soul（灵魂/系统人格）**
   - 与 Skill 类似的结构，但仅接受 `SOUL.md` 文件
   - 托管在 onlycrabs.ai（基于主机名的入口点）

5. **Comment、Star、AuditLog**
   - 评论、收藏、审计日志

#### 元数据规范

技能在 `SKILL.md` 的 YAML frontmatter 中声明运行时需求：

```yaml
---
name: my-skill
description: 通过 Todoist API 管理任务
metadata:
  openclaw:
    requires:
      env:
        - TODOIST_API_KEY
      bins:
        - curl
    primaryEnv: TODOIST_API_KEY
    install:
      - kind: brew
        formula: jq
        bins: [jq]
---
```

支持的字段：
- `requires.env`：环境变量
- `requires.bins`：必需的 CLI 工具
- `requires.anyBins`：至少需要一个的 CLI 工具
- `requires.config`：配置文件路径
- `install`：依赖安装规范（brew、node、go、uv）
- `nix`：Nix 插件指针（用于 nix-clawdbot）
- `os`：操作系统限制

### 关键设计决策

1. **纯文本技能包**
   - 限制为文本文件（50MB 上限），不接受二进制文件
   - 扩展名白名单 + MIME 类型检查
   - 降低安全风险，便于静态分析

2. **Convex 作为后端**
   - 无服务器架构，简化部署
   - 内置文件存储（`_storage`）
   - 实时查询 + HTTP Actions
   - 向量搜索原生支持

3. **软删除 + 审核流程**
   - 版本软删除（`softDeletedAt`），保留历史
   - 自动隐藏机制（>3 举报）
   - 版主可恢复，管理员可硬删除

4. **GitHub 账号年龄门槛**
   - 发布技能/灵魂需要 GitHub 账号 ≥14 天
   - 评论也需要 ≥14 天
   - 减少垃圾内容和滥用

5. **向量搜索优先**
   - 使用 embeddings 而非关键词搜索
   - 索引 SKILL.md + 其他文本文件 + 元数据摘要
   - 支持过滤器（标签、所有者、最小星标数、更新时间）

6. **CLI 优先的工作流**
   - `clawhub install <slug>` - 安装技能
   - `clawhub sync` - 扫描本地技能，自动发布/更新
   - `clawhub update --all` - 批量更新
   - 本地状态管理：`.clawhub/lock.json`（工作目录）+ `.clawhub/origin.json`（技能文件夹）

## 关键特性

### 1. 技能发布与版本管理

- **上传流程**（50MB 限制）：
  1. 客户端请求上传会话
  2. 通过 Convex 上传 URL 上传每个文件
  3. 提交元数据 + 文件列表 + 变更日志 + 版本 + 标签
  4. 服务器验证（大小、扩展名、SKILL.md 存在、frontmatter 可解析、版本唯一性、GitHub 账号年龄）
  5. 存储文件 + 元数据，设置 `latest` 标签，更新统计

- **版本控制**：
  - 每次上传创建新 `SkillVersion`
  - `latest` 标签自动指向最新版本（除非用户重新标记）
  - 支持回滚：移动 `latest`（和其他标签）到旧版本

### 2. 安全与审核

- **静态扫描**：
  - 发布时持久化确定性静态扫描结果
  - `moderationVerdict`: `clean | suspicious | malicious`
  - `moderationReasonCodes[]`：机器可读的原因代码
  - `moderationEvidence[]`：文件/行证据（有上限）

- **举报机制**：
  - 每个用户最多 20 个活跃举报
  - 第 4 个唯一举报触发自动隐藏
  - 技能举报：软删除 + `moderationStatus = hidden`
  - 评论举报：软删除评论

- **AI 评论扫描**：
  - 使用 OpenAI 分类诈骗评论
  - `scamScanVerdict`: `not_scam | likely_scam | certain_scam`
  - 仅 `certain_scam` + `high` 置信度触发自动封禁

- **封禁流程**：
  - 硬删除所有拥有的技能
  - 软删除所有评论
  - 撤销 API 令牌
  - 设置 `deletedAt`

### 3. CLI 工具

- **认证**：`clawhub login`、`clawhub whoami`
- **发现**：`clawhub search ...`、`clawhub explore`
- **本地管理**：
  - `clawhub install <slug>` - 安装到 `./skills/<slug>`
  - `clawhub uninstall <slug>` - 仅删除本地安装
  - `clawhub list` - 列出已安装技能
  - `clawhub update --all` - 批量更新
- **检查**：`clawhub inspect <slug>` - 不安装直接查看
- **发布**：
  - `clawhub publish <path>` - 发布单个技能
  - `clawhub sync` - 扫描根目录，自动发布/更新
- **遥测**：
  - `clawhub sync` 时报告安装遥测（计算安装数）
  - 通过 `CLAWHUB_DISABLE_TELEMETRY=1` 禁用

### 4. Nix 插件支持

- **nixmode 技能**：
  - 在 SKILL.md frontmatter 中存储 nix-clawdbot 插件指针
  - Nix 插件捆绑技能包 + CLI 二进制 + 配置标志/需求

示例：
```yaml
---
name: peekaboo
metadata:
  clawdbot:
    nix:
      plugin: "github:clawdbot/nix-steipete-tools?dir=tools/peekaboo"
      systems: ["aarch64-darwin"]
    config:
      requiredEnv: ["PADEL_AUTH_FILE"]
      stateDirs: [".config/padel"]
      example: "config = { env = { PADEL_AUTH_FILE = \"/run/agenix/padel-auth\"; }; };"
    cliHelp: "padel --help\nUsage: padel [command]\n"
---
```

### 5. onlycrabs.ai（SOUL.md 注册中心）

- **基于主机名的入口点**：`onlycrabs.ai`
- **灵魂捆绑包**：仅接受 `SOUL.md`（暂不支持额外文件）
- **与技能共享基础设施**：相同的版本控制、搜索、审核机制
- **用途**：发布和共享 Agent 的系统人格/提示词

### 6. GitHub 备份

- **GitHub App 集成**：
  - 自动备份所有技能到 `openclaw/skills` 仓库（2,524 stars）
  - 当前存档 1,000+ 个技能
  - 每个技能一个目录，包含所有版本
- **历史存档**：
  - 保留可疑/恶意技能用于进一步分析
  - 用户应优先使用网站下载，将此视为历史存档
## 总结

ClawHub 是 OpenClaw 生态系统的关键基础设施，解决了 Agent 技能的分发、版本管理、安全审核和发现问题。其核心价值在于：

1. **标准化**：定义了技能包格式和元数据规范
2. **安全优先**：多层次的安全审核机制
3. **开发者友好**：CLI 优先的工作流 + 自动化同步
4. **语义搜索**：向量搜索提升可发现性
5. **社区驱动**：开放的发布平台 + 审核机制

对于 ClawButler 而言，ClawHub 提供了一个成熟的参考架构，可以借鉴其在模板管理、安全审核、向量搜索、CLI 工具、遥测统计等方面的设计，进一步增强 ClawButler 作为 Agent 控制平面的能力。
