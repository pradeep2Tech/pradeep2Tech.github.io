"""MongoDB answer engine for top-150 interview questions."""

from __future__ import annotations

import re
from typing import Callable, Dict

from mongodb_questions_data import QUESTIONS
from mongodb_top150_unique_answers import UNIQUE_ANSWERS

SECTIONS = ("short", "detailed", "internal", "production", "mistakes", "followup")


def slug_anchor(question: str) -> str:
    """Create Hugo-friendly heading anchors."""
    base = question.lower().strip()
    base = re.sub(r"[^\w\s-]", "", base)
    base = re.sub(r"[\s_]+", "-", base)
    base = re.sub(r"-{2,}", "-", base).strip("-")
    return base[:80].rstrip("-")


def format_answer_block(question: str, sections: dict) -> str:
    """Format one answer block in markdown."""
    return (
        f"## {question}\n\n"
        f"### Short Answer\n{sections['short']}\n\n"
        f"### Detailed Explanation\n{sections['detailed']}\n\n"
        f"### Internal Working\n{sections['internal']}\n\n"
        f"### Production Notes\n{sections['production']}\n\n"
        f"### Common Mistakes\n{sections['mistakes']}\n\n"
        f"### Follow-up Questions\n{sections['followup']}\n\n"
        "---\n"
    )


def _pack(
    short: str,
    detailed: str,
    internal: str,
    production: str,
    mistakes: str,
    followup: str,
) -> Dict[str, str]:
    return {
        "short": short,
        "detailed": detailed,
        "internal": internal,
        "production": production,
        "mistakes": mistakes,
        "followup": followup,
    }


def _topic_default(question: str, topic: str) -> Dict[str, str]:
    return _pack(
        short=f"For this {topic.lower()} scenario, optimize for the dominant access pattern and failover behavior, not for schema aesthetics.",
        detailed=f"Start from query shape, write/read ratio, and consistency target, then choose schema, index, and topology accordingly. In MongoDB, the right answer is usually the one that minimizes cross-shard work and reduces surprise under failover.",
        internal="MongoDB execution cost is driven by index selectivity, shard targeting, replication acknowledgment, and WiredTiger cache behavior. Designs that align with these internals keep latency predictable at scale.",
        production="Validate with `explain('executionStats')`, oplog/lag metrics, and workload replay before rollout. Treat p95/p99, replication lag, and chunk distribution as release gates.",
        mistakes="Teams often tune one query while ignoring write amplification, balancer effects, or read-freshness SLAs. Another common miss is trusting lab benchmarks without realistic cardinality and tenant skew.",
        followup=f"Which query shapes dominate for this question, and what does that imply for index order, shard targeting, and read/write concerns?",
    )


def _schema_modeling(question: str) -> Dict[str, str]:
    return _pack(
        short="Use embedding for high-locality reads and bounded growth; use references when cardinality is unbounded or update isolation matters.",
        detailed="MongoDB schema design should be query-first: colocate fields read together and avoid joins in hot paths. Move to references when arrays grow without bound, update contention rises, or document size risks the 16 MB cap.",
        internal="Each update rewrites document regions and updates all affected indexes, so oversized or frequently mutating embedded arrays increase write amplification. `$lookup` can recover normalized relationships, but it is still heavier than single-document reads.",
        production="Track document size percentile, array cardinality growth, and `$lookup` latency over time. Introduce bucketing/versioning before size or fan-out cliffs force urgent migrations.",
        mistakes="Over-normalizing from relational habits causes frequent `$lookup` and extra network hops. The opposite error is embedding endlessly growing event histories into one document.",
        followup="What is the expected max cardinality per parent entity, and how will you migrate if that bound is exceeded?",
    )


def _sharding(question: str) -> Dict[str, str]:
    return _pack(
        short="Pick a shard key with high cardinality, good write distribution, and query targeting; monotonic keys usually create hotspots.",
        detailed="Shard keys must satisfy both distribution and routing. Hashed keys smooth writes but hurt range locality; ranged/compound keys support range queries but can hot-spot if the leading dimension is monotonic.",
        internal="`mongos` targets shards using config metadata and chunk ranges. Poor keys trigger scatter-gather, jumbo chunks, and frequent migrations, which increase latency and balancer pressure.",
        production="Validate with synthetic skew and tenant-heavy workloads before cutover, then watch chunk imbalance, jumbo flags, and per-shard op counters. Use zones for residency/compliance and workload isolation where required.",
        mistakes="Choosing a shard key from a single happy-path query often fails once new filters appear. Teams also ignore unique-index constraints on sharded collections until late in the lifecycle.",
        followup="How would you prove shard targeting rate and write distribution before production, and what is your resharding trigger?",
    )


def _replication_reliability(question: str) -> Dict[str, str]:
    return _pack(
        short="Durability depends on write concern and election behavior; reliability designs should tolerate primary loss without ambiguous commits.",
        detailed="Use `w: 'majority'` for state that cannot be lost and align read concern with freshness requirements. Model failover paths explicitly so clients retry safely and can distinguish retryable errors from rolled-back writes.",
        internal="Secondaries replicate from the oplog and apply operations asynchronously; elections pick a new primary based on term, optime, and votes. Reads/writes around term changes can see transient errors unless client retry semantics are correct.",
        production="Define SLOs for replication lag, election time, and rollback risk, then validate them through controlled failover tests. Keep oplog window comfortably above maintenance and incident recovery duration.",
        mistakes="Relying on default write concern for critical flows is a common data-loss risk. Another mistake is using secondary reads without documenting acceptable staleness windows.",
        followup="Which operations require majority durability, and how does your client retry policy handle step-down and transient network partitions?",
    )


def _transactions(question: str) -> Dict[str, str]:
    return _pack(
        short="Use multi-document transactions only where cross-document invariants are mandatory; otherwise prefer idempotent single-document patterns.",
        detailed="MongoDB transactions provide snapshot isolation and atomicity across documents, but they increase latency, lock lifetime, and oplog overhead. For high-throughput domains, model data to keep the critical path in single-document atomic updates where possible.",
        internal="A transaction tracks read/write sets, may involve two-phase commit on sharded clusters, and can abort on lifetime or write conflict limits. Long transactions pin history and increase cache/replication pressure.",
        production="Keep transactions short, index all predicates, and monitor abort reasons (`WriteConflict`, timeout, transient errors). Reserve them for correctness-critical boundaries such as financial invariants.",
        mistakes="Using transactions to compensate for weak schema modeling creates fragile performance. Another frequent issue is creating collections/indexes inside active transactions in environments that disallow it.",
        followup="What invariant actually requires a transaction here, and can you redesign to preserve correctness with idempotent atomic updates instead?",
    )


def _indexing_perf(question: str) -> Dict[str, str]:
    return _pack(
        short="Design indexes from real query shapes using ESR ordering and coverage goals, then verify with `executionStats`.",
        detailed="Good index strategy balances read latency against write amplification. Compound indexes should start with equality filters, then sort keys, then range predicates; covered queries further reduce document fetch cost.",
        internal="Planner choices depend on cardinality estimates, index prefix usability, and sort compatibility. When no efficient path exists, plans degrade to COLLSCAN or expensive FETCH stages.",
        production="Continuously review index usage, scanned/returned ratios, and index size growth. Drop dead indexes and gate new indexes through replay-based validation on production-like data.",
        mistakes="Adding indexes reactively for every slow query leads to write-heavy, memory-heavy clusters. Teams also misread explain output by focusing only on winning plan name and not docs examined.",
        followup="What is the docsExamined-to-nReturned threshold your team treats as unacceptable for this workload?",
    )


def _agg_lookup(question: str) -> Dict[str, str]:
    return _pack(
        short="Aggregation performs best when selective `$match` stages run early and `$lookup` joins are index-supported on the foreign side.",
        detailed="Push filters/projections before fan-out stages and avoid carrying wide documents through the pipeline. Use `$lookup` intentionally for bounded joins; if it dominates critical latency, re-evaluate schema locality.",
        internal="Pipeline optimization can reorder some stages, but index use still depends on stage shape and field availability. Blocking stages (`$sort`, `$group`, `$facet`) consume memory and may spill when limits are exceeded.",
        production="Inspect stage-level execution stats and memory spill behavior under representative cardinality. `allowDiskUse` is acceptable for controlled analytics paths, not for core transactional APIs.",
        mistakes="Putting `$lookup` or `$unwind` before selective filters inflates intermediate sets dramatically. Another miss is lacking indexes on `localField/foreignField` join paths.",
        followup="Which pipeline stage dominates runtime now, and what evidence shows whether schema change beats further pipeline tuning?",
    )


def _troubleshooting_ops(question: str) -> Dict[str, str]:
    return _pack(
        short="Use a structured triage path: isolate symptom domain (query, replication, storage, routing) before changing config.",
        detailed="Correlate application latency, MongoDB server metrics, and recent deploy/config events to localize the fault. Most incidents are resolved faster when you prove whether the bottleneck is CPU, I/O, lock contention, or network/pathing.",
        internal="MongoDB exposes signal through profiler, `currentOp`, oplog lag, balancer state, and WiredTiger cache counters. Correct diagnosis comes from joining these signals rather than trusting a single metric spike.",
        production="Capture an incident timeline, preserve forensic artifacts, and run minimally invasive diagnostics first. Use guarded operational actions (killOp, stepDown, resync, balancer changes) with rollback conditions documented.",
        mistakes="Shotgunning index/config changes during active incidents often increases blast radius. Teams also skip post-incident validation and reintroduce the same failure mode later.",
        followup="What evidence definitively isolates the bottleneck layer, and which reversible mitigation buys the most risk reduction in the next 30 minutes?",
    )


def _security(question: str) -> Dict[str, str]:
    return _pack(
        short="Secure MongoDB with layered controls: network isolation, strong authz, TLS everywhere, and auditable credential handling.",
        detailed="Treat database security as defense-in-depth: private connectivity, least-privilege roles, encryption in transit/at rest, and rotation workflows. For regulated workloads, add auditability and key management boundaries that map to compliance controls.",
        internal="Authorization is role-based at database/collection granularity, while transport security relies on TLS handshake and certificate validation. Features like CSFLE shift trust boundaries by encrypting sensitive fields client-side before write.",
        production="Use short-lived credentials where possible, central secret managers, and automated rotation with dual credential overlap. Validate security posture with periodic role reviews, network path tests, and audit log checks.",
        mistakes="Relying on IP allowlists alone is insufficient against credential misuse and lateral movement. Another common error is embedding static credentials in app configs and CI variables.",
        followup="Which control is your primary blast-radius reducer here: network isolation, RBAC hardening, key management, or client-side encryption?",
    )


def _storage_engine(question: str) -> Dict[str, str]:
    return _pack(
        short="WiredTiger performance is governed by cache fit, checkpoint behavior, and write amplification from indexes/document churn.",
        detailed="When working set exceeds effective cache, read latency and I/O wait rise sharply. Checkpoint and eviction dynamics can create periodic stalls if write volume, compression, and index fan-out are not balanced.",
        internal="WiredTiger uses MVCC with history store and periodic checkpoints; long-running readers/transactions can pin history and grow cache pressure. Journal and checkpoint paths trade durability guarantees against I/O intensity.",
        production="Track cache dirty/used ratios, eviction throughput, and checkpoint timing alongside p99 latency. Capacity plans must include data, indexes, oplog, and growth margin, not collection bytes alone.",
        mistakes="Treating memory as a static knob without workload replay misses temporal spikes and history-store amplification. Teams also underestimate the disk impact of index-heavy schemas on write paths.",
        followup="Is your current bottleneck cache miss, checkpoint I/O, or index write amplification, and which metric proves it?",
    )


def _comparisons(question: str) -> Dict[str, str]:
    return _pack(
        short="Choose MongoDB when flexible document modeling and developer velocity outweigh strict relational constraints for the workload.",
        detailed="Platform comparisons should be tied to access patterns, consistency semantics, operational skillset, and scaling model. MongoDB excels at hierarchical JSON data and rapid schema evolution; alternatives may win for strict joins, extreme write-only time series, or specialized cache-first patterns.",
        internal="The tradeoff is between document locality and join rigor, plus replication/sharding semantics versus each competitor's partitioning model. Architecture reviews should quantify failure behavior, migration cost, and observability maturity across options.",
        production="Run benchmark scenarios that include failover, backup/restore, and operational toil, not only steady-state throughput. ADRs should record non-functional constraints and exit strategy if assumptions fail.",
        mistakes="Debates often stay at feature checklists and ignore team capability, incident response maturity, and data lifecycle policy. Another trap is dual-write architectures without explicit reconciliation ownership.",
        followup="Which non-functional requirement is decisive here: consistency guarantees, scaling envelope, operational cost, or ecosystem integration?",
    )


def _learning_paths(question: str) -> Dict[str, str]:
    return _pack(
        short="New hires should master CRUD, indexing basics, and replication behavior first; senior staff should focus on sharding, incidents, and architecture tradeoffs.",
        detailed="Onboarding should sequence fundamentals before distributed-system complexity. Staff-level progression adds capacity planning, failure-mode design, and cross-database decision-making under real production constraints.",
        internal="Skill depth maps to system layers: query planner and schema first, then storage/replication internals, then sharding and organizational runbooks. This staged model reduces cognitive overload and improves operational readiness.",
        production="Use role-specific learning paths tied to incident simulations and design reviews, not only reading lists. Evidence of readiness should include explain-plan analysis, failover drills, and shard-key ADR critiques.",
        mistakes="A common mistake is exposing junior engineers to resharding and DR design before they can reason about index and query fundamentals. The opposite error is keeping seniors on only CRUD-level material.",
        followup="Which capabilities are mandatory for each role in the first 30, 60, and 90 days?",
    )


INTENT_RULES: list[tuple[str, Callable[[str], Dict[str, str]]]] = [
    (r"(embed|embedding|schema|document model|variant|polymorphism|cqrs|view|materialized)", _schema_modeling),
    (r"(shard|chunk|balancer|reshard|zone|scatter-gather|mongos|config server|hot shard)", _sharding),
    (r"(replica|election|failover|majority|readConcern|write concern|oplog|rollback|secondary|retryable writes|linearizable)", _replication_reliability),
    (r"(transaction|two-phase commit|transactionLifetimeLimitSeconds|write conflict|snapshot)", _transactions),
    (r"(index|ixscan|collscan|covered|esr|executionstats|explain|regex|multikey|ttl)", _indexing_perf),
    (r"(aggregation|\$lookup|\$facet|\$expr|allowDiskUse|pipeline)", _agg_lookup),
    (r"(wiredtiger|checkpoint|cache|page faults|compression|journal|mvcc|storage)", _storage_engine),
    (r"(triage|troubleshoot|runbook|currentOp|mongodb\+srv|dns|oom|incident|restore|backup|dropDatabase|stuck)", _troubleshooting_ops),
    (r"(security|rbac|privilege|privatelink|tls|encryption|audit|credential|secret|internet|compliance|sovereignty)", _security),
    (r"(postgresql|cassandra|couchbase|dual-writing|comparison|review board)", _comparisons),
    (r"(new hire|onboarding|learning path|staff engineer)", _learning_paths),
]


def _intent_answer(question: str, topic: str) -> Dict[str, str]:
    q = question.lower()
    for pattern, handler in INTENT_RULES:
        if re.search(pattern, q):
            return handler(question)
    return _topic_default(question, topic)


ANSWERS: Dict[int, Dict[str, str]] = dict(UNIQUE_ANSWERS)

if len(ANSWERS) != 150:
    raise RuntimeError(f"Expected 150 answers, found {len(ANSWERS)}")


def craft_answer(num: int, question: str, topic: str, doc: str) -> dict:
    """Return a structured answer for one interview question."""
    if num in ANSWERS:
        return ANSWERS[num]
    return _intent_answer(question, topic)


__all__ = ["ANSWERS", "QUESTIONS", "craft_answer", "format_answer_block", "slug_anchor"]
