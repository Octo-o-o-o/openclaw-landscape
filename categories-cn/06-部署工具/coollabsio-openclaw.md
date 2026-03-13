> https://github.com/coollabsio/openclaw

# coollabsio-openclaw (287 stars)

## 问题与解决方案
OpenClaw 官方缺少 Docker 镜像，部署需要手动编写 Dockerfile、安装依赖、配置环境变量，且每天发布新版本导致手动更新成本高。该项目提供全自动化 Docker 构建方案，每 6 小时检查新版本并自动构建推送，通过环境变量配置所有设置，内置 Nginx 反向代理和 HTTP Basic Auth，支持 Coolify 一键部署。

## 关键特性
- 自动更新工作流：每 6 小时检查新版本，矩阵构建 amd64/arm64，合并为单一 manifest
- 环境变量配置系统：通过 configure.js 读取环境变量并写入 openclaw.json，支持 20+ AI 提供商
- Nginx 反向代理：统一入口 :8080 → :18789，支持 WebSocket 和可选 HTTP Basic Auth
- 浏览器 Sidecar 模式：独立浏览器容器通过 CDP 协议通信，支持 VNC 访问和会话复用
- 持久化存储：单一 /data 卷存储配置和用户数据，支持跨容器迁移
- 两层 Docker 构建：基础镜像（从源码构建）+ 最终镜像（添加 nginx + 配置脚本），加速构建
- 冒烟测试：构建后自动验证 openclaw --version
