# OpenClaw 官方组织小型项目合集

本文档汇总了 OpenClaw 官方组织下的 16 个小型项目，涵盖基础设施、社区治理、开发工具、自动化机器人等多个领域。这些项目虽然规模较小，但在 OpenClaw 生态系统中扮演着重要角色。

---

## nix-openclaw (519 stars)

### 问题与解决方案
OpenClaw 需要跨平台的声明式包管理和部署方案。传统的 Homebrew、npm 等工具存在版本漂移、环境不一致等问题。

nix-openclaw 提供了基于 Nix 的 OpenClaw 打包方案，实现了：
- 可复现的构建环境（pinned versions）
- 声明式配置（home-manager 集成）
- 自动保持最新（CI 自动更新）
- 插件系统集成（技能文档自动打包）

### 关键特性
- **多平台支持**：Darwin (aarch64) + Linux (x86_64/aarch64)
- **插件化架构**：每个工具作为独立的 openclawPlugin 导出
- **自动同步**：CI 每 30 分钟同步技能文档，每 10 分钟检查工具更新
- **零漂移部署**：通过 Nix flakes 锁定依赖版本
---

## openclaw.ai (222 stars)

### 问题与解决方案
OpenClaw 需要一个清晰、高效的官方门户，提供快速安装、功能展示和社区入口。

openclaw.ai 是基于 Astro 的静态站点，提供：
- 一键安装脚本（macOS/Linux/Windows）
- 集成展示页面（/integrations）
- 社区反馈页面（/shoutouts）

### 关键特性
- **多平台安装脚本**：
  - macOS/Linux: `curl -fsSL https://openclaw.ai/install.sh | bash`
  - Windows: `iwr -useb https://openclaw.ai/install.ps1 | iex`
- **智能 UI 检测**：自动检测终端类型，交互式终端使用 Gum UI，非交互式回退到纯文本
- **自动部署**：推送到 main 分支自动部署到 GitHub Pages
- **首次运行优化**：新安装自动运行 `openclaw onboard`，升级运行 `openclaw doctor --non-interactive`
---

## clawdinators (140 stars)

### 问题与解决方案
OpenClaw 需要 24/7 运行的 AI 维护者代理，用于监控 GitHub 仓库、响应 Discord 请求、自动处理 PR 和 Issue。传统的手动 SSH 部署存在配置漂移、难以复现、无法自动更新等问题。

clawdinators 提供了基于 NixOS 的镜像化部署方案：
- **镜像化部署**：每次部署都是全新的 AMI，无 SSH，无配置漂移
- **自动引导**：实例启动时从 S3 拉取加密的 secrets 和 repo seeds
- **自我更新**：systemd timer 定期运行 `flake lock --update-input` + `nixos-rebuild switch`
- **蜂巢记忆**：通过 EFS 共享状态，多实例协同工作

### 关键特性
- **双层架构**：
  - 通用层：NixOS-on-AWS 基础设施（AMI pipeline、OpenTofu、S3 bootstrap、agenix secrets）
  - 特定层：CLAWDINATOR 代理逻辑（Discord gateway、GitHub 监控、人格系统）
- **部署流程**：
  1. `nixos-generators` 构建 raw 镜像
  2. 上传到 S3
  3. AWS VM Import 创建 AMI
  4. OpenTofu 启动 EC2
  5. 实例自动下载 secrets 并运行 `nixos-rebuild switch`
- **安全设计**：
  - 使用 agenix 加密 secrets（Discord token、Anthropic API key、GitHub App 私钥）
  - 默认禁用 SSH
  - 仅绑定到 Tailscale 网络
---

## community (73 stars)

### 问题与解决方案
OpenClaw Discord 服务器需要透明、可追溯的社区治理文档，同时需要明确的团队分工和职责边界。

community 仓库提供了：
- 公开的社区政策文档（Mod Onboarding、Moderation Guide、Rules、Roles Reference、Incident Playbook）
- 四个专业团队的层级结构和职责划分
- 透明的申请流程

### 关键特性
- **四团队架构**：
  - Discord Moderator（文字频道）
  - VC Moderator（语音频道）
  - Helper（技术支持）
  - Configurator（服务器配置）
- **人工关卡设计**：团队之间有明确的职责边界，跨团队协作需要 Lead 协调
- **透明度优先**：所有政策文档开源，变更通过 GitHub Issue 讨论（Rules 除外，需在 Discord #announcements 公告）
- **申请流程**：通过邮件申请，需提供经验、推荐人、时区和可用时间
---

## clawgo (56 stars)

### 问题与解决方案
OpenClaw 需要在资源受限的设备（如树莓派）上运行轻量级节点客户端，连接到 gateway bridge，处理语音转录和聊天响应。

clawgo 是用 Go 编写的最小化无头节点客户端，提供：
- 低资源占用（适合树莓派）
- 语音转录流处理（stdin/FIFO）
- 本地 TTS 支持（espeak-ng、Piper、ElevenLabs）
- mDNS 服务发现

### 关键特性
- **跨平台编译**：`GOOS=linux GOARCH=arm64 go build`
- **灵活的输入源**：支持 stdin、FIFO、文件
- **多 TTS 引擎**：system (espeak-ng)、piper、elevenlabs、none
- **配对机制**：通过 `clawgo pair` 注册节点，需在 gateway 上批准
- **systemd 集成**：提供 systemd service 示例
---

## homebrew-tap (32 stars)

### 问题与解决方案
OpenClaw 需要通过 Homebrew 分发 CLI 工具和 macOS 应用，但不希望提交到官方 homebrew-core（审核慢、维护成本高）。

homebrew-tap 提供了自定义 Homebrew tap，支持：
- Formulae（CLI 工具）
- Casks（macOS 应用）
- 快速迭代和发布

### 关键特性
- **安装方式**：`brew tap clawdbot/tap && brew install clawdbot/tap/<name>`
- **Cask 卸载增强**：支持 `--zap` 选项清理用户数据
- **独立维护**：不依赖 homebrew-core 的审核流程
---

## hermit (26 stars)

### 问题与解决方案
OpenClaw Discord 服务器需要一个轻量级机器人，处理 GitHub 查询和 AutoMod 关键词响应。

hermit 是基于 Carbon 框架的 Discord 机器人，提供：
- `/github` 命令查询 Issue 和 PR
- AutoMod 关键词触发自动回复
- 可配置的消息模板

### 关键特性
- **Carbon 框架**：使用 Bun 运行时，快速启动
- **Gateway 事件监听**：监听 AutoModeration Action Execution 事件
- **可配置响应**：通过 `src/config/automod-messages.json` 映射关键词到消息模板
- **用户提及**：支持 `{user}` 占位符
---

## caclawphony (6 stars)

### 问题与解决方案
OpenClaw 主仓库的 PR 量巨大，需要自动化的 PR 分类、审查和合并流水线，同时保留人工审批关卡。

caclawphony 基于 Symphony 框架，将 Linear 项目看板转化为 AI 代理调度系统：
- **多阶段流水线**：Triage → Review → Prepare → Merge
- **人工关卡**：每个阶段之间需要维护者审批
- **集群检测**：自动识别重复 PR 和相关 Issue
- **GitHub 状态同步**：检查 `gh pr reviews` 确定是否已请求变更

### 关键特性
- **状态机设计**：
  - Agent 状态：Triage、Review、Prepare、Merge、Request Changes、Closure
  - Human gate 状态：Todo、Review Complete、Prepare Complete
  - Terminal 状态：Done、Duplicate
- **Symphony 集成**：
  - `after_create` hook：工作区设置、技能复制、仓库克隆
  - `before_run` hook：分支切换
  - Jinja 模板：每个状态的提示词模板
- **资源约束**：Prepare 状态最多 1 个并发（避免冲突）
- **重复检测**：运行 `pr-plan --live` 刷新缓存，然后 `pr-cluster` 进行多信号搜索
---

## trust (29 stars)

### 问题与解决方案
OpenClaw 需要公开透明的威胁模型和安全计划，建立用户信任。

trust 仓库基于 MITRE ATLAS 框架，提供：
- 结构化的威胁模型（threats.yaml）
- 攻击链和信任边界文档
- 公开的漏洞报告流程

### 关键特性
- **MITRE ATLAS 框架**：专门针对 AI/ML 系统的威胁建模
- **渲染站点**：https://trust.openclaw.ai/trust/threatmodel
- **贡献指南**：CONTRIBUTING.md 说明如何提交威胁和攻击链
---

## casa (29 stars)

### 问题与解决方案
HomeKit 数据被锁在苹果生态内，自动化和 AI Agent 无法直接访问。

casa 是 Mac Catalyst 应用，提供：
- 本地 REST API（仅 localhost）
- HomeKit 数据读写
- 内置 CLI 工具

### 关键特性
- **本地优先**：仅绑定到 127.0.0.1，无远程访问
- **可选 HomeKit**：默认关闭，需用户手动启用
- **CLI 集成**：`casa devices`、`casa characteristics set <uuid> true`
- **Sparkle 自动更新**：使用 EdDSA 签名
---

## maintainers (28 stars)

### 问题与解决方案
新维护者加入 OpenClaw 团队后，需要快速了解工作流程、安全规范和最佳实践。

maintainers 仓库提供了：
- 新维护者生存指南
- PR 工作流程（Review → Prepare → Merge）
- 安全加固清单
- 常用命令和资源链接

### 关键特性
- **安全优先**：
  - 启用 2FA（authenticator app，禁用 SMS）
  - GPG 签名提交
  - YubiKey/FIDO2 硬件密钥
  - 密码管理器
  - 警惕钓鱼和社会工程学攻击
- **PR 工作流**：
  - 从 `size:xs` 开始
  - 使用 `/reviewpr` 进行 AI 审查
  - 运行 gates：`pnpm lint && pnpm build && pnpm test`
  - 更新 CHANGELOG.md
  - 使用 `/landpr` 或 `/mergepr` 合并
- **集群思维**：不要单独处理 PR，使用 Codex 搜索相关 PR 和 Issue，一次性解决整个集群
- **Do's and Don'ts**：
  - 禁止：`@ts-nocheck`、禁用 lint 规则、使用 bun、跳过测试
  - 必须：rebase before merge、感谢贡献者、重大变更前在 `#maintainers` 公告
---

## nix-steipete-tools (28 stars)

### 问题与解决方案
OpenClaw 需要集成一系列第三方工具（截图、TTS、消息发送等），但这些工具的安装和版本管理复杂。

nix-steipete-tools 将 Peter Steinberger 的工具打包为 Nix flakes，并附带 OpenClaw 插件元数据：
- 可复现的构建
- 声明式安装
- 自动保持最新
- 技能文档集成

### 关键特性
- **10 个工具**：
  - summarize（链接 → 摘要）
  - gogcli（Google CLI）
  - goplaces（Google Places API）
  - camsnap（RTSP/ONVIF 摄像头截图）
  - sonoscli（Sonos 控制）
  - bird（X/Twitter CLI）
  - peekaboo（macOS 截图 + AI 视觉分析）
  - poltergeist（文件监控 + 自动重建）
  - sag（ElevenLabs TTS）
  - imsg（iMessage/SMS CLI）
- **双模式使用**：
  - 作为 openclawPlugin（包含技能文档）
  - 作为纯 Nix package（仅二进制）
- **自动同步**：
  - 技能文档从 openclaw/openclaw main 分支同步（每 30 分钟）
  - 工具版本从 GitHub releases 更新（每 10 分钟）
---

## butter.bot (9 stars)

### 问题与解决方案
（无 README，项目用途未知）

根据项目名称推测，可能是一个简单的 Discord 机器人或自动化工具。
---

## flawd-bot (31 stars)

### 问题与解决方案
（无 README，项目用途未知）

根据项目名称"evil twin bot"推测，可能是用于测试或演示的对抗性机器人。
---

## .github (6 stars)

### 问题与解决方案
GitHub 组织需要统一的 README、贡献指南和 Issue/PR 模板。

.github 仓库提供了：
- 组织级别的 README（显示在 https://github.com/openclaw）
- 默认的 CONTRIBUTING.md
- Issue 和 PR 模板

### 关键特性
- **组织级别配置**：所有仓库继承这些默认文件
- **统一品牌**：确保所有仓库的贡献流程一致
---

## voice-community (4 stars)

### 问题与解决方案
（无 README，项目用途未知）

根据项目名称推测，可能与 OpenClaw 的语音社区功能相关。
---

## 总结

OpenClaw 的小型项目展现了以下设计理念：

1. **声明式优先**：nix-openclaw、clawdinators 都强调配置即代码、可复现部署
2. **自动化驱动**：CI 自动更新、自我更新系统、自动化 PR 流水线
3. **透明治理**：community、trust 仓库公开所有政策和威胁模型
4. **人工关卡**：caclawphony 的多阶段流水线在自动化和人工审批之间取得平衡
5. **工具生态**：nix-steipete-tools、casa、hermit 等工具丰富了 OpenClaw 的能力边界

对 ClawButler 的核心启示：
- **配置安全 V2** 可以借鉴 clawdinators 的镜像化部署和 caclawphony 的人工关卡
- **Verified Templates V2.5** 可以参考 nix-steipete-tools 的打包标准和自动更新机制
- **Runbook 自动化** 可以引入 caclawphony 的状态机流水线和 Symphony 框架
- **联邦架构** 可以借鉴 clawgo 的节点配对机制和 clawdinators 的蜂巢记忆模式
- **安全治理** 可以参考 trust 的威胁建模和 maintainers 的安全加固清单
