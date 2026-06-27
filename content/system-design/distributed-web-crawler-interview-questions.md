---
title: "Distributed Web Crawler System Design — Interview Questions"
date: 2026-06-27T11:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a production-grade distributed web crawler."
tags: ["system-design", "interview", "distributed-systems", "kafka", "redis"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Distributed Web Crawler at Scale](/system-design/distributed-web-crawler/). These questions probe Bloom-filter deduplication, politeness enforcement, frontier scheduling, SSRF prevention, and production failure recovery — the topics interviewers dig into after the whiteboard diagram.

---

## Architecture & Trade-offs (1–10)

**1. Why separate the URL Frontier Service from Crawl Workers instead of a monolithic crawler?**

The frontier is CPU- and database-bound (scheduling, dedup, priority queues), while workers are network- and I/O-bound (HTTP fetch, parsing). Separating them allows independent horizontal scaling — add workers when Kafka lag grows without over-provisioning database connections on the scheduling tier.

**2. Why use Kafka instead of RabbitMQ for the crawl task queue?**

Kafka's replayable log lets workers re-consume backlogged tasks after outages without degrading queue performance. At ~50K messages/sec from link extraction, Kafka's sequential disk append handles sustained pressure better than AMQP-based brokers whose per-queue throughput degrades under large backlogs.

**3. Why favor Bloom filters over a distributed database query for unique link evaluation?**

Querying a disk-backed database for every discovered hyperlink introduces massive I/O bottlenecks. A Bloom filter filters out 99.9% of already-seen URLs in microseconds using ~1.2 GB of RAM for 1 billion entries — a 500 GB database scan is orders of magnitude slower and more expensive.

**4. How does your design mitigate recursive trapping via infinite calendar paths?**

A strict parameter-stripping layer during URL normalization removes session and tracking query params. Combined with a maximum depth of 20 directory levels and a per-domain crawl budget of 5,000 pages, calendar loops and pagination traps are bounded before they exhaust worker capacity.

**5. Why not use headless browsers (Puppeteer/Playwright) for every page?**

Headless rendering is 10–100× slower than static HTML parsing and consumes significantly more memory per worker. For a billion-page crawl universe at 7-day intervals, static parsing is the only viable throughput path. JavaScript rendering is reserved for a separate, lower-priority rendering pipeline.

**6. What is the read/write ratio and why does it matter for storage selection?**

Approximately 1:100 read-to-write. The system is heavily write-intensive — object storage (S3/GCS) for page content and append-heavy Kafka for task distribution are natural fits. A read-optimized cache layer is unnecessary on the content tier.

**7. How do you handle sites that block crawlers via `robots.txt`?**

The frontier fetches and caches `robots.txt` per domain (24-hour TTL in Redis). Before enqueueing a URL, the frontier checks the path against `disallowed_paths`. Workers never fetch URLs that violate robots rules.

**8. Why store raw HTML in object storage instead of PostgreSQL?**

At ~14.28 TB/day ingestion (~5.21 PB/year), relational BLOB storage is cost-prohibitive and creates vacuum/index bloat. Object storage provides petabyte-scale durability at cents per GB with no schema migration overhead.

**9. How does eventual consistency manifest in this system?**

A URL may be discovered, queued, and crawled with seconds of lag between state transitions. Downstream indexers consume from object storage asynchronously. Brief inconsistency between "URL marked COMPLETED" and "content available in S3" is acceptable.

**10. What steps protect internal workers from malicious DNS attacks (SSRF)?**

Workers route requests through a sandboxed DNS resolver that blocks non-routable private IP spaces (10.0.0.0/8, 192.168.0.0/16, 127.0.0.0/8). The resolver validates the resolved IP before the HTTP client connects, preventing Server-Side Request Forgery against internal infrastructure.

---

## Data Model & Deduplication (11–20)

**11. Why normalize host metadata into a separate `hosts` table?**

Billions of URL rows would each duplicate domain strings like `www.wikipedia.org`. Isolating host metadata reduces the metadata footprint by ~40% and centralizes `robots.txt` crawl-delay configuration per domain.

**12. How do you generate URL primary keys without a centralized ID service?**

SHA-1 hash of the normalized URL string produces a deterministic 20-byte binary key. The same URL always maps to the same hash, enabling natural deduplication without Snowflake or UUID coordination overhead.

**13. What happens when two different URLs produce identical page content?**

After fetching, the worker computes a SHA-256 checksum of the parsed HTML body. If the checksum already exists in `content_checksums`, the URL is marked `COMPLETED` without writing duplicate content to object storage.

**14. What is the false-positive rate of the Bloom filter and how do you handle it?**

At 0.1% false-positive rate for 1 billion URLs, roughly 1 in 1,000 "new" URLs is incorrectly flagged as seen. The frontier falls through to a database lookup on Bloom positives to confirm — the filter eliminates 99.9% of DB reads, not 100%.

**15. Why use MurmurHash3 for host partitioning but SHA-1 for URL identity?**

MurmurHash3 is faster and produces well-distributed shards for `Hash(domain)` partitioning. SHA-1 provides stronger collision resistance for URL identity across billions of entries, though SHA-256 would also work at slightly higher compute cost.

**16. How do you handle URL canonicalization disagreements (trailing slash, www prefix)?**

The normalization pipeline lowercases hostnames, strips default ports, removes fragments, resolves path segments, and strips tracking query parameters. `http://example.com/page` and `https://www.example.com/page/` converge to a single canonical form before hashing.

**17. What index supports the frontier's "what to crawl next" query?**

A composite index on `(crawl_status, next_crawl_at)` lets the frontier efficiently poll for URLs where `crawl_status = QUEUED` and `next_crawl_at <= NOW()`, ordered by priority.

**18. How do you track crawl history without bloating the primary URL table?**

A separate `crawl_history` table records each fetch attempt with `outcome`, `http_status`, and `crawled_at`. The `urls` table holds only the current state; history rows are append-only and can be partitioned by date or archived to cold storage.

**19. How do you handle internationalized domain names (IDN)?**

URLs are normalized to Punycode (ACE encoding) before hashing. `https://münchen.de` becomes `https://xn--mnchen-3ya.de`, ensuring a single canonical representation.

**20. What is the storage cost of URL metadata alone?**

1 billion records × 500 bytes ≈ 500 GB. This fits in a sharded PostgreSQL cluster but requires Citus or manual partitioning as the table grows beyond single-node capacity.

---

## Politeness & Scheduling (21–30)

**21. How does the Redis politeness lock prevent overloading a single domain?**

Workers execute `SET politeness:{host_hash} {worker_id} NX PX {crawl_delay_ms}`. The `NX` flag ensures only one worker holds the lock; `PX` auto-expires it after the configured delay. Other workers skip or re-queue the URL.

**22. What happens when Redis is unavailable during a crawl?**

Workers fall back to a conservative 5-second in-memory delay per domain. This is slower than normal operation but prevents hammering origins when the coordination layer is down.

**23. How do you implement priority-based scheduling (news hourly, blogs monthly)?**

Each URL carries a `priority` (1–5) and `next_crawl_at` timestamp. The frontier sets `next_crawl_at` based on site category: news seeds get 1-hour intervals, blogs get 30-day intervals. Higher-priority URLs are dequeued first when multiple URLs are ready.

**24. How do you respect `Crawl-delay` directives from `robots.txt`?**

The frontier parses `robots.txt` on first encounter, stores `crawl_delay_ms` in the `hosts` table, and caches rules in Redis. Workers read the delay when acquiring the politeness lock.

**25. How do you handle domains that return HTTP 429 (Too Many Requests)?**

Workers parse the `Retry-After` header (seconds or HTTP-date), update `next_crawl_at` accordingly, and mark the URL back to `QUEUED`. The politeness delay for that domain is temporarily increased.

**26. Should politeness be enforced per domain, per IP, or per URL?**

Per domain (host-level). Multiple workers may crawl different paths on the same host, but only one worker holds the politeness lock at a time. Per-URL politeness is too granular; per-IP is incorrect when a domain resolves to multiple IPs behind a CDN.

**27. How do you prevent a single high-priority domain from starving low-priority crawls?**

The frontier uses weighted fair queuing: dequeue up to N high-priority URLs, then at least one low-priority URL, preventing complete starvation of the long tail.

**28. How do you handle DNS TTL expiration mid-crawl?**

Workers maintain a local LRU DNS cache (10,000 entries). On cache miss or TTL expiry, the worker re-resolves through the sandboxed resolver before connecting.

**29. What is the per-domain page budget and why?**

5,000 pages per domain. This prevents a single site with millions of auto-generated pages (calendar views, faceted search) from consuming the entire crawl budget.

**30. How do you schedule re-crawls for the 7-day average interval?**

On successful crawl, the frontier sets `next_crawl_at = NOW() + interval_for_category`. URLs with `next_crawl_at` in the future remain in `COMPLETED` status until the timestamp elapses, then transition back to `QUEUED`.

---

## Scaling & Infrastructure (31–40)

**31. When do you introduce database read replicas?**

When frontier dedup lookups and scheduling queries exceed single-node read capacity. Replicas serve read-heavy dedup checks while the primary handles state transitions.

**32. What is the drawback of read replicas in this architecture?**

Replication lag can cause duplicate worker tasks — a URL marked `QUEUED` on the primary may not yet appear as `COMPLETED` on a replica. Mitigate with read-your-writes consistency on the frontier's scheduling path or accept occasional duplicate fetches (idempotent by design).

**33. How do you shard the URL table?**

Hash by `host_hash` (MurmurHash3 of domain) using Citus distribution. All URLs for a domain live on the same shard, enabling efficient per-domain queries and politeness lookups.

**34. When do you move to multi-region active-active deployments?**

When cross-continent network latency to target hosts slows crawl throughput below SLA. Geo-located worker pools in US, EU, and APAC regions crawl local targets with lower RTT.

**35. How does Kafka partitioning interact with crawl workers?**

URL tasks are partitioned by `host_hash` so all tasks for a domain route to the same partition. This co-locates scheduling decisions and reduces cross-partition ordering issues, though politeness locks in Redis are the true serialization mechanism.

**36. How do you size the worker fleet?**

50 pods at 4 vCPU / 8 GB RAM handle ~4,959 peak pages/sec with 3× headroom. HPA scales up when Kafka consumer lag exceeds 50,000 messages.

**37. What is the network bandwidth requirement at peak?**

~4,959 pages/sec × 100 KB ≈ 495 MB/s (~3.96 Gbps). Workers should be deployed in regions with sufficient egress capacity.

**38. How do you handle a viral news event that generates millions of new links in minutes?**

Kafka absorbs the spike; frontier consumers process links asynchronously. Priority scheduling ensures news-category URLs are enqueued first. Worker HPA scales on consumer lag.

**39. Why use Patroni for PostgreSQL failover?**

Patroni-driven Raft groups handle automatic primary promotion within seconds. Crawl workers continue processing from Kafka during failover; only the frontier's state writes pause briefly.

**40. How do you rebuild the Bloom filter after a catastrophic failure?**

Scan the `urls` table (or a snapshot export), insert every `url_hash` into a fresh Bloom filter, and atomically swap the filter pointer. Accept temporary duplicate fetches during rebuild — content dedup via checksums prevents duplicate storage.

---

## Failure Recovery & Production (41–50)

**41. What happens when a worker crashes mid-fetch?**

Kafka redelivers the uncommitted message to another worker. The URL may be fetched twice, but the checksum dedup layer prevents duplicate storage. Status transitions are idempotent (`QUEUED → COMPLETED`).

**42. How do you handle permanently dead links (HTTP 404/410)?**

Mark the URL `FAILED` with the HTTP status in `crawl_history`. Schedule a retry with exponential backoff (1 day, 7 days, 30 days). After 3 failures, move to a tombstone state and stop re-queuing.

**43. How do you handle malformed HTML that crashes the parser?**

Parse failures are isolated per URL. The worker logs the error, marks the URL `FAILED`, and continues processing the next task. A circuit breaker on repeated parse failures for a domain triggers an alert.

**44. What is the dead-letter queue (DLQ) pattern for failed crawls?**

URLs that fail after max retries are published to a Kafka DLQ topic. An operations dashboard surfaces DLQ depth; engineers can inspect, fix root causes, and replay messages.

**45. How do you monitor crawl health in production?**

Prometheus dashboards track `kafka_consumer_lag`, `worker_http_failure_rate`, `db_connection_pool_utilization`, and Bloom filter false-positive rate. Alert when consumer lag exceeds 50K for 5 minutes or HTTP failure rate exceeds 5%.

**46. How do you prevent seed-flooding attacks on the ingestion API?**

Token bucket rate limiting at the API gateway per client IP and API key. `X-Idempotency-Key` in Redis prevents duplicate batch ingestion on retries.

**47. What is the SLO for crawl task completion?**

≥ 99.5% of network requests resolve within a 2-second timeout window. Tasks exceeding the timeout are marked `FAILED` and retried with backoff.

**48. How do you add a new document parser (PDF, JSON) without redesigning the pipeline?**

Workers implement a `DocumentParser` interface. The crawl pipeline fetches bytes, detects content type, and delegates to the appropriate parser. Extracted links flow through the same Kafka link-extraction topic regardless of parser.

**49. How does this design differ from a naive "database lookup for every URL" approach?**

Naive designs query PostgreSQL for every discovered link, creating millions of random I/O operations per second. Production systems deploy distributed Bloom filters (RedisBloom) to decouple dedup from worker memory, and asynchronous Kafka pipelines to keep the scheduling engine free of network I/O blocking.

**50. How would you extend this crawler to support JavaScript-rendered pages?**

Add a separate low-priority rendering pipeline: a subset of URLs flagged `requires_js=true` are routed to headless-browser worker pools. Rendered DOM is fed back into the standard parse-and-extract flow. This keeps the billion-page static crawl at full throughput while selectively rendering high-value pages.
