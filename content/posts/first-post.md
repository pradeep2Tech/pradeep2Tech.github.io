---
title: "First Post"
date: 2026-02-25T10:00:00+00:00
draft: false
description: "A sample post with table, Go code, and Mermaid flowchart."
tags: ["hugo", "papermod", "github-pages"]
---

Welcome to my Hugo blog powered by PaperMod.

## Sample Markdown Table

| Feature        | Status | Notes                          |
|----------------|--------|--------------------------------|
| Hugo Setup     | Done   | Base config is in `hugo.toml` |
| PaperMod Theme | Done   | Clean and minimal              |
| GitHub Pages   | Done   | Automated via GitHub Actions   |

## Sample Go Code

```go
package main

import "fmt"

func main() {
    name := "Hugo"
    fmt.Printf("Hello, %s blog!\n", name)
}
```

## Mermaid Flowchart

```mermaid
flowchart TD
  A[Write post in Markdown] --> B[Hugo builds static site]
  B --> C[GitHub Actions deploys]
  C --> D[Live on GitHub Pages]
```
