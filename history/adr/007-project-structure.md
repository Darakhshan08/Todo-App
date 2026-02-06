# ADR-007: Project Structure

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Project Structure" not separate ADRs for monorepo vs multirepo, directory layout).

- **Status:** Proposed
- **Date:** 2026-02-06
- **Feature:** 010-fullstack-web-application
- **Context:** Phase II requires a maintainable, scalable project structure that separates concerns between frontend and backend, enables independent development and deployment, supports clean architecture principles, and follows team conventions. The constitution mandates monorepo structure with Phase-2 organization for full-stack applications.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence – affects how code is organized, developed, and maintained
     2) Alternatives: Multiple viable options considered with tradeoffs (monorepo vs multirepo vs hybrid)
     3) Scope: Cross-cutting concern affecting all development workflows and project organization
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Use **Monorepo structure with Phase-2 organization**:

- **Repository Structure**: Single repository with separate frontend and backend applications
- **Directory Layout**:
  - `Phase-2/frontend/` - Next.js application with src, components, pages, services
  - `Phase-2/backend/` - FastAPI application with models, services, api, dependencies
  - `Phase-2/specs/` - Specification files organized by type (features, api, database, ui)
- **Shared Config**: Root-level configuration files for linters, testing, and deployment
- **Independent Deployment**: Frontend and backend can be deployed separately
- **Cross-cutting Concerns**: Specifications and shared documentation in dedicated directories
- **Local Development**: Docker Compose for coordinated local development environment

<!-- For technology stacks, list all components:
     - Structure: Monorepo
     - Organization: Phase-2 with frontend/backend/specs
     - Coordination: Docker Compose
-->

## Consequences

### Positive

- ✅ **Simplified Management**: Single repository for all related code and documentation
- ✅ **Consistent Tooling**: Shared linting, formatting, and CI/CD configurations
- ✅ **Cross-team Collaboration**: Easy coordination between frontend and backend developers
- ✅ **Atomic Commits**: Changes spanning frontend and backend can be committed together
- ✅ **Shared Dependencies**: Common dependencies managed in single place
- ✅ **Specification Alignment**: Specs centralized for full-stack visibility
- ✅ **Team Adoption**: Consistent with constitution and team expectations

<!-- Example: Simplified management, improved collaboration, consistent tooling -->

### Negative

- ⚠️ **Repository Size**: Single repository grows larger over time
- ⚠️ **Build Complexity**: May require sophisticated build systems as project grows
- ⚠️ **Deployment Coupling**: Risk of unintended coupling between frontend and backend deployments
- ⚠️ **Permission Granularity**: Harder to apply different permissions to frontend vs backend code
- ⚠️ **Merge Conflicts**: Potential for more merge conflicts across teams

<!-- Example: Repository size, build complexity, deployment coupling -->

## Alternatives Considered

### Alternative A: Separate Repositories (Multirepo)
- **Pros**: Independent development cycles, separate permissions, isolated deployments
- **Cons**: Complex coordination between frontend and backend, difficulty managing cross-cutting changes
- **Why Rejected**: Constitution mandates monorepo for Phase II; coordination challenges outweigh independence benefits

### Alternative B: Hybrid Structure (Core + Extensions)
- **Pros**: Balance between monorepo and multirepo benefits
- **Cons**: Added complexity in build and deployment processes
- **Why Rejected**: Introduces unnecessary complexity for this project size; monorepo sufficient

### Alternative C: Flattened Structure (no Phase-2 nesting)
- **Pros**: Simpler directory structure
- **Cons**: Doesn't align with constitution requirements, harder to distinguish from Phase I code
- **Why Rejected**: Constitution explicitly requires Phase-2 organization for clear phase distinction

<!-- Group alternatives by cluster:
     Alternative A: Multirepo structure
     Alternative B: Hybrid structure
     Why rejected: Coordination difficulties, complexity
-->

## References

- Feature Spec: ../../specs/010-fullstack-web-application/spec.md
- Implementation Plan: ../../specs/010-fullstack-web-application/plan.md
- Related ADRs: ADR-001 (Layered Architecture Pattern), ADR-003 (Frontend Technology Stack), ADR-004 (Backend Technology Stack)
- Evaluator Evidence: [PHR reference to planning session]
