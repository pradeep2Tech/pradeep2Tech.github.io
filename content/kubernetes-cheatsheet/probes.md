---
title: "Probes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Liveness, readiness, and startup probes — HTTP, TCP, exec."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Probes"
module: 5
moduleTitle: "Operations & Security"
sectionRef: "5.2"
ShowToc: true
---

## Executive Summary

**livenessProbe** restarts unhealthy containers. **readinessProbe** removes pod from Service endpoints. **startupProbe** protects slow-starting apps from premature liveness kills.

---

## Commands

### kubectl describe pod (probe failures)

**Purpose:** See probe failure messages and restart counts.

**Syntax:**
```bash
kubectl describe pod NAME -n NS
```

**Example:**
```bash
kubectl describe pod api-0 -n myapp
```

**Output:**
```
Warning  Unhealthy  Liveness probe failed: HTTP probe failed with statuscode: 503
```

**Common mistakes:**
- Liveness too aggressive kills app during GC spikes
- Readiness failure during rollout removes capacity — expected briefly

### kubectl logs (after restart)

**Purpose:** Correlate probe kills with application errors.

**Syntax:**
```bash
kubectl logs POD -n NS --previous
```

**Example:**
```bash
kubectl logs api-0 -n myapp --previous
```

**Output:**
```
OOMKilled or stack trace...
```

**Common mistakes:**
- `--previous` empty if pod never started successfully
- Exec probe shell must exist in image — alpine lacks bash

---

## YAML Snippet

### HTTP readiness + liveness

**Purpose:** Standard Spring Boot / HTTP service probes.

**Syntax:**
```yaml
readinessProbe:\n  httpGet:\n    path: /actuator/health/readiness\n    port: 8080\n  initialDelaySeconds: 10\n  periodSeconds: 5\nlivenessProbe:\n  httpGet:\n    path: /actuator/health/liveness\n    port: 8080\n  initialDelaySeconds: 30
```

**Example:**
```yaml
startupProbe:\n  httpGet:\n    path: /actuator/health\n    port: 8080\n  failureThreshold: 30\n  periodSeconds: 10
```

**Common mistakes:**
- Same path for liveness and readiness causes traffic to unhealthy instances
- initialDelaySeconds deprecated pattern — prefer startupProbe

---

## Related Topics

- [Deployments](/kubernetes-cheatsheet/deployments/) · [Troubleshooting](/kubernetes-cheatsheet/troubleshooting/)
