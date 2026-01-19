# Tasks: CLI Specification Refinements

**Input**: Design documents from `specs/006-refine-cli-specs/`
**Prerequisites**: spec.md (defines refinements needed for specs 001, 003, 004), plan.md (implementation strategy)

**Tests**: No test tasks required - this is a documentation-only feature

**Organization**: Tasks are grouped by user story to enable independent implementation and validation of each refinement category.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

All tasks modify existing specification markdown files in `specs/` directory:
- `specs/001-add-task/spec.md` (Add Task specification)
- `specs/003-update-task/spec.md` (Update Task specification)
- `specs/004-delete-task/spec.md` (Delete Task specification)
- `specs/002-view-task-list/spec.md` (View Task List - review only)
- `specs/005-mark-complete/spec.md` (Mark Complete - review only)

---

## Phase 1: Setup (Validation & Backup)

**Purpose**: Validate existing specs and create backup before modifications

- [X] T001 Read and validate specs/001-add-task/spec.md exists and is accessible
- [X] T002 Read and validate specs/003-update-task/spec.md exists and is accessible
- [X] T003 Read and validate specs/004-delete-task/spec.md exists and is accessible
- [X] T004 Create git commit checkpoint before spec modifications with message "Checkpoint before CLI spec refinements"

---

## Phase 2: User Story 1 - Multi-line Description Input Clarity (Priority: P1) 🎯

**Goal**: Define deterministic multi-line input method across Add Task and Update Task specs

**Independent Test**: Read updated specs 001 and 003, verify they contain identical multi-line input instructions with concrete example, confirm implementer can unambiguously understand how to parse `\n` escape sequences

### Implementation for User Story 1

- [X] T005 [P] [US1] Update specs/001-add-task/spec.md edge cases section: Add new edge case "Multi-line Description Input Method" with text "To enter multi-line descriptions, users enter literal `\n` escape sequences in console input, which the system interprets as newline characters for storage and display. Example: Entering 'Step 1\nStep 2\nStep 3' creates a three-line description."
- [X] T006 [P] [US1] Update specs/003-update-task/spec.md edge cases section: Add new edge case "Multi-line Description Input Method" with identical text as spec 001 for consistency
- [X] T007 [US1] Update specs/001-add-task/spec.md edge case "Multi-line Description": Modify existing case to reference the new input method and clarify that `\n` sequences are parsed during input processing
- [X] T008 [US1] Validate both specs (001 and 003) contain consistent multi-line input documentation by reading both files and comparing the Multi-line Description Input Method edge case text

**Checkpoint**: Specs 001 and 003 now have deterministic multi-line input method documented

---

## Phase 3: User Story 2 - Field Update Semantics Distinction (Priority: P1) 🎯

**Goal**: Eliminate ambiguity between "skip field update" and "clear field" in Update Task spec

**Independent Test**: Read updated spec 003, verify FR-006/FR-007 clearly state "Press Enter to keep current [field]", verify edge cases document that field clearing is not supported in Phase I, confirm no ambiguity remains

### Implementation for User Story 2

- [X] T009 [US2] Update specs/003-update-task/spec.md FR-006: Change requirement text to "System MUST prompt the user to enter a new title with the instruction 'Press Enter to keep current title'"
- [X] T010 [US2] Update specs/003-update-task/spec.md FR-007: Change requirement text to "System MUST prompt the user to enter a new description with the instruction 'Press Enter to keep current description'"
- [X] T011 [US2] Update specs/003-update-task/spec.md edge case "Cancel Update Operation": Reword to "Field Skip (Keep Current Value) - When user presses Enter without text for a field, the system keeps the current value unchanged (skip update). The field is not cleared."
- [X] T012 [US2] Add new edge case to specs/003-update-task/spec.md: "Field Clearing Not Supported - Phase I does not support clearing a field to empty after it has been set. To clear a description, users must update it to a single space character or wait for future phases that support explicit clearing."
- [X] T013 [US2] Add new edge case to specs/003-update-task/spec.md: "No Changes Made - When user skips both title and description updates (presses Enter for both), the task remains unchanged and the system displays 'No changes made. Task remains unchanged.'"
- [X] T014 [US2] Validate spec 003 has clear distinction between skip and clear semantics by reading FR-006, FR-007, and all updated edge cases
- [X] T015 [US2] Remove or update specs/003-update-task/spec.md User Story 2 Acceptance Scenario 3 (field clearing scenario): This scenario contradicts the "Field Clearing Not Supported" design decision. Either remove it entirely or update it to test field skip behavior instead.

**Checkpoint**: Spec 003 now unambiguously defines Enter key = skip update, with field clearing deferred

---

## Phase 4: User Story 3 - Confirmation Retry Limit Safety (Priority: P1) 🎯

**Goal**: Add retry limit to confirmation prompts in Delete Task spec to prevent infinite loops

**Independent Test**: Read updated spec 004, verify FR-009 specifies maximum 3 retry attempts, verify edge cases document the retry exhaustion behavior, confirm implementer knows to add retry counter

### Implementation for User Story 3

- [X] T016 [US3] Update specs/004-delete-task/spec.md FR-009: Replace entire requirement text with "System MUST accept up to 3 invalid confirmation attempts, re-prompting with 'Error: Invalid input. Please enter 'yes' or 'no'.' after each invalid entry. After the 3rd invalid attempt, system displays 'Error: Maximum retry attempts exceeded. Returning to main menu.' and cancels the deletion."
- [X] T017 [US3] Add new edge case to specs/004-delete-task/spec.md: "Confirmation Retry Exhaustion - When user provides invalid confirmation input 3 times consecutively, the system cancels the deletion operation, displays the max retry error message, and returns to the main menu without deleting the task."
- [X] T018 [US3] Update specs/004-delete-task/spec.md edge case "Invalid Confirmation Input": Add clarification that system re-prompts up to 3 times before exhausting retries
- [X] T019 [US3] Validate spec 004 has clear retry limit of 3 attempts documented by reading FR-009 and all confirmation-related edge cases

**Checkpoint**: Spec 004 now prevents infinite loops with maximum 3 retry attempts

---

## Phase 5: User Story 4 - Error Message Prefix Consistency (Priority: P2)

**Goal**: Ensure all error messages across Phase I specs use consistent "Error: [description]" format

**Independent Test**: Read all updated specs (001-005), search for all error messages, verify every message begins with "Error:" prefix, confirm consistent pattern

### Implementation for User Story 4

- [X] T020 [P] [US4] Review specs/001-add-task/spec.md: Search for all error messages and verify they have "Error:" prefix (should already be correct, document findings)
- [X] T021 [P] [US4] Review specs/002-view-task-list/spec.md: Search for all error messages and verify they have "Error:" prefix (should already be correct, document findings)
- [X] T022 [P] [US4] Review specs/003-update-task/spec.md: Search for all error messages and ensure "Error:" prefix consistency (verify no changes needed after US2 updates)
- [X] T023 [P] [US4] Review specs/005-mark-complete/spec.md: Search for all error messages and verify they have "Error:" prefix (should already be correct, document findings)
- [X] T024 [US4] Validate specs/004-delete-task/spec.md FR-009 now uses "Error: Invalid input. Please enter 'yes' or 'no'." after T016 update
- [X] T025 [US4] Perform final cross-spec review of all error messages in specs 001-005 for format consistency by reading all error message text

**Checkpoint**: All Phase I specs now use consistent error message format

---

## Phase 6: Display Format Clarifications

**Goal**: Add explicit display format specification for Update Task current value display

**Independent Test**: Read updated spec 003 FR-005, verify it specifies the exact format for displaying current task values before prompting for updates

### Implementation for Display Format

- [X] T026 Update specs/003-update-task/spec.md FR-005: Append exact format specification to requirement text - "System MUST display current task details before prompting for updates in the format:\n```\nTask ID: task-XXX\nCurrent title: [current title value]\nCurrent description: [current description value or 'No description']\n```"
- [X] T027 Validate spec 003 FR-005 contains complete display format specification by reading the updated requirement text

**Checkpoint**: Spec 003 now has unambiguous display format for current values

---

## Phase 7: Final Validation & Documentation

**Purpose**: Comprehensive validation of all spec refinements and completion documentation

- [X] T028 Validate all 13 functional requirements (FR-001 through FR-013) have been applied to specs 001, 003, 004 by reading each requirement and its target location
- [X] T029 Perform acceptance scenario verification: Read each updated spec and confirm all 15 acceptance scenarios from spec 006 are satisfied
- [X] T030 Verify all 7 success criteria from spec 006 are met (SC-001 through SC-007) by checking each criterion against the refined specs
- [X] T031 Create git commit with all spec refinements and descriptive commit message "Apply CLI spec refinements: multi-line input, field semantics, retry limits, error consistency, display format"
- [X] T032 Update specs/006-refine-cli-specs/spec.md status from "Draft" to "Complete"
- [X] T033 Document completion summary in specs/006-refine-cli-specs/COMPLETION.md with list of all changes applied

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **User Story 1 (Phase 2)**: Depends on Setup completion - Independent from other user stories
- **User Story 2 (Phase 3)**: Depends on Setup completion - Independent from other user stories
- **User Story 3 (Phase 4)**: Depends on Setup completion - Independent from other user stories
- **User Story 4 (Phase 5)**: Depends on Phases 2-4 completion (needs all specs refined first to review)
- **Display Format (Phase 6)**: Depends on Setup completion - Independent from user stories
- **Final Validation (Phase 7)**: Depends on all previous phases (Phases 2-6)

### User Story Dependencies

- **User Story 1 (P1)**: Independent - modifies specs 001 and 003 (multi-line input edge cases)
- **User Story 2 (P1)**: Independent - modifies spec 003 only (FR-006, FR-007, edge cases)
- **User Story 3 (P1)**: Independent - modifies spec 004 only (FR-009, edge cases)
- **User Story 4 (P2)**: Depends on US1-US3 completion - reviews all specs 001-005 for consistency

### Within Each User Story

- Tasks within US1: T005 and T006 can run in parallel (different files), T007 depends on T005 (same file), T008 validates all
- Tasks within US2: Sequential (T009-T015 all modify spec 003), T014-T015 validates
- Tasks within US3: Sequential (T016-T018 all modify spec 004), T019 validates
- Tasks within US4: T020-T023 can run in parallel (different files), T024-T025 sequential validation

### Parallel Opportunities

- **Phase 1**: Tasks T001, T002, T003 can all run in parallel (reading different files)
- **Phase 2 (US1)**: Tasks T005 and T006 can run in parallel (modifying different spec files: 001 vs. 003)
- **Phase 5 (US4)**: Tasks T020, T021, T022, T023 can run in parallel (reviewing different spec files)
- **Phases 2, 3, 4, 6**: Can theoretically start in parallel after Phase 1, but recommend sequential to avoid complexity

**Recommended Execution**: Sequential by phase to maintain clarity and avoid any potential conflicts in spec 003 which is modified by multiple phases (US1, US2, Phase 6)

---

## Parallel Example: User Story 1

```bash
# Launch multi-line input documentation tasks in parallel (different files):
Task T005: "Update specs/001-add-task/spec.md edge cases section (multi-line input)"
Task T006: "Update specs/003-update-task/spec.md edge cases section (multi-line input)"
```

## Parallel Example: User Story 4

```bash
# Launch error message review tasks in parallel (different files):
Task T020: "Review specs/001-add-task/spec.md error messages"
Task T021: "Review specs/002-view-task-list/spec.md error messages"
Task T022: "Review specs/003-update-task/spec.md error messages"
Task T023: "Review specs/005-mark-complete/spec.md error messages"
```

---

## Implementation Strategy

### MVP First (User Stories 1-3 Only - All P1)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: User Story 1 - Multi-line Input (T005-T008)
3. Complete Phase 3: User Story 2 - Field Semantics (T009-T015)
4. Complete Phase 4: User Story 3 - Retry Limits (T016-T019)
5. **STOP and VALIDATE**: Verify all P1 refinements are complete and consistent
6. Optionally proceed to P2 (User Story 4) and Phase 6-7

### Incremental Delivery

1. Complete Setup → Specs validated and backed up
2. Add User Story 1 → Multi-line input method clarified (specs 001, 003)
3. Add User Story 2 → Field update semantics disambiguated (spec 003)
4. Add User Story 3 → Confirmation retry limits added (spec 004)
5. Add User Story 4 → Error message consistency ensured (all specs)
6. Add Display Format → Current value display specified (spec 003)
7. Final Validation → All refinements verified and documented

### Sequential Execution Strategy (Recommended)

With single implementer modifying multiple specs:

1. Complete Phase 1: Setup (read and validate all specs, create backup)
2. Complete Phase 2: User Story 1 (specs 001 and 003 - multi-line input)
3. Complete Phase 3: User Story 2 (spec 003 - field semantics)
4. Complete Phase 4: User Story 3 (spec 004 - retry limits)
5. Complete Phase 5: User Story 4 (cross-spec error message review)
6. Complete Phase 6: Display Format (spec 003 - current value display)
7. Complete Phase 7: Final validation and commit

**Rationale**: Sequential execution prevents merge conflicts when editing spec 003 multiple times (US1, US2, US4, Phase 6 all modify it). Simple, clear, low-risk approach for documentation editing.

### Parallel Team Strategy (Alternative)

If multiple team members available:

1. Team completes Phase 1: Setup together
2. After Phase 1:
   - Developer A: User Story 1 (specs 001, 003 - edge cases only)
   - Developer B: User Story 3 (spec 004 - retry limits)
   - Wait for both to complete
3. Developer C: User Story 2 (spec 003 - requirements + edge cases)
4. Developer D: User Story 4 (cross-spec review)
5. Developer E: Phase 6 Display Format (spec 003 - FR-005)
6. Team: Phase 7 Final Validation together

**Note**: Requires coordination to avoid conflicts in spec 003

---

## Notes

- [P] tasks = different files, no dependencies, safe for parallel execution
- [Story] label maps task to specific user story for traceability
- Each user story delivers independently verifiable spec refinements
- No code is written - all tasks edit existing markdown spec files
- After completion, specs 001, 003, 004 will be implementation-ready with zero ambiguity
- Spec 006 itself documents the meta-feature (refining other specs)
- Total refinements: 13 functional requirements across 3 Phase I specs
- Total tasks: 33 (T001-T033)
- Commit frequently: after each user story phase completion for easy rollback if needed
- All changes are reversible via git - documentation editing is low-risk
