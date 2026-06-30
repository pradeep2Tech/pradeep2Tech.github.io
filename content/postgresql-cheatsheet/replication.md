---
title: "Replication"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Streaming replication, logical replication, slots, and failover basics."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Replication"
module: 5
moduleTitle: "Scaling & High Availability"
sectionRef: "5.3"
ShowToc: true
---

## Executive Summary

**Streaming replication** ships WAL to standbys for HA. **Logical replication** publishes table changes for migrations and fan-out.

---

## Core Concepts

| Mode | Use |
| :--- | :--- |
| Physical / streaming | Hot standby, failover |
| Logical | Selective tables, upgrades, CDC |
| Replication slot | Prevents WAL removal until consumed |

---

## Quick Reference

```sql
-- On primary
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'secret';

-- pg_hba.conf: host replication replicator 10.0.0.0/24 scram-sha-256

-- Logical publication
CREATE PUBLICATION app_pub FOR TABLE orders, customers;
```

---

## Snippets

```bash
# Standby base backup
pg_basebackup -h primary -D /var/lib/postgresql/data -U replicator -Fp -Xs -P -R
```

---

## Common Gotchas

- Async replication → potential data loss on failover — know RPO.
- Replication slots on idle subscribers can fill disk with WAL.
- `pg_switch_wal()` before promotion in orchestrated failover.

---

## Related Topics

- [Previous: Sharding](/postgresql-cheatsheet/sharding/)
- [Next: Views](/postgresql-cheatsheet/views/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
