---
title: "Distributed LRU Cache System Design — Interview Questions"
date: 2026-06-27T14:30:00+00:00
draft: false
description: "Senior-level system design interview questions and answers for a distributed LRU cache — doubly linked list mechanics, consistent hashing, replication lag, cache stampede prevention, and sub-millisecond latency at 347K peak RPS."
tags: ["system-design", "interview", "distributed-systems", "caching", "architecture"]
categories: ["System Design"]
---

Companion Q&A for [Designing a Distributed LRU Cache at Scale](/system-design/distributed-lru-cache/). These questions probe LRU data structure trade-offs, consistent hashing with virtual nodes, replica consistency, stampede prevention, and production operations — the topics interviewers dig into after the whiteboard diagram.

---

## General Design Concepts (1–10)

**1. What is the primary purpose of a distributed LRU cache?**

Store frequently accessed key-value pairs in memory across multiple nodes, automatically evicting the least recently used entries when capacity is reached, while serving reads and writes at sub-millisecond latency.

**2. Why is this system read-heavy, and how does that shape the architecture?**

With a 10:1 read-to-write ratio (~91% reads), the design offloads read traffic to replica nodes, sizes the cluster for ~316K peak read RPS, and accepts eventual consistency on replicas to preserve sub-millisecond read latency.

**3. What is the difference between Cache-Aside and Read-Through patterns?**

In **Cache-Aside**, the application checks the cache first and fetches from the DB on miss, then writes back. In **Read-Through**, the cache layer itself fetches from the DB on miss. This design uses Cache-Aside so the application controls fallback logic and freshness.

**4. Why not use Redis instead of a custom in-memory engine?**

Redis is a valid off-the-shelf choice for many workloads. A custom engine is justified when you need fine-grained control over LRU eviction semantics, memory layout, lock granularity, and replication behavior without Redis protocol overhead — at the cost of operational complexity.

**5. What does "tunable consistency" mean in this context?**

Clients can choose between strict read-your-writes (route to primary) and lower-latency stale reads (route to replica). The trade-off is freshness vs latency — not a single global consistency model.

**6. How does TTL interact with LRU eviction?**

TTL is time-based expiry; LRU is space-based eviction. Both coexist: a key can expire by TTL even if recently used, and LRU evicts the oldest-accessed key when memory is full regardless of TTL.

**7. What is a cache miss, and what should the application do?**

A cache miss occurs when the requested key is absent or expired. The application fetches from the persistent DB (source of truth) and writes the result back to the cache.

**8. Why is sub-millisecond latency a hard constraint?**

At 347K peak RPS, even 1 ms of added latency per request compounds into significant queue buildup, thread pool exhaustion, and cascading timeouts across upstream services.

**9. What role does etcd play vs the cache nodes themselves?**

etcd stores cluster topology (hash ring layout, node health, primary/replica roles). It does not store cache data — only metadata for routing and leader election.

**10. How do you size the total RAM tier?**

Daily write volume (~909 GB/day) × working set ratio (20% actively queried) ≈ **182 GB** operational RAM. Size the cluster to ~256 GB (8 shards × 32 GB) for a 29% overhead buffer.

---

## LRU Data Structure (11–20)

**11. Why use a doubly linked list over a singly linked list for LRU?**

Moving a node to the head requires detaching it from its current position. A singly linked list lacks a `prev` pointer, forcing O(N) traversal. A doubly linked list detaches and re-links in O(1).

**12. Why combine a hash map with a linked list?**

The hash map provides O(1) key lookup. The linked list tracks access recency. Together they enable O(1) get, put, and eviction — neither structure alone achieves all three.

**13. Why is the key duplicated inside the CacheNode struct?**

During tail eviction, the engine must remove the evicted key from the hash map. Storing the key in the node enables O(1) hash map cleanup without a reverse lookup from pointer to key.

**14. Why do reads require a write-lock in a single-node LRU cache?**

A `get` operation promotes the accessed node to the list head by mutating `prev` and `next` pointers. This is a structural write, not a pure read — shared read locks would allow data races on the linked list.

**15. How do you achieve higher read concurrency despite the write-lock?**

At the distributed layer, route read traffic to replica nodes. Each replica has its own lock domain, multiplying effective read throughput across the cluster.

**16. What is the time complexity of get, put, and evict?**

All three are **O(1)** — hash map lookup/insert/delete plus constant-time linked-list pointer updates.

**17. What happens on put when the cache is at capacity and the key is new?**

Evict the tail node (least recently used), remove it from the hash map, then insert the new entry at the head.

**18. What happens on put when the key already exists?**

Update the value in place, move the node to the head — no eviction needed.

**19. How does passive TTL cleanup work?**

On `get`, if `expires_at` is in the past, treat the entry as a miss, remove it from both the hash map and linked list, and return cache miss.

**20. How does active TTL cleanup prevent memory leaks?**

A background task periodically samples random keys and purges expired entries. This prevents dead keys that are never read again from occupying memory indefinitely.

---

## Distributed Architecture (21–30)

**21. Why consistent hashing over static range sharding?**

Static range sharding (e.g. A–M, N–Z) creates hotspots when popular keys share the same prefix. Consistent hashing distributes keys evenly across an abstract token ring regardless of key content.

**22. What are virtual nodes (vnodes), and why use them?**

Virtual nodes map multiple hash ring positions to each physical node. This balances load when the number of physical nodes is small and prevents uneven distribution when nodes have different capacities.

**23. How does adding a new node affect the hash ring?**

Only keys mapped to the new node's vnode ranges need to move. The majority of keys stay on their current shards — unlike naive modulo hashing where every key may reshuffle.

**24. How are writes routed in a primary-replica setup?**

All writes go to the **primary** node for the target shard. If a client sends a write to a replica, the replica rejects it and returns a redirection to the current primary.

**25. Can read replicas guarantee strict linearizability?**

No. Strict linearizability requires routing all operations through the primary, which eliminates the read-offloading benefit. Replicas serve eventually consistent reads with replication lag.

**26. How does the client library avoid a central routing bottleneck?**

It caches the hash ring topology locally from etcd and computes shard routing in-process — no per-request lookup to a central proxy.

**27. What happens when a primary node crashes?**

If the primary misses its heartbeat interval (e.g. 3 seconds), etcd runs a Raft leader election and promotes the most up-to-date replica to primary.

**28. How do you prevent split-brain during a network partition?**

Enforce quorum sizing Q = ⌊N/2⌋ + 1 on the coordination cluster. Only the partition with quorum can elect a new primary.

**29. What is the trade-off of async replication?**

Writes complete fast on the primary without waiting for replica acknowledgment. Replicas may serve slightly stale data until replication catches up.

**30. How do you handle a single shard becoming a hotspot?**

Dynamically split the hotspot vnode range, or apply a local cache layer on upstream application instances for the viral key.

---

## Caching Strategy and Stampede (31–40)

**31. What is a cache stampede?**

When a popular key expires, thousands of parallel requests miss the cache simultaneously and flood the database with identical queries.

**32. How does single-flight prevent cache stampedes?**

Only one worker process acquires a distributed lock and queries the DB to refresh the key. All other requests wait for that update rather than hitting the DB independently.

**33. What is the high-water mark eviction policy?**

If RAM usage crosses 90% of the designated limit, the engine triggers aggressive proactive eviction — dropping tail nodes even if the cache has not reached its maximum item count.

**34. When should you use write-through instead of cache-aside?**

Write-through is better when you want the cache to always reflect the latest write immediately (e.g. session stores). Cache-aside is simpler when the application already manages DB fallback and can tolerate brief inconsistency.

**35. What happens during a full cluster flush?**

All in-memory keys are lost. Cache-aside rebuilds from the DB on demand. Single-flight prevents a stampede during the rebuild phase.

**36. How do you handle a key that is read frequently but never written?**

It stays near the head of the LRU list on every access and is unlikely to be evicted unless memory pressure forces tail eviction or TTL expires.

**37. Should TTL be shorter or longer than typical access intervals?**

TTL should align with business freshness requirements. If TTL is shorter than the access interval, hot keys expire unnecessarily and cause repeated DB fetches.

**38. How does replication lag affect cache-aside correctness?**

If the application writes to the DB and then to the cache, but a read hits a stale replica that hasn't replicated the DB write yet, the application may read old data from the replica and write stale data back to cache. Route read-your-writes to the primary to avoid this.

**39. What metrics indicate a stampede is happening?**

Sudden spike in DB query rate correlated with a cache key expiry event; drop in cache hit rate for a specific key; P99 DB latency spike.

**40. How do you test stampede prevention in production?**

Deliberately expire a hot key under controlled load and verify that DB query count stays at 1 (or near 1) while concurrent cache misses occur.

---

## Operations, Security, and Trade-offs (41–50)

**41. What is the target cache hit rate, and why does it matter?**

Target **> 85%**. Below that threshold, the DB absorbs too much read traffic, violating the sub-millisecond latency SLO and overwhelming the persistent store.

**42. How is rate limiting applied at the edge?**

Token bucket algorithm on the API gateway limits each client ID to **5,000 RPS**, preventing a single tenant from monopolizing cluster resources.

**43. Why mTLS between cluster nodes?**

Mutual TLS authenticates both sides of every node-to-node connection, preventing unauthorized nodes from joining the cluster or intercepting replication traffic.

**44. What is the key length limit, and why enforce it?**

**250 bytes**. Oversized keys waste hash map memory, increase network payload, and may indicate client bugs or abuse.

**45. How do you monitor memory saturation per node?**

Export per-node RAM utilization as a gauge metric. Alert when any node exceeds 80% sustained utilization — trigger vnode rebalancing or shard addition.

**46. What is the difference between Phase 4 (active-passive) and Phase 5 (active-active) multi-region?**

Active-passive has one writable region and read-only replicas elsewhere — simpler but higher write latency for remote users. Active-active allows writes in all regions — faster locally but introduces split-brain and merge conflict complexity.

**47. Why reject PostgreSQL/MySQL as the hot-path storage engine?**

Relational databases write transactions to disk via WAL for durability. Disk I/O introduces millisecond-scale latency that violates the sub-millisecond cache SLO.

**48. How does the design differ from basic static range sharding (A–M)?**

Static range sharding creates distribution imbalances and requires manual resharding. Consistent hashing with vnodes distributes keys evenly and minimizes data movement on topology changes.

**49. What SLO applies to daily read latency?**

At least **99%** of daily read operations must complete in less than **2 ms**.

**50. What is the most important follow-up question after drawing the architecture?**

"How do you handle a viral key expiring at peak traffic?" — this tests whether the candidate understands cache stampedes, single-flight, and the interaction between TTL, LRU eviction, and DB fallback.
