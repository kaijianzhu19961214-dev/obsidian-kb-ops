#!/usr/bin/env python3
"""Read-only Obsidian KB audit for the personal vault."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_VAULT = Path("/Users/zhukaijian/Documents/Obsidian Vault")
CORE_FOLDERS = (
    "00_Inbox",
    "10_Projects",
    "20_Areas",
    "30_Resources",
    "40_Permanent",
    "50_MOCs",
    "60_Daily",
    "90_Archive",
    "99_Templates",
    "attachments",
)
WIKILINK_RE = re.compile(r"!?\[\[([^\]#|^]+)")


@dataclass(frozen=True)
class NoteSummary:
    path: Path
    title: str
    has_frontmatter: bool
    links: set[str]
    mtime: datetime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only audit for an Obsidian vault.")
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--limit", type=int, default=12)
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has_frontmatter(content: str) -> bool:
    if not content.startswith("---\n"):
        return False
    return "\n---\n" in content[4:]


def body_without_frontmatter(content: str) -> str:
    if not has_frontmatter(content):
        return content

    _frontmatter, _separator, body = content[4:].partition("\n---\n")
    return body


def extract_links(content: str) -> set[str]:
    body = body_without_frontmatter(content)
    return {match.strip() for match in WIKILINK_RE.findall(body) if match.strip()}


def note_title(path: Path) -> str:
    return path.stem


def collect_notes(vault: Path) -> list[NoteSummary]:
    notes: list[NoteSummary] = []

    for path in sorted(vault.rglob("*.md")):
        if ".obsidian" in path.parts:
            continue

        content = read_text(path)
        stat = path.stat()
        notes.append(
            NoteSummary(
                path=path,
                title=note_title(path),
                has_frontmatter=has_frontmatter(content),
                links=extract_links(content),
                mtime=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc),
            )
        )

    return notes


def build_title_index(notes: list[NoteSummary]) -> set[str]:
    titles = {note.title for note in notes}
    titles.update(note.path.with_suffix("").as_posix() for note in notes)
    titles.update(note.path.stem for note in notes)
    return titles


def unresolved_links(notes: list[NoteSummary], title_index: set[str]) -> list[tuple[Path, str]]:
    broken: list[tuple[Path, str]] = []

    for note in notes:
        for link in sorted(note.links):
            if link in title_index:
                continue
            broken.append((note.path, link))

    return broken


def inbound_counts(notes: list[NoteSummary]) -> dict[str, int]:
    counts = {note.title: 0 for note in notes}

    for note in notes:
        for link in note.links:
            link_title = Path(link).name
            if link_title in counts:
                counts[link_title] += 1

    return counts


def print_section(title: str) -> None:
    print(f"\n## {title}")


def relative_to_vault(path: Path, vault: Path) -> str:
    return path.relative_to(vault).as_posix()


def main() -> None:
    args = parse_args()
    vault = args.vault.expanduser()

    if not vault.exists():
        raise SystemExit(f"Vault not found: {vault}")

    notes = collect_notes(vault)
    title_index = build_title_index(notes)
    broken_links = unresolved_links(notes, title_index)
    inbound = inbound_counts(notes)
    missing_frontmatter = [note for note in notes if not note.has_frontmatter]
    orphan_notes = [
        note
        for note in notes
        if not note.links and inbound.get(note.title, 0) == 0
        and "99_Templates" not in note.path.parts
        and "90_Archive" not in note.path.parts
    ]

    print(f"# Obsidian KB Audit - {datetime.now().date().isoformat()}")
    print(f"Vault: {vault}")
    print(f"Notes: {len(notes)}")

    print_section("Core Folders")
    for folder in CORE_FOLDERS:
        status = "ok" if (vault / folder).exists() else "missing"
        print(f"- {folder}: {status}")

    print_section("Counts")
    for folder in CORE_FOLDERS:
        target = vault / folder
        if not target.exists() or not target.is_dir():
            continue
        count = len(list(target.rglob("*.md")))
        print(f"- {folder}: {count}")

    print_section("Needs Attention")
    print(f"- Missing frontmatter: {len(missing_frontmatter)}")
    print(f"- Orphan notes: {len(orphan_notes)}")
    print(f"- Broken wikilinks: {len(broken_links)}")

    if missing_frontmatter:
        print_section("Missing Frontmatter")
        for note in missing_frontmatter[: args.limit]:
            print(f"- {relative_to_vault(note.path, vault)}")

    if orphan_notes:
        print_section("Orphan Candidates")
        for note in sorted(orphan_notes, key=lambda item: item.mtime)[: args.limit]:
            print(f"- {relative_to_vault(note.path, vault)}")

    if broken_links:
        print_section("Broken Wikilinks")
        for path, link in broken_links[: args.limit]:
            print(f"- {relative_to_vault(path, vault)} -> [[{link}]]")

    print_section("Suggested Next Run")
    if missing_frontmatter:
        print("- Patch frontmatter for the smallest safe batch first.")
    if broken_links:
        print("- Resolve broken links before broad MOC maintenance.")
    if orphan_notes:
        print("- Review orphan candidates and link useful notes from MOCs.")
    if not missing_frontmatter and not broken_links and not orphan_notes:
        print("- Vault looks tidy enough for weekly synthesis.")


if __name__ == "__main__":
    main()
