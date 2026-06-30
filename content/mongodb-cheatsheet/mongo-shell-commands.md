---
title: "Mongo Shell Commands"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "mongosh cheat sheet — connection, CRUD, admin, replica set, sharding, and diagnostic commands."
tags: ["mongodb-cheatsheet", "mongodb", "cheatsheet", "handbook"]
categories: ["MongoDB Cheatsheet"]
shortTitle: "Shell"
module: 4
moduleTitle: "Design, Ops & Reference"
sectionRef: "4.4"
ShowToc: true
---

## Executive Summary

**mongosh** is the modern MongoDB shell (replaces legacy `mongo`). It supports JavaScript, autocomplete, and improved output formatting. Use `help` and `db.help()` for context-sensitive docs.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `mongosh <uri>` | Connect to deployment |
| `show dbs` / `use db` | Database navigation |
| `show collections` | List collections |
| `db.<coll>.<method>()` | Collection API |
| `rs.*` / `sh.*` | Replica set / sharding helpers |

---

## Quick Reference — Connection

```bash
mongosh "mongodb://localhost:27017/mydb"
mongosh "mongodb+srv://cluster.mongodb.net/mydb" --username app
mongosh --host mongo1 --port 27017 --tls --tlsCAFile ca.pem
```

```javascript
// Shell helpers
help
db.help()
db.orders.help()
show profile
exit
```

---

## Quick Reference — CRUD

```javascript
db.orders.insertOne({ orderId: "O1" })
db.orders.insertMany([{ orderId: "O2" }, { orderId: "O3" }])
db.orders.find({ status: "open" }).limit(10)
db.orders.findOne({ orderId: "O1" })
db.orders.updateOne({ orderId: "O1" }, { $set: { status: "paid" } })
db.orders.updateMany({ status: "draft" }, { $set: { status: "cancelled" } })
db.orders.replaceOne({ orderId: "O1" }, { orderId: "O1", status: "new" })
db.orders.deleteOne({ orderId: "O1" })
db.orders.deleteMany({ status: "cancelled" })
db.orders.countDocuments({ status: "open" })
```

---

## Quick Reference — Admin & Diagnostics

```javascript
db.serverStatus()
db.stats()
db.orders.stats()
db.orders.validate({ full: true })
db.getCollectionNames()
db.runCommand({ connectionStatus: 1 })
db.adminCommand({ listDatabases: 1 })

// Build info & logs
db.version()
db.adminCommand({ getLog: "global" })

// Kill long operation
db.killOp(<opid>)
```

---

## Quick Reference — Replica Set & Sharding

```javascript
rs.status()
rs.conf()
rs.initiate()
rs.add("host:27017")
rs.stepDown()

sh.status()
sh.enableSharding("mydb")
sh.shardCollection("mydb.orders", { customerId: 1 })
sh.balancerCollectionStatus("mydb.orders")
```

---

## Snippets

```javascript
// Load JS file
load("scripts/seed.js")

// Pretty print
db.orders.find().limit(3).pretty()

// BSON type inspection
typeof db.orders.findOne().total

// Config from shell
config = rs.conf()
config.members[0].priority = 2
rs.reconfig(config)
```

---

## Common Gotchas

- `mongosh` uses Node.js — some legacy shell syntax differs from old `mongo`.
- `db.collection.drop()` is immediate and irreversible — no undo.
- `rs.reconfig()` requires reconfig version increment — use helper or let shell handle.
- Production admin commands need appropriate RBAC roles (`clusterAdmin`, `readWrite`).

---

## Related Topics

- [Previous: Performance](/mongodb-cheatsheet/performance/)
- [Next: Interview Questions](/mongodb-cheatsheet/interview-questions/)
- [CRUD](/mongodb-cheatsheet/crud/)
- [MongoDB Cheatsheet Index](/mongodb-cheatsheet/)
