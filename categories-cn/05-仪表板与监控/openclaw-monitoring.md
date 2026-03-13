> https://github.com/video-db/openclaw-monitoring

# OpenClaw Monitoring by VideoDB (15 stars)

## 问题与解决方案
远程运行的 AI Agent 缺乏可观测性，用户无法实时了解 Agent 的执行状态和行为，只能"发送任务 → 等待 → 收到成功消息 → 祈祷"。VideoDB Monitoring 通过实时流和可回放录制，将每次 Agent 运行转化为可观测、可审计、可分享的视频记录。

## 关键特性
- **实时流 + 可回放录制** — 每次运行生成可分享 URL（非死视频文件），支持实时观看和事后回放
- **可搜索时刻** — 通过 VideoDB 的视频索引查找特定操作（如"何时打开电子表格"）
- **Webhook 告警** — 检测到异常行为时发送通知
- **两种集成模式** — OpenClaw Skill（按需录制）和 Docker Sidecar（全程录制）
- **Agent 自我分析** — Agent 可查询自己的录制记录（"总结过去 2 小时的工作"、"制作今日工作亮点视频并发布到 YouTube"）
- **多场景应用** — 安全审计（捕获越界行为）、QA 测试（回放失败流程）、合规审计（完整视觉审计追踪）、数据集准备（构建计算机使用训练数据）
