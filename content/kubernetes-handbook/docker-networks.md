---
title: "Docker Networks"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Bridge, host, overlay, and container DNS."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Networks"
module: 7
moduleTitle: "Docker Deep Dive"
sectionRef: "7.5"
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/docker-networks/"]
---

## Executive Summary

Default **bridge** network isolates containers on host. **user-defined bridge** adds DNS by container name. **overlay** for swarm multi-host.

---

## Commands

### docker network create

**Purpose:** Create custom bridge network.

**Syntax:**
```bash
docker network create NAME
```

**Example:**
```bash
docker network create app-net
```

**Output:**
```
app-net
```

**Common mistakes:**
- Containers on default bridge cannot resolve names
- Subnet overlap breaks compose stacks joining multiple networks

### docker run --network

**Purpose:** Attach container to network at start.

**Syntax:**
```bash
docker run --network NETWORK IMAGE
```

**Example:**
```bash
docker run -d --name api --network app-net myapp:1.0
```

**Output:**
```
container id...
```

**Common mistakes:**
- Cannot change network of running container without reconnect
- `host` network removes isolation on Linux

### docker network inspect

**Purpose:** See connected containers and IPAM config.

**Syntax:**
```bash
docker network inspect NETWORK
```

**Example:**
```bash
docker network inspect app-net
```

**Output:**
```
Containers: {{ "api": {{ ... }} }}
```

**Common mistakes:**
- Empty Containers means wrong network name
- iptables rules from Docker can conflict with VPN

---

## Related Topics

- [Docker Compose](/kubernetes-handbook/docker-compose/) · [Services in Kubernetes](/kubernetes-handbook/services/)
