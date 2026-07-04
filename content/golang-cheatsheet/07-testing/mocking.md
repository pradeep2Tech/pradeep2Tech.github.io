---
title: "Mocking"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Interface-based testing, test doubles, and mock generation."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Mocking"
module: 7
moduleTitle: "Testing"
sectionRef: "7.2"
weight: 702
interviewHandbook: true
---

## Quick Revision

- **Accept interfaces, return structs** — mock interfaces in tests.
- Tools: `gomock`, `mockery`, hand-written fakes.
- Prefer fakes for simple behavior; mocks for interaction verification.

## Core Concepts

| Double | Use |
| :--- | :--- |
| Fake | Working in-memory implementation |
| Stub | Canned responses |
| Mock | Expect call sequences |

## Core Concepts

```go
type Store interface {
    Get(ctx context.Context, id string) (Item, error)
}

type fakeStore struct{ data map[string]Item }

func (f *fakeStore) Get(ctx context.Context, id string) (Item, error) {
    item, ok := f.data[id]
    if !ok {
        return Item{}, ErrNotFound
    }
    return item, nil
}
```

## Production Usage

- **Fake** — in-memory working implementation for most tests.
- **Mock** (gomock/mockery) — verify call counts/order on complex collaborators.
- Keep interfaces small at package boundaries.

## Common Mistakes

- Mocking concrete types instead of interfaces.
- Testing mock expectations instead of behavior.


---

## When do you use interface mocks versus fakes in Go tests?

### Short Answer
The mechanism-first explanation is interfaces are implicit (type,data) pairs; typed nil breaks `== nil` — for: When do you use interface mocks versus fakes in Go tests.

### Detailed Explanation
Tie method sets (value vs pointer receivers) to satisfaction and API design for: When do you use interface mocks versus fakes in Go tests.

### Internal Working
Small interfaces at boundaries; empty interface boxes values and may allocate — internal angle on: When do you use interface mocks versus fakes in Go tests.

### Production Notes
Use compile-time `var _ IF = (*T)(nil)` checks; test JSON nil edge cases for: When do you use interface mocks versus fakes in Go tests.

### Common Mistakes
Returning typed nil pointers in interface-typed APIs is a classic bug in: When do you use interface mocks versus fakes in Go tests.

### Follow-up Questions
How would you refactor a fat interface exposed by: When do you use interface mocks versus fakes in Go tests?

---
## What tools generate mocks from interfaces and tradeoffs?

### Short Answer
The senior-level answer is interfaces are implicit (type,data) pairs; typed nil breaks `== nil` — for: What tools generate mocks from interfaces and tradeoffs.

### Detailed Explanation
Tie method sets (value vs pointer receivers) to satisfaction and API design for: What tools generate mocks from interfaces and tradeoffs.

### Internal Working
Small interfaces at boundaries; empty interface boxes values and may allocate — internal angle on: What tools generate mocks from interfaces and tradeoffs.

### Production Notes
Use compile-time `var _ IF = (*T)(nil)` checks; test JSON nil edge cases for: What tools generate mocks from interfaces and tradeoffs.

### Common Mistakes
Returning typed nil pointers in interface-typed APIs is a classic bug in: What tools generate mocks from interfaces and tradeoffs.

### Follow-up Questions
How would you refactor a fat interface exposed by: What tools generate mocks from interfaces and tradeoffs?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Testing](/golang-cheatsheet/07-testing/testing/)
- [Next: Test Strategies](/golang-cheatsheet/07-testing/test-strategies/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
