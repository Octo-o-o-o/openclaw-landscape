# xianyu110/awesome-openclaw-tutorial

## 基本信息

- **GitHub**: https://github.com/xianyu110/awesome-openclaw-tutorial
- **Stars**: 2,179
- **语言**: Shell
- **创建时间**: 2026-02-10
- **最后更新**: 2026-03-11
- **描述**: 从零开始玩转OpenClaw：最全面的中文教程，涵盖安装、配置、实战案例和避坑指南（github版）
- **Topics**: openclaw, openclaw-skills
- **总字数**: 约 418,000 字（15章正文 + 14个附录 + 1个安全指南）

## 问题与解决方案

### 核心问题

OpenClaw 作为强大的 AI Agent 平台，存在以下痛点：

1. **学习曲线陡峭**: 官方文档以英文为主，中文资料稀缺，国内用户上手困难
2. **配置复杂**: 涉及 API Key、Profile、Skills、MCP、Gateway 等多层配置，新手容易迷失
3. **版本升级陷阱**: 如 2026.3.2 版本将工具权限和聊天能力隔离，默认 profile 改为 `messaging`（纯聊天模式），导致升级后 AI "变哑巴"
4. **实战案例缺失**: 缺乏面向真实场景的端到端案例，用户不知道如何将 OpenClaw 应用到实际工作中
5. **避坑指南缺失**: 用户在使用过程中频繁遇到权限、配置、兼容性等问题，缺乏系统性的排障指南

### 解决方案

awesome-openclaw-tutorial 提供了一套完整的中文学习体系：

1. **系统化教程**: 15章正文覆盖从安装到高级应用的完整路径
   - 基础篇（第1-3章）: 介绍、安装、快速开始
   - 核心功能篇（第4-7章）: 文件管理、知识管理、日程管理、自动化工作流
   - 高级篇（第8-11章）: Skills 扩展、多平台集成、API 集成、高级配置
   - 实战篇（第12-15章）: 个人生产力、高级自动化、创意应用、超级个体案例

2. **14个附录**: 覆盖配置文件结构、API Key 配置、Skills 生态、搜索指南等专题

3. **安全指南**: 独立的安全配置章节（99-security-guide.md），涵盖权限管理、数据安全、网络安全

4. **70+实战案例**: 可直接应用的场景化案例，如自动化报告生成、知识库构建、日程智能提醒等

5. **版本升级指南**: 针对 2026.3.2、2026.3.7 等关键版本的 Breaking Changes 提供详细的迁移指南

6. **配图丰富**: 50+张配置截图，降低理解门槛

7. **持续更新**: 项目状态标记为"完成，正在持续优化中"，删除重复内容，提升质量

## 核心架构

### 教程结构

```
awesome-openclaw-tutorial/
├── docs/
│   ├── 01-basics/                    # 基础篇
│   │   ├── 01-introduction.md        # OpenClaw 介绍
│   │   ├── 02-installation.md        # 安装指南
│   │   └── 03-quick-start.md         # 快速开始
│   ├── 02-core-features/             # 核心功能篇
│   │   ├── 04-file-management.md     # 文件管理
│   │   ├── 05-knowledge-management.md # 知识管理
│   │   ├── 06-schedule-management.md  # 日程管理
│   │   └── 07-automation-workflow.md  # 自动化工作流
│   ├── 03-advanced/                  # 高级篇
│   │   ├── 08-skills-extension.md    # Skills 扩展
│   │   ├── 09-multi-platform-integration.md # 多平台集成
│   │   ├── 10-api-integration.md     # API 集成
│   │   ├── 11-advanced-configuration.md # 高级配置
│   │   └── 99-security-guide.md      # 安全指南
│   ├── 04-practical-cases/           # 实战篇
│   │   ├── 12-personal-productivity.md # 个人生产力
│   │   ├── 13-advanced-automation.md   # 高级自动化
│   │   ├── 14-creative-applications.md # 创意应用
│   │   └── 15-solo-entrepreneur-cases.md # 超级个体案例
│   ├── api-key-config-guide.md       # API Key 配置指南
│   ├── config-file-structure.md      # 配置文件结构
│   ├── skills-ecosystem.md           # Skills 生态
│   └── search-guide.md               # 搜索指南
├── appendix/                         # 附录（14个专题）
├── openclaw-manager/                 # OpenClaw 管理工具
├── scripts/                          # 辅助脚本
├── search.json                       # 搜索索引
└── README.md                         # 项目首页
```

### 技术栈

- **文档格式**: Markdown
- **静态站点生成**: Jekyll（GitHub Pages）
- **搜索功能**: 自定义 JSON 索引 + 前端搜索
- **版本管理**: Git + GitHub
- **辅助工具**: Shell 脚本（如 `update-version-to-2026.3.2.sh`）

### 内容组织原则

1. **渐进式学习路径**: 从基础到高级，从理论到实战
2. **场景驱动**: 每章以实际应用场景为导向，而非单纯的功能罗列
3. **避坑优先**: 在关键配置点提供"重要提示"和"常见错误"
4. **版本感知**: 明确标注版本差异，提供升级指南
5. **可搜索**: 提供全文搜索索引，支持快速定位问题

## 关键特性

### 1. 版本升级指南

**2026.3.7 版本 Breaking Change**:
- Gateway 认证现在要求显式设置 `gateway.auth.mode`
- 必须明确选择 `token` 或 `password` 认证方式
- 如果从旧版本升级且没有配置认证，Gateway 将拒绝启动

**快速修复**:
```bash
# 设置 token 认证
openclaw config set gateway.auth.mode token
openclaw config set gateway.auth.token "your-secret-token"

# 重启 Gateway
openclaw gateway restart
```

**2026.3.2 版本 Breaking Change**:
- 工具权限和聊天能力隔离，默认 profile 改为 `messaging`（纯聊天模式）
- 升级后 OpenClaw 只能聊天不能干活（文件管理、命令执行等工具功能全部失效）

**5种 profile 说明**:
| Profile | 功能说明 |
|---------|---------|
| `messaging` | 只能发消息、管理会话（光聊天不干活） |
| `default` | 默认工具集（不含命令执行） |
| `coding` | 编程相关工具 |
| `full` | 完整工具集，包含命令执行（**推荐**） |
| `custom` | 自定义工具集 |

**快速修复**:
```bash
# 方法1: 命令行切换
openclaw config set profile full

# 方法2: 编辑配置文件
# ~/.openclaw/openclaw.json
{
  "profile": "full"
}
```

### 2. 配置文件结构详解

教程提供了完整的配置文件结构说明（`docs/config-file-structure.md`），涵盖：

- **核心配置**: `~/.openclaw/openclaw.json`
  - `profile`: 工具权限配置
  - `model`: 默认模型配置
  - `gateway`: Gateway 配置（认证、端口、CORS）
  - `skills`: Skills 配置
  - `mcp`: MCP 服务器配置
  - `extensions`: 扩展插件配置

- **API Key 配置**: `~/.openclaw/api-keys.json`
  - 支持多个 LLM 提供商（OpenAI / Anthropic / Google / Azure / 国内厂商）
  - 支持多个 API Key（负载均衡、故障转移）

- **Skills 配置**: `~/.openclaw/skills/`
  - 每个 Skill 一个目录
  - `skill.json`: Skill 元数据
  - `AGENTS.md`: Skill 使用说明

- **MCP 配置**: `~/.openclaw/mcp-servers.json`
  - MCP 服务器注册
  - 工具/资源/提示词映射

### 3. Skills 生态系统

教程提供了 Skills 生态系统的完整介绍（`docs/skills-ecosystem.md`），包括：

- **官方 Skills**: OpenClaw 官方维护的 Skills
  - `agent-browser`: 浏览器自动化
  - `agent-memory`: 长期记忆
  - `agent-scheduler`: 定时任务
  - `agent-search`: 网络搜索

- **社区 Skills**: 社区贡献的 Skills
  - 数据库操作
  - 文件处理
  - API 集成
  - 通知推送

- **自定义 Skills**: 如何开发自己的 Skills
  - Skill 结构
  - 工具定义
  - 权限管理
  - 测试与发布

### 4. 多平台集成

教程详细介绍了 OpenClaw 与其他平台的集成（第9章）：

- **IM 平台**: 钉钉、企业微信、QQ、飞书（通过 openclaw-china）
- **知识库**: Notion、语雀、飞书文档
- **项目管理**: Jira、Trello、Asana
- **代码托管**: GitHub、GitLab、Gitee
- **云存储**: 阿里云 OSS、腾讯云 COS、AWS S3

### 5. API 集成

教程提供了 API 集成的完整指南（第10章）：

- **RESTful API**: 如何通过 HTTP 请求调用外部 API
- **GraphQL API**: 如何查询 GraphQL 接口
- **WebSocket**: 如何建立实时连接
- **Webhook**: 如何接收外部事件通知
- **认证方式**: API Key / OAuth 2.0 / JWT

### 6. 实战案例

教程提供了 70+ 实战案例，涵盖：

**个人生产力（第12章）**:
- 自动化日报/周报生成
- 智能邮件分类与回复
- 会议纪要自动整理
- 知识库自动构建

**高级自动化（第13章）**:
- 多步骤工作流编排
- 条件分支与循环
- 错误处理与重试
- 并行任务执行

**创意应用（第14章）**:
- AI 绘图（Midjourney / Stable Diffusion 集成）
- 内容创作（文章、视频脚本、社交媒体文案）
- 数据可视化
- 交互式故事生成

**超级个体案例（第15章）**:
- 独立开发者工作流
- 自媒体运营自动化
- 在线教育课程制作
- 电商运营助手

### 7. 安全指南

教程提供了独立的安全指南（`docs/03-advanced/99-security-guide.md`），涵盖：

- **权限管理**: Profile 配置、工具白名单、文件系统访问控制
- **数据安全**: API Key 保护、敏感数据加密、日志脱敏
- **网络安全**: Gateway 认证、HTTPS 配置、CORS 策略
- **审计日志**: 操作记录、异常检测、合规要求

### 8. 搜索功能

教程提供了全文搜索功能（`search.md` + `search.json`）：

- **搜索索引**: 自动生成的 JSON 索引，包含所有章节的标题、内容、关键词
- **前端搜索**: 基于 JavaScript 的客户端搜索，无需后端支持
- **搜索指南**: 如何高效使用搜索功能（`docs/search-guide.md`）

### 9. OpenClaw Manager

教程提供了 OpenClaw 管理工具（`openclaw-manager/`），用于：

- **一键安装**: 自动安装 OpenClaw 及常用 Skills
- **配置管理**: 图形化配置编辑器
- **版本管理**: 版本检查、升级、回滚
- **健康检查**: 服务状态监控、日志查看
## V2.5 Breaking Changes

### Config Safety V2: Snapshot Scope 字段重命名

**变更内容**: `snapshot.type` 重命名为 `snapshot.scope`

**影响范围**: 所有使用 Config Safety 的用户

**迁移步骤**:
1. 备份现有配置: `cp ~/.clawbutler/config.json ~/.clawbutler/config.json.bak`
2. 运行迁移脚本: `bash scripts/migrate-v2-to-v2.5.sh`
3. 验证配置: `clawbutlerctl config validate`

**快速修复**:
```bash
# 手动修改配置文件
sed -i 's/"type":/"scope":/g' ~/.clawbutler/config.json
```
```

### 3. 配置文件结构文档

**借鉴点**: awesome-openclaw-tutorial 提供了完整的配置文件结构说明，帮助用户理解每个配置项的作用。

**应用场景**:
- ClawButler 的配置文件（`.env` / `docker-compose.yml` / API 配置）较为复杂
- 用户在配置时容易遗漏关键参数或填写错误的值
- 需要提供配置文件的完整参考文档，包括每个字段的类型、默认值、示例、注意事项

**具体设计**:
- 创建 `docs/appendix/config-reference.md`，列出所有配置项
- 每个配置项包含：
  - **字段名**: `gateway.auth.mode`
  - **类型**: `string`
  - **默认值**: `token`
  - **可选值**: `token` / `password`
  - **描述**: Gateway 认证模式
  - **示例**: `"token"`
  - **注意事项**: 从 V2.5 开始必须显式设置，不再有默认值
- 提供配置文件模板（`deploy/.env.template`），包含所有字段的注释

### 4. 实战案例库

**借鉴点**: awesome-openclaw-tutorial 提供了 70+ 实战案例，帮助用户快速上手。

**应用场景**:
- ClawButler 的核心价值在于"统一 Agent 控制平面"，但用户可能不清楚具体如何应用
- 需要提供端到端的实战案例，展示 ClawButler 在真实场景中的价值
- 案例应覆盖不同行业、不同规模、不同技术栈

**具体设计**:
```
docs/04-practical-cases/
├── 13-agent-governance.md
│   ├── 案例1: 多团队 Agent 权限隔离
│   ├── 案例2: Agent 配置变更审计
│   └── 案例3: Agent 成本追踪与配额管理
├── 14-cross-platform-collab.md
│   ├── 案例1: OpenClaw + Dify 协作（A2A）
│   ├── 案例2: LangGraph Agent 调用 OpenClaw MCP 工具
│   └── 案例3: 自建 Agent 接入 ClawButler Federation
└── 15-enterprise-deployment.md
    ├── 案例1: 金融行业合规部署
    ├── 案例2: 制造业 IoT + Agent 集成
    └── 案例3: 电商行业客服 Agent 编排
```

### 5. 搜索功能

**借鉴点**: awesome-openclaw-tutorial 提供了全文搜索功能，帮助用户快速定位问题。

**应用场景**:
- ClawButler 文档量较大（当前约 50+ 文件），用户难以快速找到所需信息
- 需要提供搜索功能，支持关键词、标签、分类等多维度检索
- 可集成到 Web UI 中，提供更好的用户体验

**具体设计**:
- **静态搜索**: 参考 awesome-openclaw-tutorial，生成 JSON 索引，前端 JavaScript 搜索
- **动态搜索**: 集成到 ClawButler API，提供 `GET /api/v1/docs/search?q=keyword` 接口
- **AI 搜索**: 利用 LLM 的语义理解能力，支持自然语言查询（如"如何配置 OpenClaw 平台接入？"）

### 6. 避坑指南

**借鉴点**: awesome-openclaw-tutorial 在关键配置点提供"重要提示"和"常见错误"，帮助用户避坑。

**应用场景**:
- ClawButler 的部署和配置涉及多个组件（API / Web / Mobile / CLI / DB / Cache），容易出错
- 需要在文档中明确标注常见错误和解决方案
- 需要提供自动化的健康检查工具，帮助用户快速定位问题

**具体设计**:
- 在文档中添加"常见问题"章节（`docs/appendix/troubleshooting.md`）
- 在关键配置点添加"⚠️ 重要提示"和"❌ 常见错误"
- 提供 `clawbutlerctl doctor` 命令，自动检查配置、依赖、权限等问题
- 在 Web UI 中添加"健康检查"面板，实时显示各组件状态

**示例**:
```markdown
## 常见问题

### API 容器启动失败：Permission denied

**问题现象**: API 容器日志显示 `Permission denied: '/srv/.venv/'`

**原因**: Dockerfile 中 `USER app` 指令导致 `uv` 无法写入 `/srv/.venv/`

**解决方案**:
1. 在 `USER app` 之前添加 `chown -R app:app /srv`
2. 设置 `ENV UV_CACHE_DIR=/home/app/.cache/uv`
3. 重新构建镜像: `docker compose build api`

**相关文档**: `CLAUDE.md` § Deployment Pitfalls
```

### 7. 社区贡献机制

**借鉴点**: awesome-openclaw-tutorial 是社区驱动的项目，持续接受贡献和反馈。

**应用场景**:
- ClawButler 作为开源项目，需要建立社区贡献机制
- 鼓励用户贡献文档、案例、插件、Bug 修复
- 建立贡献者激励机制（如贡献者墙、徽章、优先支持）

**具体设计**:
- 创建 `CONTRIBUTING.md`，说明如何贡献代码、文档、案例
- 创建 `docs/community/`，展示社区贡献的案例、插件、最佳实践
- 建立 GitHub Discussions，鼓励用户提问、分享经验
- 定期举办线上/线下活动（如 Meetup、Hackathon），增强社区凝聚力

### 8. 多语言支持

**借鉴点**: awesome-openclaw-tutorial 是中文教程，填补了 OpenClaw 中文资料的空白。

**应用场景**:
- ClawButler 目标用户包括中文和英文用户
- 当前文档主要为英文，需要提供中文版本
- Web UI 已支持 i18n（zh-CN / en-US），文档也应支持多语言

**具体设计**:
```
docs/
├── en/                              # 英文文档
│   ├── 01-getting-started/
│   ├── 02-core-features/
│   └── ...
├── zh-CN/                           # 中文文档
│   ├── 01-getting-started/
│   ├── 02-core-features/
│   └── ...
└── README.md                        # 多语言导航
```

- 使用 i18n 工具（如 `i18next`）管理翻译
- 在 Web UI 中添加语言切换功能
- 提供社区翻译贡献机制

## 总结

awesome-openclaw-tutorial 是一个优秀的社区驱动文档项目，为 ClawButler 提供了以下借鉴价值：

1. **系统化文档体系**: 渐进式学习路径、场景驱动、版本感知
2. **版本升级指南**: Breaking Changes 迁移、快速修复、自动化脚本
3. **配置文件参考**: 完整的字段说明、类型、默认值、示例、注意事项
4. **实战案例库**: 70+ 端到端案例，覆盖不同行业和场景
5. **搜索功能**: 全文搜索、语义搜索、AI 搜索
6. **避坑指南**: 常见问题、重要提示、健康检查工具
7. **社区贡献机制**: 开放贡献、激励机制、社区活动
8. **多语言支持**: 中英文文档、i18n 工具、社区翻译

ClawButler 可以参考 awesome-openclaw-tutorial 的文档结构和内容组织方式，建立完善的文档体系，降低用户学习成本，提升产品易用性。
