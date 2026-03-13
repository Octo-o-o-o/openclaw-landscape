> https://github.com/pepicrft/plugin-vault

# OpenClaw Vault Plugin (41 stars)

## 问题与解决方案
OpenClaw 缺乏结构化知识管理能力，用户需要外部工具（如 Obsidian）管理笔记和知识库。Vault Plugin 将本地目录转化为结构化知识库，通过 qmd 提供快速语义搜索和嵌入，保持纯 markdown 格式。

## 关键特性
- **本地优先架构** — 纯 markdown 文件存储，无需外部数据库，支持 git 同步（pull before、push after）
- **约定式目录结构** — inbox（原始捕获）、notes（常青笔记）、people（人物传记）、projects（项目简报）、concepts（概念定义）、logs（每日笔记）
- **Frontmatter 框架** — 必需字段（title、created、updated）+ 推荐字段（summary、status、tags、people、projects、sources）
- **QMD 搜索引擎** — 支持关键词、语义、混合三种搜索模式，自动安装 qmd（通过 bun 或 npm）
- **CLI + 工具 + Gateway RPC** — 三种访问方式：`openclaw vault init/add/query`、Agent 工具调用、Gateway HTTP 端点
- **自动 git 提交** — 可选的 git 自动提交和推送，保持知识库版本控制

<!-- lastCommit: 6a7050b -->
