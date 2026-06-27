---
title: "Food Delivery System Design — Interview Questions"
date: 2026-06-26T14:30:00+00:00
draft: false
description: "50 senior-level system design interview questions and answers for a Zomato/Swiggy-scale food delivery platform."
tags: ["system-design", "food-delivery", "interview", "distributed-systems"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Food Delivery Platform at Scale](/system-design/food-delivery/). These questions probe logistics matching, telemetry at 100K RPS, checkout consistency, and production failure handling — the topics interviewers dig into after the whiteboard diagram.

---

## Core System Strategy (1–10)

**1. How do you avoid dual-allocation of a delivery partner?**

Use atomic transactions in Redis via Lua scripts. When a driver is selected, the script updates their status from `IDLE` to `ALLOCATED` only if the previous state evaluates as exactly `IDLE`.

**2. What happens if a restaurant accepts an order but cancels 2 minutes later?**

The order service changes state to `REJECTED_BY_RESTAURANT`, fires an event to Kafka, triggers an automated user refund pipeline, and alerts the logistics service to offer a voucher.

**3. How do you manage database schema upgrades for the high-volume orders table without downtime?**

Use the expand-contract pattern: add the field as nullable, update application code to write to both fields, backfill historical data in batches, and safely deprecate the old column.

**4. Why choose Geohashing over R-Tree indexes like PostGIS for high-frequency location updates?**

R-Tree writes scale poorly on disk under high write volumes. Representing coordinates as base32 Geohash keys turns complex spatial lookups into simple string matches inside memory caches.

**5. How do you prevent cascading failure of the order processing service if the payment gateway experiences latency spikes?**

Implement a circuit breaker (e.g., Resilience4j) on the payment API client. If latency spikes or error rates cross thresholds, open the breaker immediately and fail fast to save core resources.

**6. How do you prevent data loss if a driver's network drops out while they are in transit?**

The mobile client caches location updates locally in an SQLite store. When connectivity returns, it flushes the backlogged telemetry frames to the ingestion backend in a compressed batch payload.

**7. What is your data archiving strategy for handling old historical order metrics?**

Implement a cron job that copies data older than 90 days out of PostgreSQL primary instances and stores it as partitioned Parquet files in an S3 data lake for long-term analytical queries.

**8. How do you calculate delivery ETA accurately in real time?**

Combine historical route durations with live traffic data and preparation updates from the restaurant, running these variables through a dedicated machine learning estimation model.

**9. How do you scale WebSocket connections to handle millions of concurrent active users?**

Deploy a dedicated fleet of stateless WebSocket gateway nodes behind an AWS Network Load Balancer configured with consistent routing policies to distribute connection footprints evenly.

**10. How do you protect your internal microservices from a distributed denial-of-service (DDoS) attack?**

Deploy AWS Shield Advanced at the edge network layer, backed by Cloudflare web application protection rules to drop malicious traffic before it reaches your internal API gateways.

---

## Data Engineering & Edge Management (11–20)

**11. How do you resolve out-of-order event streams in Kafka if a driver client redelivers failed packets?**

Include an increasing timestamp value in every telemetry message payload. The ingestion workers ignore incoming data frames if the timestamp is older than the latest entry processed.

**12. What strategy prevents popular "viral" restaurants from overwhelming database storage engines?**

Isolate high-volume menu data inside dedicated Redis read instances, completely bypassing the relational database for standard, non-checkout menu lookups.

**13. How do you handle a scenario where a user changes their delivery address mid-transit?**

The order service checks the new location, calculates the price variance, updates the route, and pushes the updated path to the driver app via live WebSocket channels.

**14. Why run a local Redis cache inside the API Gateway layer?**

It intercepts high-frequency duplicate queries (such as global configuration lookups) right at the edge, protecting downstream internal services from unnecessary processing overhead.

**15. How do you handle connection pooling configurations when your system scales out to thousands of app containers?**

Deploy a dedicated connection proxy layer like PgBouncer as a sidecar for your databases. This layer pools thousands of ephemeral application connections into a stable, high-performance pool.

**16. What happens if an order event is written to the database but the message queue broker fails before publishing?**

Implement the transactional outbox pattern. Write both the order record and the event into the same database transaction, then use a log miner like Debezium to stream events out reliably.

**17. How do you safely store and handle user passwords?**

Hash credentials on isolated authentication servers using the Argon2id derivation function, storing the resulting salt and hash patterns within protected user table structures.

**18. How do you minimize network data costs for high-volume telemetry traffic?**

Replace heavy JSON payloads with Protocol Buffers (Protobuf). This structural change reduces network transmission sizes by up to 70% per packet.

**19. How do you detect fraudulent GPS spoofing attempts in the driver application?**

Run a background component that monitors incoming telemetry pings, flagging historical steps that imply unrealistic speeds or impossible changes in direction.

**20. What strategy keeps Elasticsearch and primary databases synchronized without lagging?**

Use a Change Data Capture (CDC) engine to read PostgreSQL transaction logs directly, avoiding application-level dual-writes and processing updates asynchronously.

---

## Logistics Architecture & Engine (21–30)

**21. How does your architecture handle sudden system load spikes during unexpected rainstorms?**

The system monitors drop-offs in delivery velocity, automatically triggers surge pricing models, and scales out application containers using automated Kubernetes orchestration.

**22. What database lock type ensures cart items remain accurate during high-volume flash sales?**

Use pessimistic locking with short timeouts (`SELECT FOR UPDATE NOWAIT`) on the stock line items to prevent over-allocation issues.

**23. How do you prevent multi-pod worker assignment loops from picking up the same unassigned order?**

Group Kafka order partitions using a single consumer group ID. This setup guarantees that each order record is handled by exactly one worker instance at a time.

**24. How do you manage connections safely if a third-party payment vendor suffers a complete blackout?**

Use a circuit breaker to stop outbound calls, update the user interface to hide the broken payment option, and route new checkout requests through healthy backup vendors instead.

**25. Why use cursor-based pagination over traditional limit-offset strategies for restaurant feeds?**

Limit-offset lookups slow down as deep pages are scanned and can skip items if the underlying data changes. Cursor pagination ensures stable, high-performance lookups.

**26. How do you handle cold-start issues for newly registered restaurants on the platform?**

Inject new restaurant profiles directly into localized discovery search caches with a temporary boost score, ensuring they receive immediate visibility in nearby user feeds.

**27. What strategy allows you to safely change or update live logistics matching models without disruption?**

Deploy the new routing logic behind a feature flag system, allowing you to run controlled A/B split tests on isolated user groups in production.

**28. How do you track application health metrics without introducing performance overhead?**

Have microservices export performance counters asynchronously to local Prometheus scrapers, separating operational metrics collection from the core request path.

**29. How do you prevent large analytical reports from slowing down live transactional services?**

Route analytical workloads to read replicas or a dedicated Snowflake data warehouse, completely isolating reporting queries from the transactional order engine.

**30. What approach minimizes cross-region latency for international deployments?**

Deploy the user-facing discovery and search microservices to multiple geographical regions close to users, keeping read paths local while routing transactional mutations back home.

---

## High Availability, Security & Failure (31–40)

**31. How do you protect data consistency across services without using slow two-phase commit (2PC) blocks?**

Implement the Saga pattern using an orchestrator component. This pattern manages multi-service workflows using a sequence of local transactions and matching compensation steps.

**32. How do you safely scale your caching cluster without dropping active data keys?**

Use consistent hashing algorithms across your Redis shards, ensuring that adding or removing nodes only redistributes a predictable fraction of the key space.

**33. What happens if a database failover script accidentally promotes two master nodes at the same time?**

Use fencing tokens and lease mechanisms managed by a consensus tool like etcd to ensure only one database instance can claim the master address.

**34. How do you balance high-volume logging requirements with high infrastructure costs?**

Dynamic sampling configurations: log all failed transactions and warnings, but drop 95% of standard HTTP 200 tracking logs during peak operation windows.

**35. How do you prevent malicious users from abusing SMS login verification pathways?**

Enforce strict IP-address and phone-number rate limiting rules at the API Gateway using a sliding-window algorithm backed by a Redis cluster.

**36. What is your recovery strategy if an accidental drop-table query runs on production storage?**

Point the environment to a Point-in-Time Recovery (PITR) backup snapshot, rolling the database state forward to the exact second before the drop query executed.

**37. How do you prevent long-running WebSocket connections from consuming too much system memory?**

Configure strict read-write inactivity timeouts, enforcing heartbeat checks that disconnect stale or unresponsive client connections within 2 minutes.

**38. How do you isolate faulty microservice updates without rolling back your entire deployment?**

Deploy your applications using canary releases within a service mesh like Istio, routing a small percentage of live traffic to the new build before full rollout.

**39. Why avoid hardcoded service credentials inside application source repositories?**

Hardcoded keys risk accidental exposure. Inject credentials dynamically at runtime using a secure secret management vault like HashiCorp Vault.

**40. How do you manage high-throughput telemetry streams when Kafka brokers go offline completely?**

Route incoming telemetry data frames directly to an internal memory cluster, temporarily bypassing message logs until the core brokers recover.

---

## Edge Case Optimization (41–50)

**41. How do you manage dynamic restaurant hours when a kitchen closes earlier than expected?**

The operator mutation updates the Elasticsearch restaurant status field to `false` instantly, causing discovery queries to drop the venue from active feeds.

**42. What strategy prevents database deadlocks when multiple workers process identical order lists?**

Sort all target item rows by primary ID key sequence before requesting data locks, ensuring consistent execution orders across all parallel worker threads.

**43. How do you verify the system can survive a total infrastructure failure under peak load?**

Run scheduled chaos engineering drills (like Chaos Mesh) directly in production, intentionally crashing nodes to verify automated self-healing mechanisms.

**44. How do you prevent old, stale order data from slowing down your primary database engines?**

Apply range-based table partitioning on the `created_at` column, isolating each month's orders into distinct physical sub-tables for predictable query planning.

**45. What happens if a user applies a promotional coupon multiple times using concurrent requests?**

Enforce an isolated distributed lock key (`user:promo:{id}`) during evaluation, rejecting parallel matching mutations until the initial check transaction completes.

**46. How do you protect your web services from malicious SQL injection attack vectors?**

Ban raw string building in data layers, forcing developers to use object-relational mapping frameworks and parameterized query structures exclusively.

**47. How do you handle geographic queries that overlap international country borders?**

Use coordinate math frameworks that handle edge clipping rules, ensuring accurate spatial lookups near borders.

**48. What strategy allows you to safely change or update core database engines with zero platform downtime?**

Deploy a dual-write pipeline to sync both engines simultaneously, verify data parity over a validation window, and switch your traffic routing flags when ready.

**49. How do you keep application dependencies secure against public security exploits?**

Integrate continuous vulnerability scanners (like Snyk) into your deployment pipelines, automatically blocking code builds that introduce high-severity security vulnerabilities.

**50. How do you ensure long-term system maintainability as engineering teams grow?**

Enforce clear interface boundaries between domains, document architecture decisions using structured ADR markdown files, and define strict API schemas using OpenAPI specifications.

---

## Related Reading

- [Designing a Food Delivery Platform at Scale](/system-design/food-delivery/) — full architecture, capacity planning, and failure modes
- [Designing an E-Commerce Platform at Scale](/system-design/ecommerce/) — adjacent checkout and inventory patterns
- [Designing a URL Shortener at Scale](/system-design/urlshortner/) — caching and read/write path separation fundamentals
