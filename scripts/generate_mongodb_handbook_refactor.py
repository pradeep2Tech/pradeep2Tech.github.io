"""Generate refactored MongoDB handbook content (Phase B)."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "mongodb-cheatsheet"
DATA = ROOT / "data"
DATE = "2026-07-03T12:00:00+00:00"
BASE = "/mongodb-cheatsheet"

FM = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["mongodb-cheatsheet", "mongodb-handbook", "mongodb", "interview"]
categories: ["MongoDB Handbook"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
ShowToc: true
interviewHandbook: true{aliases}
---

"""

FM_CHEAT = FM.replace("interviewHandbook: true", "cheatSheet: true\ninterviewHandbook: true")


def aliases_block(*paths: str) -> str:
    if not paths:
        return ""
    lines = "\n".join(f'  - "{p}"' for p in paths)
    return f"\naliases:\n{lines}"


def w(rel: str, body: str, *, cheat: bool = False, alias_paths: tuple[str, ...] = (), **fm):
    path = HB / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    tmpl = FM_CHEAT if cheat else FM
    alias = aliases_block(*alias_paths)
    path.write_text(tmpl.format(date=DATE, aliases=alias, **fm) + body.strip() + "\n", encoding="utf-8")


def read_old(name: str) -> str:
    p = HB / name
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\n", "", text, count=1, flags=re.DOTALL)


def fix_links(body: str) -> str:
    mapping = {
        "/mongodb-cheatsheet/architecture/": f"{BASE}/02-core-mongodb/architecture/",
        "/mongodb-cheatsheet/documents/": f"{BASE}/01-fundamentals/documents/",
        "/mongodb-cheatsheet/collections/": f"{BASE}/01-fundamentals/collections/",
        "/mongodb-cheatsheet/crud/": f"{BASE}/01-fundamentals/crud/",
        "/mongodb-cheatsheet/atlas-basics/": f"{BASE}/01-fundamentals/atlas-basics/",
        "/mongodb-cheatsheet/indexes/": f"{BASE}/03-query-performance/indexes/",
        "/mongodb-cheatsheet/ttl-index/": f"{BASE}/03-query-performance/ttl-index/",
        "/mongodb-cheatsheet/text-search/": f"{BASE}/03-query-performance/text-search/",
        "/mongodb-cheatsheet/geospatial/": f"{BASE}/03-query-performance/geospatial/",
        "/mongodb-cheatsheet/aggregation-pipeline/": f"{BASE}/03-query-performance/aggregation-pipeline/",
        "/mongodb-cheatsheet/replication/": f"{BASE}/02-core-mongodb/replication/",
        "/mongodb-cheatsheet/sharding/": f"{BASE}/02-core-mongodb/sharding/",
        "/mongodb-cheatsheet/transactions/": f"{BASE}/02-core-mongodb/transactions/",
        "/mongodb-cheatsheet/schema-design/": f"{BASE}/02-core-mongodb/schema-design/",
        "/mongodb-cheatsheet/performance/": f"{BASE}/04-production-operations/performance/",
        "/mongodb-cheatsheet/mongo-shell-commands/": f"{BASE}/04-production-operations/monitoring/",
        "/mongodb-cheatsheet/interview-questions/": f"{BASE}/06-interview-guide/top-150-interview-questions/",
    }
    for old, new in mapping.items():
        body = body.replace(old, new)
    return body


# --- Section indexes ---
SECTIONS = [
    ("01-fundamentals", "Fundamentals", "Document model, CRUD, and Atlas basics.", 1),
    ("02-core-mongodb", "Core MongoDB", "Architecture, storage engine, replication, sharding, transactions, schema design.", 2),
    ("03-query-performance", "Query & Performance", "Indexes, aggregation, query optimization, and explain plans.", 3),
    ("04-production-operations", "Production Operations", "Performance tuning, monitoring, troubleshooting, backup, and capacity.", 4),
    ("05-comparisons", "Comparisons", "MongoDB versus PostgreSQL, Cassandra, and Couchbase.", 5),
    ("06-interview-guide", "Interview Guide", "150-question bank and role-specific subsets.", 6),
    ("07-learning-paths", "Learning Paths", "Curated reading paths by seniority and goal.", 7),
]


def main() -> None:
    for folder, title, desc, mod in SECTIONS:
        w(
            f"{folder}/_index.md",
            f"# {title}\n\n{desc}\n",
            title=title,
            desc=desc,
            short=title,
            mod=mod,
            mod_title="MongoDB Handbook",
            ref="0",
            weight=mod,
        )


    def move_cheat(
        old: str,
        new: str,
        *,
        title: str,
        desc: str,
        short: str,
        mod: int,
        mod_title: str,
        ref: str,
        weight: int,
        alias: str,
        patch: str | None = None,
    ):
        body = fix_links(read_old(old))
        if patch:
            body = patch(body)
        w(
            new,
            body,
            cheat=True,
            title=title,
            desc=desc,
            short=short,
            mod=mod,
            mod_title=mod_title,
            ref=ref,
            weight=weight,
            alias_paths=(f"{BASE}/{alias}/",),
        )


    def patch_architecture(body: str) -> str:
        body = body.replace(
            "| **WiredTiger** | Default storage engine — B-tree indexes, document-level locks |\n"
            "| **oplog** | Capped collection on primary; replication + change streams source |\n"
            "| **Journal** | Write-ahead log for crash recovery (checkpoints every ~60s) |",
            "| **WiredTiger** | Default storage engine — see [Storage Engine]({base}/02-core-mongodb/storage-engine/) |\n"
            "| **oplog** | Replication log on primary — see [Replication]({base}/02-core-mongodb/replication/) |".format(
                base=BASE
            ),
        )
        body = re.sub(
            r"\| Read concern \| Behavior \|[\s\S]*?\| `\{ j: true \}` \| Journal flush before ack \|\n",
            "For **read concern**, **write concern**, and **read preference**, see "
            f"[Replication]({BASE}/02-core-mongodb/replication/).\n",
            body,
        )
        body = body.replace(
            "## Executive Summary",
            "## Quick Revision\n\n"
            "- **mongod** stores data; **mongos** routes in sharded clusters; **config servers** hold chunk metadata.\n"
            "- Production = replica set minimum; sharding when single replica set saturates.\n\n"
            "## Executive Summary",
        )
        return body


    def patch_indexes(body: str) -> str:
        body = re.sub(
            r"\| `explain` stage \| Meaning \|[\s\S]*?\| `PROJECTION_COVERED` \| Index-only — no FETCH needed \|\n",
            "For explain stages and `executionStats`, see "
            f"[Explain Plan]({BASE}/03-query-performance/explain-plan/) and "
            f"[Query Optimization]({BASE}/03-query-performance/query-optimization/).\n",
            body,
        )
        return body


    def patch_performance(body: str) -> str:
        body = body.replace(
            "## Executive Summary\n\n"
            "MongoDB performance tuning starts with **query patterns and indexes**, then **working set in RAM**, "
            "then **hardware and topology**. Always `explain(\"executionStats\")` before adding indexes blindly.",
            "## Quick Revision\n\n"
            "- Tune queries and indexes first; then schema; then hardware and topology.\n"
            "- Use [Explain Plan]({base}/03-query-performance/explain-plan/) before adding indexes.\n"
            "- Monitoring and capacity: [Monitoring]({base}/04-production-operations/monitoring/) · "
            "[Capacity Planning]({base}/04-production-operations/capacity-planning/).\n\n"
            "## Executive Summary\n\n"
            "Holistic performance tuning for production MongoDB deployments — connection pooling, bulk patterns, "
            "and pagination strategies. Query planner and index design live on dedicated pages.".format(base=BASE),
        )
        body = re.sub(
            r"```javascript\n// Explain[\s\S]*?```\n",
            "",
            body,
            count=1,
        )
        body = re.sub(
            r"// Profiler[\s\S]*?db\.orders\.aggregate\(\[\{ \$indexStats: \{\} \}\]\)\n```\n",
            "",
            body,
        )
        body = re.sub(
            r"\| Symptom \| Likely cause \|[\s\S]*?\| Page faults \| Working set exceeds RAM \|\n",
            "For symptom → cause → fix runbooks, see "
            f"[Troubleshooting]({BASE}/04-production-operations/troubleshooting/).\n",
            body,
        )
        body = re.sub(
            r"```bash\n# mongostat[\s\S]*?```\n",
            "",
            body,
        )
        return body


    def patch_replication(body: str) -> str:
        if "## Quick Revision" not in body:
            body = body.replace(
                "## Executive Summary",
                "## Quick Revision\n\n"
                "- One **primary** accepts writes; **secondaries** tail the **oplog**.\n"
                "- Use `w: \"majority\"` for durability; understand rollback after failover.\n"
                "- **Read concern** and **read preference** control staleness vs latency.\n\n"
                "## Executive Summary",
            )
        rc = f"""
    | Read concern | Behavior |
    | :--- | :--- |
    | `local` | Return latest local data (may be rolled back) |
    | `majority` | Data acknowledged by majority of nodes |
    | `linearizable` | Strongest — single-document linearizability |

    | Write concern | Behavior |
    | :--- | :--- |
    | `{{ w: 1 }}` | Primary ack only |
    | `{{ w: "majority" }}` | Majority replica ack — durable default for prod |
    | `{{ j: true }}` | Journal flush before ack (see [Storage Engine]({BASE}/02-core-mongodb/storage-engine/)) |
    """
        if "Read concern | Behavior" not in body:
            body = body.replace("---\n\n## Snippets", rc + "\n---\n\n## Snippets")
        return body


    # --- Move existing files ---
    MOVES = [
        ("documents.md", "01-fundamentals/documents.md", "Documents", "BSON document model — types, _id, dot notation, arrays.", "Documents", 1, "Fundamentals", "1.1", 111, "documents"),
        ("collections.md", "01-fundamentals/collections.md", "Collections", "Collections, validation, capped and time series collections.", "Collections", 1, "Fundamentals", "1.2", 112, "collections"),
        ("crud.md", "01-fundamentals/crud.md", "CRUD", "Find, insert, update, delete, operators, and bulk writes.", "CRUD", 1, "Fundamentals", "1.3", 113, "crud"),
        ("atlas-basics.md", "01-fundamentals/atlas-basics.md", "Atlas Basics", "MongoDB Atlas clusters, connectivity, tiers, and managed features.", "Atlas", 1, "Fundamentals", "1.4", 114, "atlas-basics"),
        ("architecture.md", "02-core-mongodb/architecture.md", "Architecture", "MongoDB deployment topology — mongod, mongos, replica sets, sharded clusters.", "Architecture", 2, "Core MongoDB", "2.1", 201, "architecture"),
        ("replication.md", "02-core-mongodb/replication.md", "Replication", "Replica sets, oplog, elections, read/write concern, failover.", "Replication", 2, "Core MongoDB", "2.3", 203, "replication"),
        ("sharding.md", "02-core-mongodb/sharding.md", "Sharding", "Shard keys, chunks, balancer, zone sharding, and scaling.", "Sharding", 2, "Core MongoDB", "2.4", 204, "sharding"),
        ("transactions.md", "02-core-mongodb/transactions.md", "Transactions", "Multi-document ACID, sessions, retryable writes, sharded limits.", "Transactions", 2, "Core MongoDB", "2.5", 205, "transactions"),
        ("schema-design.md", "02-core-mongodb/schema-design.md", "Schema Design", "Embedding vs referencing, bucketing, polymorphism, access-pattern-first modeling.", "Schema", 2, "Core MongoDB", "2.6", 206, "schema-design"),
        ("indexes.md", "03-query-performance/indexes.md", "Indexes", "Index types, ESR rule, compound, partial, sparse, wildcard.", "Indexes", 3, "Query & Performance", "3.1", 301, "indexes"),
        ("ttl-index.md", "03-query-performance/ttl-index.md", "TTL Index", "Automatic document expiry with TTL indexes.", "TTL", 3, "Query & Performance", "3.2", 302, "ttl-index"),
        ("text-search.md", "03-query-performance/text-search.md", "Text Search", "Text indexes, $text, Atlas Search overview.", "Text Search", 3, "Query & Performance", "3.3", 303, "text-search"),
        ("geospatial.md", "03-query-performance/geospatial.md", "Geospatial", "GeoJSON, 2dsphere indexes, geo queries.", "Geospatial", 3, "Query & Performance", "3.4", 304, "geospatial"),
        ("aggregation-pipeline.md", "03-query-performance/aggregation-pipeline.md", "Aggregation Pipeline", "Pipeline stages, $lookup, $facet, optimization patterns.", "Aggregation", 3, "Query & Performance", "3.5", 305, "aggregation-pipeline"),
        ("performance.md", "04-production-operations/performance.md", "Performance", "Production performance tuning — pooling, pagination, bulk patterns.", "Performance", 4, "Production Operations", "4.1", 401, "performance"),
    ]

    PATCHERS = {
        "architecture.md": patch_architecture,
        "indexes.md": patch_indexes,
        "performance.md": patch_performance,
        "replication.md": patch_replication,
    }

    for old, new, *rest in MOVES:
        title, desc, short, mod, mod_title, ref, weight, alias = rest
        patch = PATCHERS.get(old)
        move_cheat(old, new, title=title, desc=desc, short=short, mod=mod, mod_title=mod_title, ref=ref, weight=weight, alias=alias, patch=patch)


    # --- New canonical pages ---
    w(
        "02-core-mongodb/storage-engine.md",
        f"""## Quick Revision

    - **WiredTiger** is the default storage engine — B-tree indexes, document-level locking, MVCC.
    - Writes go to cache → journal (WAL) → checkpoint to disk (~60s default).
    - Cache default ≈ 50% RAM minus 1 GB; page faults signal working-set pressure.

    ## Core Concepts

    | Component | Role |
    | :--- | :--- |
    | **Cache** | In-memory buffer for indexes and data pages |
    | **Journal** | Write-ahead log for crash recovery between checkpoints |
    | **Checkpoint** | Consistent on-disk snapshot of cached data |
    | **MVCC** | Readers see snapshot; writers don't block readers on different docs |
    | **Compression** | snappy (default), zlib, zstd for data and indexes |

    ## Internal Working

    ```mermaid
    flowchart TB
      write[Write request] --> cache[WiredTiger cache]
      cache --> journal[Journal WAL]
      journal --> ack[Ack per write concern]
      cache --> checkpoint[Periodic checkpoint]
      checkpoint --> disk[(Data files)]
    ```

    **Write path:** Document update in cache → journal record → ack when journal flushed (if `j: true`) → checkpoint persists dirty pages.

    **Read path:** Index B-tree lookup → fetch document from cache or disk → return snapshot per read concern.

    ## Architecture

    WiredTiger replaced MMAPv1 (removed). All production deployments use document-level concurrency — not collection-level locks.

    ## Design Tradeoffs

    | Choice | Trade-off |
    | :--- | :--- |
    | Larger cache | Fewer disk reads; less RAM for OS and connections |
    | `j: true` | Durability vs write latency |
    | zstd compression | CPU cost vs disk and I/O savings |
    | Frequent checkpoints | Faster recovery vs I/O burst |

    ## Production Patterns

    - Monitor **cache usage** and **eviction** metrics — sustained evictions = undersized RAM.
    - Size RAM so **working set + indexes** fit comfortably; see [Capacity Planning]({BASE}/04-production-operations/capacity-planning/).
    - Align `j: true` with `w: "majority"` for financial-grade durability.

    ## Scalability

    Storage engine is per-shard; each replica set member has independent WiredTiger cache.

    ## Reliability

    Journal + checkpoints enable crash recovery without full resync. Replication durability is separate — see [Replication]({BASE}/02-core-mongodb/replication/).

    ## Observability

    `db.serverStatus().wiredTiger`, `cache_used_percent`, `pages read into cache`, `pages written from cache`.

    ## Troubleshooting

    | Symptom | Check |
    | :--- | :--- |
    | High page faults | Working set > RAM — [Capacity Planning]({BASE}/04-production-operations/capacity-planning/) |
    | Write latency spikes | Journal flush, checkpoint I/O, disk saturation |
    | Cache full + evictions | RAM sizing or query/index bloat |

    ## Common Mistakes

    - Ignoring checkpoint I/O on shared disks during peak writes.
    - Tuning only queries when RAM cannot hold working set.

    ## Interview Questions

    - How does WiredTiger achieve document-level concurrency?
    - What is the relationship between journal, checkpoint, and `j: true`?
    - When do page faults indicate a capacity problem?

    ## Architect Notes

    Storage engine behavior explains why **RAM sizing** and **write concern** are architectural decisions, not DBA afterthoughts.
    """,
        title="Storage Engine",
        desc="WiredTiger internals — MVCC, checkpoints, journaling, compression, cache management.",
        short="Storage",
        mod=2,
        mod_title="Core MongoDB",
        ref="2.2",
        weight=202,
    )


    w(
        "03-query-performance/query-optimization.md",
        f"""## Quick Revision

    - Put **equality** fields first in compound indexes (**ESR**: Equality, Sort, Range).
    - Prefer **IXSCAN** over **COLLSCAN**; aim `totalDocsExamined` ≈ `nReturned`.
    - In aggregation, place **`$match`** and **`$sort`** early; index **`$lookup`** `foreignField`.

    ## Core Concepts

    | Concept | Guidance |
    | :--- | :--- |
    | **Query planner** | Chooses winning plan; may use index intersection sparingly |
    | **Covered query** | All filter + projection fields in index — no FETCH |
    | **COLLSCAN** | Full collection scan — acceptable only on tiny collections |
    | **IXSCAN** | Index scan — expected for hot paths |
    | **Plan cache** | Reuses plans; `$planCacheStats` for diagnostics |

    ## Internal Working

    Planner evaluates indexes against filter, sort, and projection. Rejected plans appear in `explain("executionStats").queryPlanner.rejectedPlans`.

    Compound index `{{ a: 1, b: 1, c: 1 }}` supports `{{a}}`, `{{a,b}}`, `{{a,b,c}}` prefixes — not `{{b}}` alone.

    ## Architecture

    Query shape and schema are coupled — embed to avoid `$lookup`; reference when unbounded. See [Schema Design]({BASE}/02-core-mongodb/schema-design/).

    ## Design Tradeoffs

    | Choice | Trade-off |
    | :--- | :--- |
    | Many single-field indexes | Flexibility vs write amplification and RAM |
    | One compound index | Fast for one pattern; useless for others |
    | `$lookup` | Server-side join vs extra round trips |

    ## Production Patterns

    - Run [Explain Plan]({BASE}/03-query-performance/explain-plan/) on top 10 slow queries monthly.
    - Hide unused indexes before drop (`hideIndex`) — validate in staging.
    - Pagination: range on indexed field, not large `skip`.

    ## Scalability

    Scatter-gather on sharded collections hits all shards — include shard key equality when possible. See [Sharding]({BASE}/02-core-mongodb/sharding/).

    ## Reliability

    Index builds on large collections — monitor load; use rolling builds in Atlas.

    ## Observability

    Profiler, `db.currentOp()`, Atlas Performance Advisor, `$indexStats`.

    ## Troubleshooting

    See [Troubleshooting — Slow Queries]({BASE}/04-production-operations/troubleshooting/#slow-queries).

    ## Common Mistakes

    - Leading wildcard regex (`/.*foo/`) — cannot use index.
    - `$where` / `$function` — disables index use.
    - `$lookup` without index on `foreignField`.

    ## Interview Questions

    - Explain the ESR rule with an example compound index.
    - When is a covered query possible?
    - How do you optimize a pipeline with `$lookup` and `$match`?

    ## Architect Notes

    Index design is **access-pattern design** — gather queries before schema freeze.
    """,
        title="Query Optimization",
        desc="Query planner, index selection, covered queries, COLLSCAN vs IXSCAN, aggregation optimization.",
        short="Query Opt",
        mod=3,
        mod_title="Query & Performance",
        ref="3.6",
        weight=306,
    )


    w(
        "03-query-performance/explain-plan.md",
        f"""## Quick Revision

    - Always use **`explain("executionStats")`** in production tuning.
    - Compare **`totalDocsExamined`** to **`nReturned`** — ratio near 1 is ideal.
    - Inspect **`winningPlan`** stages: IXSCAN → FETCH vs PROJECTION_COVERED.

    ## Core Concepts

    | Field / stage | Meaning |
    | :--- | :--- |
    | `winningPlan` | Selected execution tree |
    | `rejectedPlans` | Alternatives the planner discarded |
    | `executionStats.nReturned` | Documents returned |
    | `totalDocsExamined` | Documents scanned |
    | `totalKeysExamined` | Index keys scanned |
    | `executionTimeMillis` | Server-side time |
    | `COLLSCAN` | Collection scan |
    | `IXSCAN` | Index scan |
    | `FETCH` | Load full document after index |
    | `PROJECTION_COVERED` | Index-only result |

    ## Internal Working

    ```javascript
    db.orders.find({{ status: "open" }}).sort({{ createdAt: -1 }}).explain("executionStats")
    ```

    Read `queryPlanner.winningPlan.inputStage` recursively for stage tree. High `totalDocsExamined` with low `nReturned` = wrong or missing index.

    ## Architecture

    Explain on **mongos** for sharded queries shows merge stages and per-shard plans.

    ## Production Patterns

    - Baseline explains before/after index changes.
    - Atlas explains integrate with Performance Advisor suggestions.

    ## Observability

    Store explains for regression comparison during schema migrations.

    ## Troubleshooting

    | Pattern | Likely fix |
    | :--- | :--- |
    | COLLSCAN + high docsExamined | Add compound index (ESR) |
    | IXSCAN + high FETCH | Add projection to index (covered query) |
    | SORT stage + high memory | Index must support sort order |
    | SHARDING_FILTER missing | Query not targeted — add shard key |

    ## Common Mistakes

    - Using `explain()` without `executionStats` — no actual counts.
    - Judging staging explains on empty collections.

    ## Interview Questions

    - Walk through reading `winningPlan` for a slow query.
    - What does `rejectedPlans` tell you?
    - How do you detect an in-memory sort?

    ## Architect Notes

    Explain output is the **contract** between application queries and ops — automate checks in CI for critical paths where feasible.
    """,
        title="Explain Plan",
        desc="executionStats, winningPlan, rejectedPlans, and index analysis for MongoDB queries.",
        short="Explain",
        mod=3,
        mod_title="Query & Performance",
        ref="3.7",
        weight=307,
    )


    w(
        "04-production-operations/monitoring.md",
        f"""## Quick Revision

    - **mongostat** — throughput, opcounters, replication lag columns.
    - **mongotop** — per-collection read/write time.
    - **Profiler** + Atlas **Performance Advisor** — slow query discovery.
    - Alert on **replication lag**, **opcounters** anomalies, **cache pressure**.

    ## Core Concepts

    | Tool | Use |
    | :--- | :--- |
    | `mongostat` | Live server metrics (5s interval typical) |
    | `mongotop` | Collection-level latency breakdown |
    | `db.setProfilingLevel(1, {{ slowms: 100 }})` | Capture slow ops |
    | `db.currentOp()` | In-flight operations |
    | `$indexStats` | Index usage frequency |
    | Atlas metrics | CPU, disk IOPS, connections, opcounters, lag |

    ## Production Patterns

    ```bash
    mongostat --uri "mongodb://..." 5
    mongotop --uri "mongodb://..." 5
    ```

    ```javascript
    db.setProfilingLevel(1, {{ slowms: 100 }})
    db.system.profile.find().sort({{ ts: -1 }}).limit(5)
    db.currentOp({{ "active": true, "secs_running": {{ $gt: 3 }} }})
    db.orders.aggregate([{{ $indexStats: {{}} }}])
    ```

    ## Observability

    | Metric | Alert threshold (tune per SLO) |
    | :--- | :--- |
    | Replication lag | > 10–30s sustained |
    | Connections | > 80% of `maxIncomingConnections` |
    | Disk utilization | > 75% |
    | Cache evictions | Sustained high rate |
    | Queued readers/writers | Non-zero sustained |

    ## Reliability

    Lag monitoring on all secondaries; **hidden** and **delayed** nodes need separate dashboards.

    ## Troubleshooting

    Slow query triage → [Explain Plan]({BASE}/03-query-performance/explain-plan/) → [Troubleshooting]({BASE}/04-production-operations/troubleshooting/).

    ## Common Mistakes

    - Profiling level 2 in production (full logging) — disk explosion.
    - Monitoring primary only on sharded clusters — per-shard visibility required.

    ## Interview Questions

    - What mongostat columns indicate replication lag?
    - How do you find unused indexes in production?
    - What Atlas alerts would you configure before launch?

    ## Architect Notes

    Observability stack should tie **query shape** (profiler) to **capacity** (mongostat) to **topology** (per-shard lag).
    """,
        title="Monitoring",
        desc="mongostat, mongotop, Atlas metrics, replication lag monitoring, slow query analysis.",
        short="Monitoring",
        mod=4,
        mod_title="Production Operations",
        ref="4.2",
        weight=402,
    )


    w(
        "04-production-operations/troubleshooting.md",
        f"""## Quick Revision

    - **Replication lag** — disk, oplog size, write burst, network.
    - **Slow queries** — explain first; index or reshape query.
    - **Hot shard** — monotonic shard key; chunk imbalance.
    - **OOM / page faults** — working set exceeds RAM.

    ## Troubleshooting

    ### Replication Lag {{#replication-lag}}

    | Cause | Fix |
    | :--- | :--- |
    | Small oplog | Increase oplog; secondary resync if fallen off |
    | Disk saturation | Faster disks; throttle writes |
    | Large documents / bulk load | Batch off-peak; scale secondary |
    | Network partition | Fix connectivity; verify heartbeat |

    ### Slow Queries {{#slow-queries}}

    1. `explain("executionStats")` — COLLSCAN? high docsExamined?
    2. Profiler / Atlas slow query log.
    3. Add compound index (ESR) or covered projection.
    4. See [Query Optimization]({BASE}/03-query-performance/query-optimization/).

    ### Chunk Imbalance / Jumbo Chunks

    - `sh.status()` — uneven chunk distribution.
    - Monotonic shard key → single hot chunk.
    - Jumbo chunks block balancer — split or reshard migration.

    ### OOM / Cache Pressure

    - Page faults in `serverStatus.wiredTiger.cache`.
    - Remedy: RAM, indexes, working set reduction — [Capacity Planning]({BASE}/04-production-operations/capacity-planning/).

    ### Lock Contention

    - Document-level locks rarely block; long transactions or catalog ops can.
    - `db.currentOp()` for long-running ops; `db.killOp()`.

    ### Election Issues

    - Even member count; arbiter-only secondaries don't hold data.
    - Priority and network splits — check `rs.status()` and logs.

    ## Production Patterns

    Maintain runbooks linked from on-call playbooks with metric thresholds from [Monitoring]({BASE}/04-production-operations/monitoring/).

    ## Interview Questions

    - How do you diagnose replication lag vs application slowness?
    - What is a jumbo chunk and how do you remediate?
    - When can rolled-back writes occur after failover?

    ## Architect Notes

    Most production incidents are **query + capacity + shard key** — not mysterious engine bugs.
    """,
        title="Troubleshooting",
        desc="Runbooks for replication lag, slow queries, chunk imbalance, OOM, lock contention, elections.",
        short="Troubleshooting",
        mod=4,
        mod_title="Production Operations",
        ref="4.3",
        weight=403,
    )


    w(
        "04-production-operations/backup-recovery.md",
        f"""## Quick Revision

    - **mongodump/mongorestore** — logical backup; good for dev/migration.
    - **Atlas snapshots + PITR** — production default on M10+.
    - **Oplog** tail enables point-in-time between snapshots on self-managed RS.

    ## Core Concepts

    | Method | RPO | Use |
    | :--- | :--- | :--- |
    | mongodump | Snapshot time | Dev, small DBs, selective restore |
    | Atlas continuous backup | Minutes (PITR) | Production Atlas |
    | Filesystem snapshot | Crash-consistent | Self-managed with care |
    | Oplog replay | Between backups | PITR on replica sets |

    ## Production Patterns

    ```bash
    mongodump --uri="mongodb://..." --out=/backup/$(date +%F)
    mongorestore --uri="mongodb://..." /backup/2026-07-03
    ```

    Atlas: enable backup on M10+; test restore to staging quarterly.

    ## Reliability

    Test **restore drills** — backup without tested restore is worthless.

    ## Disaster Recovery

    1. Identify target RPO/RTO.
    2. Atlas: restore cluster or download snapshot.
    3. Self-managed: restore dump + replay oplog to timestamp.
    4. Validate application consistency after restore.

    ## Common Mistakes

    - mongodump on huge sharded clusters without coordination — use per-shard or Atlas.
    - No off-site copy of backups.

    ## Interview Questions

    - Compare mongodump vs Atlas PITR for production.
    - How does oplog sizing relate to PITR window?
    - What is your DR drill cadence?

    ## Architect Notes

    DR architecture must account for **sharded** topology — config server metadata and all shards.
    """,
        title="Backup & Recovery",
        desc="mongodump, mongorestore, PITR, oplog recovery, disaster recovery.",
        short="Backup",
        mod=4,
        mod_title="Production Operations",
        ref="4.4",
        weight=404,
    )


    w(
        "04-production-operations/capacity-planning.md",
        f"""## Quick Revision

    - **Working set** = hot data + indexes accessed frequently — should fit in RAM.
    - WiredTiger cache ≈ **50% RAM − 1 GB** by default.
    - Shard when single replica set saturates **CPU, disk I/O, or working set**.

    ## Core Concepts

    | Dimension | Rule of thumb |
    | :--- | :--- |
    | RAM | Working set + indexes + 25% headroom |
    | Storage | Data + indexes + oplog + journals + 30% free |
    | Connections | `maxPoolSize × app_instances` < mongod limit |
    | Shards | When vertical scale exhausted or write throughput bound |

    ## Internal Working

    Page faults (`serverStatus.wiredTiger.cache`) indicate working set overflow — latency climbs before OOM.

    ## Production Patterns

    - Growth model: data GB/month × retention × replication factor.
    - Pre-split chunks before bulk load on sharded collections.
    - Atlas cluster tier upgrades vs horizontal sharding decision tree.

    ## Scalability

    | Signal | Action |
    | :--- | :--- |
    | Sustained CPU > 70% | Scale tier or shard |
    | Disk IOPS saturated | Faster disks or shard |
    | Replication lag under write load | Scale primary or shard writes |
    | Working set >> RAM | More RAM or archive cold data |

    ## Interview Questions

    - How do you estimate if the working set fits in RAM?
    - When do you add shards vs bigger instances?
    - How does oplog size factor into capacity?

    ## Architect Notes

    Capacity planning ties **schema** (document size), **indexes** (RAM), and **shard key** (distribution) — plan all three together.
    """,
        title="Capacity Planning",
        desc="Working set, memory sizing, storage planning, growth planning, shard sizing.",
        short="Capacity",
        mod=4,
        mod_title="Production Operations",
        ref="4.5",
        weight=405,
    )


    # Comparisons
    w(
        "05-comparisons/mongodb-vs-postgresql.md",
        f"""## Quick Revision

    - **MongoDB** — flexible documents, horizontal scale, embed-first modeling.
    - **PostgreSQL** — SQL, joins, strong relational integrity, mature analytics.
    - Choose by **access patterns**, not ideology.

    ## Design Tradeoffs

    | Dimension | MongoDB | PostgreSQL |
    | :--- | :--- | :--- |
    | Schema | Flexible documents | Fixed tables + migrations |
    | Joins | `$lookup` / app-side | Native SQL joins |
    | Scale-out | Sharding built-in | Read replicas; sharding external (Citus) |
    | Transactions | Multi-doc (4.0+) | Full ACID decades |
    | Analytics | Aggregation pipeline | SQL window functions, BI ecosystem |

    ## Architecture

    MongoDB fits document-shaped domains (catalogs, content, IoT events). PostgreSQL fits relational invariants (ledger, inventory with constraints).

    ## Production Patterns

    - Hybrid: PostgreSQL system of record + MongoDB read model (CQRS).
    - See also [Database Handbook — MongoDB vs PostgreSQL](/database-handbook/mongodb-vs-postgresql/).

    ## Interview Questions

    - When would you choose MongoDB over PostgreSQL for a new platform?
    - How do you handle cross-document invariants in MongoDB?
    - What migration risks exist moving PostgreSQL → MongoDB?

    ## Architect Notes

    ADR should document **query patterns** and **consistency requirements** — not benchmark slogans.
    """,
        title="MongoDB vs PostgreSQL",
        desc="Document flexibility vs relational integrity — architect tradeoffs.",
        short="vs PostgreSQL",
        mod=5,
        mod_title="Comparisons",
        ref="5.1",
        weight=501,
    )


    w(
        "05-comparisons/mongodb-vs-cassandra.md",
        f"""## Quick Revision

    - **Cassandra** — write-optimized wide-column, tunable consistency, masterless ring.
    - **MongoDB** — rich document queries, secondary indexes, flexible aggregation.
    - Cassandra wins extreme write scale; MongoDB wins query flexibility.

    ## Design Tradeoffs

    | Dimension | MongoDB | Cassandra |
    | :--- | :--- | :--- |
    | Data model | BSON documents | Wide-column rows |
    | Query | Rich ad-hoc queries + indexes | Query must match partition key |
    | Consistency | RC/WC per operation | Tunable per read/write |
    | Ops | Replica sets + sharding | Gossip, no single master |

    ## When to Choose MongoDB

    - Evolving schema, varied queries, aggregation analytics on documents.

    ## When to Choose Cassandra

    - Time-series at massive write scale, geographic multi-DC with AP tolerance.

    ## Interview Questions

    - Compare consistency models.
    - When is Cassandra's partition key constraint unacceptable?

    ## Architect Notes

    Do not use Cassandra as a "faster MongoDB" — the query model is fundamentally different.
    """,
        title="MongoDB vs Cassandra",
        desc="Document database vs wide-column write scale — architect comparison.",
        short="vs Cassandra",
        mod=5,
        mod_title="Comparisons",
        ref="5.2",
        weight=502,
    )


    w(
        "05-comparisons/mongodb-vs-couchbase.md",
        f"""## Quick Revision

    - **Couchbase** — JSON documents + integrated caching (Memcached) + mobile sync.
    - **MongoDB** — general-purpose document DB + Atlas ecosystem.
    - Couchbase fits edge/mobile; MongoDB fits general application backend.

    ## Design Tradeoffs

    | Dimension | MongoDB | Couchbase |
    | :--- | :--- | :--- |
    | Cache layer | External (Redis) common | Integrated managed cache |
    | Mobile / offline | Mobile SDK secondary | First-class Couchbase Lite + Sync |
    | Query | MQL / aggregation | N1QL (SQL on JSON) |
    | Ops | Atlas managed option | Self-managed cluster |

    ## Interview Questions

    - When would integrated caching favor Couchbase?
    - Compare N1QL mental model to MongoDB aggregation.

    ## Architect Notes

    Evaluate **mobile sync** and **cache co-location** requirements early — they drive the decision.
    """,
        title="MongoDB vs Couchbase",
        desc="Document store comparison — caching, mobile sync, and query models.",
        short="vs Couchbase",
        mod=5,
        mod_title="Comparisons",
        ref="5.3",
        weight=503,
    )


    # Learning paths
    w(
        "07-learning-paths/mongodb-senior-engineer-path.md",
        f"""# MongoDB Senior Engineer Path

    **Goal:** Production-ready querying, indexing, and replica set operations.

    | Week | Topics |
    | :--- | :--- |
    | 1 | [Documents]({BASE}/01-fundamentals/documents/) → [CRUD]({BASE}/01-fundamentals/crud/) → [Indexes]({BASE}/03-query-performance/indexes/) |
    | 2 | [Query Optimization]({BASE}/03-query-performance/query-optimization/) → [Explain Plan]({BASE}/03-query-performance/explain-plan/) → [Aggregation]({BASE}/03-query-performance/aggregation-pipeline/) |
    | 3 | [Replication]({BASE}/02-core-mongodb/replication/) → [Transactions]({BASE}/02-core-mongodb/transactions/) |
    | 4 | [Performance]({BASE}/04-production-operations/performance/) → [Monitoring]({BASE}/04-production-operations/monitoring/) → [Troubleshooting]({BASE}/04-production-operations/troubleshooting/) |
    """,
        title="Senior Engineer Path",
        desc="Four-week path for senior engineers — queries through production ops.",
        short="Senior Path",
        mod=7,
        mod_title="Learning Paths",
        ref="7.1",
        weight=701,
    )

    w(
        "07-learning-paths/mongodb-lead-path.md",
        f"""# MongoDB Technical Lead Path

    **Goal:** Lead teams through schema, scale, and incident response.

    1. [Schema Design]({BASE}/02-core-mongodb/schema-design/) — embed/reference ADRs
    2. [Sharding]({BASE}/02-core-mongodb/sharding/) — shard key workshops
    3. [Capacity Planning]({BASE}/04-production-operations/capacity-planning/) — growth models
    4. [Monitoring]({BASE}/04-production-operations/monitoring/) + [Troubleshooting]({BASE}/04-production-operations/troubleshooting/) — runbooks
    5. [Backup & Recovery]({BASE}/04-production-operations/backup-recovery/) — drill ownership
    6. [Top 150 — Troubleshooting subset]({BASE}/06-interview-guide/troubleshooting-questions/)
    """,
        title="Technical Lead Path",
        desc="Ops, capacity, sharding, and troubleshooting for technical leads.",
        short="Lead Path",
        mod=7,
        mod_title="Learning Paths",
        ref="7.2",
        weight=702,
    )

    w(
        "07-learning-paths/mongodb-architect-path.md",
        f"""# MongoDB Architect Path

    **Goal:** Platform ADRs, comparisons, and cross-cutting reliability.

    1. [Architecture]({BASE}/02-core-mongodb/architecture/) → [Storage Engine]({BASE}/02-core-mongodb/storage-engine/)
    2. [Replication]({BASE}/02-core-mongodb/replication/) + [Sharding]({BASE}/02-core-mongodb/sharding/) — topology ADRs
    3. [Comparisons]({BASE}/05-comparisons/) — PostgreSQL, Cassandra, Couchbase
    4. [Atlas Basics]({BASE}/01-fundamentals/atlas-basics/) — managed vs self-hosted
    5. [Architect Questions]({BASE}/06-interview-guide/architect-questions/)
    6. Cross-link [Database Handbook — MongoDB](/database-handbook/mongodb/)
    """,
        title="Architect Path",
        desc="Topology, storage, comparisons, and ADR-level MongoDB decisions.",
        short="Architect Path",
        mod=7,
        mod_title="Learning Paths",
        ref="7.3",
        weight=703,
    )

    w(
        "07-learning-paths/mongodb-interview-revision-path.md",
        f"""# MongoDB Interview Revision Path

    **Goal:** 48-hour cram before senior/architect interviews.

    | Block | Time | Focus |
    | :--- | :--- | :--- |
    | **Block 1** | 2h | [Architecture]({BASE}/02-core-mongodb/architecture/) · [Storage Engine]({BASE}/02-core-mongodb/storage-engine/) · [Replication]({BASE}/02-core-mongodb/replication/) |
    | **Block 2** | 2h | [Sharding]({BASE}/02-core-mongodb/sharding/) · [Schema Design]({BASE}/02-core-mongodb/schema-design/) |
    | **Block 3** | 2h | [Query Optimization]({BASE}/03-query-performance/query-optimization/) · [Explain Plan]({BASE}/03-query-performance/explain-plan/) |
    | **Block 4** | 2h | [Troubleshooting]({BASE}/04-production-operations/troubleshooting/) · [Monitoring]({BASE}/04-production-operations/monitoring/) |
    | **Block 5** | 2h | [Top 150 Questions]({BASE}/06-interview-guide/top-150-interview-questions/) — skim all categories |

    Pair with [Architect Questions]({BASE}/06-interview-guide/architect-questions/) for panel prep.
    """,
        title="Interview Revision Path",
        desc="48-hour interview cram schedule mapped to handbook topics.",
        short="Interview Path",
        mod=7,
        mod_title="Learning Paths",
        ref="7.4",
        weight=704,
    )


    from mongodb_questions_data import QUESTIONS

    assert len(QUESTIONS) == 150, len(QUESTIONS)

    q_rows = "\n".join(
        f'| {n} | {q} | {d} | {l} | {t} | `{BASE}/{doc.replace(".md", "")}/` |'
        for n, q, d, l, t, doc in QUESTIONS
    )

    w(
        "06-interview-guide/top-150-interview-questions.md",
        f"""Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. Questions only — no answers.

    **Distribution:** Architecture 40 · Troubleshooting 30 · Performance 25 · Reliability 20 · Security 15 · Cross-cutting 20

    | # | Question | Difficulty | Level | Topic | Deep Dive |
    |---|----------|------------|--------|-------|-----------|
    {q_rows}
    """,
        title="Top 150 MongoDB Interview Questions",
        desc="150 production-oriented MongoDB interview questions mapped to handbook topics.",
        short="Top 150",
        mod=6,
        mod_title="Interview Guide",
        ref="6.1",
        weight=601,
    )

    ARCHITECT_QS = [q for _, q, _, l, _, _ in QUESTIONS if l == "Architect"][:40]
    TROUBLE_QS = [QUESTIONS[i][1] for i in range(40, 70)]
    PERF_QS = [QUESTIONS[i][1] for i in range(70, 95)]

    w(
        "06-interview-guide/architect-questions.md",
        "Questions only — no answers. Sourced from [Top 150](" + BASE + "/06-interview-guide/top-150-interview-questions/).\n\n# Architect-Level Questions\n\n"
        + "\n".join(f"{i}. {q}" for i, q in enumerate(ARCHITECT_QS, 1)),
        title="Architect-Level Questions",
        desc="Curated architect-level MongoDB interview questions.",
        short="Architect",
        mod=6,
        mod_title="Interview Guide",
        ref="6.2",
        weight=602,
    )

    w(
        "06-interview-guide/troubleshooting-questions.md",
        "Questions only — no answers.\n\n# Troubleshooting Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(TROUBLE_QS, 1)),
        title="Troubleshooting Questions",
        desc="Production troubleshooting interview questions for MongoDB.",
        short="Troubleshooting Q",
        mod=6,
        mod_title="Interview Guide",
        ref="6.3",
        weight=603,
    )

    w(
        "06-interview-guide/performance-questions.md",
        "Questions only — no answers.\n\n# Performance Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(PERF_QS, 1)),
        title="Performance Questions",
        desc="MongoDB performance and tuning interview questions.",
        short="Performance Q",
        mod=6,
        mod_title="Interview Guide",
        ref="6.4",
        weight=604,
    )


    # Handbook index
    w(
        "_index.md",
        f"""# MongoDB Handbook

    Production and interview knowledge base for **Senior Engineers**, **Technical Leads**, and **Architects** (6+ years).

    ## Learning Paths

    | Track | Start here | Goal |
    | :--- | :--- | :--- |
    | **Quick revision** | [Interview Revision Path]({BASE}/07-learning-paths/mongodb-interview-revision-path/) | 48-hour cram |
    | **Senior engineer** | [Senior Engineer Path]({BASE}/07-learning-paths/mongodb-senior-engineer-path/) | Queries, indexes, replication, ops |
    | **Technical lead** | [Lead Path]({BASE}/07-learning-paths/mongodb-lead-path/) | Sharding, capacity, runbooks |
    | **Architect** | [Architect Path]({BASE}/07-learning-paths/mongodb-architect-path/) | Topology ADRs, comparisons |
    | **Interview prep** | [Top 150 Questions]({BASE}/06-interview-guide/top-150-interview-questions/) | Role-specific banks |

    ## Modules

    1. **Fundamentals** — documents, collections, CRUD, Atlas
    2. **Core MongoDB** — architecture, storage engine, replication, sharding, transactions, schema
    3. **Query & Performance** — indexes, aggregation, optimization, explain
    4. **Production Operations** — tuning, monitoring, troubleshooting, backup, capacity
    5. **Comparisons** — PostgreSQL, Cassandra, Couchbase
    6. **Interview Guide** — 150 questions + subsets
    7. **Learning Paths** — curated reading by role

    See also: [Database Handbook — MongoDB](/database-handbook/mongodb/) · [MongoDB vs PostgreSQL](/database-handbook/mongodb-vs-postgresql/)
    """,
        title="MongoDB Handbook",
        desc="MongoDB handbook — architecture, performance, operations, and interview prep for senior engineers.",
        short="Handbook",
        mod=0,
        mod_title="MongoDB Handbook",
        ref="0",
        weight=1,
    )


    # YAML updates
    modules_yaml = """# MongoDB Handbook — module index.
    modules:
      - id: 1
        focus: "Fundamentals"
        topics:
          - 01-fundamentals/documents
          - 01-fundamentals/collections
          - 01-fundamentals/crud
          - 01-fundamentals/atlas-basics

      - id: 2
        focus: "Core MongoDB"
        topics:
          - 02-core-mongodb/architecture
          - 02-core-mongodb/storage-engine
          - 02-core-mongodb/replication
          - 02-core-mongodb/sharding
          - 02-core-mongodb/transactions
          - 02-core-mongodb/schema-design

      - id: 3
        focus: "Query & Performance"
        topics:
          - 03-query-performance/indexes
          - 03-query-performance/ttl-index
          - 03-query-performance/text-search
          - 03-query-performance/geospatial
          - 03-query-performance/aggregation-pipeline
          - 03-query-performance/query-optimization
          - 03-query-performance/explain-plan

      - id: 4
        focus: "Production Operations"
        topics:
          - 04-production-operations/performance
          - 04-production-operations/monitoring
          - 04-production-operations/troubleshooting
          - 04-production-operations/backup-recovery
          - 04-production-operations/capacity-planning

      - id: 5
        focus: "Comparisons"
        topics:
          - 05-comparisons/mongodb-vs-postgresql
          - 05-comparisons/mongodb-vs-cassandra
          - 05-comparisons/mongodb-vs-couchbase

      - id: 6
        focus: "Interview Guide"
        topics:
          - 06-interview-guide/top-150-interview-questions
          - 06-interview-guide/architect-questions
          - 06-interview-guide/troubleshooting-questions
          - 06-interview-guide/performance-questions

      - id: 7
        focus: "Learning Paths"
        topics:
          - 07-learning-paths/mongodb-senior-engineer-path
          - 07-learning-paths/mongodb-lead-path
          - 07-learning-paths/mongodb-architect-path
          - 07-learning-paths/mongodb-interview-revision-path
    """

    order_yaml = """# Topic order — derived from mongodb_cheatsheet_modules.yaml.
    topics:
      - 01-fundamentals/documents
      - 01-fundamentals/collections
      - 01-fundamentals/crud
      - 01-fundamentals/atlas-basics
      - 02-core-mongodb/architecture
      - 02-core-mongodb/storage-engine
      - 02-core-mongodb/replication
      - 02-core-mongodb/sharding
      - 02-core-mongodb/transactions
      - 02-core-mongodb/schema-design
      - 03-query-performance/indexes
      - 03-query-performance/ttl-index
      - 03-query-performance/text-search
      - 03-query-performance/geospatial
      - 03-query-performance/aggregation-pipeline
      - 03-query-performance/query-optimization
      - 03-query-performance/explain-plan
      - 04-production-operations/performance
      - 04-production-operations/monitoring
      - 04-production-operations/troubleshooting
      - 04-production-operations/backup-recovery
      - 04-production-operations/capacity-planning
      - 05-comparisons/mongodb-vs-postgresql
      - 05-comparisons/mongodb-vs-cassandra
      - 05-comparisons/mongodb-vs-couchbase
      - 06-interview-guide/top-150-interview-questions
      - 06-interview-guide/architect-questions
      - 06-interview-guide/troubleshooting-questions
      - 06-interview-guide/performance-questions
      - 07-learning-paths/mongodb-senior-engineer-path
      - 07-learning-paths/mongodb-lead-path
      - 07-learning-paths/mongodb-architect-path
      - 07-learning-paths/mongodb-interview-revision-path
    """

    (DATA / "mongodb_cheatsheet_modules.yaml").write_text(modules_yaml, encoding="utf-8")
    (DATA / "mongodb_cheatsheet_order.yaml").write_text(order_yaml, encoding="utf-8")

    # Remove old flat files
    OLD_FLAT = [
        "architecture.md",
        "documents.md",
        "collections.md",
        "crud.md",
        "atlas-basics.md",
        "indexes.md",
        "ttl-index.md",
        "text-search.md",
        "geospatial.md",
        "aggregation-pipeline.md",
        "replication.md",
        "sharding.md",
        "transactions.md",
        "schema-design.md",
        "performance.md",
        "mongo-shell-commands.md",
        "interview-questions.md",
    ]
    for name in OLD_FLAT:
        p = HB / name
        if p.exists():
            p.unlink()

    print("MongoDB handbook Phase B generated successfully.")
    print(f"Topics: {len(order_yaml.strip().splitlines()) - 2} in order yaml")


if __name__ == "__main__":
    main()
