> https://github.com/ringhyacinth/Star-Office-UI

# Star Office UI (4,092 stars)

## 问题与解决方案

AI Agent 的工作状态不可见，用户无法直观了解"Agent 此刻在做什么、昨天做了什么、是否在线"。Star Office UI 是像素风格的 AI 办公室看板，将 Agent 状态实时可视化为办公室场景，支持多 Agent 协作、中英日三语、AI 生图装修和桌面宠物模式。

## 关键特性

- **六种状态可视化** — idle/writing/researching/executing/syncing/error 自动映射到办公室不同区域，像素角色实时走动 + 气泡展示
- **昨日小记** — 自动从 `memory/*.md` 读取最近一天工作记录，脱敏后展示为卡片，提供 Agent 工作历史快照
- **多 Agent 协作** — 通过 join key 邀请其他 Agent 加入办公室，实时查看多人状态，适合团队协作场景
- **美术资产管理** — 侧边栏管理角色/场景/装饰素材，支持动态帧同步避免闪烁，可接入 Gemini API 用 AI 生成背景
- **安全加固** — 侧边栏密码保护、生产环境弱密码拦截、Session Cookie 加固，防止未授权访问
- **灵活部署** — Python 3.10+ 后端（Flask），30 秒手动部署或 Docker 一键启动，推荐 Cloudflare Tunnel 公网化

<!-- lastCommit: 6a7050b -->
