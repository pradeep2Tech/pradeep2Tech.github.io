---
title: "Serialization Interview Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Serializable contract, serialVersionUID, safer alternatives."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Serialization"
module: 5
moduleTitle: "Platform APIs"
sectionRef: "5.2"
ShowToc: true
interviewHandbook: true
aliases:
  - serialization-quick-ref
---

## Why avoid Java serialization in new systems?

### Short Answer

Security (gadget chains), brittleness across versions, poor cross-language support.

### Detailed Explanation

Prefer JSON, Protobuf, Avro. If required: `serialVersionUID`, whitelist ObjectInputFilter (9+).

### Follow-up Questions

- Externalizable vs Serializable?

---
