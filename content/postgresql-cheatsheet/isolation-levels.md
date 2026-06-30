---
title: "Isolation Levels"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "READ COMMITTED, REPEATABLE READ, SERIALIZABLE — anomalies and defaults."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Isolation"
module: 4
moduleTitle: "Transactions & Concurrency"
sectionRef: "4.2"
ShowToc: true
---

## Executive Summary

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

## Related Topics

- [Previous: Transactions](/postgresql-cheatsheet/transactions/)
- [Next: MVCC](/postgresql-cheatsheet/mvcc/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
