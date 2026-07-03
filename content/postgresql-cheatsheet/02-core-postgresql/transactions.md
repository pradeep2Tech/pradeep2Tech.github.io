---
title: "Transactions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and ACID."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Transactions"
module: 2
moduleTitle: "Core PostgreSQL"
sectionRef: "2.5"
weight: 205
ShowToc: true
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/transactions/
---

## Quick Revision

PostgreSQL is fully **ACID**. Default autocommit wraps each statement; explicit transactions group work atomically.

---

## Core Concepts

| Command | Effect |
| :--- | :--- |
| `BEGIN` / `START TRANSACTION` | Open transaction |
| `COMMIT` | Persist changes |
| `ROLLBACK` | Discard since BEGIN |
| `SAVEPOINT sp` | Nested rollback point |
| `ROLLBACK TO sp` | Undo to savepoint |

---

## Quick Reference

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

BEGIN;
SAVEPOINT before_transfer;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- oops
ROLLBACK TO before_transfer;
COMMIT;
```

---

## Snippets

```sql
-- Serializable retry pattern (app layer)
BEGIN ISOLATION LEVEL SERIALIZABLE;
-- business logic
COMMIT;  -- on 40001 serialization_failure, retry
```

---

## Common Gotchas

- DDL inside a transaction is allowed — `BEGIN; CREATE TABLE ...; ROLLBACK;` works.
- Long transactions block vacuum and bloat tables.
- Use `SET TRANSACTION READ ONLY` for reporting replicas routing.

---

## See Also

- [Previous: MVCC](/postgresql-cheatsheet/02-core-postgresql/mvcc/)
- [Next: Isolation](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)