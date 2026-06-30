---
title: "Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB interview cheat sheet — replica sets, sharding, indexes, consistency, and schema design probes."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Interview"
module: 4
moduleTitle: "Design, Ops & Reference"
sectionRef: "4.5"
ShowToc: true
---

## Executive Summary

Common MongoDB interview themes: **when to choose documents**, **replication vs sharding**, **index design**, **consistency trade-offs**, and **schema embedding decisions**. Answers should tie to access patterns and operational constraints.

---

## Core Concepts — Quick Map

| Topic | What interviewers probe |
| :--- | :--- |
| Data model | Embed vs reference, 16 MB limit |
| Indexes | ESR rule, covered queries, COLLSCAN |
| Replication | Failover, oplog, write concern |
| Sharding | Shard key choice, hot spots |
| Consistency | `readConcern` / `writeConcern` / read preference |
| Transactions | When needed vs overkill |

---

## Interview Probes

{{< interview-answer >}}
**Q:** When would you choose MongoDB over PostgreSQL?

**A:** When the domain is document-shaped (nested JSON, evolving schema), access patterns are keyed lookups rather than heavy multi-table joins, and horizontal scale via sharding is on the roadmap. I'd still flag cross-document consistency needs — PostgreSQL wins for complex relational invariants.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** Explain replica set failover.

**A:** Members heartbeat the primary. If primary is unreachable, eligible secondaries hold an election (majority votes). New primary serves writes. Writes not replicated to majority may roll back. Clients should use replica set URI, retryable writes, and `w: "majority"` for durability.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** How do you pick a shard key?

**A:** High cardinality, even distribution, and alignment with queries so most operations are targeted (single shard). Avoid monotonic keys (`timestamp`, auto-increment) alone — they create hot shards. Often compound: tenant prefix + hashed suffix. Changing shard key later is painful — decide early.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** What is the oplog?

**A:** Capped collection on the primary recording idempotent operations for replication. Secondaries tail the oplog asynchronously. It also backs change streams. Size it so secondaries can catch up after maintenance without full resync.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** Embed or reference?

**A:** Embed when data is bounded, read together, and not shared across parents. Reference when unbounded (comments, events), shared (product catalog referenced by many orders), or independently versioned. MongoDB favors embed-first; normalize when update or size pressure appears.
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** How do you debug a slow query?

**A:** Run `explain("executionStats")` — look for COLLSCAN, high `totalDocsExamined` vs `nReturned`, in-memory sort. Check profiler, `currentOp`, index usage via `$indexStats`. Fix with compound index following ESR (equality, sort, range), projection, or schema redesign.
{{< /interview-answer >}}

---

## Related Topics

- [Previous: Mongo Shell Commands](/mongodb-cheatsheet/mongo-shell-commands/)
- [Architecture](/mongodb-cheatsheet/architecture/)
- [Replication](/mongodb-cheatsheet/replication/)
- [Sharding](/mongodb-cheatsheet/sharding/)
- [Schema Design](/mongodb-cheatsheet/schema-design/)
- [Database Handbook — MongoDB vs PostgreSQL](/database-handbook/mongodb-vs-postgresql/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
