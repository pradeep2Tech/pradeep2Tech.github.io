#!/usr/bin/env python3
"""Expand thin learning-path pages across handbooks with structured curriculum."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

# handbook section -> (index url, prerequisite note)
HANDBOOKS = {
    "design-patterns": ("/design-patterns/", "SOLID and GoF pattern fluency"),
    "golang-cheatsheet": ("/golang-cheatsheet/", "Go fundamentals and concurrency"),
    "python-cheatsheet": ("/python-cheatsheet/", "Python core syntax and stdlib"),
    "redis-cheatsheet": ("/redis-cheatsheet/", "Redis data structures"),
    "postgresql-cheatsheet": ("/postgresql-cheatsheet/", "SQL and transactions"),
    "mongodb-cheatsheet": ("/mongodb-cheatsheet/", "document modeling"),
    "kafka-handbook": ("/kafka-handbook/", "messaging fundamentals"),
}


def expand_design_patterns_senior(path: Path) -> None:
    body = """# Senior Engineer Path

**Audience:** Senior engineers (5–8 years) sharpening LLD and GoF pattern fluency.

**Duration:** 2 weeks (~4 hours/week).

**Prerequisite:** Comfortable with OOP in Java or Go; skim [SRP](/design-patterns/01-solid-principles/single-responsibility-principle/) first.

**Outcome:** Select patterns by force, implement with Java/Go tabs, pass LLD screens.

---

## Week 1 — Foundations and creational/structural

| Day | Read | Practice |
| :---: | :--- | :--- |
| 1 | [SOLID module](/design-patterns/01-solid-principles/) — all 5 principles | Draw class diagram for checkout without god class |
| 2 | [SOLID Composition Guide](/design-patterns/01-solid-principles/solid-principles-composition-guide/) | Refactor one smell from [God Object](/design-patterns/07-anti-patterns/god-object/) |
| 3 | [Creational patterns](/design-patterns/02-creational-patterns/) — Factory, Builder, Singleton | When **not** to use singleton |
| 4 | [Structural patterns](/design-patterns/03-structural-patterns/) — Adapter, Decorator, Facade | Compare [Decorator vs Proxy](/design-patterns/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/) |
| 5 | [Pattern comparisons](/design-patterns/05-pattern-comparisons/) — first 3 pages | Answer 5 rows from [Top 150](/design-patterns/10-interview-guide/top-150-design-pattern-questions/) |

---

## Week 2 — Behavioral, selection, case studies

| Day | Read | Practice |
| :---: | :--- | :--- |
| 6 | [Behavioral](/design-patterns/04-behavioral-patterns/) — Strategy, Observer, State, Command | Whiteboard vending machine state |
| 7 | [Pattern selection guide](/design-patterns/09-pattern-selection-guide/) | [Decision tree](/design-patterns/09-pattern-selection-guide/pattern-decision-tree/) for notification system |
| 8 | [Parking Lot LLD](/design-patterns/08-lld-case-studies/parking-lot/) | Implement core entities in Java or Go |
| 9 | [Rate Limiter LLD](/design-patterns/08-lld-case-studies/rate-limiter/) | Token bucket vs sliding window |
| 10 | **Mock** | 45 min LLD: library management — cite 3 patterns with tradeoffs |

---

## See also

- [Interview Revision Path](/design-patterns/11-learning-paths/design-patterns-interview-revision-path/)
- [Architect Path](/design-patterns/11-learning-paths/design-patterns-architect-path/)
"""
    write_path(path, body)


def expand_generic_stub(path: Path, section: str, title: str) -> None:
    index, prereq = HANDBOOKS.get(section, (f"/{section}/", "fundamentals for this handbook"))
    body = f"""# {title}

**Audience:** Senior engineers (6+ years) building depth in this handbook.

**Duration:** 2–3 weeks at ~3 hours/week.

**Prerequisite:** {prereq}. Start from the [handbook index]({index}) if terms feel unfamiliar.

---

## How to use this path

1. Read modules **in sidebar order** — later modules assume earlier ones.
2. For each topic page: read **Executive Summary → diagram → implementation tabs**.
3. End each week with [interview guide](/{section}/) questions for that module.
4. Pair with [System Design](/system-design/) when the topic affects distributed architecture.

---

## Suggested pace

| Week | Focus |
| :---: | :--- |
| 1 | Fundamentals module — complete every page, run examples locally |
| 2 | Core/internals module — depth over speed |
| 3 | Production + interview modules — troubleshooting and architect questions |

---

## Exit criteria

- Explain top 10 topics from this handbook in 60 seconds each.
- Debug one realistic failure using the handbook's troubleshooting page.
- Link handbook concepts to a [System Design](/system-design/) case study where relevant.

---

[← Back to handbook index]({index})
"""
    write_path(path, body)


def write_path(path: Path, body: str) -> None:
    text = path.read_text(encoding="utf-8-sig")
    m = re.match(r"(---[\s\S]*?---)\s*", text)
    if not m:
        return
    if len(body.splitlines()) + 15 > len(text.splitlines()):
        path.write_text(m.group(1) + "\n\n" + body.strip() + "\n", encoding="utf-8")
        print(f"expanded {path.relative_to(ROOT)}")


def main() -> None:
    dp_senior = CONTENT / "design-patterns/11-learning-paths/design-patterns-senior-engineer-path.md"
    if dp_senior.exists():
        expand_design_patterns_senior(dp_senior)

    for path in CONTENT.rglob("*path*.md"):
        if "_index" in path.name or "_meta" in path.parts:
            continue
        lines = len(path.read_text(encoding="utf-8-sig").splitlines())
        if lines >= 80:
            continue
        section = path.relative_to(CONTENT).parts[0]
        if section == "microservices":
            continue  # already hand-expanded
        if section == "design-patterns" and "senior-engineer" in path.name:
            continue
        title = path.stem.replace("-", " ").title()
        expand_generic_stub(path, section, title)


if __name__ == "__main__":
    main()
