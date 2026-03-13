> https://github.com/ythx-101/x-tweet-fetcher

# ythx-101/x-tweet-fetcher (407 stars)

## 问题与解决方案

X/Twitter 关闭了免费 API，传统爬虫易被封禁，浏览器自动化方案脆弱。该项目通过零依赖的 HTTP 请求（单条推文）+ Camofox 浏览器自动化（评论/时间线/长文）组合方案，实现无需登录、无需 API Key 的推文抓取，输出结构化 JSON 供 Agent 直接消费。

## 关键特性

- **零配置单推抓取** — 一行命令获取推文文本、点赞数、转发数、浏览量、媒体 URL，无需任何依赖或认证
- **高级功能（Camofox）** — 支持评论树、用户时间线（最多 200 条）、X Articles 长文、X Lists、@mentions 监控
- **跨平台内容聚合** — 集成微信公众号搜索（搜狗）、微博/B站/CSDN 抓取、Google 搜索（零 API Key），一个工具覆盖中英文社交媒体
- **Agent 友好设计** — 所有输出为结构化 JSON，支持 Python 模块导入，退出码适配 cron（0=无新内容，1=有新内容）
- **用户画像分析** — 结合 LLM 分析用户推文生成 MBTI、Big Five 人格特征、话题图谱
- **增量监控模式** — `--monitor` 参数支持定时检查新 @mentions，适合自动化工作流
