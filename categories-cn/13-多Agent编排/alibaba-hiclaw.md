> https://github.com/alibaba/hiclaw

# HiClaw (1,541 stars)

## 问题与解决方案
单个 Agent 难以处理复杂任务，且缺乏协作和监督机制。HiClaw 基于 OpenClaw 构建 Agent Teams 系统，通过 Manager Agent 协调多个 Worker Agent，在 Matrix IM 中实现可视化协作和人工干预，解决复杂任务的分工和监督问题。

## 关键特性
- Manager Agent 作为 AI 总监，创建 Worker、分配任务、监控进度
- 所有通信在 Matrix Rooms 中进行，用户可随时干预
- 安全设计：Worker 仅持有 consumer token，真实凭证由 Higress AI Gateway 管理
- 一键安装脚本，内置 Matrix 服务器、文件存储、Web 客户端
- 支持从 skills.sh 拉取 80,000+ 社区技能
- 定期心跳监控，Worker 卡住时自动告警
- 支持 CoPaw Worker（80% 内存占用减少，本地浏览器自动化）

<!-- lastCommit: 6a7050b -->
