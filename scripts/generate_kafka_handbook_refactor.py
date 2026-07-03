"""Generate refactored Kafka handbook content files."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "kafka-handbook"
DATE = "2026-07-03T10:00:00+00:00"

FM = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
ShowToc: true
interviewHandbook: true
---

"""


def w(rel: str, body: str, **fm):
    path = HB / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        FM.format(date=DATE, **fm) + body.strip() + "\n",
        encoding="utf-8",
    )


# --- Section indexes ---
for folder, title, desc in [
    ("01-fundamentals", "Fundamentals", "Messaging patterns, models, and broker selection for senior engineers."),
    ("02-kafka", "Apache Kafka", "Core Kafka concepts through operations and troubleshooting."),
    ("03-broker-comparisons", "Broker Comparisons", "Architect-level comparison matrices."),
    ("04-interview-guide", "Interview Guide", "Question banks mapped to handbook topics."),
]:
    w(
        f"{folder}/_index.md",
        f"# {title}\n\n{desc}\n",
        title=title,
        desc=desc,
        short=title,
        mod=1,
        mod_title="Kafka Handbook",
        ref="0",
        weight=1,
    )

w(
    "_index.md",
    """# Kafka Handbook

Interview-first knowledge base for **Senior Engineers**, **Leads**, and **Architects** (6+ years).

## Learning Paths

| Track | Start here | Goal |
| :--- | :--- | :--- |
| **Quick revision** | [Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/) → [Kafka Core](/kafka-handbook/02-kafka/kafka-core/) | 30-minute refresh before interviews |
| **Senior engineer** | [Fundamentals](/kafka-handbook/01-fundamentals/) → [Kafka](/kafka-handbook/02-kafka/) | Production-ready producer/consumer design |
| **Architect** | [Broker Selection](/kafka-handbook/01-fundamentals/broker-selection-guide/) → [Comparisons](/kafka-handbook/03-broker-comparisons/) | ADRs, multi-broker platforms, cloud trade-offs |
| **Interview prep** | [Top 150 Questions](/kafka-handbook/04-interview-guide/top-150-interview-questions/) | Role-specific question banks |

## Modules

1. **Fundamentals** — patterns, models, queue-vs-stream, selection ADRs
2. **Apache Kafka** — core, internals, performance, security, operations, troubleshooting
3. **Broker Comparisons** — RabbitMQ, Pulsar, NATS, Redpanda, managed cloud messaging
4. **Interview Guide** — 150-question bank plus architect, troubleshooting, and trade-off lists

See also: [How to Choose a Message Broker](/technology-playbook/how-to-choose-message-broker/) · [Event-Driven Architecture](/microservices/event-driven-architecture-log-streaming/)
""",
    title="Kafka Handbook",
    desc="Kafka and enterprise messaging — interview-first handbook for senior engineers and architects.",
    short="Handbook",
    mod=0,
    mod_title="Kafka Handbook",
    ref="0",
    weight=1,
)

# --- 01 Fundamentals ---
w(
    "01-fundamentals/messaging-patterns.md",
    """## Quick Revision

- **Point-to-point**: one consumer per message (queue semantics).
- **Pub/sub**: many subscribers; Kafka uses consumer groups for scale-out consumption.
- **Event-driven**: services react to facts; temporal decoupling is the default.
- **Request/reply**: possible over Kafka (reply topic + correlation ID) but not the sweet spot.

## Core Concepts

| Pattern | Mechanism | Kafka fit |
| :--- | :--- | :--- |
| Fire-and-forget notify | Topic publish | Strong |
| Work queue | Competing consumers in one group | Strong |
| Fan-out analytics | Multiple consumer groups | Strong |
| RPC / command | Request-reply, low latency | Weak unless isolated |
| Saga / choreography | Event chains + idempotency | Strong with design discipline |

## Internal Working

Patterns map to **topics + partitions + consumer groups**. A group is a scaled consumer pool; each partition is consumed by at most one member per group at a time.

## Architecture

```mermaid
flowchart LR
  producer[Order Service] --> topic[(orders.events)]
  topic --> g1[Inventory Group]
  topic --> g2[Analytics Group]
  topic --> g3[Audit Group]
```

## Design Tradeoffs

| Choice | Upside | Downside |
| :--- | :--- | :--- |
| Async events | Scale, resilience | Harder debugging |
| Sync REST | Simple traces | Tight coupling |
| Hybrid | Right tool per flow | More platforms to operate |

## Production Patterns

- Isolate **real-time** and **batch** paths with separate consumer groups on the same topic.
- Propagate **trace context** in headers on every publish.
- Design **idempotent** handlers with business keys (`orderId`, `paymentId`).

## Scalability

Fan-out scales by adding consumer group members up to partition count per group.

## Reliability

Assume **at-least-once** delivery; retries are normal. Compensate with idempotent consumers and DLQ topics.

## Security

Topic-level ACLs per consumer group in regulated domains.

## Observability

Lag per group, produce/fetch latency, error rate per handler.

## Troubleshooting

Poison messages block partition progress — route to DLT and skip or fix offset with a runbook.

## Common Mistakes

- One consumer group shared across unrelated microservices.
- Using messaging for synchronous consistency without sagas.

## Interview Questions

- Why does event-driven architecture complicate end-to-end debugging?
- When is point-to-point still the right pattern inside Kafka?
- How do multiple consumer groups differ from SNS fan-out?

## Architect Notes

Enterprises run **hybrid** platforms: Kafka for event backbone, queues for task routing. Document the boundary in your integration ADR.
""",
    title="Messaging Patterns",
    desc="Point-to-point, pub/sub, event-driven, and request-reply patterns in production systems.",
    short="Patterns",
    mod=1,
    mod_title="Fundamentals",
    ref="1.1",
    weight=101,
)

w(
    "01-fundamentals/messaging-models.md",
    """## Quick Revision

- **Queue mental model**: message removed after ack; work distribution.
- **Log mental model**: append-only, retained, replayable; consumers track offsets.
- **Stream processing**: continuous consumption over the log.
- **Broker vs log**: RabbitMQ routes to queues; Kafka appends to partitions.

## Core Concepts

| Model | State | Consumer progress |
| :--- | :--- | :--- |
| Classic queue | Ephemeral per queue | Ack removes message |
| Durable log | Retained by policy | Offset per group |
| Stream table | Compacted changelog | Latest key wins |
| Cloud queue (SQS) | Managed, limited retention | Visibility timeout |

## Internal Working

Kafka brokers assign **monotonic offsets** per partition. Consumer groups commit offsets to `__consumer_offsets` (internal compacted topic).

## Architecture

Brokers are **dumb logs, smart clients** — routing and batching logic lives in producers/consumers and client libraries.

## Design Tradeoffs

| Dimension | Queue | Log |
| :--- | :--- | :--- |
| Replay | Manual / DLQ | Native offset reset |
| Retention | Until ack | Time or compaction |
| Fan-out | Bindings / topics | Consumer groups |
| Ops focus | Broker HA | Partitions + ISR |

## Production Patterns

- Pick log semantics when events are a **durable product asset** (analytics, audit, CDC).
- Pick queue semantics for **task ladders** (retry TTL, priority routing).

## Scalability

Logs scale via partition count; queues scale via competing consumers (with ordering trade-offs).

## Reliability

Define delivery semantics explicitly: at-most-once, at-least-once, exactly-once (usually bounded to Kafka pipeline, not end-to-end DB).

## Security

Encryption in transit mandatory; consider payload encryption for PII fields in shared clusters.

## Observability

Model-specific metrics: queue **depth** vs Kafka **consumer lag**.

## Troubleshooting

Misaligned mental model causes teams to expect queue behavior (message disappearance) from a retained log.

## Common Mistakes

- Treating Kafka like a job queue without retention planning.
- Expecting global ordering on a distributed log.

## Interview Questions

- Why is Kafka described as a commit log rather than a message queue?
- How does offset-based progress differ from per-message acknowledgement?
- When does a cloud managed queue replace a self-hosted log?

## Architect Notes

Align stakeholders on **mental model** before technology selection — most integration failures are expectation mismatches.
""",
    title="Messaging Models",
    desc="Queue versus log mental models, offsets, and consumer progress.",
    short="Models",
    mod=1,
    mod_title="Fundamentals",
    ref="1.2",
    weight=102,
)

w(
    "01-fundamentals/queue-vs-stream.md",
    """## Quick Revision

- **Queue**: compete for messages; typically delete on ack.
- **Stream/log**: append, retain, replay; partition-scoped ordering.
- **Throughput**: logs win at extreme fan-out and replay.
- **Routing**: queues win on flexible AMQP-style bindings.

## Core Concepts

{{< comparison-table caption="Queue vs stream — architect view" >}}
| Dimension | Queue (AMQP/SQS) | Stream (Kafka) |
| :--- | :--- | :--- |
| Throughput | High | Very high with batching |
| Latency | Low per message | Tunable; batching adds tail latency |
| Ordering | Per queue (single consumer) | Per partition |
| Replay | DLQ / manual | Offset reset |
| Retention | Short / until ack | Days to forever (compacted) |
| Multi-subscriber | Exchanges / SNS fan-out | Consumer groups |
| Ops complexity | Moderate | Higher (partitions, ISR, rebalance) |
{{< /comparison-table >}}

## Internal Working

Streams use **partition leaders + ISR replication**. Queues use **broker routing tables** and per-queue ack state.

## Architecture

Use streams as **system of record for events**; use queues as **work distributors** with complex routing.

## Design Tradeoffs

Hybrid architectures are normal: Kafka for `OrderPlaced` fan-out; RabbitMQ for payment retry ladders.

## Production Patterns

- Partition keys: `customerId`, `orderId` — never random UUID when order matters.
- DLQ + replay runbooks on both models.

## Scalability

Stream scale ceiling = partitions × broker I/O. Queue scale = consumers × broker capacity.

## Reliability

At-least-once + idempotent consumers on both sides.

## Security

Managed queues reduce ops burden but limit replay and fine-grained ACL models.

## Observability

Queue depth alerts vs Kafka lag alerts — different SLOs.

## Troubleshooting

| Symptom | Queue likely cause | Stream likely cause |
| :--- | :--- | :--- |
| Backlog | Slow workers | Lag / hot partition |
| Duplicates | Redelivery after visibility timeout | Rebalance / retry |
| Lost messages | Ack before process | acks=1 + leader failure |

## Common Mistakes

- Forcing one broker for all integration shapes.
- Using RabbitMQ as analytics source of truth without retention.

## Interview Questions

- Why is global ordering expensive on a stream platform?
- When would you choose retention over disappearance after ack?
- How does replay change incident response for downstream bugs?

## Architect Notes

Document **which flows are log-shaped vs queue-shaped** in your platform map — interviewers probe hybrid fluency.
""",
    title="Queue vs Stream",
    desc="Architect comparison of queue and log/stream messaging semantics.",
    short="Queue vs Stream",
    mod=1,
    mod_title="Fundamentals",
    ref="1.3",
    weight=103,
)

w(
    "01-fundamentals/broker-selection-guide.md",
    """## Quick Revision

- Choose by **integration shape**, not logo preference.
- High-volume fan-out + replay → Kafka family.
- Task routing + priority → RabbitMQ / AMQP.
- No broker ops team → managed cloud messaging.
- Multi-tenant geo replication → evaluate Pulsar.

## Core Concepts

| Need | Primary candidates |
| :--- | :--- |
| Event backbone | Kafka, Redpanda, Pulsar |
| Task queue | RabbitMQ, SQS |
| GCP native | Pub/Sub |
| Azure integration | Event Hubs (Kafka API), Service Bus |
| Edge / low latency | NATS |
| Legacy JMS | ActiveMQ, IBM MQ |

## Internal Working

Selection ADR should capture: volume, ordering, replay, ops staffing, cloud strategy, cost model.

## Architecture

```mermaid
flowchart TD
  req[Requirements] --> vol{Volume and fan-out?}
  vol -->|High + replay| log[Kafka / Pulsar / Redpanda]
  vol -->|Task queue| queue[RabbitMQ / SQS]
  vol -->|Cloud native| cloud[Pub/Sub / Event Hubs / Service Bus]
```

## Design Tradeoffs

| Factor | Self-hosted Kafka | Managed MSK/Event Hubs | SQS/Pub/Sub |
| :--- | :--- | :--- | :--- |
| Control | Full | Partial | Low |
| Ops load | High | Medium | Low |
| Replay | Full | Varies | Limited |
| Cost at scale | TCO staffing | Per-unit + ops | Per-request |

## Production Patterns

- Run **proof-of-load** before Black Friday — partition count is hard to reduce safely.
- Require **schema registry** or contract tests for shared topics.

## Scalability

Staff for **partition planning** and **consumer group operations** if you pick Kafka.

## Reliability

`min.insync.replicas` + `acks=all` for durability-critical topics.

## Security

Mutual TLS and ACLs for multi-team clusters.

## Observability

Define lag SLOs and ISR shrink alerts before go-live.

## Troubleshooting

Wrong broker choice shows up as fighting the platform (replay hacks on queues, routing hacks on Kafka).

## Common Mistakes

- Selecting Kafka without hiring/contracting for ops.
- Ignoring ordering requirements until production.

## Interview Questions

- What team capabilities must exist before self-hosted Kafka?
- When is managed cloud messaging preferable despite less control?
- How would you justify a hybrid Kafka + RabbitMQ platform?

## Architect Notes

See [Broker Comparisons](/kafka-handbook/03-broker-comparisons/) for per-technology matrices. Link ADRs from [Technology Playbook](/technology-playbook/how-to-choose-message-broker/).
""",
    title="Broker Selection Guide",
    desc="ADR framework for choosing Kafka, queues, and managed cloud messaging.",
    short="Selection Guide",
    mod=1,
    mod_title="Fundamentals",
    ref="1.4",
    weight=104,
)

# --- 02 Kafka ---
KAFKA_FILES = {
    "kafka-core.md": (
        "Kafka Core",
        "Core",
        "Topics, partitions, producers, consumers, groups, and delivery semantics.",
        "2.1",
        201,
        """## Quick Revision

- Distributed **commit log**: producers append, consumers pull by offset.
- **Topics** split into **partitions** for parallelism and ordering scope.
- **Consumer groups**: scale-out consumption; one consumer per partition per group.
- **At-least-once** default; idempotent consumers required.

## Core Concepts

| Concept | Role |
| :--- | :--- |
| Topic | Named log category |
| Partition | Ordered, immutable sequence |
| Offset | Position in partition log |
| Producer | Appends with optional key |
| Consumer group | Cooperative partition assignees |
| Leader / ISR | Write path durability |

## Internal Working

Partition = ordered log on disk. **Leader** handles reads/writes; **ISR** replicas catch up. **High watermark** = offset replicated to all ISR.

## Architecture

```mermaid
flowchart LR
  P[Producers] --> B[Broker Cluster]
  B --> G1[Group: Inventory]
  B --> G2[Group: Analytics]
```

## Design Tradeoffs

| Setting | Effect |
| :--- | :--- |
| `acks=0` | Fastest; may lose data |
| `acks=1` | Leader ack; ISR lag risk |
| `acks=all` | Durable; higher latency |
| More partitions | Throughput ↑; ordering scope ↓ |

## Production Patterns

- **Order placed** event → inventory, payment, email, fraud in parallel via separate groups.
- **Batch reconciliation** reads same topic with isolated group and higher lag tolerance.
- Business-key idempotency: `orderId` dedupe store.

## Scalability

Max consumers per group ≤ partition count. Size partitions for **peak**, not average.

## Reliability

Poison messages → **dead-letter topic** + alerting. Schema drift → **schema registry** + contract tests.

## Security

ACLs per topic and group; no PII in topic names.

## Observability

Consumer lag, produce/fetch p99, offline partitions.

## Troubleshooting

Single hot partition → bad partition key. See [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting/).

## Common Mistakes

- Random UUID partition keys.
- Committing offset before side effects complete.

## Interview Questions

- Why partitions instead of a single queue?
- What does at-least-once imply for consumer design?
- How do separate consumer groups enable fan-out?

## Architect Notes

Kafka fits when events are a **first-class asset** — analytics, audit, replay, CDC. See [Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/).
""",
    ),
    "kafka-internals.md": (
        "Kafka Internals",
        "Internals",
        "Log segments, replication, ISR, leader election, and offset storage.",
        "2.2",
        202,
        """## Quick Revision

- Messages stored in **log segments** (`.log`, `.index`, `.timeindex`).
- **ISR** = replicas caught up to leader; shrink reduces durability window.
- Offsets committed to internal **`__consumer_offsets`** topic.
- **Rebalance** redistributes partitions on group membership change.

## Core Concepts

| Component | Function |
| :--- | :--- |
| Log segment | Rolling append file |
| Sparse index | Offset → byte position |
| Controller | Partition leadership |
| KRaft / ZK | Cluster metadata quorum |
| High watermark | Readable upper bound |

## Internal Working

**Write path**: hash(key) % partitions → leader append → replicate to ISR → respond per `acks`. **Read path**: long-poll fetch up to HW.

**Unclean leader election**: non-ISR broker becomes leader → **data loss** risk for un-replicated records.

## Architecture

Sequential disk writes + OS **page cache** = high throughput. Recent data often served from memory.

## Design Tradeoffs

| Choice | Trade-off |
| :--- | :--- |
| `unclean.leader.election.enable=false` | Safer; availability hit on ISR loss |
| Log compaction | Keyed changelog; tombstone lag |
| RF=3 + rack awareness | AZ fault tolerance vs cost |

## Production Patterns

- `min.insync.replicas=2` with `acks=all` for critical topics.
- Cooperative sticky rebalance for rolling consumer deploys.

## Scalability

Metadata overhead grows with partition count — avoid partition explosion.

## Reliability

Monitor **under-replicated partitions** and ISR shrink events.

## Security

Inter-broker encryption on multi-tenant networks.

## Observability

Request handler idle ratio, log flush latency, ISR size per partition.

## Troubleshooting

| Symptom | Check |
| :--- | :--- |
| NOT_LEADER_FOR_PARTITION | Metadata stale; leader moved |
| Rebalance storm | session.timeout vs max.poll.interval |
| URP | Broker disk / network |

## Common Mistakes

- RF=1 topics in production.
- Increasing partitions without re-key strategy.

## Interview Questions

- What happens during ISR shrink?
- When is unclean leader election acceptable?
- How does log segment rolling affect retention?

## Architect Notes

Internals explain **why** ops matters — partition and ISR discipline are not optional at scale.
""",
    ),
    "kafka-performance.md": (
        "Kafka Performance",
        "Performance",
        "Throughput, latency, batching, compression, and capacity planning.",
        "2.3",
        203,
        """## Quick Revision

- **Batching** (`linger.ms`, `batch.size`) trades latency for throughput.
- **Compression** on producer reduces network; broker may recompress.
- **Partition count** caps parallel consumers per group.
- **Page cache** drives read performance for recent data.

## Core Concepts

| Knob | Effect |
| :--- | :--- |
| `linger.ms` | Wait to fill batch |
| `batch.size` | Upper batch bytes |
| `compression.type` | lz4 / zstd / snappy |
| `fetch.min.bytes` | Consumer batching |
| `num.io.threads` | Broker disk parallelism |

## Internal Working

Producers pipeline batches per partition. Brokers append sequentially — random writes are the enemy.

## Architecture

Capacity plan: peak RPS × payload × retention × RF = disk; ingress/egress bandwidth per broker.

## Design Tradeoffs

| Goal | Tuning |
| :--- | :--- |
| Throughput | Larger batches, lz4/zstd |
| Low latency | `linger.ms=0`, smaller batches |
| Cost | Tiered storage / shorter retention |

## Production Patterns

- Load-test **producer and consumer** independently before campaigns.
- Right-size brokers: network + NVMe; avoid CPU-bound GC pauses.

## Scalability

Adding consumers stops helping when `consumers >= partitions`.

## Reliability

Performance tuning must not drop `acks=all` on critical paths without explicit risk acceptance.

## Security

Compression does not replace encryption.

## Observability

p99 produce/fetch latency, broker disk %util, consumer `records-lag-max`.

## Troubleshooting

GC pauses → producer timeouts. Disk saturation → fetch latency spikes.

## Common Mistakes

- Optimizing throughput until latency SLO breaks.
- Hot partition from poor key choice.

## Interview Questions

- How do batch size and linger interact?
- When does partition count stop helping lag?
- What capacity math for 30-day retention RF=3?

## Architect Notes

State **SLOs first** (p99 latency vs MB/s), then tune — not the reverse.
""",
    ),
    "kafka-security.md": (
        "Kafka Security",
        "Security",
        "TLS, SASL, ACLs, encryption, and multi-tenant isolation.",
        "2.4",
        204,
        """## Quick Revision

- **mTLS** for client↔broker and broker↔broker.
- **SASL** (SCRAM, OAuth/OIDC) for authentication.
- **ACLs** for least-privilege topic/group/cluster ops.
- **Encryption at rest** via disk/KMS; app-layer for PII payloads.

## Core Concepts

| Layer | Mechanism |
| :--- | :--- |
| Transport | SSL/TLS listeners |
| Auth | SASL mechanisms |
| AuthZ | Kafka ACLs / RBAC (managed) |
| Audit | Authorizer logs, cloud audit trails |

## Internal Working

Clients bootstrap metadata over TLS; ACL authorizer checks principal on each API.

## Architecture

Segment networks: brokers in private subnets; no plaintext listeners in K8s production.

## Design Tradeoffs

| Approach | Notes |
| :--- | :--- |
| SCRAM | Simple; credential rotation discipline |
| mTLS | Strong; cert lifecycle ops |
| OAuth | Enterprise SSO; broker plugin support |

## Production Patterns

- Rotate broker certs with rolling restarts.
- Separate principals per service; deny `*` consume on PII topics.

## Scalability

ACL cache and authorizer latency — keep ACL sets maintainable.

## Reliability

Security misconfig shows as `TOPIC_AUTHORIZATION_FAILED` in clients.

## Security

{{% warning %}}
Plaintext listeners inside a cluster still expose traffic to anyone with pod network access.
{{% /warning %}}

## Observability

Alert on authorization failure spikes; audit admin operations.

## Troubleshooting

Client works in dev (PLAINTEXT) fails in prod (SSL) — check `security.protocol` and truststore.

## Common Mistakes

- Shared service account for all producers.
- Storing secrets in consumer properties in git.

## Interview Questions

- How would you rotate broker certificates without dropping clients?
- When is application-layer encryption needed beyond TLS?
- How do ACLs enforce least privilege on shared clusters?

## Architect Notes

Managed offerings (MSK, Confluent Cloud) shift authZ to IAM/RBAC — understand shared responsibility.
""",
    ),
    "kafka-operations.md": (
        "Kafka Operations",
        "Operations",
        "Upgrades, KRaft, Kubernetes, rolling restarts, and production runbooks.",
        "2.5",
        205,
        """## Quick Revision

- **Rolling broker restarts** trigger leader election — plan maintenance windows.
- **KRaft** replaces ZooKeeper for metadata quorum.
- **K8s**: StatefulSets/operators, PDBs, persistent volumes.
- Document **replay** and **failover** procedures before incidents.

## Core Concepts

| Operation | Risk |
| :--- | :--- |
| Broker upgrade | Rebalance / leader churn |
| Topic expand partitions | Ordering scope changes |
| Offset reset | Duplicate or skipped processing |
| Cluster expand | Reassignment traffic |

## Internal Working

Controller broker manages partition leadership. Metadata propagates to all brokers and clients.

## Architecture

MSK / Confluent Cloud / Event Hubs reduce day-2 ops; self-hosted needs 24/7 on-call for critical platforms.

## Design Tradeoffs

| Model | Ops ownership |
| :--- | :--- |
| Self-hosted | Full |
| MSK | AWS patches brokers |
| Event Hubs | Kafka protocol subset |

## Production Patterns

- Pre-upgrade compatibility matrix (broker vs client vs connect).
- Failure drills: broker kill, AZ loss, controller failover.

## Scalability

Broker count and partition leadership balance — avoid hotspot leaders.

## Reliability

PDB + RF≥3 + rack awareness for K8s broker upgrades.

## Security

Rotate credentials on schedule; audit topic creation.

## Observability

Runbooks tied to alerts: ISR shrink, offline partitions, controller moves.

## Troubleshooting

Metadata storms after mass topic creation — throttle admin API.

## Common Mistakes

- Upgrading all brokers simultaneously.
- No tested backup for topic configs and ACLs.

## Interview Questions

- What happens during rolling broker restart?
- How do you migrate ZooKeeper to KRaft safely?
- What K8s patterns apply to Kafka at scale?

## Architect Notes

Staff the **operational model** you choose — managed is not zero ops for clients, topics, and ACLs.
""",
    ),
    "kafka-troubleshooting.md": (
        "Kafka Troubleshooting",
        "Troubleshooting",
        "Consumer lag, rebalances, replication, disk, and incident runbooks.",
        "2.6",
        206,
        """## Quick Revision

- **Lag** = end offset − committed offset per partition.
- **Poison message** blocks partition until skipped or DLT.
- **URP** after network partition — check ISR and disk.
- Isolate lag: producer vs broker vs consumer.

## Core Concepts

| Symptom | First checks |
| :--- | :--- |
| Lag spike | Consumer errors, deploy, traffic |
| Rebalance loop | `max.poll.interval.ms` |
| Produce timeouts | Broker GC, disk, ISR |
| Hot partition | Key distribution |

## Internal Working

Stuck consumer on one partition blocks progress for that partition only — others continue.

## Architecture

Incident flow: alert → dashboard → partition skew → consumer logs → broker metrics.

## Design Tradeoffs

| Fix | Risk |
| :--- | :--- |
| Skip bad offset | Data loss for that message |
| Scale consumers | No effect if partitions < consumers |
| Increase retention | Disk emergency |

## Production Patterns

- DLT + replay tooling from day one.
- Runbook: all consumers stopped committing offsets.

## Scalability

Campaign traffic — pre-scale consumers to partition count.

## Reliability

Test offset reset on staging with idempotency validation.

## Security

Authorization failures mimic "consumer stuck" — check ACL changes.

## Observability

Lag by group/topic/partition; consumer rebalance rate.

## Troubleshooting

### Consumer lag during campaigns
Auto-scale consumers to partition count; fix slow handlers; check downstream DB.

### Poison messages
Route to DLT; fix deserializer; replay after schema fix.

### Schema drift
Registry compatibility mode blocked deploy — coordinate producer/consumer rollout.

### Broker patching
Expect leader movement; watch under-replicated partitions.

## Common Mistakes

- Alerting only on total lag, not per-partition skew.
- No DLT before production.

## Interview Questions

- How do you troubleshoot one partition lagging behind?
- What causes rebalance loops?
- How would you replay after a downstream bug safely?

## Architect Notes

Temporal decoupling makes traces essential — propagate trace IDs in headers.
""",
    ),
    "kafka-interview-guide.md": (
        "Kafka Interview Guide",
        "Interview",
        "Consolidated Kafka interview themes and answer framing.",
        "2.7",
        207,
        """## Quick Revision

- Frame Kafka as a **durable log** with offset-based consumption.
- Always mention **delivery semantics + idempotency + DLQ**.
- Compare to queues when asked "why Kafka" — hybrid fluency wins.
- Depth order: core → internals → ops → trade-offs.

## Core Concepts

Interviewers probe: partitioning, ISR, rebalance, exactly-once boundaries, ops readiness.

## Internal Working

Be ready to whiteboard: producer → leader → ISR → consumer fetch → offset commit.

## Architecture

Draw fan-out with multiple consumer groups on one topic.

## Design Tradeoffs

Know when **not** to pick Kafka: tight sync RPC, no ops team, no replay need.

## Production Patterns

{{< interview-answer >}}
"Kafka is a durable log — producers append, consumers track offsets, multiple consumer groups read the same stream, and you can replay. I'd clarify delivery guarantees, partition keys for ordering, and ops model. Idempotent consumers and dead-letter handling are non-negotiable in production."
{{< /interview-answer >}}

## Scalability

Partition planning early; cannot freely shrink partitions.

## Reliability

`acks=all`, `min.insync.replicas`, unclean election policy.

## Security

mTLS + ACLs for shared clusters.

## Observability

Lag, ISR, p99 latency.

## Troubleshooting

Walk through lag isolation and poison message handling.

## Common Mistakes

- Certification trivia instead of production stories.
- Claiming end-to-end exactly-once across Kafka + DB without outbox/CDC.

## Interview Questions

See [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/) for the full bank.

## Architect Notes

Link answers to **business flows** (orders, payments, CDC) — not broker trivia alone.
""",
    ),
}

for fname, (title, short, desc, ref, weight, body) in KAFKA_FILES.items():
    w(
        f"02-kafka/{fname}",
        body,
        title=title,
        desc=desc,
        short=short,
        mod=2,
        mod_title="Apache Kafka",
        ref=ref,
        weight=weight,
    )

# --- 03 Comparisons ---
COMP_MATRIX = """
{{< comparison-table caption="{caption}" >}}
| Dimension | Kafka | {other} |
| :--- | :--- | :--- |
| **Throughput** | Very high (batching) | {throughput} |
| **Latency** | Tunable; batching adds tail | {latency} |
| **Ordering** | Per partition | {ordering} |
| **Replay** | Native offset reset | {replay} |
| **Multi-tenancy** | Cluster + ACLs | {tenancy} |
| **Scalability** | Partitions + brokers | {scale} |
| **Operations** | Partitions, ISR, rebalance | {ops} |
| **Cost** | TCO staffing + infra | {cost} |
| **Reliability** | RF + ISR + acks | {reliability} |
| **Kubernetes** | Operators / Strimzi | {k8s} |
| **Best use cases** | Event streaming, CDC, analytics | {use_cases} |
{{< /comparison-table >}}
"""

w(
    "03-broker-comparisons/kafka-vs-rabbitmq.md",
    COMP_MATRIX.format(
        caption="Kafka vs RabbitMQ",
        other="RabbitMQ",
        throughput="High",
        latency="Lower per-message",
        ordering="Per queue (single consumer)",
        replay="DLQ / manual",
        tenancy="vhost isolation",
        scale="Queues + consumers",
        ops="Moderate broker HA",
        cost="Lower at small scale",
        reliability="Ack + mirrors",
        k8s="Helm charts",
        use_cases="Task queues, routing, RPC",
    )
    + """
## Quick Revision

- Kafka = **log**; RabbitMQ = **broker routing to queues**.
- Kafka for fan-out + replay; RabbitMQ for task distribution + complex routing.
- Hybrid platforms are normal.

## Core Concepts

| Pain | Kafka | RabbitMQ |
| :--- | :--- | :--- |
| Massive fan-out | Consumer groups | Exchanges + bindings |
| Replay | Offset reset | DLQ patterns |
| Task routing | Awkward | Native |
| Per-entity order | Partition key | Single active consumer |

## Internal Working

RabbitMQ removes messages on ack. Kafka retains per policy.

## Architecture

```mermaid
flowchart LR
  subgraph kafkaPath [Kafka streaming]
    p1[Order Service] --> log[(Topic)]
    log --> c1[Inventory Group]
    log --> c2[Analytics Group]
  end
  subgraph rabbitPath [RabbitMQ tasks]
    p2[Payment Service] --> ex{Exchange}
    ex --> q1[Retry Queue]
    ex --> w1[Worker]
  end
```

## Design Tradeoffs

See matrix above. Anti-pattern: RabbitMQ as analytics source of truth without retention.

## Production Patterns

| Flow | Choice |
| :--- | :--- |
| Order events to warehouse + CRM + lake | Kafka |
| Payment retry TTL ladder | RabbitMQ |
| Fraud priority dispatch | RabbitMQ |

## Scalability

Kafka wins extreme throughput; RabbitMQ wins flexible routing at moderate scale.

## Reliability

Both: at-least-once + idempotent consumers + DLQ.

## Security

AMQP TLS + vhosts vs Kafka TLS + ACLs.

## Observability

Queue depth vs consumer lag.

## Troubleshooting

| Failure | Kafka | RabbitMQ |
| :--- | :--- | :--- |
| Poison message | Stuck offset / DLT | DLQ fills |
| Upgrade | Rebalance storm | Mirror queue migration |

## Common Mistakes

- Forcing one broker for everything.

## Interview Questions

- When pick Kafka over RabbitMQ?
- How does replay differ?
- Describe a hybrid architecture.

## Architect Notes

[Broker Selection Guide](/kafka-handbook/01-fundamentals/broker-selection-guide/)
""",
    title="Kafka vs RabbitMQ",
    desc="Log vs queue — throughput, ordering, replay, and operational complexity.",
    short="vs RabbitMQ",
    mod=3,
    mod_title="Broker Comparisons",
    ref="3.1",
    weight=301,
)

w(
    "03-broker-comparisons/kafka-vs-pulsar.md",
    COMP_MATRIX.format(
        caption="Kafka vs Pulsar",
        other="Pulsar",
        throughput="Very high",
        latency="Comparable",
        ordering="Per partition",
        replay="Native",
        tenancy="Built-in multi-tenant",
        scale="Brokers + BookKeeper",
        ops="BookKeeper + broker tiers",
        cost="Higher operational surface",
        reliability="Quorum storage",
        k8s="Pulsar Helm",
        use_cases="Multi-tenant, geo-replication",
    )
    + """
## Quick Revision

- Pulsar: **unified queue + log**, strong **multi-tenancy** and **geo-replication**.
- Kafka: larger ecosystem; simpler mental model for many teams.

## Core Concepts

Pulsar separates **serving** (brokers) from **storage** (BookKeeper).

## Internal Working

Geo-replication built-in vs Kafka MirrorMaker 2 add-on.

## Architecture

Choose Pulsar when **tenant isolation** and **geo** are first-class ADR requirements.

## Design Tradeoffs

Pulsar ops learning curve vs Kafka talent pool.

## Production Patterns

Evaluate Pulsar for SaaS event platforms with per-customer namespaces.

## Scalability

Both scale horizontally; Pulsar bookie tier adds planning dimension.

## Reliability

BookKeeper quorum vs Kafka ISR — different failure models.

## Security

Pulsar namespace policies vs Kafka ACLs.

## Observability

Comparable metrics; different tooling.

## Troubleshooting

BookKeeper ensemble issues ≠ Kafka ISR issues — runbooks differ.

## Common Mistakes

Picking Pulsar without BookKeeper ops experience.

## Interview Questions

- When does Pulsar beat Kafka for multi-tenant streaming?
- How does geo-replication compare to MirrorMaker?

## Architect Notes

[Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/)
""",
    title="Kafka vs Pulsar",
    desc="Multi-tenant streaming, BookKeeper storage, and geo-replication trade-offs.",
    short="vs Pulsar",
    mod=3,
    mod_title="Broker Comparisons",
    ref="3.2",
    weight=302,
)

w(
    "03-broker-comparisons/kafka-vs-nats.md",
    COMP_MATRIX.format(
        caption="Kafka vs NATS",
        other="NATS",
        throughput="High (JetStream)",
        latency="Very low",
        ordering="Stream limits",
        replay="JetStream",
        tenancy="Accounts",
        scale="Lightweight nodes",
        ops="Low footprint",
        cost="Lower for edge",
        reliability="JetStream quorum",
        k8s="NATS operator",
        use_cases="Edge, control plane, signaling",
    )
    + """
## Quick Revision

- NATS: **low latency**, lightweight; JetStream adds persistence.
- Kafka: heavy-duty retention, ecosystem, stream processing.

## Core Concepts

NATS core is fire-and-forget; JetStream adds log semantics closer to Kafka.

## Internal Working

Different protocol and persistence layer — not drop-in Kafka replacement.

## Architecture

NATS at **edge** and **control plane**; Kafka as **central event backbone**.

## Design Tradeoffs

JetStream vs Kafka when persistence needed at small/medium scale.

## Production Patterns

IoT telemetry ingress on NATS → aggregate to Kafka for analytics.

## Scalability

NATS excels at connection count; Kafka at retained volume.

## Reliability

Define persistence tier explicitly — core NATS is not Kafka.

## Security

NATS accounts/JWT vs Kafka ACLs.

## Observability

Connection churn vs lag metrics.

## Troubleshooting

Confusing core NATS with durable JetStream semantics.

## Common Mistakes

Using NATS core for durable financial events without JetStream.

## Interview Questions

- When prefer NATS over Kafka at the edge?
- What does JetStream add?

## Architect Notes

Compare **latency SLO** and **retention** requirements first.
""",
    title="Kafka vs NATS",
    desc="Low-latency messaging and JetStream versus Kafka log platform.",
    short="vs NATS",
    mod=3,
    mod_title="Broker Comparisons",
    ref="3.3",
    weight=303,
)

w(
    "03-broker-comparisons/kafka-vs-redpanda.md",
    COMP_MATRIX.format(
        caption="Kafka vs Redpanda",
        other="Redpanda",
        throughput="Very high",
        latency="Low (C++ runtime)",
        ordering="Per partition",
        replay="Kafka-compatible",
        tenancy="ACLs",
        scale="Kafka-like",
        ops="No ZooKeeper; simpler footprint",
        cost="License + infra",
        reliability="Kafka protocol semantics",
        k8s="Redpanda operator",
        use_cases="Kafka API without ZK ops",
    )
    + """
## Quick Revision

- Redpanda: **Kafka-compatible API** without ZooKeeper.
- Evaluate compatibility matrix for Connect, Streams, custom clients.

## Core Concepts

Wire protocol compatibility ≠ full ecosystem parity for all plugins.

## Internal Working

Single binary per node; different storage engine than Apache Kafka.

## Architecture

Migration path: clients first, validate Connect/Streams workloads.

## Design Tradeoffs

Ops simplification vs ecosystem maturity of Apache Kafka.

## Production Patterns

PoC with production traffic shadowing before cutover.

## Scalability

Similar partition planning rules as Kafka.

## Reliability

Test ISR/leader behavior under your failure scenarios — don't assume identical.

## Security

TLS/SASL compatible patterns.

## Observability

Prometheus metrics; verify dashboard parity with existing runbooks.

## Troubleshooting

Client works on Kafka fails on Redpanda — check protocol feature flags.

## Common Mistakes

Assuming 100% drop-in for entire Kafka ecosystem day one.

## Interview Questions

- Why Redpanda over self-hosted Kafka?
- What migration risks remain?

## Architect Notes

[Broker Selection Guide](/kafka-handbook/01-fundamentals/broker-selection-guide/)
""",
    title="Kafka vs Redpanda",
    desc="Kafka-compatible streaming without ZooKeeper — ops and migration trade-offs.",
    short="vs Redpanda",
    mod=3,
    mod_title="Broker Comparisons",
    ref="3.4",
    weight=304,
)

w(
    "03-broker-comparisons/cloud-messaging-services.md",
    """## Quick Revision

- Interview topic: **Kafka vs managed cloud messaging** — not individual SKU trivia.
- AWS: **SQS** (queue), **SNS** (fan-out), **MSK** (Kafka managed).
- Azure: **Event Hubs** (Kafka protocol), **Service Bus** (sessions/DLQ).
- GCP: **Pub/Sub**. Legacy: **ActiveMQ**, **IBM MQ** (JMS enterprise).

## Core Concepts

{{< comparison-table caption="Kafka vs managed cloud messaging" >}}
| Dimension | Self-hosted / MSK Kafka | SQS / Pub/Sub / Service Bus |
| :--- | :--- | :--- |
| **Throughput** | Very high | High; per-service limits |
| **Latency** | Tunable | Low–moderate |
| **Ordering** | Partition keys | FIFO queues / sessions (limited) |
| **Replay** | Full | Limited or none |
| **Multi-tenancy** | ACLs / IAM | Cloud IAM + namespaces |
| **Scalability** | You plan partitions | Elastic managed |
| **Operations** | High (or MSK partial) | Minimal |
| **Cost** | Infra + staffing | Per-request / throughput units |
| **Reliability** | You configure RF/ISR | Provider SLA |
| **Kubernetes** | Strimzi / operators | SDK + IAM |
| **Best use cases** | Event backbone, CDC | Decouple without broker ops |
{{< /comparison-table >}}

## Internal Working

**SNS → SQS fan-out** parallels multiple consumer groups but without long retention replay. **Event Hubs** exposes Kafka protocol for many clients.

## Architecture

| Cloud | Kafka-aligned | Queue / bus |
| :--- | :--- | :--- |
| AWS | MSK, EventBridge+Kinesis | SQS, SNS |
| Azure | Event Hubs | Service Bus |
| GCP | — | Pub/Sub |

## Design Tradeoffs

Choose cloud queues when team cannot run broker HA and **replay is not required**. Choose Event Hubs/MSK when Kafka clients exist but ops must shrink.

## Production Patterns

- Hybrid: Kafka on-prem + Event Hubs bridge for cloud consumers.
- Legacy JMS (ActiveMQ/IBM MQ): migrate via CDC/outbox to Kafka over big-bang.

## Scalability

Cloud quotas and throttling replace partition math — monitor account limits.

## Reliability

DLQ patterns on Service Bus/SQS; not equivalent to offset replay.

## Security

IAM roles per producer/consumer; private link for compliance.

## Observability

Cloud-native metrics (ApproximateAgeOfOldestMessage, subscription backlog).

## Troubleshooting

| Issue | Cloud signal |
| :--- | :--- |
| Backlog | Queue depth / oldest age |
| Duplicates | Visibility timeout too low |
| Ordering break | Not using FIFO/session features |

## Common Mistakes

- Expecting Kafka replay semantics from standard SQS.
- Running IBM MQ **and** Kafka forever without migration map.

## Interview Questions

- When is SQS right over Kafka?
- How does SNS+SQS fan-out differ from consumer groups?
- Event Hubs vs self-hosted Kafka — ops ownership shift?

## Architect Notes

Consolidated comparison for **architect interviews** — depth on trade-offs, not console walkthroughs.
""",
    title="Cloud Messaging Services",
    desc="Kafka vs SQS, SNS, Pub/Sub, Service Bus, Event Hubs, and legacy JMS platforms.",
    short="Cloud Messaging",
    mod=3,
    mod_title="Broker Comparisons",
    ref="3.5",
    weight=305,
)

print("Comparisons done")

# --- 04 Interview guide ---
PATH_MAP = {
    "`content/kafka-handbook/kafka.md`": "`content/kafka-handbook/02-kafka/kafka-core.md`",
    "`content/kafka-handbook/rabbitmq.md`": "`content/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq.md`",
    "`content/kafka-handbook/pulsar.md`": "`content/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar.md`",
    "`content/kafka-handbook/nats.md`": "`content/kafka-handbook/03-broker-comparisons/kafka-vs-nats.md`",
    "`content/kafka-handbook/redpanda.md`": "`content/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda.md`",
    "`content/kafka-handbook/sqs.md`": "`content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md`",
    "`content/kafka-handbook/sns.md`": "`content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md`",
    "`content/kafka-handbook/google-pubsub.md`": "`content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md`",
    "`content/kafka-handbook/azure-service-bus.md`": "`content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md`",
    "`content/kafka-handbook/_index.md`": "`content/kafka-handbook/01-fundamentals/broker-selection-guide.md`",
    "`content/kafka-handbook/activemq.md`": "`content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md`",
    "`content/kafka-handbook/ibm-mq.md`": "`content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md`",
}

TOPIC_DOC_OVERRIDE = {
    "Internals": "`content/kafka-handbook/02-kafka/kafka-internals.md`",
    "Performance": "`content/kafka-handbook/02-kafka/kafka-performance.md`",
    "Security": "`content/kafka-handbook/02-kafka/kafka-security.md`",
    "Troubleshooting": "`content/kafka-handbook/02-kafka/kafka-troubleshooting.md`",
    "Observability": "`content/kafka-handbook/02-kafka/kafka-operations.md`",
    "Fundamentals": "`content/kafka-handbook/01-fundamentals/messaging-models.md`",
    "Reliability": "`content/kafka-handbook/02-kafka/kafka-internals.md`",
    "Operations": "`content/kafka-handbook/02-kafka/kafka-operations.md`",
    "Deployment": "`content/kafka-handbook/02-kafka/kafka-operations.md`",
    "Scalability": "`content/kafka-handbook/02-kafka/kafka-performance.md`",
}

old_top150 = HB / "top-150-interview-questions.md"


def extract_section(content: str, heading: str) -> list[str]:
    if heading not in content:
        return []
    part = content.split(heading, 1)[1]
    if "\n# " in part:
        part = part.split("\n# ", 1)[0]
    lines = []
    for line in part.splitlines():
        line = line.strip()
        if line and line[0].isdigit() and ". " in line[:4]:
            lines.append(line.split(". ", 1)[1])
    return lines


if old_top150.exists():
    raw = old_top150.read_text(encoding="utf-8")
    for old, new in PATH_MAP.items():
        raw = raw.replace(old, new)
    out_lines = []
    for line in raw.splitlines():
        for old, new in PATH_MAP.items():
            line = line.replace(old, new)
        if line.startswith("| ") and "`content/kafka-handbook/02-kafka/kafka-core.md`" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 7:
                topic = parts[5]
                if topic in TOPIC_DOC_OVERRIDE:
                    line = line.replace(
                        "`content/kafka-handbook/02-kafka/kafka-core.md`",
                        TOPIC_DOC_OVERRIDE[topic],
                    )
        out_lines.append(line)
    body = "\n".join(out_lines)
    if body.startswith("---"):
        body = body.split("---", 2)[-1].strip()

    intro = "Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. Questions only — no answers. Each row maps to a handbook document.\n\n"
    w(
        "04-interview-guide/top-150-interview-questions.md",
        intro + body,
        title="Top 150 Kafka Interview Questions",
        desc="150 production-oriented Kafka interview questions mapped to handbook topics.",
        short="Top 150",
        mod=4,
        mod_title="Interview Guide",
        ref="4.1",
        weight=401,
    )

    migrated = (HB / "04-interview-guide/top-150-interview-questions.md").read_text(encoding="utf-8")
    sections = {
        "architect-questions.md": ("Architect-Level Questions", "Top 25 Architect-Level Questions", "4.2", 402),
        "troubleshooting-questions.md": ("Production Troubleshooting Questions", "Top 25 Production Troubleshooting Questions", "4.3", 403),
        "design-tradeoffs.md": ("Design & Architecture Questions", "Top 25 Design & Architecture Questions", "4.4", 404),
    }
    for fname, (title_part, heading, ref, weight) in sections.items():
        qs = extract_section(migrated, f"# {heading}")
        list_md = "\n".join(f"{i}. {q}" for i, q in enumerate(qs, 1))
        w(
            f"04-interview-guide/{fname}",
            f"Questions only — no answers. Sourced from [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/).\n\n# {heading}\n\n{list_md}",
            title=title_part,
            desc=f"Curated {title_part.lower()} from the Kafka handbook question bank.",
            short=title_part.split()[0],
            mod=4,
            mod_title="Interview Guide",
            ref=ref,
            weight=weight,
        )

print("Interview guide done")
print("Generation complete.")
