# AI Agent Guide — Enterprise Knowledge Hub

Hugo static site (PaperMod theme) publishing interview-focused engineering curriculum. **~900 markdown pages** across 20 curriculum sections.

**Do not scan the full repo.** Start here, then open only the files listed for your task.

## Quick Routing

| Task | Read first | Cursor rule |
|------|------------|-------------|
| Add or edit a curriculum section | `data/curriculum_sections.yaml`, `data/curriculum_sidebar.yaml` | `curriculum-sections.mdc` |
| Edit DSA problem pages | `scripts/dsa_coding_questions_data.py`, reference `content/dsa-coding/01-arrays-hashmap-two-pointers/two-sum.md` | `dsa-coding-posts.mdc` |
| Edit design pattern / LLD pages | `data/design_patterns_modules.yaml`, reference `content/design-patterns/strategy-pattern.md` | `lld-posts.mdc` |
| Edit system design posts | reference `content/system-design/urlshortner.md` | `system-design-posts.mdc` |
| Edit microservices posts | reference `content/microservices/circuit-breaker-pattern.md` | `microservices-posts.mdc` |
| Edit security architecture posts | `content/security-architecture/`, `data/security_architecture_modules.yaml`, `data/security_architecture_order.yaml` | `security-architecture-posts.mdc` |
| Edit cheat-sheet handbooks (Java, Python, Go, K8s, Redis, PostgreSQL, Spring) | section's `data/*_modules.yaml` | `cheatsheet-template.mdc` + section rule |
| Edit layouts or shortcodes | `docs/ai-index/ARCHITECTURE.md` | — |
| Understand full section map | `docs/ai-index/SECTION-REGISTRY.md` | `project-index.mdc` |

## Repository Layout

```
tech-blog/
├── AGENTS.md                    ← you are here
├── hugo.toml                    ← site config
├── data/
│   ├── curriculum_sections.yaml ← top-level nav (home + header)
│   ├── curriculum_sidebar.yaml  ← per-section modules/order keys
│   └── <section>_modules.yaml   ← module TOC per section
│   └── <section>_order.yaml     ← flat prev/next order
├── content/<section>/           ← markdown pages (one file per topic)
├── layouts/
│   ├── <section>/list.html      ← section list layout
│   ├── <section>/single.html    ← section page layout
│   ├── partials/                ← shared nav, sidebar, collapsibles
│   └── shortcodes/              ← impl-tabs, code-tabs, api-*, callouts
├── scripts/
│   ├── build_<section>_*.py     ← sync yaml + regen pages (some sections)
│   └── generate_ai_index.py     ← regen docs/ai-index/SECTION-REGISTRY.md
├── .cursor/rules/               ← per-section authoring rules (.mdc)
└── docs/ai-index/               ← AI indexing docs (read before broad search)
```

## Curriculum Groups

Defined in `data/curriculum_sections.yaml`:

| Group | Sections |
|-------|----------|
| **design** | system-design, microservices, technology-playbook |
| **handbooks** | java-engineering, spring-boot, python-cheatsheet, golang-cheatsheet, kafka-handbook, kubernetes-handbook, redis-cheatsheet, database-handbook, postgresql-cheatsheet, mongodb-cheatsheet, cloud-handbook |
| **practice** | design-patterns, dsa-coding |
| **career** | interview-prep, ai-for-engineers |
| **security** | security-architecture |

## Security Architecture Authoring

Security Architecture is a senior-engineer-to-architect playbook.

Before editing security content:
1. Read `.cursor/rules/security-architecture-posts.mdc`.
2. Scan only the relevant files under `content/security-architecture/`.
3. Do not preserve old page boundaries if merging improves learning.
4. Avoid duplicate explanations of OAuth, JWT, Kubernetes, AWS, mTLS, secrets, and API Gateway.
5. Every security page should answer one architectural question.
6. Prefer fewer strong documents over many thin documents.
7. Backward compatibility is not required until the security section is public.

Preferred learning flow:

Trust boundaries
→ Enterprise authentication
→ Authorization
→ Browser/API security
→ Service-to-service security
→ Secrets/data protection
→ Platform security
→ Enterprise identity lifecycle
→ Supply chain
→ Security operations

## Content Types

| Type | UX | Cursor rule | Example |
|------|-----|-------------|---------|
| **Playbook** | Collapsible sections, Mermaid, API panels | `system-design-posts.mdc`, `microservices-posts.mdc` | `content/system-design/urlshortner.md` |
| **Cheat sheet** | Flat `##` headings, tables, snippets | `cheatsheet-template.mdc` | `content/java-engineering/hashmap-internals.md` |
| **Interview problem** | Problem → pattern → impl-tabs (Java + Go) | `dsa-coding-posts.mdc`, `lld-posts.mdc` | `content/dsa-coding/.../two-sum.md` |
| **Interview Q&A** | Long-form probes | section-specific | `content/interview-prep/` |

## Navigation Data Flow

```
curriculum_sections.yaml  →  home grid + header nav
curriculum_sidebar.yaml   →  maps section slug → modules yaml + order yaml
<section>_modules.yaml    →  module groups + topic slugs
<section>_order.yaml      →  flat prev/next links (section-nav.html)
```

Some sections keep structure in Python registries instead of hand-editing yaml:

- **dsa-coding** → `scripts/dsa_coding_questions_data.py` → `build_dsa_coding_handbook.py`
- **design-patterns** → `data/design_patterns_modules.yaml` + `generate_lld_stubs.py`

## Build & Preview

```bash
hugo server -D          # local preview (restart after new sections)
hugo --minify           # production build → public/
```

Section-specific regen (when yaml/scripts change):

```bash
python scripts/build_dsa_coding_handbook.py
python scripts/build_java_engineering_handbook.py
python scripts/generate_ai_index.py    # refresh SECTION-REGISTRY.md
```

## Shared Shortcodes

| Shortcode | Used by | File |
|-----------|---------|------|
| `impl-tabs` / `impl-tab` | DSA, design-patterns | `layouts/shortcodes/impl-tabs.html` |
| `code-tabs` / `code-tab` | microservices, system-design | `layouts/shortcodes/code-tabs.html` |
| `api-endpoint`, `api-request`, `api-response` | system-design | `layouts/shortcodes/api-*.html` |
| `note`, `tip`, `warning` | all sections | `layouts/shortcodes/*.html` |

## What NOT to Touch

- `themes/PaperMod/` — upstream theme; override in `layouts/` instead
- `scripts/phase_*.py`, `scripts/wave*.py` — one-off migration scripts (historical)
- `public/`, `resources/` — build output (gitignored)

## Regenerate Index

After adding sections or large content changes:

```bash
python scripts/generate_ai_index.py
```
