---
title: "Google/Meta Sponsored Ads System Design — Interview Questions"
date: 2026-06-27T12:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a Google/Meta-style sponsored ads platform — click feedback ranking, DynamoDB, Redis sorted sets, Kafka aggregation, and production failure recovery."
tags: ["system-design", "interview", "distributed-systems", "kafka", "redis", "dynamodb"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Google/Meta Sponsored Ads Platform at Scale](/system-design/sponsored-ads/). These questions probe click-feedback ranking, DynamoDB hot partitions, Redis cache hydration via CDC, Kafka replay semantics, fraud deduplication, and cross-region consistency — the topics interviewers dig into after the whiteboard diagram.

---

## Architecture & Trade-offs (1–10)

**1. Why choose DynamoDB over PostgreSQL for the ad catalog at 115K peak write RPS?**

PostgreSQL scales well vertically but sustained 115K write RPS causes lock queue delays and replication lag across master-replica topologies. DynamoDB delivers predictable single-digit millisecond performance with managed horizontal partitioning and minimal operational overhead for this write profile.

**2. Why Redis Sorted Sets instead of maintaining a heap inside the search microservice?**

Redis ZSET provides O(log N + M) top-N retrieval, atomic `ZADD`, built-in replication, and standardized cluster sharding. A custom in-process heap requires manual synchronization, lacks cross-pod consistency, and adds parsing overhead if built on raw key-value stores like Memcached.

**3. Why Kafka over AWS SNS for click event ingestion?**

SNS is push-based and drops messages after consumer acknowledgment — no offset-controlled replay during downstream crashes. Kafka's append-only disk log retains messages for extended periods, enabling pause, scale-out, or rewind of consumer offsets for disaster recovery without data loss.

**4. Why decouple click ingestion from score aggregation with a message broker?**

The click ingestion service must return `202 Accepted` in single-digit milliseconds at 115K RPS. Heavy aggregation, fraud checks, and DynamoDB writes belong in downstream consumers that batch work and absorb backpressure without blocking the HTTP hot path.

**5. What happens if an ad's score surges exponentially due to a viral item, creating a database hot partition?**

The stream aggregator collects events over a configurable 30-second window per `ad_id`, collapses point modifications into a single aggregate delta (e.g. +50,000), and performs one atomic DynamoDB mutation. This protects storage from per-click write amplification on hot keys.

**6. How does the system handle click fraud or malicious bots trying to manipulate ad rankings?**

Edge WAF rules and per-IP rate limits block obvious automated attacks synchronously. The streaming aggregator maintains a Redis lookback window of `(user_id, ad_id)` pairs and drops excessive repetitive interactions before score deltas reach DynamoDB.

**7. Since DynamoDB Global Tables use asynchronous replication, how do you handle cross-region write conflicts?**

Global Tables resolve concurrent absolute-field writes with Last-Write-Wins based on timestamp. Ad metadata changes are infrequent and single-writer per advertiser. Click scores use relative `ADD` deltas rather than absolute replacement, keeping trends accurate even when updates arrive out of sequence.

**8. How do you prevent a cache stampede if a highly popular category cache expires or drops out of memory?**

Avoid hard TTL expirations on high-traffic category keys — CDC workers continuously update Redis via DynamoDB Streams. On eviction under memory pressure, wrap database lookups in a single-flight lock so only one thread queries DynamoDB while concurrent requests wait for hydration.

**9. Why is eventual consistency acceptable for ad rankings but not for click telemetry durability?**

Minor ranking variance across users during live score updates does not materially harm the product experience. Click telemetry and financial records require zero data loss — once a click event is accepted, it must be durably flushed to Kafka disk before returning `202 Accepted`.

**10. Why separate the Ad Management Service from the Click Ingestion Service?**

Different scaling profiles: ad creation averages ~11 RPS (peak ~1,150) while clicks average ~1,157 RPS (peak ~115K). Independent services allow right-sized autoscaling, isolated failure domains, and tailored SLAs without coupling publisher workflows to telemetry throughput.

---

## Data Model & Concurrency (11–20)

**11. Why denormalize advertiser metadata into the ad catalog row instead of normalizing into separate tables?**

At 115K peak search RPS, runtime joins across Sellers, Products, and AdPlacements breach the < 200 ms P99 SLA. Denormalized rows enable single-digit millisecond point reads and bounded GSI range scans per `product_type`.

**12. What is the purpose of `last_msg_offset` on each ad row?**

It tracks the highest Kafka partition offset successfully merged into the row. Conditional updates skip events where `offset <= last_msg_offset`, guaranteeing idempotent score application across consumer restarts and replay scenarios.

**13. How does the GSI `GSI_CategoryRanking` support the search path?**

Partition key `product_type` isolates category-scoped queries. Sort key `score` (descending) enables efficient top-N retrieval on cache miss without scanning the full table.

**14. Why use `ad_id` as the DynamoDB partition key instead of `product_type`?**

`product_type` has only ~100K distinct values — partitioning on it would create hot partitions for popular categories like "iPhone." `ad_id` is high-cardinality and distributes writes uniformly across shards.

**15. How do aggregator workers avoid global mutex contention on concurrent click events?**

Events route through Go channels to workers keyed by `ad_id` hash. All mutations for a given ad_id execute on a single worker thread, providing single-key isolation without distributed locks.

**16. Why are score updates applied as `ADD` deltas rather than absolute score replacement?**

Relative increments commute — processing the same click batch in different order yields the same final score. Absolute replacement is vulnerable to out-of-order delivery and cross-region replication races.

**17. How does idempotency work at the API gateway for ad creation and click logging?**

Clients pass `X-Idempotency-Key` (UUIDv4). The gateway caches the mutation response in Redis with a 24-hour TTL. Duplicate keys within the window return the cached response without reprocessing downstream side effects.

**18. What indexing strategy supports querying all ads owned by a single advertiser?**

A secondary GSI on `advertiser_id` (not detailed in the hot search path) supports dashboard queries. The search hot path uses `GSI_CategoryRanking` exclusively.

**19. How do you handle an advertiser updating ad metadata (title, price) while clicks are incrementing the score concurrently?**

Metadata updates and score increments target different attributes on the same `ad_id` row. DynamoDB `UpdateItem` with attribute-level updates avoids lost updates on unrelated fields. Score increments use `ADD`; metadata uses `SET`.

**20. Why store click events in Snowflake separately from the operational DynamoDB catalog?**

Click stream at 20 GB/day raw (~73 TB/year) is cost-prohibitive to query in DynamoDB. Snowflake provides columnar OLAP for batch analytics, CTR trends, and fraud model training without impacting the operational hot path.

---

## Caching & Search Path (21–30)

**21. Why use CDC (DynamoDB Streams → Lambda) instead of TTL-based cache expiration?**

TTL expiry on popular categories triggers cache stampedes — thousands of concurrent requests hit DynamoDB simultaneously. CDC pushes incremental `ZADD` updates on every mutation, keeping Redis warm without mass reloads.

**22. What Redis command retrieves the top-25 ads for a category?**

`ZREVRANGEBYSCORE category:{product_type} +inf -inf LIMIT 0 25` returns members in descending score order in O(log N + 25) time.

**23. How does the Context ML Classifier map "gifts for 10 year old" to category keys?**

Production systems use a two-stage pipeline: a bi-encoder converts the query to a dense vector, and a vector database (Milvus/Pinecone) performs approximate nearest neighbor search against category embeddings. A cross-encoder reranks candidates with contextual signals.

**24. What is the fallback if the ML classifier service is unavailable?**

Degrade to an inverted keyword lookup trie or synonym map. Return ads from broad popular categories rather than failing the search request entirely.

**25. How do you merge results when a query maps to multiple categories (e.g. "comic book" and "toy")?**

Fetch top-25 from each category ZSET independently, merge into a single list, deduplicate by `ad_id`, and sort by `ranking_score` descending before returning to the client.

**26. What is the expected latency breakdown on a cache hit vs cache miss?**

Cache hit: ML classification (~20–50 ms) + Redis ZREVRANGE (~1–5 ms per category) → total well under 200 ms P99. Cache miss adds DynamoDB GSI query (~10–30 ms) plus async hydration.

**27. Why provision 12 Redis nodes when the working set is only 2.5 GB?**

Memory is not the bottleneck — throughput and HA are. Six primary shards with six cross-zone replicas provide read scaling, failover within seconds, and headroom for 200K+ joint network IOPS.

**28. How does single-flight locking work on cache miss?**

The first request for a missing category acquires a distributed lock (or in-process mutex per category key). Subsequent concurrent requests wait on the same future/promise. Once hydration completes, all waiters read from the now-warm cache.

**29. Should ad image URLs be cached in Redis alongside ranking metadata?**

The 1 KB cached payload includes `image_url` (CDN pointer), not the binary image. Images are served from CDN edge caches with their own TTL and cache hierarchy.

**30. How do you handle a new ad with `score = 0` entering a crowded category?**

The ad is added to the category ZSET via CDC on insert. It appears at the bottom of rankings until clicks accumulate score. No special "new ad boost" is in scope for this design.

---

## Streaming, Kafka & Ingestion (31–40)

**31. How many Kafka partitions should the click-events topic have?**

64 partitions per topic, allowing up to 64 parallel consumer instances. Partition count should be planned upfront — increasing partitions later does not redistribute existing keys without rebalancing.

**32. How should click events be keyed for Kafka partitioning?**

Hash by `ad_id` so all clicks for a given ad route to the same partition and consumer, preserving per-key ordering and enabling in-partition micro-batching without cross-partition coordination.

**33. What happens when Kafka consumer lag exceeds the 3-minute score propagation SLO?**

Alert on consumer lag SLI. Scale aggregator replicas up to partition count. If DB write contention is the bottleneck, increase batch window from 30s to 60s to reduce write frequency per hot key.

**34. How does the click ingestion service handle broker connection failures?**

Switch to localized disk-buffered queues or a fallback durable store (e.g. DynamoDB as a spillover). Administrative recovery workers replay buffered events to Kafka once broker connections stabilize.

**35. Why return `202 Accepted` instead of `200 OK` for click ingestion?**

`202` signals the event is queued for asynchronous processing, not yet durably scored. Clients should not assume immediate ranking impact — consistent with the ≤ 3 minute propagation SLO.

**36. How does the ad creation pipeline achieve ≤ 1 minute upload-to-indexable P99?**

Pre-signed S3 upload bypasses the API for binary data. Metadata publish to Kafka is async. The Ad Catalog Processor initializes the DynamoDB row and triggers CDC → Redis hydration. Bottleneck is typically compliance review, not infrastructure.

**37. What is the production image ingestion pipeline beyond pre-signed URL upload?**

Upload to an isolated ingest bucket triggers Lambda (virus scan, EXIF strip, compress, generate WebP variants at multiple resolutions). Optimized assets deploy to CDN edge — raw advertiser uploads are never served directly.

**38. How do you replay Kafka events after a corrupted score aggregation bug?**

Pause consumers, deploy fix, reset offset to the known-good point, and replay. Offset-based idempotency (`last_msg_offset`) prevents double-application of already-committed events.

**39. Why use 64 partitions but only 6 Kafka brokers?**

Brokers host multiple partitions each. 6 NVMe-equipped brokers handle ~250 MB/s continuous write velocity. Partition count determines consumer parallelism ceiling, not broker count directly.

**40. How does backpressure propagate from saturated downstream storage to clients?**

Aggregators slow Kafka offset consumption. If internal buffers fill, the click ingestion service returns `503 ERR_BROKER_BACKPRESSURE`. The gateway may also shed load via rate limiting before events reach the broker.

---

## Security, Operations & Edge Cases (41–50)

**41. How is advertiser authorization enforced so one seller cannot modify another's ads?**

OAuth2 tokens carry `advertiser_id` scope. The Ad Management Service validates that the authenticated identity matches the `advertiser_id` in the request body before any mutation.

**42. What rate limits protect the system from abusive traffic?**

Gateway token-bucket: 100 requests/second per client IP or advertiser API key. Breach returns `429 ERR_RATE_LIMIT_EXCEEDED`.

**43. How is service-to-service communication secured internally?**

Mutual TLS via service mesh (Istio/SPIFFE). Edge terminates TLS 1.3 for public clients. Data at rest encrypted with AES-256 across DynamoDB, S3, and Redis persistence layers.

**44. What observability signals indicate the score propagation SLO is at risk?**

Kafka consumer lag per partition, DynamoDB throttled write count, Lambda CDC processing duration, and time delta between click `timestamp` and Redis ZSET score update (measured via synthetic canary clicks).

**45. How do you handle complete availability zone failure?**

Stateless pods in other AZs absorb traffic via load balancer health checks. Redis promotes cross-zone replicas. DynamoDB replicates across AZs automatically. Anycast DNS reroutes if an entire region fails.

**46. Why is mTLS overhead acceptable for internal service calls?**

The search path makes few internal hops (gateway → ML classifier → Redis). mTLS adds ~1–2 ms per hop — negligible against the 200 ms P99 budget. The security benefit outweighs the latency cost.

**47. What happens if DynamoDB throttles write capacity during a viral click storm?**

Aggregator batch windows expand, grouping more clicks per write. On-demand capacity mode auto-scales WCUs. Exponential backoff with jitter on throttled `UpdateItem` calls prevents thundering herd on recovery.

**48. Should search results be identical for all users querying the same keyword?**

Approximately, yes — rankings are by global click-feedback score per category. Production systems may add personalization (device, location) via cross-encoder reranking, but this design uses coarse category matching with global scores.

**49. How do you cost-optimize the compute fleet for diurnal traffic patterns?**

Spot Instances for stateless Kafka consumers (tolerate node loss via replay). On-Demand for search API pods. Karpenter or cluster autoscaler scales node pools based on real-time CPU and pending pod metrics.

**50. What is the disaster recovery procedure if both Redis and DynamoDB are unavailable in a region?**

Anycast DNS routes search traffic to a healthy region with warm Global Table replicas. If all regions fail, return graceful degradation (organic results only, no sponsored ads). Kafka retains click events for full score reconstruction on recovery.

---

## Related Reading

- [Designing a Google/Meta Sponsored Ads Platform at Scale](/system-design/sponsored-ads/) — full architecture, capacity math, and failure modes
- [Designing a Global Top-K Leaderboard & Real-Time Ranking System at Scale](/system-design/leaderboard/) — adjacent Redis ZSET + Kafka streaming patterns
- [Designing a Distributed Rate Limiter at Scale](/system-design/distributed-rate-limiter/) — token-bucket enforcement at the API gateway
