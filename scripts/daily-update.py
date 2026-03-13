#!/usr/bin/env python3
"""Daily updater: fetch latest stars/status from GitHub API, update projects.json, append update-log.

Usage:
    GITHUB_TOKEN=ghp_xxx python scripts/daily-update.py

Environment:
    GITHUB_TOKEN - GitHub personal access token (optional but recommended for rate limits)
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "projects.json"
LOG_PATH = ROOT / "update-log.md"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
API_BASE = "https://api.github.com"
INACTIVE_DAYS = 180  # Mark as inactive if no push in 180 days


def github_get(path: str) -> dict | None:
    """Make an authenticated GET request to GitHub API."""
    url = f"{API_BASE}{path}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "openclaw-landscape-updater",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        if e.code == 404:
            return {"archived": True, "message": "Not Found"}
        if e.code == 403:
            print(f"  Rate limited. Sleeping 60s...")
            time.sleep(60)
            try:
                with urlopen(req, timeout=15) as resp:
                    return json.loads(resp.read())
            except Exception:
                return None
        print(f"  HTTP {e.code} for {path}")
        return None
    except Exception as e:
        print(f"  Error fetching {path}: {e}")
        return None


def update_project(project: dict) -> dict[str, str]:
    """Update a single project from GitHub API. Returns dict of changes."""
    repo = project["repo"]
    data = github_get(f"/repos/{repo}")
    if data is None:
        return {}

    changes = {}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Check if repo was deleted/not found
    if data.get("message") == "Not Found":
        if not project.get("archived"):
            project["archived"] = True
            project["status"] = "archived"
            changes["status"] = "archived (repo not found)"
        project["last_updated"] = today
        return changes

    # Update stars
    new_stars = data.get("stargazers_count", project["stars"])
    if new_stars != project["stars"]:
        changes["stars"] = f"{project['stars']} -> {new_stars}"
        project["stars"] = new_stars

    # Update archived status
    if data.get("archived", False) and not project.get("archived"):
        project["archived"] = True
        project["status"] = "archived"
        changes["status"] = "archived"
    elif not data.get("archived", False) and project.get("archived"):
        project["archived"] = False
        changes["status"] = "unarchived"

    # Check activity (pushed_at)
    pushed_at = data.get("pushed_at", "")
    if pushed_at:
        try:
            last_push = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            days_since = (now - last_push).days
            if days_since > INACTIVE_DAYS and project.get("status") == "active":
                project["status"] = "inactive"
                changes["status"] = f"inactive ({days_since}d since last push)"
            elif days_since <= INACTIVE_DAYS and project.get("status") == "inactive":
                project["status"] = "active"
                changes["status"] = "reactivated"
        except (ValueError, TypeError):
            pass

    # Update language if missing
    if not project.get("language") and data.get("language"):
        project["language"] = data["language"]
        changes["language"] = data["language"]

    # Update license if missing
    if not project.get("license") and data.get("license", {}).get("spdx_id"):
        project["license"] = data["license"]["spdx_id"]
        changes["license"] = data["license"]["spdx_id"]

    project["last_updated"] = today
    return changes


def append_update_log(added: list, updated: dict[str, dict], removed: list):
    """Append today's changes to update-log.md."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    entry_lines = [f"## {today}", ""]

    has_content = False

    if added:
        has_content = True
        entry_lines.append(f"### Added ({len(added)})")
        for p in added:
            entry_lines.append(f"- [{p['repo']}](https://github.com/{p['repo']}) -> {p['category']}")
        entry_lines.append("")

    if updated:
        has_content = True
        entry_lines.append(f"### Updated ({len(updated)})")
        for repo, changes in sorted(updated.items()):
            parts = [f"{k}: {v}" for k, v in changes.items()]
            entry_lines.append(f"- {repo}: {', '.join(parts)}")
        entry_lines.append("")

    if removed:
        has_content = True
        entry_lines.append(f"### Removed ({len(removed)})")
        for repo in removed:
            entry_lines.append(f"- {repo}")
        entry_lines.append("")

    if not has_content:
        entry_lines.append("No changes detected.")
        entry_lines.append("")

    entry_lines.append("---")
    entry_lines.append("")

    # Read existing log
    if LOG_PATH.exists():
        existing = LOG_PATH.read_text()
        # Insert after header
        if existing.startswith("# Update Log"):
            header_end = existing.index("\n\n", existing.index("# Update Log")) + 2
            new_content = existing[:header_end] + "\n".join(entry_lines) + "\n" + existing[header_end:]
        else:
            new_content = "# Update Log\n\n" + "\n".join(entry_lines) + "\n" + existing
    else:
        new_content = "# Update Log\n\n" + "\n".join(entry_lines) + "\n"

    LOG_PATH.write_text(new_content)


def main():
    if not DATA_PATH.exists():
        print(f"Error: {DATA_PATH} not found. Run generate.py first.")
        sys.exit(1)

    projects = json.loads(DATA_PATH.read_text())
    print(f"Loaded {len(projects)} projects")

    if not GITHUB_TOKEN:
        print("WARNING: No GITHUB_TOKEN set. Rate limit is 60 req/hour (unauthenticated).")
        print("Set GITHUB_TOKEN for 5000 req/hour.\n")

    all_changes: dict[str, dict] = {}
    total = len(projects)

    for i, project in enumerate(projects, 1):
        repo = project["repo"]
        print(f"  [{i}/{total}] {repo}...", end=" ", flush=True)
        changes = update_project(project)
        if changes:
            all_changes[repo] = changes
            print(f"CHANGED: {changes}")
        else:
            print("ok")

        # Rate limiting: ~0.8s between requests
        if i < total:
            time.sleep(0.8)

    # Save updated projects.json
    DATA_PATH.write_text(json.dumps(projects, indent=2, ensure_ascii=False) + "\n")
    print(f"\nUpdated {len(all_changes)} projects, saved to {DATA_PATH}")

    # Append to update log
    append_update_log(added=[], updated=all_changes, removed=[])
    print(f"Updated {LOG_PATH}")

    # Regenerate Markdown files
    print("\nRegenerating Markdown files...")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "generate.py")], check=True)

    print(f"\nDone! {len(all_changes)} changes.")


if __name__ == "__main__":
    main()
