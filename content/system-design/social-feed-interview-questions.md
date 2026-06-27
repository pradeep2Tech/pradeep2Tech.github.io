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

We decouple the celebrity ingestion path using a pull-based hybrid architecture. Instead of duplicating the post identifier across 100 million follower feeds at write time (push model), the post metadata is appended to a dedicated celebrity storage registry. When active followers read their feed, the system queries both their pre-computed push feed and fetches recent celebrity posts to merge them dynamically at read time.

**2. What happens if a fan-out worker crashes halfway through processing a message?**

Kafka consumer offsets are only committed after a fan-out batch write is successfully acknowledged by the destination caches (RedisFeed/ScyllaDB). If a worker fails mid-process, the uncommitted message batch is reassigned to another active worker instance in the consumer group, ensuring at-least-once delivery guarantees.

**3. How do you prevent cursor drift when a user scrolls their feed while new posts are arriving?**

We implement time-and-ID-bound opaque cursor tokens rather than numeric database offsets. The cursor base64 token decodes to an absolute timestamp and lexicographical ID bound (`created_at <= TIMESTAMP AND post_id < LAST_ID`). New posts arriving after the timestamp are excluded from the current scrolling session, ensuring stable page offsets.

**4. Why use ScyllaDB/Cassandra for posts instead of a relational database with partitioning?**

Social media post generation is highly write-heavy, and query patterns are highly predictable (fetch posts by `author_id` ordered by time). Relational structures introduce lock contention and B-Tree rebalancing overhead at scale. Cassandra's LSM storage model converts randomized write mutations into sequential appends, matching our performance needs.

**5. How do you implement a "Like" counter without causing database lock contention?**

We avoid direct transactional updates (`UPDATE posts SET likes = likes + 1`). Instead, interactions are streamed through Kafka topics and buffered using distributed counters in Redis via `HINCRBY`. An asynchronous worker batch-flushes these updates to ScyllaDB persistent storage every 10 seconds using delta additions.

**6. How do you defend against malicious or explicit image uploads at scale?**

Uploaded assets are initially isolated in an unreadable private S3 staging bucket. An asynchronous event-driven workflow passes the asset to automated ML moderation pipelines. The asset is moved to the public CDN-backed production bucket only after passing policy checks; otherwise, a notification is sent to the user and the asset is deleted.

**7. What is your strategy for caching the social graph relationships?**

The active social follow graph is stored in Redis Sorted Sets, where the key is the `user_id` and the members are the followed IDs scored by follow timestamp. This structure allows O(log N + M) edge lookups to find common connections or compile follow lists during feed construction.

**8. How does the system handle an active-active cross-region database split?**

We use multi-region ScyllaDB deployments configured with CRDTs (Conflict-free Replicated Data Types) and LWW (Last-Write-Wins) timestamp conflict resolution rules. For non-commutative metrics like user profile data, updates use database quorum checks across a majority of regions.

**9. Why choose Envoy over traditional Nginx setups for your API Gateway?**

Envoy provides advanced cloud-native networking features, including native HTTP/2 and gRPC upstream multiplexing, live configuration reloads via xDS APIs, advanced distributed tracing hooks, and robust circuit breaking capabilities.

**10. How do you handle cache stampedes on popular post items?**

We protect the system from cache stampedes using a combination of distributed locks (Redlock) to ensure only one worker recomputes a cache miss, along with probabilistic early expiration algorithms (XFetch). These algorithms recompute and refresh cache entries before they expire.

---

## Caching & Recovery (11–20)

**11. What happens if the pre-computed feed cache is destroyed completely?**

The Feed Service falls back to an automated Backfill Engine. This engine queries the follower cache repository to identify follow relationships and pulls the top 100 recent post references from RedisLatest for those users, rebuilding the target feed cache interactively.

**12. How do you ensure idempotency for post creation under bad network conditions?**

Clients attach a unique UUID key to the `X-Idempotency-Key` header. When a request arrives, the API Gateway runs an atomic `SETNX` operation in Redis using this key with a 120-second TTL. If the key exists, the request is rejected as a duplicate, preventing duplicate posts from being created.

**13. How do you scale down infrastructure costs during off-peak night hours?**

We use Kubernetes Horizontal Pod Autoscalers (HPA) driven by custom Prometheus metrics (like request throughput and queue lag). Storage tiers switch to automated cold tiering policies on object storage networks for old media assets.

**14. What happens when a user deletes their account?**

Account deletion initiates an asynchronous saga pattern. The user status is immediately marked as `DELETED` in the database to block user access. A background cleanup job streams delete events through Kafka to purge social relationships, invalidate cached feeds, and remove media assets over time.

**15. How do you handle pagination when a user blocks another user while scrolling?**

The Feed Engine filters posts against a dynamic bloom filter representing the user's blocked IDs during timeline generation. If a block occurs mid-scroll, the active page filtering catches the change, ensuring blocked content is removed from subsequent pages.

**16. Why choose a graph database layout over PostgreSQL for the follow network?**

We don't need a full graph database since our queries only require shallow, single-hop index scans (e.g., fetching direct followers). A normalized relational database with partial indexes handles this pattern efficiently without the operational complexity of a graph database.

**17. How do you protect your internal service microservices from cascading crashes?**

We isolate services using an internal service mesh fabric (Istio) configured with explicit request deadlines, retries with exponential backoff, and circuit-breaker thresholds. If a downstream service fails, upstream callers return degraded data or use local cache fallbacks.

**18. How do you design a system to support "Infinite Scrolling" reliably?**

The client application requests feed pages using opaque cursors. The server returns a fixed chunk of feed metadata along with a token for the next page (`next_cursor`). As the viewport approaches the bottom of the rendered list, the client pre-fetches the next page token asynchronously.

**19. How do you handle timezone localizations for global chronological feeds?**

All system timestamps are unified, captured, and stored using UTC ISO 8601 formatting. The client application converts these UTC values to the local device timezone when rendering timestamps in the UI.

**20. What database choices support multi-region user profile mutations?**

We use a globally distributed relational database architecture like CockroachDB or a sharded PostgreSQL setup with region-locked master nodes. This ensures strong consistency and regulatory compliance (like GDPR data residency) for user profiles.

---

## Security & API Hardening (21–30)

**21. How do you catch API route parameter attacks or SQL injection threats?**

We enforce strict input validation rules at the Envoy gateway layer using OpenAPI specification contracts, and all downstream database adapters use parameterized prepared statements.

**22. What caching strategy handles post metadata updates best?**

We apply a standard Cache-Aside strategy. On updates, the system purges the item from the cache. The next read operation fetches the fresh value from ScyllaDB and rehydrates the cache tier.

**23. How do you track metrics across asynchronous workers?**

We collect metrics using stateless OpenTelemetry collector sidecars that push application telemetry data to a centralized Prometheus cluster every 10 seconds.

**24. What happens if a user updates their profile picture?**

An explicit update request updates the database and sends a profile invalidation message to a Kafka topic. Workers pick up this message to refresh cached user profiles and evict outdated copies from edge caches.

**25. How do you scale media delivery for trending viral videos?**

Viral assets are cached at edge locations using geographically distributed CDN networks (such as Cloudflare or CloudFront) configured with origin shield architectures to shield primary storage buckets from high traffic spikes.

**26. Why do you use UUIDv7 or Snowflake IDs over standard database auto-increments?**

Standard auto-increments expose business metrics and cause resource contention in distributed write environments. Custom frameworks like Snowflake or UUIDv7 provide time-sortable, 64-bit unique identifiers that can be generated independently without centralized locks.

**27. How do you handle deep pagination requests efficiently?**

We enforce hard limits on maximum history access depths (e.g., limiting user feeds to 500 items). Requests for older archival data are redirected to specialized cold data storage engines instead of high-performance caches.

**28. How do you verify the health of microservices in your clusters?**

Kubernetes clusters run continuous liveness and readiness probes against custom `/healthz` endpoints. These endpoints verify local dependencies like database connections and memory limits before routing traffic to a container.

**29. What happens if a Kafka cluster experiences severe broker lag?**

The system triggers automated HPA scaling policies to deploy more consumer pods. If lag continues to grow, low-priority tasks (like analytical tracking counters) are temporarily bypassed to focus compute resources on core ingestion paths.

**30. How do you manage secrets like API keys and database credentials safely?**

Secrets are injected into container runtimes as temporary environment values using automated secrets managers like HashiCorp Vault or AWS Secrets Manager, with encryption certificates rotated automatically every 30 days.

---

## Media, Operations & Cost (31–40)

**31. How do you handle large video files over slow mobile networks?**

The client uploads video files in small, chunked byte streams to a chunker service. The service verifies each chunk using MD5 checksums, allowing interrupted uploads to resume from the last successful chunk.

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

The follow engine updates the graph database and pushes an eviction payload to a Kafka topic. Background workers consume this payload to instantly remove the unfollowed user's posts from the active user's cached feed.

**38. How do you isolate operational traffic from business intelligence queries?**

We direct analytical workloads to a dedicated data lake or read-replica warehouse (like Snowflake). This keeps heavy analytical queries isolated from the primary transactional databases.

**39. Why do you use mTLS inside your Kubernetes clusters?**

mTLS ensures all microservices authenticate each other using zero-trust principles, protecting internal service communication from spoofing or unauthorized packet sniffing.

**40. How do you maintain database connection limits under high load?**

We place database proxies like PgBouncer in front of PostgreSQL instances. These proxies pool and reuse database connections, preventing connection exhaustion under high traffic.

---

## Edge Cases & Architecture Trade-offs (41–50)

**41. What happens if a user rapidly toggles the "Like" button?**

The client application debounces the interaction locally. The API gateway also applies rate limits per user-post pair, dropping rapid toggle requests before they reach backend databases.

**42. How do you test the system for disaster recovery scenarios?**

We run scheduled chaos engineering exercises (using tools like Chaos Mesh) to inject random failures, such as availability zone outages and network lag, into staging environments to verify automated recovery paths.

**43. Why do you separate media uploads from post metadata creation?**

Media assets are large and slow to upload. Separating the architecture allows clients to upload files directly to object storage via presigned URLs. Once complete, the client submits the small metadata payload to the application tier, optimizing connection usage.

**44. How do you protect your data layers from cascading cache failures?**

We protect our databases by sizing them to handle baseline loads, using resilient circuit breakers, and configuring pre-warming routines to rehydrate empty caches before they go live.

**45. What happens if a user deletes a post?**

The system marks the post as `DELETED` in the database to hide it instantly. A deletion event is then broadcast to Kafka, triggering background jobs to purge the post from user feeds, remove it from caches, and delete associated files from object storage.

**46. How do you optimize CDN cache delivery for user feeds?**

We do not cache personalized user feeds at the CDN layer because they change frequently for each user. CDNs are used to cache static, public media assets like images and videos.

**47. How do you ensure log data remains useful during outages?**

We enforce structured JSON logging across all microservices. These logs include standardized metadata fields like `correlation_id` and `tenant_id` to make debugging easier in centralized logging systems.

**48. What is the trade-off of using long-lived JWTs?**

Long-lived JWTs are harder to revoke if compromised. We use short-lived access tokens (15-minute TTL) combined with secure, rotatable refresh tokens managed through server-side blacklist registries.

**49. How do you handle database schema migrations without downtime?**

We use multi-phase migration strategies (like Expand and Contract). New columns are added as optional fields first, then the application code is updated to write to both old and new schemas, and finally the old fields are removed once data is fully backfilled.

**50. Why use an event-driven architecture instead of direct RPC calls?**

An event-driven architecture decouples services, turning tight dependencies into asynchronous message streams. This protects the system from cascading failures, improves availability, and allows different components to scale independently.

---

## Related Reading

- [Designing a Social Graph & Feed Application at Scale](/system-design/social-feed/) — full architecture, capacity planning, and design decisions
- [Designing a Scalable Chat Application at Scale](/system-design/chat-application/) — adjacent real-time messaging design patterns
