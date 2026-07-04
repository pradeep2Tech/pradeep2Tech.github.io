#!/usr/bin/env python3
"""Fix duplicate frontmatter and normalize headings in expanded microservices pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "microservices"

HEADING_FIXES = [
    (r"^### Core Microservices Pattern.*", "## Executive Summary"),
    (r"^### Production-Grade Implementation.*", "## Architecture Diagram"),
    (r"^### Runtime Execution Path.*", "## Internal Working"),
    (r"^### Runtime Execution Paths.*", "## Internal Working"),
    (r"^### Architecture Decision Matrix", "## Design Options"),
    (r"^### Choreography vs\.", "## Design Options"),
    (r"^### API Gateway vs\.", "## Design Options"),
    (r"^### Five-Phase Migration", "## Internal Working"),
    (r"^### When to Decompose", "## Design Decisions"),
    (r"^### Critical System Design Trade-offs.*", "## Tradeoffs"),
    (r"^### Network & Latency Impact", "### Network & Latency"),
    (r"^### Data Consistency & Isolation", "### Data Consistency"),
    (r"^### Failure Modes & Cascading Risk", "## Common Failures"),
    (r"^### Interview Failure Modes.*", "## Interview Questions"),
    (r"^#### The \"Junior\" Mistake", "### Junior Mistake"),
    (r"^#### The \"Senior\" Counter-Measure", "### Senior Counter-Measure"),
    (r"^### Conway's Law Alignment", "## Design Decisions"),
    (r"^### Cutover Gate.*", "## Production Lessons"),
    (r"^## Related:", "## Supplement:"),
]


def strip_duplicate_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    first_end = text.find("\n---", 3)
    if first_end == -1:
        return text
    rest = text[first_end + 4 :].lstrip("\n")
    if rest.startswith("---") or rest.startswith("\ufeff---"):
        rest = rest.lstrip("\ufeff")
        second_end = rest.find("\n---", 3)
        if second_end != -1:
            rest = rest[second_end + 4 :].lstrip("\n")
    return text[: first_end + 4] + "\n\n" + rest


def fix_headings(body: str) -> str:
    lines = []
    for line in body.split("\n"):
        replaced = line
        for pattern, repl in HEADING_FIXES:
            if re.match(pattern, line.strip()):
                replaced = repl
                break
        lines.append(replaced)
    return "\n".join(lines)


def fix_links(body: str) -> str:
    replacements = {
        "/microservices/strangler-fig-application-pattern/": "/microservices/09-migration-modernization/strangler-pattern/",
        "/microservices/database-per-microservice/": "/microservices/03-data-management/database-per-service/",
        "/microservices/saga-pattern-distributed-transactions/": "/microservices/03-data-management/saga/",
        "/microservices/cqrs-event-sourcing/": "/microservices/03-data-management/cqrs-and-event-sourcing/",
        "/microservices/api-gateway-bff-pattern/": "/microservices/02-service-communication/api-gateway-and-bff/",
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    return body


def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8-sig")
    if "### Core Microservices" not in text and not text.count("---") > 2:
        return
    fixed = strip_duplicate_frontmatter(text)
    parts = fixed.split("---", 2)
    if len(parts) < 3:
        return
    fm = f"---{parts[1]}---"
    body = fix_headings(fix_links(parts[2].strip()))
    path.write_text(fm + "\n\n" + body + "\n", encoding="utf-8")
    print(f"fixed {path.relative_to(ROOT)}")


def main() -> None:
    for path in CONTENT.rglob("*.md"):
        if path.name == "_index.md":
            continue
        process_file(path)


if __name__ == "__main__":
    main()
