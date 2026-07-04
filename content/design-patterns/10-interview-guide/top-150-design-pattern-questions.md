---
title: "Top 150 Design Pattern Questions"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "150 production-oriented design pattern and LLD interview questions."
tags: ["design-patterns", "lld", "interview"]
categories: ["Design Patterns"]
shortTitle: "Top 150"
module: 10
moduleTitle: "Interview Guide"
sectionRef: "10.1"
weight: 1001
interviewHandbook: true
---

Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. **Questions only** — each **Deep Dive** links to the canonical handbook page.

**Distribution:** Pattern Tradeoffs 40 · Pattern Comparisons 30 · SOLID 25 · LLD Design 25 · Architecture 15 · Anti-Patterns 15

| # | Question | Difficulty | Level | Topic | Deep Dive |
|---|----------|------------|--------|-------|-----------|
| 1 | When does extracting a Strategy class reduce complexity versus inlining a switch on payment type? | Medium | Senior Engineer | Pattern Tradeoffs | [Strategy Pattern](/design-patterns/04-behavioral-patterns/strategy-pattern/) |
| 2 | What operational cost do you accept when introducing a Factory hierarchy for two database drivers? | Medium | Senior Engineer | Pattern Tradeoffs | [Factory Method Pattern](/design-patterns/02-creational-patterns/factory-method-pattern/) |
| 3 | Why might a Builder be overkill for an object with three required fields and no optional steps? | Easy | Senior Engineer | Pattern Tradeoffs | [Builder Pattern](/design-patterns/02-creational-patterns/builder-pattern/) |
| 4 | How do you decide between Singleton and dependency-injected shared instance in a Spring service? | Medium | Lead | Pattern Tradeoffs | [Singleton Pattern](/design-patterns/02-creational-patterns/singleton-pattern/) |
| 5 | What testability tradeoff appears when using a Facade that hides too many collaborators? | Medium | Lead | Pattern Tradeoffs | [Facade Pattern](/design-patterns/03-structural-patterns/facade-pattern/) |
| 6 | When does a Proxy add latency that outweighs lazy-load benefits for small objects? | Medium | Senior Engineer | Pattern Tradeoffs | [Proxy Pattern](/design-patterns/03-structural-patterns/proxy-pattern/) |
| 7 | How do you weigh Flyweight memory savings against code complexity for a glyph editor? | Hard | Architect | Pattern Tradeoffs | [Flyweight Pattern](/design-patterns/03-structural-patterns/flyweight-pattern/) |
| 8 | What maintenance burden does the Visitor pattern impose when the element hierarchy changes frequently? | Hard | Architect | Pattern Tradeoffs | [Visitor Pattern](/design-patterns/04-behavioral-patterns/visitor-pattern/) |
| 9 | When is Chain of Responsibility preferable to a single validation method with ordered checks? | Medium | Senior Engineer | Pattern Tradeoffs | [Chain Of Responsibility Pattern](/design-patterns/04-behavioral-patterns/chain-of-responsibility-pattern/) |
| 10 | How do you balance Command pattern undo stacks against memory use in a collaborative editor? | Hard | Lead | Pattern Tradeoffs | [Command Pattern](/design-patterns/04-behavioral-patterns/command-pattern/) |
| 11 | What coupling risk does Mediator introduce when the hub becomes a god object? | Medium | Lead | Pattern Tradeoffs | [Mediator Pattern](/design-patterns/04-behavioral-patterns/mediator-pattern/) |
| 12 | When should you avoid Observer and use explicit polling or message bus instead? | Medium | Senior Engineer | Pattern Tradeoffs | [Observer Pattern](/design-patterns/04-behavioral-patterns/observer-pattern/) |
| 13 | How does Template Method lock subclasses into an inheritance hierarchy — when is that unacceptable? | Medium | Lead | Pattern Tradeoffs | [Template Method Pattern](/design-patterns/04-behavioral-patterns/template-method-pattern/) |
| 14 | What concurrency pitfalls appear when State transitions are not atomic in a multi-threaded order? | Hard | Lead | Pattern Tradeoffs | [State Pattern](/design-patterns/04-behavioral-patterns/state-pattern/) |
| 15 | When does Adapter hide technical debt instead of paying down the legacy integration? | Medium | Senior Engineer | Pattern Tradeoffs | [Adapter Pattern](/design-patterns/03-structural-patterns/adapter-pattern/) |
| 16 | How do you evaluate Bridge versus simple interface extraction for payment providers? | Medium | Lead | Pattern Tradeoffs | [Bridge Pattern](/design-patterns/03-structural-patterns/bridge-pattern/) |
| 17 | What performance tradeoff exists between Composite tree walks and flat collections for menus? | Medium | Senior Engineer | Pattern Tradeoffs | [Composite Pattern](/design-patterns/03-structural-patterns/composite-pattern/) |
| 18 | When does Decorator stack depth make debugging production incidents harder? | Medium | Lead | Pattern Tradeoffs | [Decorator Pattern](/design-patterns/03-structural-patterns/decorator-pattern/) |
| 19 | How do you justify Abstract Factory when only one product type exists in the family? | Medium | Senior Engineer | Pattern Tradeoffs | [Abstract Factory Pattern](/design-patterns/02-creational-patterns/abstract-factory-pattern/) |
| 20 | What cloning costs and risks does Prototype hide compared to fresh construction? | Medium | Senior Engineer | Pattern Tradeoffs | [Prototype Pattern](/design-patterns/02-creational-patterns/prototype-pattern/) |
| 21 | When is Iterator custom implementation worth it over language-native foreach? | Easy | Senior Engineer | Pattern Tradeoffs | [Iterator Pattern](/design-patterns/04-behavioral-patterns/iterator-pattern/) |
| 22 | How do Memento snapshots affect storage when undo history is unbounded? | Medium | Lead | Pattern Tradeoffs | [Memento Pattern](/design-patterns/04-behavioral-patterns/memento-pattern/) |
| 23 | What happens to open-closed compliance when every new feature adds a new Strategy class? | Medium | Architect | Pattern Tradeoffs | [Open Closed Principle](/design-patterns/01-solid-principles/open-closed-principle/) |
| 24 | How do you prevent pattern layering from obscuring the domain model in a parking lot LLD? | Hard | Lead | Pattern Tradeoffs | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 25 | When does rate-limiter token bucket design favor Strategy over a single algorithm class? | Medium | Senior Engineer | Pattern Tradeoffs | [Rate Limiter](/design-patterns/08-lld-case-studies/rate-limiter/) |
| 26 | What tradeoff do you make between elevator SCAN scheduling simplicity and fairness? | Hard | Architect | Pattern Tradeoffs | [Elevator Control System](/design-patterns/08-lld-case-studies/elevator-control-system/) |
| 27 | How do notification channel retries change your Observer versus Command choice? | Medium | Lead | Pattern Tradeoffs | [Notification System](/design-patterns/08-lld-case-studies/notification-system/) |
| 28 | When does task scheduler priority queue design justify Command over raw Runnable? | Medium | Senior Engineer | Pattern Tradeoffs | [Task Scheduler Lld](/design-patterns/08-lld-case-studies/task-scheduler-lld/) |
| 29 | How do you weigh Repository abstraction against YAGNI for a single-table CRUD service? | Medium | Lead | Pattern Tradeoffs | [Repository And Unit Of Work](/design-patterns/06-architectural-principles/repository-and-unit-of-work/) |
| 30 | What DTO mapping overhead is acceptable at API boundaries for a high-QPS service? | Medium | Senior Engineer | Pattern Tradeoffs | [Dto Entity Mapper Separation](/design-patterns/06-architectural-principles/dto-entity-mapper-separation/) |
| 31 | When does Specification pattern readability beat inline query predicates in repositories? | Medium | Lead | Pattern Tradeoffs | [Specification Pattern](/design-patterns/06-architectural-principles/specification-pattern/) |
| 32 | How do you decide between in-process Observer and out-of-process event bus for domain events? | Hard | Architect | Pattern Tradeoffs | [Domain Driven Design Building Blocks](/design-patterns/06-architectural-principles/domain-driven-design-building-blocks/) |
| 33 | What test double strategy changes when Facade wraps five external HTTP clients? | Medium | Lead | Pattern Tradeoffs | [Facade Pattern](/design-patterns/03-structural-patterns/facade-pattern/) |
| 34 | When does caching Proxy stale data violate business SLAs? | Medium | Senior Engineer | Pattern Tradeoffs | [Proxy Pattern](/design-patterns/03-structural-patterns/proxy-pattern/) |
| 35 | How do you measure whether a pattern reduced change frequency versus added ceremony? | Hard | Architect | Pattern Tradeoffs | [When To Use Which Pattern](/design-patterns/09-pattern-selection-guide/when-to-use-which-pattern/) |
| 36 | What team skill gap makes Visitor or Memento a poor choice regardless of fit? | Medium | Architect | Pattern Tradeoffs | [Pattern Decision Tree](/design-patterns/09-pattern-selection-guide/pattern-decision-tree/) |
| 37 | When should ride-sharing matching use Strategy for surge pricing versus hard-coded rules? | Hard | Lead | Pattern Tradeoffs | [Ride Sharing System](/design-patterns/08-lld-case-studies/ride-sharing-system/) |
| 38 | How do library fine policies map to State versus Strategy without over-patterning? | Medium | Senior Engineer | Pattern Tradeoffs | [Library Management System](/design-patterns/08-lld-case-studies/library-management-system/) |
| 39 | What refactoring cost do you accept before introducing Bridge for a two-provider integration? | Medium | Lead | Pattern Tradeoffs | [Bridge Pattern](/design-patterns/03-structural-patterns/bridge-pattern/) |
| 40 | When does golden hammer Singleton usage invalidate performance tuning elsewhere? | Medium | Architect | Pattern Tradeoffs | [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/) |
| 41 | How does Factory Method differ from Builder when construction has mandatory validation at the end? | Medium | Senior Engineer | Pattern Comparison | [Factory Vs Builder](/design-patterns/05-pattern-comparisons/factory-vs-builder/) |
| 42 | When would Abstract Factory be wrong for creating a single Connection type? | Medium | Senior Engineer | Pattern Comparison | [Factory Vs Abstract Factory](/design-patterns/05-pattern-comparisons/factory-vs-abstract-factory/) |
| 43 | What intent distinguishes Decorator from Proxy when both wrap the same interface? | Medium | Senior Engineer | Pattern Comparison | [Decorator Vs Proxy Vs Bridge](/design-patterns/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/) |
| 44 | How does Bridge differ from Adapter when both sit between two abstractions? | Hard | Lead | Pattern Comparison | [Decorator Vs Proxy Vs Bridge](/design-patterns/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/) |
| 45 | When is Strategy correct but State would model the same behavior with fewer classes? | Hard | Lead | Pattern Comparison | [Strategy Vs State](/design-patterns/05-pattern-comparisons/strategy-vs-state/) |
| 46 | How does Template Method compare to Strategy for a fixed multi-step export pipeline? | Medium | Senior Engineer | Pattern Comparison | [Strategy Vs State](/design-patterns/05-pattern-comparisons/strategy-vs-state/) |
| 47 | Why might composition with Strategy beat subclassing for pricing tiers? | Medium | Senior Engineer | Pattern Comparison | [Composition Vs Inheritance](/design-patterns/05-pattern-comparisons/composition-vs-inheritance/) |
| 48 | When does inheritance remain the right tool despite composition preference? | Medium | Lead | Pattern Comparison | [Composition Vs Inheritance](/design-patterns/05-pattern-comparisons/composition-vs-inheritance/) |
| 49 | How do you choose interface versus abstract class for a shared payment contract in Java? | Medium | Senior Engineer | Pattern Comparison | [Interface Vs Abstract Class](/design-patterns/05-pattern-comparisons/interface-vs-abstract-class/) |
| 50 | What Go idioms replace abstract classes when comparing to Java pattern examples? | Medium | Senior Engineer | Pattern Comparison | [Interface Vs Abstract Class](/design-patterns/05-pattern-comparisons/interface-vs-abstract-class/) |
| 51 | How does Facade differ from Adapter for a legacy billing subsystem? | Medium | Lead | Pattern Comparison | [Facade Pattern](/design-patterns/03-structural-patterns/facade-pattern/) |
| 52 | When is Composite overkill compared to a flat list with parentId? | Easy | Senior Engineer | Pattern Comparison | [Composite Pattern](/design-patterns/03-structural-patterns/composite-pattern/) |
| 53 | How does Observer differ from Mediator for chat room message routing? | Medium | Senior Engineer | Pattern Comparison | [Mediator Pattern](/design-patterns/04-behavioral-patterns/mediator-pattern/) |
| 54 | What distinguishes Command from Strategy when both encapsulate behavior? | Medium | Senior Engineer | Pattern Comparison | [Command Pattern](/design-patterns/04-behavioral-patterns/command-pattern/) |
| 55 | How does Chain of Responsibility compare to Specification for validation pipelines? | Hard | Lead | Pattern Comparison | [Specification Pattern](/design-patterns/06-architectural-principles/specification-pattern/) |
| 56 | When does Prototype beat Factory Method for expensive object creation? | Medium | Senior Engineer | Pattern Comparison | [Prototype Pattern](/design-patterns/02-creational-patterns/prototype-pattern/) |
| 57 | How do Flyweight and Singleton interact — when are both present in the same subsystem? | Hard | Architect | Pattern Comparison | [Singleton Pattern](/design-patterns/02-creational-patterns/singleton-pattern/) |
| 58 | What comparison matrix would you use for creational patterns in a platform SDK? | Hard | Architect | Pattern Comparison | [Factory Vs Builder](/design-patterns/05-pattern-comparisons/factory-vs-builder/) |
| 59 | How does hexagonal architecture compare to layered for a modular monolith? | Hard | Architect | Pattern Comparison | [Layered Vs Hexagonal Architecture](/design-patterns/06-architectural-principles/layered-vs-hexagonal-architecture/) |
| 60 | When does DIP look like DI in code but violate dependency direction in package structure? | Hard | Lead | Pattern Comparison | [Dependency Inversion Principle](/design-patterns/01-solid-principles/dependency-inversion-principle/) |
| 61 | How do you compare Repository pattern to Active Record for team velocity? | Medium | Lead | Pattern Comparison | [Repository And Unit Of Work](/design-patterns/06-architectural-principles/repository-and-unit-of-work/) |
| 62 | What side-by-side test would prove State is needed over Strategy for order lifecycle? | Hard | Lead | Pattern Comparison | [Strategy Vs State](/design-patterns/05-pattern-comparisons/strategy-vs-state/) |
| 63 | How does Iterator custom collection compare to Stream API for internal DSLs? | Medium | Senior Engineer | Pattern Comparison | [Iterator Pattern](/design-patterns/04-behavioral-patterns/iterator-pattern/) |
| 64 | When is Memento preferable to Command for undo in a form editor? | Medium | Senior Engineer | Pattern Comparison | [Memento Pattern](/design-patterns/04-behavioral-patterns/memento-pattern/) |
| 65 | How does Visitor double-dispatch compare to switch-on-type for tax calculation? | Medium | Lead | Pattern Comparison | [Visitor Pattern](/design-patterns/04-behavioral-patterns/visitor-pattern/) |
| 66 | What three questions disambiguate Decorator, Proxy, and Bridge in a code review? | Hard | Architect | Pattern Comparison | [Decorator Vs Proxy Vs Bridge](/design-patterns/05-pattern-comparisons/decorator-vs-proxy-vs-bridge/) |
| 67 | How would you compare parking lot FeeStrategy to elevator dispatch algorithm selection? | Medium | Senior Engineer | Pattern Comparison | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 68 | When does notification fan-out favor Observer over Mediator at scale? | Hard | Lead | Pattern Comparison | [Notification System](/design-patterns/08-lld-case-studies/notification-system/) |
| 69 | How do interface default methods change the interface-versus-abstract-class debate? | Medium | Senior Engineer | Pattern Comparison | [Interface Vs Abstract Class](/design-patterns/05-pattern-comparisons/interface-vs-abstract-class/) |
| 70 | What comparison would you present when a junior proposes Singleton for every shared service? | Medium | Lead | Pattern Comparison | [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/) |
| 71 | How do you identify multiple reasons to change in a class during code review? | Medium | Senior Engineer | SOLID | [Single Responsibility Principle](/design-patterns/01-solid-principles/single-responsibility-principle/) |
| 72 | When is splitting a class by SRP premature and what signals tell you to wait? | Medium | Lead | SOLID | [Single Responsibility Principle](/design-patterns/01-solid-principles/single-responsibility-principle/) |
| 73 | How does OCP apply to adding a new payment type without modifying checkout? | Medium | Senior Engineer | SOLID | [Open Closed Principle](/design-patterns/01-solid-principles/open-closed-principle/) |
| 74 | What is the difference between open for extension and open for modification in practice? | Medium | Senior Engineer | SOLID | [Open Closed Principle](/design-patterns/01-solid-principles/open-closed-principle/) |
| 75 | Why does Rectangle/Square violate LSP and how would you model dimensions correctly? | Easy | Senior Engineer | SOLID | [Liskov Substitution Principle](/design-patterns/01-solid-principles/liskov-substitution-principle/) |
| 76 | How do preconditions and postconditions formalize substitutability in APIs? | Hard | Architect | SOLID | [Liskov Substitution Principle](/design-patterns/01-solid-principles/liskov-substitution-principle/) |
| 77 | When does a fat interface force clients to depend on methods they never call? | Medium | Senior Engineer | SOLID | [Interface Segregation Principle](/design-patterns/01-solid-principles/interface-segregation-principle/) |
| 78 | How would you split a multi-function printer interface for ISP compliance? | Medium | Senior Engineer | SOLID | [Interface Segregation Principle](/design-patterns/01-solid-principles/interface-segregation-principle/) |
| 79 | What dependency direction violation appears when a domain entity imports JDBC? | Medium | Senior Engineer | SOLID | [Dependency Inversion Principle](/design-patterns/01-solid-principles/dependency-inversion-principle/) |
| 80 | How does DIP relate to hexagonal ports without conflating the two concepts? | Hard | Lead | SOLID | [Dependency Inversion Principle](/design-patterns/01-solid-principles/dependency-inversion-principle/) |
| 81 | How do you apply SOLID when refactoring a 2,000-line OrderManager god class? | Hard | Lead | SOLID | [Solid Principles Composition Guide](/design-patterns/01-solid-principles/solid-principles-composition-guide/) |
| 82 | What smell-to-fix map entry would you use for feature envy across services? | Medium | Lead | SOLID | [Solid Principles Composition Guide](/design-patterns/01-solid-principles/solid-principles-composition-guide/) |
| 83 | How does SRP interact with transaction boundaries in a place-order use case? | Hard | Lead | SOLID | [Single Responsibility Principle](/design-patterns/01-solid-principles/single-responsibility-principle/) |
| 84 | When does OCP conflict with YAGNI on a greenfield microservice? | Medium | Architect | SOLID | [Open Closed Principle](/design-patterns/01-solid-principles/open-closed-principle/) |
| 85 | How do you explain LSP to a team that treats inheritance as code reuse only? | Medium | Lead | SOLID | [Liskov Substitution Principle](/design-patterns/01-solid-principles/liskov-substitution-principle/) |
| 86 | What ISP refactoring would you prioritize before adding a fourth client to a shared interface? | Medium | Senior Engineer | SOLID | [Interface Segregation Principle](/design-patterns/01-solid-principles/interface-segregation-principle/) |
| 87 | How does DIP enable test doubles without a DI framework? | Medium | Senior Engineer | SOLID | [Dependency Inversion Principle](/design-patterns/01-solid-principles/dependency-inversion-principle/) |
| 88 | What SOLID letter breaks first in an anemic domain model and why? | Hard | Architect | SOLID | [Anemic Domain Model](/design-patterns/07-anti-patterns/anemic-domain-model/) |
| 89 | How do SOLID principles compose when designing a notification subsystem? | Hard | Lead | SOLID | [Solid Principles Composition Guide](/design-patterns/01-solid-principles/solid-principles-composition-guide/) |
| 90 | When is a single class cohesive enough to satisfy SRP despite multiple public methods? | Medium | Senior Engineer | SOLID | [Single Responsibility Principle](/design-patterns/01-solid-principles/single-responsibility-principle/) |
| 91 | How do sealed classes in Java 17 affect OCP for expression-based extension? | Medium | Senior Engineer | SOLID | [Open Closed Principle](/design-patterns/01-solid-principles/open-closed-principle/) |
| 92 | What LSP violations appear in mock-heavy tests that never use real subclasses? | Hard | Lead | SOLID | [Liskov Substitution Principle](/design-patterns/01-solid-principles/liskov-substitution-principle/) |
| 93 | How does ISP reduce rebuild times in large multi-module Maven projects? | Medium | Lead | SOLID | [Interface Segregation Principle](/design-patterns/01-solid-principles/interface-segregation-principle/) |
| 94 | How would you teach DIP using a payment gateway example without Spring jargon? | Medium | Senior Engineer | SOLID | [Dependency Inversion Principle](/design-patterns/01-solid-principles/dependency-inversion-principle/) |
| 95 | What SOLID regression risks appear after aggressive microservice extraction? | Hard | Architect | SOLID | [Solid Principles Composition Guide](/design-patterns/01-solid-principles/solid-principles-composition-guide/) |
| 96 | What entities and relationships would you model for a multi-floor parking lot with concurrency? | Hard | Lead | LLD Design | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 97 | How do you design spot allocation to avoid double-booking under concurrent entry? | Hard | Lead | LLD Design | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 98 | What pricing strategies would you plug into a parking lot without changing allocation? | Medium | Senior Engineer | LLD Design | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 99 | How do you model elevator state machines for idle, moving, and door-open phases? | Hard | Lead | LLD Design | [Elevator Control System](/design-patterns/08-lld-case-studies/elevator-control-system/) |
| 100 | What scheduling algorithm tradeoffs exist between SCAN and LOOK for elevator dispatch? | Hard | Architect | LLD Design | [Elevator Control System](/design-patterns/08-lld-case-studies/elevator-control-system/) |
| 101 | How would you design a token-bucket rate limiter for a sliding one-minute window? | Medium | Senior Engineer | LLD Design | [Rate Limiter](/design-patterns/08-lld-case-studies/rate-limiter/) |
| 102 | What thread-safety approach would you use for in-memory rate limiting at high RPS? | Hard | Lead | LLD Design | [Rate Limiter](/design-patterns/08-lld-case-studies/rate-limiter/) |
| 103 | How do you design multi-channel notification with retry and idempotency keys? | Hard | Lead | LLD Design | [Notification System](/design-patterns/08-lld-case-studies/notification-system/) |
| 104 | What domain boundaries separate template rendering from delivery in a notification service? | Medium | Senior Engineer | LLD Design | [Notification System](/design-patterns/08-lld-case-studies/notification-system/) |
| 105 | How would you model task priority and cancellation in a scheduler LLD? | Medium | Senior Engineer | LLD Design | [Task Scheduler Lld](/design-patterns/08-lld-case-studies/task-scheduler-lld/) |
| 106 | What Command pattern role does a task scheduler play for undo and audit? | Medium | Lead | LLD Design | [Task Scheduler Lld](/design-patterns/08-lld-case-studies/task-scheduler-lld/) |
| 107 | How do you design rider-driver matching with surge pricing in ride sharing? | Hard | Architect | LLD Design | [Ride Sharing System](/design-patterns/08-lld-case-studies/ride-sharing-system/) |
| 108 | What geospatial indexing concerns affect nearest-driver queries in ride sharing? | Hard | Architect | LLD Design | [Ride Sharing System](/design-patterns/08-lld-case-studies/ride-sharing-system/) |
| 109 | How would you model book copies, reservations, and fines in library management? | Medium | Lead | LLD Design | [Library Management System](/design-patterns/08-lld-case-studies/library-management-system/) |
| 110 | What concurrency rules apply when two members reserve the last copy of a book? | Hard | Lead | LLD Design | [Library Management System](/design-patterns/08-lld-case-studies/library-management-system/) |
| 111 | How do you present class diagrams in a 45-minute LLD interview without over-engineering? | Medium | Senior Engineer | LLD Design | [When To Use Which Pattern](/design-patterns/09-pattern-selection-guide/when-to-use-which-pattern/) |
| 112 | What non-functional requirements would you elicit before designing a rate limiter? | Medium | Senior Engineer | LLD Design | [Rate Limiter](/design-patterns/08-lld-case-studies/rate-limiter/) |
| 113 | How do you scope an LLD to in-memory versus distributed when the prompt is ambiguous? | Hard | Architect | LLD Design | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 114 | What scalability follow-ups would you mention after completing parking lot LLD? | Medium | Lead | LLD Design | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 115 | How would you extend elevator LLD to multiple shafts and floor requests? | Hard | Architect | LLD Design | [Elevator Control System](/design-patterns/08-lld-case-studies/elevator-control-system/) |
| 116 | What failure modes would you discuss for notification delivery at-least-once? | Medium | Lead | LLD Design | [Notification System](/design-patterns/08-lld-case-studies/notification-system/) |
| 117 | How do you justify entity design choices when the interviewer challenges your class count? | Medium | Senior Engineer | LLD Design | [Library Management System](/design-patterns/08-lld-case-studies/library-management-system/) |
| 118 | What patterns would you name-drop sparingly in ride-sharing matching design? | Medium | Lead | LLD Design | [Ride Sharing System](/design-patterns/08-lld-case-studies/ride-sharing-system/) |
| 119 | How do you trade off synchronous matching versus async dispatch in ride sharing LLD? | Hard | Lead | LLD Design | [Ride Sharing System](/design-patterns/08-lld-case-studies/ride-sharing-system/) |
| 120 | What common LLD mistakes do candidates make on parking lot pricing extensibility? | Medium | Senior Engineer | LLD Design | [Parking Lot](/design-patterns/08-lld-case-studies/parking-lot/) |
| 121 | How does constructor injection improve testability over field injection in Spring? | Medium | Senior Engineer | Architecture | [Dependency Injection Inversion Of Control](/design-patterns/06-architectural-principles/dependency-injection-inversion-of-control/) |
| 122 | What is the composition root and where should it live in a hexagonal application? | Hard | Lead | Architecture | [Dependency Injection Inversion Of Control](/design-patterns/06-architectural-principles/dependency-injection-inversion-of-control/) |
| 123 | When does layered architecture leak domain logic into the controller layer? | Medium | Senior Engineer | Architecture | [Layered Vs Hexagonal Architecture](/design-patterns/06-architectural-principles/layered-vs-hexagonal-architecture/) |
| 124 | How do ports and adapters map to inbound versus outbound dependencies? | Hard | Lead | Architecture | [Layered Vs Hexagonal Architecture](/design-patterns/06-architectural-principles/layered-vs-hexagonal-architecture/) |
| 125 | What distinguishes an entity from a value object in DDD building blocks? | Medium | Senior Engineer | Architecture | [Domain Driven Design Building Blocks](/design-patterns/06-architectural-principles/domain-driven-design-building-blocks/) |
| 126 | How do aggregate roots enforce invariants across child entities? | Hard | Lead | Architecture | [Domain Driven Design Building Blocks](/design-patterns/06-architectural-principles/domain-driven-design-building-blocks/) |
| 127 | When should DTOs diverge from domain entities at API boundaries? | Medium | Senior Engineer | Architecture | [Dto Entity Mapper Separation](/design-patterns/06-architectural-principles/dto-entity-mapper-separation/) |
| 128 | What mapping approach avoids anemic DTOs that mirror every entity field? | Medium | Lead | Architecture | [Dto Entity Mapper Separation](/design-patterns/06-architectural-principles/dto-entity-mapper-separation/) |
| 129 | How does Unit of Work coordinate multiple repository writes in one transaction? | Hard | Lead | Architecture | [Repository And Unit Of Work](/design-patterns/06-architectural-principles/repository-and-unit-of-work/) |
| 130 | When is Repository pattern unnecessary over direct JPA in a small service? | Medium | Senior Engineer | Architecture | [Repository And Unit Of Work](/design-patterns/06-architectural-principles/repository-and-unit-of-work/) |
| 131 | How do Specification objects compose AND/OR rules for complex queries? | Medium | Lead | Architecture | [Specification Pattern](/design-patterns/06-architectural-principles/specification-pattern/) |
| 132 | What bounded context signals tell you to split a monolith before patterns help? | Hard | Architect | Architecture | [Domain Driven Design Building Blocks](/design-patterns/06-architectural-principles/domain-driven-design-building-blocks/) |
| 133 | How does IoC container lifecycle interact with request-scoped beans in web apps? | Medium | Senior Engineer | Architecture | [Dependency Injection Inversion Of Control](/design-patterns/06-architectural-principles/dependency-injection-inversion-of-control/) |
| 134 | What ADR would you write choosing hexagonal over layered for a new payment service? | Hard | Architect | Architecture | [Layered Vs Hexagonal Architecture](/design-patterns/06-architectural-principles/layered-vs-hexagonal-architecture/) |
| 135 | How do domain events differ from integration events in a notification architecture? | Hard | Architect | Architecture | [Domain Driven Design Building Blocks](/design-patterns/06-architectural-principles/domain-driven-design-building-blocks/) |
| 136 | What symptoms identify a god object beyond line count? | Medium | Senior Engineer | Anti-Pattern | [God Object](/design-patterns/07-anti-patterns/god-object/) |
| 137 | How do you refactor a god object incrementally without a big-bang rewrite? | Hard | Lead | Anti-Pattern | [God Object](/design-patterns/07-anti-patterns/god-object/) |
| 138 | What is an anemic domain model and why do CRUD services encourage it? | Medium | Senior Engineer | Anti-Pattern | [Anemic Domain Model](/design-patterns/07-anti-patterns/anemic-domain-model/) |
| 139 | How do you move behavior from service classes back into rich domain entities? | Hard | Lead | Anti-Pattern | [Anemic Domain Model](/design-patterns/07-anti-patterns/anemic-domain-model/) |
| 140 | What code smells distinguish spaghetti code from legitimate complex workflows? | Medium | Senior Engineer | Anti-Pattern | [Spaghetti Code](/design-patterns/07-anti-patterns/spaghetti-code/) |
| 141 | How does shotgun surgery manifest in microservices with shared libraries? | Medium | Lead | Anti-Pattern | [Shotgun Surgery](/design-patterns/07-anti-patterns/shotgun-surgery/) |
| 142 | What OCP refactoring reduces shotgun surgery when adding a new report format? | Medium | Lead | Anti-Pattern | [Shotgun Surgery](/design-patterns/07-anti-patterns/shotgun-surgery/) |
| 143 | How do you detect golden hammer pattern adoption in architecture reviews? | Medium | Architect | Anti-Pattern | [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/) |
| 144 | When is Singleton abuse an anti-pattern versus legitimate single instance? | Medium | Senior Engineer | Anti-Pattern | [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/) |
| 145 | How does god object relate to violation of SRP in legacy ERP modules? | Medium | Lead | Anti-Pattern | [God Object](/design-patterns/07-anti-patterns/god-object/) |
| 146 | What team practices prevent anemic domain models in DDD initiatives? | Hard | Architect | Anti-Pattern | [Anemic Domain Model](/design-patterns/07-anti-patterns/anemic-domain-model/) |
| 147 | How do cyclic dependencies contribute to spaghetti code and how do you break them? | Hard | Lead | Anti-Pattern | [Spaghetti Code](/design-patterns/07-anti-patterns/spaghetti-code/) |
| 148 | What metrics would you track after refactoring shotgun surgery hotspots? | Medium | Lead | Anti-Pattern | [Shotgun Surgery](/design-patterns/07-anti-patterns/shotgun-surgery/) |
| 149 | How do you push back when stakeholders demand a pattern for every ticket? | Medium | Architect | Anti-Pattern | [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/) |
| 150 | What anti-pattern often follows premature abstraction of a one-off script? | Easy | Senior Engineer | Anti-Pattern | [Golden Hammer](/design-patterns/07-anti-patterns/golden-hammer/) |
