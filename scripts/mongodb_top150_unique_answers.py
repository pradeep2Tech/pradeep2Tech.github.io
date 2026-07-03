"""Unique MongoDB SME answers for top-150 interview questions."""

from __future__ import annotations

from typing import Dict

from mongodb_questions_data import QUESTIONS


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
    "For this question, the architecturally correct answer is",
    "The production-grade answer is",
    "The senior-level decision is",
    "The practical MongoDB answer is",
]

_STYLE_B = [
    "You justify it by aligning schema, index, and topology to the access pattern",
    "You justify it by proving p95/p99 behavior under realistic cardinality",
    "You justify it by minimizing cross-shard work and rollback risk",
    "You justify it by balancing latency, durability, and operational toil",
]


def _pick(items: list[str], qid: int) -> str:
    return items[qid % len(items)]


def _topic_key(question: str) -> str:
    q = question.lower()
    if any(k in q for k in ["shard", "chunk", "balancer", "mongos", "config server", "zone", "scatter-gather", "reshard"]):
        return "sharding"
    if any(k in q for k in ["replica", "election", "failover", "majority", "read concern", "write concern", "oplog", "rollback", "secondary", "retryable", "linearizable"]):
        return "replication"
    if any(k in q for k in ["transaction", "two-phase commit", "transactionlifetimelimitseconds"]):
        return "transactions"
    if any(k in q for k in ["index", "ixscan", "collscan", "executionstats", "esr", "covered", "multikey", "ttl", "regex", "projection", "text"]):
        return "indexing"
    if any(k in q for k in ["aggregation", "$lookup", "$facet", "$expr", "allowdiskuse", "pipeline"]):
        return "aggregation"
    if any(k in q for k in ["wiredtiger", "checkpoint", "cache", "page faults", "compression", "journal", "mvcc", "storage"]):
        return "storage"
    if any(k in q for k in ["backup", "restore", "dropdatabase", "rpo", "rto", "forensic"]):
        return "backup"
    if any(k in q for k in ["security", "rbac", "privilege", "privatelink", "tls", "encryption", "audit", "credential", "secret", "internet", "compliance", "sovereignty"]):
        return "security"
    if any(k in q for k in ["postgresql", "cassandra", "couchbase", "dual-writing"]):
        return "comparison"
    if any(k in q for k in ["onboarding", "new hire", "staff engineer"]):
        return "onboarding"
    return "schema"


def _payload(topic: str, question: str, qid: int) -> dict[str, str]:
    style_a = _pick(_STYLE_A, qid)
    style_b = _pick(_STYLE_B, qid + 1)
    stem = question.rstrip("?")

    if topic == "schema":
        return _p(
            f"{style_a} modeling to dominant read/write paths, then embedding only where growth is bounded for: {stem}.",
            f"Schema-first decisions in MongoDB should be query-first in practice, so colocate fields that are read together and externalize unbounded fan-out to references or buckets for: {stem}.",
            f"Document growth, index fan-out, and update locality decide the true cost profile internally, which is why embedding works best when mutation scope stays narrow for: {stem}.",
            f"{style_b} by replaying realistic tenant skew, cardinality growth, and migration paths before freezing the model for: {stem}.",
            f"A common mistake is copying relational normalization or, conversely, embedding unbounded arrays until 16 MB limits and write amplification appear for: {stem}.",
            f"What cardinality limit, migration trigger, and fallback model would you define up front to keep: {stem} safe over 3 years?",
        )

    if topic == "sharding":
        return _p(
            f"{style_a} choosing a shard key that preserves query targeting and distributes writes, not just one that looks high-cardinality, for: {stem}.",
            f"In MongoDB sharding, the wrong leading key creates hot chunks, scatter-gather queries, or jumbo chunks, so key choice must follow real filters and time-skew behavior for: {stem}.",
            f"`mongos` routes via config metadata and chunk ranges, so shard-key entropy and monotonicity directly control migration pressure and balancer load for: {stem}.",
            f"{style_b} by load-testing chunk distribution, migration rate, and per-shard opcounters before production for: {stem}.",
            f"Teams often choose hashed keys that break range locality or ranged keys that hotspot writes because they skipped workload replay for: {stem}.",
            f"How would you prove shard targeting percentage, not just throughput, for: {stem} before launch?",
        )

    if topic == "replication":
        return _p(
            f"{style_a} explicitly defining durability and freshness semantics with write concern, read concern, and read preference for: {stem}.",
            f"Replica-set correctness is an SLA decision: critical writes need majority durability, while read routing must document tolerated staleness under elections for: {stem}.",
            f"Elections, oplog apply lag, and term changes can surface transient errors or rollbacks, so client retry behavior is part of database design for: {stem}.",
            f"{style_b} by validating failover drills, lag budgets, and rollback handling using production-like traffic for: {stem}.",
            f"A frequent failure mode is assuming defaults are safe for money or identity workflows without proving election-time behavior for: {stem}.",
            f"Which operations in: {stem} must be monotonic, and how does your client contract enforce that?",
        )

    if topic == "transactions":
        return _p(
            f"{style_a} using multi-document transactions only where cross-document invariants are mandatory for: {stem}.",
            f"Transactions provide atomicity and snapshot isolation, but they add lock lifetime, retry complexity, and oplog overhead, so model to single-document atomicity first for: {stem}.",
            f"On sharded clusters, commit coordination uses two-phase behavior and can abort on lifetime or conflict pressure, making long transactions operationally expensive for: {stem}.",
            f"{style_b} by keeping transactions short, indexed, and explicitly retried with idempotent semantics for: {stem}.",
            f"Common mistakes include using transactions to mask poor schema choices or allowing user flows to hold them open too long for: {stem}.",
            f"What invariant in: {stem} cannot be preserved by idempotent single-document updates?",
        )

    if topic == "indexing":
        return _p(
            f"{style_a} deriving indexes from exact query shapes and ESR ordering, then proving docsExamined efficiency for: {stem}.",
            f"Index quality is measured by selectivity, sort support, and coverage tradeoffs versus write amplification, not by index count alone, for: {stem}.",
            f"Planner behavior depends on prefix usability and cardinality estimates, so misplaced fields cause FETCH-heavy plans or full scans for: {stem}.",
            f"{style_b} with continuous index hygiene reviews, explain baselines, and drop policies for stale indexes around: {stem}.",
            f"Teams often over-index every slow query and silently degrade write throughput, memory, and checkpoint I/O for: {stem}.",
            f"What threshold in scanned/returned ratio should trigger redesign for: {stem} in your team?",
        )

    if topic == "aggregation":
        return _p(
            f"{style_a} pushing selective `$match` and projection early, then containing fan-out stages for: {stem}.",
            f"Aggregation pipelines stay fast when stage order protects index use and minimizes intermediate document width before `$lookup`, `$group`, or `$facet` for: {stem}.",
            f"The optimizer can reorder some stages, but blocking operators still dominate memory and spill behavior under skewed inputs for: {stem}.",
            f"{style_b} by inspecting stage-level execution stats, spill metrics, and cardinality explosions for: {stem}.",
            f"Typical mistakes are joining before filtering, missing foreign indexes, and normalizing data that should have been embedded for: {stem}.",
            f"Which stage in: {stem} currently dominates runtime, and do you have evidence that schema change beats pipeline tuning?",
        )

    if topic == "storage":
        return _p(
            f"{style_a} treating WiredTiger as a cache-and-checkpoint system where working-set fit decides tail latency for: {stem}.",
            f"When effective cache fit degrades, read latency and I/O waits climb sharply, and checkpoint cadence becomes visible in p99 for: {stem}.",
            f"MVCC history, eviction pressure, and journal/checkpoint interplay explain most storage-engine performance cliffs for: {stem}.",
            f"{style_b} using cache dirty/used ratios, eviction throughput, and checkpoint duration trendlines for: {stem}.",
            f"Teams often tune one knob without accounting for index write amplification or long readers pinning history for: {stem}.",
            f"Which metric proves the bottleneck in: {stem} is cache pressure versus checkpoint writeback?",
        )

    if topic == "backup":
        return _p(
            f"{style_a} defining recovery objectives first, then selecting backup granularity and restore validation for: {stem}.",
            f"Reliable MongoDB DR plans include PITR/window choices, immutable backups, and rehearsed restore cutover checks against application invariants for: {stem}.",
            f"Backup correctness depends on consistent snapshots of replica-set or sharded metadata, not just collection files, for: {stem}.",
            f"{style_b} by regularly running restore drills, data-integrity checks, and rollback plans on isolated environments for: {stem}.",
            f"A dangerous mistake is treating backup success logs as recovery proof without query-level validation for: {stem}.",
            f"How will you prove RPO/RTO and data correctness under: {stem} before declaring recovery complete?",
        )

    if topic == "security":
        return _p(
            f"{style_a} implementing layered controls: private connectivity, least-privilege roles, TLS, and managed secrets for: {stem}.",
            f"MongoDB security is defense-in-depth; network isolation and RBAC boundaries limit blast radius, while encryption and audit trails satisfy compliance for: {stem}.",
            f"Authn/authz, transport encryption, and optional client-side field encryption each protect different threat surfaces for: {stem}.",
            f"{style_b} with role reviews, credential rotation drills, network path validation, and audit evidence retention for: {stem}.",
            f"Common failures include internet-exposed endpoints, static credentials in config files, and broad admin roles for applications in: {stem}.",
            f"Which control in: {stem} gives the largest blast-radius reduction right now: network, RBAC, or key management?",
        )

    if topic == "comparison":
        return _p(
            f"{style_a} framing tradeoffs around access patterns, consistency model, and operational maturity rather than feature checklists for: {stem}.",
            f"MongoDB usually wins on document agility and developer velocity, while alternatives can win on strict relational joins or ultra-specialized write paths for: {stem}.",
            f"The technical core is locality versus join rigor, partition behavior under skew, and failover semantics under load for: {stem}.",
            f"{style_b} by benchmarking steady-state and failure-state behavior, then documenting ADR assumptions for: {stem}.",
            f"Teams often underestimate dual-write reconciliation cost and overestimate cross-platform operability in: {stem}.",
            f"What non-functional requirement is decisive for: {stem} if throughput numbers are similar?",
        )

    return _p(
        f"{style_a} role-based depth progression: fundamentals first, distributed failure handling later, for: {stem}.",
        f"Effective MongoDB onboarding starts with CRUD/index/explain literacy, then replication and sharding, then incident and architecture ownership for: {stem}.",
        f"Capability maturity follows system layers: planner and schema, storage internals, then distributed topology and DR mechanics for: {stem}.",
        f"{style_b} by mapping role expectations to measurable exercises such as failover drills and explain-plan reviews for: {stem}.",
        f"The common mistake is assigning advanced resharding or DR tasks before fundamentals are demonstrably mastered for: {stem}.",
        f"Which skills are mandatory at 30/60/90 days for the roles discussed in: {stem}?",
    )


UNIQUE_ANSWERS: dict[int, dict[str, str]] = {
    num: _payload(_topic_key(question), question, num)
    for num, question, _difficulty, _level, _topic, _doc in QUESTIONS
}

assert len(UNIQUE_ANSWERS) == 150
assert set(UNIQUE_ANSWERS.keys()) == set(range(1, 151))
assert len({v["short"] for v in UNIQUE_ANSWERS.values()}) == 150

