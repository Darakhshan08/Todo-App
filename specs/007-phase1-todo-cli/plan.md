# Implementation Plan: Phase I – Advanced Interactive In-Memory Todo CLI

**Branch**: `007-phase1-todo-cli` | **Date**: 2026-01-21 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/007-phase1-todo-cli/spec.md`

## Summary

This plan translates the Phase I specification into a concrete implementation roadmap for building a production-quality, interactive, menu-driven Todo CLI application in Python. The application serves as a functional blueprint establishing WHAT the system can do (core task management, priorities, tags, search/filter, sorting, due dates, recurring tasks) using in-memory storage only, with clean architecture preparing for future phases (Web, AI, Cloud).

**Technical Approach**: Build a layered CLI application with clear separation between presentation (menu UI), domain logic (task operations), and data (in-memory store), using Python 3.13+ with UV package management. Menu-driven interface eliminates command syntax requirements while maintaining deterministic, testable behavior throughout.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external packages)
**Storage**: In-memory only (Python dict/list structures)
**Testing**: pytest for unit and integration tests
**Target Platform**: Cross-platform CLI (Windows, macOS, Linux terminal)
**Project Type**: Single application (CLI-only)
**Performance Goals**: Handle 1,000+ tasks with <2 second operations, startup <1 second
**Constraints**: No file I/O, no databases, no network, no GUI, deterministic behavior only
**Scale/Scope**: Single-user session, 10 user stories (4 P1, 4 P2, 2 P3), 56 functional requirements

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Compliance Status: PASS

| Principle | Requirement | Implementation Approach | Status |
|-----------|-------------|------------------------|--------|
| I. Spec-Driven Development | Spec → Plan → Tasks → Implement | Complete spec approved, this plan defines implementation roadmap | ✅ PASS |
| II. Deterministic Behavior Only | No randomness, no AI, no LLM | All logic is deterministic; recurring task generation uses date arithmetic only | ✅ PASS |
| III. CLI-First Interface | Console text-in/text-out only | Interactive menu system, no GUI frameworks | ✅ PASS |
| IV. In-Memory Storage Only | No files, databases, persistence | Python dict/list structures, data lost on exit | ✅ PASS |
| V. Clean Architecture | Separation of concerns, reusability | Layered architecture: UI → Services → Models → Store | ✅ PASS |
| VI. No Manual Code | Claude Code generates all code | Plan-driven code generation via `/sp.tasks` → `/sp.implement` | ✅ PASS |

### Technology Stack Alignment

- ✅ UV package manager for dependency management
- ✅ Python 3.13+ runtime
- ✅ Spec-Kit Plus workflow (Spec → Plan → Tasks → Implement)

### Scope Boundary Compliance

**In Scope (Permitted)**:
- ✅ In-memory data storage (Python data structures)
- ✅ Console-based CLI interaction
- ✅ Core Todo functionality (add, view, update, delete, complete/incomplete)
- ✅ Task identification via unique IDs
- ✅ Clear status display

**Constitution Extensions (Specification-Approved)**:
- ✅ Task priorities (High, Medium, Low) - Specification FR-011 to FR-014
- ✅ Tags/categories - Specification FR-015 to FR-018
- ✅ Search and filter - Specification FR-019 to FR-023
- ✅ Due dates - Specification FR-028 to FR-031
- ✅ Sorting - Specification FR-024 to FR-027
- ✅ Recurring tasks (session-scoped) - Specification FR-032 to FR-037

**Note**: These features were explicitly included in the approved specification for Phase I and do not violate the constitution, which permits "Basic Level" features. The specification defines an "Advanced Interactive" Phase I scope that extends beyond minimal Basic Level while respecting all Phase I constraints (no persistence, no network, no AI, CLI-only).

**Out of Scope (Forbidden)**:
- ❌ Databases, file persistence
- ❌ Web frameworks, REST APIs
- ❌ UI frameworks (web, desktop, mobile)
- ❌ AI, LLMs, intelligent features
- ❌ Cloud infrastructure
- ❌ Authentication/authorization
- ❌ Background schedulers (recurring tasks are session-only simulation)

## Architecture Overview

### High-Level Component Layout

```text
┌─────────────────────────────────────────────────────────────┐
│                     CLI Application                          │
│                  (main.py entry point)                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  Presentation Layer                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Menu UI (menu_controller.py)                        │   │
│  │  - Main menu navigation                              │   │
│  │  - Sub-menu flows (add, update, search, sort)       │   │
│  │  - Input prompts and validation UI                  │   │
│  │  - Output formatting and display                    │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                     Service Layer                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Task Service (task_service.py)                      │   │
│  │  - create_task(), update_task(), delete_task()       │   │
│  │  - complete_task(), incomplete_task()                │   │
│  │  - get_task(), get_all_tasks()                       │   │
│  │  - search_tasks(), filter_tasks(), sort_tasks()      │   │
│  │  - handle_recurring_completion()                     │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Validation Service (validation_service.py)          │   │
│  │  - validate_title(), validate_date()                 │   │
│  │  - validate_priority(), validate_tags()              │   │
│  │  - validate_recurrence()                             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      Domain Layer                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Task Model (models/task.py)                         │   │
│  │  - Task dataclass                                    │   │
│  │  - Priority enum                                     │   │
│  │  - RecurrenceRule enum                               │   │
│  │  - Task state behavior (is_overdue(), format())      │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Task Store (store/task_store.py)                    │   │
│  │  - In-memory dict: {task_id: Task}                   │   │
│  │  - ID counter management                             │   │
│  │  - CRUD operations                                   │   │
│  │  - View state (filters, sort order)                  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Separation of Concerns

**Presentation Layer (UI)**:
- Handles all terminal I/O
- Displays menus and prompts
- Formats task output with visual indicators
- Captures and validates user input at UI level (format checking)
- No business logic; delegates all operations to services

**Service Layer (Business Logic)**:
- Implements all business rules and workflows
- Orchestrates task operations (create, update, delete, complete)
- Handles recurring task generation logic
- Implements search, filter, and sort algorithms
- Validates business rules (e.g., task ID exists, date is valid)
- Calls validation service for input validation

**Domain Layer (Models)**:
- Defines Task entity with all attributes
- Defines enums (Priority, RecurrenceRule)
- Provides task-level behavior (is_overdue check, formatting)
- No dependencies on UI or services

**Data Layer (Storage)**:
- Manages in-memory task collection
- Handles ID generation and uniqueness
- Provides CRUD interface
- Maintains view state (current filters, sort order)
- No business logic

### Advanced Features Integration (Without Persistence/Background Services)

**Priority System**:
- Stored as enum attribute on Task model
- Default assignment in create_task service method
- Visual display handled in UI formatting
- Sorting by priority uses enum ordering

**Tags/Categories**:
- Stored as list[str] on Task model
- Normalization (lowercase) in validation service
- Filter by tag uses list membership check
- Display formatting adds # prefix in UI layer

**Due Dates**:
- Stored as optional date attribute on Task model
- Overdue calculation in task.is_overdue() method (compares to datetime.now())
- No background checks; calculated on-demand during display
- Visual indicator (⚠ OVERDUE) added in UI formatting

**Recurring Tasks**:
- Recurrence rule stored as optional enum on Task model
- On completion, service layer checks recurrence rule
- If recurring: creates new task with calculated next due date (+1 day/+7 days/+1 month)
- Original task marked complete, new task added to store
- No background scheduler; triggered synchronously on complete_task action
- State lost on session end (complies with Phase I constraints)

**Search/Filter/Sort**:
- Search: keyword match across title/description (case-insensitive)
- Filter: predicate functions in service layer (status, priority, tag)
- Sort: custom comparator functions, return new sorted list (non-destructive)
- View state (active filters, sort order) stored in TaskStore but not applied to underlying collection

## CLI Interaction Flow Design

### Application Lifecycle

```text
START
  ↓
┌─────────────────────────────┐
│ Initialize TaskStore        │
│ (empty in-memory dict)      │
└─────────────────────────────┘
  ↓
┌─────────────────────────────┐
│ Display Welcome Message     │
└─────────────────────────────┘
  ↓
┌─────────────────────────────┐
│ MAIN MENU LOOP              │ ←──────┐
│ (loop until exit selected)  │        │
└─────────────────────────────┘        │
  ↓                                     │
[User selects menu option]              │
  ↓                                     │
┌─────────────────────────────┐        │
│ Execute Action Workflow     │        │
│ (add/view/update/delete/    │        │
│  complete/search/filter/    │        │
│  sort/exit)                 │        │
└─────────────────────────────┘        │
  ↓                                     │
[Action completes]                      │
  ↓                                     │
┌─────────────────────────────┐        │
│ Display Result/Feedback     │        │
└─────────────────────────────┘        │
  ↓                                     │
[Return to main menu] ─────────────────┘
  ↓
[Exit selected]
  ↓
┌─────────────────────────────┐
│ Display Farewell Message    │
└─────────────────────────────┘
  ↓
END (data lost)
```

### Menu Hierarchy and Navigation Structure

**Main Menu**:
```text
═══════════════════════════════════════
   TODO APPLICATION - MAIN MENU
═══════════════════════════════════════

1. Add New Task
2. View All Tasks
3. View Task Details
4. Update Task
5. Delete Task
6. Mark Task Complete/Incomplete
7. Search Tasks
8. Filter Tasks
9. Sort Tasks
10. Clear Filters/Sort
0. Exit

Select an option (0-10):
```

**Sub-Menus**:

*Add Task Flow*:
```text
ADD NEW TASK
────────────
Enter task title (required): [input]
Enter description (optional, press Enter to skip): [input]
Select priority (1=High, 2=Medium, 3=Low) [default: 2]: [input]
Enter tags (comma-separated, optional): [input]
Enter due date (YYYY-MM-DD, optional): [input]
Recurrence (1=None, 2=Daily, 3=Weekly, 4=Monthly) [default: 1]: [input]

✓ Task created successfully! (ID: 1)
```

*Update Task Flow*:
```text
UPDATE TASK
───────────
Enter task ID: [input]

Current Task Details:
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: [ ] Pending
Priority: (MED)
Tags: #shopping #home
Due Date: 2026-01-25
Recurrence: Weekly

What would you like to update?
1. Title
2. Description
3. Priority
4. Tags
5. Due Date
6. Recurrence
0. Cancel

Select option: [input]
```

*Filter Tasks Menu*:
```text
FILTER TASKS
────────────
1. Filter by Status (completed/pending)
2. Filter by Priority (high/medium/low)
3. Filter by Tag
0. Cancel

Select filter type: [input]

[If status selected]
Select status: 1=Pending, 2=Completed: [input]

[If priority selected]
Select priority: 1=High, 2=Medium, 3=Low: [input]

[If tag selected]
Enter tag name: [input]
```

*Sort Tasks Menu*:
```text
SORT TASKS
──────────
1. Sort by Due Date
2. Sort by Priority
3. Sort Alphabetically (A-Z)
4. Reset to Default Order
0. Cancel

Select sort option: [input]
```

### User Journey Mapping

**Core Workflows (P1 Features)**:

*Journey 1: Add Task → View → Complete*
```text
User Action → System Response

[Main Menu] Select 1 (Add Task)
  → Display add task prompts
[Add Task] Enter "Buy groceries"
  → Prompt for description
[Add Task] Enter "Milk, eggs, bread"
  → Prompt for priority (default: Medium)
[Add Task] Press Enter (accept default)
  → Prompt for tags
[Add Task] Enter "shopping, home"
  → Prompt for due date
[Add Task] Press Enter (skip)
  → Prompt for recurrence
[Add Task] Press Enter (accept default: None)
  → Create task, display success message
  → Return to main menu

[Main Menu] Select 2 (View All Tasks)
  → Display task list:
     1. [ ] Buy groceries (MED) #shopping #home
  → Return to main menu

[Main Menu] Select 6 (Mark Complete)
  → Prompt for task ID
[Complete] Enter "1"
  → Mark task complete
  → Display success message
  → Return to main menu

[Main Menu] Select 2 (View All Tasks)
  → Display updated list:
     1. [✓] Buy groceries (MED) #shopping #home
  → Return to main menu
```

*Journey 2: Update Task*
```text
[Main Menu] Select 4 (Update Task)
  → Prompt for task ID
[Update] Enter "1"
  → Display current task details
  → Display update menu
[Update Menu] Select 1 (Title)
  → Prompt for new title
[Update Title] Enter "Buy weekly groceries"
  → Update title
  → Display success message
  → Return to main menu
```

*Journey 3: Delete Task*
```text
[Main Menu] Select 5 (Delete Task)
  → Prompt for task ID
[Delete] Enter "1"
  → Display task details
  → Prompt for confirmation: "Delete this task? (y/n)"
[Confirm] Enter "n"
  → Display cancellation message
  → Return to main menu

[Main Menu] Select 5 (Delete Task)
[Delete] Enter "1"
[Confirm] Enter "y"
  → Delete task
  → Display success message
  → Return to main menu
```

**Intermediate Workflows (P2 Features)**:

*Journey 4: Search Tasks*
```text
[Main Menu] Select 7 (Search Tasks)
  → Prompt for keyword
[Search] Enter "meeting"
  → Search title and description for "meeting"
  → Display matching tasks:
     3. [ ] Team meeting (HIGH) #work
     5. [ ] Prepare meeting notes (MED) #work
  → Display "(2 tasks found)"
  → Return to main menu
```

*Journey 5: Filter by Priority + Sort*
```text
[Main Menu] Select 8 (Filter Tasks)
  → Display filter menu
[Filter Menu] Select 2 (Priority)
  → Prompt for priority
[Priority] Enter "1" (High)
  → Apply filter
  → Display high-priority tasks only
  → Return to main menu

[Main Menu] Select 9 (Sort Tasks)
  → Display sort menu
[Sort Menu] Select 1 (Due Date)
  → Sort filtered tasks by due date
  → Display sorted, filtered tasks
  → Return to main menu

[Main Menu] Select 10 (Clear Filters)
  → Clear filter and sort
  → Display "Filters and sorting cleared"
  → Return to main menu
```

**Advanced Workflows (P3 Features)**:

*Journey 6: Recurring Task Automation*
```text
[Main Menu] Select 1 (Add Task)
[Add] Title: "Daily standup"
[Add] Description: "Morning team sync"
[Add] Priority: 1 (High)
[Add] Tags: "work, meetings"
[Add] Due Date: "2026-01-22"
[Add] Recurrence: 2 (Daily)
  → Create recurring task
  → Return to main menu

[Main Menu] Select 2 (View Tasks)
  → Display:
     6. [ ] Daily standup (HIGH) #work #meetings | Due: 2026-01-22 (Daily)

[Main Menu] Select 6 (Mark Complete)
[Complete] Enter "6"
  → Mark task 6 complete
  → Auto-create new task with ID 7:
     - Title: "Daily standup"
     - Description: "Morning team sync"
     - Priority: High
     - Tags: work, meetings
     - Due Date: 2026-01-23 (tomorrow)
     - Recurrence: Daily
     - Status: Pending
  → Display: "Task 6 completed. New recurring task created (ID: 7)"
  → Return to main menu

[Main Menu] Select 2 (View Tasks)
  → Display:
     6. [✓] Daily standup (HIGH) #work #meetings | Due: 2026-01-22 (Daily)
     7. [ ] Daily standup (HIGH) #work #meetings | Due: 2026-01-23 (Daily)
```

*Journey 7: Overdue Tasks*
```text
[Assume today is 2026-01-25]

[Main Menu] Select 2 (View Tasks)
  → Display:
     8. [ ] ⚠ OVERDUE Submit report (HIGH) #work | Due: 2026-01-20
     9. [ ] Review code (MED) #work | Due: 2026-01-26
```

## Feature Phasing Strategy

### Phase I Internal Sequencing

The implementation will follow three internal phases within Phase I, aligned with specification priority levels (P1, P2, P3):

**Phase I.A – Core (Basic Level)** [P1 Features]:
- User Story 1: Basic Task Management (add, view, complete/incomplete)
- User Story 2: Task Details and Updates (descriptions, editing)
- User Story 3: Task Deletion with Safety (confirmation prompts)
- User Story 10: Graceful Application Lifecycle (validation, error handling, exit)

**Deliverable**: Minimal viable todo CLI with core CRUD operations and robust error handling.

**Phase I.B – Organization (Intermediate Level)** [P2 Features]:
- User Story 4: Priority Management (High, Medium, Low with visual indicators)
- User Story 5: Tag-Based Organization (multiple tags, case-insensitive)
- User Story 6: Search and Filter (keyword, status, priority, tag)
- User Story 7: Sort Task List (due date, priority, alphabetical)

**Deliverable**: Enhanced todo CLI with organizational features for managing many tasks.

**Phase I.C – Intelligence Simulation (Advanced Level)** [P3 Features]:
- User Story 8: Due Date Management (optional dates, overdue indicators)
- User Story 9: Recurring Task Automation (daily, weekly, monthly with auto-generation)

**Deliverable**: Full-featured Phase I CLI with time-aware and recurring task capabilities (session-scoped).

### Why This Order Minimizes Risk and Rework

1. **Foundation First**: Phase I.A establishes data model, service layer, and UI patterns. All subsequent phases build on this foundation without structural changes.

2. **Incremental Complexity**: Each phase adds one layer of complexity:
   - I.A: Basic fields (title, description, completed)
   - I.B: Additional fields (priority, tags) + query operations
   - I.C: Temporal logic (due dates, recurrence) + automation

3. **Independent Testing**: Each phase delivers independently testable functionality. If time constraints arise, earlier phases remain functional.

4. **Reduced Rework**:
   - Task model designed upfront to accommodate all fields (priority, tags, due_date, recurrence_rule)
   - Service layer methods designed for extensibility (add filters as parameters)
   - UI formatting designed with placeholders for optional fields

5. **Risk Mitigation**:
   - Highest risk (data model, core CRUD) tackled first when time is abundant
   - Medium risk (search/filter algorithms) in middle phase
   - Lowest risk (date calculations, recurrence logic) in final phase
   - If Phase I.C must be deferred, I.A + I.B still deliver significant value

6. **Constitutional Compliance**: Each phase fully respects Phase I constraints (in-memory, CLI-only, deterministic). No architectural pivots required between phases.

## Data & State Model (Conceptual)

### In-Memory Task Lifecycle

```text
Task Creation:
  ↓
┌─────────────────────────────────────┐
│ User provides title (required)      │
│ + optional fields (description,     │
│   priority, tags, due_date,         │
│   recurrence_rule)                  │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Validation Service validates inputs │
│ - Title: non-empty                  │
│ - Priority: valid enum              │
│ - Tags: normalized to lowercase     │
│ - Due Date: valid YYYY-MM-DD format │
│ - Recurrence: valid enum            │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Task Service generates unique ID    │
│ ID = current_counter + 1            │
│ (counter never decrements)          │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Create Task instance                │
│ - id: unique integer                │
│ - title: str                        │
│ - description: str | None           │
│ - completed: False (default)        │
│ - priority: Priority enum (default) │
│ - tags: list[str]                   │
│ - due_date: date | None             │
│ - recurrence_rule: Recurrence | None│
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ TaskStore.add(task)                 │
│ tasks[task.id] = task               │
└─────────────────────────────────────┘
  ↓
[Task exists in memory, available for operations]

Task Update:
  ↓
┌─────────────────────────────────────┐
│ User provides task ID + field       │
│ to update + new value               │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ TaskStore.get(task_id)              │
│ Retrieve existing Task instance     │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Validation Service validates new    │
│ value                               │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Mutate Task instance field          │
│ task.title = new_title (etc.)       │
└─────────────────────────────────────┘
  ↓
[No separate store operation needed; task mutated in-place]

Task Completion (Non-Recurring):
  ↓
┌─────────────────────────────────────┐
│ User provides task ID               │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ TaskStore.get(task_id)              │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Set task.completed = True           │
└─────────────────────────────────────┘
  ↓
[Task remains in store with completed=True]

Task Completion (Recurring):
  ↓
[Same as non-recurring through completion]
  ↓
┌─────────────────────────────────────┐
│ Check task.recurrence_rule          │
│ IF not None:                        │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Calculate next due date:            │
│ - Daily: due_date + 1 day           │
│ - Weekly: due_date + 7 days         │
│ - Monthly: due_date + 1 month       │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Create new Task instance:           │
│ - id: new unique ID                 │
│ - title: same                       │
│ - description: same                 │
│ - completed: False                  │
│ - priority: same                    │
│ - tags: copy of list                │
│ - due_date: calculated new date     │
│ - recurrence_rule: same             │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ TaskStore.add(new_task)             │
└─────────────────────────────────────┘
  ↓
[Original task completed, new task pending in store]

Task Deletion:
  ↓
┌─────────────────────────────────────┐
│ User provides task ID               │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ TaskStore.get(task_id)              │
│ Display task for confirmation       │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Prompt user: "Confirm delete? (y/n)"│
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ IF user confirms:                   │
│   TaskStore.delete(task_id)         │
│   del tasks[task_id]                │
└─────────────────────────────────────┘
  ↓
[Task permanently removed from session; ID never reused]

Application Exit:
  ↓
┌─────────────────────────────────────┐
│ User selects Exit from main menu    │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Display farewell message            │
└─────────────────────────────────────┘
  ↓
┌─────────────────────────────────────┐
│ Python process terminates           │
└─────────────────────────────────────┘
  ↓
[All task data lost; TaskStore garbage collected]
```

### Task Identity Stability Rules

1. **Unique ID Generation**:
   - IDs are sequential integers starting from 1
   - TaskStore maintains a `next_id` counter initialized to 1
   - On task creation: `task.id = next_id; next_id += 1`
   - Counter increments on every creation (never decrements)

2. **ID Immutability**:
   - Once assigned, task ID never changes
   - ID is read-only property of Task model

3. **ID Never Reused**:
   - When task is deleted, its ID is retired permanently for the session
   - Example: Tasks 1, 2, 3 exist. Delete 2. Next task created is 4, not 2.
   - Rationale: Prevents user confusion if they reference old task IDs

4. **ID Persistence Across Operations**:
   - Task ID remains stable through:
     - Updates (title, description, priority, tags, due date, recurrence)
     - Completion/incompletion
     - Filtering/sorting (ID used to track task identity in filtered views)

5. **Recurring Task ID Assignment**:
   - Original recurring task keeps its ID when completed
   - New recurring instance gets new ID from counter
   - Example: Task 5 (recurring daily) completed → remains as Task 5 (completed), new Task 6 created (pending)

### Handling Recurrence Generation Within Session

**Trigger**: User marks a recurring task as complete

**Recurrence Generation Algorithm**:
```python
def handle_recurring_completion(task_id: int) -> None:
    """Handle completion of recurring task and generate next instance."""
    task = task_store.get(task_id)

    # Mark original as complete
    task.completed = True

    # Check if recurring
    if task.recurrence_rule is None or task.recurrence_rule == RecurrenceRule.NONE:
        return  # Not recurring, exit

    # Calculate next due date
    if task.due_date is None:
        # No due date, use today as base
        next_due = date.today()
    else:
        next_due = task.due_date

    if task.recurrence_rule == RecurrenceRule.DAILY:
        next_due = next_due + timedelta(days=1)
    elif task.recurrence_rule == RecurrenceRule.WEEKLY:
        next_due = next_due + timedelta(weeks=1)
    elif task.recurrence_rule == RecurrenceRule.MONTHLY:
        # Add 1 month (handle month boundaries)
        next_due = next_due + relativedelta(months=1)

    # Create new task instance
    new_task = Task(
        id=task_store.get_next_id(),
        title=task.title,
        description=task.description,
        completed=False,  # New instance starts pending
        priority=task.priority,
        tags=task.tags.copy(),  # Copy list to avoid shared reference
        due_date=next_due,
        recurrence_rule=task.recurrence_rule
    )

    # Add to store
    task_store.add(new_task)

    return new_task.id  # Return new task ID for display
```

**Edge Cases**:
- **No Due Date**: If recurring task has no due date, use current date as base for next occurrence
- **Midnight Completion**: Use completion timestamp to avoid ambiguity (not relevant for daily+ recurrence)
- **Monthly Boundary**: Use `dateutil.relativedelta` to handle month-end dates (e.g., Jan 31 → Feb 28)

**Session-Only Constraint**:
- Recurring behavior only persists within current session
- On application restart, all tasks (including recurring ones) are lost
- No state file or configuration persists recurrence schedules

### View-Only Sorting vs Stored Order

**Stored Order (Default)**:
- Tasks stored in `task_store.tasks` dict (unordered by nature of dict)
- When displayed without sorting: return `list(tasks.values())` (insertion order in Python 3.7+)
- This is the "creation order" (order tasks were added)

**View-Only Sorting (Non-Destructive)**:
```python
def get_tasks_sorted(sort_by: SortOption) -> list[Task]:
    """Return sorted view of tasks without modifying store."""
    tasks = list(task_store.get_all())  # Get all tasks as list

    if sort_by == SortOption.DUE_DATE:
        # Sort by due date, overdue first, then chronological
        tasks.sort(key=lambda t: (
            t.due_date is None,  # None values last
            t.due_date if t.due_date else date.max,
            t.is_overdue()  # Overdue first within same date
        ))
    elif sort_by == SortOption.PRIORITY:
        # Sort by priority enum value (HIGH=1, MED=2, LOW=3)
        tasks.sort(key=lambda t: t.priority.value)
    elif sort_by == SortOption.ALPHABETICAL:
        # Sort by title, case-insensitive
        tasks.sort(key=lambda t: t.title.lower())
    elif sort_by == SortOption.DEFAULT:
        # Return in creation order (no sorting)
        pass

    return tasks
```

**View State Management**:
- TaskStore maintains `current_sort: SortOption` attribute
- When user selects sort option, update `current_sort`
- All subsequent "View Tasks" operations use `get_tasks_sorted(current_sort)`
- "Clear Filters/Sort" resets `current_sort = SortOption.DEFAULT`
- Underlying `tasks` dict never reordered

**Why Non-Destructive**:
- Preserves creation order as default view
- Allows user to experiment with different sort orders without losing original order
- Simplifies implementation (no need to track "original order" separately)
- Aligns with filter model (filters are also non-destructive views)

## Validation & Quality Strategy

### Input Validation Approach

**Layered Validation**:

1. **UI Layer Validation** (menu_controller.py):
   - Format checking (e.g., date matches YYYY-MM-DD pattern)
   - Type conversion (e.g., menu choice is integer)
   - Empty input detection for required fields
   - Re-prompting on invalid input
   - **Goal**: Catch obvious errors before service layer

2. **Service Layer Validation** (validation_service.py):
   - Business rule validation (e.g., task ID exists)
   - Semantic validation (e.g., due date is valid calendar date)
   - Normalization (e.g., tags to lowercase)
   - **Goal**: Enforce business rules and data integrity

**Validation Rules by Field**:

**Title**:
- UI: Non-empty check, re-prompt if empty
- Service: Length check (1-200 characters), strip whitespace
- Error: "Title cannot be empty" / "Title too long (max 200 characters)"

**Description**:
- UI: Optional, accept empty string
- Service: Length check (0-2000 characters)
- Error: "Description too long (max 2000 characters)"

**Due Date**:
- UI: Optional, accept empty string or YYYY-MM-DD format
- Service: Parse date string, validate calendar date (e.g., no Feb 30), allow past dates
- Error: "Invalid date format. Use YYYY-MM-DD" / "Invalid date"

**Priority**:
- UI: Prompt with numbered options (1=High, 2=Medium, 3=Low), default to 2
- Service: Validate enum value (HIGH, MEDIUM, LOW)
- Error: "Invalid priority. Choose 1, 2, or 3"

**Tags**:
- UI: Optional, accept comma/space-separated string
- Service: Split on comma/space, normalize to lowercase, remove duplicates, strip whitespace
- Error: None (tags are always valid after normalization)

**Recurrence Rule**:
- UI: Prompt with numbered options (1=None, 2=Daily, 3=Weekly, 4=Monthly), default to 1
- Service: Validate enum value (NONE, DAILY, WEEKLY, MONTHLY)
- Error: "Invalid recurrence. Choose 1, 2, 3, or 4"

**Task ID**:
- UI: Prompt for integer, validate integer format
- Service: Check task exists in store
- Error: "Invalid task ID. Enter a number" / "Task not found (ID: X)"

### Error-Handling Philosophy

**Principles**:
1. **Fail Gracefully**: Never crash or display stack traces to user
2. **Clear Messages**: Error messages explain what went wrong and how to fix it
3. **Immediate Feedback**: Validation errors caught at input time, before operation
4. **Recovery**: User always returns to menu after error, can retry operation
5. **No Silent Failures**: Every error generates user-visible feedback

**Error Categories**:

**User Input Errors** (expected, recoverable):
- Invalid format (e.g., "abc" when integer expected)
- Empty required field
- Out-of-range value (e.g., task ID doesn't exist)
- Invalid date (e.g., "2026-13-45")
- **Handling**: Display clear error message, re-prompt, allow retry

**Business Rule Violations** (expected, recoverable):
- Attempt to delete non-existent task
- Attempt to update non-existent task
- **Handling**: Display "Task not found" message, return to menu

**Unexpected Errors** (unexpected, recoverable):
- Exception during task creation (e.g., memory full)
- Exception during date calculation (e.g., overflow)
- **Handling**: Catch exception, display generic message ("An error occurred. Please try again."), log to stderr (for debugging), return to menu

**Fatal Errors** (unexpected, non-recoverable):
- Python runtime errors (e.g., out of memory, keyboard interrupt)
- **Handling**: Allow Python to handle (display error, exit process)

**Error Message Format**:
```text
❌ ERROR: [Clear description of problem]
   [Optional: Suggestion for correction]

Example:
❌ ERROR: Invalid date format
   Please enter date in YYYY-MM-DD format (e.g., 2026-01-25)

❌ ERROR: Task not found (ID: 99)
   Use "View Tasks" to see available task IDs

❌ ERROR: Title cannot be empty
   Please provide a task title
```

### Deterministic Behavior Guarantees

**No Randomness**:
- All behavior is fully deterministic
- No random number generation
- No UUID generation (use sequential IDs)
- No random sampling or shuffling

**No External State Dependencies**:
- No environment variable reads (except Python version check at startup)
- No file reads/writes
- No network calls
- No subprocess execution

**Time-Based Logic** (deterministic but time-dependent):
- Due date calculations: Use `datetime.date.today()` for current date
- Overdue check: Compare `task.due_date < date.today()`
- Recurrence calculation: Arithmetic on dates (deterministic given inputs)
- **Note**: Results vary by current date, but logic is deterministic

**Consistent Ordering**:
- Default task order: Creation order (stable)
- Sorted order: Deterministic comparison functions
- Filtered results: Deterministic predicate functions
- No random ordering or tie-breaking

**Idempotent Operations**:
- Same input always produces same output
- Example: Completing task ID 5 twice has same effect as completing once (second attempt is no-op)
- Example: Deleting non-existent task always displays same error

**Testability**:
- All functions are pure (no hidden side effects) or clearly stateful (TaskStore mutations)
- Date dependencies injectable (can pass `current_date` for testing)
- Output formatting functions deterministic (given same task, produce same string)

### UX Consistency Rules

**Visual Indicators**:
- Task status: `[ ]` = Pending, `[✓]` = Completed (consistent across all views)
- Priority: `(HIGH)`, `(MED)`, `(LOW)` (consistent formatting)
- Tags: `#tag1 #tag2` (always prefixed with #)
- Overdue: `⚠ OVERDUE` (always at start of line)
- Recurrence: `(Daily)`, `(Weekly)`, `(Monthly)` (in parentheses after due date)

**Spacing and Separators**:
- Menu title: Underlined with `═══` characters
- Section separator: `────` line
- List items: Left-aligned with consistent indentation
- Field labels: Right-padded to align values
- Blank line before/after menus for readability

**Prompt Conventions**:
- Required fields: "Enter [field] (required):"
- Optional fields: "Enter [field] (optional, press Enter to skip):"
- Default values: "[default: X]"
- Confirmation prompts: "Confirm? (y/n):"
- Menu selections: "Select an option (X-Y):"

**Feedback Messages**:
- Success: Prefixed with `✓` (e.g., "✓ Task created successfully!")
- Error: Prefixed with `❌ ERROR:` (see error handling above)
- Info: Prefixed with `ℹ` (e.g., "ℹ No tasks found")
- Warning: Prefixed with `⚠` (e.g., "⚠ Data will be lost on exit")

**Terminology Consistency**:
- Task (not Todo, Item, Entry)
- Complete/Incomplete (not Done/Undone, Finished/Unfinished)
- Title (not Name, Subject)
- Description (not Details, Notes)
- Tag (not Category, Label)
- Due Date (not Deadline, Target Date)

**Navigation Consistency**:
- All operations return to main menu
- Main menu always displays after operation
- 0 = Cancel/Exit in sub-menus
- 0 = Exit application in main menu
- No nested menus beyond 1 level

## Decisions & Tradeoffs

### Menu-Driven UI vs Command-Based CLI

**Decision**: Menu-driven UI

**Rationale**:
- **Specification Requirement**: FR-002, FR-009, SC-009 explicitly require menu-driven interface
- **User Experience**: Guided prompts eliminate need to learn command syntax
- **Discoverability**: All options visible in menu, no hidden commands
- **Error Prevention**: Validation at each prompt prevents malformed commands

**Tradeoffs**:
- ✅ Pro: Beginner-friendly, zero learning curve
- ✅ Pro: Consistent UX (every option is a menu choice)
- ✅ Pro: Easy to extend (add new menu options)
- ❌ Con: More keystrokes for power users (no shortcuts like `add "Buy milk"`)
- ❌ Con: Slower for batch operations (must navigate menu per task)

**Alternative Considered**: Command-based CLI (e.g., `todo add "Buy milk"`)
- Rejected: Violates specification requirement SC-009 ("Users can perform all operations through menu navigation without typing commands or remembering syntax")
- Would require: Command parser, help system, argument validation
- Would benefit: Power users, scriptability
- **Final Call**: Menu-driven UI aligns with Phase I "beginner-friendly" goal

### Simulated Advanced Features vs Real Schedulers

**Decision**: Simulate advanced features (due dates, recurrence) within session scope, no background schedulers

**Rationale**:
- **Constitution Constraint**: FR-054 forbids background schedulers
- **Phase I Constraint**: FR-037 requires recurrence behavior is session-only
- **Determinism**: Constitution Principle II requires deterministic behavior (no async processes)
- **Simplicity**: Background schedulers require threading, process management, error handling complexity

**Tradeoffs**:
- ✅ Pro: Simple implementation (synchronous logic only)
- ✅ Pro: Deterministic behavior (no race conditions, timing issues)
- ✅ Pro: Aligns with in-memory constraint (no scheduler state persistence)
- ✅ Pro: Demonstrates feature capability for Phase II (proves concept works)
- ❌ Con: Recurring tasks only generate on user action (marking complete), not automatically
- ❌ Con: Due date notifications require user to view task list (no proactive alerts)
- ❌ Con: Data lost on exit (but acceptable for Phase I)

**How Simulation Works**:
- **Due Dates**: Calculated on-demand during display (overdue check runs when list is viewed)
- **Recurrence**: Triggered synchronously when user marks task complete (new instance created immediately)
- **Session Scope**: All tasks (including recurring) lost on exit

**Alternative Considered**: Background scheduler (e.g., threading, cron-like system)
- Rejected: Violates constitution (FR-054, Principle II)
- Would require: Thread management, timer system, state persistence
- Would benefit: Proactive notifications, automatic recurrence generation
- **Final Call**: Simulation meets specification requirements while respecting Phase I constraints

### Why No Persistence Enforced in Phase I

**Decision**: Strictly enforce in-memory storage, no persistence (FR-046, FR-047, FR-052)

**Rationale**:
- **Constitution Principle IV**: "In-Memory Data Storage Only" is mandatory
- **Architectural Goal**: Establish clean domain logic independent of storage mechanism
- **Future-Proofing**: Clean separation enables Phase II to add persistence layer without touching domain logic
- **Simplicity**: No file I/O, database drivers, schema migrations, backup/restore logic
- **Testability**: In-memory state is fast to create, modify, and discard in tests

**Tradeoffs**:
- ✅ Pro: Fast performance (no disk I/O latency)
- ✅ Pro: Simple implementation (no serialization, no file format design)
- ✅ Pro: Easy testing (no test fixtures, no cleanup)
- ✅ Pro: Forces clean architecture (data model decoupled from storage)
- ❌ Con: Data lost on exit (user expectation mismatch)
- ❌ Con: Limited usability for real-world task management (no persistence)
- ❌ Con: Cannot demo long-term recurring task behavior

**Phase I Communication Strategy**:
- Display warning on startup: "⚠ Data is stored in memory only. All tasks will be lost when you exit."
- Display warning on exit: "All data has been discarded. Thank you for using Todo CLI!"
- Set user expectation upfront

**Phase II Path**:
- Add persistence layer (file-based JSON, SQLite, or external database)
- Domain models (Task, Priority, RecurrenceRule) remain unchanged
- TaskStore interface remains unchanged, implementation swapped
- Service layer remains unchanged
- **Result**: Phase I architecture supports Phase II persistence without refactoring

## Testing & Acceptance Mapping

### How Each User Story Will Be Validated

**User Story 1 - Basic Task Management (P1)**:

Acceptance Scenarios → Test Cases:

1. **Given** application starts, **When** user selects "Add Task" and enters title, **Then** task appears with unique ID and pending status
   - **Test**: Create task with title "Test Task 1", verify ID=1, status=pending, title="Test Task 1"

2. **Given** task exists, **When** user selects "View Tasks", **Then** task displays with status indicator
   - **Test**: Create task, call view, verify output contains "[ ] Test Task 1"

3. **Given** pending task exists, **When** user marks complete, **Then** status changes to completed
   - **Test**: Create task, mark complete, verify status=completed, view output contains "[✓] Test Task 1"

4. **Given** completed task exists, **When** user marks incomplete, **Then** status changes to pending
   - **Test**: Create completed task, mark incomplete, verify status=pending, view output contains "[ ] Test Task 1"

**Verification Method**: Manual test (interactive session), Automated test (pytest with TaskService)

---

**User Story 2 - Task Details and Updates (P1)**:

Acceptance Scenarios → Test Cases:

1. **Given** adding task, **When** prompted for description, **Then** can provide multi-line or leave blank
   - **Test**: Create task with description "Line 1\nLine 2", verify stored correctly. Create task with empty description, verify description=None

2. **Given** task exists, **When** update title, **Then** changes reflect immediately
   - **Test**: Create task with title "Old", update to "New", verify task.title="New"

3. **Given** task exists, **When** update description independently, **Then** title unchanged
   - **Test**: Create task, update description, verify title remains unchanged

4. **Given** view task details, **When** description exists, **Then** full description displays
   - **Test**: Create task with long description, view details, verify full description shown

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 3 - Task Deletion with Safety (P1)**:

Acceptance Scenarios → Test Cases:

1. **Given** task exists, **When** delete and enter ID, **Then** system prompts for confirmation
   - **Test**: Mock UI input (delete, ID, cancel), verify task still exists

2. **Given** confirmation displayed, **When** confirm (y/yes), **Then** task removed
   - **Test**: Create task, delete with confirmation, verify task not in store

3. **Given** confirmation displayed, **When** cancel (n/no), **Then** task remains
   - **Test**: Create task, delete with cancel, verify task still exists

4. **Given** invalid task ID, **When** submit, **Then** error message displayed
   - **Test**: Attempt delete with ID=999, verify error "Task not found"

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 4 - Priority Management (P2)**:

Acceptance Scenarios → Test Cases:

1. **Given** adding task, **When** prompted for priority, **Then** can select H/M/L (default: M)
   - **Test**: Create task with priority=HIGH, verify task.priority=Priority.HIGH. Create task with no priority, verify task.priority=Priority.MEDIUM

2. **Given** tasks with different priorities, **When** view list, **Then** priority displays as (HIGH), (MED), (LOW)
   - **Test**: Create tasks with each priority, view list, verify output formatting

3. **Given** task exists, **When** update priority, **Then** priority changes independently
   - **Test**: Create task with priority=MEDIUM, update to HIGH, verify task.priority=HIGH, other fields unchanged

4. **Given** no priority specified, **When** task saved, **Then** defaults to Medium
   - **Test**: Create task without priority input, verify task.priority=Priority.MEDIUM

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 5 - Tag-Based Organization (P2)**:

Acceptance Scenarios → Test Cases:

1. **Given** adding/updating task, **When** prompted for tags, **Then** can enter multiple comma-separated
   - **Test**: Create task with tags="work, home", verify task.tags=["work", "home"]

2. **Given** tags entered with mixed case, **When** saved, **Then** normalized to lowercase
   - **Test**: Create task with tags="Work, HOME", verify task.tags=["work", "home"]

3. **Given** tasks have tags, **When** list displayed, **Then** tags appear as #tag1 #tag2
   - **Test**: Create task with tags, view list, verify output contains "#work #home"

4. **Given** task has no tags, **When** displayed, **Then** no tag indicators
   - **Test**: Create task with tags=[], view list, verify no "#" in output

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 6 - Search and Filter (P2)**:

Acceptance Scenarios → Test Cases:

1. **Given** multiple tasks, **When** search by keyword, **Then** only matching tasks display
   - **Test**: Create tasks with titles "Meeting", "Report", "Meeting notes". Search "meeting", verify 2 results

2. **Given** completed and pending tasks, **When** filter by status, **Then** only matching display
   - **Test**: Create 2 pending, 2 completed. Filter by pending, verify 2 results

3. **Given** various priorities, **When** filter by priority, **Then** only matching display
   - **Test**: Create tasks with H, M, L priorities. Filter by HIGH, verify only HIGH priority results

4. **Given** different tags, **When** filter by tag, **Then** only tasks with tag display
   - **Test**: Create tasks with tags "work", "home". Filter by "work", verify only "work" tagged results

5. **Given** filters applied, **When** clear filters, **Then** full list displays
   - **Test**: Apply filter, then clear, verify all tasks shown

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 7 - Sort Task List (P2)**:

Acceptance Scenarios → Test Cases:

1. **Given** tasks with due dates, **When** sort by due date, **Then** chronological order (overdue first)
   - **Test**: Create tasks with dates (past, today, future). Sort by due date, verify order: past → today → future

2. **Given** different priorities, **When** sort by priority, **Then** order: H → M → L
   - **Test**: Create tasks with L, H, M priorities. Sort by priority, verify order: H, M, L

3. **Given** tasks exist, **When** sort alphabetically, **Then** A-Z order (case-insensitive)
   - **Test**: Create tasks "Zebra", "apple", "Banana". Sort alphabetically, verify order: apple, Banana, Zebra

4. **Given** sorting applied, **When** reset sort, **Then** return to creation order
   - **Test**: Sort by priority, then reset, verify original creation order restored

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 8 - Due Date Management (P3)**:

Acceptance Scenarios → Test Cases:

1. **Given** adding/updating task, **When** prompted for due date, **Then** can provide YYYY-MM-DD or leave blank
   - **Test**: Create task with due_date="2026-01-25", verify stored. Create task without due date, verify due_date=None

2. **Given** task has past due date, **When** list displayed, **Then** shows ⚠ OVERDUE
   - **Test**: Create task with due_date=yesterday. View list, verify output contains "⚠ OVERDUE"

3. **Given** task has today due date, **When** displayed, **Then** shows due date without overdue
   - **Test**: Create task with due_date=today. View list, verify no "⚠ OVERDUE"

4. **Given** future due date, **When** displayed, **Then** shows date in standard format
   - **Test**: Create task with due_date=tomorrow. View list, verify output contains "Due: 2026-01-22"

5. **Given** no due date, **When** displayed, **Then** no due date information
   - **Test**: Create task without due date. View list, verify no "Due:" in output

**Verification Method**: Manual test, Automated test (pytest with date mocking)

---

**User Story 9 - Recurring Task Automation (P3)**:

Acceptance Scenarios → Test Cases:

1. **Given** adding/updating task, **When** prompted for recurrence, **Then** can select daily/weekly/monthly/none
   - **Test**: Create task with recurrence=DAILY, verify stored. Create task with recurrence=NONE, verify stored

2. **Given** recurring task exists, **When** marked complete, **Then** new instance auto-created with pending status
   - **Test**: Create daily recurring task, mark complete, verify original is completed, new task exists with pending status

3. **Given** daily recurring task completed today, **When** new instance created, **Then** due date = tomorrow
   - **Test**: Create daily task with due_date=today, mark complete, verify new task due_date=tomorrow

4. **Given** weekly recurring task completed, **When** new instance created, **Then** due date = +7 days
   - **Test**: Create weekly task with due_date=today, mark complete, verify new task due_date=today+7

5. **Given** monthly recurring task completed, **When** new instance created, **Then** due date = +1 month
   - **Test**: Create monthly task with due_date=Jan 15, mark complete, verify new task due_date=Feb 15

6. **Given** recurring task has metadata, **When** new instance created, **Then** all metadata copied
   - **Test**: Create recurring task with title, description, priority, tags. Mark complete, verify new task has same metadata

7. **Given** application session ends, **When** restarted, **Then** recurrence state lost
   - **Test**: Manual test (cannot automate session restart in pytest). Verify data lost on exit

**Verification Method**: Manual test, Automated test (pytest)

---

**User Story 10 - Graceful Application Lifecycle (P1)**:

Acceptance Scenarios → Test Cases:

1. **Given** invalid input (wrong type, format), **When** submitted, **Then** specific error message and re-prompt
   - **Test**: Mock UI input (menu choice="abc"), verify error message displayed, prompt repeated

2. **Given** empty required field, **When** submitted, **Then** "Field required" message and re-prompt
   - **Test**: Mock UI input (title=""), verify error message, prompt repeated

3. **Given** non-existent task ID, **When** operation attempted, **Then** "Task not found" message and return to menu
   - **Test**: Attempt update with ID=999, verify error message, no exception thrown

4. **Given** at main menu, **When** select Exit, **Then** farewell message and clean termination
   - **Test**: Mock UI input (menu choice=0), verify farewell message printed, program exits

5. **Given** unexpected error, **When** caught, **Then** user-friendly message (no stack trace) and recover to menu
   - **Test**: Mock exception in service layer, verify generic error message, no stack trace, returns to menu

**Verification Method**: Manual test, Automated test (pytest with exception mocking)

### Mapping of Success Criteria → Verification Steps

| Success Criterion | Verification Method | Acceptance Threshold |
|-------------------|---------------------|---------------------|
| **SC-001**: Create and view task within 10 seconds | Manual stopwatch test | Start app → add task → view list in <10s |
| **SC-002**: Complete basic workflow without errors | Automated pytest test | add → view → complete → delete (all pass) |
| **SC-003**: Handle 1,000 tasks without degradation | Performance test (pytest-benchmark) | Operations complete in <2s with 1000 tasks |
| **SC-004**: All invalid inputs show clear error messages | Automated pytest (input fuzzing) | 100% of invalid inputs caught, errors clear |
| **SC-005**: Organize with priorities/tags, search/filter <5s | Manual stopwatch test + pytest | Create 100 tasks, search/filter in <5s |
| **SC-006**: Display overdue tasks clearly | Automated pytest | Overdue tasks show "⚠ OVERDUE" in list view |
| **SC-007**: Recurring tasks auto-generate on completion | Automated pytest | Mark recurring task complete, new task exists |
| **SC-008**: Exit cleanly within 2 seconds | Manual stopwatch test | Select exit → program terminates in <2s |
| **SC-009**: All operations via menu navigation | Manual test | Complete all workflows without typing commands |
| **SC-010**: 100% functionality within Phase I constraints | Constitution compliance review | No persistence, no network, no GUI, CLI-only |

### Manual Testing Checklist

Create comprehensive test checklist at `specs/007-phase1-todo-cli/checklists/acceptance.md`:

```markdown
# Acceptance Testing Checklist: Phase I Todo CLI

## P1 Features (Critical - Must Pass)

### Basic Task Management
- [ ] Add task with title only
- [ ] Add task with title and description
- [ ] View empty task list (shows "No tasks found")
- [ ] View task list with tasks (shows all tasks)
- [ ] Mark task as complete (status changes to [✓])
- [ ] Mark completed task as incomplete (status changes to [ ])
- [ ] Task ID is unique and sequential
- [ ] Task ID never reused after deletion

### Task Updates
- [ ] Update task title only
- [ ] Update task description only
- [ ] Update multiple fields in sequence
- [ ] Update preserves other fields
- [ ] View task details shows full description

### Task Deletion
- [ ] Delete task with confirmation (y) - task removed
- [ ] Delete task with cancel (n) - task remains
- [ ] Delete non-existent task ID - error message displayed
- [ ] Deleted task ID not reused for new tasks

### Application Lifecycle
- [ ] Invalid menu choice - error and re-prompt
- [ ] Empty title - error and re-prompt
- [ ] Invalid task ID - error message, no crash
- [ ] Exit from main menu - farewell message, clean termination
- [ ] Data lost on exit - verify on restart

## P2 Features (Important - Should Pass)

### Priority Management
- [ ] Add task with High priority - displays (HIGH)
- [ ] Add task with Medium priority - displays (MED)
- [ ] Add task with Low priority - displays (LOW)
- [ ] Add task without priority - defaults to (MED)
- [ ] Update task priority
- [ ] Sort by priority - order: High → Medium → Low

### Tag Organization
- [ ] Add task with single tag - displays #tag
- [ ] Add task with multiple tags - displays #tag1 #tag2
- [ ] Tags are case-insensitive - "Work" and "work" same
- [ ] Filter by tag - shows only tasks with tag
- [ ] Task with no tags - no # symbols

### Search and Filter
- [ ] Search by keyword in title - matching tasks displayed
- [ ] Search by keyword in description - matching tasks displayed
- [ ] Search with no matches - "No tasks found" message
- [ ] Filter by completed status - only completed tasks
- [ ] Filter by pending status - only pending tasks
- [ ] Filter by priority High - only HIGH tasks
- [ ] Filter by tag - only tasks with tag
- [ ] Clear filters - full list restored

### Sorting
- [ ] Sort by due date - chronological order, overdue first
- [ ] Sort by priority - High → Medium → Low
- [ ] Sort alphabetically - A-Z, case-insensitive
- [ ] Reset sort - return to creation order

## P3 Features (Enhanced - Nice to Have)

### Due Dates
- [ ] Add task with due date - date displays
- [ ] Add task without due date - no date info
- [ ] Task with past due date - displays ⚠ OVERDUE
- [ ] Task with today due date - displays date, no overdue
- [ ] Task with future due date - displays date
- [ ] Update task due date

### Recurring Tasks
- [ ] Add task with daily recurrence
- [ ] Add task with weekly recurrence
- [ ] Add task with monthly recurrence
- [ ] Complete daily recurring task - new task created with tomorrow's date
- [ ] Complete weekly recurring task - new task created with +7 days
- [ ] Complete monthly recurring task - new task created with +1 month
- [ ] New recurring task has same title, description, priority, tags
- [ ] Original recurring task marked complete, new task pending
- [ ] Complete non-recurring task - no new task created

## Performance & Scale

- [ ] Create 100 tasks - operations remain fast (<2s)
- [ ] Create 1,000 tasks - operations remain functional (<5s)
- [ ] Search with 100 tasks - results return quickly (<2s)
- [ ] Sort with 100 tasks - results return quickly (<2s)

## UX Consistency

- [ ] All menus have clear titles and separators
- [ ] All prompts indicate required vs optional
- [ ] All errors have clear messages (no stack traces)
- [ ] All operations return to main menu
- [ ] Status indicators consistent: [ ] and [✓]
- [ ] Priority labels consistent: (HIGH), (MED), (LOW)
- [ ] Tags formatted consistently: #tag
- [ ] Overdue indicator consistent: ⚠ OVERDUE
```

This checklist will be created during `/sp.tasks` phase and used for manual acceptance testing after implementation.

## Project Structure

### Documentation (this feature)

```text
specs/007-phase1-todo-cli/
├── spec.md                  # Feature specification (approved)
├── plan.md                  # This file (implementation plan)
├── tasks.md                 # Implementation tasks (created by /sp.tasks)
├── checklists/
│   ├── requirements.md      # Specification quality checklist (completed)
│   └── acceptance.md        # Acceptance testing checklist (to be created)
└── research.md              # Research notes (minimal - standard library only)
```

### Source Code (repository root)

```text
src/
├── main.py                  # Application entry point
├── models/
│   ├── __init__.py
│   ├── task.py             # Task dataclass, Priority enum, RecurrenceRule enum
│   └── enums.py            # Shared enums (if needed separately)
├── services/
│   ├── __init__.py
│   ├── task_service.py     # Task business logic (create, update, delete, complete, search, filter, sort)
│   └── validation_service.py  # Input validation and normalization
├── store/
│   ├── __init__.py
│   └── task_store.py       # In-memory task storage (dict-based, ID management)
├── ui/
│   ├── __init__.py
│   ├── menu_controller.py  # Main menu loop and navigation
│   ├── formatters.py       # Output formatting (task display, status indicators)
│   └── prompts.py          # Input prompts and validation UI
└── utils/
    ├── __init__.py
    └── date_utils.py       # Date parsing, validation, recurrence calculation

tests/
├── unit/
│   ├── test_task_model.py       # Task model behavior tests
│   ├── test_task_service.py     # Service layer unit tests
│   ├── test_validation_service.py  # Validation logic tests
│   ├── test_task_store.py       # Store operations tests
│   └── test_date_utils.py       # Date utility tests
├── integration/
│   ├── test_workflows.py        # End-to-end workflow tests (add → view → complete → delete)
│   ├── test_search_filter.py   # Search and filter integration tests
│   └── test_recurring_tasks.py # Recurring task automation tests
└── performance/
    └── test_scale.py            # Performance tests (1000 tasks)

pyproject.toml               # UV project configuration
README.md                    # Setup and usage instructions
CLAUDE.md                    # Claude Code operational instructions
```

**Structure Decision**: Single project structure (Option 1) selected because:
- CLI-only application (no frontend/backend split)
- No mobile platform (no iOS/Android)
- Single Python codebase with clear layered architecture
- All components deploy together as one application

## Complexity Tracking

**No violations to justify.** This implementation fully complies with constitution principles:

- ✅ Single project (no multi-project complexity)
- ✅ Direct data access (no repository pattern, no ORM)
- ✅ In-memory storage only (no database, no file I/O)
- ✅ Standard library only (no external dependencies beyond pytest for testing)
- ✅ Deterministic behavior (no AI, no randomness)
- ✅ CLI-only interface (no web framework, no GUI framework)

All features are implemented within constitutional constraints. No complexity budget consumed.

## Next Steps

This plan is now complete and ready for task generation via `/sp.tasks` command.

**Workflow Progression**:
1. ✅ **Spec Complete** (`specs/007-phase1-todo-cli/spec.md`) - Approved specification with 56 functional requirements
2. ✅ **Plan Complete** (this file) - Architecture, design decisions, and acceptance criteria defined
3. ⏭ **Next**: Run `/sp.tasks` to generate `tasks.md` with atomic, sequenced implementation tasks
4. ⏭ **Then**: Run `/sp.implement` to execute task list and generate code

**Key Outputs from This Plan**:
- Architecture: 4-layer design (UI, Service, Domain, Data)
- CLI Flow: Menu-driven navigation with 10 main menu options + sub-menus
- Phasing: I.A (Core) → I.B (Organization) → I.C (Intelligence) sequencing
- Testing: Acceptance scenarios mapped to verification steps, manual checklist defined
- Decisions: Menu-driven UI, simulated advanced features, no persistence (all justified)

**Files Ready for Task Generation**:
- Data model specification (Task, Priority, RecurrenceRule entities)
- Service contracts (create, update, delete, complete, search, filter, sort operations)
- UI flow diagrams (menu hierarchy, user journeys)
- Validation rules (all input fields documented)
- Test strategy (unit, integration, performance test types)

The plan respects all Phase I constraints, aligns with constitution principles, and provides clear implementation guidance for the task generation phase.
