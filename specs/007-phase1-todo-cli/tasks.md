---
description: "Implementation tasks for Phase I Advanced Interactive In-Memory Todo CLI"
---

# Tasks: Phase I – Advanced Interactive In-Memory Todo CLI

**Input**: Design documents from `/specs/007-phase1-todo-cli/`
**Prerequisites**: plan.md (architecture), spec.md (user stories)

**Tests**: Not explicitly requested in specification - tests omitted per specification requirements

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Single project structure: `src/`, `tests/` at repository root
- Paths shown below follow plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure (src/, src/models/, src/services/, src/store/, src/ui/, src/utils/, tests/)
- [X] T002 Initialize Python project with UV package manager (pyproject.toml with Python 3.13+ requirement)
- [X] T003 [P] Create README.md with setup and usage instructions per plan.md
- [X] T004 [P] Create main.py entry point with application bootstrap structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 [P] Create Priority enum (HIGH, MEDIUM, LOW) in src/models/task.py
- [X] T006 [P] Create RecurrenceRule enum (NONE, DAILY, WEEKLY, MONTHLY) in src/models/task.py
- [X] T007 Create Task dataclass with all fields (id, title, description, completed, priority, tags, due_date, recurrence_rule) in src/models/task.py
- [X] T008 Implement Task.is_overdue() method in src/models/task.py
- [X] T009 Create TaskStore class with in-memory dict storage and ID counter in src/store/task_store.py
- [X] T010 [P] Implement TaskStore.add() method in src/store/task_store.py
- [X] T011 [P] Implement TaskStore.get() method in src/store/task_store.py
- [X] T012 [P] Implement TaskStore.delete() method in src/store/task_store.py
- [X] T013 [P] Implement TaskStore.get_all() method in src/store/task_store.py
- [X] T014 [P] Implement TaskStore.get_next_id() method in src/store/task_store.py
- [X] T015 Create ValidationService class in src/services/validation_service.py
- [X] T016 [P] Implement validate_title() method in src/services/validation_service.py
- [X] T017 [P] Implement validate_description() method in src/services/validation_service.py
- [X] T018 [P] Implement validate_priority() method in src/services/validation_service.py
- [X] T019 [P] Implement validate_tags() method (normalize to lowercase) in src/services/validation_service.py
- [X] T020 [P] Implement validate_date() method (YYYY-MM-DD format) in src/services/validation_service.py
- [X] T021 [P] Implement validate_recurrence() method in src/services/validation_service.py
- [X] T022 Create date utility functions in src/utils/date_utils.py (parse_date, calculate_next_occurrence)
- [X] T023 Create base menu display functions in src/ui/formatters.py (format_task_list, format_task_details, format_menu_header)
- [X] T024 Create input prompt utilities in src/ui/prompts.py (prompt_for_input, prompt_for_choice, prompt_for_confirmation)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Task Management (Priority: P1) 🎯 MVP

**Goal**: Users can create, view, and complete tasks through an interactive menu-driven interface

**Independent Test**: Launch app → add task with title → view task list showing new task with pending status → mark complete → verify status changes to [✓]

### Implementation for User Story 1

- [X] T025 [US1] Create TaskService class in src/services/task_service.py with __init__(task_store)
- [X] T026 [US1] Implement TaskService.create_task(title, description) in src/services/task_service.py (validates, creates Task, adds to store)
- [X] T027 [US1] Implement TaskService.get_all_tasks() in src/services/task_service.py (returns list from store)
- [X] T028 [US1] Implement TaskService.complete_task(task_id) in src/services/task_service.py (sets completed=True)
- [X] T029 [US1] Implement TaskService.incomplete_task(task_id) in src/services/task_service.py (sets completed=False)
- [X] T030 [US1] Implement format_status_indicator() in src/ui/formatters.py (returns [ ] or [✓])
- [X] T031 [US1] Implement format_task_line() in src/ui/formatters.py (formats single task for list view)
- [X] T032 [US1] Implement display_task_list() in src/ui/formatters.py (displays all tasks with status indicators)
- [X] T033 [US1] Create MenuController class in src/ui/menu_controller.py with __init__(task_service)
- [X] T034 [US1] Implement MenuController.display_main_menu() in src/ui/menu_controller.py (shows menu options 1-10, 0)
- [X] T035 [US1] Implement MenuController.handle_add_task() in src/ui/menu_controller.py (prompts for title/description, calls task_service.create_task)
- [X] T036 [US1] Implement MenuController.handle_view_tasks() in src/ui/menu_controller.py (calls display_task_list)
- [X] T037 [US1] Implement MenuController.handle_complete_toggle() in src/ui/menu_controller.py (prompts for ID, toggles completion)
- [X] T038 [US1] Implement MenuController.run() main loop in src/ui/menu_controller.py (loop until exit)
- [X] T039 [US1] Wire up main.py to initialize TaskStore, ValidationService, TaskService, MenuController and call run()

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently - basic CRUD works

---

## Phase 4: User Story 2 - Task Details and Updates (Priority: P1)

**Goal**: Users can add optional descriptions to tasks and modify task details later

**Independent Test**: Create task with title and description → view full task details → edit both title and description → verify changes persist in memory

### Implementation for User Story 2

- [X] T040 [US2] Implement TaskService.get_task(task_id) in src/services/task_service.py (returns single task or None)
- [X] T041 [US2] Implement TaskService.update_task_title(task_id, new_title) in src/services/task_service.py
- [X] T042 [US2] Implement TaskService.update_task_description(task_id, new_description) in src/services/task_service.py
- [X] T043 [US2] Implement display_task_details() in src/ui/formatters.py (shows full task with all fields)
- [X] T044 [US2] Implement MenuController.handle_view_task_details() in src/ui/menu_controller.py (prompts for ID, displays details)
- [X] T045 [US2] Implement MenuController.handle_update_task() in src/ui/menu_controller.py (shows update sub-menu with options 1=Title, 2=Description, 0=Cancel)
- [X] T046 [US2] Extend handle_add_task() to accept multi-line description input in src/ui/menu_controller.py

**Checkpoint**: User Stories 1 AND 2 should both work independently - can create, view details, update tasks

---

## Phase 5: User Story 3 - Task Deletion with Safety (Priority: P1)

**Goal**: Users can delete tasks with confirmation prompts to prevent accidental data loss

**Independent Test**: Create task → select delete → cancel confirmation (task remains) → delete again with confirmation → verify task removed

### Implementation for User Story 3

- [X] T047 [US3] Implement TaskService.delete_task(task_id) in src/services/task_service.py (removes from store)
- [X] T048 [US3] Implement MenuController.handle_delete_task() in src/ui/menu_controller.py (prompts for ID, displays task, confirms y/n, deletes if confirmed)
- [X] T049 [US3] Add error handling for non-existent task IDs in src/ui/menu_controller.py (display "Task not found" message)

**Checkpoint**: User Stories 1, 2, AND 3 work independently - full basic CRUD with safety

---

## Phase 6: User Story 10 - Graceful Application Lifecycle (Priority: P1)

**Goal**: Application handles input errors gracefully, validates all inputs, and allows clean exit

**Independent Test**: Provide invalid inputs (wrong types, empty required fields, out-of-range IDs) → verify clear error messages → confirm application returns to menu without crashing → test exit command

### Implementation for User Story 10

- [X] T050 [US10] Implement error handling wrapper in src/ui/prompts.py (catches exceptions, displays user-friendly messages)
- [X] T051 [US10] Add input validation loops to all prompt functions in src/ui/prompts.py (re-prompt on invalid input)
- [X] T052 [US10] Implement handle_exit() in src/ui/menu_controller.py (displays farewell message, exits cleanly)
- [X] T053 [US10] Add try-except blocks to all menu handlers in src/ui/menu_controller.py (catch unexpected errors, display generic message, return to menu)
- [X] T054 [US10] Add startup warning message in main.py ("⚠ Data is stored in memory only. All tasks will be lost when you exit.")
- [X] T055 [US10] Add exit warning message in handle_exit() ("All data has been discarded. Thank you for using Todo CLI!")

**Checkpoint**: All P1 user stories complete - robust MVP with error handling and clean lifecycle

---

## Phase 7: User Story 4 - Priority Management (Priority: P2)

**Goal**: Users can assign priority levels (High, Medium, Low) to tasks to focus on what matters most

**Independent Test**: Create tasks with different priorities → view list with visual priority indicators (HIGH), (MED), (LOW) → verify default priority is Medium

### Implementation for User Story 4

- [X] T056 [US4] Extend TaskService.create_task() to accept priority parameter (default=MEDIUM) in src/services/task_service.py
- [X] T057 [US4] Implement TaskService.update_task_priority(task_id, new_priority) in src/services/task_service.py
- [X] T058 [US4] Implement format_priority_label() in src/ui/formatters.py (returns (HIGH), (MED), or (LOW))
- [X] T059 [US4] Update format_task_line() to include priority label in src/ui/formatters.py
- [X] T060 [US4] Update display_task_details() to show priority in src/ui/formatters.py
- [X] T061 [US4] Update handle_add_task() to prompt for priority (1=High, 2=Medium, 3=Low, default=2) in src/ui/menu_controller.py
- [X] T062 [US4] Add priority update option to handle_update_task() sub-menu in src/ui/menu_controller.py

**Checkpoint**: Priorities working - tasks can be categorized by importance

---

## Phase 8: User Story 5 - Tag-Based Organization (Priority: P2)

**Goal**: Users can assign multiple tags to tasks to categorize and organize by context

**Independent Test**: Create tasks with multiple tags → view tags displayed inline (#work #home) → verify tags are case-insensitive

### Implementation for User Story 5

- [X] T063 [US5] Extend TaskService.create_task() to accept tags parameter (list of strings) in src/services/task_service.py
- [X] T064 [US5] Implement TaskService.update_task_tags(task_id, new_tags) in src/services/task_service.py
- [X] T065 [US5] Implement format_tags() in src/ui/formatters.py (returns "#tag1 #tag2" or empty string)
- [X] T066 [US5] Update format_task_line() to include tags in src/ui/formatters.py
- [X] T067 [US5] Update display_task_details() to show tags in src/ui/formatters.py
- [X] T068 [US5] Update handle_add_task() to prompt for tags (comma-separated) in src/ui/menu_controller.py
- [X] T069 [US5] Add tags update option to handle_update_task() sub-menu in src/ui/menu_controller.py

**Checkpoint**: Tag-based organization working - tasks can be categorized by context

---

## Phase 9: User Story 6 - Search and Filter (Priority: P2)

**Goal**: Users can search tasks by keyword and filter by status, priority, or tag

**Independent Test**: Create diverse tasks → search for keyword in title/description → filter by completion status → filter by priority → filter by tag → verify correct subset displays

### Implementation for User Story 6

- [X] T070 [US6] Implement TaskService.search_tasks(keyword) in src/services/task_service.py (case-insensitive search in title and description)
- [X] T071 [US6] Implement TaskService.filter_by_status(completed) in src/services/task_service.py (returns completed or pending tasks)
- [X] T072 [US6] Implement TaskService.filter_by_priority(priority) in src/services/task_service.py (returns tasks with specific priority)
- [X] T073 [US6] Implement TaskService.filter_by_tag(tag) in src/services/task_service.py (case-insensitive tag matching)
- [X] T074 [US6] Implement TaskService.clear_filters() in src/services/task_service.py (resets view state)
- [X] T075 [US6] Add view state management to TaskStore in src/store/task_store.py (current_filter, filter_params)
- [X] T076 [US6] Implement MenuController.handle_search_tasks() in src/ui/menu_controller.py (prompts for keyword, displays results)
- [X] T077 [US6] Implement MenuController.handle_filter_tasks() in src/ui/menu_controller.py (shows filter sub-menu with options 1=Status, 2=Priority, 3=Tag, 0=Cancel)
- [X] T078 [US6] Implement MenuController.handle_clear_filters() in src/ui/menu_controller.py (clears filters, displays message)
- [X] T079 [US6] Update handle_view_tasks() to respect active filters in src/ui/menu_controller.py

**Checkpoint**: Search and filter working - users can find relevant tasks quickly

---

## Phase 10: User Story 7 - Sort Task List (Priority: P2)

**Goal**: Users can sort tasks by due date, priority, or alphabetically

**Independent Test**: Create tasks with different attributes → sort by each criterion → verify non-destructive sorting (original order can be restored)

### Implementation for User Story 7

- [X] T080 [US7] Create SortOption enum (DEFAULT, DUE_DATE, PRIORITY, ALPHABETICAL) in src/models/task.py
- [X] T081 [US7] Implement TaskService.sort_tasks(sort_by) in src/services/task_service.py (returns sorted list without modifying store)
- [X] T082 [US7] Add sort state management to TaskStore in src/store/task_store.py (current_sort)
- [X] T083 [US7] Implement sort_by_due_date logic in src/services/task_service.py (chronological, overdue first)
- [X] T084 [US7] Implement sort_by_priority logic in src/services/task_service.py (High → Medium → Low)
- [X] T085 [US7] Implement sort_by_alphabetical logic in src/services/task_service.py (case-insensitive title sort)
- [X] T086 [US7] Implement MenuController.handle_sort_tasks() in src/ui/menu_controller.py (shows sort sub-menu with options 1=Due Date, 2=Priority, 3=Alphabetical, 4=Reset, 0=Cancel)
- [X] T087 [US7] Update handle_view_tasks() to apply current sort order in src/ui/menu_controller.py
- [X] T088 [US7] Update handle_clear_filters() to also clear sort order in src/ui/menu_controller.py

**Checkpoint**: Sorting working - users can view tasks in preferred order

---

## Phase 11: User Story 8 - Due Date Management (Priority: P3)

**Goal**: Users can set optional due dates on tasks and see overdue indicators

**Independent Test**: Create tasks with various due dates (past, present, future) → view list showing overdue indicators (⚠ OVERDUE) → verify due date is optional

### Implementation for User Story 8

- [X] T089 [US8] Extend TaskService.create_task() to accept due_date parameter in src/services/task_service.py
- [X] T090 [US8] Implement TaskService.update_task_due_date(task_id, new_due_date) in src/services/task_service.py
- [X] T091 [US8] Implement format_due_date() in src/ui/formatters.py (returns "Due: YYYY-MM-DD" or "⚠ OVERDUE | Due: YYYY-MM-DD")
- [X] T092 [US8] Update format_task_line() to include due date information in src/ui/formatters.py
- [X] T093 [US8] Update display_task_details() to show due date in src/ui/formatters.py
- [X] T094 [US8] Update handle_add_task() to prompt for due date (YYYY-MM-DD, optional) in src/ui/menu_controller.py
- [X] T095 [US8] Add due date update option to handle_update_task() sub-menu in src/ui/menu_controller.py

**Checkpoint**: Due date management working - users can track time-sensitive tasks

---

## Phase 12: User Story 9 - Recurring Task Automation (Priority: P3)

**Goal**: Users can create recurring tasks that automatically generate new instances when completed

**Independent Test**: Create recurring task (e.g., daily) → mark complete → verify new pending instance appears automatically with due date adjusted

### Implementation for User Story 9

- [X] T096 [US9] Extend TaskService.create_task() to accept recurrence_rule parameter in src/services/task_service.py
- [X] T097 [US9] Implement TaskService.update_task_recurrence(task_id, new_recurrence) in src/services/task_service.py
- [X] T098 [US9] Implement handle_recurring_completion(task) in src/services/task_service.py (checks recurrence, calculates next due date, creates new task)
- [X] T099 [US9] Update TaskService.complete_task() to call handle_recurring_completion in src/services/task_service.py
- [X] T100 [US9] Implement calculate_next_occurrence() in src/utils/date_utils.py (handles daily, weekly, monthly logic)
- [X] T101 [US9] Implement format_recurrence() in src/ui/formatters.py (returns "(Daily)", "(Weekly)", "(Monthly)", or empty)
- [X] T102 [US9] Update format_task_line() to include recurrence indicator in src/ui/formatters.py
- [X] T103 [US9] Update display_task_details() to show recurrence rule in src/ui/formatters.py
- [X] T104 [US9] Update handle_add_task() to prompt for recurrence (1=None, 2=Daily, 3=Weekly, 4=Monthly, default=1) in src/ui/menu_controller.py
- [X] T105 [US9] Add recurrence update option to handle_update_task() sub-menu in src/ui/menu_controller.py
- [X] T106 [US9] Update handle_complete_toggle() to display message when recurring task creates new instance in src/ui/menu_controller.py

**Checkpoint**: All user stories complete - full-featured Phase I CLI with all specified capabilities

---

## Phase 13: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final cleanup

- [X] T107 [P] Add comprehensive docstrings to all public methods in src/models/task.py
- [X] T108 [P] Add comprehensive docstrings to all public methods in src/services/task_service.py
- [X] T109 [P] Add comprehensive docstrings to all public methods in src/services/validation_service.py
- [X] T110 [P] Add comprehensive docstrings to all public methods in src/store/task_store.py
- [X] T111 [P] Add comprehensive docstrings to all public methods in src/ui/menu_controller.py
- [X] T112 [P] Update README.md with complete usage examples and feature documentation
- [X] T113 Create acceptance testing checklist in specs/007-phase1-todo-cli/checklists/acceptance.md per plan.md
- [X] T114 [P] Add __init__.py files to all packages (src/models/, src/services/, src/store/, src/ui/, src/utils/)
- [X] T115 Verify all error messages are user-friendly (no stack traces) across all handlers
- [X] T116 Verify all visual indicators are consistent per UX consistency rules in plan.md
- [X] T117 Manual validation: Run through all 10 user story workflows to verify independent functionality

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-12)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed) or sequentially in priority order
  - P1 stories (US1, US2, US3, US10): Phases 3-6 - Core MVP
  - P2 stories (US4, US5, US6, US7): Phases 7-10 - Organization features
  - P3 stories (US8, US9): Phases 11-12 - Advanced features
- **Polish (Phase 13)**: Depends on all desired user stories being complete

### User Story Dependencies

**P1 Stories (MVP)**:
- **User Story 1** (Phase 3): Can start after Foundational - No dependencies on other stories
- **User Story 2** (Phase 4): Can start after Foundational - No dependencies (extends US1 but independent)
- **User Story 3** (Phase 5): Can start after Foundational - No dependencies (extends US1 but independent)
- **User Story 10** (Phase 6): Can start after Foundational - No dependencies (adds error handling to all)

**P2 Stories (Organization)**:
- **User Story 4** (Phase 7): Can start after Foundational - No dependencies (extends Task model)
- **User Story 5** (Phase 8): Can start after Foundational - No dependencies (extends Task model)
- **User Story 6** (Phase 9): Can start after Foundational - No dependencies (adds query operations)
- **User Story 7** (Phase 10): Can start after Foundational - No dependencies (adds sort operations)

**P3 Stories (Advanced)**:
- **User Story 8** (Phase 11): Can start after Foundational - No dependencies (extends Task model)
- **User Story 9** (Phase 12): Can start after US8 (Phase 11) - Depends on due_date for recurrence calculation

**Note**: All user stories are designed to be independently testable. Dependencies listed reflect logical build order, not technical blocking.

### Within Each User Story

- Implementation tasks typically follow this order:
  1. Service layer methods (business logic)
  2. UI formatting functions (presentation)
  3. Menu controller handlers (user interaction)
  4. Integration (wire up to existing menu)

### Parallel Opportunities

**Setup Phase**:
- T003 (README), T004 (main.py) can run in parallel

**Foundational Phase**:
- T005-T006 (enums) can run in parallel
- T010-T014 (TaskStore methods) can run in parallel after T009
- T016-T021 (ValidationService methods) can run in parallel after T015
- T023 (formatters), T024 (prompts) can run in parallel

**User Story Phases**:
- Different user stories can be worked on in parallel by different developers after Foundational completes
- Within P1: US1, US2, US3, US10 are independent
- Within P2: US4, US5, US6, US7 are independent
- Within P3: US8 is independent, US9 depends on US8

**Polish Phase**:
- T107-T111 (docstrings) can all run in parallel
- T112 (README), T113 (checklist), T114 (__init__ files) can run in parallel

---

## Parallel Example: User Story 1

```bash
# After Foundational Phase completes, launch User Story 1 tasks in sequence
# (Tasks within US1 have dependencies on each other):

# First, create service layer (T025-T029)
Task T026: "Implement TaskService.create_task() in src/services/task_service.py"
Task T027: "Implement TaskService.get_all_tasks() in src/services/task_service.py"
# ... (T028-T029)

# Then, create UI layer (T030-T032 can run in parallel after T025)
Task T030: "Implement format_status_indicator() in src/ui/formatters.py" [P]
Task T031: "Implement format_task_line() in src/ui/formatters.py" [P]
Task T032: "Implement display_task_list() in src/ui/formatters.py" [P]

# Then, create menu controller (T033-T038 must be sequential)
Task T034: "Implement MenuController.display_main_menu() in src/ui/menu_controller.py"
Task T035: "Implement MenuController.handle_add_task() in src/ui/menu_controller.py"
# ... (T036-T038)

# Finally, wire up main (T039)
Task T039: "Wire up main.py to initialize components and call run()"
```

---

## Parallel Example: Multiple User Stories

```bash
# After Foundational Phase completes, if you have multiple developers:

# Developer A starts User Story 1 (Phase 3) - T025 through T039
# Developer B starts User Story 2 (Phase 4) - T040 through T046
# Developer C starts User Story 3 (Phase 5) - T047 through T049
# Developer D starts User Story 10 (Phase 6) - T050 through T055

# All can work in parallel because they modify different files
# and are independently testable
```

---

## Implementation Strategy

### MVP First (P1 Stories Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T024) - CRITICAL - blocks all stories
3. Complete Phase 3: User Story 1 (T025-T039) - Basic task management
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Complete Phase 4: User Story 2 (T040-T046) - Task details and updates
6. Complete Phase 5: User Story 3 (T047-T049) - Task deletion
7. Complete Phase 6: User Story 10 (T050-T055) - Error handling
8. **STOP and VALIDATE**: MVP complete - all P1 stories working
9. Deploy/demo if ready

### Incremental Delivery

**Minimum Viable Product (MVP)**: Phases 1-6 only
- Setup + Foundational → Foundation ready
- Add US1 → Test independently → Basic CRUD works
- Add US2 → Test independently → Full task details
- Add US3 → Test independently → Safe deletion
- Add US10 → Test independently → Robust error handling
- **Result**: Production-ready basic todo CLI

**Enhanced Product**: Add Phases 7-10 (P2 stories)
- Add US4 → Priorities working
- Add US5 → Tags working
- Add US6 → Search/filter working
- Add US7 → Sorting working
- **Result**: Organizational features for power users

**Full Product**: Add Phases 11-12 (P3 stories)
- Add US8 → Due dates working
- Add US9 → Recurring tasks working
- **Result**: Complete Phase I specification

**Production Polish**: Phase 13
- Documentation, docstrings, validation
- **Result**: Production-ready, documented, tested

### Parallel Team Strategy

With multiple developers:

1. **Team completes Setup + Foundational together** (Phases 1-2)
2. **Once Foundational is done, split work**:
   - Developer A: User Story 1 (Phase 3)
   - Developer B: User Story 2 (Phase 4)
   - Developer C: User Story 3 (Phase 5)
   - Developer D: User Story 10 (Phase 6)
3. **All P1 stories complete → Validate MVP**
4. **Split P2 work**:
   - Developer A: User Story 4 (Phase 7)
   - Developer B: User Story 5 (Phase 8)
   - Developer C: User Story 6 (Phase 9)
   - Developer D: User Story 7 (Phase 10)
5. **All P2 stories complete → Validate enhanced product**
6. **Split P3 work**:
   - Developer A: User Story 8 (Phase 11)
   - Developer B: User Story 9 (Phase 12) - starts after US8
7. **All stories complete → Polish phase (Phase 13) in parallel**

---

## Task Summary

**Total Tasks**: 117 tasks

**By Phase**:
- Phase 1 (Setup): 4 tasks
- Phase 2 (Foundational): 20 tasks
- Phase 3 (US1): 15 tasks
- Phase 4 (US2): 7 tasks
- Phase 5 (US3): 3 tasks
- Phase 6 (US10): 6 tasks
- Phase 7 (US4): 7 tasks
- Phase 8 (US5): 7 tasks
- Phase 9 (US6): 10 tasks
- Phase 10 (US7): 9 tasks
- Phase 11 (US8): 7 tasks
- Phase 12 (US9): 11 tasks
- Phase 13 (Polish): 11 tasks

**By Priority**:
- P1 stories (US1, US2, US3, US10): 31 implementation tasks (T025-T055)
- P2 stories (US4, US5, US6, US7): 33 implementation tasks (T056-T088)
- P3 stories (US8, US9): 18 implementation tasks (T089-T106)
- Infrastructure (Setup + Foundational + Polish): 35 tasks

**Parallelizable Tasks**: 46 tasks marked [P]

**MVP Scope (Recommended)**: Phases 1-6 (55 tasks) delivers basic todo CLI with error handling

**Independent Test Criteria**: Each user story phase includes independent test description

---

## Format Validation

✅ All 117 tasks follow the required checklist format:
- [x] Checkbox prefix `- [ ]`
- [x] Sequential Task IDs (T001-T117)
- [x] [P] marker on parallelizable tasks (46 tasks)
- [x] [Story] label on user story tasks (US1-US10)
- [x] Clear descriptions with exact file paths
- [x] No template placeholders remaining

✅ All user stories mapped to tasks:
- [x] US1 (15 tasks): T025-T039
- [x] US2 (7 tasks): T040-T046
- [x] US3 (3 tasks): T047-T049
- [x] US10 (6 tasks): T050-T055
- [x] US4 (7 tasks): T056-T062
- [x] US5 (7 tasks): T063-T069
- [x] US6 (10 tasks): T070-T079
- [x] US7 (9 tasks): T080-T088
- [x] US8 (7 tasks): T089-T095
- [x] US9 (11 tasks): T096-T106

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- [Story] label (US1-US10) maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group of related tasks
- Stop at any checkpoint to validate story independently
- Tests not included per specification (not explicitly requested)
- All tasks executable without additional context (specific file paths, clear actions)
- Constitution compliance maintained (in-memory only, CLI only, deterministic, standard library)
