# ADR-004: Backend Technology Stack

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Backend Stack" not separate ADRs for framework, ORM, deployment).

- **Status:** Proposed
- **Date:** 2026-02-06
- **Feature:** 010-fullstack-web-application
- **Context:** Phase II requires a robust, scalable backend API that handles JWT authentication, manages user data isolation, provides RESTful endpoints for task management, and integrates with Neon PostgreSQL. The constitution mandates Python 3.13+ with FastAPI and SQLModel for type safety and automatic validation.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence – affects how all API endpoints and data operations are structured
     2) Alternatives: Multiple viable options considered with tradeoffs (FastAPI vs Flask vs Django)
     3) Scope: Cross-cutting concern affecting all API routes, data models, and service layers
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Use **FastAPI with SQLModel ecosystem** for the backend API:

- **Framework**: FastAPI 0.104+ - Modern Python web framework with automatic validation and documentation
- **ORM**: SQLModel - SQL database toolkit combining SQLAlchemy and Pydantic features
- **Language**: Python 3.13+ - Latest Python version for performance and features
- **Authentication**: Integration with Better Auth JWT tokens for user authentication
- **Database Driver**: Async drivers for Neon PostgreSQL with connection pooling
- **Testing**: pytest for comprehensive API testing
- **Dependencies**: pydantic for data validation and serialization

<!-- For technology stacks, list all components:
     - Framework: FastAPI 0.104+
     - ORM: SQLModel
     - Language: Python 3.13+
     - Testing: pytest
-->

## Consequences

### Positive

- ✅ **Automatic Validation**: Pydantic integration provides automatic request/response validation
- ✅ **API Documentation**: Automatic OpenAPI/Swagger documentation generation
- ✅ **Type Safety**: Strong typing reduces runtime errors and improves development experience
- ✅ **Async Support**: Native async/await support for high-performance API operations
- ✅ **Integration**: Excellent compatibility with Better Auth JWT authentication
- ✅ **Developer Experience**: Fast development cycle with hot reloading and excellent tooling
- ✅ **Security**: Built-in protection against common security vulnerabilities

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong type safety -->

### Negative

- ⚠️ **Framework Coupling**: Heavy reliance on FastAPI conventions and features
- ⚠️ **Learning Curve**: Team members unfamiliar with FastAPI may need training
- ⚠️ **Ecosystem Maturity**: FastAPI newer than Flask/Django; some edge cases may lack solutions
- ⚠️ **SQLModel Specificity**: SQLModel is relatively new; limited resources compared to pure SQLAlchemy
- ⚠️ **Async Complexity**: Async programming model can introduce complexity in certain scenarios

<!-- Example: Framework coupling, learning curve, async complexity -->

## Alternatives Considered

### Alternative Stack A: Flask + SQLAlchemy + Marshmallow
- **Pros**: Mature ecosystem, wide adoption, extensive documentation
- **Cons**: Manual validation, no automatic documentation, more boilerplate code
- **Why Rejected**: Constitution mandates FastAPI for automatic validation and documentation; slower development pace

### Alternative Stack B: Django + DRF + PostgreSQL
- **Pros**: Batteries-included framework, proven for large applications, admin panel
- **Cons**: Heavier framework, more opinionated, potentially overkill for this application
- **Why Rejected**: Constitution specifically prefers FastAPI for microservice architecture; heavier framework than needed

### Alternative Stack C: Django + FastAPI hybrid (separate services)
- **Pros**: Could leverage Django's admin features and FastAPI's API features
- **Cons**: Increased complexity with multiple frameworks, additional maintenance overhead
- **Why Rejected**: Unnecessary complexity for this use case; violates KISS principle

<!-- Group alternatives by cluster:
     Alternative Stack A: Flask + SQLAlchemy + Marshmallow
     Alternative Stack B: Django + DRF + PostgreSQL
     Why rejected: More boilerplate, less automatic validation
-->

## References

- Feature Spec: ../../specs/010-fullstack-web-application/spec.md
- Implementation Plan: ../../specs/010-fullstack-web-application/plan.md
- Related ADRs: ADR-001 (Layered Architecture Pattern), ADR-003 (Frontend Technology Stack)
- Evaluator Evidence: [PHR reference to planning session]
