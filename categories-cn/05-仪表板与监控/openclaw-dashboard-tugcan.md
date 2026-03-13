> https://github.com/tugcantopaloglu/dashboard

# tugcantopaloglu/openclaw-dashboard (418 stars)

> 调研时间：2026-03-13（更新）
> 定位：带认证和 TOTP MFA 的实时 Agent 监控仪表板，强调安全加固

## 问题与解决方案

OpenClaw Agent 运维信息散落在日志和 CLI 中，且缺乏安全的远程访问方案。本项目提供零 npm 依赖的 Node.js 仪表板，强调安全加固（TOTP MFA、CSP、审计日志、速率限制），支持通过 Tailscale 安全远程访问。

## 关键特性

### 监控与分析
- **实时会话管理** — 活跃会话状态追踪，按 status/model/date 搜索过滤
- **API 速率限制追踪** — Claude 和 Gemini API 的速率限制可视化
- **成本分析** — 按模型/会话的费用拆解
- **活动热力图** — 30 天活动可视化 + 每日连续活跃天数（streak）追踪
- **系统健康** — CPU、RAM、磁盘、温度 + 24 小时 sparkline 迷你图

### Agent 管理
- **Memory 浏览器** — 浏览 MEMORY.md、HEARTBEAT.md、daily notes
- **Cron 管理** — 查看/启用/禁用/手动触发 cron job
- **服务控制** — 重启 OpenClaw、Dashboard 及其他服务
- **Git 活动** — 跨仓库 Git 活动追踪
- **Config 编辑器** — JSON 校验 + 自动备份

### 系统集成
- **Tailscale** — 状态和 peer 监控
- **Docker** — 容器/镜像管理，资源清理
- **安全面板** — UFW 规则、开放端口、fail2ban 监控
- **系统日志** — 自动刷新日志查看器

## 安全架构（核心亮点）

| 安全特性 | 实现细节 |
|---------|---------|
| 密码存储 | PBKDF2 + 100,000 次 SHA-512 迭代 |
| MFA | TOTP (Google Authenticator / Authy 兼容)，±1 窗口容忍 |
| 暴力破解防护 | 5 次失败 → 15 分钟软锁定，20 次 → 硬锁定 |
| 密码比较 | 时序安全（timing-safe comparison），防时序攻击 |
| HTTPS 策略 | 仅 localhost (127.0.0.1) 和 Tailscale (100.64.0.0/10) 免 HTTPS |
| 安全头 | HSTS, CSP (no inline scripts), X-Frame-Options: DENY, X-Content-Type-Options: nosniff |
| CORS | 同源策略，禁止通配符 |
| 审计日志 | 所有认证和破坏性操作记录到 `data/audit.log` |
| 文件保护 | 路径遍历防护 + 1MB 负载限制 |
| 自动备份 | 覆写前自动创建 `.bak` 文件 |
| 密码恢复 | 环境变量 recovery token 机制 |

## UX 亮点

- **键盘快捷键** — 1-7 切换面板，Space 刷新，/ 搜索，Esc 关闭，? 帮助
- **浏览器通知** — 使用量接近限制时推送浏览器原生通知
- **Remember Me** — 3 小时持久登录 vs 会话级登录
- **响应式设计** — 桌面 + 平板 + 手机

<!-- lastCommit: 6a7050b -->
