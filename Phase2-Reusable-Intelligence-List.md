# Phase 2 - Reusable Intelligence List

## MAIN AGENTS (2)

### 1. product-architect-agent
**Description**: Coordinates full-stack development workflow, enforces Spec-Driven Development for Phase 2, and manages transitions between frontend/backend work.

### 2. fullstack-planner-agent
**Description**: Designs the monorepo architecture, coordinates Next.js frontend and FastAPI backend, ensures API contracts match, validates request/response flow, and coordinates deployment strategies for full-stack applications.

---

## SPECIALIZED SUBAGENTS (9)

### 1. fastapi-backend-expert
**Description**: Designs and implements FastAPI applications with async/await patterns, dependency injection, middleware, and best practices for RESTful APIs.

### 2. api-design-agent
**Description**: Creates RESTful API endpoint specifications with proper HTTP methods, request/response schemas, error handling, and JWT authentication integration for FastAPI backends.

### 3. database-schema-agent
**Description**: Creates database schema specifications using SQLModel ORM, defines table relationships, indexes, constraints, and migration strategies for Neon Serverless PostgreSQL.

### 4. auth-integration-agent
**Description**: Designs authentication flows using Better Auth, implements JWT token generation/validation, and ensures secure communication between Next.js frontend and FastAPI backend with user isolation.

### 5. nextjs-frontend-expert
**Description**: Generates Next.js component specifications using App Router, server/client component patterns, async data fetching, Tailwind CSS styling, and API integration patterns for responsive web interfaces.

### 6. api-security-agent
**Description**: Reviews and implements API security patterns including JWT middleware, user isolation in database queries, CORS configuration, and secure error handling to prevent unauthorized access.

### 7. backend-testing-expert
**Description**: Creates pytest test suites for FastAPI endpoints, database operations, authentication flows, and integration tests with coverage analysis.

### 8. ui-ux-expert
**Description**: Creates responsive, accessible UI designs using Tailwind CSS and Shadcn components with focus on user experience and visual hierarchy.

### 9. deployment-expert
**Description**: Configures Docker, docker-compose, environment variables, and deployment strategies for Vercel (frontend) and cloud platforms (backend).

---

## BACKEND SKILLS (10)

### 1. sp.fastapi-setup
**Description**: Initialize FastAPI project with proper structure and dependencies. Creates FastAPI application with async support, CORS middleware, lifespan events, and organized folder structure.

### 2. sp.backend-api-routes
**Description**: Generate REST API endpoints for resources with CRUD operations. Creates endpoints with proper HTTP methods, request validation using Pydantic, and async route handlers.

### 3. sp.sqlmodel-schema
**Description**: Define database table schemas using SQLModel ORM. Creates SQLModel table classes with proper field types, constraints, relationships, and indexes for PostgreSQL.

### 4. sp.neon-postgres
**Description**: Setup Neon PostgreSQL database connection with async support. Configures async database connection with connection pooling, error handling, and session management.

### 5. sp.backend-jwt-auth
**Description**: Implement JWT token validation middleware for FastAPI. Creates JWT authentication middleware that validates tokens, extracts user info, and ensures user isolation.

### 6. sp.better-auth-python
**Description**: Integrate Better Auth with FastAPI backend. Sets up Better Auth JWT verification in Python, validates tokens from frontend, and extracts user_id for database queries.

### 7. sp.backend-error-handling
**Description**: Implement global error handling and custom exceptions. Creates HTTPException handlers, custom error classes, and consistent error response format.

### 8. sp.backend-service-layer
**Description**: Create service layer pattern for business logic. Separates business logic from route handlers, implements reusable service classes for database operations and validation.

### 9. sp.backend-query-params
**Description**: Add filtering, sorting, and pagination to list endpoints. Implements query parameters for filtering by status, sorting by fields, and pagination with limit/offset.

### 10. sp.backend-testing
**Description**: Generate pytest test suites for API endpoints. Creates unit tests for routes, integration tests for database operations, and fixtures for test data setup.

---

## FRONTEND SKILLS (10)

### 11. sp.nextjs-setup
**Description**: Initialize Next.js 16+ project with App Router. Creates Next.js application with TypeScript, Tailwind CSS, App Router structure, and proper folder organization.

### 12. sp.nextjs-app-router
**Description**: Create Next.js App Router pages and layouts. Generates page routes with proper file naming, layouts with metadata, and loading/error states.

### 13. sp.frontend-component
**Description**: Generate reusable React components. Creates React components with TypeScript props, proper naming conventions, and separation of server/client components.

### 14. sp.frontend-api-client
**Description**: Create API client utility for backend communication. Builds type-safe API client with async functions, JWT token injection, error handling, and base URL configuration.

### 15. sp.frontend-auth
**Description**: Setup authentication context and hooks. Creates React Context for auth state, custom hooks for login/logout/signup, and token storage in localStorage/cookies.

### 16. sp.better-auth-ts
**Description**: Configure Better Auth for Next.js frontend. Sets up Better Auth client, JWT token handling, session management, and auth UI components.

### 17. sp.tailwind-css
**Description**: Apply Tailwind CSS styling patterns. Creates responsive layouts with Tailwind utility classes, custom color schemes, and consistent spacing/typography.

### 18. sp.shadcn
**Description**: Setup and use Shadcn UI components. Installs Shadcn CLI, adds pre-built components (Button, Card, Dialog, Form), and configures theme.

### 19. sp.frontend-types
**Description**: Define TypeScript interfaces for frontend data. Creates TypeScript types matching backend Pydantic models, ensuring type safety across API calls.

### 20. sp.react-hooks
**Description**: Create custom React hooks for reusable logic. Builds custom hooks for data fetching, form handling, authentication state, and side effects.

---

## INTEGRATION SKILLS (5)

### 21. sp.monorepo-setup
**Description**: Initialize monorepo structure for full-stack app. Creates organized folder structure with /frontend, /backend, /specs, shared docker-compose, and root-level configuration.

### 22. sp.api-contract
**Description**: Define shared API contract types between frontend/backend. Creates consistent type definitions (TypeScript + Pydantic) for request/response schemas to ensure type safety.

### 23. sp.docker-compose
**Description**: Create docker-compose configuration for local development. Configures multi-container setup with frontend, backend, and Postgres services, environment variables, and networking.

### 24. sp.env-config
**Description**: Setup environment variable configuration. Creates .env files for frontend/backend, documents all required variables, and ensures secrets are not committed.

### 25. sp.cors-setup
**Description**: Configure CORS between frontend and backend. Sets up CORS middleware in FastAPI to allow requests from Next.js frontend, configures allowed origins/methods/headers.

---

## SUMMARY

| Category | Count |
|----------|-------|
| Main Agents | 2 |
| Specialized Subagents | 9 |
| Backend Skills | 10 |
| Frontend Skills | 10 |
| Integration Skills | 5 |
| **TOTAL** | **36** |

---

**Version**: 1.0.0
**Last Updated**: 2026-01-28
**Phase**: Phase 2 - Full-Stack Web Application
