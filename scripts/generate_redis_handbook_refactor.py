"""Generate refactored Redis handbook content (Phase B)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "redis-cheatsheet"
DATA = ROOT / "data"
DATE = "2026-07-03T13:00:00+00:00"
BASE = "/redis-cheatsheet"


def aliases_block(*paths: str) -> str:
    if not paths:
        return ""
    lines = "\n".join(f'  - "{p}"' for p in paths)
    return f"\naliases:\n{lines}"


def make_fm(
    *,
    title: str,
    desc: str,
    short: str,
    mod: int,
    mod_title: str,
    ref: str,
    weight: int,
    alias_paths: tuple[str, ...] = (),
    cheat: bool = False,
    interview: bool = False,
) -> str:
    alias_part = aliases_block(*alias_paths)
    lines = [
        "---",
        f'title: "{title}"',
        f"date: {DATE}",
        "draft: false",
        f'description: "{desc}"',
        'tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]',
        'categories: ["Redis Handbook"]',
        f'shortTitle: "{short}"',
        f"module: {mod}",
        f'moduleTitle: "{mod_title}"',
        f'sectionRef: "{ref}"',
        f"weight: {weight}",
        ]
    if cheat:
        lines.append("cheatSheet: true")
    if interview:
        lines.append("interviewHandbook: true")
    if alias_part:
        lines.append(alias_part)
    lines.extend(["---", ""])
    return "\n".join(lines)


def w(
    rel: str,
    body: str,
    *,
    cheat: bool = False,
    interview: bool = False,
    alias_paths: tuple[str, ...] = (),
    **fm: str | int,
) -> None:
    path = HB / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    text = make_fm(
        cheat=cheat,
        interview=interview,
        alias_paths=alias_paths,
        title=str(fm["title"]),
        desc=str(fm["desc"]),
        short=str(fm["short"]),
        mod=int(fm["mod"]),
        mod_title=str(fm["mod_title"]),
        ref=str(fm["ref"]),
        weight=int(fm["weight"]),
    )
    path.write_text(text + body.strip() + "\n", encoding="utf-8")


def read_old(name: str) -> str:
    """Read legacy flat page from disk or git HEAD when flat files were removed."""
    import subprocess

    p = HB / name
    text = ""
    if p.exists():
        text = p.read_text(encoding="utf-8")
    else:
        result = subprocess.run(
            ["git", "show", f"HEAD:content/redis-cheatsheet/{name}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            text = result.stdout
    if not text.strip():
        return ""
    return re.sub(r"^---.*?---\n", "", text, count=1, flags=re.DOTALL).strip() + "\n"


def slug_from_rel(rel: str) -> str:
    return rel.replace("\\", "/").replace(".md", "")


TOPICS_ORDER = [
    "01-fundamentals/architecture",
    "01-fundamentals/data-structures",
    "02-core-redis/strings",
    "02-core-redis/hashes",
    "02-core-redis/lists",
    "02-core-redis/sets",
    "02-core-redis/sorted-sets",
    "02-core-redis/bitmaps",
    "02-core-redis/hyperloglog",
    "03-redis-internals/memory-management",
    "03-redis-internals/redis-protocol",
    "03-redis-internals/persistence",
    "03-redis-internals/replication",
    "03-redis-internals/sentinel",
    "03-redis-internals/cluster",
    "04-distributed-systems/distributed-lock",
    "04-distributed-systems/transactions",
    "04-distributed-systems/pub-sub",
    "04-distributed-systems/streams",
    "04-distributed-systems/lua-scripts",
    "05-production-patterns/caching-patterns",
    "05-production-patterns/cache-invalidation",
    "05-production-patterns/cache-breakdown",
    "05-production-patterns/cache-avalanche",
    "05-production-patterns/cache-penetration",
    "05-production-patterns/session-store",
    "05-production-patterns/rate-limiter",
    "06-performance-operations/eviction-policies",
    "06-performance-operations/performance-tuning",
    "06-performance-operations/monitoring",
    "06-performance-operations/capacity-planning",
    "06-performance-operations/troubleshooting",
    "07-comparisons/redis-vs-memcached",
    "07-comparisons/redis-vs-kafka",
    "07-comparisons/redis-vs-rabbitmq",
    "08-interview-guide/top-150-interview-questions",
    "08-interview-guide/architect-questions",
    "08-interview-guide/troubleshooting-questions",
    "08-interview-guide/performance-questions",
    "09-learning-paths/redis-senior-engineer-path",
    "09-learning-paths/redis-lead-path",
    "09-learning-paths/redis-architect-path",
    "09-learning-paths/redis-interview-revision-path",
]

TITLE_BY_SLUG = {
    "01-fundamentals/architecture": "Architecture",
    "01-fundamentals/data-structures": "Data Structures",
    "02-core-redis/strings": "Strings",
    "02-core-redis/hashes": "Hashes",
    "02-core-redis/lists": "Lists",
    "02-core-redis/sets": "Sets",
    "02-core-redis/sorted-sets": "Sorted Sets",
    "02-core-redis/bitmaps": "Bitmaps",
    "02-core-redis/hyperloglog": "HyperLogLog",
    "03-redis-internals/memory-management": "Memory Management",
    "03-redis-internals/redis-protocol": "Redis Protocol",
    "03-redis-internals/persistence": "Persistence",
    "03-redis-internals/replication": "Replication",
    "03-redis-internals/sentinel": "Sentinel",
    "03-redis-internals/cluster": "Cluster",
    "04-distributed-systems/distributed-lock": "Distributed Lock",
    "04-distributed-systems/transactions": "Transactions",
    "04-distributed-systems/pub-sub": "Pub/Sub",
    "04-distributed-systems/streams": "Streams",
    "04-distributed-systems/lua-scripts": "Lua Scripts",
    "05-production-patterns/caching-patterns": "Caching Patterns",
    "05-production-patterns/cache-invalidation": "Cache Invalidation",
    "05-production-patterns/cache-breakdown": "Cache Breakdown",
    "05-production-patterns/cache-avalanche": "Cache Avalanche",
    "05-production-patterns/cache-penetration": "Cache Penetration",
    "05-production-patterns/session-store": "Session Store",
    "05-production-patterns/rate-limiter": "Rate Limiter",
    "06-performance-operations/eviction-policies": "Eviction Policies",
    "06-performance-operations/performance-tuning": "Performance Tuning",
    "06-performance-operations/monitoring": "Monitoring",
    "06-performance-operations/capacity-planning": "Capacity Planning",
    "06-performance-operations/troubleshooting": "Troubleshooting",
    "07-comparisons/redis-vs-memcached": "Redis vs Memcached",
    "07-comparisons/redis-vs-kafka": "Redis vs Kafka",
    "07-comparisons/redis-vs-rabbitmq": "Redis vs RabbitMQ",
    "08-interview-guide/top-150-interview-questions": "Top 150 Interview Questions",
    "08-interview-guide/architect-questions": "Architect Questions",
    "08-interview-guide/troubleshooting-questions": "Troubleshooting Questions",
    "08-interview-guide/performance-questions": "Performance Questions",
    "09-learning-paths/redis-senior-engineer-path": "Senior Engineer Path",
    "09-learning-paths/redis-lead-path": "Lead Path",
    "09-learning-paths/redis-architect-path": "Architect Path",
    "09-learning-paths/redis-interview-revision-path": "Interview Revision Path",
}


def fix_links(body: str) -> str:
    mapping = {
        "/redis-cheatsheet/architecture/": f"{BASE}/01-fundamentals/architecture/",
        "/redis-cheatsheet/data-structures/": f"{BASE}/01-fundamentals/data-structures/",
        "/redis-cheatsheet/strings/": f"{BASE}/02-core-redis/strings/",
        "/redis-cheatsheet/hashes/": f"{BASE}/02-core-redis/hashes/",
        "/redis-cheatsheet/lists/": f"{BASE}/02-core-redis/lists/",
        "/redis-cheatsheet/sets/": f"{BASE}/02-core-redis/sets/",
        "/redis-cheatsheet/sorted-sets/": f"{BASE}/02-core-redis/sorted-sets/",
        "/redis-cheatsheet/bitmaps/": f"{BASE}/02-core-redis/bitmaps/",
        "/redis-cheatsheet/hyperloglog/": f"{BASE}/02-core-redis/hyperloglog/",
        "/redis-cheatsheet/persistence/": f"{BASE}/03-redis-internals/persistence/",
        "/redis-cheatsheet/replication/": f"{BASE}/03-redis-internals/replication/",
        "/redis-cheatsheet/sentinel/": f"{BASE}/03-redis-internals/sentinel/",
        "/redis-cheatsheet/cluster/": f"{BASE}/03-redis-internals/cluster/",
        "/redis-cheatsheet/distributed-lock/": f"{BASE}/04-distributed-systems/distributed-lock/",
        "/redis-cheatsheet/transactions/": f"{BASE}/04-distributed-systems/transactions/",
        "/redis-cheatsheet/pub-sub/": f"{BASE}/04-distributed-systems/pub-sub/",
        "/redis-cheatsheet/streams/": f"{BASE}/04-distributed-systems/streams/",
        "/redis-cheatsheet/lua-scripts/": f"{BASE}/04-distributed-systems/lua-scripts/",
        "/redis-cheatsheet/caching-patterns/": f"{BASE}/05-production-patterns/caching-patterns/",
        "/redis-cheatsheet/session-store/": f"{BASE}/05-production-patterns/session-store/",
        "/redis-cheatsheet/rate-limiter/": f"{BASE}/05-production-patterns/rate-limiter/",
        "/redis-cheatsheet/eviction-policies/": f"{BASE}/06-performance-operations/eviction-policies/",
        "/redis-cheatsheet/common-redis-commands/": f"{BASE}/06-performance-operations/monitoring/",
        "/redis-cheatsheet/interview-questions/": f"{BASE}/08-interview-guide/top-150-interview-questions/",
    }
    for old, new in mapping.items():
        body = body.replace(old, new)
        body = body.replace(old.rstrip("/"), new.rstrip("/"))
    return body


def render_see_also(slug: str) -> str:
    idx = TOPICS_ORDER.index(slug)
    lines = ["## See Also", ""]
    if idx > 0:
        prev_slug = TOPICS_ORDER[idx - 1]
        lines.append(f"- [Previous: {TITLE_BY_SLUG[prev_slug]}]({BASE}/{prev_slug}/)")
    if idx < len(TOPICS_ORDER) - 1:
        next_slug = TOPICS_ORDER[idx + 1]
        lines.append(f"- [Next: {TITLE_BY_SLUG[next_slug]}]({BASE}/{next_slug}/)")
    lines.append(f"- [Redis Handbook Index]({BASE}/)")
    return "\n".join(lines) + "\n"


def patch_see_also(body: str, slug: str) -> str:
    body = re.sub(r"\n## Related Topics[\s\S]*$", "\n", body).rstrip() + "\n\n"
    body = re.sub(r"\n## See Also[\s\S]*$", "\n", body).rstrip() + "\n\n"
    return body + render_see_also(slug)


def patch_architecture(body: str) -> str:
    if "## Quick Revision" not in body:
        body = body.replace(
            "## Executive Summary",
            "## Quick Revision\n\n"
            "- Redis runs command execution on one event loop thread; network I/O threads are optional.\n"
            f"- For memory internals, see [Memory Management]({BASE}/03-redis-internals/memory-management/).\n"
            f"- For protocol and pipelining internals, see [Redis Protocol]({BASE}/03-redis-internals/redis-protocol/).\n\n"
            "## Executive Summary",
        )
    body = re.sub(
        r"\| \*\*RESP\*\* \|.*\n",
        f"| **RESP** | See [Redis Protocol]({BASE}/03-redis-internals/redis-protocol/) |\n",
        body,
    )
    body = re.sub(
        r"\| \*\*Memory\*\* \|.*\n",
        f"| **Memory** | See [Memory Management]({BASE}/03-redis-internals/memory-management/) |\n",
        body,
    )
    body = body.replace(
        "| `MONITOR` on busy instance | Use `LATENCY DOCTOR`, slowlog |",
        f"| `MONITOR` on busy instance | Use [Monitoring]({BASE}/06-performance-operations/monitoring/) runbooks |",
    )
    return body


def patch_data_structures(body: str) -> str:
    return re.sub(
        r"\*\*Encoding:\*\*.*",
        f"Encoding internals and upgrade thresholds are covered in [Memory Management]({BASE}/03-redis-internals/memory-management/).",
        body,
    )


def patch_strings(body: str) -> str:
    body = re.sub(
        r"### Cache-aside read[\s\S]*?```",
        f"### Cache-aside read\n\nUse the canonical cache-aside flow in [Caching Patterns]({BASE}/05-production-patterns/caching-patterns/).",
        body,
        count=1,
    )
    body = body.replace(
        "| `SETNX` without TTL | Dead lock if client dies — always `SET NX EX` |",
        f"| `SETNX` without TTL | Dead lock risk — use lock guidance from [Distributed Lock]({BASE}/04-distributed-systems/distributed-lock/) |",
    )
    body = body.replace(
        "| **Conditional set** | `SET key val NX EX 30` — lock + TTL |",
        f"| **Conditional set** | `SET key val NX EX 30` — see [Distributed Lock]({BASE}/04-distributed-systems/distributed-lock/) |",
    )
    return body


def patch_caching_patterns(body: str) -> str:
    body = body.replace(
        "| **TTL jitter** | `EX = base + random(0, 60)` avoids thundering herd |",
        f"| **TTL jitter** | See [Cache Avalanche]({BASE}/05-production-patterns/cache-avalanche/) |",
    )
    body = body.replace(
        "### Stampede lock\n\n```bash\nSET lock:rebuild:product:99 1 NX EX 10\n# winner rebuilds; losers retry GET or wait\n```",
        f"### Stampede lock\n\nFor lock strategy and hot-key rebuild flow, see [Cache Breakdown]({BASE}/05-production-patterns/cache-breakdown/).",
    )
    body = body.replace(
        "### Probabilistic early expiration\n\nRefresh cache when `ttl < random_threshold`.",
        f"### Probabilistic early expiration\n\nSee [Cache Avalanche]({BASE}/05-production-patterns/cache-avalanche/) for expiry spread patterns.",
    )
    body = body.replace(
        "| Cache inconsistency after DB update | Delete/update cache on write |",
        f"| Cache inconsistency after DB update | Use [Cache Invalidation]({BASE}/05-production-patterns/cache-invalidation/) patterns |",
    )
    body = body.replace(
        "| Same TTL for all keys | Expiry stampede — add jitter |",
        f"| Same TTL for all keys | See [Cache Avalanche]({BASE}/05-production-patterns/cache-avalanche/) |",
    )
    body = body.replace(
        "| Caching null forever | Short TTL for negative cache |",
        f"| Caching null forever | See [Cache Penetration]({BASE}/05-production-patterns/cache-penetration/) |",
    )
    return body


def patch_lua_scripts(body: str) -> str:
    return re.sub(
        r"### Safe lock release[\s\S]*?```bash[\s\S]*?```",
        f"### Safe lock release\n\nUse the canonical lock release pattern in [Distributed Lock]({BASE}/04-distributed-systems/distributed-lock/).",
        body,
        count=1,
    )


def patch_pub_sub(body: str) -> str:
    return re.sub(
        r"### Invalidation broadcast[\s\S]*?Apps subscribe and evict local/Redis cache keys\.",
        f"### Invalidation broadcast\n\nFor full invalidation flow and consistency tradeoffs, see [Cache Invalidation]({BASE}/05-production-patterns/cache-invalidation/).",
        body,
        count=1,
    )


SECTIONS = [
    ("01-fundamentals", "Fundamentals", "Redis runtime model and type-selection basics.", 1),
    ("02-core-redis", "Core Redis", "Core Redis data types and command-centric quick references.", 2),
    ("03-redis-internals", "Redis Internals", "Memory, protocol, persistence, replication, Sentinel, and Cluster internals.", 3),
    ("04-distributed-systems", "Distributed Systems", "Coordination patterns with locks, transactions, streams, and pub/sub.", 4),
    ("05-production-patterns", "Production Patterns", "Caching, invalidation, failure-mode handling, sessions, and rate limiting.", 5),
    ("06-performance-operations", "Performance & Operations", "Tuning, monitoring, troubleshooting, capacity, and eviction policy.", 6),
    ("07-comparisons", "Comparisons", "Redis tradeoffs vs Memcached, Kafka, and RabbitMQ.", 7),
    ("08-interview-guide", "Interview Guide", "Top 150 questions plus role-specific subsets.", 8),
    ("09-learning-paths", "Learning Paths", "Role-specific reading paths for senior, lead, architect, and interview prep.", 9),
]

MODULE_TOPICS = {
    "01-fundamentals": [
        "01-fundamentals/architecture",
        "01-fundamentals/data-structures",
    ],
    "02-core-redis": [
        "02-core-redis/strings",
        "02-core-redis/hashes",
        "02-core-redis/lists",
        "02-core-redis/sets",
        "02-core-redis/sorted-sets",
        "02-core-redis/bitmaps",
        "02-core-redis/hyperloglog",
    ],
    "03-redis-internals": [
        "03-redis-internals/memory-management",
        "03-redis-internals/redis-protocol",
        "03-redis-internals/persistence",
        "03-redis-internals/replication",
        "03-redis-internals/sentinel",
        "03-redis-internals/cluster",
    ],
    "04-distributed-systems": [
        "04-distributed-systems/distributed-lock",
        "04-distributed-systems/transactions",
        "04-distributed-systems/pub-sub",
        "04-distributed-systems/streams",
        "04-distributed-systems/lua-scripts",
    ],
    "05-production-patterns": [
        "05-production-patterns/caching-patterns",
        "05-production-patterns/cache-invalidation",
        "05-production-patterns/cache-breakdown",
        "05-production-patterns/cache-avalanche",
        "05-production-patterns/cache-penetration",
        "05-production-patterns/session-store",
        "05-production-patterns/rate-limiter",
    ],
    "06-performance-operations": [
        "06-performance-operations/eviction-policies",
        "06-performance-operations/performance-tuning",
        "06-performance-operations/monitoring",
        "06-performance-operations/capacity-planning",
        "06-performance-operations/troubleshooting",
    ],
    "07-comparisons": [
        "07-comparisons/redis-vs-memcached",
        "07-comparisons/redis-vs-kafka",
        "07-comparisons/redis-vs-rabbitmq",
    ],
    "08-interview-guide": [
        "08-interview-guide/top-150-interview-questions",
        "08-interview-guide/architect-questions",
        "08-interview-guide/troubleshooting-questions",
        "08-interview-guide/performance-questions",
    ],
    "09-learning-paths": [
        "09-learning-paths/redis-senior-engineer-path",
        "09-learning-paths/redis-lead-path",
        "09-learning-paths/redis-architect-path",
        "09-learning-paths/redis-interview-revision-path",
    ],
}


def section_index_body(folder: str, title: str) -> str:
    topics = MODULE_TOPICS[folder]
    bullets = "\n".join(f"- [{TITLE_BY_SLUG[t]}]({BASE}/{t}/)" for t in topics)
    return (
        f"# {title}\n\n"
        f"This module is part of the Redis handbook structured for senior engineers, leads, and architects.\n\n"
        "## Ordered Reading\n\n"
        f"{bullets}\n\n"
        "## Start Here If...\n\n"
        "- You want canonical pages in recommended order.\n"
        "- You are preparing for production incidents or interviews.\n"
    )


def main() -> None:
    for folder, title, desc, mod in SECTIONS:
        w(
            f"{folder}/_index.md",
            section_index_body(folder, title),
            title=title,
            desc=desc,
            short=title,
            mod=mod,
            mod_title="Redis Handbook",
            ref="0",
            weight=mod,
        )

    def move_page(
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
        patch=None,
    ) -> None:
        body = fix_links(read_old(old))
        if patch:
            body = patch(body)
        slug = slug_from_rel(new)
        body = patch_see_also(body, slug)
        w(
            new,
            body,
            cheat=new.startswith("02-core-redis/"),
            title=title,
            desc=desc,
            short=short,
            mod=mod,
            mod_title=mod_title,
            ref=ref,
            weight=weight,
            alias_paths=(f"{BASE}/{alias}/",),
        )

    moves = [
        ("architecture.md", "01-fundamentals/architecture.md", "Architecture", "Redis runtime model and deployment baseline.", "Architecture", 1, "Fundamentals", "1.1", 101, "architecture"),
        ("data-structures.md", "01-fundamentals/data-structures.md", "Data Structures", "Redis type selection and key modeling basics.", "Data Struct", 1, "Fundamentals", "1.2", 102, "data-structures"),
        ("strings.md", "02-core-redis/strings.md", "Strings", "String operations, counters, and value encoding basics.", "Strings", 2, "Core Redis", "2.1", 201, "strings"),
        ("hashes.md", "02-core-redis/hashes.md", "Hashes", "Field-level object storage and hash operation patterns.", "Hashes", 2, "Core Redis", "2.2", 202, "hashes"),
        ("lists.md", "02-core-redis/lists.md", "Lists", "List operations for queue and sequence use cases.", "Lists", 2, "Core Redis", "2.3", 203, "lists"),
        ("sets.md", "02-core-redis/sets.md", "Sets", "Uniqueness and set algebra operations in Redis.", "Sets", 2, "Core Redis", "2.4", 204, "sets"),
        ("sorted-sets.md", "02-core-redis/sorted-sets.md", "Sorted Sets", "Ordered score-based collections for ranks and schedules.", "Sorted Sets", 2, "Core Redis", "2.5", 205, "sorted-sets"),
        ("bitmaps.md", "02-core-redis/bitmaps.md", "Bitmaps", "Bit-level operations for dense boolean tracking.", "Bitmaps", 2, "Core Redis", "2.6", 206, "bitmaps"),
        ("hyperloglog.md", "02-core-redis/hyperloglog.md", "HyperLogLog", "Probabilistic cardinality estimation patterns.", "HyperLogLog", 2, "Core Redis", "2.7", 207, "hyperloglog"),
        ("persistence.md", "03-redis-internals/persistence.md", "Persistence", "RDB, AOF, and hybrid durability internals.", "Persistence", 3, "Redis Internals", "3.3", 303, "persistence"),
        ("replication.md", "03-redis-internals/replication.md", "Replication", "Primary-replica replication, lag, and failover internals.", "Replication", 3, "Redis Internals", "3.4", 304, "replication"),
        ("sentinel.md", "03-redis-internals/sentinel.md", "Sentinel", "High-availability orchestration and automated failover.", "Sentinel", 3, "Redis Internals", "3.5", 305, "sentinel"),
        ("cluster.md", "03-redis-internals/cluster.md", "Cluster", "Hash slots, redirection, scaling, and shard topology.", "Cluster", 3, "Redis Internals", "3.6", 306, "cluster"),
        ("distributed-lock.md", "04-distributed-systems/distributed-lock.md", "Distributed Lock", "Lock correctness, token ownership, and failure boundaries.", "Dist Lock", 4, "Distributed Systems", "4.1", 401, "distributed-lock"),
        ("transactions.md", "04-distributed-systems/transactions.md", "Transactions", "MULTI/EXEC and optimistic coordination semantics.", "Transactions", 4, "Distributed Systems", "4.2", 402, "transactions"),
        ("pub-sub.md", "04-distributed-systems/pub-sub.md", "Pub/Sub", "Fan-out messaging semantics and delivery caveats.", "Pub/Sub", 4, "Distributed Systems", "4.3", 403, "pub-sub"),
        ("streams.md", "04-distributed-systems/streams.md", "Streams", "Consumer groups, pending entries, and delivery patterns.", "Streams", 4, "Distributed Systems", "4.4", 404, "streams"),
        ("lua-scripts.md", "04-distributed-systems/lua-scripts.md", "Lua Scripts", "Atomic server-side scripts and key-slot safety.", "Lua", 4, "Distributed Systems", "4.5", 405, "lua-scripts"),
        ("caching-patterns.md", "05-production-patterns/caching-patterns.md", "Caching Patterns", "Cache-aside, write-through, and write-behind patterns.", "Caching", 5, "Production Patterns", "5.1", 501, "caching-patterns"),
        ("session-store.md", "05-production-patterns/session-store.md", "Session Store", "Session modeling, TTL policy, and failover behavior.", "Session", 5, "Production Patterns", "5.6", 506, "session-store"),
        ("rate-limiter.md", "05-production-patterns/rate-limiter.md", "Rate Limiter", "Rate limiting algorithms with Redis data structures.", "Rate Limit", 5, "Production Patterns", "5.7", 507, "rate-limiter"),
        ("eviction-policies.md", "06-performance-operations/eviction-policies.md", "Eviction Policies", "Maxmemory policies, LRU/LFU behavior, and tradeoffs.", "Eviction", 6, "Performance & Operations", "6.1", 601, "eviction-policies"),
    ]

    patchers = {
        "architecture.md": patch_architecture,
        "data-structures.md": patch_data_structures,
        "strings.md": patch_strings,
        "caching-patterns.md": patch_caching_patterns,
        "lua-scripts.md": patch_lua_scripts,
        "pub-sub.md": patch_pub_sub,
    }

    for old, new, *rest in moves:
        title, desc, short, mod, mod_title, ref, weight, alias = rest
        move_page(
            old,
            new,
            title=title,
            desc=desc,
            short=short,
            mod=mod,
            mod_title=mod_title,
            ref=ref,
            weight=weight,
            alias=alias,
            patch=patchers.get(old),
        )

    common_commands = fix_links(read_old("common-redis-commands.md"))
    common_commands = re.sub(r"\n## Related Topics[\s\S]*$", "", common_commands).strip()

    # New internals pages
    w(
        "03-redis-internals/memory-management.md",
        patch_see_also(
            f"""## Quick Revision

- Redis memory behavior is shaped by object encoding, allocator fragmentation, and key cardinality.
- Observe `used_memory`, `used_memory_rss`, and `mem_fragmentation_ratio` together.
- Plan remediation by separating object growth from allocator overhead.

## Core Concepts

| Concept | Why it matters |
| :--- | :--- |
| `robj` + encoding | Determines memory footprint and command complexity |
| `used_memory` | Redis allocator bytes |
| `used_memory_rss` | OS resident memory |
| Fragmentation ratio | Helps identify reclaim vs workload growth |
| Active defrag | Reduces fragmentation at CPU cost |

## Internal Working

```mermaid
flowchart TB
  cmd[Command writes key] --> obj[robj allocation]
  obj --> enc[Encoding chosen by size/type]
  enc --> jem[jemalloc arenas]
  jem --> used[used_memory]
  jem --> rss[used_memory_rss]
```

```mermaid
flowchart LR
  small[Small hash/list/set] --> packed[listpack/intset]
  packed --> grow[Element growth threshold crossed]
  grow --> expanded[Hashtable/quicklist/skiplist]
```

## Architecture

Memory internals drive cluster sizing and eviction strategy; treat this page as canonical for encoding and allocator topics.

## Design Tradeoffs

| Decision | Tradeoff |
| :--- | :--- |
| Smaller values | Better cache density, extra app serialization cost |
| Active defrag on | Lower RSS drift, extra CPU |
| Aggressive TTL | Lower memory pressure, potential hit-rate drop |

## Production Patterns

- Track top key prefixes by memory and cardinality.
- Cap value sizes for hot keys used by latency-sensitive paths.

## Scalability

As key count grows, metadata overhead can dominate value bytes; capacity plans must include overhead factors.

## Reliability

Fork-based persistence can amplify memory pressure via copy-on-write; reserve memory headroom before snapshots.

## Observability

- `INFO memory`
- `MEMORY STATS`
- `MEMORY USAGE <key>`

## Troubleshooting

If ratio rises while key count is stable, evaluate fragmentation first before rewriting data model.

## Common Mistakes

- Reading `mem_fragmentation_ratio` in isolation.
- Ignoring key overhead when planning memory budgets.

## Interview Questions

- Why can `used_memory_rss` grow while `used_memory` stays flat?
- When is active defrag appropriate?

## Architect Notes

Memory decisions should be codified in ADRs because they directly impact cost, latency, and failover safety.
""",
            "03-redis-internals/memory-management",
        ),
        title="Memory Management",
        desc="Redis memory model, object encodings, allocator behavior, and fragmentation diagnostics.",
        short="Memory Mgmt",
        mod=3,
        mod_title="Redis Internals",
        ref="3.1",
        weight=301,
    )

    w(
        "03-redis-internals/redis-protocol.md",
        patch_see_also(
            f"""## Quick Revision

- Redis clients speak RESP over TCP/Unix sockets.
- Pipelining reduces round trips; execution still remains single-threaded.
- Cluster redirects (`MOVED`/`ASK`) are protocol-level client responsibilities.

## Core Concepts

| Item | Purpose |
| :--- | :--- |
| RESP2/RESP3 | Request/response serialization |
| Pipeline | Batch commands in one network RTT window |
| MOVED | Permanent slot redirect |
| ASK | Temporary redirect during slot migration |

## Internal Working

```mermaid
sequenceDiagram
  participant C as Client
  participant R as Redis
  C->>R: *2\\r\\n$3\\r\\nGET\\r\\n$3\\r\\nkey\\r\\n
  R-->>C: $5\\r\\nvalue\\r\\n
```

```mermaid
sequenceDiagram
  participant C as Client
  participant R as Redis
  C->>R: Pipeline N commands
  R-->>C: N ordered replies
```

## Architecture

Protocol behavior defines client library requirements for pooling, retries, and redirect handling in Cluster deployments.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Deep pipelines | Higher throughput, harder per-command timeout handling |
| Strict timeouts | Faster failover, more retry noise |
| TLS everywhere | Better transport security, extra latency overhead |

## Production Patterns

- Separate pooled command connections from dedicated pub/sub connections.
- Tune pipeline size by p99 latency budget instead of max throughput only.

## Scalability

Protocol efficiency is often the first tuning lever before horizontal shard expansion.

## Reliability

Client retry policy must be idempotent-aware to avoid duplicated writes.

## Observability

- Connection counts, command rates, timeout rates.
- Redirect rate (`MOVED`/`ASK`) during reshard windows.

## Troubleshooting

Frequent redirect storms usually indicate slot migration drift or stale client topology caches.

## Common Mistakes

- Treating pipelining as parallel command execution.
- Sharing one socket for pub/sub and normal command workloads.

## Interview Questions

- How do MOVED and ASK differ in recovery behavior?
- Why can pipelining improve throughput without parallel command execution?

## Architect Notes

Client protocol behavior is part of system architecture, not an implementation detail.
""",
            "03-redis-internals/redis-protocol",
        ),
        title="Redis Protocol",
        desc="RESP behavior, pipelining, connection flow, and redirect handling in Redis clients.",
        short="Protocol",
        mod=3,
        mod_title="Redis Internals",
        ref="3.2",
        weight=302,
    )

    # New performance and patterns pages
    w(
        "06-performance-operations/performance-tuning.md",
        patch_see_also(
            """## Quick Revision

- Start with command shape and network round trips before hardware changes.
- Pipeline where safe; avoid O(N) commands on hot paths.
- Validate tuning against p99 latency and error budget.

## Core Concepts

| Lever | Outcome |
| :--- | :--- |
| Pipelining | Fewer RTTs, better throughput |
| Command complexity | Protect event loop from long operations |
| Value sizing | Reduces serialization and network time |
| Connection pooling | Stabilizes client concurrency |

## Internal Working

```mermaid
flowchart TB
  app[App traffic] --> net[Network RTT]
  net --> cmd[Command execution]
  cmd --> loop[Single command thread]
  loop --> reply[Reply serialization]
```

## Architecture

Performance depends on both client behavior (batching, retries, pools) and server-side command profile.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Larger pipeline | Higher throughput, longer tail latency under bursts |
| Fewer large keys | Less key metadata, larger transfer cost |
| More shards | Better parallelism, higher operational complexity |

## Production Patterns

- Batch reads via MGET/pipeline.
- Prefer UNLINK over DEL for large-value cleanup tasks.
- Cap command cardinality in API-layer guards.

## Scalability

If CPU is saturated on one primary after command tuning, evaluate Cluster expansion.

## Reliability

Tune under failover scenarios; retries can inflate load and mask regressions.

## Observability

- p95/p99 latency by command family
- Slowlog trends
- Network throughput and connection churn

## Troubleshooting

Latency with low ops/sec often indicates blocking commands, network jitter, or persistence side effects.

## Common Mistakes

- Benchmarking only average latency.
- Enabling deep pipelines without timeout and backpressure strategy.

## Interview Questions

- When does MGET beat pipelined GET?
- Which command patterns silently become event-loop blockers?

## Architect Notes

Treat Redis tuning as a full request-path problem (client + network + command + topology).
""",
            "06-performance-operations/performance-tuning",
        ),
        title="Performance Tuning",
        desc="Latency and throughput tuning across command patterns, pipelining, and topology choices.",
        short="Perf Tuning",
        mod=6,
        mod_title="Performance & Operations",
        ref="6.2",
        weight=602,
    )

    w(
        "06-performance-operations/monitoring.md",
        patch_see_also(
            f"""## Quick Revision

- Build dashboards from INFO, slowlog, and latency diagnostics.
- Alert on replication lag, memory pressure, and connection saturation.
- Keep runbooks linked to troubleshooting decision trees.

## Core Concepts

| Signal | Why monitor |
| :--- | :--- |
| Latency by command | Detect event-loop blocking behavior |
| Replication lag | Detect durability and read-freshness risk |
| Memory trend | Detect leak-like growth and fragmentation |
| Reconnect spikes | Detect failover or network instability |

## Internal Working

```mermaid
flowchart LR
  info[INFO metrics] --> dash[Dashboards]
  slow[SLOWLOG samples] --> dash
  latency[LATENCY DOCTOR] --> runbook[Runbook actions]
```

## Architecture

Monitoring should map directly to SLOs and incident response ownership.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Dense metric collection | Better diagnostics, more telemetry cost |
| Frequent polling | Better freshness, more monitoring overhead |

## Production Patterns

- Keep baseline dashboards per deployment topology (standalone, Sentinel, Cluster).
- Include command-family split for latency and volume.

## Scalability

Monitor per-node and per-shard imbalance to detect hidden hot spots.

## Reliability

Alert quality matters more than alert quantity; tie thresholds to user impact.

## Observability

### Folded Command Reference

{common_commands}

## Troubleshooting

For runbook trees, see [Troubleshooting]({BASE}/06-performance-operations/troubleshooting/).

## Common Mistakes

- Running production diagnostics with disruptive commands.
- Missing per-shard visibility in Cluster environments.

## Interview Questions

- What does LATENCY DOCTOR add beyond SLOWLOG?
- Which metrics detect failover instability early?

## Architect Notes

Observability architecture should expose both control-plane and data-plane failures.
""",
            "06-performance-operations/monitoring",
        ),
        title="Monitoring",
        desc="Operational telemetry and command diagnostics for Redis production systems.",
        short="Monitoring",
        mod=6,
        mod_title="Performance & Operations",
        ref="6.3",
        weight=603,
        alias_paths=(f"{BASE}/common-redis-commands/",),
    )

    w(
        "06-performance-operations/troubleshooting.md",
        patch_see_also(
            """## Quick Revision

- Triage starts with symptom category: memory, latency, replication, or cluster routing.
- Confirm whether impact is node-local, shard-local, or client-wide.
- Apply remediation with rollback-safe operational steps.

## Core Concepts

| Symptom | First check |
| :--- | :--- |
| High memory | used vs rss vs key growth |
| Replication lag | backlog, link health, write spikes |
| High latency | slow commands, persistence activity, network |
| Slot imbalance | shard key patterns and migration state |

## Internal Working

```mermaid
flowchart TD
  A[Memory alert] --> B{Key count rising?}
  B -->|Yes| C[Workload growth]
  B -->|No| D[Fragmentation or COW]
  D --> E[Inspect persistence and allocator]
```

```mermaid
flowchart TD
  R[Replication lag] --> R1{Backlog sufficient?}
  R1 -->|No| R2[Increase backlog / full resync]
  R1 -->|Yes| R3[Check network and disk throughput]
```

```mermaid
flowchart TD
  H[Latency spike] --> H1{Slow commands?}
  H1 -->|Yes| H2[Optimize command shape]
  H1 -->|No| H3[Check network/persistence/failover]
```

## Architecture

Runbooks should be topology-specific and pre-linked from alerts.

## Design Tradeoffs

| Action | Risk |
| :--- | :--- |
| Immediate failover | Lower outage duration, potential stale state |
| Aggressive key eviction | Faster recovery, hit-ratio regression |
| Fast resharding | Better balance, temporary redirect churn |

## Production Patterns

- Keep diagnostic command allowlist for on-call.
- Store post-incident timelines with command and topology context.

## Scalability

Repeated hot-key incidents usually indicate key design debt, not transient ops noise.

## Reliability

Always verify replica freshness and client retry behavior before closing incidents.

## Observability

Pair this page with [Monitoring](/redis-cheatsheet/06-performance-operations/monitoring/) dashboards.

## Troubleshooting

Apply decision trees by symptom, then drill into related canonical pages.

## Common Mistakes

- Using `KEYS *` during incidents.
- Treating client timeouts as always server CPU problems.

## Interview Questions

- How do you separate hot-key from big-key incidents?
- What is your first response to MOVED storms?

## Architect Notes

A mature Redis platform has codified incident pathways for each failure class.
""",
            "06-performance-operations/troubleshooting",
        ),
        title="Troubleshooting",
        desc="Decision trees and runbooks for memory, latency, replication, and cluster incidents.",
        short="Troubleshoot",
        mod=6,
        mod_title="Performance & Operations",
        ref="6.5",
        weight=605,
    )

    w(
        "06-performance-operations/capacity-planning.md",
        patch_see_also(
            """## Quick Revision

- Capacity planning combines memory math, replication factor, and growth assumptions.
- Include overhead for key metadata, encoding transitions, and persistence headroom.
- Validate both cost and failover safety in architecture reviews.

## Core Concepts

| Dimension | Baseline input |
| :--- | :--- |
| Key count | Current + projected growth |
| Value size | p50/p95 payload distribution |
| Replication factor | Primary + replicas |
| Persistence overhead | Fork/COW and rewrite headroom |

## Internal Working

```mermaid
flowchart TB
  keys[Key count] --> mem[Dataset bytes]
  vals[Value size] --> mem
  over[Object overhead] --> mem
  mem --> repl[Replication multiplier]
  repl --> total[Total cluster memory budget]
```

## Architecture

Capacity strategy should specify scale-up thresholds and scale-out triggers.

## Design Tradeoffs

| Strategy | Tradeoff |
| :--- | :--- |
| Larger nodes | Simpler ops, bigger blast radius |
| More shards | Better parallelism, more operational complexity |

## Production Patterns

- Budget separate pools for cache, sessions, and coordination workloads.
- Re-run capacity forecast before major traffic launches.

## Scalability

Plan for hotspot risk even when total capacity looks adequate.

## Reliability

Reserve memory headroom for failover and persistence operations.

## Observability

Track growth per key prefix and per shard monthly.

## Troubleshooting

Unexpected OOM with stable traffic usually points to growth assumptions drift or missing overhead.

## Common Mistakes

- Planning only by total GB without key cardinality.
- Ignoring replication factor in cost calculations.

## Interview Questions

- How do you estimate memory for N keys with overhead?
- When do you move from one large node to Cluster?

## Architect Notes

Capacity planning is an architectural artifact, not an afterthought spreadsheet.
""",
            "06-performance-operations/capacity-planning",
        ),
        title="Capacity Planning",
        desc="Memory and topology sizing methodology for scalable and reliable Redis deployments.",
        short="Capacity",
        mod=6,
        mod_title="Performance & Operations",
        ref="6.4",
        weight=604,
    )

    w(
        "05-production-patterns/cache-invalidation.md",
        patch_see_also(
            """## Quick Revision

- Correctness requires explicit cache invalidation on write paths.
- Choose between delete-on-write, update-on-write, and event-based invalidation.
- Tie strategy to consistency and latency requirements.

## Core Concepts

| Strategy | Use when |
| :--- | :--- |
| Delete-on-write | Simple and safe default |
| Update-on-write | Predictable read latency, more write complexity |
| Pub/Sub invalidation | Multi-node local caches require fan-out |

## Internal Working

```mermaid
sequenceDiagram
  participant API as App
  participant DB as Primary DB
  participant R as Redis
  API->>DB: Write record
  DB-->>API: Commit OK
  API->>R: DEL cache:key
```

## Architecture

Define ownership: service updating source-of-truth data must also own invalidation behavior.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Delete on write | Possible brief miss bursts |
| Update on write | More serialization logic |
| Event invalidation | Extra transport dependency |

## Production Patterns

- Version keys when atomic key swaps are easier than inplace updates.
- Use idempotent invalidation events.

## Scalability

Fan-out invalidation channels need backpressure controls in large clusters.

## Reliability

Failed invalidation should be retried or reconciled by scheduled repair jobs.

## Observability

Track stale-read incidents and invalidation latency distributions.

## Troubleshooting

If stale reads persist, verify write-path ordering and consumer delivery guarantees.

## Common Mistakes

- Updating DB without cache mutation in the same flow.
- Ignoring local in-process caches while invalidating Redis only.

## Interview Questions

- Compare delete-on-write and update-on-write failure modes.
- How do you design invalidation for multi-layer caches?

## Architect Notes

Invalidation is a correctness concern and should be reviewed like transaction design.
""",
            "05-production-patterns/cache-invalidation",
        ),
        title="Cache Invalidation",
        desc="Consistency-safe invalidation strategies for Redis-backed caching systems.",
        short="Invalidation",
        mod=5,
        mod_title="Production Patterns",
        ref="5.2",
        weight=502,
    )

    w(
        "05-production-patterns/cache-breakdown.md",
        patch_see_also(
            """## Quick Revision

- Cache breakdown occurs when a single hot key expires and thundering-herd traffic hits origin.
- Use request coalescing, lock/singleflight, and stale-while-revalidate patterns.
- Keep rebuild path bounded and observable.

## Core Concepts

| Pattern | Goal |
| :--- | :--- |
| Singleflight lock | One rebuilder, many waiters |
| Stale-while-revalidate | Serve stale safely while refresh runs |
| Early refresh threshold | Refresh before hard expiry |

## Internal Working

```mermaid
sequenceDiagram
  participant C1 as Client1
  participant C2 as Client2
  participant R as Redis
  participant DB as DB
  C1->>R: GET hot:key (miss)
  C1->>R: SET lock:key NX EX 10
  C2->>R: GET hot:key (miss)
  C2-->>C2: Wait/retry
  C1->>DB: Load source
  C1->>R: SET hot:key value EX 300
```

## Architecture

Hot-key protection should be part of API design for high-fanout endpoints.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Locking | Extra latency for waiters |
| Serve stale | Slight staleness vs origin protection |
| No guard | Simpler code, origin overload risk |

## Production Patterns

- Apply hot-key dashboards per endpoint.
- Keep lock TTL short and release-safe.

## Scalability

Breakdown risk increases with fanout growth even when total QPS is stable.

## Reliability

Ensure rebuild path degrades gracefully if origin is slow.

## Observability

Track lock contention and miss burst size.

## Troubleshooting

If DB spikes on key expiry, validate singleflight effectiveness and retry behavior.

## Common Mistakes

- Locking without timeout.
- Refresh logic that can deadlock under failures.

## Interview Questions

- How does cache breakdown differ from cache avalanche?
- Which mitigation do you pick for strict p99 APIs?

## Architect Notes

Breakdown prevention is a system-protection mechanism, not only a cache optimization.
""",
            "05-production-patterns/cache-breakdown",
        ),
        title="Cache Breakdown",
        desc="Hot-key expiry mitigation patterns to prevent thundering-herd database overload.",
        short="Breakdown",
        mod=5,
        mod_title="Production Patterns",
        ref="5.3",
        weight=503,
    )

    w(
        "05-production-patterns/cache-avalanche.md",
        patch_see_also(
            """## Quick Revision

- Cache avalanche is synchronized expiry across many keys causing origin surge.
- Stagger TTLs, warm critical keys, and protect origin with bulkhead controls.
- Validate mitigation with expiry-distribution telemetry.

## Core Concepts

| Trigger | Mitigation |
| :--- | :--- |
| Same TTL cohort | Add TTL jitter |
| Cold restart | Warm high-value keys first |
| Broad invalidation | Batch and phase eviction |

## Internal Working

```mermaid
flowchart TD
  TTL[Many keys share same TTL] --> Exp[Mass expiry window]
  Exp --> Miss[Cache miss storm]
  Miss --> DB[DB overload risk]
  DB --> Mit[Apply jitter + warmup + rate limit]
```

## Architecture

Design key TTL strategy as part of release planning for large batch writes.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Larger TTL jitter | Better smoothing, less predictability |
| Aggressive warmup | Better hit rate, startup cost |

## Production Patterns

- Jitter TTL by cohort and business criticality.
- Warm top traffic keys during deploy/startup windows.

## Scalability

Avalanche frequency grows with key cohort size and synchronized deployments.

## Reliability

Use origin rate limiting and circuit breakers to survive expiry storms.

## Observability

Monitor key expiry distribution histograms and miss-rate spikes.

## Troubleshooting

If misses spike in narrow windows, inspect TTL batching and deployment timing.

## Common Mistakes

- Uniform TTL for all cache keys.
- Evicting wide keyspaces during peak hours.

## Interview Questions

- How is cache avalanche different from penetration and breakdown?
- What jitter range do you pick and why?

## Architect Notes

Avalanche control is a workload-shaping discipline that spans app and platform teams.
""",
            "05-production-patterns/cache-avalanche",
        ),
        title="Cache Avalanche",
        desc="Synchronized expiry failure mode and mitigation strategies for Redis caching.",
        short="Avalanche",
        mod=5,
        mod_title="Production Patterns",
        ref="5.4",
        weight=504,
    )

    w(
        "05-production-patterns/cache-penetration.md",
        patch_see_also(
            """## Quick Revision

- Cache penetration occurs when repeated misses for absent keys flood the origin.
- Mitigate with negative caching, Bloom filters, and strict key validation.
- Tune miss TTL separately from hit TTL.

## Core Concepts

| Defense | Purpose |
| :--- | :--- |
| Negative caching | Short-term shield for absent IDs |
| Bloom filter | Fast probable-existence check |
| Input validation | Drop invalid keys early |

## Internal Working

```mermaid
flowchart LR
  req[Request missing key] --> cache[Redis miss]
  cache --> bloom{Bloom says exists?}
  bloom -->|No| deny[Return not found quickly]
  bloom -->|Yes| db[Query origin DB]
  db --> fill[Cache null/short TTL]
```

## Architecture

Penetration defense belongs in API gateway and service logic, not cache layer alone.

## Design Tradeoffs

| Choice | Tradeoff |
| :--- | :--- |
| Negative cache | Possible stale "not found" window |
| Bloom filter | False positives, memory overhead |

## Production Patterns

- Separate TTL policy for negative entries.
- Protect high-risk endpoints with request throttling.

## Scalability

Bot traffic can amplify penetration risk even at moderate user volume.

## Reliability

Fallback paths must avoid bypassing all cache defenses during incidents.

## Observability

Track miss-by-prefix, negative-cache hit ratio, and origin QPS under miss storms.

## Troubleshooting

Persistent high miss with low hit ratio usually indicates penetration or poor key design.

## Common Mistakes

- Caching not-found forever.
- Assuming Bloom filters remove all miss traffic.

## Interview Questions

- When do you prefer negative caching over Bloom filters?
- How do you tune TTL for non-existent IDs?

## Architect Notes

Penetration controls are critical for abuse resilience and origin protection budgets.
""",
            "05-production-patterns/cache-penetration",
        ),
        title="Cache Penetration",
        desc="Miss-storm prevention strategies for absent-key traffic and bot abuse patterns.",
        short="Penetration",
        mod=5,
        mod_title="Production Patterns",
        ref="5.5",
        weight=505,
    )

    # Comparisons
    w(
        "07-comparisons/redis-vs-memcached.md",
        patch_see_also(
            """## Quick Revision

- Redis offers rich data types, persistence options, and HA topologies.
- Memcached focuses on simple key-value caching with minimal overhead.
- Choose based on feature depth vs operational simplicity.

## Design Tradeoffs

| Dimension | Redis | Memcached |
| :--- | :--- | :--- |
| Data model | Rich structures | String values |
| Persistence | Optional RDB/AOF | None |
| HA | Sentinel/Cluster | Client-side sharding only |
| Scripting | Lua/Functions | No equivalent |

## Architecture

Redis fits mixed workloads (cache + coordination). Memcached fits minimal-latency pure cache use cases.

## Production Patterns

See also [Database Handbook — Redis vs Memcached](/database-handbook/redis-vs-memcached/).

## Interview Questions

- When is Memcached still preferable to Redis?
- Which Redis features justify higher operational overhead?

## Architect Notes

This decision is typically an ADR balancing cache requirements against platform complexity.
""",
            "07-comparisons/redis-vs-memcached",
        ),
        title="Redis vs Memcached",
        desc="Architectural comparison of Redis and Memcached for cache and coordination workloads.",
        short="vs Memcached",
        mod=7,
        mod_title="Comparisons",
        ref="7.1",
        weight=701,
    )

    w(
        "07-comparisons/redis-vs-kafka.md",
        patch_see_also(
            """## Quick Revision

- Redis Streams is strong for lightweight stream processing and short retention.
- Kafka is built for durable, high-retention event logs and replay.
- Select by durability, retention, ecosystem, and scale requirements.

## Design Tradeoffs

| Dimension | Redis Streams | Kafka |
| :--- | :--- | :--- |
| Retention model | In-memory/limited persistence | Durable segmented log |
| Consumer model | Consumer groups, simpler ops | Partitioned replay-centric model |
| Operational overhead | Lower initial overhead | Higher platform complexity |

## Interview Questions

- When is Redis Streams enough vs Kafka mandatory?
- What replay and retention guarantees drive the decision?

## Architect Notes

Do not position Redis Streams as a direct Kafka replacement for long-term event sourcing.
""",
            "07-comparisons/redis-vs-kafka",
        ),
        title="Redis vs Kafka",
        desc="Tradeoffs between Redis Streams and Kafka for eventing and stream-processing workloads.",
        short="vs Kafka",
        mod=7,
        mod_title="Comparisons",
        ref="7.2",
        weight=702,
    )

    w(
        "07-comparisons/redis-vs-rabbitmq.md",
        patch_see_also(
            """## Quick Revision

- Redis Lists/Streams can power queues with lower operational overhead.
- RabbitMQ offers richer broker semantics (routing, dead-letter, delivery patterns).
- Pick based on queue semantics and failure-handling requirements.

## Design Tradeoffs

| Dimension | Redis | RabbitMQ |
| :--- | :--- | :--- |
| Routing | Basic channel/key model | Exchanges, bindings, routing keys |
| Delivery semantics | App-managed discipline | Built-in broker controls |
| Delay/retry patterns | Manual pattern design | Native queue capabilities |

## Interview Questions

- When do routing and DLQ needs force RabbitMQ adoption?
- Which queue patterns are safer in Redis Streams vs Lists?

## Architect Notes

Messaging broker selection should encode delivery guarantees explicitly in architecture docs.
""",
            "07-comparisons/redis-vs-rabbitmq",
        ),
        title="Redis vs RabbitMQ",
        desc="Queue and messaging tradeoffs between Redis-based patterns and RabbitMQ broker features.",
        short="vs RabbitMQ",
        mod=7,
        mod_title="Comparisons",
        ref="7.3",
        weight=703,
    )

    # Learning paths
    w(
        "09-learning-paths/redis-senior-engineer-path.md",
        patch_see_also(
            f"""# Redis Senior Engineer Path

**Goal:** Build strong operational and data-structure depth for production Redis services.

1. [Architecture]({BASE}/01-fundamentals/architecture/) -> [Data Structures]({BASE}/01-fundamentals/data-structures/)
2. [Core Redis]({BASE}/02-core-redis/)
3. [Memory Management]({BASE}/03-redis-internals/memory-management/) + [Persistence]({BASE}/03-redis-internals/persistence/)
4. [Caching Patterns]({BASE}/05-production-patterns/caching-patterns/) + [Rate Limiter]({BASE}/05-production-patterns/rate-limiter/)
5. [Performance Tuning]({BASE}/06-performance-operations/performance-tuning/) + [Monitoring]({BASE}/06-performance-operations/monitoring/)
""",
            "09-learning-paths/redis-senior-engineer-path",
        ),
        title="Senior Engineer Path",
        desc="Structured Redis path for senior engineers across internals, patterns, and operations.",
        short="Senior Path",
        mod=9,
        mod_title="Learning Paths",
        ref="9.1",
        weight=901,
    )

    w(
        "09-learning-paths/redis-lead-path.md",
        patch_see_also(
            f"""# Redis Lead Path

**Goal:** Lead architecture and incident readiness for Redis-backed platforms.

1. [Replication]({BASE}/03-redis-internals/replication/) + [Sentinel]({BASE}/03-redis-internals/sentinel/) + [Cluster]({BASE}/03-redis-internals/cluster/)
2. [Cache Invalidation]({BASE}/05-production-patterns/cache-invalidation/) and failure-mode pages
3. [Capacity Planning]({BASE}/06-performance-operations/capacity-planning/) + [Troubleshooting]({BASE}/06-performance-operations/troubleshooting/)
4. [Architect Questions]({BASE}/08-interview-guide/architect-questions/) for panel preparation
""",
            "09-learning-paths/redis-lead-path",
        ),
        title="Lead Path",
        desc="Leadership path for Redis reliability, scaling decisions, and incident governance.",
        short="Lead Path",
        mod=9,
        mod_title="Learning Paths",
        ref="9.2",
        weight=902,
    )

    w(
        "09-learning-paths/redis-architect-path.md",
        patch_see_also(
            f"""# Redis Architect Path

**Goal:** Make ADR-grade platform choices for Redis in distributed systems.

1. [Redis Protocol]({BASE}/03-redis-internals/redis-protocol/) + [Memory Management]({BASE}/03-redis-internals/memory-management/)
2. [Cluster]({BASE}/03-redis-internals/cluster/) and [Distributed Lock]({BASE}/04-distributed-systems/distributed-lock/)
3. [Comparisons]({BASE}/07-comparisons/) for broker/cache tradeoffs
4. [Database Handbook — Redis](/database-handbook/redis/) for cross-database ADR context
""",
            "09-learning-paths/redis-architect-path",
        ),
        title="Architect Path",
        desc="ADR-oriented Redis learning path for architecture and platform design decisions.",
        short="Architect Path",
        mod=9,
        mod_title="Learning Paths",
        ref="9.3",
        weight=903,
    )

    w(
        "09-learning-paths/redis-interview-revision-path.md",
        patch_see_also(
            f"""# Redis Interview Revision Path

**Goal:** High-signal 48-hour revision before senior and architect interviews.

| Block | Focus |
| :--- | :--- |
| 1 | [Architecture]({BASE}/01-fundamentals/architecture/) + [Data Structures]({BASE}/01-fundamentals/data-structures/) |
| 2 | [Persistence]({BASE}/03-redis-internals/persistence/) + [Replication]({BASE}/03-redis-internals/replication/) + [Cluster]({BASE}/03-redis-internals/cluster/) |
| 3 | [Distributed Lock]({BASE}/04-distributed-systems/distributed-lock/) + [Streams]({BASE}/04-distributed-systems/streams/) |
| 4 | [Cache failure pages]({BASE}/05-production-patterns/cache-breakdown/) + [Troubleshooting]({BASE}/06-performance-operations/troubleshooting/) |
| 5 | [Top 150 Questions]({BASE}/08-interview-guide/top-150-interview-questions/) |
""",
            "09-learning-paths/redis-interview-revision-path",
        ),
        title="Interview Revision Path",
        desc="48-hour Redis interview revision map with architecture and operations focus.",
        short="Interview Path",
        mod=9,
        mod_title="Learning Paths",
        ref="9.4",
        weight=904,
    )

    from redis_questions_data import QUESTIONS

    assert len(QUESTIONS) == 150, len(QUESTIONS)

    def deep_dive_link(doc: str) -> str:
        slug = doc.replace(".md", "")
        label = slug.split("/")[-1].replace("-", " ").title()
        return f"[{label}]({BASE}/{slug}/)"

    q_rows = "\n".join(
        f"| {n} | {q} | {d} | {l} | {t} | {deep_dive_link(doc)} |"
        for n, q, d, l, t, doc in QUESTIONS
    )

    w(
        "08-interview-guide/top-150-interview-questions.md",
        patch_see_also(
            f"""Curated questions for **6+ year** engineers, leads, and architects. Question index with **inline answers** below (also on canonical topic pages via **Deep Dive** links).

**Distribution:** Architecture 40 · Troubleshooting 30 · Performance 25 · Reliability 20 · Scalability 15 · Patterns 20

| # | Question | Difficulty | Level | Topic | Deep Dive |
|---|----------|------------|--------|-------|-----------|
{q_rows}
""",
            "08-interview-guide/top-150-interview-questions",
        ),
        title="Top 150 Redis Interview Questions",
        desc="150 production-oriented Redis interview questions mapped to canonical handbook pages.",
        short="Top 150",
        mod=8,
        mod_title="Interview Guide",
        ref="8.1",
        weight=801,
        interview=True,
        alias_paths=(f"{BASE}/interview-questions/",),
    )

    architect_qs = [q for _, q, _, level, _, _ in QUESTIONS if level == "Architect"][:40]
    trouble_qs = [QUESTIONS[i][1] for i in range(40, 70)]
    perf_qs = [QUESTIONS[i][1] for i in range(70, 95)]

    w(
        "08-interview-guide/architect-questions.md",
        patch_see_also(
            f"""Architect-focused subset from the [Top 150]({BASE}/08-interview-guide/top-150-interview-questions/). **Full answers** below (regenerated by `phase_c_redis_handbook.py`).

# Architect Questions

""" + "\n".join(f"{i}. {q}" for i, q in enumerate(architect_qs, 1)),
            "08-interview-guide/architect-questions",
        ),
        title="Architect Questions",
        desc="Architect-focused subset from the Redis Top 150 question bank.",
        short="Architect Q",
        mod=8,
        mod_title="Interview Guide",
        ref="8.2",
        weight=802,
        interview=True,
    )

    w(
        "08-interview-guide/troubleshooting-questions.md",
        patch_see_also(
            """Troubleshooting-focused subset — **inline answers** appended by `phase_c_redis_handbook.py`.

# Troubleshooting Questions

"""
            + "\n".join(f"{i}. {q}" for i, q in enumerate(trouble_qs, 1)),
            "08-interview-guide/troubleshooting-questions",
        ),
        title="Troubleshooting Questions",
        desc="Troubleshooting-focused subset from Redis interview question bank.",
        short="Troubleshoot Q",
        mod=8,
        mod_title="Interview Guide",
        ref="8.3",
        weight=803,
        interview=True,
    )

    w(
        "08-interview-guide/performance-questions.md",
        patch_see_also(
            """Performance-focused subset — **inline answers** appended by `phase_c_redis_handbook.py`.

# Performance Questions

"""
            + "\n".join(f"{i}. {q}" for i, q in enumerate(perf_qs, 1)),
            "08-interview-guide/performance-questions",
        ),
        title="Performance Questions",
        desc="Performance-focused subset from Redis interview question bank.",
        short="Perf Q",
        mod=8,
        mod_title="Interview Guide",
        ref="8.4",
        weight=804,
        interview=True,
    )

    # Handbook index rewrite
    w(
        "_index.md",
        f"""# Redis Handbook

Production and interview knowledge base for **Senior Engineers**, **Technical Leads**, and **Architects**.

## Learning Paths

| Track | Start here | Goal |
| :--- | :--- | :--- |
| Senior Engineer | [Senior Engineer Path]({BASE}/09-learning-paths/redis-senior-engineer-path/) | Core types, internals, and production readiness |
| Technical Lead | [Lead Path]({BASE}/09-learning-paths/redis-lead-path/) | Reliability, scaling, and incident governance |
| Architect | [Architect Path]({BASE}/09-learning-paths/redis-architect-path/) | ADR-grade design and technology tradeoffs |
| Interview Prep | [Interview Revision Path]({BASE}/09-learning-paths/redis-interview-revision-path/) | High-signal revision + Top 150 |

## Modules

1. **Fundamentals** — architecture and data-structure selection
2. **Core Redis** — commands and type-specific quick references
3. **Redis Internals** — memory, protocol, persistence, replication, Sentinel, Cluster
4. **Distributed Systems** — locks, transactions, pub/sub, streams, Lua
5. **Production Patterns** — caching patterns and cache failure modes
6. **Performance & Operations** — eviction, tuning, monitoring, capacity, troubleshooting
7. **Comparisons** — Redis vs Memcached, Kafka, RabbitMQ
8. **Interview Guide** — Top 150 and focused subsets
9. **Learning Paths** — role-oriented reading tracks

See also: [Database Handbook — Redis](/database-handbook/redis/) · [Redis vs Memcached](/database-handbook/redis-vs-memcached/)
""",
        title="Redis Handbook",
        desc="Redis handbook covering fundamentals, internals, operations, comparisons, and interview preparation.",
        short="Handbook",
        mod=0,
        mod_title="Redis Handbook",
        ref="0",
        weight=1,
    )

    # YAML output
    modules_yaml = """# Redis Handbook — module index.
modules:
  - id: 1
    focus: "Fundamentals"
    topics:
      - 01-fundamentals/architecture
      - 01-fundamentals/data-structures

  - id: 2
    focus: "Core Redis"
    topics:
      - 02-core-redis/strings
      - 02-core-redis/hashes
      - 02-core-redis/lists
      - 02-core-redis/sets
      - 02-core-redis/sorted-sets
      - 02-core-redis/bitmaps
      - 02-core-redis/hyperloglog

  - id: 3
    focus: "Redis Internals"
    topics:
      - 03-redis-internals/memory-management
      - 03-redis-internals/redis-protocol
      - 03-redis-internals/persistence
      - 03-redis-internals/replication
      - 03-redis-internals/sentinel
      - 03-redis-internals/cluster

  - id: 4
    focus: "Distributed Systems"
    topics:
      - 04-distributed-systems/distributed-lock
      - 04-distributed-systems/transactions
      - 04-distributed-systems/pub-sub
      - 04-distributed-systems/streams
      - 04-distributed-systems/lua-scripts

  - id: 5
    focus: "Production Patterns"
    topics:
      - 05-production-patterns/caching-patterns
      - 05-production-patterns/cache-invalidation
      - 05-production-patterns/cache-breakdown
      - 05-production-patterns/cache-avalanche
      - 05-production-patterns/cache-penetration
      - 05-production-patterns/session-store
      - 05-production-patterns/rate-limiter

  - id: 6
    focus: "Performance & Operations"
    topics:
      - 06-performance-operations/eviction-policies
      - 06-performance-operations/performance-tuning
      - 06-performance-operations/monitoring
      - 06-performance-operations/capacity-planning
      - 06-performance-operations/troubleshooting

  - id: 7
    focus: "Comparisons"
    topics:
      - 07-comparisons/redis-vs-memcached
      - 07-comparisons/redis-vs-kafka
      - 07-comparisons/redis-vs-rabbitmq

  - id: 8
    focus: "Interview Guide"
    topics:
      - 08-interview-guide/top-150-interview-questions
      - 08-interview-guide/architect-questions
      - 08-interview-guide/troubleshooting-questions
      - 08-interview-guide/performance-questions

  - id: 9
    focus: "Learning Paths"
    topics:
      - 09-learning-paths/redis-senior-engineer-path
      - 09-learning-paths/redis-lead-path
      - 09-learning-paths/redis-architect-path
      - 09-learning-paths/redis-interview-revision-path
"""

    order_yaml = "# Topic order — derived from redis_cheatsheet_modules.yaml.\ntopics:\n" + "\n".join(
        f"  - {topic}" for topic in TOPICS_ORDER
    )

    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "redis_cheatsheet_modules.yaml").write_text(modules_yaml, encoding="utf-8")
    (DATA / "redis_cheatsheet_order.yaml").write_text(order_yaml + "\n", encoding="utf-8")

    # Remove old flat files
    old_flat = [name for name, _, *_ in moves] + ["common-redis-commands.md", "interview-questions.md"]
    for name in old_flat:
        p = HB / name
        if p.exists():
            p.unlink()

    print("Redis handbook Phase B generated successfully.")
    print(f"Topics: {len(TOPICS_ORDER)} in order yaml")


if __name__ == "__main__":
    main()
