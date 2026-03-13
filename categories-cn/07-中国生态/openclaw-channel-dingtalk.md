> https://github.com/soimy/channel-dingtalk

# openclaw-channel-dingtalk (1,267 stars)

## 问题与解决方案
企业用户需要在钉钉内使用 AI 助手，但 OpenClaw 缺乏钉钉接入能力。该项目通过 DingTalk Channel Plugin 使用 Stream 模式（无需公网 IP）实现钉钉企业内部机器人接入，支持私聊、群聊、多种消息类型和互动卡片。

## 关键特性
- Stream 模式：WebSocket 长连接，无需公网 IP 或 Webhook
- 支持私聊和群聊（@机器人）
- 支持文本、图片、语音（自带识别）、视频、文件、钉钉文档/钉盘文件卡片
- 引用消息支持：恢复大多数引用场景（文字/图片/图文/文件/视频/语音/AI 卡片）
- Markdown 回复和互动卡片（支持流式更新）
- 进程级内存态：消息去重、session 锁、gateway in-flight 防重锁
- 国内镜像源支持（npm 镜像）

<!-- lastCommit: 6a7050b -->
