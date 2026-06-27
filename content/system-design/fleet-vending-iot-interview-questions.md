---
title: "IoT Fleet Vending Ecosystem — Interview Questions"
date: 2026-06-27T12:30:00+00:00
draft: false
description: "Senior-level system design interview questions and answers for an IoT-enabled fleet vending ecosystem — edge-offline operation, PCI isolation, MQTT/Kafka ingestion, and inventory consistency."
tags: ["system-design", "interview", "distributed-systems", "iot", "kafka", "mqtt"]
categories: ["System Design"]
---

Companion Q&A for [Designing an IoT-Enabled Fleet Vending Ecosystem at Scale](/system-design/fleet-vending-iot/). These questions probe edge state machines, offline payment risk budgets, PCI scope isolation, telemetry ingestion at 50K RPS, and production failure recovery — the topics interviewers dig into after the whiteboard diagram.

---

## Edge Architecture & Offline Operation (1–10)

**1. If a machine loses power mid-dispense, how does the system reconcile inventory state?**

Infrared drop sensors at the bottom of the chute detect a successful dispense. If a coil turns but the sensor fails to register an item break, the edge controller aborts the transaction, rolls back the local inventory deduction, and reverses the payment hold. On reboot, the machine runs a self-diagnostic sequence and uploads a stuck-item alert to the cloud.

**2. Why must core vending operations work during complete network isolation?**

Cellular LTE/5G backhaul on mobile edge networks experiences intermittent total blackout periods. Cash-based revenue cannot depend on cloud availability. The edge controller maintains a local SQLite inventory store and a state machine that completes the full select-pay-dispense loop without any cloud round-trip.

**3. How do you prevent duplicate dispensing of the final inventory unit?**

Local database mutations use SQLite `BEGIN IMMEDIATE` transactions. The inventory decrement and dispense command are wrapped in a single ACID transaction — if the dispense fails (sensor miss, motor fault), the transaction rolls back and quantity is restored.

**4. Why use a State Pattern with a ReentrantLock instead of synchronized methods on a single controller class?**

Hardware events arrive from multiple threads — MDB polling, payment callbacks, and UI input. The State Pattern isolates valid transitions per lifecycle phase (Ready → PaymentPending → Dispensing → Ready). The `ReentrantLock` ensures exactly one state mutation executes at a time without blocking unrelated read-only queries.

**5. Why dedicate single-threaded executors for MDB hardware polling?**

The Multi-Drop Bus is a shared serial interface. Concurrent writes from multiple threads cause frame corruption and unpredictable peripheral behavior. A single-threaded executor serializes all MDB commands while the business-logic state machine runs on a separate thread pool.

**6. How does the edge handle dynamic pricing updates while a transaction is in progress?**

The price is snapshotted at item selection time and stored in the transaction context. A cloud-pushed price change updates the `local_inventory.price_cents` column but does not retroactively alter an in-flight transaction. The state machine rejects selection if the slot becomes unavailable between select and payment.

**7. What happens when local flash exceeds 80% capacity during an extended outage?**

The circular telemetry log buffer drops low-priority debugging logs first to preserve high-priority transaction records and inventory snapshots. Once connectivity restores, queued events drain with exponential backoff to avoid overwhelming the cloud ingestion plane.

**8. Why is gRPC over Unix Domain Sockets preferred for internal edge IPC?**

Domain sockets avoid TCP overhead on localhost and provide typed contracts via protobuf. Asynchronous gRPC allows the payment service, inventory service, and hardware adapter to communicate without blocking the main dispensation thread.

**9. How does dual-bank flash protect against firmware upgrade failures?**

The edge gateway maintains active and passive OS layers on independent flash partitions. If the primary bank corrupts during an OTA update, a hardware watchdog triggers automatic fallback to the secondary bank, restoring the last known-good firmware.

**10. Why must a broken coil motor not halt cash validation?**

Peripheral faults must be fault-isolated. The edge controller marks the affected coordinate as `UNAVAILABLE` in local inventory and continues accepting cash for operational slots. This follows the bulkhead pattern — one hardware failure does not cascade to the entire machine.

---

## Payments & PCI Compliance (11–20)

**11. How do you handle card processing during cellular blackouts?**

Store-and-forward processing is allowed up to a **$20 risk threshold**. Below that limit, the EMV terminal authorizes offline using its internal risk parameters and queues the settlement record locally. Above $20, card transactions are denied until connectivity restores.

**12. How does the design keep the edge controller out of PCI audit scope?**

The credit card terminal operates on a secure, firewalled PCI bus. Card numbers are encrypted at the point of interaction (P2PE) inside the certified hardware security module and transmitted directly to the bank gateway. The edge controller never sees plaintext PAN data.

**13. Why accept cash, EMV chip, tap, magnetic stripe, and digital wallets on the same machine?**

Each payment modality has different failure and offline characteristics. Cash works without network. EMV chip provides strong offline cryptograms. Digital wallets (Apple Pay, Google Pay) tokenize card data. Supporting all modalities maximizes revenue capture across diverse customer preferences and connectivity conditions.

**14. How is idempotency handled for cash payment retries?**

The client generates a `transaction_id` before inserting cash. If the network fails during cloud sync, repeating the exact transaction token prevents multiple coin-return runs. The idempotency token is persisted in local SQLite before the hopper dispenses change.

**15. What is the reconciliation flow when offline card transactions reconnect?**

Queued settlement records drain to the Financial Clearing Service via Kafka. The service performs ACID ledger writes to PostgreSQL and forwards batches to the third-party processor. Anomaly detection flags devices with unusually high offline authorization counts.

**16. Why is a $20 offline risk threshold a reasonable starting point?**

It balances revenue capture during brief outages against chargeback exposure. Vending transactions are typically low-ticket ($1–$5). A $20 ceiling covers multi-item purchases while limiting per-device fraud surface. The threshold should be tunable per region based on chargeback data.

**17. How does change dispensation interact with the state machine?**

After cash insertion meets or exceeds the snapshotted price, the controller transitions to a `ChangeDispensing` sub-state. The hopper dispenses exact change, records the idempotency token, decrements inventory, and only then triggers the coil motor. Each step is atomic within the SQLite transaction boundary.

**18. Why route card settlements through a Financial Clearing Service instead of directly from the edge?**

Centralizing settlement provides ACID ledger guarantees, fraud analytics, batch reconciliation with the processor, and a single integration point for PCI-compliant audit trails. The edge only queues events; the cloud owns financial truth.

**19. How do you prevent a malicious actor from replaying offline transaction records?**

Each transaction record includes a device-signed payload with a monotonic sequence number stored in the TPM-backed keystore. The clearing service rejects records with duplicate sequence numbers or invalid signatures.

**20. What happens if the coin hopper runs out of change during a transaction?**

The state machine transitions to an error state, refunds the inserted cash (or offers alternate payment), and emits a critical `OUT_OF_CHANGE` telemetry alert. The slot remains reserved until the transaction is explicitly cancelled or completed.

---

## Cloud Ingestion & Scale (21–30)

**21. How do you prevent distributed lock exhaustion if 100,000 devices reconnect simultaneously after an outage?**

Devices use randomized exponential backoff with jitter before attempting reconnection. Connection state handling is decoupled from database writes — incoming status events land in Kafka topics, and backend consumers update fleet records at a sustainable pace without overloading PostgreSQL.

**22. Why choose an asynchronous event-driven pattern for cloud transactions instead of synchronous REST?**

Cellular connections drop frequently. A synchronous REST call that blocks until the cloud responds causes connection timeouts and freezes the device UI. An asynchronous pattern lets the device fire a transaction event, track status locally, and listen for a confirmation over MQTT without blocking local processing loops.

**23. Why MQTT over a managed IoT hub instead of REST polling from the edge?**

MQTT is lightweight, supports bidirectional push (critical for config updates), and handles intermittent connectivity with built-in QoS levels. REST polling wastes bandwidth and battery on 500,000 devices checking for updates every few seconds.

**24. How does Kafka buffer the 50,000 peak events/sec telemetry stream?**

Kafka's sequential disk append log absorbs burst traffic independently of downstream database write speed. Telemetry Processor pods consume at their own pace, and TimescaleDB writes do not block the IoT hub ingestion path.

**25. Why PostgreSQL with TimescaleDB instead of Cassandra for the cloud data plane?**

The control plane requires strict ACID enforcement for financial ledger records. TimescaleDB layers optimized time-series hypertables directly over the Postgres engine, providing both transactional integrity and high-throughput telemetry ingestion without operating a separate database technology.

**26. Why reject Cassandra for the financial ledger specifically?**

Cassandra lacks cross-row ACID mechanics. Distributed ledger reconciliation — linking a transaction to an inventory decrement to a payment settlement — requires multi-row atomicity that Cassandra's eventual-consistency model cannot guarantee without complex application-level sagas.

**27. How do Snowflake IDs improve indexing performance over UUID v4?**

Snowflake IDs are time-sortable 64-bit integers. B-tree indexes on PostgreSQL remain compact and append-mostly. UUID v4 values are random, causing index page splits and fragmentation under high write volume.

**28. What is the purpose of the composite index on `telemetry_stream(machine_id, timestamp DESC)`?**

Operational dashboards query "show me the last 24 hours of telemetry for machine X." The composite index enables index-only scans for this access pattern without sorting, keeping dashboard queries sub-second even at 262 TB/year ingestion scale.

**29. Why decouple telemetry writes from transactional writes in Kafka?**

Telemetry (1.44B events/day) and transactions (30M/day) have different consumers, retention policies, and failure tolerance. Separate topics (`telemetry.raw`, `transactions.events`) allow independent scaling, replay, and retention without cross-contamination.

**30. How does the 3× peak factor translate to infrastructure sizing?**

Average telemetry RPS is ~16,666. Multiplying by 3× accounts for fleet-wide heartbeat alignment (devices booting at similar times), regional reconnect storms, and promotional event spikes. This yields ~50,000 peak RPS, driving the 150-pod telemetry processor allocation.

---

## Security, HA & Failure Recovery (31–40)

**31. How does mutual TLS with TPM 2.0 protect the fleet?**

Each edge device is provisioned with an X.509 private key stored inside a hardware Trusted Platform Module. All cloud communication requires bidirectional mTLS — the cloud verifies the device identity, and the device verifies the cloud endpoint. No inbound ports are open on the edge gateway.

**32. What are the disaster recovery targets and how are they achieved?**

RPO ≤ 1 minute; RTO ≤ 15 minutes. Continuous WAL streaming from PostgreSQL to encrypted S3 buckets provides sub-minute recovery point. Nightly snapshots plus automated failover to synchronous standby achieve the 15-minute recovery time objective.

**33. How do you mitigate cloud split-brain during a multi-region network partition?**

Shards that drop below majority voter connection counts immediately transition to read-only mode, rejecting new data mutations until consensus recovers. This prevents conflicting inventory or financial writes across isolated regions.

**34. What SLIs and SLOs should be monitored for this system?**

SLIs: edge-to-cloud telemetry persistence latency, fleet administration API error rate, Kafka consumer lag. SLOs: 99.9% of telemetry events persisted in ≤ 500 ms; 99.95% fleet administration API availability over a trailing 30-day window.

**35. How does OpenTelemetry tracing work across edge and cloud boundaries?**

The `transaction_id` acts as a trace context propagation header. Edge proxies inject the span, MQTT bridges forward it as a message attribute, Kafka consumers continue the trace, and database writers record the final span — enabling end-to-end debugging across network boundaries.

**36. Why use cache-aside for fleet configuration instead of write-through?**

Configuration reads are frequent (every device boot, every pricing refresh) but writes are rare (administrator updates). Cache-aside avoids writing to Redis on every telemetry heartbeat. On admin write, the service invalidates the specific Redis key immediately and pushes via MQTT.

**37. What triggers the transition from Phase 3 (TimescaleDB partitioning) to Phase 4 (app-level sharding)?**

When cross-continental latency degrades operations for devices outside the primary host region. Sharding by `machine_id % number_of_shards` routes each device's reads and writes to a geographically proximate database cluster.

**38. How does the system handle a compromised edge device?**

TPM-backed mTLS credentials can be revoked centrally. The IoT hub rejects connections from revoked device certificates. The fleet management service marks the machine as `QUARANTINED`, and the operational dashboard alerts the security team.

**39. Why is a 30-second heartbeat interval the right balance?**

Shorter intervals (5s) multiply telemetry volume by 6× with marginal operational benefit. Longer intervals (5 min) delay detection of critical failures (temperature spikes, out-of-change). Thirty seconds yields 1.44B events/day — manageable at 50K peak RPS with the sized Kafka cluster.

**40. What is the architectural difference between this design and a single-machine vending prototype?**

A prototype treats the vending machine as an isolated island. This design implements strict architectural boundaries (gRPC hardware abstraction, PCI-isolated payment bus, async cloud sync), scales to 500,000 devices with a dedicated telemetry plane processing billions of data points daily, and includes resilient offline security with local databases, risk-budgeted card processing, and transactional state machines.

---

## Advanced Discussion (41–50)

**41. When would you move from Phase 6 active-active to a simpler active-passive multi-region model?**

If the business does not require sub-second cross-region inventory visibility and can tolerate eventual consistency for fleet dashboards. Active-passive reduces operational complexity and eliminates split-brain risk at the cost of higher failover latency.

**42. How would you test the offline card risk threshold in production?**

Shadow mode: process offline authorizations normally but also send them to a fraud scoring service asynchronously. Compare chargeback rates across threshold buckets before adjusting the $20 limit per region.

**43. Why is Kafka preferred over RabbitMQ for telemetry replay?**

Kafka's immutable log allows analytical systems to recalculate past events from any offset without interfering with operational consumers. RabbitMQ excels at complex routing but struggles with high-volume persistence and historical replay at 50K events/sec.

**44. How do you handle inventory sync conflicts when a machine was offline for 72 hours?**

On reconnect, the edge uploads a batch inventory snapshot. The cloud compares it against the last known state. Discrepancies beyond a tolerance threshold (e.g. > 2 units per slot) trigger an operational alert for manual audit rather than automatic overwrite — preventing cloud-side errors from corrupting ground truth.

**45. What is the role of the circular log buffer on edge flash?**

It provides FIFO-ordered durable storage for telemetry and transaction events during outages. When capacity is reached, low-priority entries are evicted first. The buffer is designed to survive at least 7 days of disconnected operation at average transaction volume.

**46. How does the Fleet Configuration Service push updates to specific machines vs entire regions?**

MQTT topic hierarchy: `fleet/{machine_id}/config` for individual updates, `fleet/region/{region_id}/config` for bulk regional changes. Devices subscribe to both their machine-specific topic and their regional topic on boot.

**47. Why size Redis at 6 shards with 16 GB RAM overhead per partition?**

The 2 GB fleet config dataset is small, but Redis also serves rate-limit counters, connection state caches, and config-push pub/sub channels. Shard overhead accounts for replication buffers, AOF rewrite memory spikes, and headroom for fleet growth to 1M devices.

**48. How would you implement time-of-day pricing without restarting in-flight transactions?**

The configuration payload includes a `effective_at` timestamp and a price schedule array. The edge controller applies the new schedule at the specified time. In-flight transactions retain their selection-time price snapshot.

**49. What metrics would you alert on for the coin hopper and cash acceptor?**

`hopper_level_cents` (alert below minimum change threshold), `bill_validator_jam_count` (alert on consecutive jams), `cash_box_full` (alert before overflow). These are high-priority telemetry fields that bypass the low-priority drop policy during flash pressure.

**50. How does this design support 30 million daily transactions without overloading the financial ledger?**

30M writes/day is ~347 WPS average — well within PostgreSQL capacity. The Financial Clearing Service batches card settlements to the third-party processor. Kafka absorbs peak bursts, and Snowflake IDs keep B-tree inserts sequential. The bottleneck is telemetry (50K RPS), not transactions.
