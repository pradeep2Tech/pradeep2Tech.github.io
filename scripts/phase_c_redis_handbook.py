"""Phase C: answer layer, See Also navigation, P0 mermaid, Top 150 deep-dive anchors."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

from redis_answer_engine import (
    QUESTIONS,
    craft_answer,
    format_answer_block,
    slug_anchor,
)

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "redis-cheatsheet"
DATA = ROOT / "data"
BASE = "/redis-cheatsheet"
TOP150 = HB / "08-interview-guide/top-150-interview-questions.md"
ARCHITECT = HB / "08-interview-guide/architect-questions.md"
TROUBLESHOOTING = HB / "08-interview-guide/troubleshooting-questions.md"
PERFORMANCE = HB / "08-interview-guide/performance-questions.md"

ANSWER_START = "<!-- interview-answers:start -->"
ANSWER_END = "<!-- interview-answers:end -->"
GUIDE_ANSWER_START = "<!-- interview-guide-answers:start -->"
GUIDE_ANSWER_END = "<!-- interview-guide-answers:end -->"

SKIP_ANSWER_PREFIXES = (
    "08-interview-guide/top-150",
    "08-interview-guide/architect-questions",
    "08-interview-guide/troubleshooting-questions",
    "08-interview-guide/performance-questions",
    "08-interview-guide/_index",
    "09-learning-paths/_index",
)

MERMAID_P0: dict[str, str] = {
    "03-redis-internals/persistence.md": """
```mermaid
sequenceDiagram
  participant Primary
  participant Child as BGSAVE child
  participant Disk
  Primary->>Child: fork
  Child->>Disk: write RDB snapshot
  Note over Primary: COW memory may rise
```
""",
    "03-redis-internals/replication.md": """
```mermaid
sequenceDiagram
  participant Primary
  participant Backlog
  participant Replica
  Primary->>Backlog: replication offset
  Replica->>Backlog: PSYNC partial resync
  Backlog-->>Replica: missing commands
```
""",
    "03-redis-internals/sentinel.md": """
```mermaid
sequenceDiagram
  participant S1 as Sentinel
  participant S2 as Sentinel
  participant Primary
  participant Replica
  S1->>S2: agree ODOWN
  S2->>Replica: promote
  Replica->>Primary: REPLICAOF NO ONE
```
""",
    "03-redis-internals/cluster.md": """
```mermaid
flowchart TB
  client[Cluster client] --> n1[Primary A slots 0-5460]
  client --> n2[Primary B slots 5461-10922]
  client --> n3[Primary C slots 10923-16383]
  n1 --> r1[Replica A]
  n2 --> r2[Replica B]
  n3 --> r3[Replica C]
```
""",
    "03-redis-internals/redis-protocol.md": """
```mermaid
sequenceDiagram
  participant Client
  participant Redis
  Client->>Redis: PIPELINE cmd1..cmdN
  Redis-->>Client: reply1..replyN
  Note over Redis: commands still run sequentially
```
""",
    "06-performance-operations/monitoring.md": """
```mermaid
flowchart LR
  INFO[INFO memory/stats] --> dash[Dashboards]
  SLOW[SLOWLOG] --> triage[Slow command triage]
  LAT[LATENCY DOCTOR] --> fix[Config/command fix]
```
""",
    "06-performance-operations/capacity-planning.md": """
```mermaid
flowchart TB
  keys[Key count forecast] --> mem[Memory estimate]
  mem --> headroom[+ replication + COW headroom]
  headroom --> decision{Scale up or Cluster?}
```
""",
    "06-performance-operations/performance-tuning.md": """
```mermaid
flowchart TB
  lat[Latency] --> net[Network RTT]
  lat --> pipe[Pipelining batch]
  lat --> cmd[Command complexity]
  lat --> hot[Hot key / single thread]
```
""",
    "05-production-patterns/cache-invalidation.md": """
```mermaid
sequenceDiagram
  participant App
  participant DB
  participant Redis
  App->>DB: write
  App->>Redis: DEL or UPDATE cache key
```
""",
    "05-production-patterns/cache-avalanche.md": """
```mermaid
flowchart TD
  A[Many keys share TTL] --> B[Mass expiry]
  B --> C[Origin overload]
  C --> D[TTL jitter + early refresh]
```
""",
    "05-production-patterns/cache-penetration.md": """
```mermaid
flowchart LR
  miss[Cache miss] --> exists{Key exists in DB?}
  exists -->|no| bloom[Bloom filter / short negative TTL]
  exists -->|yes| load[Load and cache]
```
""",
}


def load_topic_order() -> list[str]:
    order = yaml.safe_load((DATA / "redis_cheatsheet_order.yaml").read_text(encoding="utf-8"))
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


def remove_old_answers(body: str) -> str:
    if ANSWER_START in body and ANSWER_END in body:
        return re.sub(
            rf"\n?{re.escape(ANSWER_START)}[\s\S]*?{re.escape(ANSWER_END)}\n?",
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
    lines.append(f"- [Redis Handbook Index]({BASE}/)")
    lines.append(f"- [Top 150 Interview Questions]({BASE}/08-interview-guide/top-150-interview-questions/)")
    return "\n".join(lines) + "\n"


def insert_mermaid(rel_path: str, body: str) -> str:
    snippet = MERMAID_P0.get(rel_path)
    if not snippet or snippet.strip() in body:
        return body
    if "## Internal Working" in body:
        return body.replace("## Internal Working", f"## Internal Working\n{snippet.strip()}\n", 1)
    if "## Core Concepts" in body:
        return body.replace("## Core Concepts", f"## Core Concepts\n{snippet.strip()}\n", 1)
    return body.rstrip() + "\n" + snippet.strip() + "\n"


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
    doc_clean = doc.replace(".md", "").split("#")[0]
    anchor = slug_anchor(question)
    label = title_from_slug(doc_clean)
    return f"[{label} — Q{num}]({topic_url(doc_clean)}#{anchor})"


def remove_guide_answers(body: str) -> str:
    if GUIDE_ANSWER_START in body and GUIDE_ANSWER_END in body:
        return re.sub(
            rf"\n?{re.escape(GUIDE_ANSWER_START)}[\s\S]*?{re.escape(GUIDE_ANSWER_END)}\n?",
            "\n",
            body,
        )
    return body


def format_numbered_answer_block(num: int, question: str, sections: dict) -> str:
    inner = format_answer_block(question, sections)
    return f"### Q{num}. {question}\n\n" + inner[len(f"## {question}\n\n") :]


def build_numbered_answer_blocks(rows: list[tuple]) -> str:
    blocks = []
    for num, question, _d, _l, topic, doc in sorted(rows, key=lambda r: r[0]):
        sections = craft_answer(num, question, topic, doc)
        blocks.append(format_numbered_answer_block(num, question, sections))
    return "".join(blocks)


def append_guide_answers(body: str, blocks: str, heading: str = "Answers") -> str:
    if not blocks.strip():
        return body
    body = remove_guide_answers(body)
    body = remove_section(body, heading)
    section = (
        f"\n{GUIDE_ANSWER_START}\n\n"
        f"## {heading}\n\n"
        f"{blocks.rstrip()}\n\n"
        f"{GUIDE_ANSWER_END}\n"
    )
    return body.rstrip() + "\n" + section


def update_top150() -> None:
    text = TOP150.read_text(encoding="utf-8")
    fm, body = strip_front_matter(text)
    body = remove_guide_answers(body)
    body = body.replace(
        "**Questions only** on this page — answers live on linked canonical topic pages.",
        "Question index with **inline answers** below. **Deep Dive** links point to canonical handbook pages for extended context.",
    )
    body = body.replace(
        "**Questions only** — each **Deep Dive** links to the canonical handbook page.",
        "Question index with **inline answers** below. **Deep Dive** links point to canonical handbook pages for extended context.",
    )
    questions_by_num = {num: row for row in QUESTIONS for num in [row[0]]}
    out = []
    for line in body.splitlines():
        m = re.match(
            r"^\| (\d+) \| (.+?) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|",
            line,
        )
        if m and "|" in line and line.strip().endswith("|"):
            num = int(m.group(1))
            question = m.group(2).strip()
            row = questions_by_num.get(num)
            if row:
                doc_path = row[5]
                link = deep_dive_link(num, question, doc_path)
                out.append(
                    f"| {num} | {question} | {m.group(3).strip()} | {m.group(4).strip()} | "
                    f"{m.group(5).strip()} | {link} |"
                )
                continue
        out.append(line)
    body = "\n".join(out)
    body = remove_section(body, "See Also")
    answer_blocks = build_numbered_answer_blocks(list(QUESTIONS))
    body = append_guide_answers(body, answer_blocks)
    body = body.rstrip() + "\n\n---\n\n## See Also\n\n"
    body += f"- [Architect Questions]({BASE}/08-interview-guide/architect-questions/)\n"
    body += f"- [Troubleshooting Questions]({BASE}/08-interview-guide/troubleshooting-questions/)\n"
    body += f"- [Performance Questions]({BASE}/08-interview-guide/performance-questions/)\n"
    body += f"- [Redis Handbook Index]({BASE}/)\n"
    TOP150.write_text(fm + "\n\n" + body.lstrip("\n"), encoding="utf-8")


def update_subset_page(
    path: Path,
    intro: str,
    title: str,
    rows: list[tuple],
    see_also_lines: list[str],
) -> None:
    text = path.read_text(encoding="utf-8")
    fm, _body = strip_front_matter(text)
    answer_blocks = build_numbered_answer_blocks(rows)
    content = (
        f"{intro}\n\n"
        f"# {title}\n\n"
        f"{GUIDE_ANSWER_START}\n\n"
        f"{answer_blocks.rstrip()}\n\n"
        f"{GUIDE_ANSWER_END}\n\n"
        f"---\n\n"
        f"## See Also\n\n"
        + "\n".join(see_also_lines)
        + "\n"
    )
    path.write_text(fm + "\n\n" + content.lstrip("\n"), encoding="utf-8")


def update_interview_subsets() -> None:
    architect_rows = [(n, q, d, l, t, doc) for n, q, d, l, t, doc in QUESTIONS if l == "Architect"][:40]
    trouble_rows = [row for row in QUESTIONS if 41 <= row[0] <= 70]
    perf_rows = [row for row in QUESTIONS if 71 <= row[0] <= 95]

    update_subset_page(
        ARCHITECT,
        f"Architect-focused subset from the [Top 150]({BASE}/08-interview-guide/top-150-interview-questions/). **Full answers** for each question below.",
        "Architect Questions",
        architect_rows,
        [
            f"- [Previous: Top 150 Interview Questions]({BASE}/08-interview-guide/top-150-interview-questions/)",
            f"- [Next: Troubleshooting Questions]({BASE}/08-interview-guide/troubleshooting-questions/)",
            f"- [Redis Handbook Index]({BASE}/)",
        ],
    )
    update_subset_page(
        TROUBLESHOOTING,
        "Troubleshooting-focused subset with **inline answers**.",
        "Troubleshooting Questions",
        trouble_rows,
        [
            f"- [Previous: Architect Questions]({BASE}/08-interview-guide/architect-questions/)",
            f"- [Next: Performance Questions]({BASE}/08-interview-guide/performance-questions/)",
            f"- [Top 150 Interview Questions]({BASE}/08-interview-guide/top-150-interview-questions/)",
            f"- [Redis Handbook Index]({BASE}/)",
        ],
    )
    update_subset_page(
        PERFORMANCE,
        "Performance-focused subset with **inline answers**.",
        "Performance Questions",
        perf_rows,
        [
            f"- [Previous: Troubleshooting Questions]({BASE}/08-interview-guide/troubleshooting-questions/)",
            f"- [Next: Senior Engineer Path]({BASE}/09-learning-paths/redis-senior-engineer-path/)",
            f"- [Top 150 Interview Questions]({BASE}/08-interview-guide/top-150-interview-questions/)",
            f"- [Redis Handbook Index]({BASE}/)",
        ],
    )


def main() -> None:
    topics = load_topic_order()
    nav_topics = [
        t
        for t in topics
        if not t.startswith("08-interview-guide/")
        and not t.startswith("09-learning-paths/")
    ]
    groups = group_questions_by_page()
    n = update_topic_pages(nav_topics, groups)
    update_top150()
    update_interview_subsets()
    answered_pages = sum(1 for k, v in groups.items() if v and not any(
        k.startswith(p.replace("/", ".md")) for p in SKIP_ANSWER_PREFIXES
    ))
    print(
        f"Phase C complete: updated {n} topic pages, "
        f"{sum(len(v) for v in groups.values())} answers mapped, "
        f"Top 150 + subset pages with inline answers, P0 mermaid on {len(MERMAID_P0)} pages."
    )


if __name__ == "__main__":
    main()
