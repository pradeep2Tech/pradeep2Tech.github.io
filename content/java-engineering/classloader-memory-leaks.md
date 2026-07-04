---
title: "ClassLoader Memory Leaks"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "WAR redeploy, static refs, Metaspace OOM in containers."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "CL Leaks"
module: 4
moduleTitle: "JVM"
sectionRef: "4.4"
interviewHandbook: true
---

## Why classloader leaks on WAR redeploy?

**Difficulty:** Hard · **Time:** 2 min

### Short Answer

Old classloader retained by static refs, ThreadLocal values, or lingering threads — classes not unloaded, Metaspace grows.

### Detailed Explanation

Fix: undeploy hooks, remove listeners, clear ThreadLocals, avoid static collections holding app classes.

### Production Notes

Monitor Metaspace in dynamic scripting (Groovy, JSR223).

---
