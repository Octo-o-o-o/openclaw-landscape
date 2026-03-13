> https://github.com/LeoYeAI/openclaw-backup

# openclaw-backup (916 stars)

## 问题与解决方案
OpenClaw 实例的迁移和备份缺乏标准化方案，用户需要手动备份配置、凭证、会话历史等数据。该项目提供一键备份和恢复功能，将 workspace、memory、skills、credentials、bot tokens、API keys、agent session history 打包为单个归档文件，支持零重新配对迁移到新实例。

## 关键特性
- 一键备份：workspace、config、credentials、sessions、cron jobs、scripts
- 一键恢复：支持 dry-run 预览，恢复后无需重新配对
- 浏览器 UI：下载/上传/恢复备份文件
- 服务器迁移：旧机器下载备份 → 新机器上传恢复
- 安全措施：备份文件 chmod 600，HTTP 服务器强制 token 认证
- 由 MyClaw.ai 提供支持，发布在 ClaWHub
