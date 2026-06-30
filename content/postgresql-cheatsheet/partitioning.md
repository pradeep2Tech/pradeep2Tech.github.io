---
title: "Partitioning"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Declarative RANGE, LIST, HASH partitioning and partition pruning."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Partitioning"
module: 5
moduleTitle: "Scaling & High Availability"
sectionRef: "5.1"
ShowToc: true
---

## Executive Summary

**Declarative partitioning** splits one logical table into physical children. Pruning skips irrelevant partitions at plan time.

---

## Core Concepts

| Method | Key |
| :--- | :--- |
| **RANGE** | Dates, numeric ranges |
| **LIST** | Discrete values (region, status) |
| **HASH** | Even spread when no natural key |

---

## Quick Reference

```sql
CREATE TABLE measurements (
  id bigserial,
  device_id int NOT NULL,
  recorded_at timestamptz NOT NULL,
  value double precision
) PARTITION BY RANGE (recorded_at);

CREATE TABLE measurements_2026_01 PARTITION OF measurements
  FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');

CREATE INDEX ON measurements (device_id, recorded_at);
```

---

## Snippets

```sql
-- Attach existing table as partition
CREATE TABLE measurements_old (LIKE measurements INCLUDING ALL);
ALTER TABLE measurements ATTACH PARTITION measurements_old
  FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

---

## Common Gotchas

- Partition key must appear in PK/unique constraints (include partition key).
- Create future partitions before data arrives — or use `DEFAULT` partition.
- Global uniqueness across partitions requires careful constraint design.

---

## Related Topics

- [Previous: Locks](/postgresql-cheatsheet/locks/)
- [Next: Sharding](/postgresql-cheatsheet/sharding/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
