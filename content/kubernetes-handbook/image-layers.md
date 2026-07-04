---
title: "Image Layers"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Union filesystem, layer caching, and image inspection."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Layers"
module: 7
moduleTitle: "Docker Deep Dive"
sectionRef: "7.3"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/image-layers/"]
---

## Executive Summary

Images are **read-only layers** stacked with copy-on-write. Reuse layers across images to save disk and speed pulls.

---

## Commands

### docker image inspect

**Purpose:** View layer IDs, env, cmd, and rootfs.

**Syntax:**
```bash
docker image inspect IMAGE [--format='{{{{json .RootFS.Layers}}}}']
```

**Example:**
```bash
docker image inspect myapp:1.0.0 --format='{{{{.Size}}}}'
```

**Output:**
```
125829120
```

**Common mistakes:**
- Format string typos return template errors
- Size is compressed transport size estimate — not exact disk

### docker system df -v

**Purpose:** Break down image, container, and volume disk usage.

**Syntax:**
```bash
docker system df -v
```

**Example:**
```bash
docker system df -v
```

**Output:**
```
Images space usage:\nREPOSITORY   TAG   SIZE
```

**Common mistakes:**
- Dangling `<none>` images accumulate from rebuilds
- Prune carefully in shared CI runners

### docker pull

**Purpose:** Download image layers from registry.

**Syntax:**
```bash
docker pull REPO:TAG
```

**Example:**
```bash
docker pull nginx:1.27-alpine
```

**Output:**
```
Status: Downloaded newer image for nginx:1.27-alpine
```

**Common mistakes:**
- Pulling `latest` is non-reproducible — pin digest in prod
- Auth failure needs `docker login` first

---

## Related Topics

- [Dockerfile](/kubernetes-handbook/dockerfile/) · [Docker Best Practices](/kubernetes-handbook/docker-best-practices/)
