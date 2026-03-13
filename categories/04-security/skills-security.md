> https://github.com/UseAI-pro/skills-security

# UseAI-pro/openclaw-skills-security (25 stars)

## Problem & Solution

The OpenClaw ecosystem lacks a security review mechanism for skill installation. Malicious skills can steal credentials, plant backdoors, or carry out supply chain attacks (such as the ClawHavoc incident). This project provides two audit skills (skill-auditor for reviewing skills, setup-auditor for reviewing environments) and 11 reusable security modules, covering detection of 12 real-world attack types.

## Key Features

- **Dual Auditor Architecture** -- skill-auditor executes a 6-step protocol (metadata/typosquat check -> permission analysis -> dependency audit -> prompt injection scan -> network/data exfiltration analysis -> content red flags); setup-auditor executes a 4-step protocol (credential scan -> configuration hardening -> sandbox readiness -> persistence check)
- **Comprehensive Threat Coverage** -- Covers 12/12 real-world attack types (typosquatting, credential theft, crypto miners, reverse shells, prompt injection, skill loader exploits, obfuscated commands, supply chain attacks, social engineering, persistence, excessive permissions, data exfiltration)
- **Risk Rating System** -- Outputs four-tier verdicts: SAFE / SUSPICIOUS / DANGEROUS / BLOCK, with specific findings and remediation recommendations
- **Zero-Dependency Design** -- Pure Markdown instruction modules (SKILL.md) that can be pasted into any LLM (Codex CLI / Claude Code / OpenClaw) or browser tool (UseClawPro Verifier)
- **Guided Environment Audit** -- setup-auditor collects information through 5 questions (workspace path, host agent, permissions, sandbox, ports) and generates a customized remediation checklist
- **Community-Driven** -- Maintained by UseClawPro (UseAI.pro), providing an online verification tool and a verified skill directory
