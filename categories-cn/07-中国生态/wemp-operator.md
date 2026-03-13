> https://github.com/IanShaw027/wemp-operator

# wemp-operator (46 stars)

## 问题与解决方案

微信公众号运营需要手动采集热点、分析数据、管理评论，重复劳动多且效率低。wemp-operator 通过 70 个微信公众号 API 集成 + 20+ 数据源（Hacker News/V2EX 等）+ AI 智能回复，实现内容采集、数据分析、互动管理的全流程自动化，支持自然语言交互（如"帮我采集今天的 AI 热点"）。

## 关键特性

- **三大工作流** — 内容采集（AI 扩展关键词 → 选择数据源 → 采集热点 → 筛选输出）、数据分析（获取统计 → 计算指标 → 生成洞察 → 输出报告 → 推送通知）、互动管理（检查评论 → AI 生成回复 → 用户确认 → 执行回复/精选）
- **70 个 API 集成** — 完整覆盖微信公众号 API，无需额外依赖（素材管理、用户管理、消息管理、数据统计等）
- **20+ 数据源** — 支持 Hacker News、V2EX、GitHub Trending、Reddit、Product Hunt 等技术社区热点采集
- **自然语言触发** — 通过 OpenClaw Skill 机制，用户直接说"生成公众号日报"即可触发，无需记忆命令
- **AI 智能回复** — 自动检测新评论并生成回复建议，用户确认后执行（支持批量精选）
- **ClawHub 一键安装** — `openclaw skill install IanShaw027/wemp-operator` 即可部署，配置仅需 AppID/AppSecret
