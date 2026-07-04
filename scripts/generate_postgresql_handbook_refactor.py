"""Phase B — restructure postgresql-cheatsheet into numbered modules."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PG = ROOT / "content" / "postgresql-cheatsheet"
DATA = ROOT / "data"
DATE = "2026-07-03T12:00:00+00:00"
SECTION = "postgresql-cheatsheet"

FM = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
interviewHandbook: true{aliases}
---

"""


def w(rel: str, body: str, *, alias: str | None = None, **fm) -> None:
    path = PG / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    aliases = ""
    if alias:
        aliases = f'\naliases:\n  - {alias}'
    path.write_text(FM.format(date=DATE, aliases=aliases, **fm) + body.strip() + "\n", encoding="utf-8")


def migrate(rel_src: str, rel_dst: str, *, alias: str, **fm) -> None:
    src = PG / rel_src
    if not src.exists():
        src = PG / Path(rel_dst).name  # flat fallback
    if not src.exists():
        raise FileNotFoundError(rel_src)
    text = src.read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    body = body.replace("## Executive Summary", "## Quick Revision")
    body = body.replace("## Related Topics", "## See Also")
    body = body.replace("PostgreSQL Cheatsheet Index", "PostgreSQL Handbook")
    body = re.sub(
        r"\(/postgresql-cheatsheet/([a-z0-9-]+)/\)",
        lambda m: f"(/{SECTION}/{_OLD_TO_NEW.get(m.group(1), m.group(1))}/)",
        body,
    )
    w(rel_dst, body, alias=alias, **fm)


_OLD_TO_NEW: dict[str, str] = {
    "installation": "01-fundamentals/installation",
    "sql-basics": "01-fundamentals/sql-basics",
    "ddl": "01-fundamentals/ddl",
    "dml": "01-fundamentals/dml",
    "joins": "01-fundamentals/joins",
    "ctes": "01-fundamentals/ctes",
    "window-functions": "01-fundamentals/window-functions",
    "indexes": "03-query-performance/indexes",
    "explain": "03-query-performance/explain",
    "performance-tuning": "03-query-performance/performance-tuning",
    "partitioning": "03-query-performance/partitioning",
    "sharding": "03-query-performance/sharding",
    "mvcc": "02-core-postgresql/mvcc",
    "transactions": "02-core-postgresql/transactions",
    "isolation-levels": "02-core-postgresql/isolation-levels",
    "locks": "02-core-postgresql/locks",
    "replication": "04-high-availability/replication",
    "backup-restore": "04-high-availability/backup-restore",
    "views": "05-advanced-features/views",
    "materialized-views": "05-advanced-features/materialized-views",
    "json": "05-advanced-features/json",
    "functions": "05-advanced-features/functions",
    "triggers": "05-advanced-features/triggers",
    "stored-procedures": "05-advanced-features/stored-procedures",
    "vacuum": "06-production-operations/vacuum",
}


def section_indexes() -> None:
    for folder, title, desc, mod in [
        ("01-fundamentals", "Fundamentals", "SQL, DDL/DML, joins, CTEs, and window functions.", 1),
        ("02-core-postgresql", "Core PostgreSQL", "Architecture, storage, WAL, MVCC, transactions, and locking.", 2),
        ("03-query-performance", "Query Performance", "Indexes, EXPLAIN, planner, tuning, partitioning, and sharding.", 3),
        ("04-high-availability", "High Availability", "Replication, failover, backup, and disaster recovery.", 4),
        ("05-advanced-features", "Advanced Features", "Functions, procedures, triggers, views, JSON.", 5),
        ("06-production-operations", "Production Operations", "Vacuum, monitoring, pooling, troubleshooting, capacity.", 6),
        ("07-comparisons", "Comparisons", "PostgreSQL vs MySQL, Oracle, and MongoDB.", 7),
        ("08-interview-guide", "Interview Guide", "150-question bank and role-specific subsets.", 8),
        ("09-learning-paths", "Learning Paths", "Curated reading orders by seniority.", 9),
    ]:
        w(
            f"{folder}/_index.md",
            f"# {title}\n\n{desc}",
            title=title,
            desc=desc,
            short=title,
            mod=mod,
            mod_title="PostgreSQL Handbook",
            ref=f"{mod}.0",
            weight=mod * 100,
        )


def handbook_index() -> None:
    w(
        "_index.md",
        """# PostgreSQL Handbook

Interview-first knowledge base for **Senior Engineers**, **Technical Leads**, and **Architects** (6+ years).

## Learning Paths

| Track | Start here | Goal |
| :--- | :--- | :--- |
| **Senior engineer** | [Core PostgreSQL](/postgresql-cheatsheet/02-core-postgresql/) → [Query Performance](/postgresql-cheatsheet/03-query-performance/) | Internals-aware SQL and tuning |
| **Lead** | [Production Operations](/postgresql-cheatsheet/06-production-operations/) | Monitoring, incidents, capacity |
| **Architect** | [HA](/postgresql-cheatsheet/04-high-availability/) → [Comparisons](/postgresql-cheatsheet/07-comparisons/) | Platform ADRs and migration |
| **Interview cram** | [Top 150 Questions](/postgresql-cheatsheet/08-interview-guide/top-150-interview-questions/) | Mapped deep dives |

## Modules

1. **Fundamentals** — SQL, DDL/DML, joins, CTEs
2. **Core PostgreSQL** — architecture, storage engine, WAL, MVCC, transactions, locks
3. **Query Performance** — indexes, EXPLAIN, planner, tuning, partitioning
4. **High Availability** — replication, failover, backup, DR
5. **Advanced Features** — server-side programming, JSON, mat views
6. **Production Operations** — vacuum, monitoring, pooling, troubleshooting
7. **Comparisons** — vs MySQL, Oracle, MongoDB
8. **Interview Guide** — 150 questions + subsets
9. **Learning Paths** — curated schedules

See also: [Database Handbook — PostgreSQL](/database-handbook/postgresql/) · [How to Choose a Database](/technology-playbook/how-to-choose-database/)
""",
        title="PostgreSQL Handbook",
        desc="PostgreSQL internals, performance, HA, and operations for senior engineers and architects.",
        short="Handbook",
        mod=0,
        mod_title="PostgreSQL Handbook",
        ref="0",
        weight=1,
    )


def new_core_pages() -> None:
    w(
        "02-core-postgresql/architecture.md",
        """## Quick Revision

- **postmaster** supervises shared memory and spawns backends per connection.
- Background workers: **checkpointer**, **background writer**, **WAL writer**, **autovacuum**.
- Clients should use a **pooler** in microservice deployments — see [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/).

## Core Concepts

| Process | Role |
| :--- | :--- |
| postmaster | Parent; manages lifecycle |
| backend | One per client session (or pooler connection) |
| checkpointer | Writes checkpoint records; advances redo horizon |
| bgwriter | Dirty page write-ahead to reduce checkpoint spikes |
| walwriter | Flushes WAL buffers |
| autovacuum launcher/worker | Dead tuple reclaim |

## Internal Working

Connection flow: client → (PgBouncer) → postmaster forks backend → parses SQL → planner → executor. Shared memory holds **buffer pool**, lock tables, WAL buffers. Per-backend memory includes `work_mem` for sorts/hashes.

## Architecture

```mermaid
flowchart TB
  apps[Application Tier] --> pool[PgBouncer]
  pool --> pm[postmaster]
  pm --> be1[backend]
  pm --> be2[backend]
  pm --> bg[background workers]
  bg --> shm[(shared_buffers + WAL)]
  shm --> disk[(data + WAL files)]
```

## Design Tradeoffs

| Choice | Trade-off |
| :--- | :--- |
| Direct connections | Simple; poor beyond ~few hundred connections |
| Transaction pooling | High density; breaks session features |
| Single large instance | Strong consistency; vertical scale ceiling |

## Production Patterns

- One primary writer; scale reads with replicas + routing.
- Separate **WAL/disk** from data volume on cloud NVMe where possible.
- `max_connections` conservative; pooler mandatory for Java/Node fleets.

## Observability

`pg_stat_activity`, `pg_stat_bgwriter`, `pg_stat_database`, OS iowait and memory pressure.

## See Also

- [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/)
- [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/)
- [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)
""",
        title="PostgreSQL Architecture",
        desc="Process model, shared memory, and background workers for production deployments.",
        short="Architecture",
        mod=2,
        mod_title="Core PostgreSQL",
        ref="2.1",
        weight=201,
    )

    w(
        "02-core-postgresql/storage-engine.md",
        """## Quick Revision

- Tables stored in **heap** files (8 KB **pages**).
- **TOAST** stores oversized varlena values out-of-line.
- **FSM** tracks free space; **Visibility Map** enables index-only scans and vacuum skips.
- **Buffer cache** (`shared_buffers`) mirrors pages in RAM.

## Core Concepts

| Component | Function |
| :--- | :--- |
| Heap page | Line pointers → tuple versions |
| Tuple header | `xmin`, `xmax`, `ctid`, null bitmap |
| TOAST table | Compressed/external storage for wide columns |
| FSM | Page free-space hints for inserts |
| Visibility Map | All-visible / all-frozen flags per page |
| Buffer pool | LRU-ish page cache in shared memory |

## Internal Working

**INSERT**: find page with space (FSM) → write tuple → WAL → buffer dirty.**UPDATE** (non-HOT): new tuple version + index updates; old version dead until vacuum.**HOT update**: same page, no index update if indexed columns unchanged.

## Architecture

```mermaid
flowchart TB
  rel[Relation] --> main[Main Fork]
  main --> page[8KB Pages]
  page --> tup[Tuples]
  tup --> toast[TOAST fork if wide]
  page --> fsm[FSM fork]
  page --> vm[Visibility Map fork]
```

## Design Tradeoffs

| Pattern | Effect |
| :--- | :--- |
| Wide JSON/text columns | TOAST I/O on large reads |
| Fillfactor < 100 | Room for HOT updates; more bloat headroom |
| Low shared_buffers | More OS cache reliance — test on your OS |

## Production Patterns

- Monitor bloat on high-churn tables — [VACUUM](/postgresql-cheatsheet/06-production-operations/vacuum/).
- `pgstattuple` / `pgstatindex` for forensic bloat measurement.
- Index-only scans require VM bit + heap visibility recheck.

## Troubleshooting

| Symptom | Check |
| :--- | :--- |
| Table larger than row count suggests | Dead tuples / bloat → `n_dead_tup` |
| Slow wide-row reads | TOAST fetches — column design |

## Interview Questions

- Explain heap page layout and line pointers.
- When does HOT update apply?
- What does the visibility map enable?

## See Also

- [MVCC](/postgresql-cheatsheet/02-core-postgresql/mvcc/)
- [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/)
- [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/)
""",
        title="Storage Engine",
        desc="Heap pages, TOAST, FSM, visibility map, and buffer cache internals.",
        short="Storage",
        mod=2,
        mod_title="Core PostgreSQL",
        ref="2.2",
        weight=202,
    )

    w(
        "02-core-postgresql/wal.md",
        """## Quick Revision

- Every commit persists **WAL** before data pages (write-ahead logging).
- **LSN** monotonically identifies WAL position.
- **Checkpoints** bound crash recovery time.
- WAL is the foundation for **streaming replication** and **PITR**.

## Core Concepts

| Term | Meaning |
| :--- | :--- |
| WAL segment | Typically 16 MB file of log records |
| LSN | Log Sequence Number — replay pointer |
| Checkpoint | Consistent recovery starting point |
| `archive_command` | Ship completed segments for DR |
| `pg_switch_wal()` | Force segment rotation before promotion |

## Internal Working

**Commit path**: record changes in WAL buffer → `XLOG_FLUSH` → mark transaction committed in CLOG → return to client. Crash recovery **replays** WAL from last checkpoint. Standbys **replay** same WAL stream.

## Architecture

```mermaid
sequenceDiagram
  participant Tx as Transaction
  participant WAL as WAL Buffer
  participant Disk as WAL Disk
  participant Data as Data Pages
  Tx->>WAL: Insert log records
  Tx->>Disk: Flush WAL on commit
  Note over Data: Data pages may lag WAL
```

## Reliability

- Place WAL on **durable low-latency** storage — NVMe preferred.
- `synchronous_commit` and replication quorum control durability vs latency.
- Monitor WAL generation rate for disk and replica capacity.

## Production Patterns

- Enable `wal_compression` on busy OLTP if CPU allows.
- Size `max_wal_size` to avoid checkpoint storms — see [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/).
- Base backup + archived WAL for [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/).

## Troubleshooting

| Symptom | Likely cause |
| :--- | :--- |
| Disk filling | Replication slot lag or archive failure |
| Slow commits | `synchronous_commit=on` + slow sync replica |

## See Also

- [Replication](/postgresql-cheatsheet/04-high-availability/replication/)
- [Backup & Restore](/postgresql-cheatsheet/04-high-availability/backup-restore/)
- [Failover](/postgresql-cheatsheet/04-high-availability/failover/)
""",
        title="WAL Internals",
        desc="Write-ahead log, checkpoints, crash recovery, and replication foundation.",
        short="WAL",
        mod=2,
        mod_title="Core PostgreSQL",
        ref="2.3",
        weight=203,
    )


def new_performance_ops_pages() -> None:
    w(
        "03-query-performance/query-optimization.md",
        """## Quick Revision

- **Parser** → **rewriter** → **planner** → **executor**.
- Planner uses **statistics** and **cost model** (seq_page_cost, cpu_tuple_cost, …).
- Bad cardinality estimates → wrong join order — fix stats before knobs.
- **Parallel query** uses gather workers for large scans/aggregates.

## Core Concepts

| Stage | Output |
| :--- | :--- |
| Parser | Query tree |
| Planner | Cheapest path (join order, access methods) |
| Executor | Tuple pipeline |
| `pg_statistic` | Column histograms, ndistinct |
| Extended stats | Multivariate ndistinct, dependencies |

## Internal Working

Join planning: nested loop (small outer), hash join (equality, memory-bound), merge join (sorted inputs). **Genetic** optimizer kicks in for many-table joins. CTE inlining controlled by `MATERIALIZED` hints — see [CTEs](/postgresql-cheatsheet/01-fundamentals/ctes/).

## Design Tradeoffs

| Tuning | Risk |
| :--- | :--- |
| Disable seqscan globally | Hides planner mistakes |
| Raise `default_statistics_target` | Slower ANALYZE; better estimates |
| Force parallel | CPU contention on OLTP |

## Production Patterns

- Run `ANALYZE` after large data changes.
- Use `EXPLAIN (ANALYZE, BUFFERS)` — [EXPLAIN](/postgresql-cheatsheet/03-query-performance/explain/).
- `pg_stat_statements` for workload-wide regressions — [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/).

## See Also

- [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/)
- [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/)
- [Cost-Based Optimization (generic)](/database-handbook/cost-based-query-optimization/)
""",
        title="Query Optimization",
        desc="Planner, cost estimation, statistics, cardinality, joins, and parallel query.",
        short="Optimizer",
        mod=3,
        mod_title="Query Performance",
        ref="3.3",
        weight=303,
    )

    w(
        "04-high-availability/failover.md",
        """## Quick Revision

- **Streaming replication** keeps standby in recovery mode replaying WAL.
- **Promotion** ends recovery and accepts writes — `pg_ctl promote` or Patroni.
- Know **RPO** (async data loss window) and **RTO** (time to writable primary).
- Use orchestration (Patroni, repmgr, cloud HA) — manual promotion is last resort.

## Core Concepts

| Mode | RPO |
| :--- | :--- |
| Async replication | May lose un-replicated WAL |
| Sync `remote_write` | WAL received on standby |
| Sync `remote_apply` | Applied on standby — tighter |
| Quorum commit | Majority standbys |

## Architecture

```mermaid
flowchart TB
  etcd[(DCS etcd/consul)] --> patroni[Patroni]
  patroni --> primary[(Primary)]
  patroni --> sync[(Sync Standby)]
  patroni --> async[(Async Replica)]
  primary -->|WAL stream| sync
  primary -->|WAL stream| async
```

## Production Patterns

- `pg_switch_wal()` before controlled failover.
- Rewind or rebuild orphaned old primary after split-brain.
- Connection strings via VIP, DNS, or pooler with failover hooks.

## Reliability

- Test failover quarterly — untested HA fails in incidents.
- Monitor replication lag bytes and `pg_stat_replication` state.

## See Also

- [Replication](/postgresql-cheatsheet/04-high-availability/replication/)
- [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/)
- [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/)
""",
        title="Failover & HA",
        desc="Streaming replication promotion, Patroni, and HA architecture patterns.",
        short="Failover",
        mod=4,
        mod_title="High Availability",
        ref="4.2",
        weight=402,
    )

    w(
        "04-high-availability/disaster-recovery.md",
        """## Quick Revision

- **PITR** = base backup + continuous WAL archive → recover to timestamp/LSN.
- Define **RPO** (max acceptable data loss) and **RTO** (max downtime).
- Logical backups (`pg_dump`) are portable but not PITR.
- Test restores — backup without restore test is incomplete.

## Core Concepts

| Method | PITR | Granularity |
| :--- | :---: | :--- |
| `pg_dump` / `pg_restore` | No | DB/schema/table |
| Base backup + WAL archive | Yes | Cluster |
| Storage snapshot + WAL | Yes | Cluster (vendor-dependent) |

## Production Patterns

- `archive_command` or `archive_library` ships WAL to object storage.
- `recovery_target_time` for point-in-time restore.
- 3-2-1 backup rule: 3 copies, 2 media types, 1 offsite.

## Reliability

| Tier | RPO | RTO |
| :--- | :--- | :--- |
| Logical nightly dump | Up to 24h | Hours |
| WAL archive + daily base | Minutes | Tens of minutes |
| Sync replica + auto failover | ~0 | Minutes |

## See Also

- [Backup & Restore](/postgresql-cheatsheet/04-high-availability/backup-restore/)
- [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/)
- [Failover](/postgresql-cheatsheet/04-high-availability/failover/)
""",
        title="Disaster Recovery",
        desc="PITR, WAL recovery, backup strategy, RPO, and RTO planning.",
        short="DR",
        mod=4,
        mod_title="High Availability",
        ref="4.4",
        weight=404,
    )

    w(
        "06-production-operations/monitoring.md",
        """## Quick Revision

- **`pg_stat_activity`** — who is connected and what they run.
- **`pg_stat_statements`** — normalized query stats (extension).
- **`pg_locks`** — lock waits and blockers.
- **Wait events** — where time is spent (IO, Lock, LWLock, …).

## Core Concepts

| View / Extension | Use |
| :--- | :--- |
| `pg_stat_activity` | Active/idle, wait_event, query |
| `pg_stat_statements` | calls, mean_time, rows, shared_blks |
| `pg_locks` + `pg_blocking_pids()` | Blocker chains |
| `pg_stat_user_tables` | seq_scan vs idx_scan, dead tuples |
| `pg_stat_replication` | Replica lag, sync state |

## Quick Reference

```sql
SELECT pid, usename, state, wait_event_type, wait_event, left(query, 80)
FROM pg_stat_activity
WHERE state <> 'idle' ORDER BY query_start;

SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 20;

SELECT l.pid, pg_blocking_pids(l.pid) AS blockers, a.query
FROM pg_locks l JOIN pg_stat_activity a ON a.pid = l.pid
WHERE NOT l.granted;
```

## Production Patterns

- Export metrics to Prometheus (`postgres_exporter`) or cloud monitor.
- Alert: connection count, replication lag, oldest xmin, disk usage, checkpoint frequency.
- Correlate app traces with `pg_stat_activity.application_name`.

## See Also

- [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/)
- [EXPLAIN](/postgresql-cheatsheet/03-query-performance/explain/)
- [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/)
""",
        title="Monitoring",
        desc="pg_stat_activity, pg_stat_statements, pg_locks, wait events, slow query analysis.",
        short="Monitoring",
        mod=6,
        mod_title="Production Operations",
        ref="6.2",
        weight=602,
    )

    w(
        "06-production-operations/connection-pooling.md",
        """## Quick Revision

- PostgreSQL **process-per-connection** — thousands of app connections exhaust RAM/CPU.
- **PgBouncer** multiplexes clients onto fewer server connections.
- **Transaction pooling** — highest density; breaks prepared statements and some session features.
- **Session pooling** — safer semantics; lower multiplexing.

## Core Concepts

| Pool mode | Semantics |
| :--- | :--- |
| Session | 1:1 for client session lifetime |
| Transaction | Server conn only for one transaction |
| Statement | Rare; very restrictive |

## Design Tradeoffs

| Setting | Effect |
| :--- | :--- |
| `pool_size` per user/db | Cap backend usage |
| `max_client_conn` | Front-door limit |
| Prepared statements in txn mode | Must use unnamed or disable — driver-specific |

## Production Patterns

- Size: `(num_app_instances × pool_per_instance) ≤ max_connections − admin headroom`.
- Place pooler close to apps or on same host as PG for latency.
- Use `DISCARD ALL` / reset query on server connection checkout in txn mode.

## See Also

- [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/)
- [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/)
- [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/)
""",
        title="Connection Pooling",
        desc="PgBouncer, connection limits, pool sizing, transaction vs session pooling.",
        short="Pooling",
        mod=6,
        mod_title="Production Operations",
        ref="6.4",
        weight=604,
    )

    w(
        "06-production-operations/troubleshooting.md",
        """## Quick Revision

- **Slow query** → `pg_stat_statements` → `EXPLAIN (ANALYZE, BUFFERS)`.
- **Blocking** → `pg_blocking_pids()` → kill blocker or fix app lock order.
- **Bloat** → long transactions + autovacuum lag → [VACUUM](/postgresql-cheatsheet/06-production-operations/vacuum/).
- **Replication lag** → network, replay, slots, sync conflicts.

## Troubleshooting

| Symptom | First checks | Action |
| :--- | :--- | :--- |
| Slow queries | `pg_stat_statements`, explain | Index/stats/plan fix |
| Deadlock | `deadlock_detected` in logs | Retry txn; consistent lock order |
| Blocking | `pg_locks`, blockers | Shorten txn; `pg_cancel_backend` |
| Bloat | `n_dead_tup`, long `xmin` | Kill idle in transaction; tune autovacuum |
| Replica lag | `pg_stat_replication` | Index on replica; parallel apply; network |
| Connections exhausted | `pg_stat_activity` count | Pooler; fix connection leaks |
| WAL disk full | `pg_replication_slots` | Drop stale slot; fix archive |

```mermaid
flowchart TD
  slow[Slow query reported] --> pss[pg_stat_statements top]
  pss --> explain[EXPLAIN ANALYZE BUFFERS]
  explain --> idx{Seq scan on large table?}
  idx -->|yes| addidx[Add/tune index + ANALYZE]
  idx -->|no| plan[Check join order / stats / spill]
```

## See Also

- [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)
- [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/)
- [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/)
""",
        title="Troubleshooting",
        desc="Deadlocks, blocking, slow queries, bloat, replication lag, autovacuum, connections.",
        short="Troubleshooting",
        mod=6,
        mod_title="Production Operations",
        ref="6.3",
        weight=603,
    )

    w(
        "06-production-operations/capacity-planning.md",
        """## Quick Revision

- **CPU**: active queries + parallel workers + autovacuum.
- **RAM**: `shared_buffers` + `work_mem` × concurrent sorts + OS cache.
- **Connections**: apps × pool size ≤ `max_connections`.
- **Storage**: data + indexes + WAL + bloat headroom + retention.

## Core Concepts

| Resource | Heuristic starting point |
| :--- | :--- |
| `shared_buffers` | 25% RAM (benchmark on large hosts) |
| `effective_cache_size` | 50–75% RAM (planner hint) |
| `work_mem` | Conservative global; raise per-role/session for reports |
| WAL disk | Sustained write MB/s × retention window |
| Replicas | +read CPU; replay can lag on CPU-bound replicas |

## Scalability

- Partition before single-table maintenance becomes painful.
- Read replicas scale reads, not writes — [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/) for write scale-out.

## See Also

- [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/)
- [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/)
- [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/)
""",
        title="Capacity Planning",
        desc="CPU, memory, connection, and storage sizing with growth estimation.",
        short="Capacity",
        mod=6,
        mod_title="Production Operations",
        ref="6.5",
        weight=605,
    )


def comparison_pages() -> None:
    w(
        "07-comparisons/postgresql-vs-mysql.md",
        """## Quick Revision

- PostgreSQL: stronger **SQL standard**, **MVCC**, **extensions**, **JSONB**, advanced indexing.
- MySQL/InnoDB: mature replication ecosystems; workload fit depends on team and cloud.
- Choose PG for complex queries, constraints, extensions; validate ops model for either.

## Design Tradeoffs

| Dimension | PostgreSQL | MySQL (InnoDB) |
| :--- | :--- | :--- |
| MVCC model | Heap MVCC | Undo log + clustered PK |
| SQL/features | Window functions, CTEs, rich types | Improving; dialect differs |
| Replication | Physical + logical | Binlog async/semi-sync |
| Extensions | PostGIS, pgvector, … | Limited |
| JSON | jsonb + GIN | JSON type; indexing differs |

## Architect Notes

- Migration: watch sequences, `ENUM`, stored procedure dialect, and isolation semantics.
- Link: [Database Handbook — PostgreSQL](/database-handbook/postgresql/).

## See Also

- [PostgreSQL vs Oracle](/postgresql-cheatsheet/07-comparisons/postgresql-vs-oracle/)
- [PostgreSQL vs MongoDB](/postgresql-cheatsheet/07-comparisons/postgresql-vs-mongodb/)
""",
        title="PostgreSQL vs MySQL",
        desc="Architect comparison — OLTP fit, replication, SQL, and migration considerations.",
        short="vs MySQL",
        mod=7,
        mod_title="Comparisons",
        ref="7.1",
        weight=701,
    )

    w(
        "07-comparisons/postgresql-vs-oracle.md",
        """## Quick Revision

- Oracle: RAC, mature enterprise tooling, PL/SQL ecosystem, commercial licensing.
- PostgreSQL: open-source, extensible, strong SQL — common Oracle migration target.
- Plan for SQL/procedure rewrite, partitioning, and HA model differences.

## Design Tradeoffs

| Area | Oracle | PostgreSQL |
| :--- | :--- | :--- |
| HA clustering | RAC | Streaming + Patroni |
| Partitioning | Mature reference partitioning | Declarative PG 10+ |
| Licensing | Core/CAL/processor | OSS + support vendors |
| Tooling | AWR, RMAN | pg_stat_*, pgBackRest, cloud PITR |

## See Also

- [Oracle vs PostgreSQL (ADR)](/database-handbook/oracle-vs-postgresql/)
- [Failover](/postgresql-cheatsheet/04-high-availability/failover/)
""",
        title="PostgreSQL vs Oracle",
        desc="Migration programs, feature parity, licensing, and HA comparison.",
        short="vs Oracle",
        mod=7,
        mod_title="Comparisons",
        ref="7.2",
        weight=702,
    )

    w(
        "07-comparisons/postgresql-vs-mongodb.md",
        """## Quick Revision

- MongoDB: flexible schema, horizontal shard-by-default, document model.
- PostgreSQL: relational integrity, JOINs, ACID, jsonb for hybrid workloads.
- Hybrid: PG jsonb + indexes when you need transactions with semi-structured fields.

## Design Tradeoffs

| Workload | Favor |
| :--- | :--- |
| Ad hoc analytics across entities | PostgreSQL |
| Rapid schema churn, document nesting | MongoDB |
| Strong cross-record consistency | PostgreSQL |
| Massive write shard-out | MongoDB sharding or Citus |

## See Also

- [JSON & JSONB](/postgresql-cheatsheet/05-advanced-features/json/)
- [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/)
""",
        title="PostgreSQL vs MongoDB",
        desc="Document vs relational tradeoffs for architect-level selection.",
        short="vs MongoDB",
        mod=7,
        mod_title="Comparisons",
        ref="7.3",
        weight=703,
    )


def learning_paths() -> None:
    paths = [
        (
            "postgresql-senior-engineer-path.md",
            "Senior Engineer Path",
            "4-week internals and performance track.",
            """## Week 1 — Core internals
- [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/)
- [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/)
- [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/)
- [MVCC](/postgresql-cheatsheet/02-core-postgresql/mvcc/)

## Week 2 — Concurrency
- [Transactions](/postgresql-cheatsheet/02-core-postgresql/transactions/)
- [Isolation Levels](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/)
- [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/)

## Week 3 — Performance
- [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/)
- [EXPLAIN](/postgresql-cheatsheet/03-query-performance/explain/)
- [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/)

## Week 4 — Operations basics
- [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)
- [VACUUM](/postgresql-cheatsheet/06-production-operations/vacuum/)
""",
        ),
        (
            "postgresql-lead-path.md",
            "Lead Engineer Path",
            "Production operations and incident readiness.",
            """## Focus
1. [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)
2. [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/)
3. [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/)
4. [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/)
5. [Replication](/postgresql-cheatsheet/04-high-availability/replication/)
6. [Failover](/postgresql-cheatsheet/04-high-availability/failover/)
7. [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/)
""",
        ),
        (
            "postgresql-architect-path.md",
            "Architect Path",
            "HA, DR, comparisons, and platform design.",
            """## Focus
1. [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/) → [Replication](/postgresql-cheatsheet/04-high-availability/replication/)
2. [Failover](/postgresql-cheatsheet/04-high-availability/failover/) → [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/)
3. [Partitioning](/postgresql-cheatsheet/03-query-performance/partitioning/) → [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/)
4. [Comparisons](/postgresql-cheatsheet/07-comparisons/) module
5. [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
""",
        ),
        (
            "postgresql-interview-revision-path.md",
            "Interview Revision Path",
            "48-hour cram before PostgreSQL panel interviews.",
            """## Day 1 (4 hours)
| Block | Topics |
| :--- | :--- |
| 1h | Storage + WAL + MVCC |
| 1h | Isolation + Locks |
| 1h | Indexes + EXPLAIN + Planner |
| 1h | Top 50 from [Interview Guide](/postgresql-cheatsheet/08-interview-guide/top-150-interview-questions/) |

## Day 2 (4 hours)
| Block | Topics |
| :--- | :--- |
| 1h | Replication + Failover + DR |
| 1h | Vacuum + Bloat + Monitoring |
| 1h | Pooling + Capacity |
| 1h | Comparisons + architect questions |
""",
        ),
    ]
    for i, (fname, title, desc, body) in enumerate(paths, 1):
        w(
            f"09-learning-paths/{fname}",
            body,
            title=title,
            desc=desc,
            short=title.split()[0],
            mod=9,
            mod_title="Learning Paths",
            ref=f"9.{i}",
            weight=900 + i,
        )


# Top 150 questions: (question, difficulty, level, category, deep_dive_path)
QUESTIONS: list[tuple[str, str, str, str, str]] = [
    # Architecture (1-40)
    ("How does the postmaster process model differ from thread-per-connection databases?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/architecture"),
    ("What shared memory structures must fit in RAM for a production PostgreSQL cluster?", "Hard", "Architect", "Architecture", "02-core-postgresql/architecture"),
    ("Why does PostgreSQL fork a new backend per connection, and what scaling problem does that create?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/architecture"),
    ("What is the role of the checkpointer versus the background writer?", "Medium", "Lead", "Architecture", "02-core-postgresql/architecture"),
    ("How do autovacuum launcher and worker processes interact under load?", "Medium", "Lead", "Architecture", "02-core-postgresql/architecture"),
    ("Describe heap page layout including line pointers and tuple storage.", "Hard", "Senior Engineer", "Architecture", "02-core-postgresql/storage-engine"),
    ("When does PostgreSQL route a column value to TOAST storage?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/storage-engine"),
    ("What is the Free Space Map used for during inserts?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/storage-engine"),
    ("How does the visibility map enable index-only scans?", "Hard", "Lead", "Architecture", "02-core-postgresql/storage-engine"),
    ("Explain HOT updates and when index entries are skipped.", "Hard", "Senior Engineer", "Architecture", "02-core-postgresql/storage-engine"),
    ("How does shared_buffers interact with the operating system page cache?", "Medium", "Lead", "Architecture", "02-core-postgresql/storage-engine"),
    ("What is write-ahead logging and why must WAL flush precede commit acknowledgment?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/wal"),
    ("How do LSN values relate to replication and PITR?", "Hard", "Lead", "Architecture", "02-core-postgresql/wal"),
    ("What triggers a checkpoint and how does it bound crash recovery time?", "Medium", "Lead", "Architecture", "02-core-postgresql/wal"),
    ("How does crash recovery replay WAL after an unclean shutdown?", "Hard", "Architect", "Architecture", "02-core-postgresql/wal"),
    ("How does MVCC allow non-blocking reads while writers update rows?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/mvcc"),
    ("What do xmin and xmax represent in a tuple header?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/mvcc"),
    ("How is transaction snapshot visibility determined for a SELECT?", "Hard", "Lead", "Architecture", "02-core-postgresql/mvcc"),
    ("Why does UPDATE create a new row version instead of overwriting in place?", "Easy", "Senior Engineer", "Architecture", "02-core-postgresql/mvcc"),
    ("How do long-running transactions interact with vacuum and bloat?", "Hard", "Lead", "Architecture", "02-core-postgresql/mvcc"),
    ("What isolation level is PostgreSQL default and what anomalies remain?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/isolation-levels"),
    ("How does PostgreSQL REPEATABLE READ differ from the SQL standard minimum?", "Hard", "Lead", "Architecture", "02-core-postgresql/isolation-levels"),
    ("What is Serializable Snapshot Isolation and when does SQLSTATE 40001 occur?", "Hard", "Architect", "Architecture", "02-core-postgresql/isolation-levels"),
    ("What row-level locks does SELECT FOR UPDATE acquire?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/locks"),
    ("How does PostgreSQL detect and resolve deadlocks?", "Medium", "Lead", "Architecture", "02-core-postgresql/locks"),
    ("What is AccessExclusiveLock and which operations require it?", "Medium", "Lead", "Architecture", "02-core-postgresql/locks"),
    ("When are advisory locks preferable to row locks for application coordination?", "Medium", "Senior Engineer", "Architecture", "02-core-postgresql/locks"),
    ("How does declarative partitioning change planner behavior via partition pruning?", "Medium", "Lead", "Architecture", "03-query-performance/partitioning"),
    ("What constraints apply to primary keys on partitioned tables?", "Hard", "Architect", "Architecture", "03-query-performance/partitioning"),
    ("When would you choose Citus over native partitioning?", "Hard", "Architect", "Architecture", "03-query-performance/sharding"),
    ("How does streaming replication ship changes from primary to standby?", "Medium", "Lead", "Architecture", "04-high-availability/replication"),
    ("What is the difference between physical and logical replication?", "Medium", "Senior Engineer", "Architecture", "04-high-availability/replication"),
    ("How do replication slots prevent WAL removal?", "Medium", "Lead", "Architecture", "04-high-availability/replication"),
    ("What HA topology would you design for RPO near zero in a single region?", "Hard", "Architect", "Architecture", "04-high-availability/failover"),
    ("How does Patroni coordinate failover with a distributed consensus store?", "Hard", "Architect", "Architecture", "04-high-availability/failover"),
    ("What happens to the old primary after promotion in a split-brain scenario?", "Hard", "Lead", "Architecture", "04-high-availability/failover"),
    ("How does PgBouncer transaction pooling differ from session pooling architecturally?", "Hard", "Architect", "Architecture", "06-production-operations/connection-pooling"),
    ("Why is raising max_connections often the wrong fix for connection storms?", "Medium", "Lead", "Architecture", "06-production-operations/connection-pooling"),
    ("How would you architect read/write splitting with replicas and connection poolers?", "Hard", "Architect", "Architecture", "04-high-availability/replication"),
    ("When would PostgreSQL be a poor fit compared to a dedicated analytics warehouse?", "Medium", "Architect", "Architecture", "07-comparisons/postgresql-vs-mysql"),
    # Troubleshooting (41-70)
    ("What is your first step when p99 query latency doubles after a deploy?", "Medium", "Lead", "Troubleshooting", "06-production-operations/troubleshooting"),
    ("How do you find the top 10 queries by total time in production?", "Easy", "Senior Engineer", "Troubleshooting", "06-production-operations/monitoring"),
    ("How do estimated versus actual rows in EXPLAIN ANALYZE guide diagnosis?", "Medium", "Lead", "Troubleshooting", "03-query-performance/explain"),
    ("What indicates a missing index on a large table scan?", "Easy", "Senior Engineer", "Troubleshooting", "03-query-performance/explain"),
    ("How do you identify blocking sessions and their root blockers?", "Medium", "Lead", "Troubleshooting", "06-production-operations/troubleshooting"),
    ("When should you use pg_cancel_backend versus pg_terminate_backend?", "Medium", "Lead", "Troubleshooting", "06-production-operations/monitoring"),
    ("How do idle-in-transaction sessions cause vacuum starvation?", "Hard", "Lead", "Troubleshooting", "06-production-operations/vacuum"),
    ("What pg_stat_user_tables columns signal bloat risk?", "Medium", "Senior Engineer", "Troubleshooting", "06-production-operations/vacuum"),
    ("When is VACUUM FULL acceptable versus pg_repack?", "Medium", "Lead", "Troubleshooting", "06-production-operations/vacuum"),
    ("How does transaction ID wraparound threaten cluster availability?", "Hard", "Architect", "Troubleshooting", "06-production-operations/vacuum"),
    ("What symptoms indicate autovacuum cannot keep up on a hot table?", "Medium", "Lead", "Troubleshooting", "06-production-operations/troubleshooting"),
    ("How do you tune per-table autovacuum settings for append-mostly versus churn-heavy tables?", "Hard", "Lead", "Troubleshooting", "06-production-operations/vacuum"),
    ("What causes replication lag to grow on a standby during heavy write load?", "Medium", "Lead", "Troubleshooting", "06-production-operations/troubleshooting"),
    ("How can an unused replication slot fill the primary disk with WAL?", "Hard", "Lead", "Troubleshooting", "04-high-availability/replication"),
    ("How do you diagnose synchronous replication commit stalls?", "Hard", "Architect", "Troubleshooting", "04-high-availability/replication"),
    ("What wait events suggest IO-bound queries versus lock contention?", "Medium", "Senior Engineer", "Troubleshooting", "06-production-operations/monitoring"),
    ("How do you trace a deadlock from PostgreSQL logs?", "Medium", "Senior Engineer", "Troubleshooting", "02-core-postgresql/locks"),
    ("What application patterns prevent deadlocks in fund-transfer workflows?", "Medium", "Lead", "Troubleshooting", "02-core-postgresql/locks"),
    ("How does SKIP LOCKED support concurrent job queue workers?", "Medium", "Senior Engineer", "Troubleshooting", "02-core-postgresql/locks"),
    ("Why do migrations with ACCESS EXCLUSIVE locks cause outages?", "Medium", "Lead", "Troubleshooting", "02-core-postgresql/locks"),
    ("How do you detect connection leaks from application servers?", "Medium", "Lead", "Troubleshooting", "06-production-operations/troubleshooting"),
    ("What metrics alert you before max_connections is exhausted?", "Medium", "Lead", "Troubleshooting", "06-production-operations/monitoring"),
    ("How do prepared statements interact with PgBouncer transaction pooling?", "Hard", "Architect", "Troubleshooting", "06-production-operations/connection-pooling"),
    ("What causes sort operations to spill to disk and how do you confirm?", "Medium", "Senior Engineer", "Troubleshooting", "03-query-performance/explain"),
    ("How do you remediate a query plan regression after statistics drift?", "Hard", "Lead", "Troubleshooting", "03-query-performance/query-optimization"),
    ("What steps validate a backup before an incident requires restore?", "Medium", "Lead", "Troubleshooting", "04-high-availability/disaster-recovery"),
    ("How do you perform PITR to a timestamp before accidental DELETE?", "Hard", "Architect", "Troubleshooting", "04-high-availability/disaster-recovery"),
    ("What failures occur when archive_command stops shipping WAL?", "Medium", "Lead", "Troubleshooting", "02-core-postgresql/wal"),
    ("How do logical replication conflicts manifest on subscribers?", "Hard", "Lead", "Troubleshooting", "04-high-availability/replication"),
    ("What is your runbook when the primary runs out of disk on the WAL volume?", "Hard", "Lead", "Troubleshooting", "06-production-operations/troubleshooting"),
    # Performance (71-95)
    ("When would you choose a partial index over a full B-tree index?", "Medium", "Senior Engineer", "Performance", "03-query-performance/indexes"),
    ("How does a covering index with INCLUDE enable index-only scans?", "Medium", "Lead", "Performance", "03-query-performance/indexes"),
    ("When does GIN outperform B-tree for jsonb queries?", "Medium", "Senior Engineer", "Performance", "03-query-performance/indexes"),
    ("What is BRIN appropriate for and when is it wrong?", "Medium", "Lead", "Performance", "03-query-performance/indexes"),
    ("How do you identify and drop unused indexes safely?", "Medium", "Lead", "Performance", "03-query-performance/indexes"),
    ("What does EXPLAIN BUFFERS reveal about cache efficiency?", "Medium", "Senior Engineer", "Performance", "03-query-performance/explain"),
    ("How does increasing default_statistics_target affect plan quality and ANALYZE cost?", "Medium", "Lead", "Performance", "03-query-performance/query-optimization"),
    ("When does the planner choose hash join versus nested loop?", "Hard", "Senior Engineer", "Performance", "03-query-performance/query-optimization"),
    ("What parameters enable parallel sequential scan and when is parallel harmful?", "Hard", "Lead", "Performance", "03-query-performance/query-optimization"),
    ("How should work_mem be sized given concurrent connections?", "Hard", "Architect", "Performance", "03-query-performance/performance-tuning"),
    ("What is the tradeoff of raising shared_buffers on a 128 GB host?", "Medium", "Lead", "Performance", "03-query-performance/performance-tuning"),
    ("Why set random_page_cost lower on NVMe-backed instances?", "Easy", "Senior Engineer", "Performance", "03-query-performance/performance-tuning"),
    ("How does effective_cache_size influence index versus seq scan choices?", "Medium", "Senior Engineer", "Performance", "03-query-performance/query-optimization"),
    ("What CTE materialization hints affect planner inlining in PostgreSQL 12+?", "Medium", "Senior Engineer", "Performance", "01-fundamentals/ctes"),
    ("How does partition pruning fail when queries omit partition key predicates?", "Medium", "Lead", "Performance", "03-query-performance/partitioning"),
    ("What index strategy supports keyset pagination at scale?", "Hard", "Lead", "Performance", "03-query-performance/indexes"),
    ("How do you reduce write amplification from too many secondary indexes?", "Medium", "Lead", "Performance", "03-query-performance/indexes"),
    ("What role does fillfactor play in update-heavy tables?", "Medium", "Senior Engineer", "Performance", "02-core-postgresql/storage-engine"),
    ("How would you benchmark a configuration change without production risk?", "Medium", "Lead", "Performance", "03-query-performance/performance-tuning"),
    ("What OS-level tuning complements PostgreSQL on Linux for OLTP?", "Hard", "Architect", "Performance", "06-production-operations/capacity-planning"),
    ("How do materialized views trade freshness for read performance?", "Medium", "Senior Engineer", "Performance", "05-advanced-features/materialized-views"),
    ("When should REFRESH MATERIALIZED VIEW CONCURRENTLY be avoided?", "Medium", "Lead", "Performance", "05-advanced-features/materialized-views"),
    ("How does jsonb_path_ops differ from default jsonb GIN ops?", "Medium", "Senior Engineer", "Performance", "05-advanced-features/json"),
    ("What is the cost of functional indexes on lower(email)?", "Medium", "Senior Engineer", "Performance", "03-query-performance/indexes"),
    ("How do you capacity-plan WAL disk throughput for peak write bursts?", "Hard", "Architect", "Performance", "06-production-operations/capacity-planning"),
    # Reliability (96-115)
    ("What RPO does asynchronous streaming replication imply?", "Medium", "Lead", "Reliability", "04-high-availability/replication"),
    ("How do synchronous_commit and synchronous_standby_names combine?", "Hard", "Architect", "Reliability", "04-high-availability/replication"),
    ("What is pg_basebackup used for in HA bootstrap?", "Medium", "Senior Engineer", "Reliability", "04-high-availability/backup-restore"),
    ("When is pg_dump preferable to physical backup?", "Medium", "Lead", "Reliability", "04-high-availability/backup-restore"),
    ("How do you design a 3-2-1 backup strategy for PostgreSQL?", "Medium", "Architect", "Reliability", "04-high-availability/disaster-recovery"),
    ("What is recovery_target_time in PITR restore?", "Medium", "Lead", "Reliability", "04-high-availability/disaster-recovery"),
    ("How does WAL archiving enable point-in-time recovery?", "Hard", "Lead", "Reliability", "02-core-postgresql/wal"),
    ("What failure modes occur during promote when replicas are diverged?", "Hard", "Architect", "Reliability", "04-high-availability/failover"),
    ("How does pg_rewind help rejoin an old primary?", "Hard", "Lead", "Reliability", "04-high-availability/failover"),
    ("Why must DDL be considered in logical replication upgrades?", "Hard", "Architect", "Reliability", "04-high-availability/replication"),
    ("How do you monitor replication slot lag and WAL retention?", "Medium", "Lead", "Reliability", "04-high-availability/replication"),
    ("What is the impact of unvacuumed tables on crash recovery duration?", "Medium", "Senior Engineer", "Reliability", "06-production-operations/vacuum"),
    ("How does freeze protect against transaction ID wraparound?", "Hard", "Lead", "Reliability", "06-production-operations/vacuum"),
    ("What cloud-managed HA features replace self-managed Patroni?", "Medium", "Architect", "Reliability", "04-high-availability/failover"),
    ("How do you test failover without customer-visible downtime?", "Hard", "Architect", "Reliability", "04-high-availability/failover"),
    ("What data corruption detection exists in PostgreSQL at rest?", "Hard", "Architect", "Reliability", "02-core-postgresql/storage-engine"),
    ("How does SERIALIZABLE isolation protect financial invariants?", "Hard", "Lead", "Reliability", "02-core-postgresql/isolation-levels"),
    ("What is the durability guarantee with synchronous_commit=off?", "Medium", "Senior Engineer", "Reliability", "02-core-postgresql/wal"),
    ("How do you validate RTO with scheduled restore drills?", "Medium", "Lead", "Reliability", "04-high-availability/disaster-recovery"),
    ("When does logical replication lag during large bulk loads?", "Medium", "Lead", "Reliability", "04-high-availability/replication"),
    # Security (116-130) + comparisons fill to 150
    ("How does pg_hba.conf control authentication methods by network?", "Medium", "Lead", "Security", "02-core-postgresql/architecture"),
    ("Why prefer scram-sha-256 over md5 password authentication?", "Easy", "Senior Engineer", "Security", "02-core-postgresql/architecture"),
    ("What risks does SECURITY DEFINER without locked search_path create?", "Hard", "Architect", "Security", "05-advanced-features/functions"),
    ("How do row-level security policies complement GRANT?", "Hard", "Architect", "Security", "05-advanced-features/views"),
    ("How should application roles be scoped for least privilege?", "Medium", "Lead", "Security", "01-fundamentals/ddl"),
    ("What audit options exist for DDL and DML in regulated environments?", "Medium", "Architect", "Security", "05-advanced-features/triggers"),
    ("How do you rotate database credentials without downtime in pooled apps?", "Hard", "Lead", "Security", "06-production-operations/connection-pooling"),
    ("What TLS settings are required for compliance-grade encryption in transit?", "Medium", "Architect", "Security", "02-core-postgresql/architecture"),
    ("How does logical replication handle PII table subsets securely?", "Hard", "Architect", "Security", "04-high-availability/replication"),
    ("What extensions support column-level encryption tradeoffs?", "Hard", "Architect", "Security", "05-advanced-features/json"),
    ("How do you prevent SQL injection with parameterized queries in ORMs?", "Easy", "Senior Engineer", "Security", "01-fundamentals/dml"),
    ("What network segmentation pattern isolates PostgreSQL in Kubernetes?", "Hard", "Architect", "Security", "02-core-postgresql/architecture"),
    ("How are superuser capabilities restricted in production roles?", "Medium", "Lead", "Security", "02-core-postgresql/architecture"),
    ("What compliance considerations apply to cross-region replication of EU data?", "Hard", "Architect", "Security", "04-high-availability/replication"),
    ("How do you secure pg_stat_statements from exposing sensitive query text?", "Medium", "Lead", "Security", "06-production-operations/monitoring"),
    # Comparisons / architect (131-150)
    ("When would you choose PostgreSQL over MySQL for a new OLTP platform?", "Medium", "Architect", "Architecture", "07-comparisons/postgresql-vs-mysql"),
    ("What Oracle features lack direct PostgreSQL equivalents in migration?", "Hard", "Architect", "Architecture", "07-comparisons/postgresql-vs-oracle"),
    ("How does PostgreSQL jsonb compare to MongoDB document storage for transactional apps?", "Hard", "Architect", "Architecture", "07-comparisons/postgresql-vs-mongodb"),
    ("What workload signals push you toward sharding versus bigger vertical hardware?", "Hard", "Architect", "Architecture", "03-query-performance/sharding"),
    ("How would you blueprint HA for a payment ledger with strict consistency?", "Hard", "Architect", "Architecture", "04-high-availability/failover"),
    ("What ADR criteria from the database handbook justify PostgreSQL selection?", "Medium", "Architect", "Architecture", "database-handbook/postgresql"),
    ("How do you migrate from Oracle PL/SQL to PostgreSQL with minimal risk?", "Hard", "Architect", "Architecture", "07-comparisons/postgresql-vs-oracle"),
    ("When is foreign data wrapper federation acceptable versus ETL?", "Medium", "Lead", "Architecture", "03-query-performance/sharding"),
    ("How does Citus colocation affect multi-tenant schema design?", "Hard", "Architect", "Architecture", "03-query-performance/sharding"),
    ("What monitoring SLOs define PostgreSQL platform health?", "Medium", "Lead", "Architecture", "06-production-operations/monitoring"),
    ("How do you design schema migrations for zero-downtime deploys?", "Hard", "Architect", "Architecture", "01-fundamentals/ddl"),
    ("What is the role of extensions like PostGIS or pgvector in platform architecture?", "Medium", "Architect", "Architecture", "03-query-performance/indexes"),
    ("How would you evaluate managed RDS/Aurora versus self-hosted Patroni?", "Hard", "Architect", "Architecture", "04-high-availability/failover"),
    ("What connection storm patterns appear during Kubernetes pod scale events?", "Medium", "Lead", "Architecture", "06-production-operations/connection-pooling"),
    ("How do read replicas affect consistency for reporting dashboards?", "Medium", "Lead", "Architecture", "04-high-availability/replication"),
    ("What capacity triggers prompt adding a new replica versus partition pruning tuning?", "Hard", "Architect", "Architecture", "06-production-operations/capacity-planning"),
    ("How do stored procedures versus application transactions affect deploy agility?", "Medium", "Lead", "Architecture", "05-advanced-features/stored-procedures"),
    ("When should business logic live in triggers versus application services?", "Medium", "Lead", "Architecture", "05-advanced-features/triggers"),
    ("How do you document PostgreSQL platform standards for 50+ microservices?", "Hard", "Architect", "Architecture", "09-learning-paths/postgresql-architect-path"),
    ("What interview signals separate senior engineers from architects on PostgreSQL panels?", "Medium", "Architect", "Architecture", "08-interview-guide/architect-questions"),
]

assert len(QUESTIONS) == 150, f"Expected 150 questions, got {len(QUESTIONS)}"


def write_interview_guide() -> None:
    rows = ["| # | Question | Difficulty | Level | Category | Deep Dive |", "|---|----------|------------|--------|----------|-----------|"]
    for i, (q, diff, level, cat, path) in enumerate(QUESTIONS, 1):
        if path.startswith("database-handbook"):
            link = f"[Database Handbook](/{path}/)"
        else:
            link = f"[{path.split('/')[-1].replace('-', ' ').title()}](/{SECTION}/{path}/)"
        rows.append(f"| {i} | {q} | {diff} | {level} | {cat} | {link} |")

    body = (
        "Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. "
        "Questions only — no answers. Each row links to the canonical deep-dive page.\n\n"
        "## Distribution\n\n"
        "| Category | Count |\n| :--- | :---: |\n"
        "| Architecture | 40 |\n| Troubleshooting | 30 |\n| Performance | 25 |\n"
        "| Reliability | 20 |\n| Security | 15 |\n\n"
        + "\n".join(rows)
    )
    w(
        "08-interview-guide/top-150-interview-questions.md",
        body,
        title="Top 150 PostgreSQL Interview Questions",
        desc="150 production-oriented PostgreSQL interview questions mapped to handbook topics.",
        short="Top 150",
        mod=8,
        mod_title="Interview Guide",
        ref="8.1",
        weight=801,
    )

    arch_idxs = [6, 13, 19, 23, 34, 35, 37, 38, 39, 55, 65, 72, 88, 97, 100, 109, 114, 116, 123, 131, 132, 135, 136, 137, 143]
    trouble_idxs = [41, 45, 46, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 28, 30]
    perf_idxs = [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]

    def subset(name: str, title: str, ref: str, weight: int, idxs: list[int]) -> None:
        lines = [f"Questions only — no answers. Sourced from [Top 150](/{SECTION}/08-interview-guide/top-150-interview-questions/).\n", f"# {title}\n"]
        for n, idx in enumerate(idxs[:25], 1):
            lines.append(f"{n}. {QUESTIONS[idx - 1][0]}")
        w(f"08-interview-guide/{name}", "\n".join(lines), title=title, desc=f"{title} from the PostgreSQL handbook.", short=title.split()[0], mod=8, mod_title="Interview Guide", ref=ref, weight=weight)

    subset("architect-questions.md", "Top 25 Architect Questions", "8.2", 802, arch_idxs)
    subset("troubleshooting-questions.md", "Top 25 Troubleshooting Questions", "8.3", 803, trouble_idxs)
    subset("performance-questions.md", "Top 25 Performance Questions", "8.4", 804, perf_idxs)


def migrate_existing() -> None:
    moves = [
        ("installation.md", "01-fundamentals/installation.md", "/postgresql-cheatsheet/installation/", dict(title="Installation", desc="Install PostgreSQL — initdb, psql, first connection.", short="Install", mod=1, mod_title="Fundamentals", ref="1.7", weight=107)),
        ("sql-basics.md", "01-fundamentals/sql-basics.md", "/postgresql-cheatsheet/sql-basics/", dict(title="SQL Basics", desc="SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, and psql essentials.", short="SQL Basics", mod=1, mod_title="Fundamentals", ref="1.1", weight=101)),
        ("ddl.md", "01-fundamentals/ddl.md", "/postgresql-cheatsheet/ddl/", dict(title="DDL", desc="CREATE/ALTER/DROP — schemas, tables, constraints, and types.", short="DDL", mod=1, mod_title="Fundamentals", ref="1.2", weight=102)),
        ("dml.md", "01-fundamentals/dml.md", "/postgresql-cheatsheet/dml/", dict(title="DML", desc="INSERT, UPDATE, DELETE, UPSERT, and RETURNING patterns.", short="DML", mod=1, mod_title="Fundamentals", ref="1.3", weight=103)),
        ("joins.md", "01-fundamentals/joins.md", "/postgresql-cheatsheet/joins/", dict(title="Joins", desc="INNER, LEFT, LATERAL joins and top-N per group patterns.", short="Joins", mod=1, mod_title="Fundamentals", ref="1.4", weight=104)),
        ("ctes.md", "01-fundamentals/ctes.md", "/postgresql-cheatsheet/ctes/", dict(title="CTEs", desc="WITH, recursive CTEs, MATERIALIZED hints.", short="CTEs", mod=1, mod_title="Fundamentals", ref="1.5", weight=105)),
        ("window-functions.md", "01-fundamentals/window-functions.md", "/postgresql-cheatsheet/window-functions/", dict(title="Window Functions", desc="ROW_NUMBER, LAG/LEAD, PARTITION BY, frame clauses.", short="Windows", mod=1, mod_title="Fundamentals", ref="1.6", weight=106)),
        ("mvcc.md", "02-core-postgresql/mvcc.md", "/postgresql-cheatsheet/mvcc/", dict(title="MVCC", desc="Tuple visibility, xmin/xmax, snapshots, and vacuum interaction.", short="MVCC", mod=2, mod_title="Core PostgreSQL", ref="2.4", weight=204)),
        ("transactions.md", "02-core-postgresql/transactions.md", "/postgresql-cheatsheet/transactions/", dict(title="Transactions", desc="BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and ACID.", short="Transactions", mod=2, mod_title="Core PostgreSQL", ref="2.5", weight=205)),
        ("isolation-levels.md", "02-core-postgresql/isolation-levels.md", "/postgresql-cheatsheet/isolation-levels/", dict(title="Isolation Levels", desc="READ COMMITTED, REPEATABLE READ, SERIALIZABLE.", short="Isolation", mod=2, mod_title="Core PostgreSQL", ref="2.6", weight=206)),
        ("locks.md", "02-core-postgresql/locks.md", "/postgresql-cheatsheet/locks/", dict(title="Locks", desc="Row/table/advisory locks, deadlocks, pg_locks.", short="Locks", mod=2, mod_title="Core PostgreSQL", ref="2.7", weight=207)),
        ("indexes.md", "03-query-performance/indexes.md", "/postgresql-cheatsheet/indexes/", dict(title="Indexes", desc="B-tree, GIN, GiST, BRIN, partial, covering indexes.", short="Indexes", mod=3, mod_title="Query Performance", ref="3.1", weight=301)),
        ("explain.md", "03-query-performance/explain.md", "/postgresql-cheatsheet/explain/", dict(title="EXPLAIN", desc="EXPLAIN, ANALYZE, BUFFERS — plan nodes and costs.", short="EXPLAIN", mod=3, mod_title="Query Performance", ref="3.2", weight=302)),
        ("performance-tuning.md", "03-query-performance/performance-tuning.md", "/postgresql-cheatsheet/performance-tuning/", dict(title="Performance Tuning", desc="shared_buffers, work_mem, and server config knobs.", short="Perf Tuning", mod=3, mod_title="Query Performance", ref="3.4", weight=304)),
        ("partitioning.md", "03-query-performance/partitioning.md", "/postgresql-cheatsheet/partitioning/", dict(title="Partitioning", desc="Declarative RANGE, LIST, HASH partitioning.", short="Partitioning", mod=3, mod_title="Query Performance", ref="3.5", weight=305)),
        ("sharding.md", "03-query-performance/sharding.md", "/postgresql-cheatsheet/sharding/", dict(title="Sharding", desc="Citus, FDW, and application-level sharding.", short="Sharding", mod=3, mod_title="Query Performance", ref="3.6", weight=306)),
        ("replication.md", "04-high-availability/replication.md", "/postgresql-cheatsheet/replication/", dict(title="Replication", desc="Streaming and logical replication, slots.", short="Replication", mod=4, mod_title="High Availability", ref="4.1", weight=401)),
        ("backup-restore.md", "04-high-availability/backup-restore.md", "/postgresql-cheatsheet/backup-restore/", dict(title="Backup & Restore", desc="pg_dump, pg_restore, base backup, PITR overview.", short="Backup", mod=4, mod_title="High Availability", ref="4.3", weight=403)),
        ("functions.md", "05-advanced-features/functions.md", "/postgresql-cheatsheet/functions/", dict(title="Functions", desc="PL/pgSQL and SQL functions — volatility, security.", short="Functions", mod=5, mod_title="Advanced Features", ref="5.1", weight=501)),
        ("stored-procedures.md", "05-advanced-features/stored-procedures.md", "/postgresql-cheatsheet/stored-procedures/", dict(title="Stored Procedures", desc="CREATE PROCEDURE, CALL, transactions inside.", short="Procedures", mod=5, mod_title="Advanced Features", ref="5.2", weight=502)),
        ("triggers.md", "05-advanced-features/triggers.md", "/postgresql-cheatsheet/triggers/", dict(title="Triggers", desc="BEFORE/AFTER, ROW/STATEMENT triggers.", short="Triggers", mod=5, mod_title="Advanced Features", ref="5.3", weight=503)),
        ("materialized-views.md", "05-advanced-features/materialized-views.md", "/postgresql-cheatsheet/materialized-views/", dict(title="Materialized Views", desc="REFRESH, CONCURRENTLY, staleness trade-offs.", short="Mat Views", mod=5, mod_title="Advanced Features", ref="5.4", weight=504)),
        ("json.md", "05-advanced-features/json.md", "/postgresql-cheatsheet/json/", dict(title="JSON & JSONB", desc="json vs jsonb, operators, GIN indexing.", short="JSON", mod=5, mod_title="Advanced Features", ref="5.5", weight=505)),
        ("views.md", "05-advanced-features/views.md", "/postgresql-cheatsheet/views/", dict(title="Views", desc="CREATE VIEW, updatable views, security_barrier.", short="Views", mod=5, mod_title="Advanced Features", ref="5.6", weight=506)),
        ("vacuum.md", "06-production-operations/vacuum.md", "/postgresql-cheatsheet/vacuum/", dict(title="VACUUM", desc="VACUUM, autovacuum, bloat, freeze.", short="VACUUM", mod=6, mod_title="Production Operations", ref="6.1", weight=601)),
    ]
    for src, dst, alias, fm in moves:
        migrate(src, dst, alias=alias, **fm)


def patch_migrated_pages() -> None:
    """Strip duplicate deep dives; add canonical links on key pages."""
    perf = PG / "03-query-performance/performance-tuning.md"
    if perf.exists():
        t = perf.read_text(encoding="utf-8")
        t = t.replace(
            "Connection pooling (transaction mode) is almost always required in microservices.",
            "Connection pooling is almost always required in microservices — see [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/).",
        )
        t = t.replace(
            "Raising `max_connections` without a pooler increases memory and context switching.",
            "Raising `max_connections` without a pooler increases memory and context switching — size pools in [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/).",
        )
        perf.write_text(t, encoding="utf-8")

    repl = PG / "04-high-availability/replication.md"
    if repl.exists():
        t = repl.read_text(encoding="utf-8")
        if "Failover" not in t:
            t = t.replace(
                "## See Also",
                "## See Also\n\n- [Failover](/postgresql-cheatsheet/04-high-availability/failover/)\n- [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/)",
            )
        repl.write_text(t, encoding="utf-8")


def write_yaml() -> None:
    modules = {
        "modules": [
            {"id": 1, "focus": "Fundamentals", "topics": [
                "01-fundamentals/sql-basics", "01-fundamentals/ddl", "01-fundamentals/dml",
                "01-fundamentals/joins", "01-fundamentals/ctes", "01-fundamentals/window-functions",
                "01-fundamentals/installation",
            ]},
            {"id": 2, "focus": "Core PostgreSQL", "topics": [
                "02-core-postgresql/architecture", "02-core-postgresql/storage-engine", "02-core-postgresql/wal",
                "02-core-postgresql/mvcc", "02-core-postgresql/transactions", "02-core-postgresql/isolation-levels",
                "02-core-postgresql/locks",
            ]},
            {"id": 3, "focus": "Query Performance", "topics": [
                "03-query-performance/indexes", "03-query-performance/explain",
                "03-query-performance/query-optimization", "03-query-performance/performance-tuning",
                "03-query-performance/partitioning", "03-query-performance/sharding",
            ]},
            {"id": 4, "focus": "High Availability", "topics": [
                "04-high-availability/replication", "04-high-availability/failover",
                "04-high-availability/backup-restore", "04-high-availability/disaster-recovery",
            ]},
            {"id": 5, "focus": "Advanced Features", "topics": [
                "05-advanced-features/functions", "05-advanced-features/stored-procedures",
                "05-advanced-features/triggers", "05-advanced-features/materialized-views",
                "05-advanced-features/json", "05-advanced-features/views",
            ]},
            {"id": 6, "focus": "Production Operations", "topics": [
                "06-production-operations/vacuum", "06-production-operations/monitoring",
                "06-production-operations/troubleshooting", "06-production-operations/connection-pooling",
                "06-production-operations/capacity-planning",
            ]},
            {"id": 7, "focus": "Comparisons", "topics": [
                "07-comparisons/postgresql-vs-mysql", "07-comparisons/postgresql-vs-oracle",
                "07-comparisons/postgresql-vs-mongodb",
            ]},
            {"id": 8, "focus": "Interview Guide", "topics": [
                "08-interview-guide/top-150-interview-questions",
                "08-interview-guide/architect-questions",
                "08-interview-guide/troubleshooting-questions",
                "08-interview-guide/performance-questions",
            ]},
            {"id": 9, "focus": "Learning Paths", "topics": [
                "09-learning-paths/postgresql-senior-engineer-path",
                "09-learning-paths/postgresql-lead-path",
                "09-learning-paths/postgresql-architect-path",
                "09-learning-paths/postgresql-interview-revision-path",
            ]},
        ]
    }
    order = {"topics": [t for m in modules["modules"] for t in m["topics"]]}
    (DATA / "postgresql_cheatsheet_modules.yaml").write_text(
        "# PostgreSQL Handbook — module index.\n" + yaml.dump(modules, sort_keys=False), encoding="utf-8"
    )
    (DATA / "postgresql_cheatsheet_order.yaml").write_text(
        "# Flat topic order — nested slugs.\n" + yaml.dump(order, sort_keys=False), encoding="utf-8"
    )


def cleanup_flat() -> None:
    keep_roots = {"_index.md"}
    for p in PG.glob("*.md"):
        if p.name not in keep_roots:
            p.unlink()
            print(f"Removed flat {p.name}")


def main() -> None:
    migrate_existing()
    section_indexes()
    handbook_index()
    new_core_pages()
    new_performance_ops_pages()
    comparison_pages()
    learning_paths()
    write_interview_guide()
    patch_migrated_pages()
    write_yaml()
    cleanup_flat()
    print("PostgreSQL handbook Phase B refactor complete.")


if __name__ == "__main__":
    main()
