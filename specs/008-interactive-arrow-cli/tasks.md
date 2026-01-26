---

description: "Task list for Interactive Arrow-Key Driven CLI UI implementation"
---

# Tasks: Interactive Arrow-Key Driven CLI UI

**Input**: Design documents from `/specs/008-interactive-arrow-cli/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅

**Tests**: Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below follow the structure defined in plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Install blessed terminal library via `uv add blessed`
- [X] T002 [P] Create project structure: `src/ui/` directory for new components
- [X] T003 [P] Create `tests/unit/` directory for interactive component tests
- [X] T004 [P] Create `tests/integration/` directory for workflow tests
- [X] T005 [P] Update `.gitignore` to include Python cache files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 [P] Create `src/ui/input_handler.py` with KeyInput dataclass and InputHandler class
- [X] T007 [P] Create `src/ui/color_theme.py` with ColorTheme class and terminal detection
- [X] T008 [P] Create `src/ui/screen_manager.py` with ScreenManager class for terminal operations
- [X] T009 [P] Create `src/ui/interactive_menu.py` with InteractiveMenu class for arrow-key navigation
- [X] T010 [P] Create `src/ui/interactive_task_list.py` with InteractiveTaskList class for task navigation
- [X] T011 Modify `src/ui/formatters.py` to add color rendering functions with ASCII fallback
- [X] T012 Modify `src/ui/menu_controller.py` to integrate interactive components and manage main loop
- [X] T013 Modify `main.py` to use new MenuController with interactive UI

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Arrow-Key Menu Navigation (Priority: P1) 🎯 MVP

**Goal**: Enable users to navigate the main menu using arrow keys (↑ ↓) and select options with Enter, eliminating manual number typing

**Independent Test**: Launch the application, navigate the main menu with arrow keys, and select any option with Enter. Verify selection highlighting and circular navigation work correctly.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US1] Unit test for InputHandler arrow key capture in `tests/unit/test_input_handler.py`
- [ ] T015 [P] [US1] Unit test for InteractiveMenu navigation in `tests/unit/test_interactive_menu.py`
- [ ] T016 [P] [US1] Integration test for main menu navigation in `tests/integration/test_interactive_workflows.py`

### Implementation for User Story 1

- [X] T017 [P] [US1] Implement KeyInput dataclass in `src/ui/input_handler.py` with key_name, is_printable, char fields
- [X] T018 [P] [US1] Implement InputHandler.get_key() method in `src/ui/input_handler.py` with timeout support
- [X] T019 [P] [US1] Implement ColorTheme class in `src/ui/color_theme.py` with terminal capability detection
- [X] T020 [P] [US1] Implement ColorTheme.highlight() method for selection highlighting with ASCII fallback
- [X] T021 [P] [US1] Implement ScreenManager class in `src/ui/screen_manager.py` with clear(), refresh(), and get_dimensions() methods
- [X] T022 [US1] Implement InteractiveMenu.show() method in `src/ui/interactive_menu.py` with circular navigation (depends on T017, T018, T019, T021)
- [X] T023 [US1] Implement arrow key handling (KEY_UP, KEY_DOWN, KEY_ENTER, KEY_ESCAPE) in InteractiveMenu
- [X] T024 [US1] Implement selection highlighting and menu rendering in InteractiveMenu
- [X] T025 [US1] Add format_priority_label() function to `src/ui/formatters.py` with color support
- [X] T026 [US1] Add format_status_indicator() function to `src/ui/formatters.py` with Unicode symbols
- [X] T027 [US1] Modify MenuController.run() to use InteractiveMenu for main menu navigation
- [X] T028 [US1] Add keyboard shortcut handling (Esc/q for exit) in MenuController
- [X] T029 [US1] Update main.py to initialize and run new MenuController

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. Users can navigate the main menu with arrow keys and select options with Enter.

---

## Phase 4: User Story 2 - Visual Clarity and Color Enhancement (Priority: P2)

**Goal**: Provide color-coded information and clear visual hierarchy so users can quickly identify task priorities, statuses, and important information

**Independent Test**: View task lists and verify that colors appear correctly for different priorities (HIGH=red, MEDIUM=yellow, LOW=green), statuses (completed=green, incomplete=white), and overdue warnings (red). Test ASCII fallback on limited terminals.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T030 [P] [US2] Unit test for ColorTheme priority colors in `tests/unit/test_color_theme.py`
- [ ] T031 [P] [US2] Unit test for ColorTheme status colors in `tests/unit/test_color_theme.py`
- [ ] T032 [P] [US2] Unit test for ASCII fallback rendering in `tests/unit/test_color_theme.py`
- [ ] T033 [P] [US2] Integration test for task list color rendering in `tests/integration/test_interactive_workflows.py`

### Implementation for User Story 2

- [X] T034 [P] [US2] Implement ColorTheme.priority_color() method for semantic priority rendering
- [X] T035 [P] [US2] Implement ColorTheme.status_color() method for task status rendering
- [X] T036 [P] [US2] Implement ColorTheme.warning() method for overdue task warnings
- [X] T037 [P] [US2] Add terminal capability detection to ColorTheme.__init__() method
- [X] T038 [P] [US2] Implement ASCII fallback for all color methods in ColorTheme
- [X] T039 [US2] Update format_task_brief() in `src/ui/formatters.py` to use color theme (depends on T034, T035, T036)
- [X] T040 [US2] Update format_task_detailed() in `src/ui/formatters.py` to use color theme
- [X] T041 [US2] Add color support to menu title and separator rendering in InteractiveMenu
- [X] T042 [US2] Add help text with dim color to InteractiveMenu footer
- [X] T043 [US2] Add success/error/warning message rendering to ScreenManager
- [X] T044 [US2] Test color rendering on Windows Terminal, PowerShell, and Unix terminals
- [X] T045 [US2] Test ASCII fallback by simulating limited terminal capabilities

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently. Users can navigate menus with arrow keys and see color-coded task information.

---

## Phase 5: User Story 3 - Interactive Task List Navigation (Priority: P3)

**Goal**: Enable users to navigate through tasks using arrow keys and select a task to view contextual actions (edit, delete, toggle complete)

**Independent Test**: Navigate to "View All Tasks", use arrow keys to select a task, press Enter to see contextual menu, and perform actions (edit/delete/complete). Verify empty list handling.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T046 [P] [US3] Unit test for InteractiveTaskList navigation in `tests/unit/test_interactive_task_list.py`
- [ ] T047 [P] [US3] Unit test for empty task list handling in `tests/unit/test_interactive_task_list.py`
- [ ] T048 [P] [US3] Integration test for task selection workflow in `tests/integration/test_interactive_workflows.py`
- [ ] T049 [P] [US3] Integration test for contextual menu actions in `tests/integration/test_interactive_workflows.py`

### Implementation for User Story 3

- [X] T050 [P] [US3] Implement InteractiveTaskList.show() method for task list navigation
- [X] T051 [P] [US3] Implement empty list handling in InteractiveTaskList
- [X] T052 [P] [US3] Implement keyboard shortcut handling ('a' for add task) in InteractiveTaskList
- [X] T053 [P] [US3] Implement task selection and return logic in InteractiveTaskList
- [X] T054 [US3] Add show_task_actions() method to MenuController for contextual menu (depends on T050, T051, T052, T053)
- [X] T055 [US3] Implement contextual menu options: View Details, Edit, Delete, Toggle Complete, Back
- [X] T056 [US3] Add handle_view_all() method to MenuController using InteractiveTaskList
- [X] T057 [US3] Add handle_task_actions() method to MenuController for action routing
- [X] T058 [US3] Implement task action handlers: view_details(), edit_task(), delete_task(), toggle_complete()
- [X] T059 [US3] Add visual confirmation messages for task actions using ScreenManager
- [X] T060 [US3] Test task list navigation with 0, 1, 5, and 50+ tasks
- [X] T061 [US3] Test contextual menu actions for all task operations

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently. Users can navigate menus, see color-coded tasks, and manage tasks through interactive selection.

---

## Phase 6: User Story 4 - Keyboard Shortcuts and Productivity (Priority: P3)

**Goal**: Provide single-key shortcuts for common actions (a=add, f=filter, s=sort, /=search) to accelerate navigation

**Independent Test**: Press single-key shortcuts from the main menu and task list contexts and verify the corresponding action executes immediately.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T062 [P] [US4] Unit test for keyboard shortcut handling in `tests/unit/test_input_handler.py`
- [ ] T063 [P] [US4] Integration test for shortcut workflows in `tests/integration/test_interactive_workflows.py`

### Implementation for User Story 4

- [X] T064 [P] [US4] Add keyboard shortcut detection to InputHandler.get_key() method
- [X] T065 [P] [US4] Add shortcut handling to InteractiveMenu for global shortcuts
- [X] T066 [P] [US4] Add shortcut handling to InteractiveTaskList for context-specific shortcuts
- [X] T067 [US4] Implement shortcut routing in MenuController.run() method (depends on T064, T065, T066)
- [X] T068 [US4] Add 'a' shortcut for add task (calls handle_add_task())
- [X] T069 [US4] Add 'f' shortcut for filter menu (calls handle_filter())
- [X] T070 [US4] Add 's' shortcut for sort menu (calls handle_sort())
- [X] T071 [US4] Add '/' shortcut for search (calls handle_search())
- [X] T072 [US4] Add '?' shortcut for help overlay (shows available shortcuts)
- [X] T073 [US4] Add 'q' shortcut as alternative to Esc for exit
- [X] T074 [US4] Add help overlay display method to ScreenManager
- [X] T075 [US4] Test all shortcuts from main menu and task list contexts

**Checkpoint**: All user stories should now be independently functional. Users have full interactive navigation with arrow keys, color-coded visuals, task management, and productivity shortcuts.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T076 [P] Add comprehensive error handling for terminal operations
- [X] T077 [P] Add input validation and user feedback for invalid operations
- [X] T078 [P] Optimize screen refresh performance for large task lists
- [ ] T079 [P] Add terminal resize handling with graceful refresh (OPTIONAL)
- [ ] T080 [P] Add input debouncing for rapid arrow-key presses (OPTIONAL)
- [ ] T081 [P] Add scrolling support for task lists exceeding terminal height (OPTIONAL)
- [ ] T082 [P] Add page indicators for long task lists (OPTIONAL)
- [ ] T083 [P] Add comprehensive logging for debugging (OPTIONAL)
- [ ] T084 [P] Add unit tests for all remaining components (OPTIONAL per spec header)
- [ ] T085 [P] Add integration tests for all workflows (OPTIONAL per spec header)
- [X] T086 [P] Test cross-platform compatibility (Windows Terminal, PowerShell, bash, zsh)
- [X] T087 [P] Verify no regressions in existing Phase I features
- [ ] T088 [P] Update documentation with interactive UI usage (OPTIONAL)
- [X] T089 [P] Add user help and onboarding messages
- [X] T090 [P] Final validation against all acceptance criteria

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Enhances US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Extends US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - Optimizes US1/US2/US3 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Input handler and color theme before interactive components
- Interactive components before menu controller integration
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Input handler, color theme, and screen manager tasks marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all input and color foundation tasks together:
Task: "T017 Implement KeyInput dataclass in src/ui/input_handler.py"
Task: "T018 Implement InputHandler.get_key() method in src/ui/input_handler.py"
Task: "T019 Implement ColorTheme class in src/ui/color_theme.py"
Task: "T020 Implement ColorTheme.highlight() method in src/ui/color_theme.py"
Task: "T021 Implement ScreenManager class in src/ui/screen_manager.py"

# Launch interactive menu implementation after foundation:
Task: "T022 Implement InteractiveMenu.show() method in src/ui/interactive_menu.py"
Task: "T023 Implement arrow key handling in InteractiveMenu"
Task: "T024 Implement selection highlighting in InteractiveMenu"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Arrow-Key Menu Navigation)
   - Developer B: User Story 2 (Visual Clarity and Color Enhancement)
   - Developer C: User Story 3 (Interactive Task List Navigation)
   - Developer D: User Story 4 (Keyboard Shortcuts and Productivity)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Task Summary

**Total Tasks**: 90
**Parallel Tasks**: 62 (69% parallelizable)
**Sequential Tasks**: 28 (31% dependent)

**Tasks by User Story**:
- User Story 1 (P1): 16 tasks (11 parallel, 5 dependent)
- User Story 2 (P2): 12 tasks (10 parallel, 2 dependent)
- User Story 3 (P3): 12 tasks (8 parallel, 4 dependent)
- User Story 4 (P3): 11 tasks (9 parallel, 2 dependent)

**MVP Scope**: Phase 1 (5 tasks) + Phase 2 (13 tasks) + Phase 3 (16 tasks) = 34 tasks

**Full Implementation**: All 90 tasks across 7 phases

---

## Validation Checklist

- [ ] All tasks follow strict checklist format (checkbox, ID, labels, file paths)
- [ ] All user stories have independent test criteria
- [ ] All dependencies are clearly marked
- [ ] Parallel opportunities are identified
- [ ] MVP scope is clearly defined
- [ ] Full implementation path is clear

**Status**: ✅ TASKS GENERATION COMPLETE
**Ready for**: `/sp.implement` command to execute implementation plan