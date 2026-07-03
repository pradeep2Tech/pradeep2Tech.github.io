"""Remove interview answer blocks from Python handbook topic pages."""
from __future__ import annotations

import re
from pathlib import Path

from python_questions_data import QUESTIONS

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "python-cheatsheet"
BASE = "/python-cheatsheet"
TOP150 = HB / "09-interview-guide/top-150-interview-questions.md"

SKIP_DIRS = {"_meta", "09-interview-guide", "10-learning-paths"}


def strip_answers(body: str) -> str:
    body = re.sub(
        r"\n?<!-- interview-answers:start -->[\s\S]*?<!-- interview-answers:end -->\n?",
        "\n",
        body,
    )
    body = re.sub(
        r"\n---\n\n## [^\n]+\n\n### Short Answer[\s\S]*?<!-- interview-answers:end -->\n?",
        "\n",
        body,
    )
    body = re.sub(r"\n?<!-- interview-answers:end -->\n?", "\n", body)
    body = re.sub(
        r"\n---\n\n## [^\n]+\n\n### Short Answer[\s\S]*?(?=\n---\n\n## See Also|\n## See Also|\Z)",
        "\n",
        body,
    )
    if "## Interview Questions" not in body and "## See Also" in body:
        body = body.replace(
            "\n---\n\n## See Also",
            "\n\n## Interview Questions\n\n"
            f"See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).\n\n"
            "---\n\n## See Also",
            1,
        )
    return body.rstrip() + "\n"


def restore_top150() -> None:
    rows = []
    for n, q, d, l, t, doc in QUESTIONS:
        slug = doc.replace(".md", "")
        label = slug.split("/")[-1].replace("-", " ").title()
        link = f"[{label}]({BASE}/{slug}/)"
        rows.append(f"| {n} | {q} | {d} | {l} | {t} | {link} |")

    fm, _ = "", ""
    text = TOP150.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.index("---", 3) + 3
        fm = text[:end]

    body = (
        "Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. "
        "**Questions only — no answers.**\n\n"
        "**Distribution:** Internals & Runtime 40 · Concurrency & Async 30 · Performance 25 · "
        "Troubleshooting 20 · Production 15 · Core Python 20\n\n"
        "| # | Question | Difficulty | Level | Topic | Deep Dive |\n"
        "|---|----------|------------|--------|-------|-----------|\n"
        + "\n".join(rows)
        + "\n"
    )
    TOP150.write_text(fm + "\n\n" + body, encoding="utf-8")


def main() -> None:
    count = 0
    for path in sorted(HB.rglob("*.md")):
        rel_parts = path.relative_to(HB).parts
        if rel_parts[0] in SKIP_DIRS or path.name == "_index.md":
            continue
        text = path.read_text(encoding="utf-8")
        if "### Short Answer" not in text and "interview-answers" not in text:
            continue
        fm, body = "", text
        if text.startswith("---"):
            end = text.index("---", 3) + 3
            fm, body = text[:end], text[end:].lstrip("\n")
        new_body = strip_answers(body)
        if new_body != body:
            path.write_text(fm + "\n\n" + new_body.lstrip("\n"), encoding="utf-8")
            count += 1
    restore_top150()
    print(f"Stripped answers from {count} pages; Top 150 reverted to page links only.")


if __name__ == "__main__":
    main()
