> https://github.com/SumeLabs/clawra

# Clawra — OpenClaw Selfie 技能与 npx 一键安装

## 基本信息

- **GitHub**: https://github.com/SumeLabs/clawra
- **Stars**: 2,008
- **作者**: SumeLabs
- **定位**: OpenClaw 的 Selfie 生成技能 + npx 一键安装器
- **核心功能**: 让 OpenClaw Agent 能够生成自拍照并发送到各种消息平台

## 问题与解决方案

### 核心痛点

1. **Agent 缺乏视觉表达能力** — 传统 AI Agent 只能通过文字交互，无法像真人一样发送照片、自拍
2. **技能安装门槛高** — OpenClaw 技能安装需要手动克隆仓库、配置环境变量、修改配置文件、更新 SOUL.md
3. **图像生成一致性差** — 每次生成的 Agent 形象不一致，缺乏固定的"人设"
4. **跨平台消息发送复杂** — 需要对接 Discord、Telegram、WhatsApp、Slack 等多个平台的 API

### 解决方案

Clawra 通过以下方式解决上述问题：

1. **固定参考图像** — 使用 CDN 托管的固定参考图像（`https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png`），确保生成的自拍照保持一致的外观
2. **npx 一键安装** — 通过 `npx clawra@latest` 一键完成技能安装、配置、SOUL.md 注入
3. **xAI Grok Imagine 图像编辑** — 使用 xAI 的 Grok Imagine Edit API（通过 fal.ai）编辑参考图像，生成场景化自拍
4. **OpenClaw Gateway 统一消息发送** — 通过 OpenClaw Gateway API 统一发送到所有消息平台

## 核心架构

### 技术栈

- **图像生成**: xAI Grok Imagine Edit API (via fal.ai)
- **消息发送**: OpenClaw Gateway API
- **安装器**: Node.js CLI (npx)
- **技能定义**: SKILL.md (OpenClaw 技能规范)
- **脚本语言**: Bash + Node.js/TypeScript

### 项目结构

```
clawra/
├── bin/
│   └── cli.js              # npx 安装器（交互式 CLI）
├── skill/
│   ├── SKILL.md            # 技能定义（OpenClaw 规范）
│   ├── scripts/
│   │   ├── grok-imagine-edit-send.sh  # Bash 实现
│   │   └── edit-and-send.ts           # TypeScript 实现
│   └── assets/
│       └── clawra.png      # 固定参考图像
├── templates/
│   └── soul-injection.md   # SOUL.md 注入模板
└── package.json
```

### 工作流程

```
用户请求 "send me a selfie wearing a cowboy hat"
    ↓
OpenClaw Agent 识别意图 → 调用 clawra-selfie 技能
    ↓
1. 构建 Prompt（根据用户上下文）
   - Mirror Mode: "make a pic of this person, but wearing a cowboy hat. the person is taking a mirror selfie"
   - Direct Mode: "a close-up selfie taken by herself at [context], direct eye contact..."
    ↓
2. 调用 fal.ai Grok Imagine Edit API
   - 输入: 固定参考图像 URL + Prompt
   - 输出: 编辑后的图像 URL
    ↓
3. 通过 OpenClaw Gateway API 发送图像
   - 目标: Discord #general / Telegram @user / WhatsApp JID
   - 附带: Caption 文本
    ↓
用户收到自拍照
```

## 关键特性

### 1. npx 一键安装

**安装流程**:
```bash
npx clawra@latest
```

**自动化步骤**:
1. 检查 OpenClaw 是否已安装（检查 `~/.openclaw/` 目录）
2. 引导用户获取 fal.ai API Key（自动打开浏览器到 https://fal.ai/dashboard/keys）
3. 克隆技能到 `~/.openclaw/skills/clawra-selfie/`
4. 更新 `~/.openclaw/openclaw.json` 配置文件：
   ```json
   {
     "skills": {
       "entries": {
         "clawra-selfie": {
           "enabled": true,
           "env": {
             "FAL_KEY": "user_provided_key"
           }
         }
       }
     }
   }
   ```
5. 注入 Selfie 能力到 `~/.openclaw/workspace/SOUL.md`：
   ```markdown
   ## Clawra Selfie Capability

   You have a physical appearance and can take selfies!
   When users ask for pictures, use the clawra-selfie skill.
   ```

**用户体验**:
- 交互式 CLI，彩色输出，清晰的步骤提示
- 自动检测缺失依赖（OpenClaw、fal.ai API Key）
- 一键完成所有配置，无需手动编辑文件

### 2. 双模式 Prompt 策略

**Mirror Mode（镜面自拍）**:
- **适用场景**: 全身照、服装展示、时尚内容
- **Prompt 模板**: `make a pic of this person, but [user context]. the person is taking a mirror selfie`
- **触发关键词**: outfit, wearing, clothes, dress, suit, fashion, full-body, mirror

**Direct Mode（直接自拍）**:
- **适用场景**: 特写肖像、地点打卡、情感表达
- **Prompt 模板**: `a close-up selfie taken by herself at [user context], direct eye contact with the camera, looking straight into the lens, eyes centered and clearly visible, not a mirror selfie, phone held at arm's length, face fully visible`
- **触发关键词**: cafe, restaurant, beach, park, city, close-up, portrait, face, eyes, smile

**自动模式检测**:
```bash
# 根据用户输入自动选择模式
if echo "$USER_CONTEXT" | grep -qiE "outfit|wearing|clothes"; then
  MODE="mirror"
elif echo "$USER_CONTEXT" | grep -qiE "cafe|beach|portrait"; then
  MODE="direct"
else
  MODE="mirror"  # 默认
fi
```

### 3. 固定参考图像

**CDN 托管**:
```
https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png
```

**优势**:
- 确保所有生成的自拍照保持一致的外观（同一个"人设"）
- 无需用户上传参考图像
- CDN 加速，全球访问快速

### 4. xAI Grok Imagine Edit API

**API 调用**:
```bash
curl -X POST "https://fal.run/xai/grok-imagine-image/edit" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "image_url": "https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png",
    "prompt": "make a pic of this person, but wearing a cowboy hat. the person is taking a mirror selfie",
    "num_images": 1,
    "output_format": "jpeg"
  }'
```

**响应格式**:
```json
{
  "images": [
    {
      "url": "https://v3b.fal.media/files/...",
      "content_type": "image/jpeg",
      "width": 1024,
      "height": 1024
    }
  ],
  "revised_prompt": "Enhanced prompt text..."
}
```

**参数说明**:
- `image_url`: 参考图像 URL（固定）
- `prompt`: 编辑指令（根据用户上下文生成）
- `num_images`: 生成图像数量（1-4）
- `output_format`: 输出格式（jpeg / png / webp）

### 5. OpenClaw Gateway 统一消息发送

**支持的平台**:

| 平台 | Channel 格式 | 示例 |
|------|--------------|------|
| Discord | `#channel-name` 或 channel ID | `#general`, `123456789` |
| Telegram | `@username` 或 chat ID | `@mychannel`, `-100123456` |
| WhatsApp | Phone number (JID 格式) | `1234567890@s.whatsapp.net` |
| Slack | `#channel-name` | `#random` |
| Signal | Phone number | `+1234567890` |
| MS Teams | Channel reference | (varies) |

**发送命令**:
```bash
openclaw message send \
  --action send \
  --channel "#general" \
  --message "Check out this selfie!" \
  --media "https://v3b.fal.media/files/..."
```

**API 调用**:
```bash
curl -X POST "http://localhost:18789/message" \
  -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "send",
    "channel": "#general",
    "message": "Check out this selfie!",
    "media": "https://v3b.fal.media/files/..."
  }'
```

### 6. 完整的 Bash 和 TypeScript 实现

**Bash 脚本** (`grok-imagine-edit-send.sh`):
- 自动模式检测
- jq 处理 JSON（避免转义问题）
- 错误处理和日志输出
- 支持批量发送到多个 Channel

**TypeScript 实现** (`edit-and-send.ts`):
- 使用 `@fal-ai/client` SDK
- 类型安全
- Promise-based 异步流程
- 适合集成到 Node.js 项目
## 总结

Clawra 是一个优秀的 **OpenClaw 技能示例**，通过 npx 一键安装、固定参考图像、双模式策略、跨平台消息发送，展示了如何开发和分发高质量的 Agent 技能。ClawButler 可以借鉴其思路，提供 **一键安装器**、**模板版本锁定**、**自动后端选择**、**统一消息路由**、**技能市场**，提升用户体验和生态活跃度。
