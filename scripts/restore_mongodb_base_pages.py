"""Restore MongoDB handbook topic page bodies before re-applying Phase C answers."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from generate_mongodb_handbook_refactor import (
    BASE,
    PATCHERS,
    fix_links,
    patch_architecture,
    patch_indexes,
    patch_performance,
    patch_replication,
)

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "mongodb-cheatsheet"

# flat source -> nested target
MOVED = {
    "documents.md": "01-fundamentals/documents.md",
    "collections.md": "01-fundamentals/collections.md",
    "crud.md": "01-fundamentals/crud.md",
    "atlas-basics.md": "01-fundamentals/atlas-basics.md",
    "architecture.md": "02-core-mongodb/architecture.md",
    "replication.md": "02-core-mongodb/replication.md",
    "sharding.md": "02-core-mongodb/sharding.md",
    "transactions.md": "02-core-mongodb/transactions.md",
    "schema-design.md": "02-core-mongodb/schema-design.md",
    "indexes.md": "03-query-performance/indexes.md",
    "ttl-index.md": "03-query-performance/ttl-index.md",
    "text-search.md": "03-query-performance/text-search.md",
    "geospatial.md": "03-query-performance/geospatial.md",
    "aggregation-pipeline.md": "03-query-performance/aggregation-pipeline.md",
    "performance.md": "04-production-operations/performance.md",
}

NEW_PAGES = [
    "02-core-mongodb/storage-engine.md",
    "03-query-performance/query-optimization.md",
    "03-query-performance/explain-plan.md",
    "04-production-operations/monitoring.md",
    "04-production-operations/troubleshooting.md",
    "04-production-operations/backup-recovery.md",
    "04-production-operations/capacity-planning.md",
    "05-comparisons/mongodb-vs-postgresql.md",
    "05-comparisons/mongodb-vs-cassandra.md",
    "05-comparisons/mongodb-vs-couchbase.md",
]

ANSWER_START = "<!-- interview-answers:start -->"
ANSWER_END = "<!-- interview-answers:end -->"


def git_flat_body(name: str) -> str:
    result = subprocess.run(
        ["git", "show", f"HEAD:content/mongodb-cheatsheet/{name}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return re.sub(r"^---.*?---\n", "", result.stdout, count=1, flags=re.DOTALL)


def strip_answers_from_body(body: str) -> str:
    if ANSWER_START in body:
        body = re.sub(
            rf"\n?{re.escape(ANSWER_START)}[\s\S]*?{re.escape(ANSWER_END)}\n?",
            "\n",
            body,
        )
    body = re.sub(r"\n## See Also[\s\S]*$", "", body)
    body = re.sub(r"\n---\n\n## See Also[\s\S]*$", "", body)
    return body.rstrip() + "\n"


def patch_body(flat: str, body: str) -> str:
    patch = PATCHERS.get(flat)
    body = fix_links(body)
    if patch:
        body = patch(body)
    return body


def preserve_front_matter(path: Path, new_body: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.index("---", 3) + 3
        fm = text[:end]
    else:
        fm = ""
    path.write_text(fm + "\n\n" + new_body.lstrip("\n"), encoding="utf-8")


def restore_moved() -> int:
    n = 0
    for flat, nested in MOVED.items():
        path = HB / nested
        if not path.exists():
            continue
        body = patch_body(flat, git_flat_body(flat))
        preserve_front_matter(path, body)
        n += 1
    return n


def restore_new() -> int:
    n = 0
    for rel in NEW_PAGES:
        path = HB / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        _, body = text, text
        if text.startswith("---"):
            end = text.index("---", 3) + 3
            body = text[end:].lstrip("\n")
        body = strip_answers_from_body(body)
        preserve_front_matter(path, body)
        n += 1
    return n


def main() -> None:
    m = restore_moved()
    n = restore_new()
    print(f"Restored {m} moved pages from git + {n} new pages stripped of answers.")


if __name__ == "__main__":
    main()
