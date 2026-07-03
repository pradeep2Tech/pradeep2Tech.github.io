"""Phase C: expand stub pages, P0 mermaid, interview answer layer, Top 150 anchors."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

from phase_c_python_page_expansions import EXPANDED_PAGES
from python_answer_engine import QUESTIONS, craft_answer, format_answer_block, slug_anchor

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "python-cheatsheet"
DATA = ROOT / "data"
BASE = "/python-cheatsheet"
TOP150 = HB / "09-interview-guide/top-150-interview-questions.md"

ANSWER_START = "<!-- interview-answers:start -->"
ANSWER_END = "<!-- interview-answers:end -->"

SKIP_ANSWER_PREFIXES = (
    "09-interview-guide/top-150",
    "09-interview-guide/architect-questions",
    "09-interview-guide/troubleshooting-questions",
    "09-interview-guide/performance-questions",
    "09-interview-guide/_index",
    "10-learning-paths/",
)

MERMAID_P0: dict[str, str] = {
    "03-python-internals/python-runtime.md": """
```mermaid
flowchart TB
  start[Interpreter start] --> path[Init sys.path]
  path --> enc[Import encodings / site]
  enc --> main[Run __main__ module]
  main --> shutdown[atexit / shutdown]
```
""",
    "03-python-internals/cpython-internals.md": """
```mermaid
flowchart TB
  py[Python source] --> parser[Parser / AST]
  parser --> compiler[Compiler]
  compiler --> ceval[ceval loop]
  ceval --> obj[PyObject graph]
  obj --> capi[C API / extensions]
```
""",
    "03-python-internals/bytecode.md": """
```mermaid
flowchart TB
  frame[Frame] --> stack[Value stack]
  frame --> ip[Instruction pointer]
  ip --> op[Opcode dispatch]
  op --> stack
```
""",
    "03-python-internals/object-model.md": """
```mermaid
flowchart LR
  inst[Instance __dict__] --> cls[Class]
  cls --> mro[MRO parents]
  mro --> desc[Descriptor __get__]
```
""",
    "03-python-internals/garbage-collection.md": """
```mermaid
flowchart LR
  g0[gen0] --> g1[gen1]
  g1 --> g2[gen2]
  g2 --> sweep[Collect cycles]
```
""",
    "03-python-internals/gil.md": """
```mermaid
flowchart TD
  T[Thread work] --> kind{Work type?}
  kind -->|I/O or C ext| rel[GIL released]
  kind -->|Python bytecode CPU| hold[GIL held]
  hold --> scale[Use processes / native]
```
""",
    "04-concurrency/concurrency.md": """
```mermaid
flowchart TD
  W[Workload] --> io{Mostly waiting on I/O?}
  io -->|yes, async APIs| a[asyncio]
  io -->|yes, blocking libs| t[thread pool]
  io -->|no, CPU Python| p[multiprocessing]
```
""",
    "04-concurrency/asyncio.md": """
```mermaid
sequenceDiagram
  participant Loop
  participant C1 as coro A
  participant C2 as coro B
  Loop->>C1: run until await
  C1-->>Loop: suspend I/O
  Loop->>C2: run until await
  C2-->>Loop: suspend I/O
  Loop->>C1: resume on ready
```
""",
    "07-packaging-distribution/dependency-management.md": """
```mermaid
flowchart TD
  spec[pyproject dependencies] --> resolve[Resolver]
  resolve --> lock[Lock file]
  lock --> ci[Reproducible CI install]
```
""",
}


def load_topic_order() -> list[str]:
    order = yaml.safe_load((DATA / "python_cheatsheet_order.yaml").read_text(encoding="utf-8"))
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


def normalize_body(body: str) -> str:
    """Strip accidental leading indentation from generator output."""
    lines = body.splitlines()
    if not lines:
        return body
    indents = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    if indents and min(indents) >= 2:
        strip = min(indents)
        lines = [line[strip:] if line.strip() else line for line in lines]
    return "\n".join(lines).strip() + "\n"


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
    lines.append(f"- [Python Handbook Index]({BASE}/)")
    lines.append(f"- [Top 150 Interview Questions]({BASE}/09-interview-guide/top-150-interview-questions/)")
    return "\n".join(lines) + "\n"


def insert_mermaid(rel_path: str, body: str) -> str:
    snippet = MERMAID_P0.get(rel_path)
    if not snippet or snippet.strip() in body:
        return body
    for heading in ("## Internal Working", "## Core Concepts", "## Runtime Behavior"):
        if heading in body:
            return body.replace(heading, f"{heading}\n{snippet.strip()}\n", 1)
    return body.rstrip() + "\n\n" + snippet.strip() + "\n"


ENABLE_ANSWER_LAYER = False  # Set True when answer blocks are wanted on topic pages.


def append_answers(rel_path: str, body: str, blocks: list[str]) -> str:
    if not ENABLE_ANSWER_LAYER or not blocks:
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


def apply_expansion(rel_path: str, body: str) -> str:
    if rel_path in EXPANDED_PAGES:
        return EXPANDED_PAGES[rel_path].strip() + "\n"
    return body


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
        body = normalize_body(body)
        body = apply_expansion(rel, body)
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
    if not ENABLE_ANSWER_LAYER:
        return
    text = TOP150.read_text(encoding="utf-8")
    text = normalize_body(text)
    text = text.replace(
        "**Questions only — no answers.**",
        "**Questions only on this page — answers live on linked canonical topic pages.**",
    )
    out = []
    for line in text.splitlines():
        m = re.match(
            r"^\| (\d+) \| (.+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| \[([^\]]+)\]\(([^)]+)\) \|",
            line.strip(),
        )
        if m:
            num = int(m.group(1))
            question = m.group(2).strip()
            doc_path = m.group(7).replace(BASE + "/", "").strip("/").rstrip("/")
            if not doc_path.endswith(".md"):
                doc_path += ".md"
            link = deep_dive_link(num, question, doc_path)
            out.append(
                f"| {num} | {question} | {m.group(3).strip()} | {m.group(4).strip()} | "
                f"{m.group(5).strip()} | {link} |"
            )
        else:
            out.append(line.strip())
    TOP150.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    topics = load_topic_order()
    nav_topics = [
        t
        for t in topics
        if not t.startswith("09-interview-guide/")
        and not t.startswith("10-learning-paths/")
    ]
    groups = group_questions_by_page()
    n = update_topic_pages(nav_topics, groups)
    update_top150()
    print(
        f"Phase C complete: expanded {len(EXPANDED_PAGES)} pages, "
        f"updated {n} topic pages with answers, "
        f"P0 mermaid on {len(MERMAID_P0)} pages, Top 150 anchors."
    )


if __name__ == "__main__":
    main()
