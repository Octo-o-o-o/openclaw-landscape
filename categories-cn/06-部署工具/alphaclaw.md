> https://github.com/chrysb/alphaclaw

# AlphaClaw (482 stars)

## 问题与解决方案

OpenClaw 部署和运维存在配置复杂、崩溃恢复手动、可观测性不足的问题。AlphaClaw 提供浏览器配置向导、自愈 Watchdog、Git 回滚、全栈可观测性，将首次部署到首条消息的时间缩短至 5 分钟以内，支持 Railway/Render 一键部署。

## 关键特性

- **Setup UI** — 密码保护的 Web 仪表板，覆盖 Onboarding、配置管理、日常运维，无需 SSH 和 CLI
- **Gateway Manager** — 作为父进程管理 OpenClaw Gateway 的启动、监控、重启和代理
- **Watchdog** — 崩溃检测、崩溃循环恢复、自动修复（`openclaw doctor --fix`）、Telegram/Discord 通知
- **Channel Orchestration** — Telegram/Discord 机器人配对、凭证同步、Telegram 多线程 Topic 分组向导
- **Prompt Hardening** — 内置反漂移引导提示词（`AGENTS.md`、`TOOLS.md`），强制执行安全实践、提交纪律、变更摘要
- **Git Sync** — 每小时自动提交 OpenClaw workspace 到 GitHub，可配置 cron 调度，结合 Prompt Hardening 实现版本控制和审计
- **File Explorer** — 浏览器文件浏览器，支持文件可见性、内联编辑、diff 视图、Git 感知同步
- **Google Workspace OAuth** — Gmail/Calendar/Drive/Docs/Sheets/Tasks/Contacts/Meet 集成，Gmail watch + Google Pub/Sub 推送端点处理

<!-- lastCommit: 82223b3 -->
