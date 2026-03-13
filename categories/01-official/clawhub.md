> https://github.com/openclaw/clawhub

# openclaw/clawhub

## Basic Information

- **GitHub Repository**: https://github.com/openclaw/clawhub
- **Stars**: 5,292
- **Official Website**: https://clawhub.ai
- **Sister Site**: https://onlycrabs.ai (SOUL.md registry)
- **Created**: 2026-01-03
- **Last Updated**: 2026-03-11
- **Primary Language**: TypeScript
- **Repository Size**: 2,622 KB

## Problem & Solution

### Core Problems

The core problem facing the OpenClaw ecosystem is **distribution, version management, and discovery of Agent skills**. As AI Agent capabilities expand, a standardized approach is needed to:

1. **Publish and share skills**: Developers need a centralized platform to publish skill packages they build for agents
2. **Version control**: Skills need semantic versioning, changelogs, and rollback capabilities
3. **Dependency declaration**: Skills need to explicitly declare runtime dependencies (environment variables, binary tools, config files)
4. **Security review**: Uploaded skills require security scanning and content moderation to prevent malicious code
5. **Discoverability**: Users need to quickly find the skills they need through semantic search (not just keywords)
6. **CLI-friendly**: Skill installation, updates, and syncing need to be seamlessly handled via command-line tools

### Solution

ClawHub provides a **public skill registry** (similar to npm, PyPI) with the following core capabilities:

- **Text-based skill package format**: Each skill is a folder containing `SKILL.md` (required) and supporting files
- **Semantic versioning + tag system**: Each release creates a new version, with `latest` and other tag pointers
- **Vector search**: Uses OpenAI embeddings + Convex vector index for semantic search
- **GitHub OAuth authentication**: Login via GitHub account, with a 14-day account age threshold to prevent abuse
- **Automated security scanning**: Static analysis of skill code, detecting metadata mismatches and suspicious behavior
- **Moderation mechanism**: User reports, auto-hide (>3 reports), moderator/admin review workflow
- **CLI tool**: `clawhub` command-line tool supporting `install`, `update`, `publish`, `sync`, and more
- **GitHub backup**: Automatically backs up all skills to the `clawdbot/skills` repository via a GitHub App

## Core Architecture

### Tech Stack

- **Frontend**: TanStack Start (React + Vite/Nitro) - modern SPA framework
- **Backend**: Convex - serverless database + file storage + HTTP Actions
- **Authentication**: Convex Auth + GitHub OAuth
- **Search**: OpenAI `text-embedding-3-small` + Convex vector index
- **CLI**: Bun + TypeScript, published as the `clawhub` npm package
- **Shared layer**: `clawhub-schema` package defines API routes and types
- **Testing**: Vitest 4, target coverage >= 70%
- **Code quality**: Biome + Oxlint (type-aware)

### Data Model

#### Core Entities

1. **User**
   - `authId` (provided by Convex Auth)
   - `handle` (GitHub username)
   - `role`: `admin | moderator | user`
   - `avatarUrl`, `name`, `bio`
   - `githubCreatedAt` (used for the 14-day account age threshold)

2. **Skill**
   - `slug` (unique identifier)
   - `displayName`, `summary`
   - `ownerUserId`
   - `latestVersionId`, `latestTagVersionId`
   - `tags` mapping: `{ tag -> versionId }`
   - `badges`: `redactionApproved`, `highlighted`, `official`, `deprecated`
   - `moderationStatus`: `active | hidden | removed`
   - `moderationFlags`, `moderationReason`
   - `stats`: `downloads`, `stars`, `versions`, `comments`

3. **SkillVersion**
   - `skillId`, `version` (semver)
   - `changelog` (required)
   - `files`: `[{ path, size, storageId, sha256 }]`
   - `parsed` (metadata extracted from SKILL.md frontmatter)
   - `embeddingId` (vector search)
   - `softDeletedAt` (soft delete)

4. **Soul (System Persona)**
   - Similar structure to Skill, but only accepts `SOUL.md` files
   - Hosted on onlycrabs.ai (hostname-based entry point)

5. **Comment, Star, AuditLog**
   - Comments, favorites, and audit logs

#### Metadata Specification

Skills declare their runtime requirements in the YAML frontmatter of `SKILL.md`:

```yaml
---
name: my-skill
description: Manage tasks via the Todoist API
metadata:
  openclaw:
    requires:
      env:
        - TODOIST_API_KEY
      bins:
        - curl
    primaryEnv: TODOIST_API_KEY
    install:
      - kind: brew
        formula: jq
        bins: [jq]
---
```

Supported fields:
- `requires.env`: Environment variables
- `requires.bins`: Required CLI tools
- `requires.anyBins`: At least one of these CLI tools is needed
- `requires.config`: Configuration file paths
- `install`: Dependency installation specs (brew, node, go, uv)
- `nix`: Nix plugin pointer (for nix-clawdbot)
- `os`: Operating system restrictions

### Key Design Decisions

1. **Plain-text skill packages**
   - Limited to text files (50MB cap), binary files not accepted
   - Extension whitelist + MIME type checking
   - Reduces security risk, facilitates static analysis

2. **Convex as backend**
   - Serverless architecture, simplifies deployment
   - Built-in file storage (`_storage`)
   - Real-time queries + HTTP Actions
   - Native vector search support

3. **Soft delete + moderation workflow**
   - Version soft delete (`softDeletedAt`), preserves history
   - Auto-hide mechanism (>3 reports)
   - Moderators can restore, admins can hard-delete

4. **GitHub account age threshold**
   - Publishing skills/souls requires a GitHub account >= 14 days old
   - Commenting also requires >= 14 days
   - Reduces spam and abuse

5. **Vector search first**
   - Uses embeddings rather than keyword search
   - Indexes SKILL.md + other text files + metadata summary
   - Supports filters (tags, owner, minimum stars, update date)

6. **CLI-first workflow**
   - `clawhub install <slug>` - Install a skill
   - `clawhub sync` - Scan local skills, auto-publish/update
   - `clawhub update --all` - Batch update
   - Local state management: `.clawhub/lock.json` (working directory) + `.clawhub/origin.json` (skill folder)

## Key Features

### 1. Skill Publishing & Version Management

- **Upload workflow** (50MB limit):
  1. Client requests an upload session
  2. Upload each file via a Convex upload URL
  3. Submit metadata + file list + changelog + version + tags
  4. Server validation (size, extensions, SKILL.md presence, frontmatter parseable, version uniqueness, GitHub account age)
  5. Store files + metadata, set `latest` tag, update statistics

- **Version control**:
  - Each upload creates a new `SkillVersion`
  - `latest` tag automatically points to the newest version (unless the user re-tags)
  - Rollback support: Move `latest` (and other tags) to an older version

### 2. Security & Moderation

- **Static scanning**:
  - Persists deterministic static scan results at publish time
  - `moderationVerdict`: `clean | suspicious | malicious`
  - `moderationReasonCodes[]`: Machine-readable reason codes
  - `moderationEvidence[]`: File/line evidence (capped)

- **Reporting mechanism**:
  - Each user can have up to 20 active reports
  - 4th unique report triggers auto-hide
  - Skill reports: soft delete + `moderationStatus = hidden`
  - Comment reports: soft-delete the comment

- **AI comment scanning**:
  - Uses OpenAI to classify scam comments
  - `scamScanVerdict`: `not_scam | likely_scam | certain_scam`
  - Only `certain_scam` + `high` confidence triggers auto-ban

- **Ban workflow**:
  - Hard-delete all owned skills
  - Soft-delete all comments
  - Revoke API tokens
  - Set `deletedAt`

### 3. CLI Tool

- **Authentication**: `clawhub login`, `clawhub whoami`
- **Discovery**: `clawhub search ...`, `clawhub explore`
- **Local management**:
  - `clawhub install <slug>` - Install to `./skills/<slug>`
  - `clawhub uninstall <slug>` - Remove local installation only
  - `clawhub list` - List installed skills
  - `clawhub update --all` - Batch update
- **Inspection**: `clawhub inspect <slug>` - View without installing
- **Publishing**:
  - `clawhub publish <path>` - Publish a single skill
  - `clawhub sync` - Scan root directory, auto-publish/update
- **Telemetry**:
  - `clawhub sync` reports installation telemetry (counts installs)
  - Disable via `CLAWHUB_DISABLE_TELEMETRY=1`

### 4. Nix Plugin Support

- **nixmode skills**:
  - Stores nix-clawdbot plugin pointers in SKILL.md frontmatter
  - Nix plugins bundle skill packages + CLI binaries + config flags/requirements

Example:
```yaml
---
name: peekaboo
metadata:
  clawdbot:
    nix:
      plugin: "github:clawdbot/nix-steipete-tools?dir=tools/peekaboo"
      systems: ["aarch64-darwin"]
    config:
      requiredEnv: ["PADEL_AUTH_FILE"]
      stateDirs: [".config/padel"]
      example: "config = { env = { PADEL_AUTH_FILE = \"/run/agenix/padel-auth\"; }; };"
    cliHelp: "padel --help\nUsage: padel [command]\n"
---
```

### 5. onlycrabs.ai (SOUL.md Registry)

- **Hostname-based entry point**: `onlycrabs.ai`
- **Soul bundles**: Only accepts `SOUL.md` (no additional files supported yet)
- **Shared infrastructure with skills**: Same version control, search, and moderation mechanisms
- **Purpose**: Publish and share agent system personas/prompts

### 6. GitHub Backup

- **GitHub App integration**:
  - Automatically backs up all skills to the `openclaw/skills` repository (2,524 stars)
  - Currently archives 1,000+ skills
  - One directory per skill, containing all versions
- **Historical archive**:
  - Retains suspicious/malicious skills for further analysis
  - Users should preferentially use the website for downloads, treating this as a historical archive

## Summary

ClawHub is critical infrastructure for the OpenClaw ecosystem, solving the problems of agent skill distribution, version management, security review, and discovery. Its core value lies in:

1. **Standardization**: Defines the skill package format and metadata specification
2. **Security first**: Multi-layered security review mechanisms
3. **Developer-friendly**: CLI-first workflow + automated syncing
4. **Semantic search**: Vector search improves discoverability
5. **Community-driven**: Open publishing platform + moderation mechanisms
