---
title: "Java Version Migration Guide"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "LTS matrix, feature deltas, upgrade checkpoints, interview facts."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Version Migration"
module: 6
moduleTitle: "Interview Cheat Sheets"
sectionRef: "6.5"
interviewHandbook: true
cheatSheet: true
aliases:
  - java-lts-release-matrix
  - java-recent-features
  - java-version-features-interview
---


| LTS | Headline features |
| :---: | :--- |
| 8 | Lambdas, streams, `Optional`, `java.time` |
| 11 | HTTP client, removed Java EE from JDK |
| 17 | Records, sealed, pattern `instanceof` |
| 21 | Virtual threads, sequenced collections, pattern switch |
| 25 | Current LTS upgrade target |

| Migration | Action |
| :--- | :--- |
| 8 → 11 | JAXB/JAX-WS modules, `jdeps` |
| 11 → 17 | `--add-opens` audit, strong encapsulation |
| 17 → 21 | Virtual threads pilot, pinning review |

| Post-17 adopt | Defer |
| :--- | :--- |
| Records, sealed ADTs | Preview features without flag plan |
| Virtual threads for IO | Foreign API without need |

---

## Why LTS for enterprises?

**Difficulty:** Easy · **Time:** 30 sec

### Short Answer

Predictable vendor support, security patches, slower change absorption.

### Detailed Explanation

Non-LTS every 6 months — only if you own upgrade cadence.

---
