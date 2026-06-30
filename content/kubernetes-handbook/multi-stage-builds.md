---
title: "Multi-stage Builds"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Separate build and runtime stages for smaller images."
tags: ["kubernetes-handbook", "kubernetes", "docker", "cheatsheet", "handbook"]
categories: ["Kubernetes Handbook"]
shortTitle: "Multi-stage"
module: 6
moduleTitle: "Docker"
sectionRef: "6.6"
ShowToc: true
cheatSheet: true
aliases: ["/kubernetes-cheatsheet/multi-stage-builds/"]
---

## Executive Summary

**Multi-stage builds** use multiple `FROM` stages — compile in SDK image, copy artifacts into minimal runtime image.

---

## Commands

### docker build --target

**Purpose:** Build only up to named stage.

**Syntax:**
```bash
docker build --target STAGE -t TAG .
```

**Example:**
```bash
docker build --target runtime -t myapp:prod .
```

**Output:**
```
Successfully tagged myapp:prod
```

**Common mistakes:**
- Wrong target name fails at end of Dockerfile
- Dev stage may lack files copied only in later stage

### docker build (multi-stage)

**Purpose:** Full multi-stage build producing small runtime image.

**Syntax:**
```bash
docker build -t NAME:TAG .
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
- COPY --from= wrong stage name breaks build
- Build tools in final stage bloat image and attack surface

---

## Dockerfile Snippet

```dockerfile
FROM eclipse-temurin:21-jdk-alpine AS build
WORKDIR /app
COPY . .
RUN ./mvnw -q -DskipTests package

FROM eclipse-temurin:21-jre-alpine AS runtime
COPY --from=build /app/target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## Related Topics

- [Dockerfile](/kubernetes-handbook/dockerfile/) · [Docker Best Practices](/kubernetes-handbook/docker-best-practices/)
