---
name: task-decomposer
description: Breaks approved specifications or plans into atomic, Claude Code–executable tasks
category: execution
input: High-level execution or implementation plan (spec.md, plan.md, or both)
output: Ordered list of atomic tasks with dependencies and execution strategy
context: Used before Claude performs any execution to convert plans into actionable work
constraints:
  - No application code generation
  - No agent definitions
  - Task decomposition and ordering only
---

## Overview

`task_decomposer` is a reusable execution skill for Hackathon II – Evolution of Todo. It converts approved specifications and technical plans into atomic, independently-executable tasks that Claude Code can complete.

**When to use**: After spec and plan are approved, before implementation begins. Use whenever you need to break large work into manageable, testable units.

**Key responsibility**: Transform "how to build it" (plan) into "exactly what to do, in what order" (tasks).

---

## Core Principles of Task Decomposition

### 1. **Atomicity: One Clear Action Per Task**

Each task must:
- Have a **single, well-defined outcome** (not "build auth system" but "create login endpoint")
- Be **independently completable** by Claude Code
- Require **no ambiguity** about what "done" means
- Produce **testable, deliverable code**

**Example**:
```
✅ ATOMIC: "Create User model with email and password fields in src/models/user.py"
❌ VAGUE: "Set up authentication"
```

### 2. **Independence: Testable in Isolation**

Each task should be:
- **Independently testable** (no requirement that previous tasks ran)
- **Demonstrable** (clear output even if others are incomplete)
- **Parallelizable** where possible (no false dependencies)

**Example**:
```
✅ INDEPENDENT: User Story 1 can be fully implemented, tested, and shown to users
                even if User Story 2 tasks haven't started
❌ DEPENDENT: "Build auth" cannot be completed without "build models" first
```

### 3. **Sequencing: Right Order, Right Dependencies**

Tasks must be ordered by:
1. **Logical prerequisites** (can't test without code to test)
2. **Blocking dependencies** (foundation must be done first)
3. **Parallelization opportunities** (independent work can run simultaneously)

**Example**:
```
T001: Create project structure (no dependencies)
  ↓ (blocks everything)
T002: Setup database schema (depends on T001)
  ↓ (blocks data tasks)
T003: [P] Create User model (depends on T002)
T004: [P] Create Task model (depends on T002)
  ↓ (both can run in parallel)
T005: Implement UserService (depends on T003)
T006: Implement TaskService (depends on T004)
```

### 4. **Specificity: Exact File Paths and Locations**

Never leave location ambiguous:

**Example**:
```
✅ SPECIFIC: "Create UserService class in src/services/user_service.py with methods: create, read, update, delete"
❌ VAGUE: "Implement user service somewhere in the codebase"
```

### 5. **Testability: Clear Success Criteria**

Each task must define:
- **What artifact is created** (file, class, function, endpoint)
- **How to verify it works** (test it, run it, call the endpoint)
- **What acceptance looks like** (specific output, behavior, or data)

**Example**:
```
✅ TESTABLE: "Create POST /api/tasks endpoint that accepts title, description,
             returns JSON with task_id, status, created_at. Error if title missing (400)"
❌ UNTESTABLE: "Build tasks API endpoint"
```

---

## Task Format & Structure

### Required Task Format

```
- [ ] [ID] [P?] [Story?] Description with exact file path
```

### Format Components

| Component | Required? | Format | Purpose |
|-----------|-----------|--------|---------|
| **Checkbox** | ✅ Always | `- [ ]` | Visual progress tracking |
| **Task ID** | ✅ Always | T001, T002, ... | Sequential execution order |
| **[P] Marker** | Optional | `[P]` only if parallelizable | Shows independent work |
| **[Story] Label** | For feature tasks | `[US1]`, `[US2]`, etc. | Maps to user story in spec |
| **Description** | ✅ Always | Action + file path | Clear, specific outcome |

### Valid Task Examples

```
✅ - [ ] T001 Create project structure per implementation plan
✅ - [ ] T005 [P] Setup database connection in src/db.py
✅ - [ ] T012 [P] [US1] Create User model in src/models/user.py
✅ - [ ] T014 [US1] Implement UserService in src/services/user_service.py
✅ - [ ] T020 [P] [US2] Create Task model in src/models/task.py
```

### Invalid Task Examples

```
❌ - [ ] Create User model (missing ID, file path)
❌ - [ ] T001 [US1] Create model (too vague, no file path)
❌ T001 [US1] Create User model (missing checkbox)
❌ - [ ] T001 Create user (missing file path)
```

---

## Task Organization by Phase

### Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize project structure and dependencies

**Includes**:
- Project scaffolding (folders, files, config)
- Dependency management (requirements, package.json)
- Tool configuration (linting, formatting, testing)
- Documentation templates
- Build/run setup

**Characteristics**:
- No application code yet
- Prerequisite for all other work
- Generally 3-5 tasks
- All must be sequential (each builds on previous)

**Example**:
```
- [ ] T001 Create project structure (src/, tests/, config/)
- [ ] T002 Initialize Python dependencies with uv
- [ ] T003 [P] Setup pytest for testing
- [ ] T004 [P] Configure linting with ruff
```

---

### Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build core infrastructure that multiple user stories depend on

**⚠️ CRITICAL**: This phase **blocks all user story work**. Nothing proceeds until complete.

**Includes**:
- Database schema and ORM setup
- Authentication/authorization framework
- API routing and middleware
- Base models and entities
- Error handling infrastructure
- Logging system
- Configuration management

**Characteristics**:
- Enables all user stories
- Some tasks can run in parallel (different systems)
- Generally 5-10 tasks
- Clear checkpoint: "Foundation ready, user stories can begin"

**Example**:
```
- [ ] T005 Setup SQLAlchemy and database connection
- [ ] T006 [P] Create base User model (needed by all stories)
- [ ] T007 [P] Create base Task model (needed by all stories)
- [ ] T008 Setup FastAPI app and CORS middleware
- [ ] T009 Implement JWT authentication middleware
- [ ] T010 Setup error handling and logging
```

**Checkpoint**: "All foundational infrastructure ready. User stories can now be implemented in parallel."

---

### Phase 3+: User Stories (Priority Order)

**Purpose**: Implement each user story independently, in priority order (P1, P2, P3, etc.)

**One phase per user story** organized as:

**Substep A: Tests (OPTIONAL - only if TDD requested)**
- Write test cases for acceptance scenarios
- Ensure tests FAIL before implementation
- Tests are marked [P] (parallelizable)

**Substep B: Models (if data involved)**
- Create entity models
- Define relationships
- Add validation logic
- Tests must pass before moving to services

**Substep C: Services/Business Logic**
- Implement core functionality
- Handles domain rules
- Depends on models being complete

**Substep D: Endpoints/UI**
- Create API endpoints or UI components
- Depends on services being complete

**Substep E: Integration & Edge Cases**
- Add validation, error handling, logging
- Handle edge cases from acceptance scenarios

**Checkpoint**: "User Story [N] is fully functional and independently testable"

**Example for User Story 1: Add Task**:
```
## Phase 3: User Story 1 - Add Task (Priority: P1)

Tests (Optional - TDD approach):
- [ ] T011 [P] [US1] Write test for add_task endpoint in tests/test_tasks.py
- [ ] T012 [P] [US1] Write test for task validation in tests/test_validation.py

Implementation:
- [ ] T013 [US1] Create Task model with title, description fields in src/models/task.py
- [ ] T014 [US1] Implement add_task in TaskService in src/services/task_service.py
- [ ] T015 [US1] Create POST /api/tasks endpoint in src/routes/tasks.py
- [ ] T016 [US1] Add error handling and validation
- [ ] T017 [US1] Add logging for add_task operations

Checkpoint: User Story 1 complete - can create tasks via API
```

---

### Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Final touches after all user stories are complete

**Includes**:
- Documentation (README, API docs)
- Performance optimization
- Security hardening
- Cleanup and refactoring
- Final integration testing
- Deployment configuration

**Characteristics**:
- Only done after all user stories work
- Polish should never change feature behavior
- Generally 3-5 tasks

**Example**:
```
- [ ] T100 Generate API documentation
- [ ] T101 [P] Add README with setup instructions
- [ ] T102 [P] Configure production database connection
- [ ] T103 Create deployment guide
```

---

## Dependency Analysis & Sequencing

### Identifying Dependencies

**Three types of dependencies**:

1. **Blocking Dependencies** (hard prerequisite)
   - Example: Can't create User model without database setup
   - Must be sequential: Foundation → Models → Services → Endpoints

2. **Shared Dependencies** (multiple tasks use same artifact)
   - Example: Multiple services depend on User model
   - Can start in parallel once User model is complete
   - Mark as [P] when possible

3. **No Dependencies** (completely independent)
   - Example: Setting up linting and formatting tools
   - Mark as [P], can run simultaneously

### Dependency Graph Pattern

```
T001: Setup project
  ↓ (hard dependency)
T002: Setup database
  ├→ T003 [P] Create User model
  │  └→ T005 UserService
  │     └→ T007 User endpoints
  │
  ├→ T004 [P] Create Task model
  │  └→ T006 TaskService
  │     └→ T008 Task endpoints
  │
  └→ T009 [P] Setup auth middleware

Result: T003, T004, T009 can all run in parallel after T002
```

### How to Read This

- **T001 → T002**: Hard dependency (sequential)
- **T003, T004 in same tier**: Parallelizable ([P])
- **T005 depends on T003**: Wait for model before service
- **T007 depends on T005**: Wait for service before endpoint

---

## Task Decomposition Workflow

### Step 1: Parse the Plan

**Input**: approved plan.md file

**Extract**:
- Tech stack (what tools/languages)
- Project structure (where things go)
- Component breakdown (what modules exist)
- Service dependencies (what calls what)
- Database/API architecture

**Output**: Understanding of "how this will be built"

---

### Step 2: Extract User Stories

**Input**: approved spec.md file

**Extract**:
- Each user story (what user can do)
- Priority levels (P1, P2, P3, etc.)
- Acceptance scenarios (how to verify)
- Key entities involved (what data)

**Output**: List of features to build, in priority order

---

### Step 3: Map Features to Architecture

**For each user story, identify**:
- What models are needed?
- What services implement the logic?
- What endpoints expose the feature?
- What data relationships matter?

**Example**:

| User Story | Models | Services | Endpoints |
|---|---|---|---|
| US1: Add Task | Task | TaskService | POST /api/tasks |
| US2: View Tasks | Task, User | TaskService, UserService | GET /api/tasks |
| US3: Delete Task | Task | TaskService | DELETE /api/tasks/{id} |

---

### Step 4: Identify Phases

**Phase 1**: Setup (project structure, tools)
**Phase 2**: Foundation (models, services both stories need)
**Phase 3**: User Story 1 (highest priority)
**Phase 4**: User Story 2 (lower priority)
**Phase 5**: Polish (documentation, deployment)

---

### Step 5: Create Task Breakdown

**For each phase**:

1. **List sequential tasks** (those with hard dependencies)
2. **Identify parallelizable work** (tasks with [P] marker)
3. **Add specific file paths** (where code goes)
4. **Define acceptance criteria** (how to verify)
5. **Create dependency comments** (which tasks must come first)

**Example**:
```
## Phase 2: Foundation

- [ ] T005 Setup SQLAlchemy in src/db.py
- [ ] T006 [P] Create User model in src/models/user.py
- [ ] T007 [P] Create Task model in src/models/task.py
         (both can run after T005)
- [ ] T008 Setup FastAPI middleware in src/app.py
         (can run parallel to T006, T007)

## Phase 3: User Story 1 - Add Task

- [ ] T010 [P] [US1] Write tests in tests/test_tasks.py
- [ ] T011 [US1] Implement add_task in src/services/task_service.py
         (depends on T007 Task model, can wait for tests)
- [ ] T012 [US1] Create POST endpoint in src/routes/tasks.py
         (depends on T011 service)
```

---

### Step 6: Validate Task Quality

**Checklist for each task**:

- [ ] Has unique, sequential ID (T001, T002...)
- [ ] Has clear description with file path
- [ ] Is atomic (one clear outcome)
- [ ] Is independently testable
- [ ] Has dependencies listed (or [P] if none)
- [ ] Story label matches spec (if user story phase)
- [ ] Acceptance criteria are clear
- [ ] No ambiguity about "done"

**Example of validating**:

```
Original: "Implement authentication"
Problems: Too vague, no file path, not atomic, unclear done criteria

Fixed: "Create JWT authentication middleware in src/middleware/auth.py
       that validates bearer tokens, extracts user_id, raises 401 if invalid"
Benefits: Specific file, clear acceptance (token validation works), testable
```

---

## Execution Strategy: How Claude Code Uses Tasks

### Task Execution Model

Claude Code executes tasks in order:

```
1. Reads task ID and description
2. Opens/creates files mentioned
3. Writes code to implement the task
4. Tests/verifies the task works
5. Commits code with task ID reference
6. Moves to next task
```

### What Makes a Task Executable

**Claude Code can execute a task if**:
- File path is clear and unambiguous
- Acceptance criteria are specific (not "looks good")
- Dependencies are complete
- No blocking prerequisite is missing
- Code required is within plan scope

**Claude Code cannot execute if**:
- Too vague ("make it better")
- References missing prerequisite tasks
- Requires decisions not in spec/plan
- Scope creeps beyond approved plan

### Example: Good vs Bad Task Breakdown

**BAD** (Claude can't execute):
```
- [ ] T005 Build the user authentication system
```
Problems:
- No file path
- Too large (not atomic)
- Unclear acceptance criteria
- Ambiguous scope

**GOOD** (Claude can execute):
```
- [ ] T005 Create User model with email, password fields in src/models/user.py
- [ ] T006 Implement hash_password and verify_password functions in src/utils/auth.py
- [ ] T007 Create JWT token generation in src/services/auth_service.py
- [ ] T008 Create POST /api/auth/signup endpoint in src/routes/auth.py
       Accepts: email, password. Returns: user_id, token, expires_at. Errors: 400 if email exists
- [ ] T009 Create POST /api/auth/login endpoint in src/routes/auth.py
       Accepts: email, password. Returns: user_id, token, expires_at. Errors: 401 if invalid
```

Benefits:
- Each task has clear file path
- Each task is atomic (one responsibility)
- Accept criteria are specific
- Tasks can be executed sequentially by Claude Code
- Each task is independently testable

---

## Parallelization Opportunities

### When Can Tasks Run in Parallel?

Tasks can run in parallel (`[P]` marker) when:
- ✅ They modify different files
- ✅ They don't depend on each other's output
- ✅ No blocking prerequisite is shared

Tasks CANNOT run in parallel when:
- ❌ One depends on output of the other
- ❌ Both modify the same file
- ❌ Both require same prerequisite not yet complete

### Parallel Execution Example

```
## Phase 2: Foundation

T005: Setup database
  ↓ (prerequisite - blocks following)

T006 [P] Create User model (src/models/user.py)
T007 [P] Create Task model (src/models/task.py)
T008 [P] Setup API routing (src/app.py)

These 3 can run in parallel (different files, no interdependencies)

  ↓ (all must complete)

T009: Create UserService (depends on T006)
T010: Create TaskService (depends on T007)

These 2 can run in parallel (depend on different models, different services)

  ↓ (both must complete)

T011 [P] Create User endpoints (depends on T009)
T012 [P] Create Task endpoints (depends on T010)

These 2 can run in parallel (depend on different services)
```

### Marking Parallelizable Tasks

```
- [ ] T006 [P] Create User model in src/models/user.py
```

The `[P]` means: "This task is independent and can run parallel to other [P] tasks."

---

## Common Task Decomposition Mistakes

### Mistake 1: Tasks Too Large

**Problem**: Task describes too much work

```
❌ T001 Build full CRUD API for tasks
```

**Fix**: Break into smaller, atomic tasks
```
✅ T005 Create Task model in src/models/task.py
✅ T006 Create TaskService in src/services/task_service.py
✅ T007 Create POST /api/tasks endpoint
✅ T008 Create GET /api/tasks endpoint
✅ T009 Create PUT /api/tasks/{id} endpoint
✅ T010 Create DELETE /api/tasks/{id} endpoint
```

---

### Mistake 2: Tasks Too Vague

**Problem**: Unclear what "done" means

```
❌ T012 Implement validation
```

**Fix**: Be specific about what to validate
```
✅ T012 Add validation to User model:
       - email must be valid format (regex)
       - password must be 8+ chars
       - Raise ValidationError if invalid
       In: src/models/user.py
```

---

### Mistake 3: Missing File Paths

**Problem**: Ambiguous where code goes

```
❌ T008 Create authentication service
```

**Fix**: Specify exact location
```
✅ T008 Create AuthService class in src/services/auth_service.py
       with methods: create_token, verify_token
```

---

### Mistake 4: False Dependencies

**Problem**: Task marked sequential when it could be parallel

```
❌ T006 Create User model
❌ T007 Create Task model (must wait for T006)
```

Issue: Task model doesn't depend on User model, but task order suggests it does.

**Fix**: Mark as parallelizable
```
✅ T006 [P] Create User model in src/models/user.py
✅ T007 [P] Create Task model in src/models/task.py
```

Both can run after T005 (foundation).

---

### Mistake 5: Not Tied to User Stories

**Problem**: Can't tell if work is user-facing

```
❌ T020 Implement validation
```

**Fix**: Link to user story
```
✅ T020 [US1] Add task title validation in src/models/task.py
       (ensures User Story 1: Add Task works correctly)
```

---

## Task Quality Checklist

Before marking a task ready for Claude Code execution:

### Task Format ✓
- [ ] Has checkbox: `- [ ]`
- [ ] Has sequential ID: T001, T002, ...
- [ ] Has description with file path
- [ ] [P] marker only if parallelizable
- [ ] [Story] label if user story phase

### Task Content ✓
- [ ] Single, clear outcome
- [ ] Specific file paths (no ambiguity)
- [ ] Independently testable
- [ ] No ambiguity about "done"
- [ ] Acceptance criteria are measurable

### Dependencies ✓
- [ ] Lists prerequisite tasks if any
- [ ] Or marked [P] if independent
- [ ] No circular dependencies
- [ ] Correct execution order

### Scope ✓
- [ ] Matches approved spec
- [ ] Matches approved plan
- [ ] No features added or removed
- [ ] Fits current phase

---

## Integration with Claude Code

### How to Present Tasks to Claude Code

**Format**: Single Markdown file (tasks.md) containing:

```markdown
# Tasks: [Feature Name]

[Overview of what will be built]

## Phase 1: Setup
- [ ] T001 ...
- [ ] T002 ...

## Phase 2: Foundation
- [ ] T005 ...
- [ ] T006 [P] ...
- [ ] T007 [P] ...

## Phase 3: User Story 1
- [ ] T010 [US1] ...
- [ ] T011 [US1] ...

## Dependency Graph
[ASCII diagram showing task order]

## Parallel Execution Opportunities
[Which tasks can run simultaneously]
```

### How Claude Code Executes Tasks

1. **Reads tasks.md** - Understands full breakdown
2. **Executes in order** - Follows task IDs sequentially
3. **References task ID** - Commits include "Task: T-005"
4. **Checks dependencies** - Won't skip prerequisites
5. **Marks complete** - Checkbox becomes ✅

---

## Example: Complete Task Breakdown

### Specification Input

```markdown
# Feature: Task Management

## User Story 1: Add Task (P1)
As a user, I can create a new task by providing a title and optional description.

## User Story 2: List Tasks (P1)
As a user, I can see all my tasks with their status.

## User Story 3: Delete Task (P2)
As a user, I can delete a task I no longer need.
```

### Plan Input

```markdown
# Architecture: Task Management

## Components
1. Task model (id, title, description, completed)
2. TaskService (CRUD operations)
3. API endpoints (POST, GET, DELETE)

## Database
PostgreSQL with SQLAlchemy ORM

## Structure
- src/models/ → Data models
- src/services/ → Business logic
- src/routes/ → API endpoints
```

### Task Decomposition Output

```markdown
# Tasks: Task Management

## Phase 1: Setup
- [ ] T001 Create project structure (src/, tests/)
- [ ] T002 Initialize Python dependencies with uv
- [ ] T003 [P] Configure pytest

## Phase 2: Foundation
- [ ] T005 Setup SQLAlchemy connection in src/db.py
- [ ] T006 Create base Task model in src/models/task.py
           Fields: id, title, description, completed, created_at
- [ ] T007 Setup FastAPI app in src/app.py
- [ ] T008 Create TaskService in src/services/task_service.py

## Phase 3: User Story 1 - Add Task (P1)
- [ ] T010 [US1] Create POST /api/tasks endpoint in src/routes/tasks.py
           Accepts: title (required), description (optional)
           Returns: task_id, title, completed, created_at
           Error: 400 if title missing

## Phase 4: User Story 2 - List Tasks (P1)
- [ ] T015 [US2] Create GET /api/tasks endpoint in src/routes/tasks.py
           Returns: Array of all tasks with status
           Query params: status (all|pending|completed)

## Phase 5: User Story 3 - Delete Task (P2)
- [ ] T020 [US3] Create DELETE /api/tasks/{id} endpoint in src/routes/tasks.py
           Returns: success message
           Error: 404 if task not found

## Phase 6: Polish
- [ ] T025 Generate API documentation
- [ ] T026 Add README with setup instructions

## Dependency Graph
T001 → T002 → T005 ─┬→ T006 → T008 → T010 → T015 → T020 → T025
                    └→ T007 ──────────────────────────────→ T026

T003 can run parallel to T002

## Parallel Execution
- T003 (configure pytest) can run parallel to T002 (dependencies)
- T006, T007, T008 can start after T005 (foundation prerequisite)
- US1, US2, US3 must follow Foundation phase, but can be prioritized
```

---

## Summary: Task Decomposer's Job

This skill helps you:

| Responsibility | What It Does |
|---|---|
| **Parse Plans** | Extract architecture, structure, components |
| **Extract Stories** | Identify user stories and priorities |
| **Map Work** | Connect features to components |
| **Sequence Tasks** | Order work by dependencies |
| **Identify Parallelization** | Mark independent work [P] |
| **Create Breakdown** | Generate phase-by-phase task list |
| **Validate Quality** | Ensure tasks are atomic, executable, specific |
| **Enable Execution** | Produce tasks.md ready for Claude Code |

**Output**: A clear, executable task list that Claude Code can follow to build the feature.

---

**Last Updated**: 2026-01-17
**Project**: Hackathon II – Evolution of Todo
**Phase**: All Phases (Execution Planning)
**Usage**: `/sp.tasks` command and task breakdown workflows

