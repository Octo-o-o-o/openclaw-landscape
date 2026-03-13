# phioranex/openclaw-docker (528 stars)

## 问题与解决方案

OpenClaw 官方需要从源码构建，依赖管理和环境配置复杂，首次部署门槛高。phioranex/openclaw-docker 提供预构建镜像和一键安装脚本，每日自动构建并每 6 小时检查上游更新，确保用户始终使用最新版本，大幅降低部署成本。

## 关键特性

- **预构建镜像** — `ghcr.io/phioranex/openclaw-docker:latest`，无需本地编译 Node.js 项目
- **一键安装脚本** — Linux/macOS `curl | bash`，Windows PowerShell `irm | iex`，自动检查 Docker 前置条件
- **自动更新机制** — 每日构建 + 每 6 小时检查上游 release，CI/CD 全自动化
- **安装选项丰富** — `--pull-only`（仅拉取镜像）、`--skip-onboard`（跳过向导）、`--no-start`（不启动网关）、`--install-dir`（自定义目录）
- **Docker Compose 集成** — 提供 `docker-compose.yml` 模板，简化多容器编排
- **持久化卷映射** — `~/.openclaw` 配置和 `~/.openclaw/workspace` 工作区自动挂载
