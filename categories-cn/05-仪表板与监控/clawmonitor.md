> https://github.com/openclawq/clawmonitor

# ClawMonitor

> openclawq/clawmonitor · ⭐ 32 · Python · MIT
> 调研时间：2026-03-13

## 概述

ClawMonitor 是一个轻量级的 OpenClaw Agent 会话实时监控工具。提供 TUI（终端用户界面）和 CLI 两种交互方式，可以追踪多个 Agent 会话的状态、消息交换和执行进度。

## 核心功能

| 功能 | 说明 |
|------|------|
| 会话状态追踪 | 实时显示每个 session 的状态（WORKING / FINISHED / INTERRUPTED / NO_MESSAGE） |
| TUI 交互界面 | 全屏终端界面，支持颜色编码（OK=绿 / RUN=青 / IDLE=黄 / ALERT=红） |
| 离线监控 | 通过 `*.jsonl.lock` 文件在 Gateway 不可用时仍可工作 |
| Nudge 功能 | 通过 `chat.send` 主动催促 Agent 汇报进度 |
| Snapshot 导出 | 导出当前所有会话状态快照 |
| Report 生成 | 生成会话报告 |
| 日志集成 | 可选的 Gateway 日志 tail，支持飞书/Telegram 特殊规则 |

## 技术栈

- **语言**：Python
- **界面**：TUI（终端用户界面）
- **配置**：TOML（`~/.config/clawmonitor/config.toml`）
- **日志**：JSONL（`~/.local/state/clawmonitor/events.jsonl`）
- **分发**：PyPI（`pip install clawmonitor`）

## CLI 命令

```bash
clawmonitor init       # 初始化配置
clawmonitor tui        # 启动交互式监控
clawmonitor status     # 显示会话状态
clawmonitor snapshot   # 导出当前状态
clawmonitor nudge      # 发送进度催促请求
clawmonitor report     # 生成会话报告
```

## 架构亮点

1. **安全意识**：自动脱敏 token，不 dump 敏感配置
2. **XDG 规范**：遵循 XDG 目录规范（config / state / cache 分离）
3. **离线降级**：Gateway 断连时通过 lock 文件维持基本监控
4. **ClawHub 集成**：提供 `skills/claw-monitor/` 目录，可作为 OpenClaw skill 使用
5. **IM 感知**：检测 Telegram 线程绑定路由（`BOUND_OTHER` 标记）

<!-- lastCommit: 6a7050b -->
