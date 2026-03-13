> https://github.com/mnfst/manifest

# Manifest (3,733 stars)

## 问题与解决方案

OpenClaw 将所有请求发送到同一模型，小任务也调用大模型导致成本浪费。Manifest 是 OpenClaw 插件，通过 23 维度评分算法在 <2ms 内将请求路由到最合适的模型，节省高达 70% 成本。提供 Cloud 和 Local 两种部署模式，Local 模式所有数据留在本地，Cloud 模式仅传输 OpenTelemetry 元数据（不含消息内容）。

## 关键特性

- **23 维度路由算法** — 在 <2ms 内评估请求并路由到最合适模型，比 ClawRouter 的 15 维度更细粒度
- **Cloud/Local 双模式** — Cloud 模式跨设备访问仪表盘 + 多 Agent 连接，Local 模式数据完全本地存储（http://127.0.0.1:2099）
- **OTLP 原生支持** — 标准 OpenTelemetry 摄取（traces/metrics/logs），可与现有可观测性栈集成
- **零编码安装** — OpenClaw 插件一键安装，无需修改代码，自动拦截请求并路由
- **隐私优先架构** — Cloud 模式的盲代理物理上无法读取 prompt（与"信任我们"的服务本质不同），Local 模式数据永不离开本地
- **匿名产品分析** — 仅收集哈希机器 ID、OS 平台、包版本、事件名称，可通过 `MANIFEST_TELEMETRY_OPTOUT=1` 或配置文件关闭
