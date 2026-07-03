"""Phase C: answer layer, See Also navigation, P0 mermaid, Top 150 deep-dive links."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

from mongodb_answer_engine import (
    QUESTIONS,
    craft_answer,
    format_answer_block,
    slug_anchor,
)

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "mongodb-cheatsheet"
DATA = ROOT / "data"
BASE = "/mongodb-cheatsheet"
TOP150 = HB / "06-interview-guide/top-150-interview-questions.md"

ANSWER_START = "<!-- interview-answers:start -->"
ANSWER_END = "<!-- interview-answers:end -->"

# Pages that receive answer blocks (exclude interview index pages)
SKIP_ANSWER_PREFIXES = (
    "06-interview-guide/top-150",
    "06-interview-guide/architect-questions",
    "06-interview-guide/troubleshooting-questions",
    "06-interview-guide/performance-questions",
    "06-interview-guide/_index",
    "07-learning-paths/_index",
)

MERMAID_P0: dict[str, str] = {
    "02-core-mongodb/storage-engine.md": """
```mermaid
sequenceDiagram
  participant App
  participant Cache as WiredTiger cache
  participant Journal
  participant Disk
  App->>Cache: write document
  Cache->>Journal: WAL record
  Journal-->>App: ack (if j:true)
  Cache->>Disk: checkpoint (~60s)
```
""",
    "02-core-mongodb/replication.md": """
```mermaid
sequenceDiagram
  participant Primary
  participant Oplog
  participant Secondary
  Primary->>Oplog: append op
  Secondary->>Oplog: tail cursor
  Oplog-->>Secondary: apply op
  Note over Secondary: election if primary lost
```
""",
    "02-core-mongodb/sharding.md": """
```mermaid
sequenceDiagram
  participant Balancer
  participant Config
  participant ShardA
  participant ShardB
  Balancer->>Config: plan chunk move
  Balancer->>ShardA: migrate chunk
  ShardA->>ShardB: copy + finalize
  Config-->>Balancer: update metadata
```
""",
    "03-query-performance/query-optimization.md": """
```mermaid
flowchart TD
  Q[Query] --> P[Planner]
  P --> I{Index usable?}
  I -->|yes| IX[IXSCAN]
  I -->|no| CS[COLLSCAN]
  IX --> F[FETCH or covered return]
```
""",
    "03-query-performance/explain-plan.md": """
```mermaid
flowchart TB
  WP[winningPlan] --> ST[stage tree]
  ST --> IX[IXSCAN]
  ST --> FE[FETCH]
  ST --> COV[PROJECTION_COVERED]
  ES[executionStats] --> DER[totalDocsExamined / nReturned]
```
""",
    "04-production-operations/monitoring.md": """
```mermaid
flowchart LR
  MS[mongostat] --> OPS[opcounters / lag]
  MT[mongotop] --> COLL[collection time]
  PF[profiler] --> SQ[slow queries]
  AT[Atlas metrics] --> ALT[alerts]
```
""",
    "04-production-operations/troubleshooting.md": """
```mermaid
flowchart TD
  S[Symptom] --> L{Replication lag?}
  L -->|yes| RL[oplog / disk / network]
  L -->|no| Q{Slow query?}
  Q -->|yes| EX[explain + index]
  Q -->|no| C{Cache/OOM?}
  C -->|yes| RAM[capacity plan]
```
""",
    "04-production-operations/capacity-planning.md": """
```mermaid
flowchart TB
  WS[Working set] --> RAM{Fits in cache?}
  RAM -->|no| PF[page faults rise]
  RAM -->|yes| OK[stable p99]
  PF --> SCALE[more RAM or shard]
```
""",
}


def load_topic_order() -> list[str]:
    order = yaml.safe_load((DATA / "mongodb_cheatsheet_order.yaml").read_text(encoding="utf-8"))
    return order["topics"]


def topic_url(slug: str) -> str:
    return f"{BASE}/{slug}/"


def title_from_slug(slug: str) -> str:
    return slug.split("/")[-1].replace("-", " ").title()


def strip_front_matter(text: str) -> tuple[str, str]:
    if text.startswith("---"):
        end = text.index("---", 3) + 3
        return text[:end], text[end:].lstrip("\n")
    return "", text


def remove_section(body: str, heading: str) -> str:
    pattern = rf"\n## {re.escape(heading)}[\s\S]*?(?=\n## |\Z)"
    return re.sub(pattern, "", body, count=1)


def remove_related_topics(body: str) -> str:
    return re.sub(r"\n## Related Topics[\s\S]*?(?=\n## |\Z)", "", body)


def remove_old_answers(body: str) -> str:
    if ANSWER_START in body and ANSWER_END in body:
        return re.sub(
            rf"\n?{re.escape(ANSWER_START)}[\s\S]*?{re.escape(ANSWER_END)}\n?",
            "\n",
            body,
        )
    if ANSWER_END in body:
        return re.sub(
            rf"\n# Interview Answers[\s\S]*?{re.escape(ANSWER_END)}\n?",
            "\n",
            body,
        )
    return body


def build_see_also(slug: str, topics: list[str]) -> str:
    if slug not in topics:
        return ""
    idx = topics.index(slug)
    lines = ["## See Also", ""]
    if idx > 0:
        prev = topics[idx - 1]
        lines.append(f"- [Previous: {title_from_slug(prev)}]({topic_url(prev)})")
    if idx < len(topics) - 1:
        nxt = topics[idx + 1]
        lines.append(f"- [Next: {title_from_slug(nxt)}]({topic_url(nxt)})")
    lines.append(f"- [MongoDB Handbook Index]({BASE}/)")
    lines.append(f"- [Top 150 Interview Questions]({BASE}/06-interview-guide/top-150-interview-questions/)")
    return "\n".join(lines) + "\n"


def insert_mermaid(rel_path: str, body: str) -> str:
    snippet = MERMAID_P0.get(rel_path)
    if not snippet or snippet.strip() in body:
        return body
    if "sequenceDiagram" in snippet and "sequenceDiagram" in body:
        return body
    if "## Internal Working" in body:
        return body.replace("## Internal Working", f"## Internal Working\n{snippet.strip()}\n", 1)
    if "## Core Concepts" in body:
        return body.replace("## Core Concepts", f"## Core Concepts\n{snippet.strip()}\n", 1)
    return body + "\n" + snippet.strip() + "\n"


def append_answers(rel_path: str, body: str, blocks: list[str]) -> str:
    if not blocks:
        return body
    body = remove_section(body, "Interview Questions")
    section = (
        f"\n{ANSWER_START}\n\n"
        "# Interview Answers (Top 150)\n\n"
        + "".join(blocks)
        + f"{ANSWER_END}\n"
    )
    return body.rstrip() + "\n" + section


def group_questions_by_page() -> dict[str, list[tuple]]:
    groups: dict[str, list[tuple]] = defaultdict(list)
    for row in QUESTIONS:
        groups[row[5]].append(row)
    return groups


def build_answer_blocks(rows: list[tuple]) -> list[str]:
    blocks = []
    for num, question, _d, _l, topic, doc in sorted(rows, key=lambda r: r[0]):
        sections = craft_answer(num, question, topic, doc)
        blocks.append(format_answer_block(question, sections))
    return blocks


def update_topic_pages(topics: list[str], groups: dict[str, list[tuple]]) -> int:
    count = 0
    for slug in topics:
        rel = f"{slug}.md"
        path = HB / rel
        if not path.exists():
            continue
        if any(slug.startswith(p) for p in SKIP_ANSWER_PREFIXES):
            continue
        fm, body = strip_front_matter(path.read_text(encoding="utf-8"))
        body = remove_related_topics(body)
        body = remove_old_answers(body)
        body = insert_mermaid(rel, body)
        blocks = build_answer_blocks(groups.get(rel, []))
        body = append_answers(rel, body, blocks)
        body = remove_section(body, "See Also")
        body = body.rstrip() + "\n\n---\n\n" + build_see_also(slug, topics)
        path.write_text(fm + "\n\n" + body.lstrip("\n"), encoding="utf-8")
        count += 1
    return count


def deep_dive_link(num: int, question: str, doc: str) -> str:
    slug = doc.replace(".md", "")
    anchor = slug_anchor(question)
    label = title_from_slug(slug)
    return f"[{label} — Q{num}]({topic_url(slug)}#{anchor})"


def update_top150() -> None:
    text = TOP150.read_text(encoding="utf-8")
    text = text.replace(
        "Questions only — no answers.",
        "Questions only on this page — answers live on linked canonical topic pages.",
    )
    out = []
    qmap = {n: (q, doc) for n, q, *_rest, doc in [(r[0], r[1], r[2], r[3], r[4], r[5]) for r in QUESTIONS]}
    for line in text.splitlines():
        m = re.match(r"^\| (\d+) \| (.+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| `([^`]+)` \|", line)
        if m:
            num = int(m.group(1))
            question = m.group(2)
            doc = m.group(6).replace(BASE + "/", "").strip("/")
            if not doc.endswith(".md"):
                doc = doc + ".md"
            link = deep_dive_link(num, question, doc)
            out.append(
                f"| {num} | {question} | {m.group(3).strip()} | {m.group(4).strip()} | "
                f"{m.group(5).strip()} | {link} |"
            )
        else:
            out.append(line)
    TOP150.write_text("\n".join(out) + "\n", encoding="utf-8")


def update_learning_path_answers() -> None:
    rel = "07-learning-paths/mongodb-senior-engineer-path.md"
    path = HB / rel
    rows = [r for r in QUESTIONS if r[5] == rel]
    if not path.exists() or not rows:
        return
    fm, body = strip_front_matter(path.read_text(encoding="utf-8"))
    body = remove_old_answers(body)
    blocks = build_answer_blocks(rows)
    body = append_answers(rel, body, blocks)
    path.write_text(fm + "\n\n" + body.lstrip("\n"), encoding="utf-8")


def main() -> None:
    """Apply answer layer. Run restore_mongodb_base_pages.py first if pages were corrupted."""
    topics = load_topic_order()
    # Only handbook topic pages for See Also / answers (exclude interview + learning path list at end)
    nav_topics = [
        t
        for t in topics
        if not t.startswith("06-interview-guide/")
        and not t.startswith("07-learning-paths/")
    ]
    groups = group_questions_by_page()
    n = update_topic_pages(nav_topics, groups)
    update_learning_path_answers()
    update_top150()
    print(f"Phase C complete: updated {n} topic pages, Top 150 deep-dive anchors, P0 mermaid on {len(MERMAID_P0)} pages.")


if __name__ == "__main__":
    main()
