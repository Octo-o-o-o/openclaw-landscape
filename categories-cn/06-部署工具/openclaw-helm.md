> https://github.com/serhanekicii/openclaw-helm

# openclaw-helm (149 stars)

## 问题与解决方案

OpenClaw 官方未提供 Kubernetes 部署方案，企业用户需要自行编写 Deployment/Service/ConfigMap 等资源清单，配置复杂且难以标准化。openclaw-helm 基于 bjw-s app-template 提供生产级 Helm Chart，支持单实例部署、Secret 管理、端口映射和设备配对流程，简化 K8s 环境的 OpenClaw 运维。

## 关键特性

- **生产级 Helm Chart** — 基于 bjw-s app-template v3，支持 Kubernetes >= 1.26
- **架构清晰** — Gateway（18789）+ Chromium CDP（9222，可选），单实例部署（不可水平扩展）
- **Secret 管理** — 通过 `envFrom.secretRef` 注入 `ANTHROPIC_API_KEY` 和 `OPENCLAW_GATEWAY_TOKEN`
- **设备配对流程** — 提供 `kubectl port-forward` + `kubectl exec` 命令示例，简化首次配对
- **私有镜像支持** — 支持自定义 `image.repository` 和 `image.tag`，适配企业内部镜像仓库
- **Artifact Hub 发布** — 官方 Helm 仓库托管，`helm repo add` 即可安装

<!-- lastCommit: 6a7050b -->
