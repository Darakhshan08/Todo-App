# Feature Specification: Mark Task Complete/Incomplete

**Feature Branch**: `005-mark-complete`
**Created**: 2026-01-18
**Status**: Draft
**Input**: User needs to toggle the completion status of tasks to track progress

## User Scenarios & Testing

### User Story 1 - Mark Task as Complete (Priority: P1)

As a user, I can mark a task as complete so that I can track which work items I have finished and distinguish them from pending tasks.

**Why this priority**: Completion tracking is the primary purpose of a todo application. Users need to mark tasks complete to track progress, feel accomplishment, and focus on remaining work.

**Independent Test**: Create an incomplete task, mark it complete, verify status changes to complete and displays "✓" symbol. Core value proposition of task management.

**Acceptance Scenarios**:

1. **Given** task-001 exists with incomplete status, **When** I mark it as complete, **Then** its status changes to complete
2. **Given** I mark task-001 as complete, **When** I view the task list, **Then** task-001 displays with "✓" symbol indicating completion
3. **Given** I mark a task as complete, **When** the operation completes, **Then** I see confirmation message "Task 'task-001: [title]' marked as complete."

---

### User Story 2 - Mark Task as Incomplete (Toggle Functionality) (Priority: P1)

As a user, I can mark a completed task as incomplete so that I can handle situations where work needs to be redone or I marked completion by mistake.

**Why this priority**: Users make mistakes or circumstances change. Tasks marked complete may need to be reopened. Toggle functionality provides flexibility and error recovery.

**Independent Test**: Create a complete task, mark it incomplete, verify status changes back to incomplete and displays "✗" symbol. Essential for status management flexibility.

**Acceptance Scenarios**:

1. **Given** task-001 exists with complete status, **When** I mark it as incomplete, **Then** its status changes to incomplete
2. **Given** I mark task-001 as incomplete, **When** I view the task list, **Then** task-001 displays with "✗" symbol indicating incomplete status
3. **Given** I mark a complete task as incomplete, **When** the operation completes, **Then** I see confirmation message "Task 'task-001: [title]' marked as incomplete."

---

### User Story 3 - Status Toggle via Single Operation (Priority: P2)

As a user, I can use a single "toggle status" operation that automatically flips the task between complete and incomplete states so that I don't need to remember the current status before changing it.

**Why this priority**: A toggle operation simplifies the user interface and reduces cognitive load. Users can simply "flip the status" without checking the current state first.

**Independent Test**: Use toggle operation on incomplete task (becomes complete), then toggle again (becomes incomplete). Demonstrates intuitive status flipping.

**Acceptance Scenarios**:

1. **Given** task-001 is incomplete, **When** I toggle its status, **Then** it becomes complete
2. **Given** task-001 is complete, **When** I toggle its status, **Then** it becomes incomplete
3. **Given** I toggle a task's status twice, **When** I view the task, **Then** it returns to its original status
4. **Given** I toggle a task status, **When** the toggle completes, **Then** I see confirmation showing the new status (e.g., "Task 'task-001: [title]' is now complete.")

---

### Edge Cases

- **Non-Existent Task ID**: When user attempts to mark a task that doesn't exist, system displays "Error: Task with ID 'task-XXX' not found." and returns to main menu without changes.
- **Invalid Task ID Format**: When user enters an invalid ID format (e.g., "5" instead of "task-005"), system displays "Error: Invalid task ID format. Please use format 'task-NNN' (e.g., task-001)."
- **Idempotent Status Change**: When user marks an already-complete task as complete again (if using separate complete/incomplete commands), operation succeeds with message "Task 'task-001' is already complete."
- **Toggle Multiple Times**: When user toggles the same task multiple times in succession, each toggle correctly flips the status without errors.
- **Status Preservation Across Views**: When user marks a task complete and then views the task list multiple times, the complete status persists throughout the session.
- **Title and Description Unchanged**: When marking a task complete or incomplete, the title and description remain exactly as they were (only status changes).

## Requirements

### Functional Requirements

- **FR-001**: System MUST prompt the user to enter the task ID of the task whose status they want to change
- **FR-002**: System MUST validate that the provided task ID exists in the task list
- **FR-003**: System MUST reject task IDs that don't exist with error message "Error: Task with ID 'task-XXX' not found."
- **FR-004**: System MUST validate task ID format matches "task-NNN" pattern (e.g., task-001, task-042)
- **FR-005**: System MUST display the current task details (ID, title, current status) before changing status
- **FR-006**: System MUST support toggling status from incomplete to complete
- **FR-007**: System MUST support toggling status from complete to incomplete
- **FR-008**: System MUST update the task's status in the in-memory data structure
- **FR-009**: System MUST preserve the task's ID, title, and description when changing status (only status changes)
- **FR-010**: System MUST display confirmation message showing the new status (e.g., "Task 'task-001: [title]' is now complete." or "Task 'task-001: [title]' is now incomplete.")
- **FR-011**: System MUST immediately reflect status changes when viewing the task list (updated status symbols ✓/✗)
- **FR-012**: System MUST return the user to the main menu after status change completes

### Key Entities

- **Task Status**: Represents the completion state of a task
  - **Status Values**: "complete" (represented by ✓ symbol) or "incomplete" (represented by ✗ symbol)
  - **Toggle Operation**: Flips status from current state to opposite state
  - **Affected Attributes**: Only the status field changes; ID, title, and description remain unchanged

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can toggle task status in under 8 seconds
- **SC-002**: Status changes are immediately reflected in the task list view (0-second delay)
- **SC-003**: System prevents 100% of invalid status changes (non-existent IDs, wrong format)
- **SC-004**: Task title and description remain unchanged after status toggle (100% preservation)
- **SC-005**: Users receive clear feedback showing the new status within 1 second of toggle operation
- **SC-006**: Status toggle operations succeed 100% of the time for valid task IDs

## Assumptions

1. **In-Memory Status Update**: Status changes are applied directly to the in-memory data structure. No file writes or database updates are performed.
2. **Task Lookup by ID**: Tasks are identified and updated using their unique task ID string (e.g., "task-001").
3. **Binary Status States**: Tasks have exactly two states: complete and incomplete. No intermediate states (e.g., "in progress") exist.
4. **Status Persistence**: Status changes persist in memory for the duration of the application session. Once marked complete, a task remains complete until explicitly toggled back.
5. **Synchronous Operation**: Status toggle completes before returning to the main menu.
6. **No Status History**: The system does not track when a task was marked complete or how many times status has been toggled.
7. **Status-Only Modification**: Changing status does not affect any other task attributes (ID, title, description remain unchanged).
8. **Toggle Interface**: The operation is designed as a toggle (flip current state) rather than separate "mark complete" and "mark incomplete" commands, though both approaches satisfy requirements.
