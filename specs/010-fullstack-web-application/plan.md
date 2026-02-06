# Implementation Plan: Full-Stack Web Application

**Branch**: `010-fullstack-web-application` | **Date**: 2026-02-05 | **Spec**: [link](./spec.md)

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Modern multi-user full-stack web application with Next.js frontend, FastAPI backend, Neon PostgreSQL database, and Better Auth authentication implementing Todo functionality with JWT-based user isolation, responsive UI with Tailwind CSS and shadcn/ui, following monorepo structure with Phase-2/frontend, Phase-2/backend, and Phase-2/specs directories.

## Technical Context

**Language/Version**: Python 3.13+, TypeScript/JavaScript for Next.js, SQL for Neon PostgreSQL
**Primary Dependencies**: Next.js 16+ with App Router, FastAPI, SQLModel, Better Auth, Tailwind CSS, shadcn/ui
**Storage**: Neon Serverless PostgreSQL with SQLModel ORM
**Testing**: pytest for backend, Jest/React Testing Library for frontend
**Target Platform**: Web application for Vercel (frontend) and cloud deployment (backend)
**Project Type**: Full-stack web application
**Performance Goals**: <2 seconds API response time under normal load, 100 concurrent users support
**Constraints**: <200ms p95 latency, JWT authentication required on all endpoints, user data isolation
**Scale/Scope**: Multi-user support, 100+ concurrent users, persistent data storage

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

1. ✅ **Spec-Driven Development**: All code follows Agentic Dev Stack workflow (Spec → Plan → Tasks → Implement)
2. ✅ **Full-Stack Architecture**: Clean separation between Next.js frontend and FastAPI backend services
3. ✅ **JWT-Based Authentication**: User authentication with Better Auth JWT tokens with user isolation
4. ✅ **Persistent Data Storage**: Data stored in Neon Serverless PostgreSQL database using SQLModel ORM
5. ✅ **Clean Architecture**: Clear separation between frontend, backend, and database layers
6. ✅ **No Manual Code Generation**: Claude Code is the only entity authorized to generate code
7. ✅ **Security First**: All API endpoints require JWT tokens and enforce user isolation
8. ✅ **Quality Standards**: Type safety with TypeScript/Pydantic, responsive design, optimized performance, security measures

## Research Findings (Phase 0)

### Authentication Implementation
- **Decision**: Use Better Auth with JWT tokens for stateless authentication
- **Rationale**: Provides secure, scalable authentication without server-side sessions; works well with Next.js frontend and FastAPI backend
- **Alternatives considered**: Custom JWT implementation, OAuth providers, traditional session-based auth

### Database Connection Strategy
- **Decision**: Use Neon Serverless PostgreSQL with async connection pooling
- **Rationale**: Serverless nature scales automatically; async operations improve performance; SQLModel provides Pydantic integration
- **Alternatives considered**: Traditional PostgreSQL, MongoDB, SQLite

### API Design Pattern
- **Decision**: RESTful API with FastAPI dependency injection
- **Rationale**: FastAPI provides automatic validation, documentation, and type safety; REST is familiar and well-supported
- **Alternatives considered**: GraphQL, gRPC

### Frontend Architecture
- **Decision**: Next.js App Router with client/server components
- **Rationale**: App Router provides modern routing; server components optimize performance; client components handle interactivity
- **Alternatives considered**: Create React App, Vite, Remix

## Data Model (Phase 1)

### User Entity
- **Fields**: id (string), email (string), name (string), created_at (datetime)
- **Source**: Managed by Better Auth
- **Relationships**: One-to-many with tasks (user_id foreign key)

### Task Entity
- **Fields**:
  - id (integer, primary key)
  - user_id (string, foreign key → users.id)
  - title (string, 1-200 characters, required)
  - description (text, optional, max 1000 characters)
  - completed (boolean, default false)
  - created_at (datetime)
  - updated_at (datetime)
- **Indexes**: user_id for filtering performance
- **Validation**: Title required, length constraints, completed boolean

### State Transitions
- **Task Status**: Pending ↔ Completed (toggle via PATCH /api/{user_id}/tasks/{id}/complete)

## API Contracts (Phase 1)

### Authentication Endpoints
- **POST /api/auth/signup** - User registration with JWT token response
- **POST /api/auth/login** - User authentication with JWT token response
- **POST /api/auth/logout** - Session termination

### Task Management Endpoints
- **GET /api/{user_id}/tasks** - List all tasks for a user (requires JWT)
  - Query params: status (all/pending/completed), sort (created/title/due_date)
  - Response: Array of Task objects
- **POST /api/{user_id}/tasks** - Create a new task (requires JWT)
  - Request body: {title: string, description?: string}
  - Response: Created Task object
- **GET /api/{user_id}/tasks/{id}** - Get specific task details (requires JWT)
  - Response: Task object
- **PUT /api/{user_id}/tasks/{id}** - Update a task (requires JWT)
  - Request body: {title?: string, description?: string}
  - Response: Updated Task object
- **DELETE /api/{user_id}/tasks/{id}** - Delete a task (requires JWT)
  - Response: {status: "deleted", task_id: number}
- **PATCH /api/{user_id}/tasks/{id}/complete** - Toggle task completion (requires JWT)
  - Response: {task_id: number, completed: boolean, title: string}

### Security Requirements
- All endpoints require valid JWT token in Authorization: Bearer <token> header
- Each user only accesses their own data (filtered by user_id in URL)
- Input validation on all endpoints
- Rate limiting for abuse prevention

## Project Structure

### Documentation (this feature)

```text
specs/010-fullstack-web-application/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Web application structure
backend/
├── src/
│   ├── models/
│   │   ├── user_model.py
│   │   └── task_model.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   └── task_service.py
│   ├── api/
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   └── task_routes.py
│   └── dependencies/
│       └── auth_dependencies.py
├── requirements.txt
└── tests/

frontend/
├── src/
│   ├── components/
│   │   ├── TaskList/
│   │   ├── TaskForm/
│   │   └── Auth/
│   ├── pages/
│   │   ├── dashboard/
│   │   ├── login/
│   │   └── signup/
│   ├── services/
│   │   ├── apiClient.ts
│   │   └── authService.ts
│   └── hooks/
│       └── useAuth.ts
├── package.json
└── tests/

Phase-2/
├── frontend/          # Next.js application
├── backend/           # FastAPI application
├── specs/             # Specification files organized by type
│   ├── features/      # Feature specifications
│   ├── api/           # API specifications
│   ├── database/      # Database specifications
│   └── ui/            # UI specifications
└── docker-compose.yml # Local development environment
```

**Structure Decision**: Selected the full-stack web application structure with separate frontend and backend projects to maintain clean separation of concerns. The monorepo structure follows the Phase-2 organization with dedicated directories for frontend, backend, and specifications as required by the constitution.

## Quickstart Guide (Phase 1)

### Local Development Setup
1. Clone repository and navigate to project root
2. Install dependencies:
   ```bash
   # Backend
   cd Phase-2/backend
   uv venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   uv pip install -r requirements.txt

   # Frontend
   cd ../frontend
   npm install
   ```
3. Set up environment variables:
   ```bash
   # Create .env files in both frontend and backend
   # Configure Better Auth with JWT secret
   # Configure Neon PostgreSQL connection string
   ```
4. Start services:
   ```bash
   # Terminal 1: Start backend
   cd Phase-2/backend
   uv run uvicorn main:app --reload

   # Terminal 2: Start frontend
   cd Phase-2/frontend
   npm run dev
   ```

### Environment Configuration
- BETTER_AUTH_SECRET: JWT signing secret (same for frontend and backend)
- DATABASE_URL: Neon PostgreSQL connection string
- NEXT_PUBLIC_BETTER_AUTH_URL: Frontend auth URL
- API_BASE_URL: Backend API URL for frontend API client

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None] | [No violations detected] | [All constitution requirements satisfied] |