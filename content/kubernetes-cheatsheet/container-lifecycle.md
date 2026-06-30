---
title: "Container Lifecycle"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Create, start, stop, pause, restart, and remove."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Lifecycle"
module: 6
moduleTitle: "Docker"
sectionRef: "6.9"
ShowToc: true
---

## Executive Summary

Container states: **created → running → paused/stopped → removed**. Restart policies control daemon restart behavior.

---

## Commands

### docker run

**Purpose:** Create and start container from image.

**Syntax:**
```bash
docker run [OPTIONS] IMAGE [COMMAND]
```

**Example:**
```bash
docker run -d --name api --restart unless-stopped -p 8080:8080 myapp:1.0
```

**Output:**
```
long-container-id
```

**Common mistakes:**
- Port already allocated error — pick free host port
- `--rm` auto-deletes on stop — good for CI, bad for debug

### docker stop / start

**Purpose:** Graceful SIGTERM then SIGKILL stop; start existing container.

**Syntax:**
```bash
docker stop CONTAINER [&& docker start CONTAINER]
```

**Example:**
```bash
docker stop api && docker start api
```

**Output:**
```
api\napi
```

**Common mistakes:**
- Default stop timeout 10s — apps need longer graceful shutdown
- Start fails if name conflict with new container

### docker restart

**Purpose:** Restart running or stopped container.

**Syntax:**
```bash
docker restart CONTAINER
```

**Example:**
```bash
docker restart api
```

**Output:**
```
api
```

**Common mistakes:**
- Restart does not pull new image — recreate container for upgrades
- Rapid restart loops hide application crash cause — check logs

### docker rm

**Purpose:** Remove stopped container.

**Syntax:**
```bash
docker rm [-f] CONTAINER
```

**Example:**
```bash
docker rm -f api
```

**Output:**
```
api
```

**Common mistakes:**
- `-f` kills running container — data loss in container layer
- Cannot remove running without `-f`

---

## Related Topics

- [Docker Commands](/kubernetes-cheatsheet/docker-commands/) · [Pods lifecycle](/kubernetes-cheatsheet/pods/)
