> https://github.com/aliramw/dingtalk-ai-table

# dingtalk-ai-table (66 stars)

## Problem & Solution

The DingTalk AI Table (multi-dimensional table) API operations are complex and documentation is scattered, making manual calls inefficient. This project wraps 19 DingTalk AI Table APIs as MCP tools, provides scripts for bulk field creation, bulk record import, and security testing, supports the new ID system (baseId/tableId/fieldId/recordId), and achieves production-grade quality with 21/21 tests passing.

## Key Features

- **Full coverage of the new API** — Adapted to the new MCP tools released on 2026-03-10, covering 19 APIs (table management, field operations, record CRUD, view management, etc.)
- **Bulk operation scripts** — `bulk_add_fields.py` for bulk field creation, `import_records.py` for bulk record import, with type validation and error rollback support
- **ID system migration** — Deprecates the old `dentryUuid/sheetIdOrName` system, fully migrated to the new `baseId/tableId/fieldId/recordId`, with a migration guide provided
- **Security and construction testing** — `test_security.py` covers SQL injection, XSS, path traversal, and other security tests to ensure robust input validation and error handling
- **Environment variable configuration** — Requires `DINGTALK_MCP_URL` (MCP service address); recommends `OPENCLAW_WORKSPACE` (file sandbox root directory); supports `mcporter` binary invocation
- **Error code documentation** — Provides `error-codes.md` with detailed troubleshooting guides covering authentication failures, insufficient permissions, parameter errors, and other common issues

<!-- lastCommit: d582892ee15d0987e042769220fa98660d1a9bd9 -->
