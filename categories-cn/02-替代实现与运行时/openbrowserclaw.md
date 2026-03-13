> https://github.com/sachaa/openbrowserclaw

# openbrowserclaw (558 stars)

## 问题与解决方案

传统 AI 助手需要服务器基础设施（数据库、文件系统、后台进程），增加部署成本和隐私风险。openbrowserclaw 将整个 Agent 运行时搬进浏览器标签页，利用 IndexedDB/OPFS/Web Worker/WebAssembly 实现零基础设施的个人 AI 助手，数据完全本地化。

## 关键特性

- **纯浏览器架构** — IndexedDB（消息/任务/配置）+ OPFS（文件存储）+ Web Worker（Agent 循环）+ WebVM（v86 Alpine Linux 沙箱）
- **零服务器依赖** — 所有状态和计算在客户端，API 密钥 AES-256-GCM 加密存储
- **内置工具链** — `bash`（WebVM 沙箱）、`javascript`（隔离作用域）、`read_file`/`write_file`、`fetch_url`、`update_memory`、`create_task`
- **多渠道支持** — 浏览器内聊天 + Telegram Bot API（纯 HTTPS，无 WebSocket）
- **PWA 离线能力** — Service Worker 缓存，标签页关闭后任务队列保留
- **Cron 调度器** — 浏览器内 cron 表达式解析和任务触发

<!-- lastCommit: 6a7050b -->
