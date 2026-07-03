---
title: "Distributed Email Delivery System Design — Interview Questions"
date: 2026-06-27T12:30:00+00:00
draft: false
description: "Senior-level system design interview questions and answers for a Gmail/Outlook-scale distributed email delivery platform."
tags: ["system-design", "interview", "distributed-systems", "kafka", "postgresql"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Distributed Email Delivery System at Scale](/system-design/email-delivery/). These questions probe outbox patterns, Kafka decoupling, attachment offloading, BCC privacy, search architecture, SMTP relay resilience, and production failure recovery — the topics interviewers dig into after the whiteboard diagram.

---

## Architecture & Trade-offs (1–10)

**1. Why use Kafka for outbox processing instead of writing directly to downstream microservices over HTTP?**

Direct HTTP calls couple services tightly. If downstream validation or SMTP services slow down or fail, the ingress transmission service blocks threads, quickly exhausting resources and dropping requests. Kafka decouples the process — it acts as a durable buffer, allowing the system to accept incoming emails immediately while downstream workers consume and process events at an optimal rate.

**2. How does the system handle "noisy neighbor" issues if an enterprise account suddenly sends millions of emails simultaneously?**

Rate-limiting pools at the API gateway and separate Kafka topics for standard and high-volume users. If an account exceeds configured rate limits, its traffic routes to a lower-priority queue with capped processing workers. Large delivery bursts are isolated and do not degrade performance for standard users.

**3. Why is UUIDv7 preferred over UUIDv4 or standard auto-incrementing IDs for indexing emails?**

Auto-incrementing IDs expose total transaction volumes and leak system data if exposed in public APIs. UUIDv4 avoids this but generates random values that cause high fragmentation in database B-tree indexes. UUIDv7 includes a 48-bit timestamp prefix, combining global uniqueness with natural time ordering — the database appends records sequentially, maximizing cache efficiency and indexing performance.

**4. What happens if an email contains multiple large attachments? How do we avoid overloading the transactional database?**

The client does not upload raw binary files through the main email generation endpoint. Instead, it requests a pre-signed, multi-part upload URL pointing directly to an isolated S3 object storage bucket. The client uploads attachments directly to S3 and receives an immutable reference ID. Only this ID is sent in the final email payload, keeping transactional database records lightweight and predictable.

**5. How do we safely execute full-text search across billions of historical messages without introducing high query latencies?**

We do not perform runtime `LIKE` queries against primary relational shards. An offline data pipeline streams finalized message records into an optimized Elasticsearch cluster. Elasticsearch splits text into inverted indexes, allowing keyword evaluation across millions of documents within milliseconds — completely separating search workloads from core transactional databases.

**6. Why is the outbox pattern necessary instead of publishing to Kafka directly from the send API?**

Dual-write risk: broker publish can succeed while the DB rolls back (or vice versa). [Transactional Outbox Overview](/system-design/transactional-outbox-overview/) — same-transaction outbox row + CDC relay.

**7. Why shard by `owner_user_id` instead of `message_id`?**

A user's inbox, sent folder, and metadata all query by `owner_user_id + folder_type + received_at`. Co-locating all metadata for a user on one shard enables single-shard timeline queries. Sharding by `message_id` would scatter a single user's mailbox across every shard, requiring expensive scatter-gather on every inbox load.

**8. How does the system enforce global email address uniqueness under CP requirements?**

The `users` table enforces a unique index on `email_address`. Registration flows write to a single authoritative shard (or a dedicated identity service) with synchronous replication across availability zones. A duplicate insert returns `409 Conflict` before any mailbox is provisioned.

**9. Why accept eventual consistency for delivery but not for onboarding?**

Duplicate email handles create permanent identity conflicts that are expensive to resolve. A few seconds of inbox delivery lag is invisible to most users and can be masked with optimistic UI ("Sending..."). Blocking composition or dropping a send interaction is not tolerated.

**10. Why separate `mailbox_messages` from `mailbox_metadata`?**

The message body is immutable and shared conceptually across sender and recipients, while each user has independent folder placement, read state, and timestamps. Denormalizing into a per-user metadata row avoids wide-row updates on the message body and enables efficient `owner_user_id + folder_type + received_at` index scans.

---

## Delivery Pipeline & Protocols (11–20)

**11. How are BCC recipients handled to preserve privacy?**

At the delivery routing stage, the BCC field is stripped from the message envelope for all recipients except the sender's own Sent-folder record. Internal routing fans out individual deliveries per recipient with sanitized headers.

**12. What happens when an external MX server is unreachable?**

SMTP relay workers retry with exponential backoff and jitter. Messages remain in the delivery queue. After repeated failures over a 72-hour window, the message is removed from the active queue and a bounce notification is returned to the sender.

**13. How does internal (same-domain) delivery differ from external delivery?**

Internal delivery writes directly to `mailbox_messages` + `mailbox_metadata` via the Inbound Delivery Consumer — no SMTP hop. External delivery routes through the SMTP Relay Worker Cluster after MX resolution. The Smart Routing Engine branches at the Kafka consumer based on recipient domain.

**14. Why run spam, DLP, and attachment validation in parallel?**

These checks are independent and may involve external service calls with variable latency. `CompletableFuture.allOf` (or equivalent) runs them concurrently. The orchestrator commits validation traces to a ledger only after all complete, preserving an audit trail.

**15. How does the S3 malware scanner integrate with the send pipeline?**

Files are scanned asynchronously on S3 object-create events. Results are written to S3ValidationDB. During send, the Attachment Scanner Gateway reads pre-computed flags — if a scan is still pending, the orchestrator can defer or reject based on policy.

**16. What is the purpose of the Validation Ledger?**

It records per-step outcomes (spam check, DLP, attachment scan) for each `message_id`. This supports debugging, compliance audits, and idempotent replay — consumers can detect already-validated messages and skip redundant work.

**17. How does idempotency on `POST /emails/send` work?**

The client sends `X-Idempotency-Key`. The ingress service performs `SETNX` in Redis with a 24-hour TTL. On duplicate key, the service returns the original `message_id` and `QUEUED` status without re-enqueueing.

**18. Why return `202 Accepted` instead of `200 OK` on send?**

Delivery is asynchronous. `202` correctly signals that the request was accepted for processing but not yet completed. The client can poll or receive a push notification when the message lands in the recipient's inbox.

**19. How are email threads constructed?**

Each message carries a `thread_id`. Replies inherit the parent's `thread_id` (or the parent's `message_id` for the first reply). The UI groups messages by `thread_id` sorted by `received_at`.

**20. Why is bulk/marketing email excluded from this design?**

Bulk traffic has different throughput, reputation, and compliance profiles. Mixing it with conversational mail risks IP blacklisting and noisy-neighbor degradation. Bulk senders are throttled or routed to dedicated external pools.

---

## Storage, Caching & Search (21–30)

**21. Why PostgreSQL for mailbox storage instead of MongoDB?**

Email metadata relies on predictable relational mappings, timestamp-sorted indexes, and strict transactional dual-writes between `mailbox_messages` and `mailbox_metadata`. Modern sharded PostgreSQL handles massive write throughput while guaranteeing exact query constraints.

**22. Why Cassandra for outbox/archive logs?**

Cassandra's LSM-tree storage provides linear append speeds ideal for high-volume immutable logs. Structured, relation-heavy operational layouts remain on PostgreSQL; Cassandra handles the firehose of pipeline trace data.

**23. How big is the Redis directory cache and what does it store?**

Approximately **6.4 TB** globally — 500M DAU × 100 cached contact entries × 128 bytes per entry. It stores active directory mappings for auto-suggestions and top contact records.

**24. What cache eviction policy is used?**

Least Recently Used (LRU) with an explicit 2-hour sliding TTL. Active sessions stay responsive; inactive directory lookups are automatically removed.

**25. How is cache invalidation handled for profile updates?**

Updates to account profiles or contact directories trigger an immediate `DEL` on affected Redis keys, forcing subsequent requests to fetch fresh data from the database shard.

**26. Why not store attachment bytes in PostgreSQL?**

A 2 MB average attachment at 10% prevalence adds ~1 PB/day of blob traffic. Object storage (S3) is purpose-built for large binary assets with pre-signed direct upload, keeping the transactional engine lightweight.

**27. How does the Aggregator/ETL pipeline feed Elasticsearch?**

It consumes change streams from `mailbox_messages` and `mailbox_metadata`, flattens them into search documents (sender, recipients, subject, body snippet, timestamp, folder), and bulk-indexes into Elasticsearch. Search never touches the primary DB.

**28. How do you handle search index lag?**

A few seconds of lag is acceptable for email search. The UI can show recently sent messages from the mailbox API while the search index catches up. Correlation IDs track indexing delay in observability dashboards.

**29. What composite index drives inbox timeline queries?**

`CREATE INDEX idx_owner_folder_time ON mailbox_metadata (owner_user_id, folder_type, received_at DESC)` — a single index seek returns the user's folder sorted by time.

**30. How is draft autosave optimized for ≤ 200 ms P99?**

Drafts write to a fast NoSQL/draft cache store (not the heavy mailbox shard). Autosave is a lightweight upsert keyed by `draft_id` without entering the outbox pipeline.

---

## Security, Reliability & Operations (31–40)

**31. What rate limits protect the system from abuse?**

Standard users: max **20 API submissions/second**. Outbound sends: max **100 executions/minute**. Enforced via sliding-window counters in Redis at the API gateway.

**32. How is data encrypted?**

TLS 1.3 for all transport lanes; internal SMTP uses STARTTLS. At rest: AES-256 on storage arrays. Sensitive fields (password hashes, access keys) are encrypted at the application layer before disk write.

**33. What happens during a Kafka cluster outage?**

Application services fall back to localized dead-letter queues on persistent block storage. Once brokers recover, background workers drain and replay buffered transactions — no accepted send is lost.

**34. What are the RTO and RPO targets?**

RTO ≤ 30 seconds for AZ failover; ≤ 15 minutes for regional outage. RPO = 0 within a local zone cluster (sync replication); ≤ 1 second for catastrophic multi-region recovery (async cross-region stream).

**35. How does `X-Correlation-ID` support debugging?**

The API gateway stamps every request with a unique correlation ID that propagates through all internal services, Kafka streams, and validation queues — enabling end-to-end traces in OpenTelemetry/Jaeger.

**36. What SLOs does the system commit to?**

Ingress availability: **99.99%**. Internal delivery: **99%** of same-domain transmissions readable within **≤ 2.0 seconds**. Draft ingestion: **P99 ≤ 200 ms**.

**37. How do you prevent compromised accounts from sending spam?**

Per-user rate limits, outbound send caps (100/min), spam scoring on every message, and automatic account throttling when anomaly detection triggers. Enterprise noisy-neighbor isolation via separate Kafka topics.

**38. Why OAuth2 + JWT instead of session cookies for API auth?**

Stateless JWT validation at the API gateway avoids session store lookups on every request — critical at ~694K peak read RPS. Short-lived tokens with refresh flows balance security and performance.

**39. What happens if Elasticsearch and the search API are both down?**

Core mail read/write continues unaffected. The search endpoint returns a graceful degradation response. Index updates queue in Kafka for catch-up indexing on recovery.

**40. How would you add IMAP/POP3 support to this architecture?**

IMAP/POP3 gateways would be read-heavy adapter services sitting in front of the same `mailbox_metadata` + `mailbox_messages` shards. They translate folder/list/fetch commands into the existing data model without changing the core send pipeline.

---

## Scaling & Advanced Topics (41–50)

**41. When do you move from read replicas to horizontal sharding?**

When single-instance write throughput is exhausted or per-shard table space exceeds ~2 TB. Phase 4 entry: `Shard_ID = MurmurHash3(owner_user_id) % Total_Shards`.

**42. What triggers multi-region active-passive deployment?**

Multi-continent latency concerns (Phase 5). Primary region handles writes; async replication serves read outposts. Phase 6 (active-active) requires anycast routing and conflict resolution for concurrent draft edits.

**43. How many Kafka partitions are needed at peak?**

Core topics use at least **48 partitions** to allow parallel consumer processing. At ~520K peak events/sec, partition count and broker count (15 NVMe brokers) are sized together to avoid per-partition bottlenecks.

**44. How many application pods serve the ingress tier?**

**120 pods** (2 vCPU, 4 GB RAM each), auto-scaling when average CPU crosses 70%. Sized for ~173K peak ingress write RPS.

**45. Why decouple attachment upload from the send API (vs single-transaction upload)?**

Uploading 25 MB through the compose API causes frequent timeouts, ties ingress threads to slow client uploads, and bloats API gateway memory. Pre-signed S3 URLs let clients upload directly to object storage in parallel while drafting.

**46. How do you handle a user with millions of messages in one folder?**

Pagination via `received_at` cursor (not offset) on `idx_owner_folder_time`. Cold messages archive to cheaper storage tiers. Optional per-user shard splitting if a single mailbox exceeds shard capacity.

**47. What is the difference between the Kafka Ingress Topic and Delivery Topic?**

Ingress Topic carries raw outbox events entering the validation pipeline. Delivery Topic carries sanitized, validated events ready for the Smart Routing Engine. Separating them allows independent scaling and replay of validation without re-processing delivery.

**48. How would you implement read receipts?**

A separate lightweight event table (or metadata flag) keyed by `(message_id, recipient_user_id)`. The read action updates `is_read` in `mailbox_metadata` and optionally publishes a notification event to the sender — kept off the hot send path.

**49. What monitoring metrics are most critical?**

Kafka consumer lag (pipeline delay), ingress P99 latency, internal delivery velocity SLO compliance, SMTP relay failure rate, Elasticsearch indexing lag, Redis cache hit ratio, and outbox table depth (CDC backlog indicator).

**50. If you had to cut scope for an MVP, what would you defer?**

Full-text search (Elasticsearch + ETL), external SMTP delivery (internal-only first), S3 async malware scanning (inline scan stub), multi-region active-active, and thread grouping. Core MVP: register, draft, send, internal delivery, folder views, and basic attachments via pre-signed URLs.
