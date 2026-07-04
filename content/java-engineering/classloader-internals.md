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
interviewHandbook: true
---

Class loaders define **namespace boundaries** for classes. The **parent-delegation model** prevents replacing `java.lang.String` from application code and underpins modular isolation in containers and app servers.

---

## Class loader delegation — why parent-first?

**Difficulty:** Medium · **Time:** 2 min

### Short Answer

Security and **single definition** — core JDK classes loaded once by bootstrap/platform loaders; app code cannot spoof `java.*`.

### Detailed Explanation

Default: child asks parent to load; parent tries its parent up to bootstrap. Only if parent fails does child load from its own classpath. Tomcat/OSGi use **child-first** for web apps to isolate WAR dependencies.

### Interview Questions

1. Who loads `java.lang.Object`?
2. How do you break parent delegation intentionally?
3. Module path vs classpath — which loader?

### Follow-up Questions

- How break delegation (OSGi, Tomcat)?

---
## Bootstrap vs Platform vs Application loader?

**Difficulty:** Medium · **Time:** 1–2 min

### Short Answer

**Bootstrap** (null `getClassLoader()`): `java.base` core classes. **Platform** (extension): JDK modules not in base. **Application** (system): application classpath/module path.

### Detailed Explanation

JDK 9+ module system: loaders align with module layers. `ClassLoader.getSystemClassLoader()` returns application loader in most apps.

### Interview Questions

1. Can you instantiate BootstrapClassLoader?
2. What loader loads JDBC driver from `META-INF/services`?

---
## Custom classloader use cases?

**Difficulty:** Hard · **Time:** 2 min

### Short Answer

Hot reload, plugin architectures, bytecode generation (agents), isolating conflicting dependency versions.

### Detailed Explanation

Must define `findClass` or delegate properly; leaking custom loaders retains all their classes (Metaspace leak). Always null out refs on undeploy.

### Production Notes

Prefer JPMS layers or container isolation over hand-rolled loaders unless building a plugin platform.

### Interview Questions

1. What happens if same class name loaded by two loaders?
2. How does `instanceof` interact with different loaders?

---
## ClassLoader Interview Drill

### 1. Symptom: `ClassCastException` on same class name — cause?

Same FQCN loaded by two different class loaders — types incompatible.

---

### 2. `Thread.contextClassLoader` purpose?

Frameworks set it so libraries load classes from the right module/WAR.

---
