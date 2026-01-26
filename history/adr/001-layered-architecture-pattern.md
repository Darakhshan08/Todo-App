# ADR-001: Layered Architecture Pattern for CLI Application

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2026-01-19
- **Feature:** Phase I – In-Memory Todo CLI
- **Context:** Phase I requires a Python console application with clean separation of concerns to enable Phase II evolution (web API, persistence). The application must be testable, maintainable, and align with Clean Architecture principles (Constitution Principle V).

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: ✅ Long-term consequence for architecture – defines how all features are structured
     2) Alternatives: ✅ Multiple viable options considered (monolithic, data-driven, MVC)
     3) Scope: ✅ Cross-cutting concern affecting all 5 features and future phases
-->

## Decision

Implement a **4-layer architecture** for the CLI application:

1. **CLI Layer** (`src/cli/`)
   - `ui.py` – User prompts, display formatting, menu navigation
   - `commands.py` – Command handlers routing user actions to services

2. **Service Layer** (`src/services/`)
   - `task_service.py` – Business logic for CRUD operations (add, view, update, delete, toggle)
   - Centralizes all task management logic for reuse in future phases

3. **Validator Layer** (`src/services/`)
   - `task_validator.py` – Input validation (title/description length, ID format, whitespace trimming)
   - Ensures data integrity before storage

4. **Data Model Layer** (`src/models/`)
   - `task.py` – Task entity definition (id, title, description, status, created_at)
   - ID generation logic (sequential task-001, task-002, task-003)
   - In-memory storage (List[Task])

**Data Flow**: CLI → Commands → Service → Validator → Model → Memory

## Consequences

### Positive

- ✅ **Phase II Ready**: Service layer can be directly wrapped by REST API endpoints without refactoring business logic
- ✅ **Testability**: Each layer can be unit tested independently (validators, services, models)
- ✅ **Maintainability**: Clear separation of concerns makes code easier to understand and modify
- ✅ **Reusability**: Service layer logic can be imported by future web/mobile interfaces
- ✅ **Constitutional Compliance**: Satisfies Clean Architecture principle (Principle V)
- ✅ **Validation Centralization**: Single validator prevents duplicate validation logic across features

### Negative

- ⚠️ **Overhead for Simple App**: 4 layers may seem over-engineered for Phase I's simple requirements
- ⚠️ **More Files**: ~8 Python files instead of 1-2 monolithic files increases initial complexity
- ⚠️ **Learning Curve**: Team members unfamiliar with layered architecture need time to understand structure
- ⚠️ **Import Management**: Requires careful dependency management to avoid circular imports

## Alternatives Considered

### Alternative A: Monolithic Single-File Approach
- **Structure**: All logic in `main.py` (CLI + business logic + validation + data model)
- **Pros**: Simpler for Phase I; faster initial development; fewer imports
- **Cons**: Impossible to reuse business logic in Phase II; difficult to test; violates Clean Architecture principle
- **Why Rejected**: Constitution mandates clean architecture; Phase II evolution would require complete refactor

### Alternative B: Data-Driven Design (Active Record Pattern)
- **Structure**: Task model contains business logic methods (task.add(), task.delete())
- **Pros**: Common in ORMs (ActiveRecord, Django models); less boilerplate
- **Cons**: Tight coupling between data and behavior; harder to swap storage layers; violates Single Responsibility
- **Why Rejected**: Constitution requires separation of concerns; Phase II needs flexible service layer

### Alternative C: MVC Pattern (Model-View-Controller)
- **Structure**: Models (data), Views (CLI display), Controllers (command routing)
- **Pros**: Well-known pattern; clear separation
- **Cons**: Controller layer often becomes bloated; no explicit service layer for Phase II API
- **Why Rejected**: Layered architecture with service layer better aligns with future API needs

## References

- Feature Spec: [specs/001-add-task/spec.md](../../specs/001-add-task/spec.md) (and 002-005)
- Implementation Plan: [specs/001-add-task/plan.md](../../specs/001-add-task/plan.md) (lines 118-175)
- Constitution: [.specify/memory/constitution.md](../../.specify/memory/constitution.md) (Principle V – Clean Architecture)
- Related ADRs: ADR-002 (In-Memory Storage Strategy)
- Evaluator Evidence: [history/prompts/phase-i-core/7-phase-i-execution-plan.plan.prompt.md](../../history/prompts/phase-i-core/7-phase-i-execution-plan.plan.prompt.md)

---

**Decision Made By**: Phase I Planning (Claude Code + Spec-Kit Plus)
**Approved By**: Hackathon Team
**Review Date**: 2026-01-19
