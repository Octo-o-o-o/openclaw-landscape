> https://github.com/tsconfigdotjson/lobsterd

# lobsterd (25 stars)

## 问题与解决方案
多租户 OpenClaw 部署缺乏强隔离，共享主机存在安全风险和资源竞争。lobsterd 通过 Firecracker MicroVM 为每个租户提供轻量级虚拟机，实现网络隔离、per-tenant overlay 文件系统和独立 OpenClaw Gateway。

## 关键特性
- **Firecracker MicroVM 编排** — 每个租户运行在独立的轻量级 VM 中，支持 suspend/resume（零 RAM 占用）
- **Per-tenant Overlay 文件系统** — 基于 Alpine rootfs 的 overlay 镜像，租户数据完全隔离
- **网络隔离** — 每个 VM 独立网络栈，通过 Caddy 反向代理统一访问
- **完整 CLI 工具链** — `spawn`（创建租户）、`exec`（SSH 进入）、`configure`（打开 OpenClaw TUI）、`devices`（列出配对设备）、`evict`（删除租户）、`molt`（健康检查和修复）
- **Watchdog 守护进程** — systemd 服务自动监控租户健康状态，支持自动重启和快照
- **REST API** — `buoy` 命令启动 HTTP 服务器，镜像 CLI 功能，支持 Bearer token 认证
- **Tailscale 集成** — 默认通过 Tailscale Serve 提供远程访问（端口 8443）

<!-- lastCommit: 033c6df -->
