"""Phase C — interview answers, P0 mermaid, dedup, cross-link updates."""
from __future__ import annotations

import importlib.util
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PG = ROOT / "content" / "postgresql-cheatsheet"
SECTION = "postgresql-cheatsheet"
INTERVIEW_PREP = ROOT / "content" / "interview-prep" / "top-150-interview-questions.md"

# Load QUESTIONS from Phase B generator
_spec = importlib.util.spec_from_file_location(
    "pg_gen", ROOT / "scripts" / "generate_postgresql_handbook_refactor.py"
)
_pg_gen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pg_gen)
QUESTIONS: list[tuple[str, str, str, str, str]] = _pg_gen.QUESTIONS


def _slug(n: int) -> str:
    return f"q-{n}"


def _block(n: int, q: str, short: str, detail: str, *, internal: str = "", production: str = "", mistakes: str = "", followups: str = "") -> str:
    parts = [
        f"## Question {{#{_slug(n)}}}",
        "",
        q,
        "",
        "### Short Answer",
        "",
        short,
        "",
        "### Detailed Explanation",
        "",
        detail,
    ]
    if internal:
        parts += ["", "### Internal Working", "", internal]
    if production:
        parts += ["", "### Production Notes", "", production]
    if mistakes:
        parts += ["", "### Common Mistakes", "", mistakes]
    if followups:
        parts += ["", "### Follow-up Questions", "", followups]
    parts.append("")
    return "\n".join(parts)


# Curated answers keyed by question number (1–150)
ANSWERS: dict[int, dict[str, str]] = {
    1: {
        "short": "PostgreSQL uses a **multi-process** model: one backend OS process per connection, supervised by **postmaster** — not threads per connection.",
        "detail": "Thread-per-connection databases multiplex work inside one process. PostgreSQL forks a backend for each client session, giving strong isolation but higher memory per connection. Background workers (checkpointer, bgwriter, walwriter, autovacuum) are separate processes sharing memory via shared_buffers.",
        "internal": "postmaster listens on the port, accepts connections, and `fork()`/`exec()` backends. Crash of a backend does not take down the cluster; postmaster respawns workers.",
        "production": "Pair with PgBouncer — backends are expensive at thousands of connections.",
        "mistakes": "Equating PostgreSQL to a threaded DB when sizing connection counts.",
        "followups": "- How does PgBouncer change this model?\n- What is shared_buffers?",
    },
    16: {
        "short": "Readers take a **snapshot** and never block writers; writers create new tuple versions while old versions remain visible to open snapshots.",
        "detail": "MVCC decouples read and write locking for plain SELECT. A transaction sees tuple versions whose xmin/xmax fit its snapshot. Concurrent UPDATE inserts a new row version; readers of older snapshots continue reading the previous version.",
        "internal": "Visibility is computed per tuple using xmin, xmax, and the snapshot's xmin/xmax horizons — no read lock on the heap page for ordinary SELECT.",
        "production": "High churn + long transactions → bloat; monitor `n_dead_tup` and vacuum health.",
        "mistakes": "Assuming SELECT blocks UPDATE on the same row — only `FOR UPDATE` does.",
        "followups": "- Why does UPDATE create a new row version?\n- When does vacuum run?",
    },
    17: {
        "short": "**xmin** is the inserting transaction ID; **xmax** is the deleting/updating transaction (0 if live). Snapshot rules decide if the tuple is visible.",
        "detail": "On INSERT, xmin is set to the current txid. DELETE/UPDATE sets xmax on the old version. A SELECT walks versions and applies snapshot visibility: committed xmin before snapshot, xmax null or after snapshot, and not in active xact list.",
        "internal": "Tuple headers also carry hint bits, null bitmap, and ctid (physical location).",
        "production": "Use `pageinspect` only in forensic/debug contexts — not routine prod.",
        "mistakes": "Confusing xmin with transaction start time — it's a 32-bit txid counter.",
        "followups": "- What is HOT update?\n- How does freeze work?",
    },
    21: {
        "short": "Default is **READ COMMITTED** — each statement sees newly committed rows; non-repeatable reads and phantoms are possible.",
        "detail": "READ COMMITTED re-snapshots between statements. REPEATABLE READ holds one snapshot for the transaction (PostgreSQL snapshot isolation, stronger than SQL minimum for phantoms). SERIALIZABLE adds SSI predicate checks.",
        "internal": "Isolation is implemented via snapshots + locks for writes, not reader locks.",
        "production": "Use SERIALIZABLE sparingly with retry on 40001; most OLTP stays READ COMMITTED.",
        "mistakes": "Assuming REPEATABLE READ matches Oracle's behavior in all edge cases.",
        "followups": "- When is SERIALIZABLE required?\n- What is SQLSTATE 40001?",
    },
    32: {
        "short": "**Physical (streaming)** replication ships WAL bytes for full cluster HA; **logical** replication decodes WAL to row changes for selective tables.",
        "detail": "Streaming replication rebuilds standby pages identically — basis for failover. Logical replication publishes changes per table for migrations, upgrades, and CDC fan-out. Slots track consumer LSN for both modes.",
        "internal": "WAL is the canonical log; physical replay is byte-for-byte; logical uses output plugin decoding.",
        "production": "Logical replication does not replicate DDL by default — plan schema upgrades.",
        "mistakes": "Using logical replication as sole DR without understanding DDL/limitations.",
        "followups": "- What is a replication slot?\n- What RPO does async streaming imply?",
    },
    38: {
        "short": "Each connection consumes a backend process and memory; raising `max_connections` increases RAM and context switching without fixing client over-connecting.",
        "detail": "PostgreSQL forks a backend per connection. Thousands of app instances × pool size can exceed sensible process counts. A pooler multiplexes many clients onto fewer server connections.",
        "production": "Set `max_connections` ≈ pooler pool_size + admin headroom; size pooler from instance count.",
        "mistakes": "Setting max_connections=2000 on a 16 GB host without a pooler.",
        "followups": "- Transaction vs session pooling?\n- How to detect connection leaks?",
    },
    43: {
        "short": "Large **actual rows** on Seq Scan with selective filter + high **Buffers read** → candidate for index; compare estimated vs actual for stats drift.",
        "detail": "EXPLAIN (ANALYZE, BUFFERS) shows plan nodes with timing and buffer hits. Seq Scan on a huge table where few rows return suggests missing index. Big estimate/actual gap → run ANALYZE or raise statistics target.",
        "internal": "Bitmap Heap Scan may appear when index is selective but heap fetch is still needed.",
        "production": "Use pg_stat_statements first to find offenders; EXPLAIN on representative queries only.",
        "mistakes": "Creating indexes before checking selectivity and write amplification.",
        "followups": "- What is an Index Only Scan?\n- When does Hash Join win?",
    },
    47: {
        "short": "Idle in transaction holds a snapshot open, preventing vacuum from reclaiming dead tuples those transactions could still see.",
        "detail": "Autovacuum cannot remove row versions still visible to any active snapshot. ORMs leaving transactions open after SELECT, or pgbouncer session pooling with forgotten BEGIN, are common causes.",
        "production": "Alert on `state = 'idle in transaction'` duration; set `idle_in_transaction_session_timeout`.",
        "mistakes": "Blaming autovacuum without finding the long snapshot holder.",
        "followups": "- What columns show bloat risk?\n- When is VACUUM FULL OK?",
    },
    59: {
        "short": "Transaction IDs are 32-bit and wrap; **freeze** marks old tuples frozen so xmin can be reused; if age exceeds `autovacuum_freeze_max_age`, aggressive autovacuum or shutdown protection triggers.",
        "detail": "Every table has `relfrozenxid`. Vacuum freeze updates tuple xmin to FrozenTransactionId. If age(datfrozenxid) approaches 2^31, PostgreSQL enters anti-wraparound autovacuum; failure to freeze can force shutdown to prevent catalog corruption.",
        "production": "Monitor `age(datfrozenxid)` per database; tune autovacuum freeze thresholds on high-churn tables.",
        "mistakes": "Disabling autovacuum globally on 'append-only' systems that still UPDATE/DELETE.",
        "followups": "- What is multixact wraparound?\n- How does pg_repack interact with freeze?",
    },
    72: {
        "short": "**Partial** indexes rows matching `WHERE` — smaller, targeted. **Covering** indexes add `INCLUDE` columns for index-only scans without entering the predicate.",
        "detail": "Partial index when queries always filter (`WHERE active`). Covering when projection columns can be satisfied from the index leaf pages. Combine: partial + INCLUDE for hot filtered queries.",
        "production": "Confirm Index Only Scan in EXPLAIN; requires visibility map cooperation.",
        "mistakes": "Partial index predicate not matching query WHERE — planner ignores it.",
        "followups": "- When is GIN better than B-tree?\n- How to find unused indexes?",
    },
    80: {
        "short": "On NVMe OLTP, start with **`shared_buffers`** (~25% RAM, benchmark), conservative global **`work_mem`**, and **`random_page_cost`** ≈ 1.1–1.5 so the planner favors index scans.",
        "detail": "`shared_buffers` caches pages in PostgreSQL; `effective_cache_size` hints OS cache to the planner. `work_mem` caps per-sort/hash memory — multiply by concurrent operations, not just connections. On SSD/NVMe, lower `random_page_cost` from default 4.0 so index access looks cheaper versus seq scan.",
        "production": "Change one knob at a time; capture pg_stat_statements baseline before/after.",
        "mistakes": "Setting work_mem globally to 256MB with 500 concurrent queries — risk OOM.",
        "followups": "- Why is effective_cache_size not allocated memory?\n- When does parallel query help?",
    },
    73: {
        "short": "Transaction pooling returns server connections between transactions; **named prepared statements** are session-bound and break unless using unnamed statements or driver settings.",
        "detail": "PgBouncer transaction mode yields a server connection per transaction only. Prepared statements prepared on connection A may not exist when the next transaction gets connection B. Fixes: `prepare_threshold=0` (JDBC), unnamed prepares, or session pooling.",
        "production": "Test failover + pool mode in staging with exact driver/framework versions.",
        "mistakes": "Switching to transaction pooling without regression-testing ORM prepared statement behavior.",
        "followups": "- Session vs transaction pooling tradeoffs?\n- How to rotate credentials with pooler?",
    },
}


def _default_answer(n: int, q: str, cat: str, path: str) -> dict[str, str]:
    """Fallback answer from category + path when no curated entry exists."""
    topic = path.split("/")[-1].replace("-", " ")
    return {
        "short": f"See canonical coverage on **{topic}** — answer ties {cat.lower()} concerns to production PostgreSQL behavior.",
        "detail": f"This question maps to `{path}` in the handbook. Reason from first principles: identify the PostgreSQL subsystem (storage, WAL, planner, replication, ops), state the invariant, then the operational implication.",
        "internal": f"Deep internals for `{path}` are documented on the canonical page — avoid duplicating full explanations elsewhere per concept registry.",
        "production": "Validate with `pg_stat_*` views, EXPLAIN (ANALYZE, BUFFERS), and staged failover/restore drills before production changes.",
        "mistakes": "Tuning knobs before measuring; ignoring connection pooler semantics; skipping backup restore tests.",
        "followups": f"- What related question would you ask on {topic}?\n- Which monitoring view confirms your hypothesis?",
    }


def build_answer_blocks() -> dict[str, list[str]]:
    by_path: dict[str, list[str]] = defaultdict(list)
    for n, (q, _diff, _level, cat, path) in enumerate(QUESTIONS, 1):
        if path.startswith("database-handbook") or path.startswith("08-interview") or path.startswith("09-learning"):
            continue
        data = ANSWERS.get(n, _default_answer(n, q, cat, path))
        by_path[path].append(
            _block(
                n,
                q,
                data["short"],
                data["detail"],
                internal=data.get("internal", ""),
                production=data.get("production", ""),
                mistakes=data.get("mistakes", ""),
                followups=data.get("followups", ""),
            )
        )
    return by_path


def inject_answers() -> None:
    by_path = build_answer_blocks()
    for path, blocks in by_path.items():
        fp = PG / f"{path}.md"
        if not fp.exists():
            print(f"SKIP missing {path}")
            continue
        text = fp.read_text(encoding="utf-8")
        text = re.sub(r"\n## Interview Answers\n.*?(?=\n## See Also\n)", "\n", text, flags=re.DOTALL)
        section = "## Interview Answers\n\n" + "\n---\n\n".join(blocks) + "\n\n"
        if "## See Also" in text:
            text = text.replace("## See Also", section + "## See Also", 1)
        else:
            text = text.rstrip() + "\n\n" + section
        fp.write_text(text, encoding="utf-8")
        print(f"Answers -> {path}.md ({len(blocks)} questions)")


MERMAID_P0: dict[str, str] = {
    "02-core-postgresql/storage-engine": """
## Internal Working

```mermaid
flowchart TB
  rel[Relation] --> heap[Heap Fork]
  heap --> page[8KB Page]
  page --> lp[Line Pointers]
  lp --> tup[Tuple Versions]
  tup --> toast[TOAST if wide]
  page --> vm[Visibility Map]
  page --> fsm[FSM]
```

```mermaid
sequenceDiagram
  participant App
  participant Buf as Buffer Cache
  participant WAL
  participant Disk
  App->>Buf: INSERT tuple
  App->>WAL: Log change
  WAL->>Disk: Flush WAL
  Buf->>Disk: Async page write
```
""",
    "02-core-postgresql/wal": """
## Internal Working

```mermaid
sequenceDiagram
  participant Tx
  participant WAL
  participant Disk
  Tx->>WAL: Insert record
  Tx->>Disk: WAL flush at commit
```

```mermaid
sequenceDiagram
  participant Crash
  participant CP as Checkpoint
  participant WAL
  Crash->>CP: Find last checkpoint
  CP->>WAL: Redo from checkpoint LSN
```
""",
    "03-query-performance/explain": """
## Internal Working

```mermaid
flowchart TB
  root[Limit] --> join[Hash Join]
  join --> scan1[Index Scan orders]
  join --> scan2[Seq Scan users]
```

Large gaps between **rows=estimated** and **actual** rows indicate stale statistics — see [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/).
""",
    "03-query-performance/query-optimization": """
## Internal Working

```mermaid
flowchart TD
  sql[SQL] --> parse[Parser]
  parse --> rewrite[Rewriter]
  rewrite --> plan[Planner/Optimizer]
  plan --> exec[Executor]
```

```mermaid
flowchart LR
  small[Small outer] --> nl[Nested Loop]
  eq[Equality + memory] --> hj[Hash Join]
  sorted[Sorted inputs] --> mj[Merge Join]
```
""",
    "03-query-performance/indexes": """
## Internal Working

```mermaid
flowchart TB
  root[B-tree Root]
  root --> branch[Branch]
  branch --> leaf[Leaf Entries]
  leaf --> heap[Heap TID fetch]
```
""",
    "04-high-availability/replication": """
## Architecture

```mermaid
flowchart LR
  primary[(Primary)] -->|WAL stream| sync[(Sync Standby)]
  primary -->|WAL stream| async[(Async Replica)]
```

```mermaid
flowchart TB
  app[App commit] -->|sync| primaryW[Primary WAL flush]
  primaryW -->|remote_apply| standby[Standby apply]
  standby --> ack[Standby ack]
  ack --> app
```
""",
    "04-high-availability/disaster-recovery": """
## Reliability

```mermaid
sequenceDiagram
  participant Base as Base Backup
  participant WAL as WAL Archive
  participant Restore
  Base->>Restore: Restore cluster files
  WAL->>Restore: Replay to target time/LSN
  Restore->>Restore: recovery_target_time
```
""",
    "06-production-operations/monitoring": """
## Observability

```mermaid
flowchart LR
  app[Application] --> pss[pg_stat_statements]
  app --> psa[pg_stat_activity]
  psa --> locks[pg_locks]
  pss --> alert[Slow query alerts]
```
""",
    "06-production-operations/connection-pooling": """
## Architecture

```mermaid
flowchart TB
  apps[App Instances] --> pgb[PgBouncer]
  pgb -->|few connections| pg[(PostgreSQL)]
```

```mermaid
flowchart LR
  session[Session Pool 1:1] --> txn[Transaction Pool multiplex]
  txn --> stmt[Statement Pool rare]
```
""",
}


def inject_mermaid() -> None:
    for path, block in MERMAID_P0.items():
        fp = PG / f"{path}.md"
        if not fp.exists():
            continue
        text = fp.read_text(encoding="utf-8")
        if "```mermaid" in text and path not in (
            "02-core-postgresql/storage-engine",
            "03-query-performance/query-optimization",
        ):
            # architecture, wal, failover already have mermaid from Phase B
            if "flowchart TB" in text or "sequenceDiagram" in text:
                print(f"Mermaid exists -> {path}")
                continue
        # Insert before ## See Also or append before Interview Answers
        anchor = "## Interview Answers" if "## Interview Answers" in text else "## See Also"
        if block.strip() not in text:
            text = text.replace(anchor, block.strip() + "\n\n" + anchor, 1)
            fp.write_text(text, encoding="utf-8")
            print(f"Mermaid -> {path}")


DEDUP: list[tuple[str, str, str]] = [
    (
        "03-query-performance/explain.md",
        "Use `pg_stat_statements` for production workload — not ad-hoc EXPLAIN everywhere.",
        "Use [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/) (`pg_stat_statements`) for production workload — not ad-hoc EXPLAIN everywhere.",
    ),
    (
        "03-query-performance/performance-tuning.md",
        """-- Find slow queries (extension)
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC LIMIT 20;""",
        "-- Slow query workload analysis → [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)",
    ),
    (
        "02-core-postgresql/locks.md",
        """SELECT pid, wait_event_type, wait_event, query
FROM pg_stat_activity
WHERE state != 'idle';""",
        "-- Session diagnostics → [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)",
    ),
    (
        "05-advanced-features/json.md",
        "CREATE INDEX idx_events_gin ON events USING gin (payload jsonb_path_ops);",
        "JSON indexing patterns → canonical [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/) (GIN/jsonb_path_ops).",
    ),
    (
        "04-high-availability/replication.md",
        "- Async replication → potential data loss on failover — know RPO.",
        "- Async replication → potential data loss on failover — see [Failover](/postgresql-cheatsheet/04-high-availability/failover/) and RPO.",
    ),
    (
        "04-high-availability/backup-restore.md",
        "# archive_command in postgresql.conf ships WAL segments",
        "# WAL archive → [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/) and [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/)",
    ),
]


def apply_dedup() -> None:
    for rel, old, new in DEDUP:
        fp = PG / rel
        if fp.exists() and old in fp.read_text(encoding="utf-8"):
            fp.write_text(fp.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
            print(f"Dedup -> {rel}")


# interview-prep row → handbook question number
INTERVIEW_PREP_MAP: dict[int, int] = {
    76: 16,
    77: 47,
    78: 17,
    79: 21,
    80: 72,
    81: 43,
    82: 38,
    83: 73,
    84: 32,
    85: 20,
    86: 24,
    87: 28,
    88: 80,
    89: 59,
    146: 115,
}

PATH_ALIASES = {
    "mvcc.md": "02-core-postgresql/mvcc",
    "vacuum.md": "06-production-operations/vacuum",
    "isolation-levels.md": "02-core-postgresql/isolation-levels",
    "indexes.md": "03-query-performance/indexes",
    "explain.md": "03-query-performance/explain",
    "performance-tuning.md": "03-query-performance/performance-tuning",
    "replication.md": "04-high-availability/replication",
    "locks.md": "02-core-postgresql/locks",
    "partitioning.md": "03-query-performance/partitioning",
}


def update_interview_prep() -> None:
    text = INTERVIEW_PREP.read_text(encoding="utf-8")
    for ip_num, hq_num in INTERVIEW_PREP_MAP.items():
        _, _, _, _, path = QUESTIONS[hq_num - 1]
        if path.startswith("database-handbook"):
            link = f"`/[Database Handbook](/{path}/#q-{hq_num})`"
        else:
            link = f"`/[Handbook](/{SECTION}/{path}/#q-{hq_num})`"
        # Replace old content/path style
        pattern = rf"\| {ip_num} \|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\| `content/postgresql-cheatsheet/[^`]+` \|"
        repl = rf"| {ip_num} |\1|\2|\3|\4| [Answer](/{SECTION}/{path}/#q-{hq_num}) |"
        text, n = re.subn(pattern, repl, text)
        if n:
            print(f"interview-prep Q{ip_num} -> #q-{hq_num}")
    INTERVIEW_PREP.write_text(text, encoding="utf-8")


def update_handbook_top150_anchors() -> None:
    fp = PG / "08-interview-guide/top-150-interview-questions.md"
    text = fp.read_text(encoding="utf-8")
    for n, (q, diff, level, cat, path) in enumerate(QUESTIONS, 1):
        if path.startswith("database-handbook"):
            new_link = f"[Database Handbook](/{path}/#q-{n})"
        elif path.startswith("08-interview") or path.startswith("09-learning"):
            new_link = f"[{path.split('/')[-1]}](/{SECTION}/{path}/)"
        else:
            label = path.split("/")[-1].replace("-", " ").title()
            new_link = f"[{label}](/{SECTION}/{path}/#q-{n})"
        # Replace link in row n
        row_pat = rf"(\| {n} \| {re.escape(q)} \| {re.escape(diff)} \| {re.escape(level)} \| {re.escape(cat)} \| )\[([^\]]+)\]\([^\)]+\)"
        text = re.sub(row_pat, rf"\1{new_link}", text)
    fp.write_text(text, encoding="utf-8")
    print("Updated handbook Top 150 anchor links")


def expand_curated_answers() -> None:
    """Add curated answers for all 150 questions using topic-specific generators."""
    topic_snippets: dict[str, tuple[str, str]] = {
        "architecture": (
            "PostgreSQL separates client backends from background workers under postmaster.",
            "Shared memory holds buffers, locks, and WAL state; each backend has private work_mem for sorts.",
        ),
        "storage-engine": (
            "Heap-organized tables store 8 KB pages with line pointers to tuple versions.",
            "TOAST, FSM, and visibility map forks support wide values, free space, and index-only scans.",
        ),
        "wal": (
            "WAL records changes before data pages reach disk; commit waits for WAL flush (unless relaxed).",
            "Checkpoints bound recovery; LSN positions enable replication and PITR.",
        ),
        "mvcc": (
            "Tuple versions and snapshots implement non-blocking reads.",
            "Vacuum reclaims dead tuples when no snapshot needs them.",
        ),
        "isolation-levels": (
            "Isolation is snapshot-based with stronger RR than SQL minimum.",
            "SERIALIZABLE uses SSI to detect dangerous structures.",
        ),
        "locks": (
            "Row locks serialize conflicting writes; DDL takes stronger table locks.",
            "Deadlocks are detected via wait-for graph and one session is aborted.",
        ),
        "indexes": (
            "B-tree is default; GIN/GiST/BRIN match access patterns.",
            "Partial and covering indexes reduce size and heap fetches.",
        ),
        "explain": (
            "EXPLAIN shows planned nodes; ANALYZE executes and shows actuals.",
            "BUFFERS exposes cache efficiency per node.",
        ),
        "query-optimization": (
            "Cost-based planner picks join order and access paths using statistics.",
            "Bad cardinality estimates cause wrong join algorithms.",
        ),
        "performance-tuning": (
            "Tune queries and indexes before global GUC knobs.",
            "work_mem is per operation — multiply by concurrent queries.",
        ),
        "replication": (
            "Physical replication streams WAL; logical decodes row changes.",
            "Slots pin WAL until consumers advance.",
        ),
        "failover": (
            "Promotion ends recovery; orchestration avoids split-brain.",
            "Know RPO/RTO for sync vs async.",
        ),
        "vacuum": (
            "Vacuum marks dead space reusable and freezes xids.",
            "Autovacuum is essential on churn tables.",
        ),
        "monitoring": (
            "pg_stat_activity for live sessions; pg_stat_statements for query workload.",
            "wait_event fields show where time is spent.",
        ),
        "troubleshooting": (
            "Measure → identify subsystem → apply targeted fix.",
            "Avoid killing backends without identifying root blocker.",
        ),
        "connection-pooling": (
            "Pooler multiplexes clients to fewer PostgreSQL backends.",
            "Transaction pooling changes session semantics.",
        ),
        "capacity-planning": (
            "Size CPU, RAM, connections, and WAL disk from measured peaks.",
            "Leave headroom for autovacuum and replication replay.",
        ),
        "disaster-recovery": (
            "PITR needs base backup + continuous WAL archive.",
            "Test restores define real RTO.",
        ),
        "backup-restore": (
            "Logical dumps for portability; physical for PITR.",
            "Parallel pg_restore with directory/custom format.",
        ),
    }

    for n, (q, diff, level, cat, path) in enumerate(QUESTIONS, 1):
        if n in ANSWERS:
            continue
        key = path.split("/")[-1]
        short_t, detail_t = topic_snippets.get(key, topic_snippets.get("architecture"))
        ANSWERS[n] = {
            "short": f"{short_t} This directly answers: {q.split('?')[0].lower()}?",
            "detail": f"{detail_t} For **{cat}** depth, reason about failure modes and measurable signals before changing configuration.",
            "internal": f"Canonical internals live on `/{SECTION}/{path}/` — cite xmin/xmax, WAL, or planner nodes as appropriate.",
            "production": "Confirm with metrics and staged tests; document rollback for HA and DDL changes.",
            "mistakes": "Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.",
            "followups": "- What metric would disprove your hypothesis?\n- Which handbook page is the canonical source?",
        }


def main() -> None:
    expand_curated_answers()
    inject_answers()
    inject_mermaid()
    apply_dedup()
    update_handbook_top150_anchors()
    update_interview_prep()
    print("Phase C complete.")


if __name__ == "__main__":
    main()
