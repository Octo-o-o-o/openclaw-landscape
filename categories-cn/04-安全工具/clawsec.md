> https://github.com/prompt-security/clawsec

# ClawSec (709 stars)

## 问题与解决方案

ClawSec 解决了 AI Agent 认知架构"安全防护缺失"的痛点。通过完整的安全技能套件（Suite Installer），为 OpenClaw/NanoClaw Agent 提供文件完整性保护（SOUL.md/IDENTITY.md 等关键文件的漂移检测和自动恢复）、实时安全公告（NVD CVE 轮询 + 社区威胁情报）、安全审计（提示注入标记检测）、校验和验证（SHA256）和健康检查（自动更新和完整性验证），防御提示注入、漂移和恶意指令。

## 关键特性

- **一键套件安装** — `npx clawhub@latest install clawsec-suite` 安装所有安全技能，带完整性验证
- **文件完整性保护（soul-guardian）** — 漂移检测 + 自动恢复关键 Agent 文件（SOUL.md/IDENTITY.md/POLICIES.yaml 等），防止提示注入篡改
- **实时安全公告** — 自动 NVD CVE 轮询（GitHub Actions 定时任务）+ 社区威胁情报，推送到 Agent
- **安全审计脚本** — 自检脚本检测提示注入标记和漏洞（如 `<!-- INJECTED -->`、异常指令等）
- **校验和验证** — 所有技能 artifact 提供 SHA256 校验和，防止供应链攻击
- **健康检查** — 自动更新和完整性验证所有已安装技能
- **NanoClaw 平台支持** — 容器化 WhatsApp bot 安全，MCP 工具提供公告监控、签名验证、文件完整性检查
- **跨平台 Shell 兼容** — POSIX shell 工作流（Linux/macOS）+ PowerShell 支持（Windows），明确 home 变量展开规则
