---
title: "Locks"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Row/table/advisory locks, deadlocks, pg_locks."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Locks"
module: 2
moduleTitle: "Core PostgreSQL"
sectionRef: "2.7"
weight: 207
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/locks/
---

## Quick Revision

Locks serialize conflicting access. Row-level locks are default for DML; DDL takes stronger locks. **Advisory locks** coordinate app-level mutexes.

---

## Core Concepts

| Lock | Typical cause |
| :--- | :--- |
| `RowExclusive` | INSERT/UPDATE/DELETE |
| `ShareRowExclusive` | CREATE TRIGGER, some ALTER |
| `AccessExclusive` | DROP, TRUNCATE, VACUUM FULL — blocks all |
| `Advisory` | `pg_advisory_lock(key)` app mutex |

---

## Quick Reference

```sql
-- Session diagnostics → [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)

SELECT l.pid, l.mode, l.granted, a.query
FROM pg_locks l
JOIN pg_stat_activity a ON a.pid = l.pid
WHERE NOT l.granted;

SELECT pg_cancel_backend(pid);      -- polite
SELECT pg_terminate_backend(pid);   -- force
```

---

## Snippets

```sql
-- Advisory lock (session-level)
SELECT pg_advisory_lock(42);
-- critical section
SELECT pg_advisory_unlock(42);

-- Row lock
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
```

---

## Common Gotchas

- Deadlock → PostgreSQL aborts one transaction — app should retry.
- `LOCK TABLE` in migrations — schedule off-peak.
- `NOWAIT` / `SKIP LOCKED` for queue workers.

---


## Interview Answers

## Question {#q-24}

What row-level locks does SELECT FOR UPDATE acquire?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: what row-level locks does select for update acquire?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-25}

How does PostgreSQL detect and resolve deadlocks?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: how does postgresql detect and resolve deadlocks?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-26}

What is AccessExclusiveLock and which operations require it?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: what is accessexclusivelock and which operations require it?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-27}

When are advisory locks preferable to row locks for application coordination?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: when are advisory locks preferable to row locks for application coordination?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-57}

How do you trace a deadlock from PostgreSQL logs?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: how do you trace a deadlock from postgresql logs?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-58}

What application patterns prevent deadlocks in fund-transfer workflows?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: what application patterns prevent deadlocks in fund-transfer workflows?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-59}

How does SKIP LOCKED support concurrent job queue workers?

### Short Answer

Transaction IDs are 32-bit and wrap; **freeze** marks old tuples frozen so xmin can be reused; if age exceeds `autovacuum_freeze_max_age`, aggressive autovacuum or shutdown protection triggers.

### Detailed Explanation

Every table has `relfrozenxid`. Vacuum freeze updates tuple xmin to FrozenTransactionId. If age(datfrozenxid) approaches 2^31, PostgreSQL enters anti-wraparound autovacuum; failure to freeze can force shutdown to prevent catalog corruption.

### Production Notes

Monitor `age(datfrozenxid)` per database; tune autovacuum freeze thresholds on high-churn tables.

### Common Mistakes

Disabling autovacuum globally on 'append-only' systems that still UPDATE/DELETE.

### Follow-up Questions

- What is multixact wraparound?
- How does pg_repack interact with freeze?

---

## Question {#q-60}

Why do migrations with ACCESS EXCLUSIVE locks cause outages?

### Short Answer

Row locks serialize conflicting writes; DDL takes stronger table locks. This directly answers: why do migrations with access exclusive locks cause outages?

### Detailed Explanation

Deadlocks are detected via wait-for graph and one session is aborted. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/locks/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Isolation](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/)
- [Next: Indexes](/postgresql-cheatsheet/03-query-performance/indexes/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
