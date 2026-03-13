> https://github.com/knownsec/openclaw-security

# OpenClaw Security Guide by Knownsec (55 stars)

## Problem & Solution
The rapid growth of OpenClaw has been accompanied by serious security risks. ZoomEye data shows 63,026 identifiable instances worldwide, and the GitHub Advisory Database records 245 related vulnerabilities. Knownsec has published a full-lifecycle security practice guide covering installation, configuration, usage, and maintenance.

## Key Features
- **Secure Installation Checklist** -- Download from trusted sources, deploy in isolated environments (VPS > VM > Docker), principle of least privilege, regular upgrades, configuration backups
- **Configuration Security Audit** -- Minimize exposure (local mode + firewall deny on port 18789), enable token authentication, regularly run `openclaw security audit --deep`
- **Skill Review Rules** -- Check for arbitrary shell execution, filesystem writes, network requests to unknown domains, environment variable access, Base64-encoded code, dynamic code execution
- **Daily Inspection Scripts** -- Check Gateway port binding (`ss -lntp`), anonymous access verification, root identity run check, firewall policy verification
- **Incident Response Procedures** -- Emergency handling steps for system anomalies (lag, traffic anomalies, high CPU/memory)
- **Bilingual Documentation** -- Localized security guide for the Chinese market in both Chinese and English
