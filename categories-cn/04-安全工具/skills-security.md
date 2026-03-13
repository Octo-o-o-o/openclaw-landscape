> https://github.com/UseAI-pro/skills-security

# UseAI-pro/openclaw-skills-security (25 stars)

## 问题与解决方案

OpenClaw 生态的技能安装缺乏安全审查机制，恶意技能可能窃取凭证、植入后门或执行供应链攻击（如 ClawHavoc 事件）。该项目提供两个审计技能（skill-auditor 审查技能、setup-auditor 审查环境）和 11 个可复用安全模块，覆盖 12 种真实攻击类型的检测。

## 关键特性

- **双审计器架构** — skill-auditor 执行 6 步协议（元数据/typosquat 检查 → 权限分析 → 依赖审计 → prompt injection 扫描 → 网络/数据泄露分析 → 内容红旗），setup-auditor 执行 4 步协议（凭证扫描 → 配置加固 → 沙箱就绪 → 持久化检查）
- **威胁覆盖完整** — 覆盖 12/12 种真实攻击类型（typosquatting、凭证窃取、加密矿工、反向 shell、prompt injection、技能加载器漏洞、混淆命令、供应链攻击、社会工程、持久化、过度权限、数据泄露）
- **风险评级系统** — 输出 SAFE / SUSPICIOUS / DANGEROUS / BLOCK 四级判定，附带具体发现和修复建议
- **零依赖设计** — 纯 Markdown 指令模块（SKILL.md），可粘贴到任何 LLM（Codex CLI / Claude Code / OpenClaw）或浏览器工具（UseClawPro Verifier）
- **向导式环境审计** — setup-auditor 通过 5 个问题（workspace 路径、host agent、权限、沙箱、端口）收集信息，生成定制化修复清单
- **社区驱动** — 由 UseClawPro（UseAI.pro）维护，提供在线验证工具和已验证技能目录

<!-- lastCommit: 6a7050b -->
