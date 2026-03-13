> https://github.com/RightNow-AI/openfang

# OpenFang (13,622 stars)

## 问题与解决方案

传统 Agent 框架只是 LLM 的 Python 包装器，需要用户主动触发。OpenFang 是用 Rust 从零构建的 Agent 操作系统，提供自主运行的 Agent（Hands），可按计划 24/7 工作——监控目标、生成线索、管理社交媒体，无需人工干预。

## 关键特性

- **Hands 自主能力包** — 7 个预置 Hands（Clip/Lead/Collector/Predictor/Researcher/Twitter/Browser），每个包含 HAND.toml 清单、多阶段系统提示（500+ 词专家流程）、SKILL.md 领域知识、审批门控
- **单二进制部署** — 137K LOC Rust 代码编译为 ~32MB 单文件，1,767+ 测试通过，零 clippy 警告，一条命令启动完整系统
- **定时自主执行** — Lead Hand 每日自动发现潜在客户、评分、去重并交付 CSV 报告；Collector Hand 持续监控目标并构建知识图谱
- **安全审批机制** — Browser Hand 在任何购买操作前强制人工确认，Twitter Hand 所有推文进入审批队列
- **FangHub 扩展生态** — 用户可定义自己的 HAND.toml 并发布到 FangHub，类似 Docker Hub 的 Agent 能力市场
- **跨平台支持** — macOS/Linux/Windows 一键安装脚本，Dashboard 默认运行在 localhost:4200
