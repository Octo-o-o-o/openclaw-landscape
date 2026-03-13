> https://github.com/sharbelxyz/x-bookmarks

# sharbelxyz/x-bookmarks (241 stars)

## 问题与解决方案

X/Twitter 的书签功能缺乏导出和批量管理能力，用户无法将收藏的推文用于知识管理或 Agent 工作流。该项目提供 OpenClaw 技能，通过浏览器自动化批量导出书签为结构化数据，支持过滤、搜索和与其他工具集成。

## 关键特性

- **批量书签导出** — 自动遍历 X 书签列表，提取推文 ID、文本、作者、时间戳、媒体链接等完整元数据
- **结构化输出** — 导出为 JSON/CSV 格式，便于导入 Notion、Obsidian 等知识管理工具或供 Agent 消费
- **过滤与搜索** — 支持按关键词、日期范围、作者筛选书签，快速定位目标内容
- **OpenClaw 原生集成** — 作为标准 SKILL.md 技能，可直接通过 `npx sundial-hub add x-bookmarks` 安装
- **增量同步** — 支持仅导出新增书签，避免重复处理已导出内容
- **隐私保护** — 本地运行，不上传书签数据到第三方服务器
