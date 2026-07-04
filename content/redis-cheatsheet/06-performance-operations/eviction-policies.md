---
title: "Eviction Policies"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "Maxmemory policies, LRU/LFU behavior, and tradeoffs."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Eviction"
module: 6
moduleTitle: "Performance & Operations"
sectionRef: "6.1"
weight: 601

aliases:
  - "/redis-cheatsheet/eviction-policies/"
---

## Executive Summary

When **`maxmemory`** is hit, Redis evicts keys per **`maxmemory-policy`** â€” critical for cache workloads. **noeviction** returns errors instead (good for non-cache primary store).

---

## Core Concepts

| Policy | Evicts |
| :--- | :--- |
| `noeviction` | Nothing â€” writes fail |
| `allkeys-lru` | Any key â€” approximate LRU |
| `allkeys-lfu` | Any key â€” frequency (Redis 4+) |
| `volatile-lru` | Keys with TTL only |
| `volatile-lfu` | TTL keys by frequency |
| `volatile-ttl` | Shortest TTL first |
| `allkeys-random` / `volatile-random` | Random |

**LRU** is sampled (`maxmemory-samples`), not exact global LRU.

---

## Quick Reference

```bash
CONFIG GET maxmemory
CONFIG GET maxmemory-policy
CONFIG SET maxmemory 4gb
CONFIG SET maxmemory-policy allkeys-lfu
INFO memory
```

---

## Snippets

```conf
maxmemory 2gb
maxmemory-policy allkeys-lfu
maxmemory-samples 10
```

Set **TTL on cache keys** when using `volatile-*` policies.

---

## Common Gotchas

| Pitfall | Fix |
| :--- | :--- |
| `volatile-lru` but keys have no TTL | Nothing evicted â†’ OOM |
| Hot key evicted with LRU | Consider `lfu` or app-level TTL jitter |
| No `maxmemory` in container | Set to ~75% of container limit |

---

## When is noeviction the correct maxmemory-policy for a non-cache primary store?

### Short Answer
The production-grade Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by alerting before hit ratio collapses and testing eviction under synthetic fill for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When is noeviction the correct maxmemory-policy for a non-cache primary store?

---
## How would you investigate volatile-lru not evicting keys when memory is full?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How would you investigate volatile-lru not evicting keys when memory is full.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How would you investigate volatile-lru not evicting keys when memory is full.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How would you investigate volatile-lru not evicting keys when memory is full.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: How would you investigate volatile-lru not evicting keys when memory is full.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How would you investigate volatile-lru not evicting keys when memory is full.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How would you investigate volatile-lru not evicting keys when memory is full?

---
## When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

---
## How do maxmemory-samples settings affect eviction accuracy and CPU?

### Short Answer
For this question, the architecturally correct Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by alerting before hit ratio collapses and testing eviction under synthetic fill for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How do maxmemory-samples settings affect eviction accuracy and CPU?

---
<!-- interview-answers:end -->

---

## When is noeviction the correct maxmemory-policy for a non-cache primary store?

### Short Answer
The production-grade Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by alerting before hit ratio collapses and testing eviction under synthetic fill for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When is noeviction the correct maxmemory-policy for a non-cache primary store?

---
## How would you investigate volatile-lru not evicting keys when memory is full?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How would you investigate volatile-lru not evicting keys when memory is full.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How would you investigate volatile-lru not evicting keys when memory is full.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How would you investigate volatile-lru not evicting keys when memory is full.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: How would you investigate volatile-lru not evicting keys when memory is full.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How would you investigate volatile-lru not evicting keys when memory is full.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How would you investigate volatile-lru not evicting keys when memory is full?

---
## When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

---
## How do maxmemory-samples settings affect eviction accuracy and CPU?

### Short Answer
For this question, the architecturally correct Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by alerting before hit ratio collapses and testing eviction under synthetic fill for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How do maxmemory-samples settings affect eviction accuracy and CPU?

---
<!-- interview-answers:end -->

---

## When is noeviction the correct maxmemory-policy for a non-cache primary store?

### Short Answer
The production-grade Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by alerting before hit ratio collapses and testing eviction under synthetic fill for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When is noeviction the correct maxmemory-policy for a non-cache primary store?

---
## How would you investigate volatile-lru not evicting keys when memory is full?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How would you investigate volatile-lru not evicting keys when memory is full.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How would you investigate volatile-lru not evicting keys when memory is full.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How would you investigate volatile-lru not evicting keys when memory is full.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: How would you investigate volatile-lru not evicting keys when memory is full.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How would you investigate volatile-lru not evicting keys when memory is full.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How would you investigate volatile-lru not evicting keys when memory is full?

---
## When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

---
## How do maxmemory-samples settings affect eviction accuracy and CPU?

### Short Answer
For this question, the architecturally correct Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by alerting before hit ratio collapses and testing eviction under synthetic fill for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How do maxmemory-samples settings affect eviction accuracy and CPU?

---
<!-- interview-answers:end -->

---

## When is noeviction the correct maxmemory-policy for a non-cache primary store?

### Short Answer
The production-grade Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by alerting before hit ratio collapses and testing eviction under synthetic fill for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When is noeviction the correct maxmemory-policy for a non-cache primary store?

---
## How would you investigate volatile-lru not evicting keys when memory is full?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How would you investigate volatile-lru not evicting keys when memory is full.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How would you investigate volatile-lru not evicting keys when memory is full.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How would you investigate volatile-lru not evicting keys when memory is full.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: How would you investigate volatile-lru not evicting keys when memory is full.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How would you investigate volatile-lru not evicting keys when memory is full.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How would you investigate volatile-lru not evicting keys when memory is full?

---
## When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

---
## How do maxmemory-samples settings affect eviction accuracy and CPU?

### Short Answer
For this question, the architecturally correct Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by alerting before hit ratio collapses and testing eviction under synthetic fill for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How do maxmemory-samples settings affect eviction accuracy and CPU?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Rate Limiter](/redis-cheatsheet/05-production-patterns/rate-limiter/)
- [Next: Performance Tuning](/redis-cheatsheet/06-performance-operations/performance-tuning/)
- [Redis Handbook Index](/redis-cheatsheet/)
- [Top 150 Interview Questions](/redis-cheatsheet/08-interview-guide/top-150-interview-questions/)
