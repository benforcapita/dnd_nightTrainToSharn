#!/usr/bin/env python3
"""
Combine all markdown files from the NightTrainToSharn vault into a single
well-structured .txt document for NotebookLM import.

Output: sync-output/NightTrainToSharn_NotebookLM.txt
"""

import os
import re
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path("/Users/benblum/Documents/NightTrainToSharn")
OUTPUT_DIR = VAULT_ROOT / "sync-output"
EXCLUDE_DIRS = {".obsidian", ".git", "node_modules", ".sync-tools", "sync-output", "vault", "worldbuilding-expander"}

def clean_filename(name: str) -> str:
    """Strip leading numeric prefixes like '01 - ' for cleaner display."""
    return re.sub(r'^\d+\s*-\s*', '', name)

def is_markdown_file(path: Path) -> bool:
    return path.suffix == '.md'

def should_exclude(path: Path) -> bool:
    parts = set(path.relative_to(VAULT_ROOT).parts)
    return bool(parts & EXCLUDE_DIRS)

def gather_files() -> list[Path]:
    files = []
    for md in VAULT_ROOT.rglob("*.md"):
        if should_exclude(md):
            continue
        files.append(md)
    files.sort()
    return files

def combine_files(files: list[Path]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("NIGHT TRAIN TO SHARN — Complete Campaign Vault")
    lines.append(f"Synced: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Files: {len(files)}")
    lines.append("=" * 72)
    lines.append("")

    current_folder = None

    for fpath in files:
        rel = fpath.relative_to(VAULT_ROOT)
        folder = str(rel.parent) if str(rel.parent) != "." else "Root"

        # Folder header when we enter a new folder
        if folder != current_folder:
            current_folder = folder
            clean_folder = clean_filename(folder)
            lines.append("")
            lines.append("#" * 60)
            lines.append(f"  {clean_folder}")
            lines.append("#" * 60)
            lines.append("")

        # File header
        title = clean_filename(fpath.stem)
        lines.append("-" * 50)
        lines.append(f"  {title}")
        lines.append("-" * 50)
        lines.append("")

        # File content
        try:
            content = fpath.read_text(encoding="utf-8")
            # Strip YAML frontmatter if present
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            lines.append(content.strip())
        except Exception as e:
            lines.append(f"[Error reading file: {e}]")

        lines.append("")
        lines.append("")

    # Table of contents at the end
    lines.append("")
    lines.append("#" * 60)
    lines.append("  TABLE OF CONTENTS")
    lines.append("#" * 60)
    lines.append("")
    for fpath in files:
        rel = fpath.relative_to(VAULT_ROOT)
        folder = clean_filename(str(rel.parent)) if str(rel.parent) != "." else "Root"
        title = clean_filename(fpath.stem)
        lines.append(f"  [{folder}]  {title}")

    return "\n".join(lines)

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    files = gather_files()
    
    if not files:
        print("No markdown files found.")
        return

    print(f"Found {len(files)} markdown files.")

    combined = combine_files(files)
    
    out_path = OUTPUT_DIR / "NightTrainToSharn_NotebookLM.txt"
    out_path.write_text(combined, encoding="utf-8")
    
    # Word count
    words = len(combined.split())
    print(f"Output: {out_path}")
    print(f"Words: {words:,}  (NotebookLM limit: 500,000)")
    print("Ready for NotebookLM import.")

if __name__ == "__main__":
    main()
