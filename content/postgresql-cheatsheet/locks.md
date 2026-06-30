---
title: "Locks"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Row/table/advisory locks, deadlocks, and pg_locks diagnostics."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Locks"
module: 4
moduleTitle: "Transactions & Concurrency"
sectionRef: "4.4"
ShowToc: true
---

## Executive Summary

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
SELECT pid, wait_event_type, wait_event, query
FROM pg_stat_activity
WHERE state != 'idle';

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

## Related Topics

- [Previous: MVCC](/postgresql-cheatsheet/mvcc/)
- [Next: Partitioning](/postgresql-cheatsheet/partitioning/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
