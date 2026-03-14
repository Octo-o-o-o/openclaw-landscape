> https://github.com/prompt-security/clawsec

# ClawSec (709 stars)

## Problem & Solution

ClawSec addresses the lack of security protection in AI Agent cognitive architectures. Through a comprehensive security skill suite (Suite Installer), it provides OpenClaw/NanoClaw Agents with file integrity protection (drift detection and automatic recovery for critical files like SOUL.md/IDENTITY.md), real-time security advisories (NVD CVE polling + community threat intelligence), security auditing (prompt injection marker detection), checksum verification (SHA256), and health checks (automatic updates and integrity verification), defending against prompt injection, drift, and malicious instructions.

## Key Features

- **One-Click Suite Installation** -- `npx clawhub@latest install clawsec-suite` installs all security skills with integrity verification
- **File Integrity Protection (soul-guardian)** -- Drift detection + automatic recovery of critical Agent files (SOUL.md/IDENTITY.md/POLICIES.yaml, etc.), preventing prompt injection tampering
- **Real-Time Security Advisories** -- Automated NVD CVE polling (GitHub Actions scheduled tasks) + community threat intelligence, pushed to Agent
- **Security Audit Scripts** -- Self-inspection scripts detecting prompt injection markers and vulnerabilities (e.g., `<!-- INJECTED -->`, anomalous instructions)
- **Checksum Verification** -- SHA256 checksums provided for all skill artifacts, preventing supply chain attacks
- **Health Checks** -- Automatic updates and integrity verification for all installed skills
- **NanoClaw Platform Support** -- Containerized WhatsApp bot security, MCP tools providing advisory monitoring, signature verification, and file integrity checks
- **Cross-Platform Shell Compatibility** -- POSIX shell workflows (Linux/macOS) + PowerShell support (Windows), with explicit home variable expansion rules

<!-- lastCommit: 277c0ab -->
