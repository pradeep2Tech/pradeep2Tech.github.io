---
title: "Atlas Basics"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "MongoDB Atlas cheat sheet — clusters, connection strings, backups, VPC peering, and serverless."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Atlas"
module: 4
moduleTitle: "Design, Ops & Reference"
sectionRef: "4.2"
ShowToc: true
---

## Executive Summary

**MongoDB Atlas** is the managed cloud service — replica sets and sharded clusters with automated backups, monitoring, and global clusters. Connection uses **`mongodb+srv://`** SRV records.

---

## Core Concepts

| Tier | Use |
| :--- | :--- |
| **M10+** | Production — dedicated VMs, backup, VPC peering |
| **M0/M2/M5** | Dev/free — shared resources |
| **Serverless** | Auto-scale for variable workloads |
| **Flex** | Pay-per-operation dev tier |

| Feature | Recap |
| :--- | :--- |
| **Cloud Provider** | AWS, GCP, Azure regions |
| **Global Cluster** | Zone-aware reads/writes |
| **Atlas Search** | Lucene indexes |
| **Triggers** | Serverless functions on change streams |
| **Data Federation** | Query S3 / Atlas data together |

---

## Quick Reference

```bash
# Connection string (SRV)
mongodb+srv://<user>:<password>@cluster0.xxxxx.mongodb.net/mydb?retryWrites=true&w=majority

# Atlas CLI (install: atlas CLI)
atlas clusters list
atlas clusters describe Cluster0
atlas dbusers create --username app --password '...' --role readWrite@mydb
atlas backups snapshots list --clusterName Cluster0
```

```javascript
// Network access — IP allowlist or VPC peering / PrivateLink
// Database access — SCRAM user or X.509 / OIDC (enterprise)

// Load sample data (Atlas UI or)
mongosh "mongodb+srv://cluster..." --file sampleData.js
```

---

## Snippets

```yaml
# Spring Boot application.yml
spring:
  data:
    mongodb:
      uri: ${MONGODB_URI}  # never commit credentials
```

```javascript
// Atlas Search index definition (JSON via API/UI)
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "title": { "type": "string", "analyzer": "lucene.standard" },
      "body": { "type": "string" }
    }
  }
}
```

---

## Common Gotchas

- M0 clusters pause after inactivity — not for production cron jobs without keep-alive.
- `mongodb+srv` requires DNS SRV resolution — some corporate DNS blocks it.
- Backup PITR requires M10+ and adds storage cost.
- Cross-region clusters increase write latency — place primary near writers.

---

## Related Topics

- [Previous: Schema Design](/mongodb-cheatsheet/schema-design/)
- [Next: Performance](/mongodb-cheatsheet/performance/)
- [Text Search](/mongodb-cheatsheet/text-search/)
- [Replication](/mongodb-cheatsheet/replication/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
