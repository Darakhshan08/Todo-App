# Feature Specification: Update Task

**Feature Branch**: `003-update-task`
**Created**: 2026-01-18
**Status**: Draft
**Input**: User needs to modify existing task details (title and/or description)

## User Scenarios & Testing

### User Story 1 - Update Task Title (Priority: P1)

As a user, I can update a task's title so that I can correct mistakes, clarify wording, or reflect changes in requirements.

**Why this priority**: Tasks evolve over time. Users need to correct typos, update wording, or refine task descriptions as understanding improves. This is essential for maintaining accurate task lists.

**Independent Test**: Create a task, invoke update operation, change the title, verify the new title is saved and displayed. Delivers immediate value for task maintenance.

**Acceptance Scenarios**:

1. **Given** task-001 exists with title "Buy milk", **When** I update the title to "Buy organic milk", **Then** the task title changes to "Buy organic milk"
2. **Given** I update a task title, **When** the update completes, **Then** I see a confirmation message showing the updated title
3. **Given** I update a task title, **When** I view the task list afterward, **Then** the new title is displayed

---

### User Story 2 - Update Task Description (Priority: P2)

As a user, I can update a task's description so that I can add context, update instructions, or clarify requirements as new information becomes available.

**Why this priority**: Task descriptions often need refinement. Users may initially create tasks without descriptions and add them later, or update descriptions as requirements change.

**Independent Test**: Create a task with a description, update the description, verify the change is saved. Useful for maintaining task context over time.

**Acceptance Scenarios**:

1. **Given** task-001 exists with description "Buy from Whole Foods", **When** I update the description to "Buy from Trader Joe's or Whole Foods", **Then** the description changes accordingly
2. **Given** task-001 exists without a description, **When** I add a description "Remember to use coupons", **Then** the description is saved and displayed
3. **Given** task-001 exists with a description, **When** I press Enter without text for the description prompt, **Then** the description remains unchanged (field skip behavior)

---

### User Story 3 - Task Identification for Updates (Priority: P1)

As a user, I can specify which task to update by entering its task ID so that I can reliably update the correct task without ambiguity.

**Why this priority**: Users must be able to precisely target the task they want to update. Task ID-based selection ensures accuracy and prevents accidental updates to the wrong task.

**Independent Test**: Create multiple tasks, specify a task ID for update, verify only that task is modified. Critical for reliable task management.

**Acceptance Scenarios**:

1. **Given** tasks task-001, task-002, and task-003 exist, **When** I request to update task-002, **Then** only task-002 is modified
2. **Given** I enter a task ID that doesn't exist, **When** the system looks up the task, **Then** I receive the error "Error: Task with ID 'task-999' not found."
3. **Given** I enter an invalid task ID format (e.g., "5" instead of "task-005"), **When** the system validates the input, **Then** I receive the error "Error: Invalid task ID format. Please use format 'task-NNN' (e.g., task-001)."

---

### Edge Cases

- **Non-Existent Task ID**: When user attempts to update a task ID that doesn't exist, system displays "Error: Task with ID 'task-XXX' not found." and returns to the main menu without making changes.
- **Invalid Title Update**: When user provides an empty title during update, system displays "Error: Task title cannot be empty. Please provide a title." and re-prompts for a valid title.
- **Title Length Validation**: When user provides a title longer than 200 characters during update, system displays "Error: Title exceeds maximum length of 200 characters. Please shorten your title." and re-prompts.
- **Description Length Validation**: When user provides a description longer than 1000 characters during update, system displays "Error: Description exceeds maximum length of 1000 characters." and re-prompts.
- **Update with Same Value**: When user updates a field to the same value it already has, the update succeeds without error (idempotent operation).
- **Partial Updates**: When user updates only the title (leaving description unchanged) or only the description (leaving title unchanged), only the specified field changes while the other remains intact.
- **Field Skip (Keep Current Value)**: When user presses Enter without text for a field, the system keeps the current value unchanged (skip update). The field is not cleared.
- **Field Clearing Not Supported**: Phase I does not support clearing a field to empty after it has been set. To clear a description, users must update it to a single space character or wait for future phases that support explicit clearing.
- **No Changes Made**: When user skips both title and description updates (presses Enter for both), the task remains unchanged and the system displays 'No changes made. Task remains unchanged.'
- **Multi-line Description Input Method**: To enter multi-line descriptions, users enter literal `\n` escape sequences in console input, which the system interprets as newline characters for storage and display. Example: Entering 'Step 1\nStep 2\nStep 3' creates a three-line description.

## Requirements

### Functional Requirements

- **FR-001**: System MUST prompt the user to enter the task ID of the task they want to update
- **FR-002**: System MUST validate that the provided task ID exists in the task list
- **FR-003**: System MUST reject task IDs that don't exist with error message "Error: Task with ID 'task-XXX' not found."
- **FR-004**: System MUST validate task ID format matches "task-NNN" pattern (e.g., task-001, task-042)
- **FR-005**: System MUST display current task details before prompting for updates in the format:
```
Task ID: task-XXX
Current title: [current title value]
Current description: [current description value or 'No description']
```
- **FR-006**: System MUST prompt the user to enter a new title with the instruction 'Press Enter to keep current title'
- **FR-007**: System MUST prompt the user to enter a new description with the instruction 'Press Enter to keep current description'
- **FR-008**: System MUST allow users to update only the title, only the description, or both
- **FR-009**: System MUST validate new title is not empty (after trimming whitespace) if provided
- **FR-010**: System MUST validate new title does not exceed 200 characters
- **FR-011**: System MUST validate new description does not exceed 1000 characters (if provided)
- **FR-012**: System MUST trim leading and trailing whitespace from updated title and description
- **FR-013**: System MUST preserve the task ID and status when updating title or description
- **FR-014**: System MUST update the task in the in-memory data structure with the new values
- **FR-015**: System MUST display a confirmation message showing what was updated (title, description, or both)
- **FR-016**: System MUST return the user to the main menu after update completes

### Key Entities

- **Task Update**: Represents a modification to an existing task with the following updatable attributes:
  - **Title**: New title value (string, optional update, max 200 characters)
  - **Description**: New description value (string, optional update, max 1000 characters)
  - **Non-updatable attributes**: Task ID and status remain unchanged during update operation

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can successfully update a task title in under 15 seconds
- **SC-002**: Users can successfully update a task description in under 20 seconds
- **SC-003**: System prevents 100% of invalid updates (non-existent IDs, empty titles, excessive length)
- **SC-004**: Updated task information is immediately reflected when viewing the task list
- **SC-005**: Users receive clear confirmation feedback within 1 second of completing an update
- **SC-006**: Task ID and status remain unchanged after update operations (100% preservation)

## Assumptions

1. **In-Memory Update**: Updates are applied directly to the in-memory data structure. No file writes or database updates are performed.
2. **Task Lookup by ID**: Tasks are identified and retrieved using their unique task ID string (e.g., "task-001").
3. **Partial Updates Supported**: Users can update just the title, just the description, or both in a single update operation.
4. **No Update History**: The system does not track update history or maintain previous versions of task data.
5. **Immediate Effect**: Updates take effect immediately upon confirmation. No undo or rollback capability is provided.
6. **Single Task Update**: Each update operation modifies exactly one task. Batch updates are not supported.
7. **Synchronous Operation**: Update completes before returning to the main menu.
8. **Status Preservation**: Updating a task's title or description does not affect its completion status.
