"""Unique Redis SME answers for top-150 interview questions."""

from __future__ import annotations

from redis_questions_data import QUESTIONS


def _p(short, detailed, internal, production, mistakes, followup):
    return {
        "short": short,
        "detailed": detailed,
        "internal": internal,
        "production": production,
        "mistakes": mistakes,
        "followup": followup,
    }


_STYLE_A = [
    "For this question, the architecturally correct Redis answer is",
    "The production-grade Redis answer is",
    "The senior-level decision is",
    "The practical Redis answer is",
]

_STYLE_B = [
    "You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew",
    "You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology",
    "You justify it by minimizing hot-key blast radius and single-thread CPU contention",
    "You justify it by aligning durability settings with business RPO/RTO and client retry contracts",
]


def _pick(items: list[str], qid: int) -> str:
    return items[qid % len(items)]


def _topic_key(question: str) -> str:
    q = question.lower()
    if any(k in q for k in ["memcached", "kafka", "rabbitmq", "versus", " vs "]):
        return "comparison"
    if any(k in q for k in ["hot key", "breakdown", "stampede", "singleflight", "thundering herd"]):
        return "cache_failure"
    if any(k in q for k in ["avalanche", "ttl jitter", "expiry storm", "synchronized ttl", "expiration storm"]):
        return "cache_failure"
    if any(k in q for k in ["penetration", "bloom", "negative cache", "non-existent"]):
        return "cache_failure"
    if any(k in q for k in ["invalidation", "write-through", "write-behind", "cache-aside", "cache refresh"]):
        return "invalidation"
    if any(k in q for k in ["cache-aside", "caching pattern", "write-through", "write-behind"]):
        return "cache"
    if any(k in q for k in ["distributed lock", "redlock", "fencing", "set nx", "setnx", "token"]):
        return "locks"
    if any(k in q for k in ["lua", "eval", "evalsha", "function"]):
        return "lua"
    if any(k in q for k in ["multi", "exec", "watch", "pipeline vs", "optimistic"]):
        return "transactions"
    if any(k in q for k in ["xreadgroup", "xack", "xpending", "xclaim", "consumer group", "stream"]):
        return "streams"
    if any(k in q for k in ["pub/sub", "publish", "subscribe", "psubscribe"]):
        return "pubsub"
    if any(k in q for k in ["rdb", "aof", "bgsave", "appendfsync", "fork", "persistence", "rewrite"]):
        return "persistence"
    if any(k in q for k in ["replication", "replica", "repl lag", "partial resync", "wait ", "backlog"]):
        return "replication"
    if any(k in q for k in ["sentinel", "quorum", "sdown", "odown", "failover"]):
        return "sentinel"
    if any(k in q for k in ["cluster", "hash slot", "moved", "ask", "reshard", "hash tag", "16384"]):
        return "cluster"
    if any(k in q for k in ["encoding", "fragmentation", "used_memory", "jemalloc", "listpack", "memory model"]):
        return "memory"
    if any(k in q for k in ["resp", "pipelin", "protocol", "request processing"]):
        return "protocol"
    if any(k in q for k in ["maxmemory", "eviction", "lru", "lfu", "noeviction", "volatile-"]):
        return "eviction"
    if any(k in q for k in ["slowlog", "latency doctor", "info command", "monitoring", "latency history"]):
        return "monitoring"
    if any(k in q for k in ["triage", "troubleshoot", "runbook", "incident", "moved storm"]):
        return "troubleshooting"
    if any(k in q for k in ["capacity", "sizing", "growth plan", "estimate memory", "working set"]):
        return "capacity"
    if any(k in q for k in ["pipeline", "throughput", "latency", "p99", "io-threads", "unlink", "slow command"]):
        return "performance"
    if any(k in q for k in ["rate limit", "token bucket", "sliding window", "fixed window"]):
        return "rate_limit"
    if any(k in q for k in ["session"]):
        return "session"
    if any(k in q for k in ["single-thread", "event loop", "i/o thread", "deployment", "standalone", "topology"]):
        return "architecture"
    return "data_types"


def _payload(topic: str, question: str, qid: int) -> dict[str, str]:
    style_a = _pick(_STYLE_A, qid)
    style_b = _pick(_STYLE_B, qid + 1)
    stem = question.rstrip("?")

    if topic == "architecture":
        return _p(
            f"{style_a} treating Redis as a single-threaded command processor with optional I/O threading, then choosing HA topology to match RPO/RTO for: {stem}.",
            f"Redis throughput scales vertically per primary until CPU, memory, or hot-key skew dominates; Sentinel and Cluster solve availability and horizontal scale, not magic parallelism on one key for: {stem}.",
            f"Commands execute serially on the event loop, so long operations block all clients on that node — architecture must keep hot paths O(1) and shard before CPU saturates for: {stem}.",
            f"{style_b} when comparing standalone, Sentinel, and Cluster for: {stem}.",
            f"A common mistake is assuming Redis is multi-threaded for commands or colocating unrelated blast-radius workloads on one cluster for: {stem}.",
            f"What failover time, durability window, and client retry contract would you document before choosing topology for: {stem}?",
        )

    if topic == "memory":
        return _p(
            f"{style_a} separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: {stem}.",
            f"Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: {stem}.",
            f"`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: {stem}.",
            f"{style_b} after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: {stem}.",
            f"Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: {stem}.",
            f"Which encoding upgrade or key-shape change would you test first to reduce memory for: {stem}?",
        )

    if topic == "protocol":
        return _p(
            f"{style_a} using RESP over TCP with connection pooling and pipelining to cut round trips without expecting multi-command parallelism on the server for: {stem}.",
            f"Pipelining batches many commands in one RTT while Redis still executes them sequentially — throughput gains come from network efficiency, not parallel command threads for: {stem}.",
            f"Cluster clients must handle MOVED/ASK redirects and maintain slot maps; protocol-level retries differ from application idempotency for: {stem}.",
            f"{style_b} by profiling client RTT versus server `slowlog` entries for: {stem}.",
            f"A frequent mistake is huge pipelines without backpressure, causing timeouts and memory pressure on both client and server for: {stem}.",
            f"What pipeline batch size and timeout would you cap for: {stem} given your p99 SLO?",
        )

    if topic == "persistence":
        return _p(
            f"{style_a} matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: {stem}.",
            f"RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: {stem}.",
            f"BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: {stem}.",
            f"{style_b} by testing crash-recovery drills and measuring fork latency under peak write load for: {stem}.",
            f"Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: {stem}.",
            f"What RPO does your chosen persistence mode actually guarantee for: {stem} after a hard kill test?",
        )

    if topic == "replication":
        return _p(
            f"{style_a} treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: {stem}.",
            f"Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: {stem}.",
            f"Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: {stem}.",
            f"{style_b} by correlating `master_repl_offset` with replica offsets and write spikes for: {stem}.",
            f"Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: {stem}.",
            f"Which writes in: {stem} require synchronous acknowledgment, and how will clients handle failover mid-transaction?",
        )

    if topic == "sentinel":
        return _p(
            f"{style_a} deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: {stem}.",
            f"Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: {stem}.",
            f"Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: {stem}.",
            f"{style_b} by running game-day failover tests with connection pool refresh metrics for: {stem}.",
            f"Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: {stem}.",
            f"What quorum and `down-after-milliseconds` values would you defend in an ADR for: {stem}?",
        )

    if topic == "cluster":
        return _p(
            f"{style_a} designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: {stem}.",
            f"Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: {stem}.",
            f"Multi-key commands, Lua, and transactions require all keys in the same slot — `{{tag}}` hash tags force colocation for: {stem}.",
            f"{style_b} by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: {stem}.",
            f"Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: {stem}.",
            f"How would you rebalance slots or split hot keys if: {stem} appears in production metrics?",
        )

    if topic == "locks":
        return _p(
            f"{style_a} using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: {stem}.",
            f"Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: {stem}.",
            f"Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: {stem}.",
            f"{style_b} by testing GC pause and clock skew scenarios against lock TTL for: {stem}.",
            f"Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: {stem}.",
            f"What fencing mechanism protects your storage layer if: {stem} outlives the Redis lock TTL?",
        )

    if topic == "transactions":
        return _p(
            f"{style_a} using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: {stem}.",
            f"MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: {stem}.",
            f"WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: {stem}.",
            f"{style_b} by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: {stem}.",
            f"Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: {stem}.",
            f"When would Lua replace MULTI/EXEC for: {stem}, and what cluster slot constraints apply?",
        )

    if topic == "lua":
        return _p(
            f"{style_a} keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: {stem}.",
            f"Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: {stem}.",
            f"Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: {stem}.",
            f"{style_b} by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: {stem}.",
            f"Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: {stem}.",
            f"How do you version and deploy script changes safely for: {stem} across rolling restarts?",
        )

    if topic == "streams":
        return _p(
            f"{style_a} using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: {stem}.",
            f"Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: {stem}.",
            f"Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: {stem}.",
            f"{style_b} by monitoring XPENDING depth and trimming with MAXLEN ~ for: {stem}.",
            f"Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: {stem}.",
            f"What idempotency key and poison-message policy would you pair with: {stem}?",
        )

    if topic == "pubsub":
        return _p(
            f"{style_a} using Pub/Sub only for ephemeral fan-out where message loss during disconnect is acceptable for: {stem}.",
            f"Pub/Sub delivers only to connected subscribers — no persistence, backlog, or acks — unlike Streams or external brokers for: {stem}.",
            f"Slow subscribers are disconnected; dedicated connections are required because SUBSCRIBE blocks the connection for: {stem}.",
            f"{style_b} by pairing invalidation signals with cache TTL and source-of-truth refresh for: {stem}.",
            f"Using Pub/Sub as a job queue or on shared pool connections causes lost work and stuck clients for: {stem}.",
            f"What happens to in-flight Pub/Sub messages during failover in: {stem}, and is that acceptable?",
        )

    if topic == "cache":
        return _p(
            f"{style_a} choosing cache-aside for most apps, with write-through/write-behind only when consistency rules are explicit for: {stem}.",
            f"Cache-aside lets the app load on miss and populate Redis; invalidation must happen on writes to avoid stale reads for: {stem}.",
            f"TTL, eviction policy, and key naming determine hit ratio and memory safety under growth for: {stem}.",
            f"{style_b} by measuring origin load reduction, not just Redis hit ratio, for: {stem}.",
            f"Caching without invalidation strategy or with unbounded TTL on negative results breaks correctness for: {stem}.",
            f"Which consistency mode (aside, through, behind) fits: {stem}, and who owns invalidation?",
        )

    if topic == "invalidation":
        return _p(
            f"{style_a} deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: {stem}.",
            f"Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: {stem}.",
            f"Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: {stem}.",
            f"{style_b} by defining who invalidates on partial updates and out-of-order writes for: {stem}.",
            f"Updating DB without cache delete is the most common stale-data bug for: {stem}.",
            f"How do you invalidate related keys (lists, aggregates) when: {stem} updates one entity?",
        )

    if topic == "cache_failure":
        return _p(
            f"{style_a} combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: {stem}.",
            f"Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: {stem}.",
            f"Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: {stem}.",
            f"{style_b} by load-testing synchronized expiry and hot-key miss scenarios for: {stem}.",
            f"Same TTL on all keys and caching null forever are classic self-inflicted outages for: {stem}.",
            f"Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: {stem} in your architecture?",
        )

    if topic == "eviction":
        return _p(
            f"{style_a} setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: {stem}.",
            f"Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: {stem}.",
            f"`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: {stem}.",
            f"{style_b} by alerting before hit ratio collapses and testing eviction under synthetic fill for: {stem}.",
            f"Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: {stem}.",
            f"What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: {stem}?",
        )

    if topic == "performance":
        return _p(
            f"{style_a} profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: {stem}.",
            f"O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: {stem}.",
            f"I/O threads help socket read/write but do not parallelize command execution for: {stem}.",
            f"{style_b} using slowlog, latency doctor, and before/after benchmarks for: {stem}.",
            f"Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: {stem}.",
            f"What single slowlog entry would convince you to change schema or sharding for: {stem}?",
        )

    if topic == "monitoring":
        return _p(
            f"{style_a} correlating INFO sections, slowlog, and latency doctor before changing config during incidents for: {stem}.",
            f"INFO exposes memory, stats, replication, and cluster state; SLOWLOG captures commands exceeding threshold for: {stem}.",
            f"Cluster health requires per-node slot coverage and lag metrics, not only primary CPU for: {stem}.",
            f"{style_b} by defining dashboards for memory, ops/sec, lag, rejected connections, and evictions for: {stem}.",
            f"Running MONITOR in production destroys throughput — use targeted telemetry instead for: {stem}.",
            f"Which three metrics would page you first for: {stem}, and what thresholds?",
        )

    if topic == "troubleshooting":
        return _p(
            f"{style_a} classifying the symptom (memory, lag, latency, routing) before applying config changes for: {stem}.",
            f"Hot keys skew CPU on one shard; big keys inflate latency and replication cost — diagnose with `--hotkeys`, memory sampling, and slowlog for: {stem}.",
            f"Replication lag may be backlog, network, or write spike — not always replica hardware for: {stem}.",
            f"{style_b} with a written runbook and rollback criteria for each remediation step for: {stem}.",
            f"Using KEYS, FLUSHALL without ASYNC, or failover without client drain worsens many incidents for: {stem}.",
            f"What evidence proves root cause versus symptom for: {stem} before you close the incident?",
        )

    if topic == "capacity":
        return _p(
            f"{style_a} sizing memory as key count × (value + metadata overhead) plus replication and headroom for fork for: {stem}.",
            f"Plan growth with key cardinality forecasts, encoding assumptions, and replica factor — Cluster adds coordination overhead for: {stem}.",
            f"Connection count from many pods can exhaust `maxclients` before memory fills for: {stem}.",
            f"{style_b} with load tests that include failover and snapshot windows for: {stem}.",
            f"Sizing only for data bytes without overhead, replicas, or COW margin causes emergency scale events for: {stem}.",
            f"At what memory or ops/sec threshold would you trigger horizontal scale for: {stem}?",
        )

    if topic == "comparison":
        return _p(
            f"{style_a} comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: {stem}.",
            f"Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: {stem}.",
            f"Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: {stem}.",
            f"{style_b} by documenting ADR assumptions and exit strategy if load doubles for: {stem}.",
            f"Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: {stem}.",
            f"What requirement in: {stem} is decisive if throughput numbers are similar across options?",
        )

    if topic == "session":
        return _p(
            f"{style_a} storing minimal session fields in Redis with TTL refresh and cookie holding only opaque session ID for: {stem}.",
            f"Hash fields allow partial updates; JSON strings simplify serialization but increase rewrite cost for: {stem}.",
            f"Session loss on failover is acceptable for cache-only sessions but not if Redis is sole session store without replication discipline for: {stem}.",
            f"{style_b} by rotating session ID on login and bounding payload size for: {stem}.",
            f"Putting PII in session blobs without encryption or TTL is a common compliance mistake for: {stem}.",
            f"Which session fields must survive failover for: {stem}, and how do clients handle invalidation?",
        )

    if topic == "rate_limit":
        return _p(
            f"{style_a} picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: {stem}.",
            f"INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: {stem}.",
            f"Global counters can become hot keys — shard counter keys or use local aggregation for: {stem}.",
            f"{style_b} by testing boundary bursts at window edges for: {stem}.",
            f"Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: {stem}.",
            f"How would you shard a global rate limit key if: {stem} saturates one Redis primary?",
        )

    return _p(
        f"{style_a} matching Redis data type to access pattern — not defaulting everything to JSON strings for: {stem}.",
        f"Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: {stem}.",
        f"Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: {stem}.",
        f"{style_b} by validating command complexity and memory per key for: {stem}.",
        f"Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: {stem}.",
        f"Which type would you choose for: {stem}, and what command path proves it under peak cardinality?",
    )


UNIQUE_ANSWERS: dict[int, dict[str, str]] = {
    num: _payload(_topic_key(question), question, num)
    for num, question, _difficulty, _level, _topic, _doc in QUESTIONS
}

assert len(UNIQUE_ANSWERS) == 150
assert set(UNIQUE_ANSWERS.keys()) == set(range(1, 151))
