#!/usr/bin/env python3
"""
create_github_issues.py - GitHub Issues Toplu Olusturucu

docs/issues/ klasorundeki tum markdown issue dosyalarini okur ve
GitHub CLI ('gh') kullanarak depoya otomatik olarak issue acar.

Gereksinim:
    - GitHub CLI kurulu ve giris yapilmis olmali ('gh auth login')

Kullanim:
    python scripts/create_github_issues.py --repo <kullanici-adi>/<repo-adi>
    python scripts/create_github_issues.py --dry-run
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


def parse_issue_file(file_path: Path):
    """Markdown dosyasindaki frontmatter ve govdeyi ayristirir."""
    content = file_path.read_text(encoding="utf-8")
    
    # Frontmatter regex
    frontmatter_match = re.search(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not frontmatter_match:
        return None
    
    fm_text = frontmatter_match.group(1)
    body = frontmatter_match.group(2).strip()
    
    # Baslik
    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', fm_text, re.MULTILINE)
    title = title_match.group(1) if title_match else file_path.stem
    
    # Etiketler
    labels_match = re.search(r'labels:\s*\[(.*?)\]', fm_text)
    labels = []
    if labels_match:
        raw_labels = labels_match.group(1)
        labels = [l.strip().strip('"').strip("'") for l in raw_labels.split(",") if l.strip()]
        
    # Milestone
    milestone_match = re.search(r'milestone:\s*["\']?(.*?)["\']?$', fm_text, re.MULTILINE)
    milestone = milestone_match.group(1) if milestone_match else None
    
    return {
        "title": title,
        "labels": labels,
        "milestone": milestone,
        "body": body,
        "file": file_path.name
    }


def main():
    parser = argparse.ArgumentParser(description="GitHub issue dosyalarini depoya yukler.")
    parser.add_argument("--repo", type=str, help="GitHub repo (ornek: dogan/knee-goniometer)")
    parser.add_argument("--dry-run", action="store_true", help="Gercekte olusturma, sadece komutlari yazdir")
    args = parser.parse_args()

    issues_dir = Path(__file__).resolve().parent.parent / "docs" / "issues"
    if not issues_dir.exists():
        print(f"Hata: {issues_dir} dizini bulunamadi.")
        sys.exit(1)

    issue_files = sorted(list(issues_dir.glob("issue_*.md")))
    print(f"Toplam {len(issue_files)} adet issue dosyasi bulundu.\n")

    # Zaten olusturulanlar: issue_01, issue_02, issue_03, issue_04
    already_created = ["issue_01_pcnt_driver.md", "issue_02_differential_receiver.md", "issue_03_bluetooth_spp.md", "issue_04_angle_calculation_fw.md"]

    for file_path in issue_files:
        if file_path.name in already_created:
            continue

        issue_data = parse_issue_file(file_path)
        if not issue_data:
            print(f"[ATLANDI] {file_path.name} ayrıştırılamadı.")
            continue

        # Eksik etiketleri repo uzerinde olustur
        for lbl in issue_data["labels"]:
            if not args.dry_run:
                subprocess.run(["gh", "label", "create", lbl, "--repo", args.repo or "eyyoibo/CSE396-Group11-Knee-Goniometer", "--force"], capture_output=True)

        cmd = ["gh", "issue", "create", "--title", issue_data["title"], "--body", issue_data["body"]]
        
        if issue_data["labels"]:
            for lbl in issue_data["labels"]:
                cmd.extend(["--label", lbl])
        if args.repo:
            cmd.extend(["--repo", args.repo])

        if args.dry_run:
            print(f"[DRY-RUN] {issue_data['file']} -> {issue_data['title']}")
            print("  Komut: " + " ".join(f'"{c}"' if " " in c else c for c in cmd[:8]) + " ...\n")
        else:
            print(f"[YUKLENIYOR] {issue_data['title']}...")
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                print(f"  Basarili: {result.stdout.strip()}")
            except FileNotFoundError:
                print("  Hata: 'gh' (GitHub CLI) bulunamadi. Lutfen GitHub CLI yukleyin veya --dry-run ile komutlari gorun.")
                break
            except subprocess.CalledProcessError as e:
                print(f"  Hata olustu: {e.stderr.strip()}")

    print("\nIslem tamamlandi.")


if __name__ == "__main__":
    main()
