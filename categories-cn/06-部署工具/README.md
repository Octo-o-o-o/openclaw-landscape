# 部署工具

| # | 项目 | Stars | 简介 | 调研 |
|---|------|-------|------|------|
| 1 | [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) | 2,978 | OpenClaw 作为一个功能强大的开源个人 AI 助手平台，其部署和配置过程对普通用户存在较高门槛： | [openclawinstaller.md](openclawinstaller.md) |
| 2 | [phioranex/openclaw-docker](https://github.com/phioranex/openclaw-docker) | 528 | OpenClaw 官方需要从源码构建，依赖管理和环境配置复杂，首次部署门槛高。 | [phioranex-docker.md](phioranex-docker.md) |
| 3 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | 482 | OpenClaw 部署和运维存在配置复杂、崩溃恢复手动、可观测性不足的问题。 | [alphaclaw.md](alphaclaw.md) |
| 4 | [coollabsio/openclaw](https://github.com/coollabsio/openclaw) | 287 | OpenClaw 官方缺少 Docker 镜像，部署需要手动编写 Dockerfile、安装依赖、配置环境变量，且每天发布新版本导致手动更新成本高。 | [coollabsio-openclaw.md](coollabsio-openclaw.md) |
| 5 | [serhanekicii/openclaw-helm](https://github.com/serhanekicii/openclaw-helm) | 149 | OpenClaw 官方未提供 Kubernetes 部署方案，企业用户需要自行编写 Deployment/Service/ConfigMap 等资源清单，... | [openclaw-helm.md](openclaw-helm.md) |
| 6 | [tsconfigdotjson/lobsterd](https://github.com/tsconfigdotjson/lobsterd) | 25 | 多租户 OpenClaw 部署缺乏强隔离，共享主机存在安全风险和资源竞争。 | [lobsterd.md](lobsterd.md) |
