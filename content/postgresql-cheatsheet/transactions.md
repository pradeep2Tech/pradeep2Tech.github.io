---
title: "Transactions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and ACID recap."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Transactions"
module: 4
moduleTitle: "Transactions & Concurrency"
sectionRef: "4.1"
ShowToc: true
---

## Executive Summary

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

## Related Topics

- [Previous: Perf Tuning](/postgresql-cheatsheet/performance-tuning/)
- [Next: Isolation](/postgresql-cheatsheet/isolation-levels/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
