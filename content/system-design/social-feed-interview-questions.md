---
title: "Social Graph & Feed System Design — Interview Questions"
date: 2026-06-27T10:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a Facebook/Instagram-scale social graph and feed application."
tags: ["system-design", "interview", "distributed-systems", "architecture", "redis", "kafka"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Social Graph & Feed Application at Scale](/system-design/social-feed/). These questions probe hybrid fan-out, celebrity pull paths, cursor pagination, engagement counter pipelines, and production failure handling — the topics interviewers dig into after the whiteboard diagram.

---

## Fan-Out & Feed Generation (1–10)

**1. How do you handle hot keys when a celebrity with 100M followers posts a video?**

We use hybrid fan-out. Instead of copying the post ID into 100 million follower feeds, Fan-out Worker records it in Celebrity Store. On a feed read, Feed Service merges precomputed Redis Feed IDs with recent Celebrity Store IDs and recommendations, then hydrates the selected IDs through Post Service.

**2. What happens if a fan-out worker crashes halfway through processing a message?**

Kafka consumer offsets are committed only after the Fan-out Worker's idempotent batch write is acknowledged by Redis Feed or Celebrity Store. If a worker fails mid-batch, Kafka reassigns the uncommitted partition to another consumer. The batch is replayed under at-least-once delivery, and deterministic Sorted Set members prevent duplicate feed entries.

**3. How do you prevent cursor drift when a user scrolls their feed while new posts are arriving?**

We use a signed, versioned opaque cursor containing the last `(created_at, post_id)` pair rather than a numeric offset. The next page applies `created_at < :time OR (created_at = :time AND post_id < :id)` under the same descending order. The post ID is a deterministic tie-breaker, so new arrivals do not shift items already traversed.

**4. Why use ScyllaDB for posts instead of a relational database with partitioning?**

Post generation is write-intensive and its access paths are predictable. ScyllaDB's LSM-tree engine converts random mutations into sequential writes and scales horizontally. Post Service maintains denormalized `posts_by_author` and `posts_by_id` projections for chronological author scans and bounded feed hydration; this trades joins and ad hoc queries for predictable throughput and latency.

**5. How do you implement a "Like" counter without causing database lock contention?**

We avoid hot-row updates such as `UPDATE posts SET likes = likes + 1`. Like Service and Comment Service update Redis Counters with `HINCRBY` and publish `like-created` or `comment-created`. Post Service's engagement projection consumer batch-flushes durable deltas to ScyllaDB every 10 seconds; Kafka replay and idempotent event IDs support recovery.

**6. How do you defend against malicious or explicit image uploads at scale?**

Clients upload assets through presigned URLs into private S3 Raw storage. An asynchronous `media-uploaded` workflow validates, moderates, and transforms the object. Approved derivatives are written to S3 Processed and served through the CDN; rejected objects remain private and are removed according to lifecycle policy.

**7. What is your strategy for caching the social graph relationships?**

PostgreSQL is the system of record for the follow graph. Redis caches active following lists as Sorted Sets under `graph:following:{user_id}`, with followed IDs scored by follow timestamp. User Service owns both the cache-aside lookup and invalidation on `follow-created`, `follow-deleted`, and block events.

**8. How does the system handle an active-active cross-region database split?**

We avoid unconstrained multi-writer semantics. Reconstructable feeds remain AP-leaning and converge from replicated events, while account and follow-graph writes use home-region ownership, fencing tokens, and controlled regional failover. ScyllaDB replication handles post-domain availability; PostgreSQL profile mutations retain a single authoritative writer to prevent split brain.

**9. Why use Envoy as the API Gateway data plane?**

API Gateway uses Envoy for HTTP/2 and gRPC upstream multiplexing, dynamic xDS configuration, distributed-tracing integration, and circuit breaking. The choice does not eliminate application-level authentication, authorization, validation, or idempotency enforcement.

**10. How do you handle cache stampedes on popular post items?**

We combine request coalescing, short leased locks with fencing tokens, probabilistic early refresh, and jittered TTLs. Circuit breakers prevent a miss storm from overwhelming PostgreSQL or ScyllaDB, while stale-but-valid or reduced feeds provide graceful degradation.

---

## Caching & Recovery (11–20)

**11. What happens if the pre-computed feed cache is destroyed completely?**

Feed Service performs a bounded on-demand rebuild. It obtains followed-author IDs through User Service, recent post IDs through Post Service's Author Timeline Cache, celebrity IDs from Celebrity Store, and optional candidates from Recommendation Service. It merges and deduplicates those streams, repopulates Redis Feed, and uses request coalescing plus circuit breakers to protect PostgreSQL and ScyllaDB.

**12. How do you ensure idempotency for post creation under bad network conditions?**

Clients attach a UUID in `X-Idempotency-Key`. Post Service atomically reserves the key in the Idempotency Cache for the documented 24-hour replay window and associates it with a request fingerprint. An identical retry returns the original response; reuse with a different payload returns `409 Conflict`.

**13. How do you scale down infrastructure costs during off-peak night hours?**

We use Kubernetes Horizontal Pod Autoscalers (HPA) driven by custom Prometheus metrics (like request throughput and queue lag). Storage tiers switch to automated cold tiering policies on object storage networks for old media assets.

**14. What happens when a user deletes their account?**

Account deletion starts an asynchronous saga. User Service first marks the PostgreSQL account `DELETED` to block access, then reliably publishes `account-deleted`. Idempotent consumers purge graph edges, feeds, search and recommendation projections, and media according to retention and legal-hold policy.

**15. How do you handle pagination when a user blocks another user while scrolling?**

Feed Service applies the current block-state projection during candidate filtering and again during Post Service hydration. A block event invalidates graph and feed entries asynchronously; the hydration check prevents stale cached IDs from exposing blocked content on subsequent pages.

**16. Why choose PostgreSQL instead of a graph database for the follow network?**

We don't need a full graph database since our queries only require shallow, single-hop index scans (e.g., fetching direct followers). A normalized relational database with partial indexes handles this pattern efficiently without the operational complexity of a graph database.

**17. How do you protect your internal service microservices from cascading crashes?**

We isolate services with explicit deadlines, bulkheads, circuit breakers, and bounded retries with exponential backoff and jitter. Retries are limited to idempotent operations. Optional feed sources fail independently, allowing Feed Service to return a partial chronological feed instead of amplifying a dependency outage.

**18. How do you design a system to support "Infinite Scrolling" reliably?**

The client application requests feed pages using opaque cursors. The server returns a fixed chunk of feed metadata along with a token for the next page (`next_cursor`). As the viewport approaches the bottom of the rendered list, the client pre-fetches the next page token asynchronously.

**19. How do you handle timezone localizations for global chronological feeds?**

All system timestamps are unified, captured, and stored using UTC ISO 8601 formatting. The client application converts these UTC values to the local device timezone when rendering timestamps in the UI.

**20. What database choices support multi-region user profile mutations?**

User Service owns profiles in PostgreSQL. At multi-region scale, each account has an authoritative home region; cross-region replicas serve eligible reads, while fencing and controlled promotion preserve a single writer during failover. Data-residency policy determines placement and replication boundaries.

---

## Security & API Hardening (21–30)

**21. How do you catch API route parameter attacks or SQL injection threats?**

API Gateway enforces coarse OpenAPI shape, authentication, and request-size limits. Each business service still performs authoritative semantic validation and authorization, while PostgreSQL adapters use parameterized statements and ScyllaDB access uses bound CQL parameters.

**22. What caching strategy handles post metadata updates best?**

Post metadata is owned and hydrated by Post Service; Feed Service caches only post IDs. If Post Service introduces a metadata cache, it uses cache-aside with event-driven invalidation on `post-approved`, `post-rejected`, `post-deleted`, or processed-media changes. ScyllaDB remains authoritative.

**23. How do you track metrics across asynchronous workers?**

Services emit traces and metrics through OpenTelemetry SDKs and collectors. Prometheus scrapes metric endpoints, while trace context and event IDs propagate through Kafka headers. Dashboards and alerts track feed p99 latency, Kafka lag age, Redis hit ratio, dependency errors, and freshness SLOs.

**24. What happens if a user updates their profile picture?**

User Service commits the PostgreSQL update and publishes `profile-updated` through its reliable event-publication path. Consumers invalidate or refresh the Redis User Profile Cache; personalized profile data is not stored at the CDN edge.

**25. How do you scale media delivery for trending viral videos?**

Viral assets are cached at edge locations using geographically distributed CDN networks (such as Cloudflare or CloudFront) configured with origin shield architectures to shield primary storage buckets from high traffic spikes.

**26. Why do you use UUIDv7 or Snowflake IDs over standard database auto-increments?**

Standard auto-increments expose business metrics and create a centralized allocation dependency. Snowflake-style 64-bit IDs and 128-bit UUIDv7 IDs are time-sortable and can be generated without a database sequence; Snowflake requires worker-ID and clock discipline, while UUIDv7 has a larger storage footprint.

**27. How do you handle deep pagination requests efficiently?**

We bound the online feed window and page size, reject abusive cursor depth, and use keyset pagination rather than offsets. If historical browsing becomes a product requirement, it receives a separately capacity-planned archive API instead of falling through to unbounded scans on serving stores.

**28. How do you verify the health of microservices in your clusters?**

Kubernetes uses liveness probes only for unrecoverable local process failure and readiness probes to control traffic admission. Readiness reflects whether the instance can serve safely without requiring every optional dependency to be healthy; dependency health is monitored separately to avoid ejecting all pods during a shared outage.

**29. What happens if Kafka consumer lag grows severely?**

Consumers scale on lag age and backlog only up to the available partition count. If lag continues growing, the platform adds partitions or brokers where appropriate, throttles noncritical producers, and prioritizes moderation and fan-out over analytics. Kafka absorbs short bursts; sustained lag triggers admission control before retention or disk safety limits are breached.

**30. How do you manage secrets like API keys and database credentials safely?**

Secrets are delivered at runtime from a managed secret store such as HashiCorp Vault or AWS Secrets Manager using workload identity and least-privilege policies. Credentials and certificates rotate according to their risk policy, and applications support reload without embedding secrets in images or source control.

---

## Media, Operations & Cost (31–40)

**31. How do you handle large video files over slow mobile networks?**

The client uses S3 multipart upload with presigned part URLs, uploading directly to S3 Raw without a media-proxy service. Part checksums and the multipart upload ID support integrity verification and resume; abandoned uploads are removed by lifecycle policy.

**32. Why do you use Redis Sorted Sets for active user feeds?**

Sorted Sets store element values paired with numeric rankings. By mapping `post_id` entries to numeric generation timestamps, we can query chronological feed slices in O(log N + M) time using commands like `ZREVRANGEBYSCORE`.

**33. How do you measure system throughput health during traffic spikes?**

We track core metrics like request success rates (2xx vs 5xx errors), p99 latency spikes, and system saturation indicators (like thread usage and connection pool queuing delays).

**34. What is the operational impact of setting a short cache TTL?**

Short TTL values improve data freshness but increase cache miss rates, which raises the read load on backend databases during traffic spikes. We use longer TTLs combined with active event-driven invalidation to balance freshness and database load.

**35. How do you prevent internal service credentials from leaking across codebases?**

We isolate application dependencies using strict infrastructure-as-code configurations (like Terraform) combined with fine-grained IAM resource access controls.

**36. How do you profile performance degradation in production?**

We analyze system latency by running continuous, low-overhead production profiling tools (like Pyroscope) combined with sample tracing tokens injected through the OpenTelemetry framework.

**37. What happens if a user unfollows another user?**

User Service updates the PostgreSQL follow graph and publishes `follow-deleted`. Consumers invalidate the Follow Graph Cache and remove the author's IDs from the follower's Redis Feed asynchronously. The read path still applies current relationship and block visibility rules during hydration.

**38. How do you isolate operational traffic from business intelligence queries?**

Independent Kafka consumers load a dedicated analytical store or data lake. BI queries run there rather than against PostgreSQL, ScyllaDB, Redis, or OpenSearch serving clusters, preserving transactional and feed-path capacity.

**39. Why do you use mTLS inside your Kubernetes clusters?**

mTLS ensures all microservices authenticate each other using zero-trust principles, protecting internal service communication from spoofing or unauthorized packet sniffing.

**40. How do you maintain database connection limits under high load?**

We place database proxies like PgBouncer in front of PostgreSQL instances. These proxies pool and reuse database connections, preventing connection exhaustion under high traffic.

---

## Edge Cases & Architecture Trade-offs (41–50)

**41. What happens if a user rapidly toggles the "Like" button?**

The client application debounces the interaction locally. The API gateway also applies rate limits per user-post pair, dropping rapid toggle requests before they reach backend databases.

**42. How do you test the system for disaster recovery scenarios?**

We run scheduled recovery exercises for node, availability-zone, network, Kafka-lag, Redis-loss, and regional-failover scenarios. Tests begin in staging and progress to tightly scoped production experiments with abort conditions, validating runbooks, RPO/RTO, alarms, and data reconciliation.

**43. Why do you separate media uploads from post metadata creation?**

Media assets are large and slow to upload. Separating the architecture allows clients to upload files directly to object storage via presigned URLs. Once complete, the client submits the small metadata payload to the application tier, optimizing connection usage.

**44. How do you protect your data layers from cascading cache failures?**

We protect our databases by sizing them to handle baseline loads, using resilient circuit breakers, and configuring pre-warming routines to rehydrate empty caches before they go live.

**45. What happens if a user deletes a post?**

Post Service marks the ScyllaDB record as `DELETED` and reliably publishes `post-deleted`. Fan-out and cache consumers purge the ID from Redis Feed, Author Timeline Cache, Celebrity Store, and Redis Trending; Search Indexer removes the document, and Media workers apply the object-retention policy.

**46. How do you optimize CDN cache delivery for user feeds?**

We do not cache personalized user feeds at the CDN layer because they change frequently for each user. CDNs are used to cache static, public media assets like images and videos.

**47. How do you ensure log data remains useful during outages?**

We emit structured logs with correlation ID, trace ID, event ID, service, error code, Kafka partition/offset, retry count, and degradation decision. User identifiers are minimized or pseudonymized, and tokens or content are never logged.

**48. What is the trade-off of using long-lived JWTs?**

Long-lived JWTs are harder to revoke if compromised. We use short-lived access tokens (15-minute TTL) combined with secure, rotatable refresh tokens managed through server-side blacklist registries.

**49. How do you handle database schema migrations without downtime?**

We use multi-phase migration strategies (like Expand and Contract). New columns are added as optional fields first, then the application code is updated to write to both old and new schemas, and finally the old fields are removed once data is fully backfilled.

**50. Why use an event-driven architecture instead of direct RPC calls?**

We use synchronous RPC for request/response operations that require an immediate result, such as feed hydration, and Kafka events for moderation, fan-out, indexing, recommendation generation, notification, and cache invalidation. This separation provides replay, backpressure, and independent scaling, at the cost of idempotency requirements and eventual consistency.

---

## Related Reading

- [Designing a Social Graph & Feed Application at Scale](/system-design/social-feed/) — full architecture, capacity planning, and design decisions
- [Designing a Scalable Chat Application at Scale](/system-design/chat-application/) — adjacent real-time messaging design patterns
