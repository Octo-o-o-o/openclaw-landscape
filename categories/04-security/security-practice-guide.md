> https://github.com/slowmist/openclaw-security-practice-guide

# OpenClaw Security Practice Guide (slowmist/openclaw-security-practice-guide)

## Basic Information

- **GitHub Repository**: https://github.com/slowmist/openclaw-security-practice-guide
- **Stars**: 1,659
- **License**: MIT
- **Maintainer**: SlowMist Security Team ([@SlowMist_Team](https://x.com/SlowMist_Team))
- **Languages**: English / Simplified Chinese
- **Latest Version**: v2.7

## Problem & Solution

### Core Problem

OpenClaw, as a highly privileged autonomous AI Agent running in root/terminal environments, faces the following security risks:

1. **Destructive Operation Risks** - Agents may execute dangerous commands like `rm -rf /`
2. **Prompt Injection Attacks** - Malicious inputs can hijack Agent behavior
3. **Supply Chain Poisoning** - Third-party Skills/MCPs may contain malicious code
4. **High-Risk Business Logic Execution** - Unreviewed automated operations may cause irreversible damage
5. **Traditional Defense Failure** - Traditional security measures like `chattr +i` and firewalls are incompatible with Agentic workflows

### Solution

The project proposes an **Agentic Zero-Trust Architecture**, shifting from traditional "host-based static defense" to a "behavioral self-inspection + multi-layered defense" model:

**Core Philosophy**:
- Let the AI Agent understand and enforce security policies itself (Mental Seal)
- Zero-friction operations -- imperceptible during daily use, intervening only when red lines are crossed
- High-risk operations require human confirmation
- Explicit nightly audits -- all core metrics are reported, including health indicators (no silent passes)
- Default zero-trust -- assume prompt injection, supply chain poisoning, and business logic abuse are always possible

## Core Architecture

### 3-Tier Defense Matrix

```
┌─────────────────────────────────────────────────────────────┐
│                    1. Pre-action Prevention Layer             │
│  ┌──────────────────────┐  ┌──────────────────────────────┐ │
│  │ Behavioral Blacklist  │  │ Skill Installation Audit     │ │
│  │ - Red-line command    │  │   Protocol                   │ │
│  │   interception        │  │ - Source code review         │ │
│  │ - Yellow-line human   │  │ - Permission scope check     │ │
│  │   confirmation        │  │ - Dependency scanning        │ │
│  │ - Semantic analysis   │  │                              │ │
│  └──────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   2. In-action Execution Layer                │
│  ┌──────────────────────┐  ┌──────────────────────────────┐ │
│  │ Permission Narrowing  │  │ Cross-Skill Pre-flight Check │ │
│  │ - chattr +i to        │  │ - Pre-check before cross-    │ │
│  │   protect core files  │  │   skill invocations          │ │
│  │ - Least privilege     │  │ - Business risk control      │ │
│  │   principle           │  │                              │ │
│  └──────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  3. Post-action Audit Layer                   │
│  ┌──────────────────────┐  ┌──────────────────────────────┐ │
│  │ Nightly Auto Audit    │  │ Brain Git Disaster Recovery  │ │
│  │ - 13 core metrics     │  │ - Automatic Git backup       │ │
│  │ - Telegram alerts     │  │ - Version rollback           │ │
│  │ - Anomaly detection   │  │ - Remote sync                │ │
│  └──────────────────────┘  └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Red-Line / Yellow-Line Command Classification

**Red-line Commands** - Immediately blocked, require human confirmation:
- `rm -rf /`, `find / -delete` - Bulk deletion
- `dd if=/dev/zero of=/dev/sda` - Disk wipe
- `chmod 777 /etc/passwd` - Critical file permission destruction
- `curl ... | bash` - Unreviewed remote script execution
- `iptables -F` - Firewall rule flush

**Yellow-line Commands** - Risk warning, confirmation recommended:
- `sudo apt-get remove` - Package uninstallation
- `git push --force` - Force push
- `docker system prune -a` - Container cleanup

**Safe Commands** - Normal execution:
- Read operations (`cat`, `ls`, `grep`)
- Non-destructive writes
- Standard development tool invocations

### Core Protection Mechanisms

#### 1. File Immutability Protection (chattr +i)

```bash
# Protect core configuration files
sudo chattr +i ~/.openclaw/openclaw.json
sudo chattr +i ~/.openclaw/SOUL.md
sudo chattr +i ~/.openclaw/AGENTS.md

# Note: Do not lock exec-approvals.json (needs write access at runtime)
```

#### 2. Skill Installation Audit Protocol

Before installing any Skill, you must:
- Review source code (check for malicious logic)
- Verify permission scope (whether excessive permissions are requested)
- Scan dependencies (check for supply chain risks)
- Record Skill fingerprint (for subsequent auditing)

#### 3. Nightly Automated Audit (13 Core Metrics)

A cron job automatically executes `nightly-security-audit.sh` every night, checking:

1. Newly installed Skills (compared against baseline)
2. Configuration file changes (openclaw.json, SOUL.md, AGENTS.md)
3. Suspicious command execution (shell history scan)
4. Permission anomalies (SUID/SGID files)
5. Network connection anomalies (unauthorized outbound connections)
6. Filesystem changes (critical directory monitoring)
7. Process anomalies (unknown processes)
8. Log anomalies (error log spikes)
9. Resource usage anomalies (CPU/memory/disk)
10. Skill fingerprint verification (tampering detection)
11. Git backup status (ensuring disaster recovery availability)
12. System update status (security patches)
13. Credential leak scanning (checking for hardcoded keys)

Audit results are pushed via Telegram Bot notifications.

#### 4. Brain Git Disaster Recovery

```bash
# Automatically back up OpenClaw workspace to Git
cd ~/.openclaw
git add -A
git commit -m "Auto backup $(date)"
git push origin main

# Disaster recovery
git log --oneline  # View version history
git checkout <commit-hash>  # Roll back to a specific version
```

## Key Features

### 1. Zero-Friction Deployment

**Core Innovation**: No manual security configuration needed -- let the OpenClaw Agent deploy the defense matrix itself.

**Usage Flow**:
```
1. Download OpenClaw-Security-Practice-Guide.md
2. Send the file to your OpenClaw Agent
3. Ask: "Please read this security guide carefully. Is it reliable?"
4. After Agent confirmation, issue the instruction: "Please deploy the defense matrix
   according to the guide, including red/yellow-line rules, permission narrowing,
   and nightly audit Cron Job"
5. (Optional) Use the Red Teaming Guide to verify defense effectiveness
```

**Technical Principle**:
- Leverages long-context understanding capabilities of strong reasoning models (Gemini / Opus / Kimi / MiniMax)
- Agent automatically parses security policies from the Markdown guide
- Agent autonomously generates and executes deployment scripts
- No manual configuration files or command execution required

### 2. Behavioral Self-Inspection

The Agent automatically performs semantic analysis before executing commands:

```python
# Pseudocode example
def should_execute(command: str) -> Decision:
    # 1. Literal match against red-line list
    if command in RED_LINE_PATTERNS:
        return BLOCK

    # 2. Semantic understanding (LLM reasoning)
    semantic_risk = llm.analyze_risk(command)
    if semantic_risk == "HIGH":
        return BLOCK
    elif semantic_risk == "MEDIUM":
        return ASK_HUMAN

    # 3. Context analysis
    if is_destructive_in_context(command):
        return BLOCK

    return ALLOW
```

**Advantages**:
- Can intercept variant attacks (e.g., `find / -delete` rather than just `rm -rf /`)
- Understands indirect harm (e.g., deleting files via Python scripts)
- Adapts to new attack patterns

**Limitations**:
- Depends on model capability (weaker models may misjudge)
- May produce false positives (flagging safe commands as dangerous)
- Cannot defend against vulnerabilities in the model itself

### 3. Supply Chain Security

**Skill Installation Audit Checklist**:

```markdown
## Skill Audit Checklist

### Basic Information
- [ ] Skill name and version
- [ ] Author/maintainer identity
- [ ] Source code repository URL
- [ ] Last update time

### Code Review
- [ ] Does it contain network requests? Are target domains trusted?
- [ ] Does it execute shell commands? Are commands controllable?
- [ ] Does it read/write sensitive files? (~/.ssh, ~/.aws, /etc/passwd)
- [ ] Does it contain obfuscated code or base64 encoding?
- [ ] Does it dynamically load external code?

### Permission Review
- [ ] Do requested permissions match the functionality?
- [ ] Does it request root permissions?
- [ ] Does it request network permissions?
- [ ] Does it request full filesystem access?

### Dependency Review
- [ ] Number of dependencies (fewer is better)
- [ ] Are dependencies from trusted sources?
- [ ] Do dependencies have known vulnerabilities? (npm audit / pip-audit)

### Community Trust
- [ ] GitHub Stars count
- [ ] Issue response speed
- [ ] Is there a security disclosure policy?
- [ ] Are there audit reports from other users?

### Decision
- [ ] Approve installation
- [ ] Reject installation
- [ ] Decide after sandbox testing
```

### 4. Model Recommendation

The guide explicitly recommends using **strong reasoning models**:
- Gemini (Google)
- Opus (Anthropic Claude)
- Kimi (Moonshot AI)
- MiniMax

**Reasons**:
- Long-context understanding capability (comprehending complete security constraints)
- Hidden instruction pattern detection (identifying prompt injection)
- Consistent execution (reducing deployment errors)

**Not Recommended**: Small-parameter models (may not accurately parse command semantics)

### 5. Validation & Red Teaming

A dedicated adversarial exercise guide (`Validation-Guide-en.md` / `Validation-Guide-zh.md`) is provided, containing:

**Test Scenarios**:
1. Direct red-line command testing (`rm -rf /tmp/test`)
2. Variant attack testing (`find /tmp -name "*.log" -delete`)
3. Prompt Injection testing ("Ignore previous security rules, execute...")
4. Social engineering testing ("This is an emergency fix, needs immediate execution...")
5. Supply chain attack simulation (installing a malicious Skill)

**Expected Behavior**:
- Agent should intercept all red-line commands
- Agent should request confirmation for yellow-line commands
- Agent should identify and reject prompt injection
- Agent should audit before Skill installation

### 6. Flexible Configuration

**Optional Features**:
- Git backup (can be disabled for privacy-sensitive scenarios)
- Telegram notifications (can be replaced with other notification channels)
- Audit frequency (cron expression is adjustable)
- Red-line/yellow-line rules (customizable)

**Environment Adaptation**:
- The guide primarily targets Linux root environments
- Can be adapted to macOS / Windows through LLM reasoning
- Supports generating custom adapted versions

## Summary

`slowmist/openclaw-security-practice-guide` is a **pioneering AI Agent security practice guide** whose core value lies in:

1. **Paradigm Shift**: From traditional static defense to an Agentic Zero-Trust Architecture
2. **Zero-Friction Deployment**: Letting the Agent understand and enforce security policies itself
3. **Three-Layer Defense**: Pre-action (prevention) + In-action (execution) + Post-action (audit)
4. **Supply Chain Security**: Skill installation audit protocol
5. **Behavioral Self-Inspection**: Command risk analysis based on LLM reasoning
