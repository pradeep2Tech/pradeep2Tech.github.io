---
title: "Sharding"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Citus, foreign data wrappers, and application-level sharding patterns."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Sharding"
module: 5
moduleTitle: "Scaling & High Availability"
sectionRef: "5.2"
ShowToc: true
---

## Executive Summary

PostgreSQL single-node scales vertically; **sharding** spreads data across nodes. Options: **Citus**, **FDW**, or app-level routing.

---

## Core Concepts

| Approach | Trade-off |
| :--- | :--- |
| **Citus** | Native distributed PG — colocation, rebalance |
| **Foreign Data Wrapper** | Federated queries — not true shard autonomy |
| **App routing** | Full control — you own cross-shard queries |
| **Read replicas** | Scale reads, not writes — not sharding |

---

## Quick Reference

```sql
-- Citus (extension) sketch
SELECT create_distributed_table('events', 'tenant_id');

-- postgres_fdw
CREATE EXTENSION postgres_fdw;
CREATE SERVER shard1 FOREIGN DATA WRAPPER postgres_fdw
  OPTIONS (host 'shard1.internal', dbname 'app');
```

---

## Snippets

```sql
-- App-level: tenant_id in every query + connection per shard
-- Avoid cross-shard JOINs in hot paths — aggregate in app or OLAP layer
```

---

## Common Gotchas

- Choose shard key early — resharding is painful.
- Co-locate related tables on same shard (Citus `colocate_with`).
- Global sequences and FK across shards need application patterns.

---

## Related Topics

- [Previous: Partitioning](/postgresql-cheatsheet/partitioning/)
- [Next: Replication](/postgresql-cheatsheet/replication/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
