# Feature Specification: Phase I – Advanced Interactive In-Memory Todo CLI

**Feature Branch**: `007-phase1-todo-cli`
**Created**: 2026-01-21
**Status**: Draft
**Input**: User description: "Phase I – Advanced Interactive In-Memory Todo CLI (Blueprint Edition)"

## Overview

This specification defines a production-quality, interactive, menu-driven Todo CLI application using Python. This Phase I implementation serves as the functional blueprint for all future phases (Web, AI, Cloud), establishing WHAT the system can do. Later phases will evolve HOW it runs.

### Phase I Constraints

- CLI-only interface (no GUI, no web UI)
- In-memory storage only (data lost on exit)
- Single-user, session-based execution
- Python 3.13+
- UV package manager (no pip-only flows)
- No databases, no file storage, no network calls
- No background schedulers or notifications
- Advanced features must simulate behavior within session only
- Launch command: `uv run main.py`

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Task Management (Priority: P1)

As a user, I want to create, view, and complete tasks through an interactive menu-driven interface so that I can track my daily activities without learning command syntax.

**Why this priority**: Core functionality that provides immediate value. Without this, there is no todo application. Every subsequent feature builds upon this foundation.

**Independent Test**: Can be fully tested by launching the app, adding a task with a title, viewing the task list showing the new task with pending status, marking it complete, and verifying the status changes. This delivers standalone value as a minimal task tracker.

**Acceptance Scenarios**:

1. **Given** the application starts, **When** user selects "Add Task" from the menu and enters a title, **Then** the task appears in the task list with a unique ID and pending status
2. **Given** a task exists in the list, **When** user selects "View Tasks", **Then** the task displays with clear status indicator ([ ] for pending, [✓] for completed)
3. **Given** a pending task exists, **When** user marks it as complete, **Then** the task status changes to completed and displays with [✓] indicator
4. **Given** a completed task exists, **When** user marks it as incomplete, **Then** the task status changes back to pending and displays with [ ] indicator

---

### User Story 2 - Task Details and Updates (Priority: P1)

As a user, I want to add optional descriptions to tasks and modify task details later so that I can capture context and adapt to changing requirements.

**Why this priority**: Essential for practical use. Tasks often require additional context beyond a title, and requirements change over time.

**Independent Test**: Can be tested by creating a task with title and description, viewing the full task details, editing both title and description, and verifying changes persist in memory during the session.

**Acceptance Scenarios**:

1. **Given** user is adding a new task, **When** prompted for description, **Then** user can provide multi-line text or leave blank
2. **Given** a task exists, **When** user selects "Update Task" and chooses the task by ID, **Then** user can modify title and/or description independently
3. **Given** a task is being updated, **When** user provides new values, **Then** changes are reflected immediately in the task list
4. **Given** user views task details, **When** description exists, **Then** full description displays with clear formatting

---

### User Story 3 - Task Deletion with Safety (Priority: P1)

As a user, I want to delete tasks with confirmation prompts so that I can remove completed or irrelevant items without accidental data loss.

**Why this priority**: Critical for managing task list size and preventing user errors that lead to frustration.

**Independent Test**: Can be tested by creating a task, selecting delete, canceling the confirmation (task remains), deleting again with confirmation, and verifying the task is removed.

**Acceptance Scenarios**:

1. **Given** a task exists, **When** user selects "Delete Task" and enters task ID, **Then** system prompts for confirmation before deletion
2. **Given** deletion confirmation is displayed, **When** user confirms (y/yes), **Then** task is permanently removed from the session
3. **Given** deletion confirmation is displayed, **When** user cancels (n/no), **Then** task remains unchanged in the list
4. **Given** user attempts to delete non-existent task ID, **When** ID is submitted, **Then** system displays clear error message and returns to menu

---

### User Story 4 - Priority Management (Priority: P2)

As a user, I want to assign priority levels (High, Medium, Low) to tasks so that I can focus on what matters most.

**Why this priority**: Enhances productivity by enabling prioritization, but the application is functional without it.

**Independent Test**: Can be tested by creating tasks with different priorities, viewing the list with visual priority indicators (HIGH), (MED), (LOW), and verifying default priority is Medium when not specified.

**Acceptance Scenarios**:

1. **Given** user is adding a task, **When** prompted for priority, **Then** user can select High, Medium, or Low (default: Medium)
2. **Given** tasks with different priorities exist, **When** user views task list, **Then** priority displays with clear visual indicators: (HIGH), (MED), (LOW)
3. **Given** a task exists, **When** user updates the task, **Then** priority can be changed independently from other fields
4. **Given** no priority is specified during creation, **When** task is saved, **Then** priority defaults to Medium

---

### User Story 5 - Tag-Based Organization (Priority: P2)

As a user, I want to assign multiple tags to tasks (e.g., work, home, study) so that I can categorize and organize tasks by context.

**Why this priority**: Improves organization for users managing multiple life areas, but core task management works without it.

**Independent Test**: Can be tested by creating tasks with multiple tags, viewing tags displayed inline (#work #home), and verifying tags are case-insensitive.

**Acceptance Scenarios**:

1. **Given** user is adding or updating a task, **When** prompted for tags, **Then** user can enter multiple comma-separated tags
2. **Given** tags are entered with mixed case, **When** task is saved, **Then** tags are normalized to lowercase for consistency
3. **Given** tasks have tags, **When** task list is displayed, **Then** tags appear inline with format #tag1 #tag2
4. **Given** a task has no tags, **When** displayed, **Then** no tag indicators appear

---

### User Story 6 - Search and Filter (Priority: P2)

As a user, I want to search tasks by keyword and filter by status, priority, or tag so that I can quickly find relevant tasks in a large list.

**Why this priority**: Critical for usability with many tasks, but less important when starting with few tasks.

**Independent Test**: Can be tested by creating diverse tasks, searching for a keyword appearing in title/description, filtering by completion status, filtering by priority, filtering by tag, and verifying correct subset displays.

**Acceptance Scenarios**:

1. **Given** multiple tasks exist, **When** user searches by keyword, **Then** only tasks with keyword in title or description display
2. **Given** completed and pending tasks exist, **When** user filters by completion status, **Then** only matching tasks display
3. **Given** tasks with various priorities exist, **When** user filters by priority level, **Then** only tasks with that priority display
4. **Given** tasks with different tags exist, **When** user filters by tag, **Then** only tasks containing that tag display
5. **Given** filters are applied, **When** user clears filters, **Then** full task list displays again

---

### User Story 7 - Sort Task List (Priority: P2)

As a user, I want to sort tasks by due date, priority, or alphabetically so that I can view tasks in the order most useful for my workflow.

**Why this priority**: Enhances usability but is not essential for core functionality.

**Independent Test**: Can be tested by creating tasks with different attributes, sorting by each criterion (due date, priority, alphabetical), and verifying non-destructive sorting (original order can be restored).

**Acceptance Scenarios**:

1. **Given** tasks with due dates exist, **When** user sorts by due date, **Then** tasks display in chronological order with overdue first
2. **Given** tasks with different priorities exist, **When** user sorts by priority, **Then** tasks display in order: High → Medium → Low
3. **Given** tasks exist, **When** user sorts alphabetically, **Then** tasks display in alphabetical order by title (case-insensitive)
4. **Given** sorting is applied, **When** user returns to menu or resets sort, **Then** tasks return to default order (creation order)

---

### User Story 8 - Due Date Management (Priority: P3)

As a user, I want to set optional due dates on tasks and see overdue indicators so that I can manage time-sensitive work.

**Why this priority**: Advanced feature that adds time awareness but is not required for basic task management.

**Independent Test**: Can be tested by creating tasks with various due dates (past, present, future), viewing the list showing overdue indicators (⚠ OVERDUE), and verifying due date is optional (tasks can exist without it).

**Acceptance Scenarios**:

1. **Given** user is adding or updating a task, **When** prompted for due date, **Then** user can provide date in YYYY-MM-DD format or leave blank
2. **Given** a task has a due date in the past, **When** task list is displayed, **Then** task shows ⚠ OVERDUE indicator
3. **Given** a task has a due date today, **When** task list is displayed, **Then** task shows due date without overdue indicator
4. **Given** a task has a future due date, **When** task list is displayed, **Then** task shows due date in standard format
5. **Given** a task has no due date, **When** displayed, **Then** no due date information appears

---

### User Story 9 - Recurring Task Automation (Priority: P3)

As a user, I want to create recurring tasks (daily, weekly, monthly) that automatically generate new instances when completed, so that I can manage repeating responsibilities without manual re-creation.

**Why this priority**: Advanced productivity feature that automates repetitive work, but most tasks are one-time actions.

**Independent Test**: Can be tested by creating a recurring task (e.g., daily), marking it complete, and verifying a new pending instance appears automatically with due date adjusted according to recurrence rule. Test each recurrence type (daily, weekly, monthly).

**Acceptance Scenarios**:

1. **Given** user is adding or updating a task, **When** prompted for recurrence, **Then** user can select daily, weekly, monthly, or none
2. **Given** a recurring task exists, **When** marked as complete, **Then** a new instance is automatically created with pending status
3. **Given** a daily recurring task is completed today, **When** new instance is created, **Then** due date is set to tomorrow
4. **Given** a weekly recurring task is completed, **When** new instance is created, **Then** due date is set to same day next week
5. **Given** a monthly recurring task is completed, **When** new instance is created, **Then** due date is set to same day next month
6. **Given** recurring task has tags/priority, **When** new instance is created, **Then** all metadata is copied to new instance
7. **Given** application session ends, **When** restarted, **Then** recurrence state is lost (session-only constraint)

---

### User Story 10 - Graceful Application Lifecycle (Priority: P1)

As a user, I want the application to handle my input errors gracefully, validate all inputs, and allow me to exit cleanly so that I have a frustration-free experience.

**Why this priority**: Essential for user experience and preventing crashes. This is part of the core application contract.

**Independent Test**: Can be tested by providing invalid inputs (wrong data types, out-of-range IDs, empty required fields), verifying clear error messages appear, and confirming application returns to menu without crashing. Test exit command to ensure clean shutdown.

**Acceptance Scenarios**:

1. **Given** user provides invalid input (wrong type, format), **When** input is submitted, **Then** system displays specific error message and re-prompts
2. **Given** user provides empty input for required field, **When** submitted, **Then** system displays "Field required" message and re-prompts
3. **Given** user references non-existent task ID, **When** operation is attempted, **Then** system displays "Task not found" message and returns to menu
4. **Given** user is at main menu, **When** user selects Exit/Quit, **Then** application displays farewell message and terminates cleanly
5. **Given** unexpected error occurs, **When** error is caught, **Then** system displays user-friendly message (no stack trace) and recovers to menu

---

### Edge Cases

- **Empty Task List**: When no tasks exist, what does the task list display? Display "No tasks found. Create your first task!" message instead of empty list
- **Duplicate Task IDs**: How are task IDs generated to ensure uniqueness? Use auto-incrementing integer starting at 1, never reuse IDs even after deletion
- **Very Long Task Titles**: How are titles exceeding terminal width displayed? Truncate with ellipsis (...) in list view, show full title in detail view
- **Very Long Descriptions**: How are multi-line descriptions displayed in list view? Show first 50 characters with ellipsis, full text in detail view
- **Invalid Date Formats**: What happens when user enters malformed date? Display clear format example (YYYY-MM-DD) and re-prompt
- **Special Characters in Tags**: How are tags with spaces or special characters handled? Tags with spaces treated as separate tags (split on whitespace/comma)
- **Concurrent Date Boundary**: What happens to recurring tasks when completed exactly at midnight? Use completion timestamp to calculate next occurrence
- **Filter with No Results**: What displays when filter returns zero tasks? Display "No tasks match your filters" with option to clear filters
- **Maximum Tasks**: Is there a practical limit on tasks in memory? No enforced limit, but expect performance degradation beyond 10,000 tasks
- **Ambiguous Menu Input**: What happens if user enters invalid menu choice? Display "Invalid selection. Please choose 1-N" and re-display menu

## Requirements *(mandatory)*

### Functional Requirements

#### Core Task Management
- **FR-001**: Application MUST launch via `uv run main.py` command
- **FR-002**: Application MUST display an interactive menu-driven interface on startup with numbered options
- **FR-003**: Application MUST allow users to add tasks with required title and optional description
- **FR-004**: Application MUST assign unique, sequential, auto-incrementing integer IDs to each task starting from 1
- **FR-005**: Application MUST never reuse task IDs, even after deletion
- **FR-006**: Application MUST display tasks with clear status indicators: [ ] for pending, [✓] for completed
- **FR-007**: Application MUST allow users to toggle task completion status (complete ↔ incomplete)
- **FR-008**: Application MUST allow users to update task title and description independently
- **FR-009**: Application MUST prompt for confirmation before deleting tasks
- **FR-010**: Application MUST permanently remove deleted tasks from the session

#### Priority System
- **FR-011**: Application MUST support three priority levels: High, Medium, Low
- **FR-012**: Application MUST default new tasks to Medium priority if not specified
- **FR-013**: Application MUST display priority visually with labels: (HIGH), (MED), (LOW)
- **FR-014**: Application MUST allow users to set and update task priority

#### Tag System
- **FR-015**: Application MUST allow users to assign zero or more tags to each task
- **FR-016**: Application MUST treat tags as case-insensitive (normalize to lowercase)
- **FR-017**: Application MUST display tags inline with format #tag1 #tag2
- **FR-018**: Application MUST accept tags as comma-separated or space-separated input

#### Search and Filter
- **FR-019**: Application MUST provide keyword search across task title and description
- **FR-020**: Application MUST provide filter by completion status (completed, pending, all)
- **FR-021**: Application MUST provide filter by priority level (High, Medium, Low)
- **FR-022**: Application MUST provide filter by tag (exact match, case-insensitive)
- **FR-023**: Application MUST allow clearing filters to return to full task list

#### Sorting
- **FR-024**: Application MUST provide sort by due date (chronological, overdue first)
- **FR-025**: Application MUST provide sort by priority (High → Medium → Low)
- **FR-026**: Application MUST provide sort by title (alphabetical, case-insensitive)
- **FR-027**: Application MUST implement sorting non-destructively (original order can be restored)

#### Due Dates
- **FR-028**: Application MUST allow optional due date assignment in YYYY-MM-DD format
- **FR-029**: Application MUST calculate and display overdue status (due date < current date)
- **FR-030**: Application MUST display overdue tasks with ⚠ OVERDUE indicator
- **FR-031**: Application MUST validate date format and reject invalid dates

#### Recurring Tasks
- **FR-032**: Application MUST support recurrence rules: daily, weekly, monthly, or none
- **FR-033**: Application MUST automatically create new task instance when recurring task is marked complete
- **FR-034**: Application MUST calculate next due date based on recurrence rule: daily (+1 day), weekly (+7 days), monthly (+1 month)
- **FR-035**: Application MUST copy all task metadata (title, description, priority, tags, recurrence) to new instance
- **FR-036**: Application MUST mark original recurring task as complete and new instance as pending
- **FR-037**: Application MUST maintain recurrence behavior only within current session (lost on exit)

#### User Experience
- **FR-038**: Application MUST validate all user inputs and display specific error messages for invalid input
- **FR-039**: Application MUST handle empty required fields by displaying error and re-prompting
- **FR-040**: Application MUST handle non-existent task IDs with "Task not found" error
- **FR-041**: Application MUST display clear spacing, separators, and visual hierarchy in CLI output
- **FR-042**: Application MUST provide Exit/Quit option that cleanly terminates the session
- **FR-043**: Application MUST display farewell message on exit
- **FR-044**: Application MUST never display technical stack traces to end users
- **FR-045**: Application MUST return to main menu after each operation completes

#### Data Management
- **FR-046**: Application MUST store all data in memory only (no file persistence)
- **FR-047**: Application MUST lose all task data when application exits
- **FR-048**: Application MUST use Python 3.13+ runtime environment
- **FR-049**: Application MUST use UV package manager for dependency management
- **FR-050**: Application MUST operate as single-user, session-based execution model

#### Phase I Constraints
- **FR-051**: Application MUST NOT implement GUI or web UI interfaces
- **FR-052**: Application MUST NOT persist data to files, databases, or external storage
- **FR-053**: Application MUST NOT make network calls or external API requests
- **FR-054**: Application MUST NOT implement background schedulers or daemons
- **FR-055**: Application MUST NOT implement real reminders or system notifications
- **FR-056**: Application MUST simulate all advanced features within session scope only

### Key Entities

- **Todo Task**: Represents a single task item with unique identifier, textual content, completion status, priority level, categorization tags, optional due date, and optional recurrence behavior. Tasks are the primary data entity. Attributes include: id (unique integer), title (required string), description (optional string), completed (boolean), priority (enum: high/medium/low), tags (list of strings), due_date (optional date), recurrence_rule (optional enum: daily/weekly/monthly/none)

- **Application Session**: Represents a single execution lifecycle of the application from launch to exit. Contains all tasks in memory, tracks current ID counter for task generation, maintains current view state (filters, sorting), and manages menu navigation state. Session is destroyed completely on exit with no persistence

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create a task and view it in the list within 10 seconds using only menu selections
- **SC-002**: Users can complete basic task workflow (add → view → complete → delete) without encountering errors on valid input
- **SC-003**: Application handles at least 1,000 tasks in memory without performance degradation (operations complete within 2 seconds)
- **SC-004**: All invalid inputs result in clear error messages (no technical jargon or stack traces displayed)
- **SC-005**: Users can organize tasks using priorities and tags, and retrieve specific tasks via search/filter in under 5 seconds
- **SC-006**: Application displays overdue tasks clearly when viewing task list (visual indicator visible without additional action)
- **SC-007**: Recurring tasks automatically generate next instance on completion without user intervention
- **SC-008**: Application exits cleanly with confirmation within 2 seconds of user selection
- **SC-009**: Users can perform all operations through menu navigation without typing commands or remembering syntax
- **SC-010**: 100% of required functionality works within Phase I constraints (no persistence, no network, no GUI)

## Assumptions

- Users have Python 3.13+ installed on their system
- Users have UV package manager installed and accessible in PATH
- Users interact with application via terminal/command prompt with minimum 80 character width
- Users understand basic todo list concepts (task, complete, priority)
- Users can read and input dates in YYYY-MM-DD format
- Terminal supports basic text formatting (spaces, line breaks, standard ASCII characters)
- System clock is accurate for due date calculations
- Users accept data loss on application exit (in-memory constraint is understood)
- Users operate in single-user environment (no concurrent access requirements)
- Application runs on operating systems supporting Python 3.13+ (Windows, macOS, Linux)

## Out of Scope

The following are explicitly excluded from Phase I:

- Persistent storage (files, databases, cloud storage)
- User authentication or multi-user support
- Web interface, REST API, or GraphQL endpoints
- Mobile application or desktop GUI
- Network synchronization or cloud backup
- Email, SMS, or push notifications
- Background services or scheduled jobs
- Third-party integrations (calendar, email, project management tools)
- Real-time reminders or alerts
- Task sharing or collaboration features
- Undo/redo functionality
- Task history or audit logs
- Data import/export functionality
- Customizable themes or UI preferences
- Keyboard shortcuts or CLI command syntax
- Task dependencies or subtasks
- File attachments or links
- Time tracking or productivity analytics
- Natural language processing for task creation
- AI-powered suggestions or automation

These features may be considered in future phases (Web, AI, Cloud) as appropriate.
