---
title: "Rolling Updates"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "maxSurge, maxUnavailable, and deployment strategy."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Rolling Updates"
module: 6
moduleTitle: "Operations & Security"
sectionRef: "6.1"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/rolling-updates/"]
---

## Executive Summary

Deployment **strategy** controls rollout: `RollingUpdate` with `maxSurge` and `maxUnavailable`, or `Recreate` for single-replica stateful behavior.

---

## Commands

### kubectl set image (trigger rollout)

**Purpose:** Change image to start a rolling update.

**Syntax:**
```bash
kubectl set image deployment/NAME CONTAINER=IMAGE -n NS
```

**Example:**
```bash
kubectl set image deployment/myapp api=myapp:2.1.0 -n myapp
```

**Output:**
```
deployment.apps/myapp image updated
```

**Common mistakes:**
- maxUnavailable 0 with maxSurge 1 is safest but slower
- Readiness probe must pass before old pods terminate

### kubectl rollout pause / resume

**Purpose:** Pause rollout to batch changes or verify canary.

**Syntax:**
```bash
kubectl rollout pause deployment/NAME -n NS
```

**Example:**
```bash
kubectl rollout pause deployment/myapp -n myapp
```

**Output:**
```
deployment.apps/myapp paused
```

**Common mistakes:**
- Forgotten pause leaves rollout stuck — document runbooks
- Resume continues from current revision

### kubectl rollout status

**Purpose:** Block until rollout completes or fails.

**Syntax:**
```bash
kubectl rollout status deployment/NAME -n NS --timeout=5m
```

**Example:**
```bash
kubectl rollout status deployment/myapp -n myapp --timeout=5m
```

**Output:**
```
Waiting for deployment "myapp" rollout to finish: 2 of 3 updated replicas are available...
```

**Common mistakes:**
- Timeout in CI should fail pipeline
- Progress deadline exceeded — check `kubectl describe deploy`

---

## Related Topics

- [Deployments](/kubernetes-handbook/deployments/) · [Probes](/kubernetes-handbook/probes/)
