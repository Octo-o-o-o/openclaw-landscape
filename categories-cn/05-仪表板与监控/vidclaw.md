> https://github.com/madrzak/vidclaw

# VidClaw (139 stars)

## 问题与解决方案
OpenClaw Agent 在远程服务器上运行时缺乏可观测性，用户无法实时了解 Agent 的执行状态和行为。VidClaw 通过实时录屏和回放功能，将 Agent 的每次运行转化为可观测、可审计、可分享的视频记录。

## 关键特性
- **看板任务管理** — Backlog → Todo → In Progress → Done 拖拽式任务流，Agent 通过心跳或 cron 自动拾取任务
- **实时使用追踪** — 从会话记录解析 token 使用量和成本估算，匹配 Anthropic 速率限制窗口的进度条
- **模型热切换** — 从仪表板直接切换 Claude 模型，通过 OpenClaw 配置监听器热重载
- **活动日历视图** — 从内存文件和任务历史解析的月度 Agent 活动视图
- **工作区文件浏览器** — 支持 markdown 预览、语法高亮和下载的文件浏览器
- **技能管理器** — 查看所有捆绑/工作区技能，启用/禁用，创建自定义技能

<!-- lastCommit: 6a7050b -->
