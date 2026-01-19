# Tasks: Phase I – In-Memory Python Console Todo Application

**Feature**: Phase I Complete Implementation (5 Core Features)
**Branch**: `001-add-task`
**Date**: 2026-01-19
**Plan**: [specs/001-add-task/plan.md](./plan.md)

---

## Summary

This task breakdown covers the complete Phase I implementation of the in-memory Python console Todo application. All 5 core features are organized by user story priority and designed for independent implementation and testing.

**Total Tasks**: 23
**Parallel Opportunities**: 12 tasks can run in parallel within their phases
**MVP Scope**: User Story 1 (Add Task) + foundational infrastructure = 8 tasks

---

## Implementation Strategy

**Approach**: Incremental delivery by user story priority. Each story is independently testable and delivers standalone value.

**Execution Order**:
1. **Phase 1**: Setup (project scaffolding) – 2 tasks
2. **Phase 2**: Foundational (shared infrastructure) – 3 tasks
3. **Phase 3**: User Story 1 (Add Task) – P1 priority – 3 tasks
4. **Phase 4**: User Story 2 (View Task List) – P1 priority – 3 tasks
5. **Phase 5**: User Story 3 (Update Task) – P1 priority – 3 tasks
6. **Phase 6**: User Story 4 (Delete Task) – P1 priority – 3 tasks
7. **Phase 7**: User Story 5 (Mark Complete) – P1 priority – 3 tasks
8. **Phase 8**: Integration & Polish – 3 tasks

**Parallel Execution**: Within each user story phase, tasks marked [P] can run in parallel if needed.

---

## Phase 1: Setup

**Goal**: Initialize Python project structure per implementation plan

### Tasks

- [ ] T001 Create project directory structure (src/, tests/, specs/, history/)
- [ ] T002 Create pyproject.toml with UV package manager configuration and pytest dependency

**Completion Criteria**: Directory structure matches plan.md; pyproject.toml is valid and installable

---

## Phase 2: Foundational (Blocking Prerequisites)

**Goal**: Implement shared infrastructure required by all user stories

### Tasks

- [ ] T003 [P] Implement Task data model in src/models/task.py with id, title, description, status, created_at attributes
- [ ] T004 [P] Implement TaskValidator in src/services/task_validator.py with title/description/id validation functions
- [ ] T005 Implement TaskService skeleton in src/services/task_service.py with in-memory task storage (empty list)

**Completion Criteria**: All foundational modules exist; Task model can be instantiated; Validator functions can be called; TaskService has empty storage ready

---

## Phase 3: User Story 1 – Add Task (P1)

**User Story**: As a user, I can create a new task with a title and optional description so that I can quickly capture todo items.

**Independent Test**: Launch application, enter title when prompted, verify task appears with unique ID and incomplete status.

**Spec Reference**: [specs/001-add-task/spec.md](../../001-add-task/spec.md)

### Tasks

- [ ] T006 [US1] Implement ID generator in src/models/task.py (sequential task-001, task-002, task-003 format)
- [ ] T007 [US1] Implement add_task() in src/services/task_service.py (validate → create Task → store in list)
- [ ] T008 [US1] Implement add_task_command() in src/cli/commands.py (prompt title/description → call service → display confirmation)

**Completion Criteria**: Users can create tasks with title-only or title+description. Tasks receive unique IDs (task-001, task-002, etc.). Validation rejects empty titles and oversized input per spec.

**Acceptance Scenarios** (from spec):
- ✅ Create task with title "Buy groceries" → task-001 created with incomplete status
- ✅ Create task with title and description → both saved correctly
- ✅ Empty title → error "Task title cannot be empty"
- ✅ Title >200 chars → error "Title exceeds maximum length"
- ✅ Description >1000 chars → error "Description exceeds maximum length"
- ✅ Whitespace trimming → "  Call mom  " becomes "Call mom"

---

## Phase 4: User Story 2 – View Task List (P1)

**User Story**: As a user, I can view a list of all my tasks with clear status indicators so that I can see what work is pending and completed.

**Independent Test**: Create multiple tasks (some complete, some incomplete), invoke view operation, verify all tasks displayed with status symbols (✓/✗).

**Spec Reference**: [specs/002-view-task-list/spec.md](../../002-view-task-list/spec.md)

### Tasks

- [ ] T009 [US2] Implement get_all_tasks() in src/services/task_service.py (return list of all tasks in creation order)
- [ ] T010 [US2] Implement task display formatter in src/cli/ui.py (format: "task-001 ✗ Title" with description below)
- [ ] T011 [US2] Implement view_list_command() in src/cli/commands.py (retrieve tasks → format → display, handle empty list)

**Completion Criteria**: All tasks display with ID, status symbol (✓ complete, ✗ incomplete), title, and description. Empty list shows "No tasks found. Your task list is empty."

**Acceptance Scenarios** (from spec):
- ✅ View 3 tasks (2 incomplete, 1 complete) → all display with correct status symbols
- ✅ Task with description → description shown below title
- ✅ Task without description → no description line or "No description" shown
- ✅ Empty list → "No tasks found" message displayed
- ✅ Multi-line descriptions → line breaks preserved

---

## Phase 5: User Story 3 – Update Task (P1)

**User Story**: As a user, I can update a task's title and/or description so that I can correct mistakes or reflect changes in requirements.

**Independent Test**: Create a task, invoke update operation, change title/description, verify changes saved and displayed.

**Spec Reference**: [specs/003-update-task/spec.md](../../003-update-task/spec.md)

### Tasks

- [ ] T012 [US3] Implement find_task_by_id() in src/services/task_service.py (lookup task by ID string)
- [ ] T013 [US3] Implement update_task() in src/services/task_service.py (find task → validate new values → update title/description)
- [ ] T014 [US3] Implement update_task_command() in src/cli/commands.py (prompt for ID → show current values → prompt for new values → call service)

**Completion Criteria**: Users can update title only, description only, or both. Task ID and status remain unchanged. Pressing Enter without text keeps current value. Non-existent IDs show error.

**Acceptance Scenarios** (from spec):
- ✅ Update task-001 title from "Buy milk" to "Buy organic milk" → title changes
- ✅ Update description → new description saved
- ✅ Update with empty title → error "Task title cannot be empty"
- ✅ Non-existent task ID → error "Task with ID 'task-999' not found"
- ✅ Invalid ID format (e.g., "5") → error "Invalid task ID format"
- ✅ Press Enter to skip field → current value preserved

---

## Phase 6: User Story 4 – Delete Task (P1)

**User Story**: As a user, I can delete a task by ID so that I can remove tasks that are no longer relevant or were created by mistake.

**Independent Test**: Create multiple tasks, delete one by ID with confirmation, verify it no longer appears in task list.

**Spec Reference**: [specs/004-delete-task/spec.md](../../004-delete-task/spec.md)

### Tasks

- [ ] T015 [US4] Implement delete_task() in src/services/task_service.py (find task → remove from list, do NOT renumber IDs)
- [ ] T016 [US4] Implement confirmation prompt in src/cli/ui.py (accept yes/y/no/n, case-insensitive)
- [ ] T017 [US4] Implement delete_task_command() in src/cli/commands.py (prompt ID → show task → confirm → call service → display result)

**Completion Criteria**: Users can delete tasks by ID after confirmation. Remaining tasks keep original IDs (no renumbering). Cancelled deletions leave task unchanged. Non-existent IDs show error.

**Acceptance Scenarios** (from spec):
- ✅ Delete task-002 with confirmation "yes" → task removed from list
- ✅ View list after deletion → only task-001 and task-003 remain
- ✅ Confirmation prompt → "Are you sure you want to delete task-002: [title]? (yes/no)"
- ✅ Enter "no" → deletion cancelled, task preserved
- ✅ Non-existent ID → error "Task with ID 'task-999' not found. No deletion performed."
- ✅ Invalid confirmation input → error "Invalid input. Please enter 'yes' or 'no'."

---

## Phase 7: User Story 5 – Mark Complete (P1)

**User Story**: As a user, I can toggle a task's completion status so that I can track which work items are finished.

**Independent Test**: Create incomplete task, mark complete, verify status changes to ✓. Mark complete task as incomplete, verify status changes to ✗.

**Spec Reference**: [specs/005-mark-complete/spec.md](../../005-mark-complete/spec.md)

### Tasks

- [ ] T018 [US5] Implement toggle_status() in src/services/task_service.py (find task → flip status: incomplete↔complete)
- [ ] T019 [US5] Implement status display logic in src/cli/ui.py (✓ for complete, ✗ for incomplete)
- [ ] T020 [US5] Implement toggle_status_command() in src/cli/commands.py (prompt ID → call service → display new status)

**Completion Criteria**: Users can toggle task status between complete/incomplete. Title and description remain unchanged. Status immediately reflected in view list. Non-existent IDs show error.

**Acceptance Scenarios** (from spec):
- ✅ Mark incomplete task as complete → status changes to "complete", displays ✓
- ✅ Mark complete task as incomplete → status changes to "incomplete", displays ✗
- ✅ Toggle task-001 twice → returns to original status
- ✅ Confirmation message → "Task 'task-001: [title]' is now complete."
- ✅ Non-existent ID → error "Task with ID 'task-999' not found."
- ✅ View list after toggle → status symbol updated immediately

---

## Phase 8: Integration & Polish

**Goal**: Complete CLI loop, main entry point, and cross-feature integration

### Tasks

- [ ] T021 Implement main menu in src/cli/ui.py (display options: 1-Add, 2-View, 3-Update, 4-Delete, 5-Toggle, 6-Exit)
- [ ] T022 Implement main CLI loop in src/main.py (display menu → route to command handlers → loop until exit)
- [ ] T023 Create README.md with setup instructions (UV install, run command, feature descriptions)

**Completion Criteria**: Full CLI application runs from `python src/main.py`. All 5 features accessible via menu. Exit option terminates cleanly. README has clear setup and usage instructions.

---

## Dependencies

### User Story Dependency Graph

```
Phase 1 (Setup)
    ↓
Phase 2 (Foundational) ← Blocks ALL user stories
    ↓
    ├─→ Phase 3 (US1: Add Task) ────────────────┐
    ├─→ Phase 4 (US2: View List) ───────────────┤
    ├─→ Phase 5 (US3: Update Task) ─────────────┤ → Phase 8 (Integration)
    ├─→ Phase 6 (US4: Delete Task) ─────────────┤
    └─→ Phase 7 (US5: Mark Complete) ───────────┘
```

**Key Dependencies**:
- **Foundational blocks ALL**: User stories require Task model, validator, and service skeleton
- **User stories are INDEPENDENT**: US1-US5 can be implemented in parallel after Phase 2 completes
- **Integration requires ALL stories**: Phase 8 depends on all user story implementations

### Parallel Execution Opportunities

**Phase 2** (after T002 completes):
- T003, T004 can run in parallel (different files, no dependencies)

**Phase 3-7** (after Phase 2 completes):
- US1 (T006-T008), US2 (T009-T011), US3 (T012-T014), US4 (T015-T017), US5 (T018-T020) can ALL be implemented in parallel by different developers/agents
- Within each story: Tasks can run sequentially OR in parallel if file-based isolation is maintained

**Phase 8** (after all user stories):
- T021-T023 run sequentially (integration dependencies)

---

## Validation Checklist

### Format Validation
- ✅ All tasks follow checklist format: `- [ ] [ID] [Labels] Description with file path`
- ✅ Task IDs sequential (T001-T023)
- ✅ [P] markers present for parallelizable tasks (T003, T004)
- ✅ [US#] labels present for user story tasks (T006-T020)

### Completeness Validation
- ✅ All 5 user stories from specs have dedicated phases
- ✅ Each user story has independent test criteria
- ✅ Foundational infrastructure identified and separated
- ✅ Integration phase includes CLI loop and entry point
- ✅ All file paths from plan.md are covered

### Acceptance Criteria Coverage
- ✅ US1 Add Task: 6 scenarios covered (create, validate, trim, errors)
- ✅ US2 View List: 5 scenarios covered (display, symbols, empty list)
- ✅ US3 Update Task: 6 scenarios covered (update title/description, validation, errors)
- ✅ US4 Delete Task: 6 scenarios covered (delete, confirm, cancel, errors)
- ✅ US5 Mark Complete: 6 scenarios covered (toggle, display, errors)

---

## MVP Scope Recommendation

**Minimum Viable Product** (8 tasks):
- Phase 1: T001-T002 (Setup)
- Phase 2: T003-T005 (Foundational)
- Phase 3: T006-T008 (US1: Add Task)

**Rationale**: This MVP enables users to create and store tasks with validation. Delivers core value (task capture) without requiring view, update, delete, or status management.

**Next Increment** (add 3 tasks): Phase 4 (T009-T011) → enables viewing created tasks

---

## Task Summary

| Phase | User Story | Task Count | Parallel Tasks | Estimated Scope |
|-------|-----------|------------|----------------|-----------------|
| Phase 1 | Setup | 2 | 0 | Small |
| Phase 2 | Foundational | 3 | 2 (T003, T004) | Medium |
| Phase 3 | US1: Add Task | 3 | 0 | Medium |
| Phase 4 | US2: View List | 3 | 0 | Medium |
| Phase 5 | US3: Update | 3 | 0 | Medium |
| Phase 6 | US4: Delete | 3 | 0 | Medium |
| Phase 7 | US5: Mark Complete | 3 | 0 | Medium |
| Phase 8 | Integration | 3 | 0 | Small |
| **TOTAL** | | **23** | **2** | **Medium** |

**Estimated Implementation Time**: 4-6 hours for experienced developer; 2-3 hours for Claude Code with approved specs

---

## Next Steps

1. **Review and approve** this task breakdown
2. **Run `/sp.implement`** to begin execution (starts with T001)
3. **Verify each phase** independently before moving to next
4. **Track progress** using task checkboxes

**Status**: ✅ Tasks generated and ready for implementation
