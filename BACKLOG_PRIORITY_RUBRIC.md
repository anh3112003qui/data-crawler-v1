# Backlog Prioritization Rubric

This rubric defines how we evaluate and rank backlog items for **data-crawler-v1**. Each item is scored against the following criteria (0‑5 points each). The total score determines priority.

## Criteria

| Criterion | Description | Points (0‑5) |
|-----------|-------------|--------------|
| **Scope** | Size of work required (e.g., number of files, complexity). Smaller scope gets higher points. |  |
| **Impact** | Business or user impact if delivered (revenue, users, compliance). Higher impact gets higher points. |  |
| **Dependencies** | Number of other tasks/blockers. Fewer dependencies scores higher. |  |
| **Urgency** | Time‑sensitivity (regulatory, deadline‑driven). More urgent scores higher. |  |
| **Risk Reduction** | Mitigates high‑risk technical debt or security issues. Greater risk reduction scores higher. |  |

## Scoring Example

- **Scope**: 3 (medium effort, <3 days)
- **Impact**: 5 (critical customer‑facing bug)
- **Dependencies**: 2 (depends on two other tickets)
- **Urgency**: 4 (needs fix before next release)
- **Risk Reduction**: 3 (removes moderate security risk)

**Total Score**: 17 / 25 → **High priority**.

## Priority Bands

| Total Score | Priority |
|-------------|----------|
| 0‑10 | Low |
| 11‑17 | Medium |
| 18‑25 | High |

Use this rubric during backlog grooming to assign a **Priority** label to each item.
