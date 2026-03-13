# OpenClaw Official Organization Small Projects Collection

This document summarizes 16 small projects under the OpenClaw official organization, covering infrastructure, community governance, development tools, automation bots, and more. While smaller in scale, these projects play important roles in the OpenClaw ecosystem.

---

## nix-openclaw (519 stars)

### Problem & Solution
OpenClaw needs a cross-platform, declarative package management and deployment solution. Traditional tools like Homebrew and npm suffer from version drift, environment inconsistency, and similar issues.

nix-openclaw provides a Nix-based packaging solution for OpenClaw, delivering:
- Reproducible build environments (pinned versions)
- Declarative configuration (home-manager integration)
- Automatic freshness (CI auto-updates)
- Plugin system integration (automatic skill document packaging)

### Key Features
- **Multi-platform support**: Darwin (aarch64) + Linux (x86_64/aarch64)
- **Plugin architecture**: Each tool exported as an independent openclawPlugin
- **Auto-sync**: CI syncs skill documents every 30 minutes, checks tool updates every 10 minutes
- **Zero-drift deployment**: Dependency versions locked via Nix flakes
---

## openclaw.ai (222 stars)

### Problem & Solution
OpenClaw needs a clear, efficient official portal providing quick installation, feature showcases, and community entry points.

openclaw.ai is an Astro-based static site providing:
- One-click install scripts (macOS/Linux/Windows)
- Integration showcase pages (/integrations)
- Community feedback pages (/shoutouts)

### Key Features
- **Multi-platform install scripts**:
  - macOS/Linux: `curl -fsSL https://openclaw.ai/install.sh | bash`
  - Windows: `iwr -useb https://openclaw.ai/install.ps1 | iex`
- **Smart UI detection**: Automatically detects terminal type, uses Gum UI for interactive terminals, falls back to plain text for non-interactive
- **Auto-deploy**: Pushes to the main branch automatically deploy to GitHub Pages
- **First-run optimization**: New installs auto-run `openclaw onboard`, upgrades run `openclaw doctor --non-interactive`
---

## clawdinators (140 stars)

### Problem & Solution
OpenClaw needs 24/7 AI maintainer agents to monitor GitHub repositories, respond to Discord requests, and auto-handle PRs and Issues. Traditional manual SSH deployments suffer from config drift, poor reproducibility, and lack of auto-updates.

clawdinators provides a NixOS-based image deployment solution:
- **Image-based deployment**: Every deployment is a fresh AMI, no SSH, no config drift
- **Auto-bootstrap**: Instances pull encrypted secrets and repo seeds from S3 at startup
- **Self-updating**: systemd timer periodically runs `flake lock --update-input` + `nixos-rebuild switch`
- **Hive memory**: State shared across instances via EFS for multi-instance coordination

### Key Features
- **Dual-layer architecture**:
  - General layer: NixOS-on-AWS infrastructure (AMI pipeline, OpenTofu, S3 bootstrap, agenix secrets)
  - Specific layer: CLAWDINATOR agent logic (Discord gateway, GitHub monitoring, persona system)
- **Deployment workflow**:
  1. `nixos-generators` builds a raw image
  2. Upload to S3
  3. AWS VM Import creates an AMI
  4. OpenTofu launches EC2
  5. Instance auto-downloads secrets and runs `nixos-rebuild switch`
- **Security design**:
  - Uses agenix to encrypt secrets (Discord token, Anthropic API key, GitHub App private key)
  - SSH disabled by default
  - Binds only to the Tailscale network
---

## community (73 stars)

### Problem & Solution
The OpenClaw Discord server needs transparent, traceable community governance documentation, along with clear team division of labor and responsibility boundaries.

The community repository provides:
- Public community policy documents (Mod Onboarding, Moderation Guide, Rules, Roles Reference, Incident Playbook)
- Hierarchical structure and responsibility divisions for four specialized teams
- Transparent application processes

### Key Features
- **Four-team architecture**:
  - Discord Moderator (text channels)
  - VC Moderator (voice channels)
  - Helper (technical support)
  - Configurator (server configuration)
- **Human checkpoint design**: Clear responsibility boundaries between teams, cross-team collaboration requires Lead coordination
- **Transparency first**: All policy documents are open source, changes discussed via GitHub Issues (except Rules, which require Discord #announcements posts)
- **Application process**: Apply via email, providing experience, references, timezone, and availability
---

## clawgo (56 stars)

### Problem & Solution
OpenClaw needs a lightweight node client running on resource-constrained devices (like Raspberry Pi), connecting to the gateway bridge and handling voice transcription and chat responses.

clawgo is a minimal headless node client written in Go, providing:
- Low resource footprint (suitable for Raspberry Pi)
- Voice transcription stream processing (stdin/FIFO)
- Local TTS support (espeak-ng, Piper, ElevenLabs)
- mDNS service discovery

### Key Features
- **Cross-platform compilation**: `GOOS=linux GOARCH=arm64 go build`
- **Flexible input sources**: Supports stdin, FIFO, file
- **Multiple TTS engines**: system (espeak-ng), piper, elevenlabs, none
- **Pairing mechanism**: Register nodes via `clawgo pair`, requires approval on the gateway
- **systemd integration**: Provides systemd service examples
---

## homebrew-tap (32 stars)

### Problem & Solution
OpenClaw needs to distribute CLI tools and macOS apps via Homebrew, but doesn't want to submit to the official homebrew-core (slow review process, high maintenance cost).

homebrew-tap provides a custom Homebrew tap supporting:
- Formulae (CLI tools)
- Casks (macOS apps)
- Fast iteration and releases

### Key Features
- **Installation**: `brew tap clawdbot/tap && brew install clawdbot/tap/<name>`
- **Enhanced Cask uninstall**: Supports `--zap` option to clean up user data
- **Independent maintenance**: Not dependent on homebrew-core's review process
---

## hermit (26 stars)

### Problem & Solution
The OpenClaw Discord server needs a lightweight bot to handle GitHub queries and AutoMod keyword responses.

hermit is a Discord bot built on the Carbon framework, providing:
- `/github` command for querying Issues and PRs
- AutoMod keyword-triggered auto-replies
- Configurable message templates

### Key Features
- **Carbon framework**: Uses the Bun runtime for fast startup
- **Gateway event listening**: Monitors AutoModeration Action Execution events
- **Configurable responses**: Maps keywords to message templates via `src/config/automod-messages.json`
- **User mentions**: Supports `{user}` placeholder
---

## caclawphony (6 stars)

### Problem & Solution
The OpenClaw main repository has a massive volume of PRs, requiring an automated PR triage, review, and merge pipeline while preserving human approval checkpoints.

caclawphony is based on the Symphony framework, transforming a Linear project board into an AI agent dispatch system:
- **Multi-stage pipeline**: Triage -> Review -> Prepare -> Merge
- **Human checkpoints**: Maintainer approval required between each stage
- **Cluster detection**: Automatically identifies duplicate PRs and related Issues
- **GitHub status sync**: Checks `gh pr reviews` to determine if changes have been requested

### Key Features
- **State machine design**:
  - Agent states: Triage, Review, Prepare, Merge, Request Changes, Closure
  - Human gate states: Todo, Review Complete, Prepare Complete
  - Terminal states: Done, Duplicate
- **Symphony integration**:
  - `after_create` hook: Workspace setup, skill copying, repository cloning
  - `before_run` hook: Branch switching
  - Jinja templates: Prompt templates for each state
- **Resource constraints**: Prepare state allows maximum 1 concurrent task (to avoid conflicts)
- **Duplicate detection**: Runs `pr-plan --live` to refresh cache, then `pr-cluster` for multi-signal search
---

## trust (29 stars)

### Problem & Solution
OpenClaw needs a publicly transparent threat model and security plan to build user trust.

The trust repository is based on the MITRE ATLAS framework, providing:
- Structured threat model (threats.yaml)
- Attack chain and trust boundary documentation
- Public vulnerability reporting process

### Key Features
- **MITRE ATLAS framework**: Specifically designed for AI/ML system threat modeling
- **Rendered site**: https://trust.openclaw.ai/trust/threatmodel
- **Contribution guide**: CONTRIBUTING.md explains how to submit threats and attack chains
---

## casa (29 stars)

### Problem & Solution
HomeKit data is locked within the Apple ecosystem, making it inaccessible to automation and AI Agents.

casa is a Mac Catalyst app providing:
- Local REST API (localhost only)
- HomeKit data read/write
- Built-in CLI tool

### Key Features
- **Local-first**: Binds only to 127.0.0.1, no remote access
- **Optional HomeKit**: Disabled by default, requires manual user activation
- **CLI integration**: `casa devices`, `casa characteristics set <uuid> true`
- **Sparkle auto-update**: Uses EdDSA signing
---

## maintainers (28 stars)

### Problem & Solution
New maintainers joining the OpenClaw team need to quickly understand workflows, security standards, and best practices.

The maintainers repository provides:
- New maintainer survival guide
- PR workflow (Review -> Prepare -> Merge)
- Security hardening checklist
- Common commands and resource links

### Key Features
- **Security first**:
  - Enable 2FA (authenticator app, disable SMS)
  - GPG-signed commits
  - YubiKey/FIDO2 hardware keys
  - Password manager
  - Watch out for phishing and social engineering attacks
- **PR workflow**:
  - Start with `size:xs`
  - Use `/reviewpr` for AI review
  - Run gates: `pnpm lint && pnpm build && pnpm test`
  - Update CHANGELOG.md
  - Use `/landpr` or `/mergepr` to merge
- **Cluster thinking**: Don't handle PRs individually; use Codex to search related PRs and Issues, resolving the entire cluster at once
- **Do's and Don'ts**:
  - Don't: `@ts-nocheck`, disable lint rules, use bun, skip tests
  - Must: Rebase before merge, thank contributors, announce major changes in `#maintainers`
---

## nix-steipete-tools (28 stars)

### Problem & Solution
OpenClaw needs to integrate a series of third-party tools (screenshots, TTS, messaging, etc.), but installing and version-managing these tools is complex.

nix-steipete-tools packages Peter Steinberger's tools as Nix flakes with OpenClaw plugin metadata:
- Reproducible builds
- Declarative installation
- Automatic freshness
- Skill document integration

### Key Features
- **10 tools**:
  - summarize (link -> summary)
  - gogcli (Google CLI)
  - goplaces (Google Places API)
  - camsnap (RTSP/ONVIF camera screenshots)
  - sonoscli (Sonos control)
  - bird (X/Twitter CLI)
  - peekaboo (macOS screenshots + AI vision analysis)
  - poltergeist (file monitoring + auto-rebuild)
  - sag (ElevenLabs TTS)
  - imsg (iMessage/SMS CLI)
- **Dual-mode usage**:
  - As an openclawPlugin (includes skill documents)
  - As a pure Nix package (binaries only)
- **Auto-sync**:
  - Skill documents synced from openclaw/openclaw main branch (every 30 minutes)
  - Tool versions updated from GitHub releases (every 10 minutes)
---

## butter.bot (9 stars)

### Problem & Solution
(No README, project purpose unknown)

Based on the project name, this is likely a simple Discord bot or automation tool.
---

## flawd-bot (31 stars)

### Problem & Solution
(No README, project purpose unknown)

Based on the project name "evil twin bot," this is likely an adversarial bot used for testing or demonstrations.
---

## .github (6 stars)

### Problem & Solution
A GitHub organization needs a unified README, contribution guide, and Issue/PR templates.

The .github repository provides:
- Organization-level README (displayed at https://github.com/openclaw)
- Default CONTRIBUTING.md
- Issue and PR templates

### Key Features
- **Organization-level configuration**: All repositories inherit these default files
- **Unified branding**: Ensures a consistent contribution workflow across all repositories
---

## voice-community (4 stars)

### Problem & Solution
(No README, project purpose unknown)

Based on the project name, this is likely related to OpenClaw's voice community features.
---

## Summary

OpenClaw's small projects demonstrate the following design philosophies:

1. **Declarative first**: nix-openclaw and clawdinators both emphasize configuration-as-code and reproducible deployment
2. **Automation-driven**: CI auto-updates, self-updating systems, automated PR pipelines
3. **Transparent governance**: community and trust repositories publicly share all policies and threat models
4. **Human checkpoints**: caclawphony's multi-stage pipeline balances automation with human approval
5. **Tool ecosystem**: nix-steipete-tools, casa, hermit, and other tools extend OpenClaw's capability boundaries
