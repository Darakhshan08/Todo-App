# ADR-002: In-Memory Storage Strategy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2026-01-19
- **Feature:** Phase I – In-Memory Todo CLI
- **Context:** Phase I requires a simple, fast storage mechanism that supports up to 999 tasks per session. The constitution mandates in-memory storage only (no files, databases, or persistence). The storage must support sequential ID generation (task-001, task-002, task-003) and maintain task creation order.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: ✅ Long-term consequence – storage strategy affects all CRUD operations and Phase II migration
     2) Alternatives: ✅ Multiple viable options (list vs dict vs custom class)
     3) Scope: ✅ Cross-cutting concern affecting all 5 features and data model design
-->

## Decision

Use a **simple list-based storage** with a separate ID counter:

```python
# Global module-level storage (process-scoped)
tasks: List[Task] = []           # Stores Task objects in creation order
next_id: int = 1                 # Counter for ID generation (1, 2, 3, ...)
```

**ID Generation Strategy**:
- Format: `"task-{next_id:03d}"` → task-001, task-002, task-003
- Increment `next_id` after each task creation
- IDs are **never reused** within a session (even after deletion)
- Maximum: 999 tasks per session (3-digit format)

**Task Lookup Strategy**:
- Linear search through list by ID string matching: `next(t for t in tasks if t.id == target_id)`
- Acceptable for Phase I scale (sub-100ms for <1000 items)

**Deletion Strategy**:
- Remove from list without renumbering: `tasks.remove(task)`
- Remaining tasks keep original IDs (no ID reassignment)

## Consequences

### Positive

- ✅ **Simplicity**: Minimal code; no complex data structures; easy to understand
- ✅ **Constitutional Compliance**: Pure in-memory (Principle IV); no file I/O
- ✅ **Deterministic**: Predictable behavior; no randomness; fully testable
- ✅ **Maintains Order**: List preserves insertion order for FR-005 (view in creation order)
- ✅ **Phase II Ready**: Easy to swap list with database ORM (List[Task] → DB query)
- ✅ **No Dependencies**: Python stdlib only; no external packages

### Negative

- ⚠️ **Performance**: O(n) lookup for update/delete/toggle operations (acceptable for n<1000)
- ⚠️ **Memory Inefficiency**: Storing full Task objects (vs just IDs + dict) uses more memory
- ⚠️ **No Indexing**: Cannot quickly filter by status or search by title without iteration
- ⚠️ **ID Limit**: 999 tasks per session (acceptable for Phase I; would need expansion for production)
- ⚠️ **Data Loss on Exit**: All tasks lost when process terminates (intentional per constitution)

## Alternatives Considered

### Alternative A: Dictionary Storage (ID → Task mapping)
- **Structure**: `tasks: Dict[str, Task] = {}` with ID as key
- **Pros**: O(1) lookup by ID; fast update/delete/toggle
- **Cons**: Loses insertion order (critical for FR-005 in view-list spec); requires separate list or OrderedDict
- **Why Rejected**: Insertion order is a core requirement; OrderedDict doesn't simplify enough to justify

### Alternative B: Custom TaskStore Class
- **Structure**: Class with `add()`, `get()`, `delete()`, `all()` methods wrapping list
- **Pros**: Encapsulation; can add indexing later; cleaner API
- **Cons**: Over-engineering for Phase I; more code; doesn't add value vs simple list
- **Why Rejected**: YAGNI principle; simple list is sufficient for current requirements

### Alternative C: SQLite In-Memory Database
- **Structure**: `:memory:` SQLite with Task table
- **Pros**: SQL querying; indexing; mature; production-ready
- **Cons**: Violates constitution (no databases); adds dependency; overkill for Phase I
- **Why Rejected**: Constitution explicitly forbids databases (Principle IV)

### Alternative D: Dual Structure (List + Dict)
- **Structure**: Maintain both `List[Task]` for order and `Dict[str, Task]` for lookup
- **Pros**: O(1) lookup + preserved order
- **Cons**: Double memory usage; synchronization complexity; mutation errors
- **Why Rejected**: Premature optimization; Phase I scale doesn't justify complexity

## References

- Feature Spec: [specs/002-view-task-list/spec.md](../../specs/002-view-task-list/spec.md) (FR-005: creation order)
- Implementation Plan: [specs/001-add-task/plan.md](../../specs/001-add-task/plan.md) (lines 234-265: Data Model)
- Constitution: [.specify/memory/constitution.md](../../.specify/memory/constitution.md) (Principle IV – In-Memory Only)
- Related ADRs: ADR-001 (Layered Architecture Pattern)
- Evaluator Evidence: [history/prompts/phase-i-core/9-specification-analysis.misc.prompt.md](../../history/prompts/phase-i-core/9-specification-analysis.misc.prompt.md)

---

**Decision Made By**: Phase I Planning (Claude Code + Spec-Kit Plus)
**Approved By**: Hackathon Team
**Review Date**: 2026-01-19
**Performance Assumption**: O(n) lookup acceptable for n<1000 (validated by plan.md performance goal: sub-100ms)
