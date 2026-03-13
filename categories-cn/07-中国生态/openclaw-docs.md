> https://github.com/yeuxuan/openclaw-docs

# yeuxuan/openclaw-docs

## 基本信息

- **Stars**: 533
- **URL**: https://github.com/yeuxuan/openclaw-docs
- **在线文档**: https://openclaw-docs.dx3n.cn
- **License**: MIT
- **技术栈**: VitePress + Azure Static Web Apps

## 问题与解决方案

### 核心问题

OpenClaw 官方文档以英文为主，中文用户面临以下困难：

1. **语言障碍**：官方文档英文为主，中文用户理解成本高
2. **缺乏系统性**：官方文档分散，缺少从入门到精通的完整学习路径
3. **源码剖析缺失**：缺少对 OpenClaw 核心模块的深度源码解析
4. **安装教程不够详细**：各种平台、各种通道的安装配置缺少图文教程
5. **AI 框架原理不清晰**：上下文工程、状态机、记忆系统等核心概念缺少系统讲解

### 解决方案

yeuxuan/openclaw-docs 是 **OpenClaw 完整中文文档站**，提供：

- **276 篇原创中文教程**：覆盖安装、配置、源码、AI 框架
- **4 条学习主线**：
  - Track 0：安装教程（147 篇）
  - Track A：完整工程主线（59 篇）
  - Track B：AI 核心框架（22 篇）
  - Track C：通道适配器（含于 Track A）
- **函数级精度**：关键模块精确到具体函数的源码入口与调用链路
- **小白友好**：安装教程全程图文，零基础 10 分钟跑起来
- **SEO 完备**：276 页独立 description、sitemap、IndexNow 自动推送

## 核心架构

### 文档站架构

```
openclaw-docs/
├── docs/
│   ├── index.md                            # 首页
│   ├── tutorials/                          # Track 0：安装教程（147 篇）
│   │   ├── getting-started/                # 快速入门与向导安装
│   │   ├── installation/                   # Docker / Node / 云服务器部署
│   │   ├── gateway/                        # Gateway 配置与运维
│   │   ├── channels/                       # 通道接入（Telegram/WhatsApp/Discord 等）
│   │   ├── providers/                      # AI 模型 Provider 配置
│   │   ├── concepts/                       # 核心概念（上下文/记忆/状态机等）
│   │   ├── tools/                          # 工具系统（浏览器/执行/技能/子智能体）
│   │   ├── automation/                     # 自动化（Webhook/Cron/Poll）
│   │   └── help/                           # 故障排查与常见问题
│   ├── beginner-openclaw-guide/            # Track A：完整工程主线（59 篇）
│   └── beginner-openclaw-framework-focus/  # Track B：AI 核心框架（22 篇）
├── docs/.vitepress/
│   ├── config.mts                          # 站点配置（SEO / 导航 / 侧边栏）
│   └── theme/                              # 自定义主题与样式
└── scripts/
    ├── convert-mdx.mjs                     # MDX → VitePress Markdown 批量转换
    └── ping-indexnow.mjs                   # 构建后自动推送 URL 到 Bing IndexNow
```

### 技术栈

| 层级 | 技术 | 用途 |
|------|------|------|
| 静态站点生成器 | VitePress | Markdown → HTML，内置搜索、导航 |
| 部署平台 | Azure Static Web Apps | 自动构建、CDN 分发、HTTPS |
| SEO 优化 | IndexNow API | 自动推送 URL 到 Bing 索引 |
| 内容格式 | Markdown + Frontmatter | 文档编写，元数据管理 |

### 学习路径设计

```
Track 0: 安装教程（147 篇）
├── 快速入门
│   ├── 什么是 OpenClaw
│   ├── 系统要求
│   └── 5 分钟快速安装
├── 详细安装
│   ├── Docker 部署
│   ├── Node.js 源码部署
│   └── 云服务器部署（阿里云/腾讯云/AWS）
├── Gateway 配置
│   ├── 配置文件结构
│   ├── 环境变量
│   └── 启动参数
├── 通道接入
│   ├── Telegram Bot 配置
│   ├── WhatsApp 配置
│   ├── Discord Bot 配置
│   └── 飞书 Bot 配置
├── AI 模型配置
│   ├── Claude API 配置
│   ├── GPT API 配置
│   ├── DeepSeek 配置
│   └── Ollama 本地模型配置
└── 故障排查
    ├── 常见错误代码
    ├── 日志分析
    └── 社区求助指南

Track A: 完整工程主线（59 篇）
├── CLI 启动框架
│   ├── 入口函数 main()
│   ├── 命令解析
│   └── 子命令路由
├── Gateway 控制平面
│   ├── Gateway 启动流程
│   ├── 配置加载
│   └── 服务注册
├── 通道适配器
│   ├── 接口合同
│   ├── 注册链路
│   ├── 账号生命周期
│   ├── 入站路由
│   └── 出站发送解耦
├── Agent 执行链路
│   ├── 消息接收
│   ├── 上下文构建
│   ├── 模型调用
│   ├── 工具执行
│   └── 响应发送
└── 流式订阅
    ├── SSE 实现
    └── WebSocket 实现

Track B: AI 核心框架（22 篇）
├── 上下文工程
│   ├── 系统提示词
│   ├── 用户消息
│   └── 历史消息管理
├── Agent 状态机
│   ├── 状态定义
│   ├── 状态转换
│   └── 状态持久化
├── 工具策略与审批
│   ├── 工具注册
│   ├── 工具调用
│   └── 审批流程
├── 模型回退
│   ├── 主模型失败检测
│   └── 备用模型切换
├── 记忆系统
│   ├── 短期记忆（会话内）
│   ├── 长期记忆（跨会话）
│   └── 记忆检索
└── Hook 插件注入机制
    ├── Hook 定义
    ├── Hook 注册
    └── Hook 执行
```

## 关键特性

### 1. 函数级精度的源码剖析

**示例：Gateway 启动流程**

```
文章：《Gateway 启动流程详解》

1. 入口函数
   - 文件：src/cli/commands/gateway.ts
   - 函数：startGateway()
   - 行号：L42-L89

2. 配置加载
   - 文件：src/core/config-loader.ts
   - 函数：loadConfig()
   - 调用链：startGateway() → loadConfig() → parseConfigFile()

3. 通道注册
   - 文件：src/channels/registry.ts
   - 函数：registerChannels()
   - 遍历：config.channels.forEach(ch => registerChannel(ch))

4. Agent 初始化
   - 文件：src/agents/agent-manager.ts
   - 函数：initializeAgents()
   - 状态机：IDLE → INITIALIZING → READY
```

### 2. 图文并茂的安装教程

**特点**：
- **截图丰富**：每个关键步骤都有截图
- **命令可复制**：所有命令都用代码块展示，一键复制
- **错误示例**：展示常见错误的截图和解决方法
- **视频教程**：部分复杂操作提供视频演示

### 3. 多平台安装指南

| 平台 | 教程数量 | 覆盖内容 |
|------|---------|---------|
| macOS | 15 篇 | Homebrew 安装、M1/M2 兼容性、权限配置 |
| Linux | 20 篇 | Ubuntu/Debian/CentOS/Arch，systemd 配置 |
| Windows | 12 篇 | WSL2 安装、PowerShell 配置、防火墙设置 |
| Docker | 18 篇 | docker-compose、多容器编排、数据持久化 |
| 云服务器 | 25 篇 | 阿里云/腾讯云/AWS/GCP，安全组配置 |

### 4. 通道接入完整指南

**每个通道的教程结构**：

```
Telegram Bot 接入指南
├── 1. 创建 Bot（BotFather 操作截图）
├── 2. 获取 Token
├── 3. 配置 openclaw.json
├── 4. 启动 Gateway
├── 5. 测试对话
├── 6. 常见问题
│   ├── Bot 无响应
│   ├── 消息发送失败
│   └── 权限不足
└── 7. 高级配置
    ├── Webhook 模式
    ├── 群组管理
    └── 命令菜单
```

### 5. SEO 优化策略

**实现**：

```javascript
// scripts/ping-indexnow.mjs
import { readFileSync } from 'fs';
import fetch from 'node-fetch';

const sitemap = readFileSync('docs/.vitepress/dist/sitemap.xml', 'utf-8');
const urls = [...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(m => m[1]);

// 推送到 Bing IndexNow
await fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    host: 'openclaw-docs.dx3n.cn',
    key: process.env.INDEXNOW_KEY,
    urlList: urls
  })
});
```

**效果**：
- 新文章发布后 1 小时内被 Bing 索引
- 搜索"OpenClaw 中文文档"排名第一
- 每月自然搜索流量 5000+ 访问

### 6. MDX 到 VitePress 转换工具

**问题**：原始文档可能是 MDX 格式（React 组件）

**解决**：

```javascript
// scripts/convert-mdx.mjs
import { readFileSync, writeFileSync } from 'fs';
import { glob } from 'glob';

const files = glob.sync('docs/**/*.mdx');

files.forEach(file => {
  let content = readFileSync(file, 'utf-8');

  // 转换 React 组件为 Markdown
  content = content.replace(/<Callout type="warning">(.*?)<\/Callout>/gs,
    ':::warning\n$1\n:::');
  content = content.replace(/<Tabs>(.*?)<\/Tabs>/gs,
    (match, inner) => convertTabs(inner));

  // 保存为 .md
  writeFileSync(file.replace('.mdx', '.md'), content);
});
```
## 总结

yeuxuan/openclaw-docs 是一个**文档工程的典范**，其价值不在于代码，而在于：

1. **系统性**：276 篇文档形成完整的知识体系
2. **精确性**：函数级精度的源码剖析
3. **友好性**：图文并茂，零基础可上手
4. **可发现性**：SEO 优化，搜索引擎友好

ClawButler 可以借鉴其文档架构、学习路径设计、SEO 优化策略，构建一个**世界级的文档站**，降低用户学习成本，提升产品竞争力。

<!-- lastCommit: 137e138 -->
