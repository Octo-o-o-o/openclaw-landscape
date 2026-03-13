# OpenClaw Security Guide by Knownsec (55 stars)

## 问题与解决方案
OpenClaw 的快速增长伴随严重安全风险，ZoomEye 数据显示全球 63,026 个可识别实例，GitHub Advisory Database 记录 245 个相关漏洞。Knownsec（知道创宇）发布全生命周期安全实践指南，覆盖安装、配置、使用和维护。

## 关键特性
- **安全安装检查清单** — 从可信源下载、隔离环境部署（VPS > VM > Docker）、最小权限原则、定期升级、配置备份
- **配置安全审计** — 最小化暴露（本地模式 + 防火墙拒绝 18789 端口）、启用 token 认证、定期运行 `openclaw security audit --deep`
- **SKILL 审查规则** — 检查任意 shell 执行、文件系统写入、未知域名网络请求、环境变量访问、Base64 编码代码、动态代码执行
- **日常检查脚本** — 检查 Gateway 端口绑定（`ss -lntp`）、匿名访问验证、root 身份运行检查、防火墙策略验证
- **事件响应流程** — 系统异常（卡顿、流量异常、CPU/内存高）时的应急处理步骤
- **中英双语文档** — 面向中国市场的本地化安全指南
