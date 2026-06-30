---
title: "MVCC"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Tuple visibility, xmin/xmax, snapshots, and vacuum interaction."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "MVCC"
module: 4
moduleTitle: "Transactions & Concurrency"
sectionRef: "4.3"
ShowToc: true
---

## Executive Summary

**Multi-Version Concurrency Control** keeps old row versions for in-flight transactions. Readers don't block writers; **VACUUM** reclaims dead tuples.

---

## Core Concepts

| Concept | Role |
| :--- | :--- |
| `xmin` | Inserting transaction ID |
| `xmax` | Deleting/updating transaction ID |
| **Snapshot** | Visible tuple set for a transaction |
| **Dead tuple** | Old version no longer visible to any snapshot |
| **VACUUM** | Marks space reusable; **FREEZE** prevents wraparound |

---

## Quick Reference

```sql
-- Tuple metadata (extension)
CREATE EXTENSION IF NOT EXISTS pageinspect;
-- heap_page_items, tuple headers — advanced debugging

SELECT relname, n_live_tup, n_dead_tup, last_vacuum, last_autovacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

---

## Snippets

```mermaid
flowchart LR
  write[UPDATE row] --> new[New tuple version]
  write --> old[Old tuple dead]
  old --> vacuum[VACUUM reclaims]
  read[SELECT snapshot] --> visible[Sees live version only]
```

---

## Common Gotchas

- High churn tables need healthy autovacuum — watch `n_dead_tup`.
- Long transactions prevent vacuum from reclaiming space → bloat.
- `SELECT ... FOR UPDATE` locks current row version.

---

## Related Topics

- [Previous: Isolation](/postgresql-cheatsheet/isolation-levels/)
- [Next: Locks](/postgresql-cheatsheet/locks/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
