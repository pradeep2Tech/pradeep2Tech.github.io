---
title: "Consistency Models — Architect Guide"
date: 2026-07-04T11:00:00+00:00
draft: false
description: "Consistency models for distributed systems — strong, eventual, causal, read-your-writes, and interview trade-offs with availability and latency."
tags: ["system-design", "distributed-systems", "consistency", "interview"]
categories: ["System Design"]
shortTitle: "Consistency Models"
module: 2
moduleTitle: "Distributed Systems"
sectionRef: "2.2"
ShowToc: true
---

## Overview

A **consistency model** defines what guarantees readers observe after writes in a distributed system — whether all clients see the same value immediately, in order, or eventually. It is the bridge between [CAP & PACELC](/system-design/cap-and-pacelc/) and concrete architecture (replicas, caches, queues).

Architects pick a model per **use case**, not globally. Ledgers need strong consistency; feeds tolerate eventual consistency with bounded staleness.

---

## Why It Matters

| Wrong model | Production symptom |
| :--- | :--- |
| Eventual on payments | Double spend, negative balance |
| Strong everywhere | High latency, regional outage sensitivity |
| No read-your-writes | User “doesn’t see” their own post after submit |
| Ignoring monotonic reads | UI flickers backward in time |

Interviewers ask consistency to see if you distinguish **user-visible anomalies** from academic definitions.

---

## Core Concepts

### Consistency spectrum

```mermaid
flowchart LR
    STRONG[Strong / Linearizable]
    SEQ[Sequential]
    CAUSAL[Causal]
    EVENTUAL[Eventual]
    STRONG --> SEQ --> CAUSAL --> EVENTUAL
```

| Model | Guarantee (simplified) | Typical latency | Example use |
| :--- | :--- | :--- | :--- |
| **Strong / linearizable** | All ops appear in one global order | Highest | Locks, leader election, money |
| **Sequential** | All see same order of ops | High | Coordination services |
| **Causal** | Causally related ops seen in order | Medium | Comment threads, messaging |
| **Read-your-writes** | User sees own updates | Medium | Profile edit, session state |
| **Monotonic reads** | No time travel on reads | Medium | Feed scroll |
| **Eventual** | Replicas converge if no new writes | Lowest | Counters, analytics, CDN |

### Client-visible anomalies

| Anomaly | Description | Prevented by |
| :--- | :--- | :--- |
| **Dirty read** | Read uncommitted data | Read committed+ |
| **Stale read** | Replica lag | Sync read, RYW routing |
| **Lost update** | Concurrent writes overwrite | Transactions, CAS, CRDT |
| **Write skew** | Two transactions read disjoint rows, conflict | Serializable isolation |

Single-node anomalies map to [ACID isolation levels](/system-design/database-transactions-and-acid-isolation/). Distributed consistency adds **replication lag** and **partition** behavior.

### Consistency vs isolation vs CAP

| Concept | Scope | Question answered |
| :--- | :--- | :--- |
| **ACID isolation** | Single database | What anomalies can concurrent TX see? |
| **Consistency model** | Replicated / distributed store | What do clients see across replicas? |
| **CAP** | Under partition | C or A when network splits? |

### Choosing a model (decision table)

| Data type | Recommended model | Mechanism |
| :--- | :--- | :--- |
| Account balance | Strong | Single primary + sync replica or consensus |
| Product catalog | Eventual + short TTL cache | Async replication |
| User session prefs | Read-your-writes | Sticky routing or primary read-after-write |
| Social timeline | Eventual / causal | Async fan-out, version vectors |
| Collaborative edit | CRDT / causal | [CRDTs](/system-design/crdts-and-multi-master-conflict-resolution/) |

---

## Architect Perspective

### Interview framework

1. **Classify the operation** — read vs write; user-scoped vs global
2. **Name acceptable staleness** — “30s old feed OK?”
3. **Pick routing** — primary read, quorum, sticky session
4. **State failure under partition** — link to [CAP & PACELC](/system-design/cap-and-pacelc/)
5. **Mention conflict resolution** — merge, LWW, CRDT, saga

### Replication patterns vs consistency

| Pattern | Consistency profile |
| :--- | :--- |
| Single leader | Strong on primary; bounded stale on replicas |
| Multi-leader | Causal/eventual; conflicts possible |
| Leaderless quorum | Tunable (R+W > N) |

See [Replication Lag & Read Replicas](/system-design/replication-lag-read-replica-topology/).

---

## Common Mistakes

| Mistake | Fix |
| :--- | :--- |
| “We use strong consistency” without defining scope | Per entity or per operation |
| Assuming cache is consistent with DB | TTL + invalidation strategy |
| Ignoring read-your-writes after redirect | Route post-write reads to primary |
| Using LWW globally | Silent data loss in multi-master |

---

## Interview Questions

1. **Difference between strong consistency and serializable isolation?**
2. **Design read path for a profile update — how soon does user see change?**
3. **What is eventual consistency? Give a product where it fits.**
4. **How do vector clocks relate to causal consistency?**
5. **Quorum read R=2, W=2, N=3 — what consistency do you get?**

**Case studies:** [Hotel Booking](/system-design/hotel-booking/) · [Stock Broker](/system-design/stock-broker-trading/) · [Social Feed](/system-design/social-feed/)

---

## Related Topics

- [CAP & PACELC](/system-design/cap-and-pacelc/)
- [Database Transactions & ACID](/system-design/database-transactions-and-acid-isolation/)
- [CRDTs & Multi-Master](/system-design/crdts-and-multi-master-conflict-resolution/)
- [Replication Lag](/system-design/replication-lag-read-replica-topology/)
- [Capacity Estimation](/system-design/capacity-estimation/) — read/write ratio drives consistency cost

---

## Deep Dive References

| Topic | Location |
| :--- | :--- |
| Concurrency control & isolation (PRIMARY) | [Microservices — Concurrency Control](/microservices/04-distributed-systems/concurrency-control/) |
| CAP & PACELC (PRIMARY) | [Microservices — CAP & PACELC](/microservices/04-distributed-systems/cap-and-pacelc/) |
