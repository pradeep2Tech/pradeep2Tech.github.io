---
title: "ClassLoader Internals"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Bootstrap, platform, application loaders, delegation model."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "ClassLoaders"
module: 4
moduleTitle: "JVM"
sectionRef: "4.3"
ShowToc: true
interviewHandbook: true
---

## Class loader delegation — why parent-first?

### Short Answer

Security and single definition — core classes cannot be spoofed by child loaders.

### Detailed Explanation

Bootstrap loads `java.*`. Application loader loads classpath/module path. Child delegates to parent before loading itself.

### Follow-up Questions

- How break delegation (OSGi, Tomcat)?

---
