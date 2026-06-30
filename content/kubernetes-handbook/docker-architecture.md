---
title: "Docker Architecture"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Client, daemon, containerd, runc, and image registry flow."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Docker Arch"
module: 6
moduleTitle: "Docker"
sectionRef: "6.1"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/docker-architecture/"]
---

## Executive Summary

**Docker CLI** talks to **dockerd**, which uses **containerd** and **runc** to create OCI containers. Images live in registries; local storage uses layered graph drivers.

---

## Core Concepts

```mermaid
flowchart LR
  cli["docker CLI"] --> daemon["dockerd"]
  daemon --> containerd["containerd"]
  containerd --> runc["runc"]
  runc --> container["Container"]
  daemon --> registry["Registry"]
```

---

## Commands

### docker version

**Purpose:** Show client and server API versions.

**Syntax:**
```bash
docker version
```

**Example:**
```bash
docker version
```

**Output:**
```
Client: Docker Engine 26.1.0\nServer: Docker Engine 26.1.0
```

**Common mistakes:**
- Client/server version skew can cause API errors
- Server section missing means daemon not running

### docker info

**Purpose:** Display storage driver, cgroup, registry mirrors, and limits.

**Syntax:**
```bash
docker info
```

**Example:**
```bash
docker info
```

**Output:**
```
Storage Driver: overlay2\nCgroup Driver: systemd
```

**Common mistakes:**
- Root dir full causes cryptic pull/build failures
- Check `Insecure Registries` for on-prem registry config

### docker context ls

**Purpose:** List Docker contexts (local, remote, ECS).

**Syntax:**
```bash
docker context ls
```

**Example:**
```bash
docker context ls
```

**Output:**
```
NAME        DESCRIPTION\ndefault *   Current DOCKER_HOST
```

**Common mistakes:**
- Wrong context pushes images to unexpected host
- Remote context needs TLS certs configured

---

## Related Topics

- [Docker Commands](/kubernetes-handbook/docker-commands/) · [Container Lifecycle](/kubernetes-handbook/container-lifecycle/) · [Kubernetes Handbook — Docker](/kubernetes-handbook/docker/)
