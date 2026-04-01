# Backlog Prioritization Rubric

This rubric defines how we evaluate and rank backlog items for the **data-crawler-v1** project.

## Evaluation Dimensions

1. **Scope** (0‑5) – How much of the codebase or functionality is affected.
2. **Impact** (0‑5) – Expected value to users or business (performance, reliability, new capability).
3. **Urgency** (0‑5) – Time‑sensitivity (e.g., security fix, blocking release).
4. **Dependencies** (0‑5) – Number and criticality of other items that must be completed first.
5. **Effort Estimate** (0‑5) – Relative effort required (higher score for lower effort).

## Scoring

Each dimension is scored from 0 (lowest) to 5 (highest). The total score (max 25) determines priority:

- **21‑25** – *Critical*: Must be addressed in the next sprint.
- **16‑20** – *High*: Schedule early in the upcoming sprint.
- **11‑15** – *Medium*: Plan for the current or next sprint.
- **0‑10**  – *Low*: Can be deferred.

## Process

1. Review each open issue/PR.
2. Assign scores for each dimension.
3. Sum scores to obtain the total priority score.
4. Sort items by descending total score.
5. Select the top 5 items for immediate work.

## Documentation

All backlog items should have a **Rubric Score** comment block in the issue description following this template:

```
**Rubric Scores**
- Scope: X
- Impact: Y
- Urgency: Z
- Dependencies: W
- Effort: V
```

The scores will be used by the Dev Engineer to generate the *Top 5 Priority* list.

---

*Created by Dev Engineer on $(date)*
