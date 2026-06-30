---
title: "Docker Commands"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Essential docker CLI for images, containers, and registry."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Docker CLI"
module: 6
moduleTitle: "Docker"
sectionRef: "6.8"
ShowToc: true
---

## Executive Summary

Essential **docker** CLI — images, containers, registry, and cleanup.

---

## Commands

### docker images

**Purpose:** List local images with tags and sizes.

**Syntax:**
```bash
docker images [REPO]
```

**Example:**
```bash
docker images myapp
```

**Output:**
```
REPOSITORY   TAG    IMAGE ID       SIZE\nmyapp        1.0    abc123def456   220MB
```

**Common mistakes:**
- Dangling `<none>` tags from rebuild — filter or prune
- IMAGE ID enough for local ops — prefer name:tag in scripts

### docker ps

**Purpose:** List running containers.

**Syntax:**
```bash
docker ps [-a] [--filter label=...]
```

**Example:**
```bash
docker ps -a --filter name=api
```

**Output:**
```
CONTAINER ID   IMAGE     STATUS\nabc123         myapp:1.0 Exited (1) 2h ago
```

**Common mistakes:**
- Exited containers still hold writable layer — `docker rm`
- Name filter is substring — can match multiple

### docker tag / push

**Purpose:** Tag image for registry and upload.

**Syntax:**
```bash
docker tag SRC:TAG REGISTRY/REPO:TAG && docker push REGISTRY/REPO:TAG
```

**Example:**
```bash
docker tag myapp:1.0 registry.example.com/myapp:1.0 && docker push registry.example.com/myapp:1.0
```

**Output:**
```
1.0: digest: sha256:... size: ...
```

**Common mistakes:**
- Push wrong arch image to multi-arch repo breaks pulls
- Must docker login to private registry first

### docker exec

**Purpose:** Run command in running container.

**Syntax:**
```bash
docker exec [-it] CONTAINER COMMAND
```

**Example:**
```bash
docker exec -it api sh
```

**Output:**
```
# shell prompt
```

**Common mistakes:**
- `-it` needs TTY — fails in some CI environments
- Changes in exec session not in image — rebuild to persist

### docker system prune

**Purpose:** Remove unused data.

**Syntax:**
```bash
docker system prune [-a] [-f] [--volumes]
```

**Example:**
```bash
docker system prune -af
```

**Output:**
```
Total reclaimed space: 2.5GB
```

**Common mistakes:**
- `-a` removes all unused images — aggressive on dev machine
- `--volumes` deletes unused volumes — irreversible

---

## Related Topics

- [Container Lifecycle](/kubernetes-cheatsheet/container-lifecycle/) · [Docker Best Practices](/kubernetes-cheatsheet/docker-best-practices/)
