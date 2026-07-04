---
title: "Isolation Levels"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "READ COMMITTED, REPEATABLE READ, SERIALIZABLE."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Isolation"
module: 2
moduleTitle: "Core PostgreSQL"
sectionRef: "2.6"
weight: 206
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/isolation-levels/
---

## Quick Revision

Isolation controls what concurrent transactions see. PostgreSQL default is **READ COMMITTED**; **REPEATABLE READ** and **SERIALIZABLE** use snapshot isolation.

---

## Core Concepts

| Level | Dirty read | Non-repeatable read | Phantom |
| :--- | :---: | :---: | :---: |
| READ UNCOMMITTED | — | — | — (acts as READ COMMITTED) |
| **READ COMMITTED** (default) | No | Yes | Yes |
| **REPEATABLE READ** | No | No | No* |
| **SERIALIZABLE** | No | No | No |

*PostgreSQL RR prevents phantoms via snapshot — stricter than SQL standard minimum.

---

## Quick Reference

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN ISOLATION LEVEL SERIALIZABLE;

SHOW transaction_isolation;
```

---

## Snippets

```sql
-- Serializable conflict
BEGIN ISOLATION LEVEL SERIALIZABLE;
SELECT sum(balance) FROM accounts WHERE user_id = 1;
-- concurrent writer commits conflicting update
COMMIT;  -- may raise SQLSTATE 40001
```

---

## Common Gotchas

- READ COMMITTED sees **new** rows committed after each statement in the txn.
- REPEATABLE READ holds one snapshot for the whole transaction.
- SERIALIZABLE adds predicate locking — retry on `serialization_failure`.

---


## Interview Answers

## Question {#q-21}

What isolation level is PostgreSQL default and what anomalies remain?

### Short Answer

Default is **READ COMMITTED** — each statement sees newly committed rows; non-repeatable reads and phantoms are possible.

### Detailed Explanation

READ COMMITTED re-snapshots between statements. REPEATABLE READ holds one snapshot for the transaction (PostgreSQL snapshot isolation, stronger than SQL minimum for phantoms). SERIALIZABLE adds SSI predicate checks.

### Internal Working

Isolation is implemented via snapshots + locks for writes, not reader locks.

### Production Notes

Use SERIALIZABLE sparingly with retry on 40001; most OLTP stays READ COMMITTED.

### Common Mistakes

Assuming REPEATABLE READ matches Oracle's behavior in all edge cases.

### Follow-up Questions

- When is SERIALIZABLE required?
- What is SQLSTATE 40001?

---

## Question {#q-22}

How does PostgreSQL REPEATABLE READ differ from the SQL standard minimum?

### Short Answer

Isolation is snapshot-based with stronger RR than SQL minimum. This directly answers: how does postgresql repeatable read differ from the sql standard minimum?

### Detailed Explanation

SERIALIZABLE uses SSI to detect dangerous structures. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/isolation-levels/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-23}

What is Serializable Snapshot Isolation and when does SQLSTATE 40001 occur?

### Short Answer

Isolation is snapshot-based with stronger RR than SQL minimum. This directly answers: what is serializable snapshot isolation and when does sqlstate 40001 occur?

### Detailed Explanation

SERIALIZABLE uses SSI to detect dangerous structures. For **Architecture** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/isolation-levels/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-112}

How does SERIALIZABLE isolation protect financial invariants?

### Short Answer

Isolation is snapshot-based with stronger RR than SQL minimum. This directly answers: how does serializable isolation protect financial invariants?

### Detailed Explanation

SERIALIZABLE uses SSI to detect dangerous structures. For **Reliability** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/02-core-postgresql/isolation-levels/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Transactions](/postgresql-cheatsheet/02-core-postgresql/transactions/)
- [Next: Locks](/postgresql-cheatsheet/02-core-postgresql/locks/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
