# Agent-Skills Mapping

## Overview
This document maps which skills each agent/subagent uses during their workflow.

---

## MAIN AGENTS

### 1. product-architect-agent
**Role**: Overall coordinator and governance

**Skills Used**:
- (Coordinates other agents, doesn't use skills directly)
- Spawns and manages all subagents
- Reviews outputs from all skills

**Workflow**:
```
User Request → product-architect-agent → Spawns appropriate subagents → Reviews outputs
```

---

### 2. fullstack-planner-agent
**Role**: Monorepo and integration planning

**Skills Used**:
1. sp.monorepo-setup
2. sp.api-contract
3. sp.docker-compose
4. sp.env-config
5. sp.cors-setup

**Workflow**:
```
1. sp.monorepo-setup (Create folder structure)
2. sp.api-contract (Define shared types)
3. sp.env-config (Setup environment variables)
4. sp.docker-compose (Configure local development)
5. sp.cors-setup (Enable frontend-backend communication)
```

**When to Use**:
- Start of Phase 2
- Setting up monorepo
- Planning integration strategy

---

## BACKEND SUBAGENTS

### 3. fastapi-backend-expert
**Role**: FastAPI application implementation

**Skills Used**:
1. sp.fastapi-setup
2. sp.backend-api-routes
3. sp.backend-error-handling
4. sp.backend-service-layer

**Workflow**:
```
1. sp.fastapi-setup (Initialize FastAPI project)
2. sp.backend-api-routes (Create CRUD endpoints)
3. sp.backend-service-layer (Add business logic)
4. sp.backend-error-handling (Add error handlers)
```

**When to Use**:
- Implementing backend API
- Creating route handlers
- Setting up FastAPI structure

---

### 4. api-design-agent
**Role**: API specification and contract design

**Skills Used**:
1. sp.backend-api-routes
2. sp.api-contract
3. sp.backend-jwt-auth

**Workflow**:
```
1. sp.api-contract (Define request/response schemas)
2. sp.backend-api-routes (Generate endpoint structure)
3. sp.backend-jwt-auth (Add authentication requirements)
```

**When to Use**:
- Before implementing endpoints
- Designing API contracts
- Planning authentication flow

---

### 5. database-schema-agent
**Role**: Database schema design

**Skills Used**:
1. sp.sqlmodel-schema
2. sp.neon-postgres

**Workflow**:
```
1. sp.sqlmodel-schema (Define table models)
2. sp.neon-postgres (Setup database connection)
```

**When to Use**:
- Designing database tables
- Creating relationships
- Setting up Neon connection

---

### 6. auth-integration-agent
**Role**: Authentication implementation across stack

**Skills Used**:
1. sp.better-auth-ts (Frontend)
2. sp.better-auth-python (Backend)
3. sp.backend-jwt-auth (Backend)
4. sp.frontend-auth (Frontend)

**Workflow**:
```
1. sp.better-auth-ts (Setup Better Auth on frontend)
2. sp.better-auth-python (Setup Better Auth on backend)
3. sp.backend-jwt-auth (Add JWT validation)
4. sp.frontend-auth (Create auth context/hooks)
```

**When to Use**:
- Implementing authentication
- Setting up JWT flow
- Creating signup/signin

---

### 7. api-security-agent
**Role**: Security review and implementation

**Skills Used**:
1. sp.backend-jwt-auth
2. sp.cors-setup
3. sp.backend-error-handling

**Workflow**:
```
1. sp.backend-jwt-auth (Verify JWT validation)
2. sp.cors-setup (Check CORS configuration)
3. sp.backend-error-handling (Review error responses)
```

**When to Use**:
- Before deployment
- Security audits
- Reviewing API security

---

### 8. backend-testing-expert
**Role**: Backend testing implementation

**Skills Used**:
1. sp.backend-testing

**Workflow**:
```
1. sp.backend-testing (Generate test suites)
2. Run pytest and verify coverage
```

**When to Use**:
- After implementing endpoints
- Before deployment
- Continuous testing

---

## FRONTEND SUBAGENTS

### 9. nextjs-frontend-expert
**Role**: Next.js application implementation

**Skills Used**:
1. sp.nextjs-setup
2. sp.nextjs-app-router
3. sp.frontend-component
4. sp.frontend-api-client
5. sp.frontend-types

**Workflow**:
```
1. sp.nextjs-setup (Initialize Next.js project)
2. sp.nextjs-app-router (Create pages/layouts)
3. sp.frontend-types (Define TypeScript types)
4. sp.frontend-component (Build UI components)
5. sp.frontend-api-client (Setup API communication)
```

**When to Use**:
- Building frontend UI
- Creating pages and layouts
- Implementing data fetching

---

### 10. ui-ux-expert
**Role**: UI design and styling

**Skills Used**:
1. sp.tailwind-css
2. sp.shadcn
3. sp.frontend-component
4. sp.react-hooks

**Workflow**:
```
1. sp.shadcn (Setup Shadcn UI components)
2. sp.frontend-component (Create styled components)
3. sp.tailwind-css (Apply responsive styling)
4. sp.react-hooks (Add interactive behavior)
```

**When to Use**:
- Designing UI layouts
- Styling components
- Ensuring responsiveness

---

### 11. deployment-expert
**Role**: Deployment configuration

**Skills Used**:
1. sp.docker-compose
2. sp.env-config

**Workflow**:
```
1. sp.env-config (Configure environment variables)
2. sp.docker-compose (Create deployment configuration)
```

**When to Use**:
- Preparing for deployment
- Setting up local environment
- Configuring production

---

## SKILLS DEPENDENCY MAP

### Backend Setup Flow
```
sp.fastapi-setup
  ↓
sp.neon-postgres
  ↓
sp.sqlmodel-schema
  ↓
sp.backend-api-routes
  ↓
sp.backend-jwt-auth
  ↓
sp.backend-service-layer
  ↓
sp.backend-error-handling
  ↓
sp.backend-query-params
  ↓
sp.backend-testing
```

### Frontend Setup Flow
```
sp.nextjs-setup
  ↓
sp.frontend-types
  ↓
sp.nextjs-app-router
  ↓
sp.shadcn
  ↓
sp.frontend-component
  ↓
sp.tailwind-css
  ↓
sp.frontend-api-client
  ↓
sp.react-hooks
```

### Authentication Flow
```
sp.better-auth-ts (Frontend)
  ↓
sp.frontend-auth (Frontend)
  ↓
sp.better-auth-python (Backend)
  ↓
sp.backend-jwt-auth (Backend)
```

### Integration Flow
```
sp.monorepo-setup
  ↓
sp.api-contract
  ↓
sp.env-config
  ↓
sp.cors-setup
  ↓
sp.docker-compose
```

---

## QUICK REFERENCE TABLE

| Agent/Subagent | Primary Skills | Skill Count |
|----------------|---------------|-------------|
| product-architect-agent | (Coordinates all) | 0 |
| fullstack-planner-agent | monorepo-setup, api-contract, docker-compose, env-config, cors-setup | 5 |
| fastapi-backend-expert | fastapi-setup, backend-api-routes, backend-error-handling, backend-service-layer | 4 |
| api-design-agent | backend-api-routes, api-contract, backend-jwt-auth | 3 |
| database-schema-agent | sqlmodel-schema, neon-postgres | 2 |
| auth-integration-agent | better-auth-ts, better-auth-python, backend-jwt-auth, frontend-auth | 4 |
| api-security-agent | backend-jwt-auth, cors-setup, backend-error-handling | 3 |
| backend-testing-expert | backend-testing | 1 |
| nextjs-frontend-expert | nextjs-setup, nextjs-app-router, frontend-component, frontend-api-client, frontend-types | 5 |
| ui-ux-expert | tailwind-css, shadcn, frontend-component, react-hooks | 4 |
| deployment-expert | docker-compose, env-config | 2 |

---

## WORKFLOW EXAMPLE: Building Task CRUD Feature

### Step 1: Planning (fullstack-planner-agent)
```
Uses: sp.api-contract
Output: Task API contract defined
```

### Step 2: Database (database-schema-agent)
```
Uses: sp.sqlmodel-schema, sp.neon-postgres
Output: Task table created in Neon DB
```

### Step 3: Backend API (fastapi-backend-expert + api-design-agent)
```
Uses: sp.backend-api-routes, sp.backend-service-layer
Output: Task CRUD endpoints implemented
```

### Step 4: Authentication (auth-integration-agent)
```
Uses: sp.backend-jwt-auth, sp.better-auth-python
Output: JWT validation on Task endpoints
```

### Step 5: Security Review (api-security-agent)
```
Uses: sp.backend-jwt-auth, sp.cors-setup
Output: Security verified, user isolation confirmed
```

### Step 6: Frontend UI (nextjs-frontend-expert + ui-ux-expert)
```
Uses: sp.frontend-component, sp.tailwind-css, sp.shadcn
Output: Task list, form, and item components
```

### Step 7: Frontend Auth (auth-integration-agent)
```
Uses: sp.better-auth-ts, sp.frontend-auth
Output: Login/signup forms, auth context
```

### Step 8: API Integration (nextjs-frontend-expert)
```
Uses: sp.frontend-api-client, sp.frontend-types
Output: Frontend connected to backend API
```

### Step 9: Testing (backend-testing-expert)
```
Uses: sp.backend-testing
Output: Test suite with >80% coverage
```

### Step 10: Deployment (deployment-expert)
```
Uses: sp.docker-compose, sp.env-config
Output: Docker setup, environment configured
```

---

## SKILLS USAGE FREQUENCY

| Skill | Used By Agents | Frequency |
|-------|----------------|-----------|
| sp.api-contract | fullstack-planner-agent, api-design-agent | High |
| sp.backend-jwt-auth | auth-integration-agent, api-security-agent, api-design-agent | High |
| sp.frontend-component | nextjs-frontend-expert, ui-ux-expert | High |
| sp.env-config | fullstack-planner-agent, deployment-expert | Medium |
| sp.docker-compose | fullstack-planner-agent, deployment-expert | Medium |
| sp.cors-setup | fullstack-planner-agent, api-security-agent | Medium |
| sp.backend-testing | backend-testing-expert | Low |
| sp.react-hooks | ui-ux-expert | Low |

---

**Version**: 1.0.0
**Last Updated**: 2026-01-28
**Purpose**: Maps agents to their skills for Phase 2 implementation
