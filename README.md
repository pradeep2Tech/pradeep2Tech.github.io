# Pradeep CS — Engineering Notes

Enterprise Knowledge Hub: system design, microservices, domain handbooks, design patterns, DSA, and interview prep. Built with [Hugo](https://gohugo.io/) + PaperMod theme.

## Local Preview

```bash
hugo server -D
```

## AI / Contributor Index

Before editing or searching the codebase, read:

- **[AGENTS.md](AGENTS.md)** — routing table for common tasks
- **[docs/ai-index/SECTION-REGISTRY.md](docs/ai-index/SECTION-REGISTRY.md)** — all 20 curriculum sections
- **[docs/ai-index/ARCHITECTURE.md](docs/ai-index/ARCHITECTURE.md)** — layouts, shortcodes, navigation

Regenerate section registry after structural changes:

```bash
python scripts/generate_ai_index.py
```

## Curriculum Sections

Registered in `data/curriculum_sections.yaml`:

| Group | Sections |
|-------|----------|
| Design | System Design, Microservices, Technology Decisions |
| Handbooks | Java, Spring Boot, Python, Go, Kafka, Kubernetes, Redis, Database, PostgreSQL, MongoDB, Cloud |
| Practice | Design Patterns, DSA & Coding |
| Career | Interview Prep, AI for Engineers |
| Security | Security Architecture |

Authoring rules for AI tools live in `.cursor/rules/`.
