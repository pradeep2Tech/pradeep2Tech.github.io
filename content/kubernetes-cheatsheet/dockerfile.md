---
title: "Dockerfile"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "FROM, COPY, RUN, CMD, ENTRYPOINT, and layer caching."
tags: ["kubernetes-cheatsheet", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Cheatsheet"]
shortTitle: "Dockerfile"
module: 6
moduleTitle: "Docker"
sectionRef: "6.2"
ShowToc: true
---

## Executive Summary

**Dockerfile** instructions build images layer by layer. Order matters for cache: pin bases, copy dependency files before source, combine RUN where sensible.

---

## Commands

### docker build

**Purpose:** Build image from Dockerfile in context directory.

**Syntax:**
```bash
docker build -t NAME:TAG [PATH] [-f Dockerfile]
```

**Example:**
```bash
docker build -t myapp:1.0.0 .
```

**Output:**
```
Successfully tagged myapp:1.0.0
```

**Common mistakes:**
- Large build context slows build — use `.dockerignore`
- `-f` wrong path builds unexpected recipe

### docker build --no-cache

**Purpose:** Force full rebuild ignoring layer cache.

**Syntax:**
```bash
docker build --no-cache -t NAME:TAG .
```

**Example:**
```bash
docker build --no-cache -t myapp:1.0.0 .
```

**Output:**
```
Successfully tagged myapp:1.0.0
```

**Common mistakes:**
- Slower but needed when base image security patch must apply
- CI should periodically use no-cache for supply chain hygiene

### docker history

**Purpose:** Show Dockerfile layer commands and sizes.

**Syntax:**
```bash
docker history IMAGE
```

**Example:**
```bash
docker history myapp:1.0.0
```

**Output:**
```
IMAGE       CREATED        SIZE\n<missing>   2 minutes ago   120MB
```

**Common mistakes:**
- `<missing>` layers from squashed or pulled images
- Large RUN layers — refactor Dockerfile

---

## Dockerfile Snippet

```dockerfile
FROM eclipse-temurin:21-jre-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app
COPY target/app.jar app.jar
USER app
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## Related Topics

- [Multi-stage Builds](/kubernetes-cheatsheet/multi-stage-builds/) · [Image Layers](/kubernetes-cheatsheet/image-layers/) · [Docker Best Practices](/kubernetes-cheatsheet/docker-best-practices/)
