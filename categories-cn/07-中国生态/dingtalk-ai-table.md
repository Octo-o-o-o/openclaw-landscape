> https://github.com/aliramw/dingtalk-ai-table

# dingtalk-ai-table (46 stars)

## 问题与解决方案

钉钉 AI 表格（多维表）的 API 操作复杂且文档分散，手动调用效率低。该项目通过 MCP tools 封装 19 个钉钉 AI 表格 API，提供批量字段新增、批量记录导入、安全测试等脚本，支持新版 ID 体系（baseId/tableId/fieldId/recordId），实现 21/21 测试通过的生产级质量。

## 关键特性

- **新版 API 全覆盖** — 适配 2026-03-10 发布的新版 MCP tools，覆盖 19 个 API（表格管理、字段操作、记录 CRUD、视图管理等）
- **批量操作脚本** — `bulk_add_fields.py` 批量新增字段、`import_records.py` 批量导入记录，支持类型校验和错误回滚
- **ID 体系迁移** — 废弃旧版 `dentryUuid/sheetIdOrName`，全面切换到新版 `baseId/tableId/fieldId/recordId`，提供迁移指南
- **安全与构造测试** — `test_security.py` 覆盖 SQL 注入、XSS、路径遍历等安全测试，确保输入验证和错误处理健壮性
- **环境变量配置** — 必需 `DINGTALK_MCP_URL`（MCP 服务地址）、推荐 `OPENCLAW_WORKSPACE`（文件沙箱根目录），支持 `mcporter` 二进制调用
- **错误码文档** — 提供 `error-codes.md` 详细排查指南，覆盖认证失败、权限不足、参数错误等常见问题
