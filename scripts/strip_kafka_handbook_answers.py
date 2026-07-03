"""Strip deep interview answer blocks from Kafka handbook cheatsheet pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content/kafka-handbook"
TOP150 = HB / "04-interview-guide/top-150-interview-questions.md"

ANSWER_START = re.compile(
    r"\n---\n+(## [^\n]+\n\n### Short Answer)",
    re.MULTILINE,
)

SKIP_DIRS = {"_meta"}


def strip_page_answers(text: str) -> tuple[str, bool]:
    m = ANSWER_START.search(text)
    if not m:
        return text, False
    return text[: m.start()].rstrip() + "\n", True


def strip_all_pages() -> int:
    count = 0
    for path in sorted(HB.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        original = path.read_text(encoding="utf-8")
        cleaned, changed = strip_page_answers(original)
        if changed:
            path.write_text(cleaned, encoding="utf-8")
            count += 1
    return count


def strip_top150_anchors() -> None:
    text = TOP150.read_text(encoding="utf-8")
    text = text.replace(
        "Each row links to the canonical deep-dive page.",
        "Each row links to the canonical cheatsheet page (questions only — no long-form answers).",
    )
    text = re.sub(r"\]\((/kafka-handbook/[^)#]+)(?:#[^)]+)?\)", r"](\1/)", text)
    text = re.sub(r"(/kafka-handbook/[^)\s]+)/\)", r"\1/)", text)
    TOP150.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    n = strip_all_pages()
    strip_top150_anchors()
    print(f"Stripped answer blocks from {n} pages; Top 150 anchors removed.")
