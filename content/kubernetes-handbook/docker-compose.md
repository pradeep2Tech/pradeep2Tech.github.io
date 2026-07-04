---
title: "Docker Compose"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Multi-container local stacks — services, networks, volumes."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Compose"
module: 7
moduleTitle: "Docker Deep Dive"
sectionRef: "7.7"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/docker-compose/"]
---

## Executive Summary

**Docker Compose** defines multi-container apps in `compose.yaml` — services, networks, volumes, env, and dependencies.

---

## Commands

### docker compose up

**Purpose:** Create and start all services.

**Syntax:**
```bash
docker compose up [-d] [-f FILE]
```

**Example:**
```bash
docker compose up -d
```

**Output:**
```
Container myapp-api-1  Started
```

**Common mistakes:**
- Forgot `-d` attaches logs to terminal
- Stale orphans from renamed services — `docker compose down --remove-orphans`

### docker compose ps

**Purpose:** List compose project containers and ports.

**Syntax:**
```bash
docker compose ps
```

**Example:**
```bash
docker compose ps
```

**Output:**
```
NAME          IMAGE        STATUS    PORTS\nmyapp-api-1   myapp:1.0    running   0.0.0.0:8080->8080/tcp
```

**Common mistakes:**
- Shows only current project — set `COMPOSE_PROJECT_NAME`
- Healthcheck failing shows unhealthy status

### docker compose logs

**Purpose:** Tail logs for one or all services.

**Syntax:**
```bash
docker compose logs [-f] [SERVICE]
```

**Example:**
```bash
docker compose logs -f api
```

**Output:**
```
api-1  | Started on port 8080
```

**Common mistakes:**
- `-f` never exits — use in dev only
- Service name is compose key not container name

### docker compose down

**Purpose:** Stop and remove containers and default network.

**Syntax:**
```bash
docker compose down [-v]
```

**Example:**
```bash
docker compose down -v
```

**Output:**
```
Container myapp-api-1  Removed
```

**Common mistakes:**
- `-v` deletes named volumes — data loss
- Does not remove built images — prune separately

---

## Related Topics

- [Docker Networks](/kubernetes-handbook/docker-networks/) · [Docker Volumes](/kubernetes-handbook/docker-volumes/)
