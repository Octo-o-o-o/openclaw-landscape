# Deployment Tools

> Docker, Helm, installers, and other deployment solutions.
> Docker、Helm、安装程序及其他部署方案。

**6 projects** | [Back to overview](../README.md)

---

### OpenClawInstaller - OpenClaw 一键部署工具

[miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) | Stars: 2,978 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 作为一个功能强大的开源个人 AI 助手平台，其部署和配置过程对普通用户存在较高门槛：

---

### phioranex/openclaw-docker

[phioranex/openclaw-docker](https://github.com/phioranex/openclaw-docker) | Stars: 528 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方需要从源码构建，依赖管理和环境配置复杂，首次部署门槛高。phioranex/openclaw-docker 提供预构建镜像和一键安装脚本，每日自动构建并每 6 小时检查上游更新，确保用户始终使用最新版本，大幅降低部署成本。

**Features:** 预构建镜像, 一键安装脚本, 自动更新机制, 安装选项丰富, Docker Compose 集成, 持久化卷映射

---

### AlphaClaw

[chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | Stars: 481
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 部署和运维存在配置复杂、崩溃恢复手动、可观测性不足的问题。AlphaClaw 提供浏览器配置向导、自愈 Watchdog、Git 回滚、全栈可观测性，将首次部署到首条消息的时间缩短至 5 分钟以内，支持 Railway/Render 一键部署。

**Features:** Setup UI, Gateway Manager, Watchdog, Channel Orchestration, Prompt Hardening, Git Sync

---

### coollabsio-openclaw

[coollabsio/openclaw](https://github.com/coollabsio/openclaw) | Stars: 287
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方缺少 Docker 镜像，部署需要手动编写 Dockerfile、安装依赖、配置环境变量，且每天发布新版本导致手动更新成本高。该项目提供全自动化 Docker 构建方案，每 6 小时检查新版本并自动构建推送，通过环境变量配置所有设置，内置 Nginx 反向代理和 HTTP Basic Auth，支持 Coolify 一键部署。

**Features:** 自动更新工作流, 环境变量配置系统, Nginx 反向代理, 浏览器 Sidecar 模式, 持久化存储, 两层 Docker 构建

---

### openclaw-helm

[serhanekicii/openclaw-helm](https://github.com/serhanekicii/openclaw-helm) | Stars: 149
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方未提供 Kubernetes 部署方案，企业用户需要自行编写 Deployment/Service/ConfigMap 等资源清单，配置复杂且难以标准化。openclaw-helm 基于 bjw-s app-template 提供生产级 Helm Chart，支持单实例部署、Secret 管理、端口映射和设备配对流程，简化 K8s 环境的 OpenClaw 运维。

**Features:** 生产级 Helm Chart, 架构清晰, Secret 管理, 设备配对流程, 私有镜像支持, Artifact Hub 发布

---

### lobsterd

[tsconfigdotjson/lobsterd](https://github.com/tsconfigdotjson/lobsterd) | Stars: 25
Researched: 2026-03-11 | Updated: 2026-03-13

多租户 OpenClaw 部署缺乏强隔离，共享主机存在安全风险和资源竞争。lobsterd 通过 Firecracker MicroVM 为每个租户提供轻量级虚拟机，实现网络隔离、per-tenant overlay 文件系统和独立 OpenClaw Gateway。

**Features:** Firecracker MicroVM 编排, Per-tenant Overlay 文件系统, 网络隔离, 完整 CLI 工具链, Watchdog 守护进程, REST API

---
