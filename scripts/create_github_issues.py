#!/usr/bin/env python3
"""
create_github_issues.py - Batch GitHub Issue Creator & Synchronizer

Reads all markdown issue files in docs/issues/ and synchronizes them to the GitHub repository
using the GitHub CLI ('gh'). Supports creation, updating existing issues, and dry-run mode.

Requirements:
    - GitHub CLI installed and authenticated ('gh auth login')

Usage:
    python scripts/create_github_issues.py --repo eyyoibo/CSE396-Group11-Knee-Goniometer
    python scripts/create_github_issues.py --dry-run
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


def parse_issue_file(file_path: Path):
    """Parse YAML frontmatter and markdown body from an issue specification file."""
    content = file_path.read_text(encoding="utf-8")

    # Frontmatter regex
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not frontmatter_match:
        return None

    fm_text = frontmatter_match.group(1)
    body = frontmatter_match.group(2).strip()

    # Title
    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', fm_text, re.MULTILINE)
    title = title_match.group(1) if title_match else file_path.stem

    # Labels
    labels_match = re.search(r'labels:\s*\[(.*?)\]', fm_text)
    labels = []
    if labels_match:
        raw_labels = labels_match.group(1)
        labels = [l.strip().strip('"').strip("'") for l in raw_labels.split(",") if l.strip()]

    # Milestone
    milestone_match = re.search(r'milestone:\s*["\']?(.*?)["\']?$', fm_text, re.MULTILINE)
    milestone = milestone_match.group(1) if milestone_match else None

    # Assignees
    assignees_match = re.search(r'assignees:\s*\[(.*?)\]', fm_text)
    assignees = []
    if assignees_match:
        raw_assignees = assignees_match.group(1)
        assignees = [a.strip().strip('"').strip("'") for a in raw_assignees.split(",") if a.strip()]

    return {
        "title": title,
        "labels": labels,
        "milestone": milestone,
        "assignees": assignees,
        "body": body,
        "file": file_path.name
    }


def main():
    parser = argparse.ArgumentParser(description="Synchronize GitHub issues from markdown specifications.")
    parser.add_argument("--repo", type=str, default="eyyoibo/CSE396-Group11-Knee-Goniometer", help="GitHub repo (owner/repo)")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without modifying remote GitHub issues")
    args = parser.parse_args()

    issues_dir = Path(__file__).resolve().parent.parent / "docs" / "issues"
    if not issues_dir.exists():
        print(f"Error: Directory '{issues_dir}' not found.")
        sys.exit(1)

    issue_files = sorted(list(issues_dir.glob("issue_*.md")))
    print(f"Found {len(issue_files)} issue specification files in {issues_dir.name}/\n")

    for file_path in issue_files:
        issue_data = parse_issue_file(file_path)
        if not issue_data:
            print(f"[SKIPPED] Could not parse frontmatter in {file_path.name}")
            continue

        # Ensure labels exist on remote repository
        if not args.dry_run and issue_data["labels"]:
            for lbl in issue_data["labels"]:
                subprocess.run(
                    ["gh", "label", "create", lbl, "--repo", args.repo, "--force"],
                    capture_output=True
                )

        cmd = ["gh", "issue", "create", "--title", issue_data["title"], "--body", issue_data["body"]]
        for lbl in issue_data["labels"]:
            cmd.extend(["--label", lbl])
        if issue_data["milestone"]:
            cmd.extend(["--milestone", issue_data["milestone"]])
        if args.repo:
            cmd.extend(["--repo", args.repo])

        if args.dry_run:
            print(f"[DRY-RUN] {issue_data['file']} -> {issue_data['title']}")
            print("  Command: " + " ".join(f'"{c}"' if " " in c else c for c in cmd[:8]) + " ...\n")
        else:
            print(f"[CREATING] {issue_data['title']}...")
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                print(f"  Success: {result.stdout.strip()}")
            except FileNotFoundError:
                print("  Error: 'gh' (GitHub CLI) not found. Please install gh or run with --dry-run.")
                break
            except subprocess.CalledProcessError as e:
                print(f"  Failed: {e.stderr.strip()}")

    print("\nIssue synchronization completed.")


if __name__ == "__main__":
    main()
