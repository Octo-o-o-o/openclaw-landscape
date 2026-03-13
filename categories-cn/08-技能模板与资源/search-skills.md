> https://github.com/blessonism/search-skills

# blessonism/openclaw-search-skills (232 stars)

## 问题与解决方案

通用搜索引擎（Google/Bing）无法满足 Agent 的深度研究需求，缺乏学术论文、专利、代码仓库等垂直领域的精准检索能力。该项目提供 10+ 个专业搜索技能（arXiv、Google Scholar、GitHub、专利数据库等），为 Agent 提供多源、结构化的深度搜索能力。

## 关键特性

- **垂直搜索覆盖** — 支持学术论文（arXiv、Google Scholar、PubMed）、代码仓库（GitHub、GitLab）、专利（USPTO、EPO）、技术文档（Stack Overflow、MDN）
- **结构化输出** — 每个搜索结果包含标题、摘要、作者、引用数、发布日期、DOI/URL 等完整元数据，便于 Agent 后续处理
- **高级过滤** — 支持按时间范围、引用数阈值、编程语言、许可证类型等条件精准筛选
- **批量检索** — 支持一次查询多个数据源，自动去重和排序，生成综合报告
- **引用追踪** — 自动提取论文引用关系，构建知识图谱，支持"顺藤摸瓜"式深度研究
- **OpenClaw 原生集成** — 每个搜索技能独立打包为 SKILL.md，可按需安装（如 `npx sundial-hub add arxiv-search`）

<!-- lastCommit: 6a7050b -->
