> https://github.com/SumeLabs/clawra

# Clawra — OpenClaw Selfie Skill with npx One-Click Install

## Basic Information

- **GitHub**: https://github.com/SumeLabs/clawra
- **Stars**: 2,008
- **Author**: SumeLabs
- **Positioning**: Selfie generation skill for OpenClaw + npx one-click installer
- **Core function**: Enables OpenClaw Agents to generate selfie photos and send them to various messaging platforms

## Problem & Solution

### Core Pain Points

1. **Agents lack visual expression ability** — Traditional AI Agents can only interact through text, unable to send photos or selfies like a real person
2. **High skill installation barrier** — Installing OpenClaw skills requires manually cloning repositories, configuring environment variables, modifying config files, and updating SOUL.md
3. **Poor image generation consistency** — Each generated Agent image looks different, lacking a fixed "persona"
4. **Cross-platform messaging is complex** — Requires interfacing with APIs of Discord, Telegram, WhatsApp, Slack, and other platforms

### Solution

Clawra addresses these issues through:

1. **Fixed reference image** — Uses a CDN-hosted fixed reference image (`https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png`) to ensure generated selfies maintain a consistent appearance
2. **npx one-click install** — Completes skill installation, configuration, and SOUL.md injection with `npx clawra@latest`
3. **xAI Grok Imagine image editing** — Uses xAI's Grok Imagine Edit API (via fal.ai) to edit the reference image and generate contextual selfies
4. **OpenClaw Gateway unified messaging** — Sends to all messaging platforms through the OpenClaw Gateway API

## Core Architecture

### Tech Stack

- **Image generation**: xAI Grok Imagine Edit API (via fal.ai)
- **Messaging**: OpenClaw Gateway API
- **Installer**: Node.js CLI (npx)
- **Skill definition**: SKILL.md (OpenClaw skill specification)
- **Script languages**: Bash + Node.js/TypeScript

### Project Structure

```
clawra/
├── bin/
│   └── cli.js              # npx installer (interactive CLI)
├── skill/
│   ├── SKILL.md            # Skill definition (OpenClaw specification)
│   ├── scripts/
│   │   ├── grok-imagine-edit-send.sh  # Bash implementation
│   │   └── edit-and-send.ts           # TypeScript implementation
│   └── assets/
│       └── clawra.png      # Fixed reference image
├── templates/
│   └── soul-injection.md   # SOUL.md injection template
└── package.json
```

### Workflow

```
User requests "send me a selfie wearing a cowboy hat"
    |
OpenClaw Agent identifies intent -> calls clawra-selfie skill
    |
1. Build Prompt (based on user context)
   - Mirror Mode: "make a pic of this person, but wearing a cowboy hat. the person is taking a mirror selfie"
   - Direct Mode: "a close-up selfie taken by herself at [context], direct eye contact..."
    |
2. Call fal.ai Grok Imagine Edit API
   - Input: Fixed reference image URL + Prompt
   - Output: Edited image URL
    |
3. Send image via OpenClaw Gateway API
   - Target: Discord #general / Telegram @user / WhatsApp JID
   - Attached: Caption text
    |
User receives selfie photo
```

## Key Features

### 1. npx One-Click Install

**Installation process**:
```bash
npx clawra@latest
```

**Automated steps**:
1. Checks if OpenClaw is installed (checks `~/.openclaw/` directory)
2. Guides user to obtain fal.ai API Key (automatically opens browser to https://fal.ai/dashboard/keys)
3. Clones skill to `~/.openclaw/skills/clawra-selfie/`
4. Updates `~/.openclaw/openclaw.json` configuration file:
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
5. Injects selfie capability into `~/.openclaw/workspace/SOUL.md`:
   ```markdown
   ## Clawra Selfie Capability

   You have a physical appearance and can take selfies!
   When users ask for pictures, use the clawra-selfie skill.
   ```

**User experience**:
- Interactive CLI with colored output and clear step prompts
- Automatically detects missing dependencies (OpenClaw, fal.ai API Key)
- Completes all configuration with one click, no manual file editing needed

### 2. Dual-Mode Prompt Strategy

**Mirror Mode (Mirror Selfie)**:
- **Use case**: Full-body shots, outfit showcases, fashion content
- **Prompt template**: `make a pic of this person, but [user context]. the person is taking a mirror selfie`
- **Trigger keywords**: outfit, wearing, clothes, dress, suit, fashion, full-body, mirror

**Direct Mode (Direct Selfie)**:
- **Use case**: Close-up portraits, location check-ins, emotional expression
- **Prompt template**: `a close-up selfie taken by herself at [user context], direct eye contact with the camera, looking straight into the lens, eyes centered and clearly visible, not a mirror selfie, phone held at arm's length, face fully visible`
- **Trigger keywords**: cafe, restaurant, beach, park, city, close-up, portrait, face, eyes, smile

**Automatic mode detection**:
```bash
# Automatically selects mode based on user input
if echo "$USER_CONTEXT" | grep -qiE "outfit|wearing|clothes"; then
  MODE="mirror"
elif echo "$USER_CONTEXT" | grep -qiE "cafe|beach|portrait"; then
  MODE="direct"
else
  MODE="mirror"  # Default
fi
```

### 3. Fixed Reference Image

**CDN hosting**:
```
https://cdn.jsdelivr.net/gh/SumeLabs/clawra@main/assets/clawra.png
```

**Advantages**:
- Ensures all generated selfies maintain a consistent appearance (same "persona")
- No need for users to upload a reference image
- CDN acceleration for fast global access

### 4. xAI Grok Imagine Edit API

**API call**:
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

**Response format**:
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

**Parameter description**:
- `image_url`: Reference image URL (fixed)
- `prompt`: Edit instruction (generated based on user context)
- `num_images`: Number of images to generate (1-4)
- `output_format`: Output format (jpeg / png / webp)

### 5. OpenClaw Gateway Unified Messaging

**Supported platforms**:

| Platform | Channel Format | Example |
|----------|---------------|---------|
| Discord | `#channel-name` or channel ID | `#general`, `123456789` |
| Telegram | `@username` or chat ID | `@mychannel`, `-100123456` |
| WhatsApp | Phone number (JID format) | `1234567890@s.whatsapp.net` |
| Slack | `#channel-name` | `#random` |
| Signal | Phone number | `+1234567890` |
| MS Teams | Channel reference | (varies) |

**Send command**:
```bash
openclaw message send \
  --action send \
  --channel "#general" \
  --message "Check out this selfie!" \
  --media "https://v3b.fal.media/files/..."
```

**API call**:
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

### 6. Complete Bash and TypeScript Implementations

**Bash script** (`grok-imagine-edit-send.sh`):
- Automatic mode detection
- jq for JSON processing (avoids escaping issues)
- Error handling and log output
- Supports batch sending to multiple channels

**TypeScript implementation** (`edit-and-send.ts`):
- Uses `@fal-ai/client` SDK
- Type-safe
- Promise-based async flow
- Suitable for integration into Node.js projects

## Summary

Clawra is an excellent **OpenClaw skill example** that demonstrates how to develop and distribute high-quality Agent skills through npx one-click installation, fixed reference images, dual-mode strategy, and cross-platform messaging.
