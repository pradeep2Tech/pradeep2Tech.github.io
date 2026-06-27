---
title: "Stock Broker Trading System Design — Interview Questions"
date: 2026-06-27T10:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a Zerodha/Groww/Upstox-scale stock broker trading platform."
tags: ["system-design", "trading", "interview", "distributed-systems"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Stock Broker Trading Platform at Scale](/system-design/stock-broker-trading/). These questions probe ACID ledger consistency, exchange gateway resilience, sub-100 ms order paths, and real-time market data at 10K ticks/sec — the topics interviewers dig into after the whiteboard diagram.

---

## Core Consistency & Messaging (1–10)

**1. How does the system prevent the dual-write problem when updating the database and publishing to Kafka simultaneously?**

Implement the **Transactional Outbox Pattern**. The order service writes both the order record and an outbound event notification in a single ACID transaction. Debezium tails the PostgreSQL WAL asynchronously and streams events to Kafka without adding latency to the transaction loop.

**2. How do you design for split-brain scenarios in a multi-region deployment?**

For critical ledger balances, avoid multi-master async replication. Use a globally distributed database (CockroachDB or Google Spanner) with Raft/Paxos consensus — writes require confirmation from a strict majority of voting replicas before commit.

**3. What strategy prevents slow WebSocket clients from causing memory exhaustion on gateway servers?**

Enforce **Reactive Streams backpressure**. If a client's processing queue exceeds a memory threshold, the gateway drops that connection's real-time buffer and downgrades to a lightweight sampled notification feed until the client catches up.

**4. If an exchange confirmation message is delayed by 10 minutes, how does the system reconcile user margins?**

On order acceptance, lock the worst-case margin requirement as `blocked_margin`. Capital stays locked until the delayed execution message arrives via Kafka, at which point the reconciliation engine releases blocked funds and updates the active balance.

**5. How do you handle extreme clock skew across distributed servers evaluating limit order expirations?**

Do not rely on local system clocks. Order validity windows are driven by **logical block sequence timestamps** from the exchange market data feed. An official market-close event cancels outstanding daily limit orders uniformly regardless of local clock skew.

**6. How would you handle a sudden 100× spike in traffic caused by a market crash?**

Edge gateways combine leaky-bucket rate limiting with dynamic feature flags. Temporarily disable non-essential reads (historical reports, advanced portfolio analytics) to shed load and protect core order placement and margin validation pipelines.

**7. Why use InfluxDB for historical data instead of a relational database with time indexes?**

Relational B-Tree indexes degrade under constant high-volume tick writes. InfluxDB uses an LSM-tree variation optimized for time-series ingestion, concurrent writes, and long-term compression for charting queries.

**8. How do you guarantee message ordering inside Kafka for partial stock order fills?**

Use `order_id` as the **Kafka partition key**. All lifecycle events for a given order route to the same partition sequentially, preventing a final settlement event from being processed ahead of an earlier partial fill.

**9. What happens if the Outbound Exchange Gateway experiences a network partition while sending an order?**

The gateway maintains persistent FIX sessions with native sequence tracking. On reconnect, it renegotiates message sequence alignment with the exchange, identifying whether the pending order was received or needs retransmission — without duplicate placement.

**10. How do you mitigate cache stampede risks when a highly popular stock experiences major volatility?**

Implement **probabilistic early expiration (XFetch)** with mutual exclusion locking. When a hot key nears expiration under heavy read load, only one worker fetches fresh data while concurrent requests continue serving slightly stale cached values for a few milliseconds.

---

## Financial Integrity & Concurrency (11–20)

**11. How do you prevent a malicious user from executing an internal balance double-spend?**

Enforce **Optimistic Concurrency Control** via a mandatory `version_id` column on `user_ledgers`. Updates validate the version matches the read snapshot; concurrent modifications abort and retry from the new state.

**12. How do you handle database connections efficiently during peak trading hours when pods scale rapidly?**

Deploy **PgBouncer** as a connection proxy between microservices and PostgreSQL. Thousands of ephemeral application pods share a lean pool of persistent database connections, preventing connection exhaustion on the primary.

**13. How do you design the system to handle regulatory audits requiring 7 years of immutable trade history?**

Route long-term analytical streams from Kafka into **S3 Object Lock** buckets with WORM (Write Once, Read Many) policies, preventing modification or deletion for the mandatory retention period.

**14. What are the trade-offs of Snowflake IDs vs. UUIDv4 keys for the orders table?**

UUIDv4 random indexing causes page fragmentation and slower writes as clustered primary keys. Snowflake IDs are 64-bit, time-sortable integers that append sequentially to index pages, maximizing disk I/O efficiency with decentralized generation.

**15. How do you defend public WebSocket endpoints against DDoS connection floods?**

Route traffic through cloud security layers (Cloudflare Magic Transit) for attack scrubbing at the edge. API gateways enforce geo-fencing and cap concurrent open connections per unique IP before traffic reaches stateful WebSocket pools.

**16. What is your strategy for deploying schema updates to the high-volume orders table without downtime?**

Follow **expand-contract online migration**: add column as non-blocking background operation, dual-write from application code, backfill historical rows, switch reads to new column, then deprecate the old field.

**17. How does the system handle absolute failure of the time-series database during trading hours?**

InfluxDB is decoupled from transactional loops. Core trading continues; ingestion workers buffer ticks in persistent Kafka topics (sized for 24-hour retention) and replay from last known offsets on recovery.

**18. How do you clean up data in Redis Pub/Sub when thousands of users close their apps simultaneously?**

Pub/Sub channels are ephemeral — if all clients disconnect, Redis stops routing data instantly with no manual garbage collection. Gateway nodes use ping-pong heartbeats; on socket close, they unsubscribe from that user's watchlists immediately.

**19. How do you implement circuit breakers on outbound exchange links without dropping valid trades?**

Use Resilience4j: if failure rate crosses 5%, the breaker opens and routes subsequent orders to a **local persistent fail-safe queue** while alerting operators — keeping order states auditable inside system boundaries.

**20. Why avoid automated sharding engines like Vitess or Citus during early deployment?**

Sharding engines add substantial operational complexity, require careful primary key design, and make cross-shard transactions expensive. A well-tuned PostgreSQL primary with provisioned IOPS handles initial target volumes with a simpler operational footprint.

---

## Real-Time Data & Portfolio (21–30)

**21. How do you design a high-performance system to calculate unrealized P&L for millions of users simultaneously?**

Use an **in-memory streaming engine**. The portfolio service maintains position tallies in Redis; as LTP ticks stream through Redis Pub/Sub, it combines current prices with cached buy-in bases to update valuations without repetitive database queries.

**22. What happens if a user submits a market order when a stock has no active buyers or sellers?**

The validated order routes to the exchange order book. If no liquidity exists, the exchange holds it open. OMS tracks status via inbound Kafka confirmations, marking the order `SENT_TO_EXCHANGE` / `UNEXECUTED` and notifying the user.

**23. How do you handle compliance logging for user actions while keeping order routing latency low?**

Isolate audit logging from transactional loops. Critical actions write to an in-memory queue; a background worker batches and ships entries asynchronously to Elasticsearch, keeping audit overhead off the low-latency order path.

**24. What strategy allows you to test system performance safely against production-scale workloads?**

Use **traffic shadowing (dark launching)** at the API Gateway. Duplicate a sampled stream of encrypted production requests to an isolated staging environment without affecting live trading or user data.

**25. How do you manage connection limits when using serverless components for background processing?**

Do not attach Lambda functions directly to the relational database. Serverless tasks route updates through SQS or Kafka; central microservices consume events sequentially and maintain stable database connection metrics.

**26. How do you protect user financial balances from silent data corruption or bit rot?**

Build **Merkle Tree** append-only logs for transaction records. An hourly integrity job recalculates log hashes and flags variations, detecting storage-layer alterations immediately.

**27. Why use the FIX Protocol instead of JSON-over-HTTP REST for exchange gateways?**

JSON requires significant CPU overhead for parsing under high volume. FIX uses a lightweight binary-tag matrix designed for low-latency financial communications, minimizing payload footprints and parse latency.

**28. How do you handle partial fills for a limit order of 100,000 shares executing in 50 pieces over an hour?**

OMS treats executions as multi-stage state adjustments. Each partial fill streams through Kafka, creating a unique `trades` sub-entry. The parent `orders` record updates to `PARTIALLY_FILLED` with an incremented executed quantity counter.

**29. What is your strategy for gracefully degrading features when a third-party KYC provider goes down?**

Save registrations as `REGISTRATION_COMPLETE` / `KYC_PENDING` in a secure pool. Users explore the platform and manage watchlists while queue workers automatically retry verification when the provider restores service.

**30. How do you prevent accidental out-of-order execution when a user modifies a limit order multiple times quickly?**

Assign an incremental **sequence revision ID** at the API Gateway. OMS rejects modification requests whose sequence number is lower than the current version stored in the database.

---

## Scaling, Deployment & Operations (31–40)

**31. How do you scale the WebSocket Gateway cluster during sudden volatility surges?**

WebSocket nodes hold persistent TCP connections, making CPU-based autoscaling ineffective for rapid surges. Pre-scale based on daily trends with generous buffer capacity; edge routing uses consistent hashing to distribute new connections to underutilized nodes.

**32. What strategy protects the primary relational database from lock escalation during high-volume trading?**

Modify data using explicit **primary key pointer queries** only. Tight transactional boundaries lock individual rows, preventing expensive table-wide lock upgrades from unindexed update statements.

**33. Why use Redis Streams instead of Kafka for real-time client watchlist updates?**

Kafka's durable disk retention introduces unnecessary I/O overhead for temporary UI notifications. Redis Streams runs entirely in memory, delivering lower latency for short-lived watchlist update workflows.

**34. How do you prevent sensitive user information from leaking into application logs?**

Build custom **regex log masking filters** in Logback/Log4j2 that redact national tax IDs, passwords, and banking details before log lines are written to disk.

**35. How do you balance network compression and processing latency for real-time market feeds?**

Use **Zstandard (zstd)** compression in streaming pipelines. Compared to gzip, zstd provides strong compression ratios with minimal CPU overhead and adjustable optimization levels within low-millisecond latency budgets.

**36. What happens if a Kafka broker partition becomes corrupted during peak trading hours?**

Configure topics with **replication factor 3** and `min.insync.replicas=2`. Unhealthy brokers are demoted automatically; the cluster transitions to healthy partition replicas without data loss.

**37. How do you isolate the performance impact of high-frequency options traders from retail investors?**

Implement **infrastructure multi-tenancy isolation** at API routing layers. Institutional and HFT accounts route through dedicated gateway endpoints backed by isolated microservice and database replica pools.

**38. How do you handle edge-case orders that cross market close boundaries, such as Good-Till-Cancelled (GTC) trades?**

Standard daily orders are canceled by nightly settlement engines. GTC orders persist in a dedicated store; pre-market initialization engines reload them into hot memory cache and re-route to the exchange book each morning.

**39. What is your architectural response to catastrophic failure of the primary cloud provider region?**

Maintain an automated **multi-region DR strategy**. The primary region streams data asynchronously to a mirrored secondary region. On total outage, automated tools update global DNS and bring backup environments online with minimal downtime.

**40. Why use fixed-point data types instead of floating-point numbers for currency valuations?**

Floating-point types introduce subtle rounding errors from binary base-2 conversion. PostgreSQL `NUMERIC` and Java `BigDecimal` enforce arbitrary-precision fixed-point math for exact ledger correctness.

---

## Edge Cases & Production Philosophy (41–50)

**41. How do you design user watchlists to scale when users follow hundreds of high-volatility stocks?**

Use an **in-memory bitmask filtering system** on gateway nodes. Register a unified subscription covering the asset directory; as prices update, bitmask checks filter irrelevant ticks and fan out only relevant movements per user connection.

**42. How do you protect the system from memory spikes during large end-of-day report generation?**

Isolate reporting workloads on a dedicated read-only database instance. Reporting services use **streaming data cursors** to fetch rows in small batches rather than loading entire datasets into application memory.

**43. Why use structural interfaces instead of concrete classes for core domain validation models?**

Interface contracts decouple trading business logic from technical implementations, enabling mock substitution in tests and stack swaps without changing primary business services.

**44. How do you minimize processing latencies inside core Java-based microservices?**

Use custom **object memory pools** for frequent transactional types (order envelopes, context tokens). Reusing pre-allocated references reduces allocation churn and keeps garbage collection pauses short and predictable.

**45. What strategy ensures smooth, zero-downtime updates for stateful WebSocket server tiers?**

Deploy **blue-green canary rolling updates**. Spin up new server tiers alongside production; migrate connections gradually via edge routing. Old servers remain online until active sessions drop naturally.

**46. How do you protect data pipelines against corrupted payloads from software updates?**

Enforce **schema verification** via Apache Avro or Protocol Buffers registries. Every service validates payloads against central schema definitions before publishing; the registry enforces backward compatibility rules.

**47. Why use container platforms like Kubernetes instead of bare-metal servers?**

Bare-metal offers raw performance but lacks agility for volatile market traffic. Kubernetes provides automated self-healing, resource isolation, and rapid orchestration for safe deployments at scale.

**48. How do you handle edge-case cancellations when a user pulls an order at the exact millisecond it executes?**

The exchange order book is the absolute source of truth. If cancellation and execution cross paths, the exchange processes one first and rejects the other. OMS reconciles via inbound Kafka confirmations and corrects the ledger balance.

**49. How do you verify system capacity readiness ahead of major high-volume market events?**

Run automated **end-to-end production stress tests** during off-market hours. Distributed load generators simulate market-crash traffic volumes to locate bottlenecks and optimize resource configurations before live trading resumes.

**50. What core philosophy guides decisions when balancing performance against implementation complexity?**

Follow **pragmatic, production-grade architecture**: avoid complex theoretical scaling until operational metrics prove necessity. Prioritize data correctness and ironclad integrity above all else, keeping solutions maintainable as the user base grows.

---

## Related Reading

- [Designing a Stock Broker Trading Platform at Scale](/system-design/stock-broker-trading/) — full architecture, capacity planning, and failure modes
- [Designing an E-Commerce Platform at Scale](/system-design/ecommerce/) — adjacent checkout and ledger patterns
- [Designing a Food Delivery Platform at Scale](/system-design/food-delivery/) — real-time telemetry fan-out and WebSocket scaling patterns
