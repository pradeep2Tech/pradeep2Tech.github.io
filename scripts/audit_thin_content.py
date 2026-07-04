#!/usr/bin/env python3
"""Audit thin content pages across handbooks."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
THRESHOLD = 100

STUB_MARKERS = [
    "Canonical page for",
    "Cross-handbook depth: link out",
    "Expanded from legacy playbook",
    "Apply at service boundaries within the microservices fleet",
]

def is_stub(text: str, lines: int) -> bool:
    if lines < 60:
        return True
    if lines < THRESHOLD and any(m in text for m in STUB_MARKERS):
        return True
    # Very few headings = likely stub
    headings = sum(1 for ln in text.splitlines() if ln.startswith("## "))
    if lines < THRESHOLD and headings < 6:
        return True
    return False

def main():
    by_section: dict[str, list[tuple[int, str, bool]]] = {}
    for path in sorted(CONTENT.rglob("*.md")):
        if "_index.md" in path.name or "_meta" in path.parts:
            continue
        rel = path.relative_to(CONTENT)
        section = rel.parts[0]
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        lines = len(text.splitlines())
        stub = is_stub(text, lines)
        if lines < THRESHOLD or stub:
            by_section.setdefault(section, []).append((lines, str(rel).replace("\\", "/"), stub))

    for section in sorted(by_section):
        items = sorted(by_section[section])
        stubs = sum(1 for _, _, s in items if s)
        print(f"\n=== {section} ({len(items)} thin, {stubs} likely stubs) ===")
        for lines, rel, stub in items[:20]:
            flag = "STUB" if stub else "thin"
            print(f"  {lines:4d} [{flag}] {rel}")
        if len(items) > 20:
            print(f"  ... +{len(items)-20} more")

if __name__ == "__main__":
    main()
