---
title: "Docker Volumes"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Named volumes, bind mounts, and tmpfs for persistence."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Volumes"
module: 7
moduleTitle: "Docker Deep Dive"
sectionRef: "7.4"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/docker-volumes/"]
---

## Executive Summary

**Volumes** persist data outside container lifecycle. Prefer **named volumes** over anonymous; **bind mounts** for dev hot-reload.

---

## Commands

### docker volume create

**Purpose:** Create a named volume.

**Syntax:**
```bash
docker volume create NAME
```

**Example:**
```bash
docker volume create pgdata
```

**Output:**
```
pgdata
```

**Common mistakes:**
- Volume names global on host — coordinate in Compose
- Wrong driver for swarm vs local

### docker run -v

**Purpose:** Mount volume or bind path into container.

**Syntax:**
```bash
docker run -v VOLUME_OR_PATH:CONTAINER_PATH IMAGE
```

**Example:**
```bash
docker run -d -v pgdata:/var/lib/postgresql/data postgres:16
```

**Output:**
```
container id...
```

**Common mistakes:**
- Bind mount `:Z` SELinux label needed on RHEL/Fedora
- Windows path syntax differs for bind mounts

### docker volume ls / inspect

**Purpose:** List volumes and find mountpoint on host.

**Syntax:**
```bash
docker volume inspect NAME
```

**Example:**
```bash
docker volume inspect pgdata
```

**Output:**
```
Mountpoint: /var/lib/docker/volumes/pgdata/_data
```

**Common mistakes:**
- `docker volume prune` deletes unused — data loss
- Backup requires stopping container or filesystem snapshot

---

## Related Topics

- [Docker Compose](/kubernetes-handbook/docker-compose/) · [Container Lifecycle](/kubernetes-handbook/container-lifecycle/)
