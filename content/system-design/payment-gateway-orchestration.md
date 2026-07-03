---
title: "Designing a Payment Gateway Orchestration System at Scale"
date: 2026-06-27T10:00:00+00:00
draft: false
description: "Production-grade system design for a multi-tenant payment gateway orchestration engine — payment intents, PCI tokenization, processor routing, idempotency, and reconciliation at 10K TPS."
tags: ["system-design", "payments", "distributed-systems", "microservices", "postgresql", "redis", "kafka", "pci-dss"]
categories: ["System Design"]
---

A payment gateway orchestration engine sits between merchants and external processors (PayU, Razorpay, Stripe-style APIs). Merchants declare **payment intents**, customers complete checkout in a **hosted PCI boundary**, and the gateway **tokenizes card data**, **routes captures** to processors, and **reconciles** terminal states via webhooks and background workers.

At scale this is a **write-heavy, CP-critical** system: financial state must stay consistent, authorization paths must complete in under **200 ms** (excluding processor time), and peak throughput targets **10,000 write TPS** with roughly **50,000 read RPS** from status polling and checkout reloads. This post covers the full design — requirements, capacity math, API contracts, schema, architecture, orchestration logic, technology choices, caching, infrastructure sizing, and failure modes. For 50 senior-level interview follow-ups, see [Payment Gateway Interview Questions](/system-design/payment-gateway-orchestration-interview-questions/).

---

## 1. Requirements and Goals

### Functional Requirements (MVP)

| Requirement | Description |
| :--- | :--- |
| **Payment intent lifecycle** | Merchants initiate a unique payment session with amount, currency, and order reference. |
| **Hosted checkout / elements** | Generate secure, short-lived session pages or custom frontend URLs that capture cardholder data (CHD) inside the gateway's isolated environment. |
| **Tokenization & PCI compliance** | PAN, CVV, and expiry are captured, tokenized, and isolated cryptographically — merchant servers never enter PCI-DSS scope. |
| **Processor orchestration & routing** | Dynamically select, transform, and dispatch transactions to external processors based on merchant routing rules. |
| **Async callback ingestion** | Ingest webhooks and callbacks from processors to track intermediate and terminal order states. |
| **Transaction status visibility** | Near-real-time polling endpoints and asynchronous merchant webhooks for settlement progress. |

### Out of Scope

| Item | Reason |
| :--- | :--- |
| Partial payments / split rules | Adds ledger complexity beyond orchestration core |
| Refund routing, chargeback disputes, payout accounting | Separate financial settlement domain |
| Direct card-network integration | Handled by downstream payment processors |

### Clarifying Assumptions

| Question | Assumption |
| :--- | :--- |
| Build direct card-network integrations? | **No** — orchestrate across existing processors; the engine is an intelligent router. |
| Retry policy on processor timeout? | **Idempotent retry up to 3 times**, then `PENDING_RECONCILIATION`; never blind retries. |
| Cross-service audit tracing? | Inject signed `X-Gateway-Trace-ID` at the API gateway; write to immutable compliance logs. |

### Non-Functional Requirements

| NFR | Target |
| :--- | :--- |
| **Consistency** | **CP over AP** — no split-brain, double-deduction, or phantom state updates |
| **Latency** | Gateway processing (auth parsing, validation, tokenization, routing) **< 200 ms**, excluding processor time |
| **Security** | **PCI-DSS Level 1** — NACL isolation, dedicated tokenization, HSM-backed keys |
| **Availability** | **99.999%** on payment ingestion layer |
| **Peak write TPS** | **10,000 TPS** |
| **Peak read RPS** | **~50,000 RPS** (5:1 read/write from polling, hooks, page reloads) |

---

## 2. Back-of-the-Envelope Calculations

### Traffic Estimates

Design target: **100 million transactions/day** at peak distributed load.

| Metric | Calculation | Result |
| :--- | :--- | :--- |
| Transactions / day | Design target | **100,000,000** |
| State transitions per txn | Intent → Session → Pay → Callback → Webhook | **5 requests** |
| Total requests / day | 100M × 5 | **500,000,000** |
| Peak write TPS | Given | **10,000 TPS** |
| Peak read RPS | 10K × 5 (read/write ratio) | **50,000 RPS** |

### Storage

| Assumption | Calculation | Result |
| :--- | :--- | :--- |
| Row footprint (intent + metadata) | ~1 KB / record | — |
| Daily ingest | 100M × 1 KB | **~100 GB / day** |
| Annual ingest | 100 GB × 365 | **~36.5 TB / year** |

### Cache Sizing (Active Sessions)

Checkout sessions use a **10-minute TTL**:

```
Active sessions = 10,000 TPS × 600 s = 6,000,000 sessions
Memory          = 6M × 1.5 KB       ≈ 9 GB RAM (active buffer)
```

With a **99% cache hit ratio** on merchant config and active sessions, Redis must retain ~9 GB of hot session state plus routing metadata.

### Bandwidth & Event Bus

| Path | Calculation | Result |
| :--- | :--- | :--- |
| Write ingress | 10K TPS × 2 KB | **20 MB/s** |
| Read egress | 50K RPS × 1 KB | **50 MB/s** |
| **Total peak** | 20 + 50 MB/s | **~70 MB/s (~560 Mbps)** |
| Kafka events | 10K TPS × 3 internal events | **30,000 events/sec** |

---

## 3. API Design

| # | Method | Path | Purpose |
| :---: | :--- | :--- | :--- |
| 1 | POST | `/v1/payment_intents` | Create Payment Intent |
| 2 | POST | `/v1/checkout/sessions` | Create Checkout Session |
| 3 | POST | `/v1/charge` | Charge (internal PCI zone) |

{{< api-endpoint method="POST" path="/v1/payment_intents" desc="Create Payment Intent" open="true" >}}
Headers:

```
Authorization: Bearer sk_live_merchant_id_alpha
Idempotency-Key: idem_key_uuid_v4_abc123
Content-Type: application/json
```

{{< api-request >}}
```json
{
  "amount": 15000,
  "currency": "INR",
  "merchant_order_id": "ord_9981245",
  "customer_id": "cust_3321"
}
```
{{< /api-request >}}

{{< api-response code="201" label="Created" >}}
```json
{
  "id": "pi_1102934",
  "client_secret": "secret_pi_1102934_auth_token_xyz",
  "status": "requires_payment_method",
  "amount": 15000,
  "currency": "INR",
  "created_at": 1779945840
}
```
{{< /api-response >}}
{{< /api-endpoint >}}

{{< api-endpoint method="POST" path="/v1/checkout/sessions" desc="Create Checkout Session" >}}
{{< api-request >}}
```json
{
  "payment_intent_id": "pi_1102934",
  "success_url": "https://merchant.com/success",
  "cancel_url": "https://merchant.com/cancel"
}
```
{{< /api-request >}}

{{< api-response code="200" label="OK" >}}
```json
{
  "session_id": "cs_99881122",
  "redirect_url": "https://checkout.gateway.com/pay/cs_99881122",
  "expires_at": 1779946440
}
```
{{< /api-response >}}
{{< /api-endpoint >}}

{{< api-endpoint method="POST" path="/v1/charge" desc="Charge (internal PCI zone only)" >}}
{{< api-notes >}}
Callable only from the isolated ingestion layer, not merchant backends.
{{< /api-notes >}}
{{< api-request >}}
```json
{
  "session_id": "cs_99881122",
  "card_token": "tok_encrypted_hsm_99218",
  "cvv_encrypted": "enc_cvv_332"
}
```
{{< /api-request >}}
{{< api-response code="202" label="Accepted" >}}
```json
{
  "transaction_id": "txn_554192",
  "status": "processing"
}
```
{{< /api-response >}}
{{< /api-endpoint >}}

{{< api-notes >}}
**Idempotency protocol**

1. Client sends a unique `Idempotency-Key` on every mutating request.
2. API gateway issues atomic `SETNX` to Redis: `KEY = "idem:{merchant_id}:{header_key}"`.
3. If key exists → return cached HTTP response; halt downstream routing.
4. If key absent → process request; persist final response to Redis with **24-hour TTL**.
{{< /api-notes >}}

**Common HTTP error codes**

{{% api-errors %}}
| Status | Condition |
| :--- | :--- |
| **400** | Validation failure (invalid currency, malformed payload) |
| **401** | Bad API signature, expired key, credential leak |
| **409** | Same `Idempotency-Key` with changed request body |
| **429** | IP or merchant rate-limit breach |
{{% /api-errors %}}
---

## 4. Data Model

```mermaid
erDiagram
    MERCHANT ||--o{ PAYMENT_INTENT : owns
    PAYMENT_INTENT ||--o{ PAYMENT_TRANSACTION : generates
    PAYMENT_TRANSACTION ||--o{ PAYMENT_LEDGER : records

    MERCHANT {
        varchar id PK
        varchar api_key_hash UK
        jsonb routing_strategy_json
        timestamp created_at
    }
    PAYMENT_INTENT {
        varchar id PK
        varchar merchant_id FK
        bigint amount
        char currency
        varchar status
        varchar idempotency_key UK
        int version
        timestamp updated_at
    }
    PAYMENT_TRANSACTION {
        varchar id PK
        varchar payment_intent_id FK
        varchar processor_type
        varchar external_reference_id
        varchar status
        char card_fingerprint
        int version
    }
    PAYMENT_LEDGER {
        bigserial id PK
        varchar transaction_id FK
        varchar entry_type
        bigint amount
        varchar reconciliation_status
    }
```

### `merchants`

| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | `VARCHAR(64)` | Primary key |
| `api_key_hash` | `VARCHAR(256)` | Unique — salted SHA-256 for validation |
| `routing_strategy_json` | `JSONB` | Denormalized processor weights and fallback rules |
| `created_at` | `TIMESTAMPTZ` | Tenant creation time |

### `payment_intents`

| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | `VARCHAR(64)` | Format `pi_...` |
| `merchant_id` | `VARCHAR(64)` | FK → `merchants.id` |
| `amount` | `BIGINT` | Smallest currency unit (paise/cents) |
| `currency` | `CHAR(3)` | ISO 4217 |
| `status` | `VARCHAR(32)` | `REQUIRES_PAYMENT_METHOD`, `PROCESSING`, `SUCCEEDED`, `FAILED` |
| `idempotency_key` | `VARCHAR(128)` | Unique per merchant |
| `version` | `INT` | Optimistic locking counter |
| `updated_at` | `TIMESTAMPTZ` | Last state transition |

### `payment_transactions`

| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | `VARCHAR(64)` | Format `txn_...` |
| `payment_intent_id` | `VARCHAR(64)` | FK → `payment_intents.id` |
| `processor_type` | `VARCHAR(32)` | `PAYU`, `RAZORPAY`, `STRIPE`, etc. |
| `external_reference_id` | `VARCHAR(128)` | Processor-side reference (indexed) |
| `status` | `VARCHAR(32)` | `SENT_TO_PROCESSOR`, `ACKNOWLEDGED`, `SETTLED`, `DECLINED` |
| `card_fingerprint` | `CHAR(64)` | Anonymized card signature for fraud profiling |
| `version` | `INT` | Optimistic locking counter |

### `payment_ledgers` (Immutable Reconciliation Target)

| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | `BIGSERIAL` | Primary key |
| `transaction_id` | `VARCHAR(64)` | FK → `payment_transactions.id` |
| `entry_type` | `VARCHAR(16)` | `DEBIT` or `CREDIT` |
| `amount` | `BIGINT` | Smallest currency unit |
| `reconciliation_status` | `VARCHAR(32)` | `UNRECONCILED`, `MATCHED`, `DISCREPANCY` |

### Indexing Strategy

| Index | Purpose |
| :--- | :--- |
| `UNIQUE (merchant_id, idempotency_key)` | Strict single execution per intent boundary |
| `INDEX (status) WHERE status = 'SENT_TO_PROCESSOR'` | Fast sweep for reconciliation workers |
| `INDEX (external_reference_id)` | Webhook correlation lookups |

**Normalization choice:** core financial tables stay in **3NF** for narrow-row writes and low lock contention. Merchant routing config is **denormalized JSONB** to avoid join-heavy hot-path lookups.

---

## 5. High-Level Architecture

```mermaid
flowchart LR
    Customer([Paying Customer])
    Merchant([Merchant Backend])

    subgraph edge["Edge"]
        LB["Anycast LB / API Gateway"]
    end

    subgraph k8sCore["Kubernetes Mesh"]
        IntentSvc["Payment Intent Service"]
        SessionSvc["Checkout Session Service"]
        IngestionSvc["Secure Charge Ingestion"]
        Orchestrator["Processor Orchestrator"]
        CallbackSvc["Callback Collector"]
        Reconciler["Reconciliation Engine"]

        RedisCluster[("Redis Cluster")]
        PGPrimary[("PostgreSQL Primary")]
        KafkaBus[[Kafka Cluster]]
    end

    subgraph pciZone["PCI-DSS Enclave"]
        TokenSvc["Tokenization Engine"]
        HSM["HSM"]
    end

    subgraph external["External Processors"]
        Connector["Processor Adapters"]
        ExtProc["PayU / Razorpay APIs"]
    end

    subgraph analytics["Analytics Layer"]
        ClickHouse[("ClickHouse")]
    end

    Customer -->|"HTTPS checkout"| LB
    Merchant -->|"POST /intents"| LB

    LB --> IntentSvc
    LB --> SessionSvc
    LB --> IngestionSvc

    IntentSvc --> PGPrimary
    SessionSvc --> RedisCluster
    IngestionSvc --> RedisCluster
    IngestionSvc --> TokenSvc
    TokenSvc --> HSM
    IngestionSvc --> KafkaBus

    Orchestrator --> KafkaBus
    Orchestrator --> PGPrimary
    Orchestrator --> Connector
    Connector --> ExtProc
    ExtProc -->|"webhooks"| CallbackSvc
    CallbackSvc --> KafkaBus

    KafkaBus --> ClickHouse
    Reconciler --> PGPrimary
    KafkaBus --> Reconciler
```

### Write Path — Payment Capture

1. Merchant creates a **payment intent** → persisted to PostgreSQL with idempotency guard in Redis.
2. Merchant (or frontend) creates a **checkout session** → session metadata cached in Redis (10-min TTL).
3. Customer submits card data to **Secure Charge Ingestion** (never touches merchant servers).
4. Ingestion service calls **Tokenization Engine** inside the PCI enclave → HSM produces encrypted token.
5. Ingestion emits a state event to **Kafka** and returns `202 processing`.
6. **Processor Orchestrator** consumes the event, evaluates merchant routing rules, and dispatches via the appropriate **adapter connector**.
7. Processor webhook hits **Callback Collector** → Kafka → state update → merchant notification.

### Read Path — Status Visibility

1. Merchant or checkout UI polls `GET /v1/payment_intents/{id}` or `GET /v1/transactions/{id}`.
2. **Redis read-through** serves active session and recent intent state.
3. On cache miss → PostgreSQL read replica ([CQRS](/system-design/cqrs-overview/) phase) → populate Redis.
4. Terminal states trigger async merchant webhooks via a dedicated Kafka dispatch topic.

### Component Responsibilities

| Component | Responsibility |
| :--- | :--- |
| **Edge API Gateway** | TLS termination, rate limiting, signature validation, trace ID injection |
| **Payment Intent Service** | Anchor intent records with ACID guarantees |
| **Checkout Session Service** | Short-lived UI tokens and session cache |
| **Secure Charge Ingestion** | PCI-bound card capture; bypasses merchant infrastructure |
| **Tokenization Engine** | PAN → stateless synthetic token via HSM |
| **Processor Orchestrator** | Routing, adapter dispatch, circuit breaking, retry |
| **Callback Collector** | High-throughput webhook ingestion |
| **Reconciliation Engine** | Cross-check internal state vs processor reports |

---

## 6. Orchestration, State Machine & ID Generation

### Payment Intent State Machine

```mermaid
stateDiagram-v2
    [*] --> REQUIRES_PAYMENT_METHOD: intent created
    REQUIRES_PAYMENT_METHOD --> PROCESSING: charge submitted
    PROCESSING --> SUCCEEDED: processor confirms
    PROCESSING --> FAILED: declined / timeout exhausted
    PROCESSING --> PENDING_RECONCILIATION: ambiguous after 3 retries
    PENDING_RECONCILIATION --> SUCCEEDED: reconciler confirms
    PENDING_RECONCILIATION --> FAILED: reconciler denies
    SUCCEEDED --> [*]
    FAILED --> [*]
```

Implemented via the **State pattern** — each status encapsulates valid transitions, avoiding nested conditionals.

### Processor Routing

The orchestrator reads `routing_strategy_json` from cache and selects a processor:

```
effective_weight(processor) = base_weight × health_score × success_rate_24h
```

On processor outage, a **circuit breaker** opens ([Resilience Patterns](/system-design/resilience-patterns-overview/)) and traffic fails over to the next weighted processor (e.g., Razorpay → PayU).

### Adapter Pattern

{{< impl-tabs default="java" java="Java" golang="Go" >}}
{{< impl-tab lang="java" >}}

```java
public interface PaymentProcessorConnector {
    ProcessorResponse processCapture(CaptureRequest request) throws GatewayNetworkException;
    ProcessorResponse queryExternalStatus(String externalTransactionId);
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
// TODO: idiomatic Go equivalent — mirror the Java snippet above
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

Each processor (Razorpay, PayU, Stripe) implements this interface — core logic stays decoupled from third-party JSON contracts.

### Concurrency Controls

| Mechanism | Application |
| :--- | :--- |
| **Optimistic locking** | `UPDATE ... SET status = :new, version = version + 1 WHERE id = :id AND version = :expected` |
| **Distributed lock** | `SET dlock:{txn_id} {token} NX PX 5000` before capture — prevents double-click double-charge |
| **Strict table access order** | Always update `payment_intents` before `payment_transactions` — prevents deadlocks |

### ID Generation

| Strategy | Verdict |
| :--- | :--- |
| UUID v4 | Rejected — random B-tree inserts degrade index performance |
| Auto-increment | Rejected — leaks volume metrics; single-node write bottleneck |
| **Snowflake ID** | **Selected** — 64-bit, chronologically sortable, distributed, index-friendly |

### Retry & Reconciliation

- Processor HTTP client timeout: **3,000 ms** with **[bulkhead](/system-design/resilience-patterns-overview/)**-isolated thread pools per connector.
- On timeout: idempotent retry up to **3 attempts** with the same idempotency token.
- After exhaustion: transition to `PENDING_RECONCILIATION`; background worker polls processor status API.

---

## 7. Database Selection and Scaling

### Technology Comparison

| Database | ACID | Throughput | Joins | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **PostgreSQL** | Strong (single primary) | Medium-high; scales via sharding | Native | **Selected** |
| MongoDB | Eventual / document locks | High unstructured | Poor | Rejected — weak financial constraints |
| Cassandra | Tunable eventual | Extreme writes | None | Rejected — no relational ledger model |
| CockroachDB | Distributed consensus | High distributed | Yes | Deferred — 3× replication overhead for initial single-region deploy |

### Messaging: Kafka vs RabbitMQ

**Kafka selected.** RabbitMQ drops messages after consumer ack; Kafka's append-only log enables replay — critical when the reconciliation engine must reconstruct history after a state failure.

### Scaling Evolution

```mermaid
flowchart TD
    S1["Phase 1: PostgreSQL Monolith<br/>Primary + sync standby<br/>Up to ~1,500 write TPS"]
    S2["Phase 2: CQRS Read Replicas<br/>Offload polling & dashboards"]
    S3["Phase 3: Vertical Partitioning<br/>Split merchants config from transactions"]
    S4["Phase 4: Shard by merchant_id<br/>hash(merchant_id) mod N<br/>Beyond ~8,000 write TPS"]
    S5["Phase 5: Multi-Region Edge<br/>Regional Redis + active-passive DB"]

    S1 --> S2 --> S3 --> S4 --> S5
```

| Phase | Trigger |
| :--- | :--- |
| Phase 1 | Launch — single primary + synchronous AZ replica (Patroni-managed) |
| Phase 2 | Read contention starves primary writes |
| Phase 3 | Checkpoint I/O spikes on monolithic tables |
| Phase 4 | Single-node write ceiling (~8K TPS) |
| Phase 5 | Cross-continent latency exceeds authorization budget |

### High Availability

| Component | Configuration | RPO / RTO |
| :--- | :--- | :--- |
| PostgreSQL | Patroni + etcd quorum; single-primary enforced | **RPO = 0**, **RTO < 30 s** |
| Kafka | `replication.factor = 3`, `min.insync.replicas = 2` | Event replay within seconds |
| Redis | 3 shards + 3 read replicas | Session fallback to PostgreSQL |

---

## 8. Caching Strategy

| Cache Target | Pattern | TTL |
| :--- | :--- | :--- |
| Merchant routing config | Cache-aside + write-through invalidation on admin update | 1 hour |
| Checkout session metadata | Read-through from Redis | **10 minutes** |
| Idempotency responses | Write-on-complete | **24 hours** |
| Recent intent status | Read-through | 5 minutes |

### Redis Configuration

- Eviction policy: **`allkeys-lru`** under memory pressure.
- Probabilistic early expiration on hot merchant config keys to prevent cache stampede.
- Two-tier model: **Caffeine** local cache (sub-ms) in service pods backed by central Redis.

### Sizing

```
Active sessions:  6M × 1.5 KB  ≈ 9 GB
Merchant config:  ~500 MB
Idempotency keys: ~2 GB peak
Headroom (2×):    ≈ 24 GB effective
```

Recommended: **3 primary shards + 3 replicas**, **32 GB RAM per node**.

---

## 9. Capacity Planning

Infrastructure sized for **10,000 peak write TPS** and **50,000 read RPS**:

| Component | Metric | Assumption | Recommendation |
| :--- | :--- | :--- | :--- |
| **Checkout / Ingestion Pods** | Peak write TPS | 10K TPS; ~250 TPS/pod | **40 pods** (4 vCPU, 8 GB each) |
| **Intent / Session Pods** | Mixed read/write | ~50K RPS aggregate | **30 pods** (2 vCPU, 4 GB) |
| **Orchestrator Consumers** | Kafka ingest | 30K events/sec | **20 pods** with bulkhead pools |
| **Redis Cluster** | Hot state | ~24 GB effective | **3 shards + 3 replicas**, 32 GB/node |
| **PostgreSQL** | Daily ingest | ~100 GB/day | **1 primary + 2 sync replicas**; time-based partitioning weekly |
| **Kafka** | Event rate | 30K events/sec | **5 brokers**, NVMe SSD, 7-day retention |
| **ClickHouse** | Analytics | Async from Kafka | **3-node cluster** |
| **Network** | Peak throughput | 70 MB/s | **~560 Mbps** provisioned |
| **HPA triggers** | Scale-out | CPU > 65% or > 2,500 connections/pod | Auto-scale ingestion and orchestrator pools |

---

## 10. Key Design Decisions Summary

| Decision | Choice | Rationale |
| :--- | :--- | :--- |
| Consistency model | **CP** (single PostgreSQL primary) | Financial mutations cannot tolerate split-brain |
| Primary datastore | PostgreSQL + JSONB routing config | ACID ledger + denormalized hot-path reads |
| Event bus | Kafka | Durable replay for reconciliation |
| PCI boundary | Isolated enclave + HSM tokenization | Shrinks audit scope; merchants never see PAN |
| Idempotency | Redis SETNX + 24h response cache | Duplicate requests return identical signatures |
| Status reads | Redis read-through, not DB polling | Avoids connection exhaustion at 50K RPS |
| Processor integration | Adapter pattern + bulkhead pools | Isolates slow processors from the gateway |
| Reconciliation | Immutable double-entry ledger | Handles missing webhooks and settlement gaps |
| ID generation | Snowflake | Sortable, distributed, index-efficient |
| Isolation level | READ COMMITTED + optimistic version | Performance with explicit contention fallback |
| Observability | `X-Gateway-Trace-ID` + signed audit logs | Compliance-grade cross-service tracing |
| SLO — availability | **99.995%** rolling 30-day | Ingestion layer |
| SLO — internal latency | **P95 < 45 ms** pre-processor | Gateway processing budget |
| SLO — error rate | **< 0.001%** 5xx | Transaction error velocity |

### Security Highlights

| Layer | Control |
| :--- | :--- |
| Network | Zero-trust PCI enclave; no inbound internet on tokenization tier |
| Transit | TLS 1.3 + mTLS between services |
| At rest | AES-256 volumes via KMS; monthly key rotation |
| Logging | AOP sanitization — PAN replaced with `[REDACTED_PAN]` |
| Edge | WAF + sliding-window rate limits in Redis |
| Multi-tenant | PostgreSQL Row-Level Security filtered by `merchant_id` |

### Production Improvements Over Naive Designs

| Naive Pattern | Production Alternative |
| :--- | :--- |
| Frontend polls PostgreSQL for status | Redis read-through + WebSocket status streams at gateway |
| Simple DB update loop for reconciliation | Immutable ledger + dedicated reconciliation pipeline |
| No edge rate limiting | Distributed token-bucket limits at API gateway |
| Card capture in general microservice | Dedicated PCI enclave decoupled from orchestrator logic |

---

## 11. Failure Modes and Mitigations

| Failure | Impact | Mitigation |
| :--- | :--- | :--- |
| **Redis unavailable** | Session lookups miss cache | Fall through to PostgreSQL; circuit breaker rate-limits non-essential traffic |
| **Kafka broker outage** | Settlement updates stall | Local disk buffer on ingestion pods; replay on recovery |
| **Processor timeout (Razorpay)** | Capture fails | Circuit breaker opens; reroute to backup processor (PayU) |
| **Gateway crash after processor success** | Internal state stuck at `SENT_TO_PROCESSOR` | Reconciliation worker polls processor API → `SUCCEEDED` |
| **Duplicate customer submit** | Risk of double charge | Redis distributed lock on client token; idempotency key enforcement |
| **Poison Kafka message** | Consumer crash loop | Dead Letter Queue; manual inspection; stream continues |
| **Primary DB failure** | Writes blocked | Patroni promotes sync standby; RPO = 0 |
| **Cache stampede on hot merchant** | DB spike on config expiry | Probabilistic early refresh; background pre-warm cron |
| **Processor webhook missed** | Stale terminal state | Reconciliation cron polls external status endpoints |
| **HSM unavailable** | Cannot tokenize | Fail closed — reject charge; alert ops; no PAN in fallback path |

---

## What's Next

The companion post [Payment Gateway Interview Questions](/system-design/payment-gateway-orchestration-interview-questions/) covers 50 senior-level probes — bulkhead isolation, 3DS flows, fraud carding defense, schema migrations at billions of rows, and multi-region data localization.
