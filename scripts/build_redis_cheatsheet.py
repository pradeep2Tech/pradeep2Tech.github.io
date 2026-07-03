"""Build Redis Cheatsheet pages from data/redis_cheatsheet_modules.yaml.

DEPRECATED for handbook structure: use scripts/generate_redis_handbook_refactor.py instead.
This script regenerates the legacy flat layout and will overwrite Phase B nested content.
"""
from __future__ import annotations

import textwrap
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "redis-cheatsheet"
DATE = "2026-06-30T10:00:00+00:00"
SECTION = "redis-cheatsheet"
SECTION_TITLE = "Redis Cheatsheet"

TOPIC_META: dict[str, tuple[str, str, str]] = {
    "architecture": (
        "Redis Architecture",
        "Architecture",
        "Single-threaded event loop, I/O threads, memory model, and client protocol recap.",
    ),
    "data-structures": (
        "Redis Data Structures Overview",
        "Data Structures",
        "Type encoding, keyspace, TTL, and when to pick each Redis data type.",
    ),
    "strings": (
        "Redis Strings",
        "Strings",
        "GET/SET, counters, bitmap base, and string encoding internals.",
    ),
    "hashes": (
        "Redis Hashes",
        "Hashes",
        "Field-value maps, HSET/HGET, and compact encoding for small objects.",
    ),
    "lists": (
        "Redis Lists",
        "Lists",
        "LPUSH/RPOP, blocking pops, and list-backed queues.",
    ),
    "sets": (
        "Redis Sets",
        "Sets",
        "SADD/SMEMBERS, set algebra, and membership at O(1).",
    ),
    "sorted-sets": (
        "Redis Sorted Sets",
        "Sorted Sets",
        "ZADD/ZRANGE, scores, rank, and leaderboards.",
    ),
    "bitmaps": (
        "Redis Bitmaps",
        "Bitmaps",
        "SETBIT/GETBIT, BITOP, and bitfield commands for compact flags.",
    ),
    "hyperloglog": (
        "Redis HyperLogLog",
        "HyperLogLog",
        "PFADD/PFCOUNT — approximate distinct counts in fixed memory.",
    ),
    "streams": (
        "Redis Streams",
        "Streams",
        "XADD/XREADGROUP, consumer groups, and at-least-once processing.",
    ),
    "pub-sub": (
        "Redis Pub/Sub",
        "Pub/Sub",
        "PUBLISH/SUBSCRIBE, pattern channels, and fire-and-forget messaging.",
    ),
    "transactions": (
        "Redis Transactions",
        "Transactions",
        "MULTI/EXEC, WATCH, optimistic locking, and pipeline vs transaction.",
    ),
    "lua-scripts": (
        "Redis Lua Scripts",
        "Lua Scripts",
        "EVAL/EVALSHA, atomic server-side logic, and script caching.",
    ),
    "persistence": (
        "Redis Persistence",
        "Persistence",
        "RDB snapshots, AOF append-only log, and hybrid durability trade-offs.",
    ),
    "replication": (
        "Redis Replication",
        "Replication",
        "Primary-replica sync, partial resync, and read scaling.",
    ),
    "sentinel": (
        "Redis Sentinel",
        "Sentinel",
        "Automatic failover, quorum, and sentinel-managed topology.",
    ),
    "cluster": (
        "Redis Cluster",
        "Cluster",
        "Hash slots, 16384 partitions, resharding, and cluster-aware clients.",
    ),
    "eviction-policies": (
        "Redis Eviction Policies",
        "Eviction",
        "maxmemory, LRU/LFU/TTL policies, and volatile vs allkeys.",
    ),
    "caching-patterns": (
        "Redis Caching Patterns",
        "Caching Patterns",
        "Cache-aside, write-through, write-behind, and stampede mitigation.",
    ),
    "distributed-lock": (
        "Redis Distributed Lock",
        "Distributed Lock",
        "SET NX PX, Redlock debate, and fencing tokens.",
    ),
    "rate-limiter": (
        "Redis Rate Limiter",
        "Rate Limiter",
        "Fixed window, sliding window, and token bucket with INCR/EXPIRE.",
    ),
    "session-store": (
        "Redis Session Store",
        "Session Store",
        "Hash-based sessions, TTL refresh, and sticky vs shared sessions.",
    ),
    "common-redis-commands": (
        "Common Redis Commands",
        "Commands",
        "Server, key, info, and admin commands you'll run in production.",
    ),
    "interview-questions": (
        "Redis Interview Questions",
        "Interview",
        "High-signal Redis probes for senior backend and architect interviews.",
    ),
}


@dataclass
class Page:
    summary: str
    concepts: str
    quick_ref: str
    snippets: str
    gotchas: str


def flatten_topics(modules: list) -> list[str]:
    topics: list[str] = []
    for mod in modules:
        topics.extend(mod["topics"])
    return topics


def iter_module_topics(modules: list) -> list[tuple[int, str, str, int]]:
    result: list[tuple[int, str, str, int]] = []
    for mod in modules:
        for idx, slug in enumerate(mod["topics"], start=1):
            result.append((mod["id"], mod["focus"], slug, idx))
    return result


def write_order_yaml(topics: list[str], path: Path) -> None:
    header = (
        "# Flat topic order — derived from redis_cheatsheet_modules.yaml.\n"
        "# Prefer editing data/redis_cheatsheet_modules.yaml for module structure.\n"
        "topics:\n"
    )
    path.write_text(header + "".join(f"  - {s}\n" for s in topics), encoding="utf-8")


def see_also(slug: str, ordered: list[str]) -> str:
    links: list[str] = []
    idx = ordered.index(slug)
    if idx > 0:
        prev = ordered[idx - 1]
        links.append(f"- [Previous: {TOPIC_META[prev][1]}](/{SECTION}/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        links.append(f"- [Next: {TOPIC_META[nxt][1]}](/{SECTION}/{nxt}/)")
    links.append(f"- [{SECTION_TITLE} Index](/{SECTION}/)")
    links.append("- [Redis vs Memcached](/database-handbook/redis-vs-memcached/)")
    links.append("- [Database Handbook](/database-handbook/)")
    return "\n".join(links)


def front_matter(slug: str, mod_id: int, mod_title: str, topic_idx: int) -> str:
    title, short, desc = TOPIC_META[slug]
    return f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["redis-cheatsheet", "redis", "cheatsheet", "handbook"]
categories: ["{SECTION_TITLE}"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{mod_id}.{topic_idx}"
ShowToc: true
---

"""


def render(page: Page, slug: str, ordered: list[str]) -> str:
    return "\n".join(
        [
            "## Executive Summary",
            "",
            page.summary.strip(),
            "",
            "---",
            "",
            "## Core Concepts",
            "",
            page.concepts.strip(),
            "",
            "---",
            "",
            "## Quick Reference",
            "",
            page.quick_ref.strip(),
            "",
            "---",
            "",
            "## Snippets",
            "",
            page.snippets.strip(),
            "",
            "---",
            "",
            "## Common Gotchas",
            "",
            page.gotchas.strip(),
            "",
            "---",
            "",
            "## Related Topics",
            "",
            see_also(slug, ordered),
            "",
        ]
    )


def p(summary: str, concepts: str, quick_ref: str, snippets: str, gotchas: str) -> Page:
    return Page(summary, concepts, quick_ref, snippets, gotchas)


PAGE_BODIES: dict[str, Page] = {
    "architecture": p(
        summary="**Redis** is an in-memory data structure server: one **primary thread** executes commands, optional **I/O threads** handle networking, and data lives in **RAM** with optional RDB/AOF persistence. Clients speak the **RESP** protocol over TCP (or Unix socket).",
        concepts=textwrap.dedent("""
            ```mermaid
            flowchart TB
              clients[Clients] --> io[I/O threads optional]
              io --> event[Event loop - command thread]
              event --> dict[Keyspace dict]
              dict --> types[Strings / Lists / Sets / ...]
              event --> aof[(AOF)]
              event --> rdb[(RDB)]
              event --> repl[Replication buffer]
            ```

            | Component | Recap |
            | :--- | :--- |
            | **Event loop** | Single thread runs commands — no locks on data structures |
            | **I/O threads** (6+) | Read/write sockets in parallel; command execution stays single-threaded |
            | **Keyspace** | Global hash table: key → typed object (robj) |
            | **RESP** | Simple text protocol; pipelining = many commands, one round trip |
            | **Memory** | `used_memory` vs `used_memory_rss`; jemalloc allocator |
            | **Modules** | Redis Stack, RediSearch, RedisJSON extend core via API |
        """),
        quick_ref=textwrap.dedent("""
            ```bash
            redis-cli INFO server
            redis-cli INFO memory
            redis-cli INFO stats
            redis-cli CONFIG GET maxmemory
            redis-cli CONFIG GET io-threads
            redis-cli CLIENT LIST
            redis-cli MONITOR          # debug only — kills prod throughput
            ```
        """),
        snippets=textwrap.dedent("""
            ### `redis.conf` essentials

            ```conf
            bind 0.0.0.0
            protected-mode yes
            port 6379
            maxmemory 2gb
            maxmemory-policy allkeys-lru
            io-threads 4
            io-threads-do-reads yes
            appendonly yes
            appendfsync everysec
            ```

            ### Connection from app (Lettuce — Java)

            ```java
            RedisClient client = RedisClient.create("redis://localhost:6379");
            StatefulRedisConnection<String, String> conn = client.connect();
            conn.sync().set("key", "value");
            ```
        """),
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `KEYS *` in production | Use `SCAN` with cursor |\n| `MONITOR` on busy instance | Use `LATENCY DOCTOR`, slowlog |\n| Assuming multi-threaded command execution | Only one command thread — offload with sharding (Cluster) |\n| No `maxmemory` + no eviction | OOM kill at OS level |",
    ),
    "data-structures": p(
        summary="Every Redis key maps to **one typed value**. Pick the type by access pattern — not everything is a JSON string. Types share **TTL on the key**, not per-field TTL (except streams entries have IDs).",
        concepts=textwrap.dedent("""
            | Type | Use when | Core commands |
            | :--- | :--- | :--- |
            | **String** | Counters, cache blobs, bitmaps | `GET`, `SET`, `INCR` |
            | **Hash** | Object fields (user profile) | `HSET`, `HGET`, `HGETALL` |
            | **List** | Queue, timeline tail | `LPUSH`, `RPOP`, `BLPOP` |
            | **Set** | Unique tags, intersections | `SADD`, `SINTER` |
            | **Sorted set** | Rankings, delayed jobs by score | `ZADD`, `ZRANGEBYSCORE` |
            | **Stream** | Log, consumer groups | `XADD`, `XREADGROUP` |
            | **HyperLogLog** | Cardinality estimate | `PFADD`, `PFCOUNT` |
            | **GEO** | Lat/long (sorted-set backed) | `GEOADD`, `GEORADIUS` |

            **Encoding:** Redis picks compact encodings (ziplist, listpack, intset) for small values and upgrades to hash table / skip list as data grows.
        """),
        quick_ref="```bash\nredis-cli TYPE mykey\nredis-cli OBJECT ENCODING mykey\nredis-cli TTL mykey\nredis-cli PTTL mykey\nredis-cli EXPIRE mykey 3600\nredis-cli PERSIST mykey\n```",
        snippets="### Key naming convention\n\n```\napp:entity:id:field\nsession:{userId}\ncache:product:{sku}\nlock:order:{orderId}\n```\n\n### Inspect type\n\n```bash\nredis-cli HSET user:42 name Alice age 30\nredis-cli TYPE user:42        # hash\nredis-cli OBJECT ENCODING user:42\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Storing JSON strings for field updates | Use **Hash** or RedisJSON module |\n| `HGETALL` on huge hashes | `HSCAN` or fetch needed fields |\n| TTL on hash field | TTL is on **key** — split keys if per-field expiry needed |",
    ),
    "strings": p(
        summary="**Strings** are Redis's simplest type — binary-safe blobs up to **512 MB**. Used for caching, counters, distributed flags, and as the underlying type for **bitmaps**.",
        concepts="| Feature | Detail |\n| :--- | :--- |\n| **Binary safe** | Any byte sequence |\n| **Atomic counters** | `INCR`, `INCRBY`, `DECR` |\n| **Conditional set** | `SET key val NX EX 30` — lock + TTL |\n| **Batch** | `MGET`, `MSET` |\n| **Encoding** | `int` for integers, `embstr`/`raw` for strings |",
        quick_ref="```bash\nSET cache:item:1 \"payload\" EX 300\nGET cache:item:1\nSETNX lock:job 1\nINCR page:views\nINCRBY wallet:42 100\nAPPEND log:buf \"line\\n\"\nSTRLEN cache:item:1\nGETRANGE cache:item:1 0 99\nSETBIT flags 7 1\nGETBIT flags 7\n```",
        snippets="### Cache-aside read\n\n```bash\nGET product:99\n# miss → load DB → SET product:99 \"{json}\" EX 600\n```\n\n### Compare-and-set pattern\n\n```bash\nSET balance:42 100\n# optimistic: WATCH + MULTI or Lua script\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Large values in strings | Split or compress; watch network I/O |\n| `GET` + `SET` for counters under race | Use `INCR` — atomic |\n| `SETNX` without TTL | Dead lock if client dies — always `SET NX EX` |",
    ),
    "hashes": p(
        summary="**Hashes** store field → value maps — ideal for **objects** (user, session, product attributes) with O(1) single-field access.",
        concepts="| Command | Purpose |\n| :--- | :--- |\n| `HSET` / `HGET` | Set/get one field |\n| `HMSET` / `HMGET` | Multi field (HMSET deprecated — use `HSET` multi) |\n| `HGETALL` | All fields — careful on large hashes |\n| `HINCRBY` | Atomic numeric field increment |\n| `HSCAN` | Cursor iteration |\n\nSmall hashes use **listpack** encoding; large ones use **hash table**.",
        quick_ref="```bash\nHSET user:42 name Alice email alice@example.com\nHGET user:42 name\nHMGET user:42 name email\nHGETALL user:42\nHINCRBY user:42 loginCount 1\nHEXISTS user:42 email\nHDEL user:42 tempField\nHLEN user:42\nHSCAN user:42 0 MATCH name* COUNT 100\n```",
        snippets="### Session hash\n\n```bash\nHSET session:abc userId 42 roles admin,editor\nEXPIRE session:abc 1800\n```\n\n### Partial update without reading full object\n\n```bash\nHSET product:99 price 19.99 stock 42\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `HGETALL` on 10k fields | `HSCAN` or field-specific `HMGET` |\n| Nested objects | Flatten fields or use RedisJSON |\n| Expecting per-field TTL | Expire whole key or use separate keys |",
    ),
    "lists": p(
        summary="**Lists** are doubly-linked lists of strings — used as **stacks**, **queues**, and **blocking work queues** with `BLPOP`/`BRPOP`.",
        concepts="| Pattern | Commands |\n| :--- | :--- |\n| Stack | `LPUSH` + `LPOP` |\n| Queue | `LPUSH` + `RPOP` |\n| Blocking consumer | `BLPOP queue 0` |\n| Trim bounded log | `LPUSH` + `LTRIM` |\n| Reliable queue | `RPOPLPUSH` / `BRPOPLPUSH` (deprecated → streams) |",
        quick_ref="```bash\nLPUSH jobs \"task-1\" \"task-2\"\nRPOP jobs\nBLPOP jobs 30\nLLEN jobs\nLRANGE jobs 0 -1\nLTRIM jobs 0 999\nLINDEX jobs 0\nLINSERT jobs BEFORE \"task-2\" \"task-1b\"\n```",
        snippets="### Simple job queue\n\n```bash\n# producer\nLPUSH queue:email '{\"to\":\"a@b.com\"}'\n# worker (blocking 10s)\nBLPOP queue:email 10\n```\n\n### Recent-items cap\n\n```bash\nLPUSH recent:42 itemId\nLTRIM recent:42 0 49\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| At-most-once with `RPOP` | Worker crash loses job — use **Streams** + consumer group |\n| `LRANGE 0 -1` on huge list | O(N) — paginate with indexes |\n| Multiple consumers on one list | Race on `RPOP` — one winner only |",
    ),
    "sets": p(
        summary="**Sets** are unordered unique strings — **O(1)** add/remove/membership; **set algebra** (`SINTER`, `SUNION`, `SDIFF`) powers tagging and relationship queries.",
        concepts="| Operation | Command |\n| :--- | :--- |\n| Add / remove | `SADD`, `SREM` |\n| Membership | `SISMEMBER` |\n| All members | `SMEMBERS` (small sets) |\n| Iterate | `SSCAN` |\n| Intersection | `SINTER key1 key2` |\n| Union | `SUNION` |\n| Difference | `SDIFF` |",
        quick_ref="```bash\nSADD tags:article:1 redis cache nosql\nSISMEMBER tags:article:1 redis\nSMEMBERS tags:article:1\nSCARD tags:article:1\nSINTER tags:article:1 tags:article:2\nSUNION user:1:likes user:2:likes\nSDIFF user:1:likes user:2:likes\nSREM tags:article:1 nosql\n```",
        snippets="### Mutual followers (intersection)\n\n```bash\nSINTER user:1:followers user:2:followers\n```\n\n### Unique visitors (HyperLogLog often better at scale)\n\n```bash\nSADD visitors:2026-06-30 user-42\nSCARD visitors:2026-06-30\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `SMEMBERS` on large sets | `SSCAN` |\n| Storing high-cardinality unique IDs in sets | Use **HyperLogLog** or **Bitmap** if approximate OK |\n| `SINTER` on huge sets | Can block event loop — consider pre-compute or sharding |",
    ),
    "sorted-sets": p(
        summary="**Sorted sets (ZSET)** combine unique member + **float score** — sorted by score in **O(log N)**. Leaderboards, priority queues, and time-indexed data.",
        concepts="| Command | Purpose |\n| :--- | :--- |\n| `ZADD` | Add/update score |\n| `ZRANGE` / `ZREVRANGE` | Rank by index |\n| `ZRANGEBYSCORE` | Score range query |\n| `ZRANK` / `ZREVRANK` | Position of member |\n| `ZINCRBY` | Atomic score bump |\n| `ZPOPMIN` / `ZPOPMAX` | Pop lowest/highest |\n\nEncoding: **listpack** (small) or **skip list + hash table**.",
        quick_ref="```bash\nZADD leaderboard 100 player1 200 player2 150 player3\nZREVRANGE leaderboard 0 9 WITHSCORES\nZRANK leaderboard player2\nZINCRBY leaderboard 50 player1\nZRANGEBYSCORE tasks 0 1690000000 LIMIT 0 10\nZREM leaderboard player3\nZCARD leaderboard\nZCOUNT leaderboard 100 200\n```",
        snippets="### Delayed job queue (score = run-at epoch ms)\n\n```bash\nZADD delayed 1690000000000 job-uuid-1\nZRANGEBYSCORE delayed 0 1690000100000 LIMIT 0 1\nZREM delayed job-uuid-1\n```\n\n### Top-N with ties\n\n```bash\nZREVRANGE leaderboard 0 99 WITHSCORES\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Score collisions for time ordering | Use composite score or stream IDs |\n| `ZRANGEBYSCORE` on huge range | Add `LIMIT` |\n| Updating member name | Remove + add — member string is identity |",
    ),
    "bitmaps": p(
        summary="**Bitmaps** treat a string value as a bit array — **SETBIT/GETBIT** for flags, **BITOP** for AND/OR/XOR, extremely compact for boolean analytics.",
        concepts="| Command | Purpose |\n| :--- | :--- |\n| `SETBIT key offset 1` | Set bit |\n| `GETBIT key offset` | Read bit |\n| `BITCOUNT key` | Count set bits |\n| `BITOP AND dest k1 k2` | Bitwise ops |\n| `BITFIELD` | Get/set/int increment on bit fields |\n\nClassic use: **DAU** — `SETBIT visits:2026-06-30 userId 1`.",
        quick_ref="```bash\nSETBIT visits:2026-06-30 42 1\nGETBIT visits:2026-06-30 42\nBITCOUNT visits:2026-06-30\nBITOP AND active both:2026-06-29 both:2026-06-30\nBITFIELD flags GET u8 0\n```",
        snippets="### Daily active users\n\n```bash\nSETBIT dau:2026-06-30 10042 1\nBITCOUNT dau:2026-06-30\n```\n\n### Feature flags per user segment\n\n```bash\nSETBIT features:beta userId 1\nGETBIT features:beta userId\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Sparse high offsets | Memory grows to max offset — consider Hash or HLL |\n| User IDs not dense integers | Map to dense index or use Set/HLL |\n| `BITOP` on large keys | CPU spike on single thread |",
    ),
    "hyperloglog": p(
        summary="**HyperLogLog** estimates **cardinality** (~0.81% error) using **~12 KB** per key regardless of billions of elements — not for membership tests.",
        concepts="| Property | Value |\n| :--- | :--- |\n| **Commands** | `PFADD`, `PFCOUNT`, `PFMERGE` |\n| **Memory** | ~12 KB per key |\n| **Exact?** | No — approximate distinct count |\n| **Merge** | `PFMERGE` unions sketches |\n\nUse for: UV counts, unique IPs, funnel dedup at scale.",
        quick_ref="```bash\nPFADD uv:2026-06-30 user-1 user-2 user-1\nPFCOUNT uv:2026-06-30\nPFMERGE uv:week23 uv:day1 uv:day2 uv:day3\nPFCOUNT uv:week23\n```",
        snippets="### Page unique views\n\n```bash\nPFADD page:/home:uv session-abc session-def session-abc\nPFCOUNT page:/home:uv\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Need exact count | Use Set (memory cost) or external store |\n| Test membership | HLL cannot — use Set or Bloom (module) |\n| Small cardinalities | Error dominates — Set may be fine under ~10k |",
    ),
    "streams": p(
        summary="**Streams** are append-only logs with **auto IDs** (`milliseconds-sequence`). **Consumer groups** give at-least-once delivery, pending entries, and acknowledgment — Redis's replacement for list-based queues.",
        concepts="""```mermaid
flowchart LR
  prod[Producer XADD] --> stream[(Stream)]
  stream --> cg[Consumer Group]
  cg --> c1[Consumer A]
  cg --> c2[Consumer B]
  c1 --> xack[XACK]
```

| Command | Purpose |
| :--- | :--- |
| `XADD` | Append entry |
| `XREAD` | Read from ID |
| `XGROUP CREATE` | Consumer group |
| `XREADGROUP` | Group read |
| `XACK` | Ack processed |
| `XPENDING` | Unacked messages |
| `XCLAIM` | Reclaim stale pending |""",
        quick_ref="```bash\nXADD orders * userId 42 amount 99.99\nXREAD COUNT 10 STREAMS orders 0\nXGROUP CREATE orders processors $ MKSTREAM\nXREADGROUP GROUP processors c1 COUNT 1 STREAMS orders >\nXACK orders processors 1690000000000-0\nXPENDING orders processors\nXTRIM orders MAXLEN ~ 10000\n```",
        snippets="### Producer / consumer sketch\n\n```bash\n# producer\nXADD events * type ORDER_PLACED id 42\n# consumer\nXREADGROUP GROUP workers w1 BLOCK 5000 COUNT 10 STREAMS events >\nXACK events workers <message-id>\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| No `XACK` after read | Message stays pending — monitor `XPENDING` |\n| Consumer crash | Use `XAUTOCLAIM` / `XCLAIM` with idle time |\n| Unbounded stream | `XTRIM` or `MAXLEN ~` on `XADD` |",
    ),
    "pub-sub": p(
        summary="**Pub/Sub** is fire-and-forget **fan-out messaging** — subscribers only receive messages while connected; **no persistence**, no acks, no replay.",
        concepts="| Mode | Subscribe |\n| :--- | :--- |\n| Channel | `SUBSCRIBE news` |\n| Pattern | `PSUBSCRIBE news.*` |\n| Publish | `PUBLISH news.sports \"score\"` |\n\nSeparate connection recommended — subscriber connection blocks in subscribe mode.",
        quick_ref="```bash\n# terminal 1\nSUBSCRIBE notifications\n# terminal 2\nPUBLISH notifications \"deploy complete\"\n# pattern\nPSUBSCRIBE cache:*\nPUBLISH cache:invalidate product:99\nPUBSUB CHANNELS\nPUBSUB NUMSUB notifications\n```",
        snippets="### Invalidation broadcast\n\n```bash\nPUBLISH cache:invalidate '{\"key\":\"product:99\"}'\n```\n\nApps subscribe and evict local/Redis cache keys.",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Message loss if no subscriber | Use **Streams** or external broker |\n| Slow subscriber | Disconnect — no backlog |\n| `SUBSCRIBE` on shared pool connection | Dedicated pub/sub connections |",
    ),
    "transactions": p(
        summary="**MULTI/EXEC** batches commands atomically — all queued commands run in sequence without interleaving. **Not** rollback on failure mid-batch. **WATCH** enables optimistic locking.",
        concepts="| Feature | Behavior |\n| :--- | :--- |\n| `MULTI` | Start queue |\n| `EXEC` | Run all or nothing if `WATCH` keys changed |\n| `DISCARD` | Abort queue |\n| `WATCH key` | Abort `EXEC` if key modified since `WATCH` |\n| **Pipeline** | Batch without atomicity — faster for bulk |\n\nErrors: compile-time (bad command in `MULTI`) vs exec-time (e.g. `INCR` on string).",
        quick_ref="```bash\nWATCH balance:42\nGET balance:42\nMULTI\nDECRBY balance:42 10\nINCRBY balance:99 10\nEXEC\n# EXEC returns nil if WATCH key changed\n```",
        snippets="### Transfer with WATCH\n\n```bash\nWATCH account:A account:B\nMULTI\nDECRBY account:A 50\nINCRBY account:B 50\nEXEC\n```\n\nPrefer **Lua** for complex atomic logic.",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Expecting RDBMS-style rollback | Failed command doesn't undo prior commands in `EXEC` |\n| Long `MULTI` block | Blocks other clients — keep short |\n| `WATCH` on hot keys | High abort rate — use Lua or Redisson |",
    ),
    "lua-scripts": p(
        summary="**Lua scripts** run **atomically** on the server — no other commands interleave. Use for compare-and-set, rate limits, and lock release checks.",
        concepts="| API | Purpose |\n| :--- | :--- |\n| `EVAL script numkeys key [key ...] arg [arg ...]` | Run script |\n| `EVALSHA sha` | Run cached bytecode |\n| `SCRIPT LOAD` | Preload → SHA |\n\nScripts should be deterministic. Redis 7+ supports **Functions** (persistent library).",
        quick_ref="```bash\nEVAL \"return redis.call('GET', KEYS[1])\" 1 mykey\nSCRIPT LOAD \"return redis.call('INCR', KEYS[1])\"\nEVALSHA <sha> 1 counter\n```",
        snippets="### Safe lock release\n\n```lua\nif redis.call('GET', KEYS[1]) == ARGV[1] then\n  return redis.call('DEL', KEYS[1])\nelse\n  return 0\nend\n```\n\n```bash\nEVAL \"<script>\" 1 lock:order:1 token-uuid\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Long Lua scripts | Blocks entire server — keep O(1) |\n| Non-deterministic calls banned | No `TIME`, random, or cross-slot keys in Cluster |\n| Hard-coded keys in Cluster | All keys in same hash slot or use hash tags `{tag}` |",
    ),
    "persistence": p(
        summary="Redis offers **RDB** (point-in-time snapshots) and **AOF** (append-only command log). Production often uses **both**: RDB for fast restarts, AOF for finer durability.",
        concepts="""| Mode | Mechanism | Trade-off |
| :--- | :--- | :--- |
| **RDB** | `SAVE` / `BGSAVE` fork + dump | Compact; may lose data since last snapshot |
| **AOF** | Log every write | `always` / `everysec` / `no` fsync |
| **Hybrid** | RDB preamble in AOF rewrite | Best of both |
| **none** | Pure cache | Fastest; data lost on restart |

`fork` for BGSAVE causes copy-on-write memory spike.""",
        quick_ref="```bash\nSAVE                    # blocking — avoid prod\nBGSAVE\nLASTSAVE\nCONFIG GET save\nCONFIG GET appendonly\nCONFIG GET appendfsync\nBGREWRITEAOF\n```",
        snippets="```conf\nsave 900 1\nsave 300 10\nsave 60 10000\nappendonly yes\nappendfsync everysec\nno-appendfsync-on-rewrite yes\nauto-aof-rewrite-percentage 100\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `appendfsync always` | Durability max; throughput min |\n| `everysec` | Up to ~1s loss on crash |\n| BGSAVE during memory pressure | Monitor COW — tune `save` rules |",
    ),
    "replication": p(
        summary="**Primary → replica** async replication. Replicas serve **reads** (optional) and provide failover candidates. **Partial resync** via replication backlog on short disconnects.",
        concepts="""```mermaid
flowchart LR
  primary[(Primary)] --> repl[Replication stream]
  repl --> r1[Replica 1]
  repl --> r2[Replica 2]
```

| Setting | Purpose |
| :--- | :--- |
| `REPLICAOF host port` | Join as replica |
| `INFO replication` | Lag, offset, role |
| `replica-read-only yes` | Block writes on replica |
| `min-replicas-to-write` | Quorum write safety |""",
        quick_ref="```bash\nINFO replication\nROLE\nREPLICAOF 10.0.0.1 6379\nREPLICAOF NO ONE    # promote manually\nCONFIG GET repl-backlog-size\n```",
        snippets="### Read from replica (Spring Lettuce)\n\n```java\n// configure ReadFrom.REPLICA_PREFERRED for read scaling\n```\n\nMonitor `master_repl_offset` vs `slave_repl_offset` for lag.",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Stale reads on replica | `WAIT numreplicas timeout` after write if needed |\n| Replica writable | Keep `replica-read-only yes` |\n| Full resync after long outage | Increase `repl-backlog-size` |",
    ),
    "sentinel": p(
        summary="**Sentinel** monitors primaries/replicas, performs **automatic failover**, and acts as a **configuration provider** for clients — typically 3+ sentinel processes for quorum.",
        concepts="| Concept | Detail |\n| :--- | :--- |\n| **Quorum** | `sentinel monitor mymaster ... 2` — 2 sentinels to agree on failover |\n| **SDOWN/ODOWN** | Subjective vs objective down |\n| **Failover** | Elect replica → `REPLICAOF NO ONE` → re-point others |\n| **Client** | Ask Sentinel for current primary address |\n\nSentinel runs as separate processes (or K8s sidecars), not inside `redis-server`.",
        quick_ref="```bash\nredis-cli -p 26379 SENTINEL masters\nredis-cli -p 26379 SENTINEL replicas mymaster\nredis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster\nredis-cli -p 26379 SENTINEL failover mymaster\n```",
        snippets="```conf\nsentinel monitor mymaster 127.0.0.1 6379 2\nsentinel down-after-milliseconds mymaster 5000\nsentinel failover-timeout mymaster 60000\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Even number of sentinels | Use odd count (3, 5) for split-brain |\n| Client cache stale primary | Use sentinel-aware driver with refresh |\n| Failover during high write load | `min-replicas-to-write` guard |",
    ),
    "cluster": p(
        summary="**Redis Cluster** shards keys across **16384 hash slots** on multiple primaries — each with replicas. Clients must be **cluster-aware** (`MOVED`/`ASK` redirects).",
        concepts="""| Topic | Detail |
| :--- | :--- |
| **Slot** | `CRC16(key) mod 16384` |
| **Hash tag** | `{user}:profile` and `{user}:orders` → same slot |
| **MOVED** | Permanent redirect — client updates slot map |
| **ASK** | Temporary during resharding |
| **Min nodes** | 3 primaries typical for production |

Multi-key ops require same slot — use hash tags.""",
        quick_ref="```bash\nCLUSTER INFO\nCLUSTER NODES\nCLUSTER SLOTS\nCLUSTER KEYSLOT mykey\nredis-cli --cluster create host1:6379 host2:6379 --cluster-replicas 1\nredis-cli --cluster reshard host1:6379\nredis-cli -c -h host1 -p 6379   # cluster mode\n```",
        snippets="### Hash tag for multi-key transaction\n\n```bash\nMSET {user:42}:name Alice {user:42}:email a@b.com\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `MGET` keys on different slots | Cluster rejects — use hash tags or separate calls |\n| Non-cluster client | Gets `MOVED` errors |\n| Lua with multiple keys | All keys must share slot |",
    ),
    "eviction-policies": p(
        summary="When **`maxmemory`** is hit, Redis evicts keys per **`maxmemory-policy`** — critical for cache workloads. **noeviction** returns errors instead (good for non-cache primary store).",
        concepts="| Policy | Evicts |\n| :--- | :--- |\n| `noeviction` | Nothing — writes fail |\n| `allkeys-lru` | Any key — approximate LRU |\n| `allkeys-lfu` | Any key — frequency (Redis 4+) |\n| `volatile-lru` | Keys with TTL only |\n| `volatile-lfu` | TTL keys by frequency |\n| `volatile-ttl` | Shortest TTL first |\n| `allkeys-random` / `volatile-random` | Random |\n\n**LRU** is sampled (`maxmemory-samples`), not exact global LRU.",
        quick_ref="```bash\nCONFIG GET maxmemory\nCONFIG GET maxmemory-policy\nCONFIG SET maxmemory 4gb\nCONFIG SET maxmemory-policy allkeys-lfu\nINFO memory\n```",
        snippets="```conf\nmaxmemory 2gb\nmaxmemory-policy allkeys-lfu\nmaxmemory-samples 10\n```\n\nSet **TTL on cache keys** when using `volatile-*` policies.",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `volatile-lru` but keys have no TTL | Nothing evicted → OOM |\n| Hot key evicted with LRU | Consider `lfu` or app-level TTL jitter |\n| No `maxmemory` in container | Set to ~75% of container limit |",
    ),
    "caching-patterns": p(
        summary="Standard cache patterns with Redis: **cache-aside**, **read-through**, **write-through**, **write-behind** — plus **stampede** protection with locks or probabilistic early expiry.",
        concepts="""```mermaid
flowchart LR
  app[App] -->|1 miss| redis[(Redis)]
  app -->|2 load| db[(DB)]
  app -->|3 populate| redis
```

| Pattern | Flow |
| :--- | :--- |
| **Cache-aside** | App reads cache; on miss loads DB and sets cache |
| **Write-through** | Write DB + cache together |
| **Write-behind** | Write cache; async flush to DB |
| **TTL jitter** | `EX = base + random(0, 60)` avoids thundering herd |""",
        quick_ref="Cache-aside:\n```bash\nGET key || (load DB; SET key val EX 300)\n```\n\nInvalidate:\n```bash\nDEL key\n# or PUBLISH cache:invalidate key\n```",
        snippets="### Stampede lock\n\n```bash\nSET lock:rebuild:product:99 1 NX EX 10\n# winner rebuilds; losers retry GET or wait\n```\n\n### Probabilistic early expiration\n\nRefresh cache when `ttl < random_threshold`.",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Cache inconsistency after DB update | Delete/update cache on write |\n| Same TTL for all keys | Expiry stampede — add jitter |\n| Caching null forever | Short TTL for negative cache |",
    ),
    "distributed-lock": p(
        summary="Minimal lock: **`SET key token NX PX ttl`**. Release only if token matches (Lua). **Redlock** (multi-instance) is debated — prefer **fencing tokens** with durable store for correctness.",
        concepts="| Rule | Why |\n| :--- | :--- |\n| **Unique token** | Prevent deleting another owner's lock |\n| **TTL** | Auto-release if holder dies |\n| **Lua unlock** | Compare-and-del atomically |\n| **Fencing** | Monotonic token to storage prevents stale writes |\n\nLibraries: Redisson, Lettuce recipes, Spring Integration.",
        quick_ref="```bash\nSET lock:resource:1 uuid NX PX 30000\n# renew with Lua if work runs longer\n# release via EVAL compare-and-del\n```",
        snippets="```lua\n-- acquire returns OK or nil\nreturn redis.call('SET', KEYS[1], ARGV[1], 'NX', 'PX', ARGV[2])\n```\n\n```lua\n-- release\nif redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('DEL', KEYS[1]) else return 0 end\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `SETNX` without TTL | Deadlock |\n| `DEL` without token check | Deletes another client's lock |\n| Long GC pause > TTL | Lock expires; use fencing + short critical sections |",
    ),
    "rate-limiter": p(
        summary="Redis counters + TTL implement **fixed window**, **sliding window** (sorted set or INCR with multiple buckets), and **token bucket** — atomic via `INCR` or Lua.",
        concepts="| Algorithm | Sketch |\n| :--- | :--- |\n| **Fixed window** | `INCR rate:user:42:minute` + `EXPIRE 60` |\n| **Sliding window** | `ZADD` timestamp members; trim old |\n| **Token bucket** | Hash: tokens + last_refill; Lua refill |\n| **Global limit** | Single key or sharded counters |",
        quick_ref="```bash\nINCR rate:api:user:42:202606301045\nEXPIRE rate:api:user:42:202606301045 60\n# if count > limit → 429\n```",
        snippets="### Sliding window (sorted set)\n\n```bash\nZADD rate:user:42 now now\nZREMRANGEBYSCORE rate:user:42 0 now-60000\nZCARD rate:user:42\nEXPIRE rate:user:42 61\n```",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Fixed window burst at boundary | 2× traffic at edges — use sliding |\n| Race without atomicity | `INCR` is atomic; complex logic → Lua |\n| Hot key on global limit | Shard counter keys |",
    ),
    "session-store": p(
        summary="Store sessions as **Hash** (`session:id` → fields) or **String** (serialized JSON) with **TTL**. Shared Redis enables **stateless** app servers behind a load balancer.",
        concepts="| Approach | Pros |\n| :--- | :--- |\n| **Hash fields** | Partial updates, smaller payloads |\n| **JSON string** | Simple serialization |\n| **TTL refresh** | `EXPIRE` on each request (sliding session) |\n| **Cookie** | Store only session ID — not data |\n\nSpring Session Redis uses hash + default namespace.",
        quick_ref="```bash\nHSET session:abc userId 42 roles admin\nEXPIRE session:abc 1800\nHGETALL session:abc\nDEL session:abc\nTTL session:abc\n```",
        snippets="### Spring Session (conceptual)\n\n```yaml\nspring.session.store-type: redis\nspring.data.redis.host: localhost\n```\n\nSession key pattern: `spring:session:sessions:<id>`",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| Large session blobs | Keep minimal data in session |\n| No TTL | Memory leak — always expire |\n| Session fixation | Rotate ID on login |\n| GDPR — sensitive data in Redis | Encrypt or store reference only |",
    ),
    "common-redis-commands": p(
        summary="Production **admin**, **key**, and **debug** commands — bookmark this page for on-call.",
        concepts="| Category | Commands |\n| :--- | :--- |\n| **Server** | `INFO`, `CONFIG GET/SET`, `SHUTDOWN`, `SLOWLOG` |\n| **Keys** | `DEL`, `UNLINK`, `EXISTS`, `SCAN`, `TYPE`, `TTL` |\n| **Debug** | `LATENCY DOCTOR`, `MEMORY DOCTOR`, `OBJECT` |\n| **Danger** | `FLUSHALL`, `KEYS`, `DEBUG SEGFAULT` |",
        quick_ref=textwrap.dedent("""
            ```bash
            # Health
            redis-cli PING
            redis-cli INFO server | grep redis_version
            redis-cli SLOWLOG GET 10

            # Key scan (prod-safe)
            redis-cli SCAN 0 MATCH user:* COUNT 100

            # Memory
            redis-cli MEMORY USAGE mykey
            redis-cli MEMORY STATS

            # Bulk delete (async free)
            redis-cli UNLINK key1 key2

            # Client management
            redis-cli CLIENT KILL TYPE normal ADDR ...
            redis-cli CLIENT PAUSE 5000
            ```
        """),
        snippets="### Safe iteration\n\n```bash\nSCAN 0 MATCH cache:* COUNT 500\n```\n\nRepeat with returned cursor until 0.",
        gotchas="| Pitfall | Fix |\n| :--- | :--- |\n| `KEYS *` | Blocks — `SCAN` |\n| `FLUSHALL` without `ASYNC` | Blocks on large datasets |\n| `CONFIG SET` without persist | Lost on restart — update `redis.conf` |",
    ),
    "interview-questions": p(
        summary="High-signal **Redis interview probes** — architecture, persistence, cluster, caching, and correctness traps.",
        concepts="| Theme | Sample probe |\n| :--- | :--- |\n| **Threading** | Why single-threaded? I/O threads? |\n| **Durability** | RDB vs AOF trade-offs |\n| **Cache** | Cache-aside vs write-through; stampede |\n| **HA** | Sentinel vs Cluster |\n| **Correctness** | Distributed lock pitfalls |",
        quick_ref="Quick drills: explain `SET NX EX`, `WATCH`/`MULTI`, hash slot math, `volatile-lru` vs `allkeys-lru`, replica lag.",
        snippets="""{{< interview-answer >}}
**Q:** Why is Redis fast?

**A:** In-memory data structures, single-threaded command path (no lock contention), efficient encodings, optional I/O threading, and simple protocol. Bottleneck is usually memory size, network, or single-core CPU — not disk I/O for pure cache workloads.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** Can you lose data with `appendfsync everysec`?

**A:** Yes — up to ~1 second of writes if the process crashes between write and fsync. `always` is safer but slower. Many caches accept `everysec`; financial primary stores may not.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** How does Redis Cluster split keys?

**A:** 16384 hash slots; slot = CRC16(key) mod 16384. Hash tags `{...}` force colocation. Clients track slot → node map and follow MOVED/ASK redirects.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** What's wrong with `SETNX` for locks?

**A:** No TTL → deadlock if client dies. Must use `SET key token NX PX ms`. Unlock must compare token in Lua before DEL. Still doesn't prevent stale work after TTL expiry without fencing tokens.
{{< /interview-answer >}}""",
        gotchas="Practice explaining **exactly-once** (impossible with basic Redis queue), **hot keys**, and **big key** remediation (`UNLINK`, split, read replicas).",
    ),
}


def main() -> None:
    raise SystemExit(
        "build_redis_cheatsheet.py is deprecated. "
        "Run: python scripts/generate_redis_handbook_refactor.py"
    )
    modules = yaml.safe_load(modules_path.read_text(encoding="utf-8"))["modules"]
    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "redis_cheatsheet_order.yaml")

    CONTENT.mkdir(parents=True, exist_ok=True)
    expected = {f"{slug}.md" for slug in ordered}

    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        if slug not in PAGE_BODIES:
            raise KeyError(f"Missing PAGE_BODIES for {slug}")
        body = render(PAGE_BODIES[slug], slug, ordered)
        path = CONTENT / f"{slug}.md"
        path.write_text(front_matter(slug, mod_id, mod_title, topic_idx) + body, encoding="utf-8")

    for path in CONTENT.glob("*.md"):
        if path.name != "_index.md" and path.name not in expected:
            path.unlink()

    print(f"Wrote {len(ordered)} pages to {CONTENT}")


if __name__ == "__main__":
    main()
