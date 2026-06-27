---
title: "Distributed Rate Limiter System Design — Interview Questions"
date: 2026-06-27T12:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a distributed rate limiter — token bucket algorithms, Redis Lua atomicity, fail-open resiliency, and gateway enforcement at 1M RPS."
tags: ["system-design", "interview", "distributed-systems", "redis", "architecture"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Distributed Rate Limiter at Scale](/system-design/distributed-rate-limiter/). These questions probe algorithm trade-offs, Redis Lua atomicity, fail-open vs fail-closed strategies, hotspot key mitigation, and production operations — the topics interviewers dig into after the whiteboard diagram.

---

## General Design Concepts (1–10)

**1. Why prioritize availability over consistency for a rate limiter?**

If the rate limiter prioritizes consistency, any network glitch requires locking the system, which drops all incoming customer traffic. Prioritizing availability ensures legitimate users can still access services during temporary edge issues.

**2. Where should a rate limiter be placed in a system?**

Place it within the API Gateway or reverse proxy layer. This intercepts and drops abusive traffic early, preventing unnecessary resource consumption in downstream services.

**3. What are the problems with client-side rate limiting?**

Client-side mechanisms are untrusted. Users can bypass or manipulate local code, configuration rules, or tracking cookies.

**4. How do you handle rate limiting for unauthenticated users?**

Track and limit requests using deterministic identifiers like the client's public IP address, or fallback routing contexts.

**5. What happens if a user's IP changes frequently?**

IP-based tracking can become inaccurate. For reliable enforcement, transition to application-level identifiers like API keys or session tokens as early as possible.

**6. How does the system support dynamic rule changes without downtime?**

Use a decoupled admin service that writes updates to a relational database and pushes real-time invalidation signals to a distributed cache.

**7. What is a "fail-open" strategy?**

An operational model where validation failures (like cache timeouts or crashes) allow requests to pass through rather than blocking traffic.

**8. When should you choose a "fail-closed" approach instead?**

Use it for high-security environments, such as payment gateways or authentication endpoints, where security and fraud prevention override availability.

**9. How do you protect against distributed denial of service (DDoS) attacks?**

Use a layered defense. Volumetric network-layer filtering handles massive attacks at the edge (CDN), while application-layer rate limiters manage authentic API behavior.

**10. What is the difference between rate limiting and traffic shaping?**

Rate limiting immediately drops excess requests with errors. Traffic shaping queues and delays requests to match a smoother target delivery rate.

---

## Algorithms Comparison (11–20)

**11. How does the Fixed Window Counter algorithm work?**

It divides time into static windows (e.g. 1-minute blocks) and tracks request counts using an integer counter that resets at each boundary.

**12. What is the major flaw in the Fixed Window Counter algorithm?**

It suffers from boundary bursting, where a client can send their full quota at the end of one window and another full quota at the start of the next, doubling the allowed rate across the boundary.

**13. How does the Sliding Window Log algorithm fix the boundary burst issue?**

It records a timestamp log for every request and filters out logs older than the sliding window frame, ensuring accurate tracking at any point in time.

**14. What is the main bottleneck of the Sliding Window Log algorithm?**

High memory consumption. Storing individual timestamps for millions of requests quickly wears out cache memory resources.

**15. Explain the Sliding Window Counter approximation approach.**

It uses a mathematical formula that combines the count of the current window with a weighted percentage of the previous window to estimate the request rate dynamically.

**16. What is the main trade-off when using the Sliding Window Counter?**

It assumes traffic in the previous window was distributed evenly, which can lead to slight inaccuracies if requests arrived in bursts.

**17. How does the Token Bucket algorithm handle bursty traffic?**

Tokens accumulate up to a maximum bucket capacity. This allows clients to spend tokens rapidly for short bursts of traffic until the bucket empties.

**18. Explain the Leaky Bucket algorithm mechanics.**

Requests enter a bounded queue and drain out to downstream processors at a fixed, constant rate, ensuring a smooth and predictable traffic flow.

**19. When would you use a Leaky Bucket over a Token Bucket?**

Choose a Leaky Bucket when downstream services require a highly stable, uniform consumption rate and cannot handle sudden bursts of traffic.

**20. Can you implement a Token Bucket without running a background thread to refill tokens?**

Yes. Calculate token replenishment lazily on each incoming request by comparing the current timestamp with the last recorded update timestamp.

---

## Concurrency & Scaling Focus (21–30)

**21. How do you prevent race conditions when multiple gateway nodes update the same cache key?**

Execute operations inside atomic Redis Lua scripts. This ensures the check-and-update steps run as a single transaction.

**22. Why avoid using distributed locks (like Redlock) for tracking rate limits?**

Distributed locking requires multiple network round-trips to acquire and release locks, which adds too much latency overhead for live traffic paths.

**23. How do you scale out a centralized state store like Redis to support millions of requests?**

Implement cluster sharding using consistent hashing on a partition key, such as the `user_id` or `api_key`.

**24. What is the "hotspot key" problem in a sharded cache environment?**

A single viral user or a high-traffic enterprise account routes all their requests to the same shard, overloading that specific node while others remain underutilized.

**25. How can you mitigate hotspot key issues within the cache tier?**

Implement a multi-level cache. Store a small portion of the count state locally within the gateway node for high-volume keys to reduce lookups to the central cache.

**26. Explain the "Thundering Herd" problem relative to rate limit resets.**

When a high-traffic window resets, blocked clients all retry simultaneously, creating a massive traffic spike that can overwhelm downstream systems.

**27. How do you handle clock drift across multiple geo-distributed gateway instances?**

Use a central time source, like the Redis cluster time, or synchronize server clocks using NTP (Network Time Protocol) to keep drift within safe milliseconds.

**28. How would you rate limit a multi-tenant SaaS application?**

Include the `tenant_id` as part of the cache key prefix, and map lookups to different SLA tiers dynamically during rule evaluation.

**29. What are the risks of using consistent hashing for shard allocation?**

If a shard fails, its keys shift to adjacent nodes, which can trigger a cascading failure if those nodes lack the capacity to handle the extra load.

**30. How do you isolate performance impact across different customers?**

Enforce dedicated queue pipelines or separate processing threads for different tiers to prevent lower-tier traffic spikes from slowing down high-priority paths.

---

## Technology Selection Details (31–40)

**31. Why choose Redis over Memcached for distributed rate limiting?**

Redis natively supports complex data types (like Hashes) and server-side Lua execution, which are required for atomic token bucket calculations.

**32. When would a relational database like PostgreSQL be appropriate for rate limiting?**

Only for storing configuration rules and administrative settings, not for tracking real-time request counters.

**33. Why do we use Apache Kafka instead of RabbitMQ for logging metrics?**

Kafka is designed for high-throughput append logs and partition streaming, making it ideal for processing millions of metric events without blocking core services.

**34. What are the trade-offs of using an API Gateway plug-in vs. a standalone rate limiting service?**

An inline plug-in minimizes network latency by avoiding an extra out-of-process hop, whereas a standalone service provides better architectural separation and decoupling.

**35. Why use Envoy Proxy as the foundation for an API Gateway?**

Envoy provides high-performance, non-blocking asynchronous network execution and supports custom filter extensions via Lua or WebAssembly (WASM).

**36. What is the benefit of using ClickHouse for analytics processing?**

ClickHouse is a columnar database optimized for fast, real-time aggregation queries across billions of telemetry log rows.

**37. Can we use JWT claims to skip database lookups entirely?**

Yes. Cryptographically signed JWT tokens can safely store user metadata and subscription tiers, allowing the gateway to read user details without querying a database.

**38. How does consistent hashing differ from traditional modulo hashing?**

Modulo hashing changes almost all key mappings when a node is added or removed, while consistent hashing only shifts a small fraction of keys, minimizing rebalancing overhead.

**39. What is the trade-off of using a high-level language like Java vs. C++/Go for rate limiters?**

Languages with garbage collection (like Java) can introduce unpredictable latency spikes during cleanup cycles under extreme load, whereas C++ or Go offer more stable, lower-level performance.

**40. Why avoid global active-active synchronization for counter state across continents?**

Cross-continental replication is limited by the speed of light, introducing hundreds of milliseconds of latency that violate the 5 ms processing requirement.

---

## Resiliency & Production Operations (41–50)

**41. How do you verify the system works under heavy load before launching?**

Run distributed load tests using tools like Locust or JMeter to simulate millions of concurrent connections against a staging environment.

**42. What alerts would indicate a critical failure in the rate limiter tier?**

Set up alerts for high p99 execution latencies (≥ 5 ms), elevated rates of internal server errors (5xx), or prolonged circuit breaker trips.

**43. How do you perform a seamless configuration update across the gateway cluster?**

Use an external configuration broker or a database write-through path to push updates incrementally, validating changes on a small canary group first.

**44. What happens if a malicious user falsifies authentication headers?**

The gateway's auth filter must catch and reject invalid signatures early, preventing unauthenticated traffic from hitting the rate limiter logic.

**45. How can you optimize infrastructure costs for the rate limiting tier?**

Configure horizontal auto-scaling (HPA) to scale down gateway and cache nodes during low-traffic periods, such as overnight hours.

**46. What metric confirms that the rate limiter is successfully protecting downstream services?**

A stable or drop in downstream CPU usage and database connection queues during an external traffic spike indicates the rate limiter is effectively shedding excess load.

**47. How do you prevent cache stampedes when hot configuration keys expire?**

Use a background process to proactively refresh cache keys before they expire, or apply random jitter to TTL durations to stagger expirations.

**48. How do you debug an issue where a client claims they are being throttled incorrectly?**

Query the analytical data warehouse (e.g. ClickHouse) using the client's ID and correlation tracing IDs to analyze their request timelines and exact bucket state.

**49. What role does a sidecar proxy play in service-to-service rate limiting?**

A sidecar proxy handles traffic rules directly at the service boundary, managing localized communication limits between microservices within the internal mesh.

**50. How do you ensure the logging infrastructure doesn't run out of disk space?**

Implement aggressive log rotation rules, compress old files, and stream telemetry data immediately to an external object storage cluster with automatic expiration policies.

---

## Production Improvements Over Basic Designs

These are the structural upgrades that separate a production-grade rate limiter from an educational prototype:

| Improvement | Why it matters |
| :--- | :--- |
| **Atomic Lua scripting** vs basic Redis commands | Eliminates multi-step check-then-act race conditions without distributed lock overhead |
| **Inline gateway execution** vs standalone RL service | Avoids an extra network hop per request; meets the 5 ms latency ceiling |
| **Explicit fail-open circuit breakers** | Preserves availability when the cache tier goes dark — omitted from most tutorial designs |
| **Async telemetry via Kafka** | Analytics never blocks the live request evaluation path |
