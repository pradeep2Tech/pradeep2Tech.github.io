---
title: "Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "PostgreSQL interview probes — MVCC, indexes, replication, and tuning."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Interview"
module: 9
moduleTitle: "Interview Prep"
sectionRef: "9.1"
ShowToc: true
---

## Executive Summary

Common PostgreSQL interview themes: **MVCC**, **indexes**, **isolation**, **replication**, **VACUUM**, and practical SQL tuning.

---

## Core Concepts

| Topic | Probe |
| :--- | :--- |
| MVCC | Why UPDATE creates a new row version |
| Indexes | When GIN beats B-tree |
| Isolation | Difference READ COMMITTED vs REPEATABLE READ |
| Locks | `FOR UPDATE` vs `FOR SHARE` |
| Replication | Streaming vs logical — use cases |
| Performance | How you'd debug a slow query |

---

## Quick Reference

```sql
-- "Find missing index" pattern
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
-- Seq Scan on huge table + high filter selectivity → candidate for index
```

---

## Snippets

{{< interview-answer question="Why does PostgreSQL need VACUUM?" >}}
Updates and deletes leave **dead tuples**. MVCC keeps old versions visible to open transactions. VACUUM marks dead space reusable and prevents transaction ID wraparound. Without it, tables bloat and eventually the cluster risks shutdown for wraparound protection.
{{< /interview-answer >}}

{{< interview-answer question="Explain partial vs covering index." >}}
A **partial** index indexes a subset of rows (`WHERE active`) — smaller and faster for targeted queries. A **covering** index includes extra columns via `INCLUDE` so an **Index Only Scan** can satisfy the query without heap visits, reducing I/O.
{{< /interview-answer >}}

{{< interview-answer question="How does PostgreSQL implement REPEATABLE READ?" >}}
The transaction takes a **snapshot** at first statement (or transaction start depending on version/config). All reads see the same snapshot; concurrent commits by others are invisible for reads. Writes can still conflict — serialization failures possible on conflicting updates.
{{< /interview-answer >}}

---

## Common Gotchas

- Tie answers to production: connection pooling, `pg_stat_statements`, replication lag.
- Mention trade-offs, not buzzwords — interviewers probe depth.
- Cross-link handbook pages for MVCC, indexes, and EXPLAIN.

---

## Related Topics

- [Previous: Backup](/postgresql-cheatsheet/backup-restore/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
