---
title: "How to Choose a Database"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Decision framework for relational, document, wide-column, graph, and specialized stores."
tags: ["technology-playbook", "decision", "database", "architecture"]
categories: ["Technology Playbook"]
shortTitle: "Choose Database"
module: 2
moduleTitle: "Technology Decision Matrix"
sectionRef: "2.1"
weight: 201
---

## 1. Executive Summary

Database selection is not "PostgreSQL vs MongoDB on Twitter." It starts with **access patterns**, **consistency requirements**, **scale trajectory**, and **operational capacity**. This page gives a repeatable checklist architects use in ADRs, RFPs, and interviews — then maps patterns to store **classes** (relational, document, wide-column, key-value, graph, time-series, search, analytics, vector).

---

## 2. What Problem It Solves

| Without a framework | With a framework |
| :--- | :--- |
| Brand-driven choices (Oracle because enterprise) | Workload-driven shortlist |
| OLTP store abused for BI | Clear OLTP vs warehouse split |
| Surprise scale limits at launch | Partition/shard plan upfront |
| Team cannot operate chosen DB | Managed service vs self-hosted fit |

---

## 3. Where It Fits in Architecture

```mermaid
flowchart TD
  req[Business Requirements] --> patterns[Access Patterns & SLAs]
  patterns --> classify{Store Class}
  classify --> rdbms[Relational OLTP]
  classify --> doc[Document]
  classify --> wide[Wide Column]
  classify --> kv[Key-Value / Cache]
  classify --> graph[Graph]
  classify --> ts[Time Series]
  classify --> search[Search Index]
  classify --> olap[Analytics Warehouse]
  classify --> vec[Vector Store]
  rdbms --> poc[POC + Load Test]
  doc --> poc
  wide --> poc
  kv --> poc
  graph --> poc
  ts --> poc
  search --> poc
  olap --> poc
  vec --> poc
  poc --> adr[Architecture Decision Record]
```

---

## 4. When to Choose — Decision Checklist

{{< decision-card title="Step 1 — Classify the workload" >}}
1. **Transactional OLTP** — ACID, JOINs, reporting on normalized model → **Relational** (PostgreSQL, MySQL, Oracle, SQL Server)
2. **Flexible product schema** — nested JSON, rapid iteration → **Document** (MongoDB, Couchbase, Cosmos DB)
3. **Write-heavy, massive scale** — time-series IoT, global write path → **Wide column** (Cassandra, ScyllaDB)
4. **Sub-ms key lookups** — session, cache, rate limit counters → **Key-value** (Redis, DynamoDB)
5. **Relationship traversal** — fraud rings, dependencies → **Graph** (Neo4j, Neptune)
6. **Metrics & telemetry** → **Time series** (InfluxDB, TimescaleDB)
7. **Full-text & faceted search** → **Search** (Elasticsearch, OpenSearch, Solr)
8. **Petabyte analytics** → **Warehouse / OLAP** (Snowflake, BigQuery, ClickHouse)
9. **Semantic / RAG retrieval** → **Vector** (pgvector, Milvus, Pinecone, Weaviate)
{{< /decision-card >}}

{{< decision-card title="Step 2 — Non-functional filters" >}}
- **Consistency:** strong vs eventual — does stale read cost money?
- **Latency p99:** single-digit ms vs seconds acceptable?
- **Ops model:** managed cloud vs self-hosted on Kubernetes?
- **Compliance:** region residency, encryption, audit trail
- **Team skills:** what can you run at 3 a.m. during an incident?
{{< /decision-card >}}

---

## 5. When Not to Choose — Anti-patterns

| Anti-pattern | Why it fails |
| :--- | :--- |
| One database for everything | Wrong tool → performance cliffs and ops pain |
| MongoDB for heavy multi-table reporting | JOINs and aggregations become application code |
| Cassandra for low-volume CRUD | Ops overhead without scale benefit |
| Elasticsearch as system of record | Not a transactional primary store |
| Vector DB without hybrid strategy | Relational metadata + vectors often belong together (pgvector) |

---

## 6. Popular Tools / Products by Class

| Class | Primary options | Cloud managed examples |
| :--- | :--- | :--- |
| **Relational** | [PostgreSQL](/database-handbook/postgresql/), [MySQL](/database-handbook/mysql/), [Oracle](/database-handbook/oracle/), [SQL Server](/database-handbook/sql-server/) | RDS, Aurora, Azure SQL, Cloud SQL |
| **Document** | [MongoDB](/database-handbook/mongodb/), [Couchbase](/database-handbook/couchbase/), [Cosmos DB](/database-handbook/cosmos-db/) | Atlas, Cosmos DB |
| **Wide column** | [Cassandra](/database-handbook/cassandra/), [ScyllaDB](/database-handbook/scylladb/) | Keyspaces, self-hosted operators |
| **Key-value** | [Redis](/database-handbook/redis/), [DynamoDB](/database-handbook/dynamodb/) | ElastiCache, DynamoDB |
| **Graph** | [Neo4j](/database-handbook/neo4j/), [Neptune](/database-handbook/amazon-neptune/) | Neptune, Aura |
| **Search** | [Elasticsearch](/database-handbook/elasticsearch/), [OpenSearch](/database-handbook/opensearch/) | OpenSearch Service |
| **Analytics** | [Snowflake](/database-handbook/snowflake/), [BigQuery](/database-handbook/bigquery/), [ClickHouse](/database-handbook/clickhouse/) | Native cloud warehouses |
| **Vector** | [pgvector](/ai-for-engineers/pgvector/), [Milvus](/ai-for-engineers/milvus/), [Pinecone](/ai-for-engineers/pinecone/) | Managed vector services |

---

## 7. Trade-offs

{{< comparison-table caption="Store class selection matrix" >}}
| If you need… | Prefer | Avoid as primary |
| :--- | :--- | :--- |
| ACID ledger & JOINs | Relational | Document without schema discipline |
| Flexible catalog schema | Document | Wide column for small datasets |
| Global write scale | Wide column | Single-node relational |
| Session / hot cache | Redis / key-value | Relational row per session at scale |
| Full-text product search | OpenSearch / Elasticsearch | LIKE queries on OLTP |
| Executive dashboards | Warehouse / OLAP | OLTP replicas without guardrails |
| RAG similarity search | Vector + metadata store | Brute-force embedding scan in app memory |
{{< /comparison-table >}}

---

## 8. Real-World Example

**BFSI payments platform**

| Data | Store | Reason |
| :--- | :--- | :--- |
| Ledger & balances | PostgreSQL / Oracle | ACID, audit, regulatory familiarity |
| Idempotency keys & rate limits | Redis | TTL, fast dedup |
| `PaymentCompleted` events | Kafka + warehouse | Streaming + Snowflake reporting |
| Customer support search | OpenSearch | Fuzzy match on tickets + accounts |
| Fraud graph analysis | Neo4j | Ring detection traversals |

**Inventory ERP:** Oracle or SQL Server core + Redis cache for store availability + nightly ETL to BigQuery for supply-chain BI.

---

## 9. Failure Scenarios

- **Connection storm** during deploy — pool sizing and RDS Proxy
- **Replica lag** — users see stale account balance
- **Missing index** on OLTP — p99 latency destroys checkout
- **Dual-write** between DB and search — use CDC/outbox instead

See [Transactional Outbox](/database-handbook/transactional-outbox-pattern/) for reliable sync patterns.

---

## 10. Best Practices

1. Separate **OLTP**, **cache**, **search**, and **warehouse** — sync via CDC/outbox.
2. Shortlist **two** candidates; run identical POC queries at 2× expected QPS.
3. Document **RPO/RTO** and test restore quarterly in regulated domains.
4. Prefer **PostgreSQL + extensions** (pgvector, Timescale) when one ops team owns the data plane.
5. Write an **ADR** with rejected alternatives — interviews and audits both ask "why not X?"

---

## 11. Interview Answer

{{< interview-answer >}}
"I start with access patterns: read/write ratio, consistency, latency, and scale in 12 months. I map to store class — relational for ACID ledgers, document for flexible catalogs, wide column for write-heavy global scale, Redis for hot keys, search engine for full-text, warehouse for BI. I factor ops — managed vs self-hosted — and compliance. I rarely pick one database for everything; I design OLTP plus cache plus search plus analytics with CDC between them."
{{< /interview-answer >}}

---

## 12. Related Topics

- [Databases module](/technology-playbook/module-databases/) — product-specific pages
- [MongoDB vs PostgreSQL](/database-handbook/mongodb-vs-postgresql/) · [Oracle vs PostgreSQL](/database-handbook/oracle-vs-postgresql/)
- [How to Choose a Cache](/technology-playbook/how-to-choose-cache/)
- [Database Internals](/database-handbook/) — MVCC, indexing, outbox patterns
