---
title: "Top 150 PostgreSQL Interview Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "150 production-oriented PostgreSQL interview questions mapped to handbook topics."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Top 150"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.1"
weight: 801
interviewHandbook: true
---

Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. Questions only — no answers. Each row links to the canonical deep-dive page.

## Distribution

| Category | Count |
| :--- | :---: |
| Architecture | 40 |
| Troubleshooting | 30 |
| Performance | 25 |
| Reliability | 20 |
| Security | 15 |

| # | Question | Difficulty | Level | Category | Deep Dive |
|---|----------|------------|--------|----------|-----------|
| 1 | How does the postmaster process model differ from thread-per-connection databases? | Medium | Senior Engineer | Architecture | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-1) |
| 2 | What shared memory structures must fit in RAM for a production PostgreSQL cluster? | Hard | Architect | Architecture | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-2) |
| 3 | Why does PostgreSQL fork a new backend per connection, and what scaling problem does that create? | Medium | Senior Engineer | Architecture | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-3) |
| 4 | What is the role of the checkpointer versus the background writer? | Medium | Lead | Architecture | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-4) |
| 5 | How do autovacuum launcher and worker processes interact under load? | Medium | Lead | Architecture | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-5) |
| 6 | Describe heap page layout including line pointers and tuple storage. | Hard | Senior Engineer | Architecture | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-6) |
| 7 | When does PostgreSQL route a column value to TOAST storage? | Medium | Senior Engineer | Architecture | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-7) |
| 8 | What is the Free Space Map used for during inserts? | Medium | Senior Engineer | Architecture | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-8) |
| 9 | How does the visibility map enable index-only scans? | Hard | Lead | Architecture | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-9) |
| 10 | Explain HOT updates and when index entries are skipped. | Hard | Senior Engineer | Architecture | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-10) |
| 11 | How does shared_buffers interact with the operating system page cache? | Medium | Lead | Architecture | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-11) |
| 12 | What is write-ahead logging and why must WAL flush precede commit acknowledgment? | Medium | Senior Engineer | Architecture | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-12) |
| 13 | How do LSN values relate to replication and PITR? | Hard | Lead | Architecture | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-13) |
| 14 | What triggers a checkpoint and how does it bound crash recovery time? | Medium | Lead | Architecture | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-14) |
| 15 | How does crash recovery replay WAL after an unclean shutdown? | Hard | Architect | Architecture | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-15) |
| 16 | How does MVCC allow non-blocking reads while writers update rows? | Medium | Senior Engineer | Architecture | [Mvcc](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-16) |
| 17 | What do xmin and xmax represent in a tuple header? | Medium | Senior Engineer | Architecture | [Mvcc](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-17) |
| 18 | How is transaction snapshot visibility determined for a SELECT? | Hard | Lead | Architecture | [Mvcc](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-18) |
| 19 | Why does UPDATE create a new row version instead of overwriting in place? | Easy | Senior Engineer | Architecture | [Mvcc](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-19) |
| 20 | How do long-running transactions interact with vacuum and bloat? | Hard | Lead | Architecture | [Mvcc](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-20) |
| 21 | What isolation level is PostgreSQL default and what anomalies remain? | Medium | Senior Engineer | Architecture | [Isolation Levels](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/#q-21) |
| 22 | How does PostgreSQL REPEATABLE READ differ from the SQL standard minimum? | Hard | Lead | Architecture | [Isolation Levels](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/#q-22) |
| 23 | What is Serializable Snapshot Isolation and when does SQLSTATE 40001 occur? | Hard | Architect | Architecture | [Isolation Levels](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/#q-23) |
| 24 | What row-level locks does SELECT FOR UPDATE acquire? | Medium | Senior Engineer | Architecture | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-24) |
| 25 | How does PostgreSQL detect and resolve deadlocks? | Medium | Lead | Architecture | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-25) |
| 26 | What is AccessExclusiveLock and which operations require it? | Medium | Lead | Architecture | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-26) |
| 27 | When are advisory locks preferable to row locks for application coordination? | Medium | Senior Engineer | Architecture | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-27) |
| 28 | How does declarative partitioning change planner behavior via partition pruning? | Medium | Lead | Architecture | [Partitioning](/postgresql-cheatsheet/03-query-performance/partitioning/#q-28) |
| 29 | What constraints apply to primary keys on partitioned tables? | Hard | Architect | Architecture | [Partitioning](/postgresql-cheatsheet/03-query-performance/partitioning/#q-29) |
| 30 | When would you choose Citus over native partitioning? | Hard | Architect | Architecture | [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/#q-30) |
| 31 | How does streaming replication ship changes from primary to standby? | Medium | Lead | Architecture | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-31) |
| 32 | What is the difference between physical and logical replication? | Medium | Senior Engineer | Architecture | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-32) |
| 33 | How do replication slots prevent WAL removal? | Medium | Lead | Architecture | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-33) |
| 34 | What HA topology would you design for RPO near zero in a single region? | Hard | Architect | Architecture | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-34) |
| 35 | How does Patroni coordinate failover with a distributed consensus store? | Hard | Architect | Architecture | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-35) |
| 36 | What happens to the old primary after promotion in a split-brain scenario? | Hard | Lead | Architecture | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-36) |
| 37 | How does PgBouncer transaction pooling differ from session pooling architecturally? | Hard | Architect | Architecture | [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-37) |
| 38 | Why is raising max_connections often the wrong fix for connection storms? | Medium | Lead | Architecture | [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-38) |
| 39 | How would you architect read/write splitting with replicas and connection poolers? | Hard | Architect | Architecture | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-39) |
| 40 | When would PostgreSQL be a poor fit compared to a dedicated analytics warehouse? | Medium | Architect | Architecture | [Postgresql Vs Mysql](/postgresql-cheatsheet/07-comparisons/postgresql-vs-mysql/#q-40) |
| 41 | What is your first step when p99 query latency doubles after a deploy? | Medium | Lead | Troubleshooting | [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/#q-41) |
| 42 | How do you find the top 10 queries by total time in production? | Easy | Senior Engineer | Troubleshooting | [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/#q-42) |
| 43 | How do estimated versus actual rows in EXPLAIN ANALYZE guide diagnosis? | Medium | Lead | Troubleshooting | [Explain](/postgresql-cheatsheet/03-query-performance/explain/#q-43) |
| 44 | What indicates a missing index on a large table scan? | Easy | Senior Engineer | Troubleshooting | [Explain](/postgresql-cheatsheet/03-query-performance/explain/#q-44) |
| 45 | How do you identify blocking sessions and their root blockers? | Medium | Lead | Troubleshooting | [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/#q-45) |
| 46 | When should you use pg_cancel_backend versus pg_terminate_backend? | Medium | Lead | Troubleshooting | [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/#q-46) |
| 47 | How do idle-in-transaction sessions cause vacuum starvation? | Hard | Lead | Troubleshooting | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-47) |
| 48 | What pg_stat_user_tables columns signal bloat risk? | Medium | Senior Engineer | Troubleshooting | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-48) |
| 49 | When is VACUUM FULL acceptable versus pg_repack? | Medium | Lead | Troubleshooting | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-49) |
| 50 | How does transaction ID wraparound threaten cluster availability? | Hard | Architect | Troubleshooting | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-50) |
| 51 | What symptoms indicate autovacuum cannot keep up on a hot table? | Medium | Lead | Troubleshooting | [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/#q-51) |
| 52 | How do you tune per-table autovacuum settings for append-mostly versus churn-heavy tables? | Hard | Lead | Troubleshooting | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-52) |
| 53 | What causes replication lag to grow on a standby during heavy write load? | Medium | Lead | Troubleshooting | [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/#q-53) |
| 54 | How can an unused replication slot fill the primary disk with WAL? | Hard | Lead | Troubleshooting | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-54) |
| 55 | How do you diagnose synchronous replication commit stalls? | Hard | Architect | Troubleshooting | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-55) |
| 56 | What wait events suggest IO-bound queries versus lock contention? | Medium | Senior Engineer | Troubleshooting | [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/#q-56) |
| 57 | How do you trace a deadlock from PostgreSQL logs? | Medium | Senior Engineer | Troubleshooting | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-57) |
| 58 | What application patterns prevent deadlocks in fund-transfer workflows? | Medium | Lead | Troubleshooting | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-58) |
| 59 | How does SKIP LOCKED support concurrent job queue workers? | Medium | Senior Engineer | Troubleshooting | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-59) |
| 60 | Why do migrations with ACCESS EXCLUSIVE locks cause outages? | Medium | Lead | Troubleshooting | [Locks](/postgresql-cheatsheet/02-core-postgresql/locks/#q-60) |
| 61 | How do you detect connection leaks from application servers? | Medium | Lead | Troubleshooting | [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/#q-61) |
| 62 | What metrics alert you before max_connections is exhausted? | Medium | Lead | Troubleshooting | [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/#q-62) |
| 63 | How do prepared statements interact with PgBouncer transaction pooling? | Hard | Architect | Troubleshooting | [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-63) |
| 64 | What causes sort operations to spill to disk and how do you confirm? | Medium | Senior Engineer | Troubleshooting | [Explain](/postgresql-cheatsheet/03-query-performance/explain/#q-64) |
| 65 | How do you remediate a query plan regression after statistics drift? | Hard | Lead | Troubleshooting | [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/#q-65) |
| 66 | What steps validate a backup before an incident requires restore? | Medium | Lead | Troubleshooting | [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/#q-66) |
| 67 | How do you perform PITR to a timestamp before accidental DELETE? | Hard | Architect | Troubleshooting | [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/#q-67) |
| 68 | What failures occur when archive_command stops shipping WAL? | Medium | Lead | Troubleshooting | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-68) |
| 69 | How do logical replication conflicts manifest on subscribers? | Hard | Lead | Troubleshooting | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-69) |
| 70 | What is your runbook when the primary runs out of disk on the WAL volume? | Hard | Lead | Troubleshooting | [Troubleshooting](/postgresql-cheatsheet/06-production-operations/troubleshooting/#q-70) |
| 71 | When would you choose a partial index over a full B-tree index? | Medium | Senior Engineer | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-71) |
| 72 | How does a covering index with INCLUDE enable index-only scans? | Medium | Lead | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-72) |
| 73 | When does GIN outperform B-tree for jsonb queries? | Medium | Senior Engineer | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-73) |
| 74 | What is BRIN appropriate for and when is it wrong? | Medium | Lead | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-74) |
| 75 | How do you identify and drop unused indexes safely? | Medium | Lead | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-75) |
| 76 | What does EXPLAIN BUFFERS reveal about cache efficiency? | Medium | Senior Engineer | Performance | [Explain](/postgresql-cheatsheet/03-query-performance/explain/#q-76) |
| 77 | How does increasing default_statistics_target affect plan quality and ANALYZE cost? | Medium | Lead | Performance | [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/#q-77) |
| 78 | When does the planner choose hash join versus nested loop? | Hard | Senior Engineer | Performance | [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/#q-78) |
| 79 | What parameters enable parallel sequential scan and when is parallel harmful? | Hard | Lead | Performance | [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/#q-79) |
| 80 | How should work_mem be sized given concurrent connections? | Hard | Architect | Performance | [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/#q-80) |
| 81 | What is the tradeoff of raising shared_buffers on a 128 GB host? | Medium | Lead | Performance | [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/#q-81) |
| 82 | Why set random_page_cost lower on NVMe-backed instances? | Easy | Senior Engineer | Performance | [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/#q-82) |
| 83 | How does effective_cache_size influence index versus seq scan choices? | Medium | Senior Engineer | Performance | [Query Optimization](/postgresql-cheatsheet/03-query-performance/query-optimization/#q-83) |
| 84 | What CTE materialization hints affect planner inlining in PostgreSQL 12+? | Medium | Senior Engineer | Performance | [Ctes](/postgresql-cheatsheet/01-fundamentals/ctes/#q-84) |
| 85 | How does partition pruning fail when queries omit partition key predicates? | Medium | Lead | Performance | [Partitioning](/postgresql-cheatsheet/03-query-performance/partitioning/#q-85) |
| 86 | What index strategy supports keyset pagination at scale? | Hard | Lead | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-86) |
| 87 | How do you reduce write amplification from too many secondary indexes? | Medium | Lead | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-87) |
| 88 | What role does fillfactor play in update-heavy tables? | Medium | Senior Engineer | Performance | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-88) |
| 89 | How would you benchmark a configuration change without production risk? | Medium | Lead | Performance | [Performance Tuning](/postgresql-cheatsheet/03-query-performance/performance-tuning/#q-89) |
| 90 | What OS-level tuning complements PostgreSQL on Linux for OLTP? | Hard | Architect | Performance | [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/#q-90) |
| 91 | How do materialized views trade freshness for read performance? | Medium | Senior Engineer | Performance | [Materialized Views](/postgresql-cheatsheet/05-advanced-features/materialized-views/#q-91) |
| 92 | When should REFRESH MATERIALIZED VIEW CONCURRENTLY be avoided? | Medium | Lead | Performance | [Materialized Views](/postgresql-cheatsheet/05-advanced-features/materialized-views/#q-92) |
| 93 | How does jsonb_path_ops differ from default jsonb GIN ops? | Medium | Senior Engineer | Performance | [Json](/postgresql-cheatsheet/05-advanced-features/json/#q-93) |
| 94 | What is the cost of functional indexes on lower(email)? | Medium | Senior Engineer | Performance | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-94) |
| 95 | How do you capacity-plan WAL disk throughput for peak write bursts? | Hard | Architect | Performance | [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/#q-95) |
| 96 | What RPO does asynchronous streaming replication imply? | Medium | Lead | Reliability | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-96) |
| 97 | How do synchronous_commit and synchronous_standby_names combine? | Hard | Architect | Reliability | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-97) |
| 98 | What is pg_basebackup used for in HA bootstrap? | Medium | Senior Engineer | Reliability | [Backup Restore](/postgresql-cheatsheet/04-high-availability/backup-restore/#q-98) |
| 99 | When is pg_dump preferable to physical backup? | Medium | Lead | Reliability | [Backup Restore](/postgresql-cheatsheet/04-high-availability/backup-restore/#q-99) |
| 100 | How do you design a 3-2-1 backup strategy for PostgreSQL? | Medium | Architect | Reliability | [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/#q-100) |
| 101 | What is recovery_target_time in PITR restore? | Medium | Lead | Reliability | [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/#q-101) |
| 102 | How does WAL archiving enable point-in-time recovery? | Hard | Lead | Reliability | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-102) |
| 103 | What failure modes occur during promote when replicas are diverged? | Hard | Architect | Reliability | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-103) |
| 104 | How does pg_rewind help rejoin an old primary? | Hard | Lead | Reliability | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-104) |
| 105 | Why must DDL be considered in logical replication upgrades? | Hard | Architect | Reliability | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-105) |
| 106 | How do you monitor replication slot lag and WAL retention? | Medium | Lead | Reliability | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-106) |
| 107 | What is the impact of unvacuumed tables on crash recovery duration? | Medium | Senior Engineer | Reliability | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-107) |
| 108 | How does freeze protect against transaction ID wraparound? | Hard | Lead | Reliability | [Vacuum](/postgresql-cheatsheet/06-production-operations/vacuum/#q-108) |
| 109 | What cloud-managed HA features replace self-managed Patroni? | Medium | Architect | Reliability | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-109) |
| 110 | How do you test failover without customer-visible downtime? | Hard | Architect | Reliability | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-110) |
| 111 | What data corruption detection exists in PostgreSQL at rest? | Hard | Architect | Reliability | [Storage Engine](/postgresql-cheatsheet/02-core-postgresql/storage-engine/#q-111) |
| 112 | How does SERIALIZABLE isolation protect financial invariants? | Hard | Lead | Reliability | [Isolation Levels](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/#q-112) |
| 113 | What is the durability guarantee with synchronous_commit=off? | Medium | Senior Engineer | Reliability | [Wal](/postgresql-cheatsheet/02-core-postgresql/wal/#q-113) |
| 114 | How do you validate RTO with scheduled restore drills? | Medium | Lead | Reliability | [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/#q-114) |
| 115 | When does logical replication lag during large bulk loads? | Medium | Lead | Reliability | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-115) |
| 116 | How does pg_hba.conf control authentication methods by network? | Medium | Lead | Security | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-116) |
| 117 | Why prefer scram-sha-256 over md5 password authentication? | Easy | Senior Engineer | Security | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-117) |
| 118 | What risks does SECURITY DEFINER without locked search_path create? | Hard | Architect | Security | [Functions](/postgresql-cheatsheet/05-advanced-features/functions/#q-118) |
| 119 | How do row-level security policies complement GRANT? | Hard | Architect | Security | [Views](/postgresql-cheatsheet/05-advanced-features/views/#q-119) |
| 120 | How should application roles be scoped for least privilege? | Medium | Lead | Security | [Ddl](/postgresql-cheatsheet/01-fundamentals/ddl/#q-120) |
| 121 | What audit options exist for DDL and DML in regulated environments? | Medium | Architect | Security | [Triggers](/postgresql-cheatsheet/05-advanced-features/triggers/#q-121) |
| 122 | How do you rotate database credentials without downtime in pooled apps? | Hard | Lead | Security | [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-122) |
| 123 | What TLS settings are required for compliance-grade encryption in transit? | Medium | Architect | Security | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-123) |
| 124 | How does logical replication handle PII table subsets securely? | Hard | Architect | Security | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-124) |
| 125 | What extensions support column-level encryption tradeoffs? | Hard | Architect | Security | [Json](/postgresql-cheatsheet/05-advanced-features/json/#q-125) |
| 126 | How do you prevent SQL injection with parameterized queries in ORMs? | Easy | Senior Engineer | Security | [Dml](/postgresql-cheatsheet/01-fundamentals/dml/#q-126) |
| 127 | What network segmentation pattern isolates PostgreSQL in Kubernetes? | Hard | Architect | Security | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-127) |
| 128 | How are superuser capabilities restricted in production roles? | Medium | Lead | Security | [Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/#q-128) |
| 129 | What compliance considerations apply to cross-region replication of EU data? | Hard | Architect | Security | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-129) |
| 130 | How do you secure pg_stat_statements from exposing sensitive query text? | Medium | Lead | Security | [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/#q-130) |
| 131 | When would you choose PostgreSQL over MySQL for a new OLTP platform? | Medium | Architect | Architecture | [Postgresql Vs Mysql](/postgresql-cheatsheet/07-comparisons/postgresql-vs-mysql/#q-131) |
| 132 | What Oracle features lack direct PostgreSQL equivalents in migration? | Hard | Architect | Architecture | [Postgresql Vs Oracle](/postgresql-cheatsheet/07-comparisons/postgresql-vs-oracle/#q-132) |
| 133 | How does PostgreSQL jsonb compare to MongoDB document storage for transactional apps? | Hard | Architect | Architecture | [Postgresql Vs Mongodb](/postgresql-cheatsheet/07-comparisons/postgresql-vs-mongodb/#q-133) |
| 134 | What workload signals push you toward sharding versus bigger vertical hardware? | Hard | Architect | Architecture | [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/#q-134) |
| 135 | How would you blueprint HA for a payment ledger with strict consistency? | Hard | Architect | Architecture | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-135) |
| 136 | What ADR criteria from the database handbook justify PostgreSQL selection? | Medium | Architect | Architecture | [Database Handbook](/database-handbook/postgresql/#q-136) |
| 137 | How do you migrate from Oracle PL/SQL to PostgreSQL with minimal risk? | Hard | Architect | Architecture | [Postgresql Vs Oracle](/postgresql-cheatsheet/07-comparisons/postgresql-vs-oracle/#q-137) |
| 138 | When is foreign data wrapper federation acceptable versus ETL? | Medium | Lead | Architecture | [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/#q-138) |
| 139 | How does Citus colocation affect multi-tenant schema design? | Hard | Architect | Architecture | [Sharding](/postgresql-cheatsheet/03-query-performance/sharding/#q-139) |
| 140 | What monitoring SLOs define PostgreSQL platform health? | Medium | Lead | Architecture | [Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/#q-140) |
| 141 | How do you design schema migrations for zero-downtime deploys? | Hard | Architect | Architecture | [Ddl](/postgresql-cheatsheet/01-fundamentals/ddl/#q-141) |
| 142 | What is the role of extensions like PostGIS or pgvector in platform architecture? | Medium | Architect | Architecture | [Indexes](/postgresql-cheatsheet/03-query-performance/indexes/#q-142) |
| 143 | How would you evaluate managed RDS/Aurora versus self-hosted Patroni? | Hard | Architect | Architecture | [Failover](/postgresql-cheatsheet/04-high-availability/failover/#q-143) |
| 144 | What connection storm patterns appear during Kubernetes pod scale events? | Medium | Lead | Architecture | [Connection Pooling](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-144) |
| 145 | How do read replicas affect consistency for reporting dashboards? | Medium | Lead | Architecture | [Replication](/postgresql-cheatsheet/04-high-availability/replication/#q-145) |
| 146 | What capacity triggers prompt adding a new replica versus partition pruning tuning? | Hard | Architect | Architecture | [Capacity Planning](/postgresql-cheatsheet/06-production-operations/capacity-planning/#q-146) |
| 147 | How do stored procedures versus application transactions affect deploy agility? | Medium | Lead | Architecture | [Stored Procedures](/postgresql-cheatsheet/05-advanced-features/stored-procedures/#q-147) |
| 148 | When should business logic live in triggers versus application services? | Medium | Lead | Architecture | [Triggers](/postgresql-cheatsheet/05-advanced-features/triggers/#q-148) |
| 149 | How do you document PostgreSQL platform standards for 50+ microservices? | Hard | Architect | Architecture | [postgresql-architect-path](/postgresql-cheatsheet/09-learning-paths/postgresql-architect-path/) |
| 150 | What interview signals separate senior engineers from architects on PostgreSQL panels? | Medium | Architect | Architecture | [architect-questions](/postgresql-cheatsheet/08-interview-guide/architect-questions/) |
