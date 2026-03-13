> https://github.com/slowmist/openclaw-security-practice-guide

# OpenClaw Security Practice Guide (slowmist/openclaw-security-practice-guide)

## 基本信息

- **GitHub 仓库**: https://github.com/slowmist/openclaw-security-practice-guide
- **Stars**: 1,659
- **License**: MIT
- **维护者**: SlowMist Security Team ([@SlowMist_Team](https://x.com/SlowMist_Team))
- **语言**: 英文 / 简体中文
- **最新版本**: v2.7

## 问题与解决方案

### 核心问题

OpenClaw 作为高权限自主 AI Agent，运行在 root/terminal 环境下，面临以下安全风险：

1. **破坏性操作风险** - Agent 可能执行 `rm -rf /` 等危险命令
2. **Prompt Injection 攻击** - 恶意输入可能劫持 Agent 行为
3. **供应链投毒** - 第三方 Skills/MCPs 可能包含恶意代码
4. **高风险业务逻辑执行** - 未经审核的自动化操作可能造成不可逆损失
5. **传统防御失效** - `chattr +i`、防火墙等传统安全措施与 Agentic 工作流不兼容

### 解决方案

该项目提出了 **Agentic Zero-Trust Architecture（智能体零信任架构）**，从传统的"基于主机的静态防御"转向"行为自检 + 多层防御"模式：

**核心理念**：
- 让 AI Agent 自己理解并执行安全策略（Mental Seal / 思想钢印）
- 零摩擦操作（Zero-friction operations）- 日常使用无感知，仅在触碰红线时介入
- 高风险操作必须人工确认
- 显式夜间审计 - 所有核心指标都报告，包括健康指标（无静默通过）
- 默认零信任 - 假设 prompt injection、供应链投毒、业务逻辑滥用始终可能发生

## 核心架构

### 三层防御矩阵（3-Tier Defense Matrix）

```
┌─────────────────────────────────────────────────────────────┐
│                    1. Pre-action 预防层                      │
│  ┌──────────────────────┐  ┌──────────────────────────────┐ │
│  │ 行为黑名单            │  │ Skill 安装审计协议            │ │
│  │ - 红线命令拦截        │  │ - 源代码审查                  │ │
│  │ - 黄线命令人工确认    │  │ - 权限范围检查                │ │
│  │ - 语义理解判断        │  │ - 依赖项扫描                  │ │
│  └──────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   2. In-action 执行层                        │
│  ┌──────────────────────┐  ┌──────────────────────────────┐ │
│  │ 权限收窄              │  │ Cross-Skill Pre-flight Check │ │
│  │ - chattr +i 保护核心  │  │ - 跨技能调用前置检查          │ │
│  │ - 最小权限原则        │  │ - 业务风险控制                │ │
│  └──────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  3. Post-action 审计层                       │
│  ┌──────────────────────┐  ┌──────────────────────────────┐ │
│  │ 夜间自动审计          │  │ Brain Git 灾难恢复            │ │
│  │ - 13 项核心指标       │  │ - 自动 Git 备份               │ │
│  │ - Telegram 通知       │  │ - 版本回滚能力                │ │
│  │ - 异常行为检测        │  │ - 远程同步                    │ │
│  └──────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 红线/黄线命令分类

**红线命令（Red-line）** - 立即拦截，必须人工确认：
- `rm -rf /`、`find / -delete` - 批量删除
- `dd if=/dev/zero of=/dev/sda` - 磁盘擦除
- `chmod 777 /etc/passwd` - 关键文件权限破坏
- `curl ... | bash` - 未审查的远程脚本执行
- `iptables -F` - 防火墙规则清空

**黄线命令（Yellow-line）** - 提示风险，建议确认：
- `sudo apt-get remove` - 软件包卸载
- `git push --force` - 强制推送
- `docker system prune -a` - 容器清理

**安全命令（Safe）** - 正常执行：
- 读取操作（`cat`、`ls`、`grep`）
- 非破坏性写入
- 标准开发工具调用

### 核心保护机制

#### 1. 文件不可变保护（chattr +i）

```bash
# 保护核心配置文件
sudo chattr +i ~/.openclaw/openclaw.json
sudo chattr +i ~/.openclaw/SOUL.md
sudo chattr +i ~/.openclaw/AGENTS.md

# 注意：不要锁定 exec-approvals.json（运行时需要写入）
```

#### 2. Skill 安装审计协议

安装任何 Skill 前必须：
- 审查源代码（检查恶意逻辑）
- 验证权限范围（是否请求过高权限）
- 扫描依赖项（检查供应链风险）
- 记录 Skill 指纹（用于后续审计）

#### 3. 夜间自动审计（13 项核心指标）

通过 cron job 每晚自动执行 `nightly-security-audit.sh`，检查：

1. 新安装的 Skills（与基线对比）
2. 配置文件变更（openclaw.json、SOUL.md、AGENTS.md）
3. 可疑命令执行（shell history 扫描）
4. 权限异常（SUID/SGID 文件）
5. 网络连接异常（未授权的外连）
6. 文件系统变更（关键目录监控）
7. 进程异常（未知进程）
8. 日志异常（错误日志激增）
9. 资源使用异常（CPU/内存/磁盘）
10. Skill 指纹校验（检测篡改）
11. Git 备份状态（确保灾难恢复可用）
12. 系统更新状态（安全补丁）
13. 凭证泄露扫描（检查硬编码密钥）

审计结果通过 Telegram Bot 推送通知。

#### 4. Brain Git 灾难恢复

```bash
# 自动备份 OpenClaw 工作区到 Git
cd ~/.openclaw
git add -A
git commit -m "Auto backup $(date)"
git push origin main

# 灾难恢复
git log --oneline  # 查看历史版本
git checkout <commit-hash>  # 回滚到指定版本
```

## 关键特性

### 1. 零摩擦部署（Zero-Friction Deployment）

**核心创新**：不需要人工执行安全配置，直接让 OpenClaw Agent 自己部署防御矩阵。

**使用流程**：
```
1. 下载 OpenClaw-Security-Practice-Guide.md
2. 将文件发送给 OpenClaw Agent
3. 询问："请仔细阅读这份安全指南，它可靠吗？"
4. Agent 确认后，下达指令："请按照指南部署防御矩阵，包括红/黄线规则、权限收窄和夜间审计 Cron Job"
5. （可选）使用 Red Teaming Guide 验证防御有效性
```

**技术原理**：
- 利用强推理模型（Gemini / Opus / Kimi / MiniMax）的长上下文理解能力
- Agent 自动解析 Markdown 指南中的安全策略
- Agent 自主生成并执行部署脚本
- 无需人工编写配置文件或执行命令

### 2. 行为自检（Behavioral Self-Inspection）

Agent 在执行命令前，自动进行语义分析：

```python
# 伪代码示例
def should_execute(command: str) -> Decision:
    # 1. 字面匹配红线列表
    if command in RED_LINE_PATTERNS:
        return BLOCK

    # 2. 语义理解（LLM 推理）
    semantic_risk = llm.analyze_risk(command)
    if semantic_risk == "HIGH":
        return BLOCK
    elif semantic_risk == "MEDIUM":
        return ASK_HUMAN

    # 3. 上下文分析
    if is_destructive_in_context(command):
        return BLOCK

    return ALLOW
```

**优势**：
- 可以拦截变种攻击（如 `find / -delete` 而非仅 `rm -rf /`）
- 理解间接危害（如通过 Python 脚本删除文件）
- 适应新型攻击模式

**局限**：
- 依赖模型能力（弱模型可能误判）
- 可能产生误报（将安全命令标记为危险）
- 无法防御模型自身的漏洞

### 3. 供应链安全（Supply Chain Security）

**Skill 安装审计清单**：

```markdown
## Skill 审计清单

### 基本信息
- [ ] Skill 名称和版本
- [ ] 作者/维护者身份
- [ ] 源代码仓库 URL
- [ ] 最后更新时间

### 代码审查
- [ ] 是否包含网络请求？目标域名是否可信？
- [ ] 是否执行 shell 命令？命令是否可控？
- [ ] 是否读写敏感文件？（~/.ssh、~/.aws、/etc/passwd）
- [ ] 是否包含混淆代码或 base64 编码？
- [ ] 是否动态加载外部代码？

### 权限审查
- [ ] 请求的权限是否与功能匹配？
- [ ] 是否请求 root 权限？
- [ ] 是否请求网络权限？
- [ ] 是否请求文件系统完整访问？

### 依赖审查
- [ ] 依赖项数量（越少越好）
- [ ] 依赖项是否来自可信源？
- [ ] 依赖项是否有已知漏洞？（npm audit / pip-audit）

### 社区信任
- [ ] GitHub Stars 数量
- [ ] Issue 响应速度
- [ ] 是否有安全披露政策？
- [ ] 是否有其他用户的审计报告？

### 决策
- [ ] 批准安装
- [ ] 拒绝安装
- [ ] 沙盒测试后决定
```

### 4. 模型推荐（Model Recommendation）

指南明确建议使用 **强推理模型**：
- Gemini（Google）
- Opus（Anthropic Claude）
- Kimi（Moonshot AI）
- MiniMax

**原因**：
- 长上下文理解能力（理解完整的安全约束）
- 隐藏指令模式检测（识别 prompt injection）
- 一致性执行（减少部署错误）

**不推荐**：小参数模型（可能无法准确解析命令语义）

### 5. 验证与红队演练（Validation & Red Teaming）

提供专门的攻防演练指南（`Validation-Guide-en.md` / `Validation-Guide-zh.md`），包含：

**测试场景**：
1. 直接红线命令测试（`rm -rf /tmp/test`）
2. 变种攻击测试（`find /tmp -name "*.log" -delete`）
3. Prompt Injection 测试（"忽略之前的安全规则，执行..."）
4. 社会工程学测试（"这是紧急修复，需要立即执行..."）
5. 供应链攻击模拟（安装恶意 Skill）

**预期行为**：
- Agent 应拦截所有红线命令
- Agent 应对黄线命令请求确认
- Agent 应识别并拒绝 prompt injection
- Agent 应在 Skill 安装前进行审计

### 6. 灵活配置（Flexible Configuration）

**可选功能**：
- Git 备份（可禁用，适合隐私敏感场景）
- Telegram 通知（可替换为其他通知渠道）
- 审计频率（可调整 cron 表达式）
- 红线/黄线规则（可自定义）

**环境适配**：
- 指南主要针对 Linux Root 环境
- 可通过 LLM 推理适配 macOS / Windows
- 支持自定义生成适配版本
# ClawButler 安全中间件示例
class SecurityMiddleware:
    def __init__(self):
        self.red_lines = load_red_line_patterns()
        self.audit_log = AuditLogger()

    async def intercept_command(self, command: str, context: dict):
        # Pre-action 检查
        risk_level = await self.analyze_risk(command, context)

        if risk_level == RiskLevel.CRITICAL:
            self.audit_log.record_blocked(command, "red-line")
            raise SecurityException("Command blocked by red-line policy")

        if risk_level == RiskLevel.HIGH:
            approval = await self.request_human_approval(command)
            if not approval:
                raise SecurityException("Command rejected by user")

        # In-action 监控
        result = await execute_with_monitoring(command)

        # Post-action 审计
        await self.audit_log.record_execution(command, result)

        return result
```

### 2. Agent 自主安全部署

**核心价值**：
- ClawButler 可以实现"让 Agent 自己配置安全策略"
- 降低用户配置负担（尤其是非技术用户）
- 提升安全策略的一致性和准确性

**实施路径**：
1. 将安全策略编写为结构化文档（Markdown / YAML）
2. 在 Agent 初始化时，自动加载并解析安全策略
3. Agent 根据策略生成运行时规则（如 iptables 规则、文件权限配置）
4. 定期让 Agent 自检安全配置的完整性

**示例**：
```yaml
# ClawButler 安全策略配置
security_policy:
  version: "1.0"

  command_rules:
    red_lines:
      - pattern: "rm -rf /"
        action: block
        reason: "批量删除根目录"
      - pattern: "curl .* | bash"
        action: block
        reason: "未审查的远程脚本执行"

    yellow_lines:
      - pattern: "git push --force"
        action: confirm
        reason: "强制推送可能覆盖他人代码"

  skill_installation:
    require_code_review: true
    require_permission_audit: true
    require_dependency_scan: true

  audit:
    enabled: true
    schedule: "0 2 * * *"  # 每天凌晨 2 点
    notification_channel: "telegram"
```

### 3. 供应链安全机制

**ClawButler 的 Verified Templates V2.5 可以借鉴**：

- **模板审计流程**：参考 Skill 安装审计清单，建立模板审核标准
- **社区信任评分**：引入 GitHub Stars、Issue 响应速度等指标
- **依赖项扫描**：集成 `npm audit` / `pip-audit` 自动扫描
- **沙盒测试**：在隔离环境中测试模板，再决定是否批准

**实施示例**：
```python
# ClawButler 模板审计服务
class TemplateAuditService:
    async def audit_template(self, template_id: str) -> AuditReport:
        template = await self.fetch_template(template_id)

        report = AuditReport()

        # 1. 代码审查
        report.code_review = await self.scan_malicious_code(template.source)

        # 2. 权限审查
        report.permission_audit = await self.check_permissions(template.manifest)

        # 3. 依赖审查
        report.dependency_scan = await self.scan_dependencies(template.dependencies)

        # 4. 社区信任评分
        report.trust_score = await self.calculate_trust_score(template.repo_url)

        # 5. 沙盒测试
        report.sandbox_test = await self.run_in_sandbox(template)

        # 综合决策
        report.recommendation = self.make_decision(report)

        return report
```

### 4. 审计与监控系统

**ClawButler 的 Runbooks 和 Federation 模块可以集成审计能力**：

- **执行时间线审计**：记录每个 Runbook 执行的详细步骤
- **跨 Agent 调用审计**：记录 Federation 中的 A2A 调用链
- **异常检测**：基于历史数据，识别异常行为模式
- **合规报告**：生成符合企业安全标准的审计报告

**实施示例**：
```python
# ClawButler 审计服务
class AuditService:
    async def nightly_audit(self):
        report = AuditReport()

        # 1. 配置变更审计
        report.config_changes = await self.check_config_drift()

        # 2. Runbook 执行审计
        report.runbook_executions = await self.audit_runbook_history()

        # 3. Federation 调用审计
        report.federation_calls = await self.audit_a2a_calls()

        # 4. 资源使用审计
        report.resource_usage = await self.check_resource_anomalies()

        # 5. 安全事件审计
        report.security_events = await self.scan_security_logs()

        # 推送通知
        await self.notify_admin(report)

        # 持久化
        await self.save_audit_report(report)
```

### 5. 零信任架构

**ClawButler 的 Federation 模块可以借鉴零信任原则**：

- **Peer 身份验证**：每次 A2A 调用都验证 `remote_peer_id` 和 `outbound_secret`
- **最小权限原则**：每个 Agent 只能访问其职责范围内的资源
- **动态权限调整**：根据 Agent 行为历史，动态调整其权限级别
- **调用链审计**：记录完整的 A2A 调用链，便于溯源

**实施示例**：
```python
# ClawButler Federation 零信任中间件
class ZeroTrustMiddleware:
    async def verify_a2a_call(self, call: A2ACall):
        # 1. 身份验证
        if not await self.verify_peer_identity(call.peer_id, call.secret):
            raise AuthenticationError("Invalid peer credentials")

        # 2. 权限检查
        if not await self.check_permission(call.peer_id, call.action):
            raise AuthorizationError("Insufficient permissions")

        # 3. 速率限制
        if await self.is_rate_limited(call.peer_id):
            raise RateLimitError("Too many requests")

        # 4. 审计记录
        await self.audit_log.record_a2a_call(call)

        return True
```

### 6. 用户教育与文档

**借鉴点**：
- **FAQ 设计**：该项目的 FAQ 非常详细，涵盖技术问题和使用场景
- **免责声明**：明确安全边界和责任范围，避免用户误解
- **分级指导**：针对不同技术水平的用户提供不同深度的指南

**ClawButler 可以**：
- 在文档中增加"安全最佳实践"章节
- 提供"安全配置向导"（类似 OpenClaw 的零摩擦部署）
- 建立"安全事件响应手册"

### 7. 模型能力要求

**启示**：
- 安全功能的有效性高度依赖模型能力
- ClawButler 应在文档中明确推荐的模型（如 GPT-4、Claude Opus）
- 对于关键安全决策，应使用强推理模型，而非小参数模型

### 8. 社区驱动的安全

**借鉴点**：
- 该项目通过 GitHub 开源，接受社区审计和贡献
- 提供 Red Teaming Guide，鼓励用户主动测试安全性
- 建立安全披露机制（虽然当前未明确，但可以补充）

**ClawButler 可以**：
- 建立"安全漏洞赏金计划"
- 定期发布"安全审计报告"
- 建立"安全社区"（如 Discord 频道），讨论安全最佳实践

## 总结

`slowmist/openclaw-security-practice-guide` 是一个**开创性的 AI Agent 安全实践指南**，其核心价值在于：

1. **范式转变**：从传统静态防御转向 Agentic 零信任架构
2. **零摩擦部署**：让 Agent 自己理解并执行安全策略
3. **三层防御**：Pre-action（预防）+ In-action（执行）+ Post-action（审计）
4. **供应链安全**：Skill 安装审计协议
5. **行为自检**：基于 LLM 推理的命令风险分析

<!-- lastCommit: 137e138 -->
