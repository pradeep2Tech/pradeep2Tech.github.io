---
title: "Docker Best Practices"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Non-root users, slim bases, .dockerignore, and scanning."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Docker Prod"
module: 6
moduleTitle: "Docker"
sectionRef: "6.10"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/docker-best-practices/"]
---

## Executive Summary

Run as **non-root**, use **minimal base images**, pin **digests**, scan in CI, keep secrets out of layers, and set **healthcheck** / **resource limits** in orchestrators.

---

## Commands

### docker scout cve / scan (or trivy)

**Purpose:** Scan image for known vulnerabilities.

**Syntax:**
```bash
docker scout cve IMAGE  # or: trivy image IMAGE
```

**Example:**
```bash
docker scout cve myapp:1.0
```

**Output:**
```
TARGET myapp:1.0\n  CRITICAL  0\n  HIGH      2
```

**Common mistakes:**
- Base image choice drives CVE count — alpine vs distroless tradeoffs
- Scan in CI gate — not only before prod deploy

### docker build with USER

**Purpose:** Verify container runs non-root.

**Syntax:**
```bash
docker run --rm IMAGE id
```

**Example:**
```bash
docker run --rm myapp:1.0 id
```

**Output:**
```
uid=1000(app) gid=1000(app)
```

**Common mistakes:**
- Bind ports <1024 need root or CAP_NET_BIND_SERVICE
- Volume mount permissions must match USER

### docker inspect Health

**Purpose:** Check Dockerfile HEALTHCHECK status.

**Syntax:**
```bash
docker inspect --format='{{{{.State.Health.Status}}}}' CONTAINER
```

**Example:**
```bash
docker inspect --format='{{{{.State.Health.Status}}}}' api
```

**Output:**
```
healthy
```

**Common mistakes:**
- Missing HEALTHCHECK means orchestrator must define probes
- Unhealthy container still running — depends on restart policy

---

## Related Topics

- [Multi-stage Builds](/kubernetes-handbook/multi-stage-builds/) · [Production Best Practices](/kubernetes-handbook/production-best-practices/) · [Microservices — Application Containerization](/microservices/application-containerization-docker/)
