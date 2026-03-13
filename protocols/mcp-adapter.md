# openclaw-mcp-adapter (27 stars)

## 问题与解决方案

MCP（Model Context Protocol）服务器提供的工具无法被 OpenClaw Agent 直接调用，需要通过 CLI Skill 包装，增加了调用链路和延迟。该插件在 OpenClaw 启动时自动连接 MCP 服务器，发现并注册其工具为原生 Agent 工具，实现零中间层的直接调用。

## 关键特性

- **启动时自动发现** — Gateway 启动时连接配置的 MCP 服务器，自动发现并注册所有工具为一等公民工具
- **双传输协议支持** — 支持 stdio（子进程启动）和 HTTP（连接运行中的服务器）两种传输方式
- **工具名称前缀** — 可选的 `toolPrefix` 配置，避免多服务器工具名冲突（如 `myserver_toolname`）
- **沙箱集成** — 支持将 MCP 工具添加至沙箱工具白名单，实现细粒度权限控制
- **环境变量替换** — 支持在配置中使用 `${VAR}` 语法引用环境变量，安全管理 API 密钥
- **TypeScript 实现** — 使用 TypeScript 开发，提供类型安全和良好的开发体验
