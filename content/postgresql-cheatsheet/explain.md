---
title: "EXPLAIN"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "EXPLAIN, ANALYZE, BUFFERS — read plans, costs, and node types."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "EXPLAIN"
module: 3
moduleTitle: "Query Performance"
sectionRef: "3.2"
ShowToc: true
---

## Executive Summary

`EXPLAIN` shows the planner's chosen path. Add **ANALYZE** to execute and show actual row counts and timing; **BUFFERS** reveals cache hits.

---

## Core Concepts

| Node | Meaning |
| :--- | :--- |
| `Seq Scan` | Full table read — OK for small tables |
| `Index Scan` | Index lookup + heap fetch |
| `Index Only Scan` | Satisfied from index — ideal |
| `Bitmap Heap Scan` | Index bitmap then heap visit |
| `Nested Loop` | Good for small outer sets |
| `Hash Join` | Build hash on inner — equality joins |
| `Merge Join` | Pre-sorted inputs |

---

## Quick Reference

```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 42;

EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 42;

EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)
SELECT o.* FROM orders o JOIN users u ON u.id = o.user_id WHERE u.email = 'a@b.com';
```

---

## Snippets

```sql
-- Compare estimated vs actual rows — big gaps mean stale stats
-- Run: ANALYZE orders;

-- Force plan for testing only (session-local)
SET enable_seqscan = off;
```

---

## Common Gotchas

- High **actual** vs **estimated** rows → run `ANALYZE` or increase `default_statistics_target`.
- `EXPLAIN` without `ANALYZE` is cheap but can mislead on row estimates.
- Use `pg_stat_statements` for production workload — not ad-hoc EXPLAIN everywhere.

---

## Related Topics

- [Previous: Indexes](/postgresql-cheatsheet/indexes/)
- [Next: Perf Tuning](/postgresql-cheatsheet/performance-tuning/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
