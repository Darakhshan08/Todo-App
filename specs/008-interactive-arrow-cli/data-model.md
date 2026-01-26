# Data Model: Interactive Arrow-Key Driven CLI UI

**Feature**: Interactive Arrow-Key Driven CLI UI
**Date**: 2026-01-22
**Status**: No new entities - UI layer only

## Overview

This feature does NOT introduce new data entities. All changes are confined to the UI presentation layer. Existing Phase I domain models remain unchanged.

## Existing Entities (No Modifications)

### Task
**Location**: `src/models/task.py`
**Status**: ✅ NO CHANGES REQUIRED

Domain model representing a todo task with all attributes (id, title, description, completed, priority, tags, due_date, recurrence_rule). This entity is used by the interactive UI for display and selection but requires no modifications.

### Priority
**Location**: `src/models/task.py`
**Status**: ✅ NO CHANGES REQUIRED

Enum representing task priority levels (HIGH, MEDIUM, LOW). The interactive UI will render these with color coding (red, yellow, green) but the enum definition remains unchanged.

### RecurrenceRule
**Location**: `src/models/task.py`
**Status**: ✅ NO CHANGES REQUIRED

Enum representing recurring task patterns (NONE, DAILY, WEEKLY, MONTHLY). The interactive UI will display these with formatted labels but the enum definition remains unchanged.

### SortOption
**Location**: `src/models/task.py`
**Status**: ✅ NO CHANGES REQUIRED

Enum for task sorting options (DUE_DATE, PRIORITY, ALPHABETICAL). The interactive UI will present these as menu choices but the enum definition remains unchanged.

## New UI State Types (Internal Only)

These are ephemeral UI state types that do NOT represent domain entities:

### MenuState (Internal)
**Purpose**: Track current menu selection state in interactive components
**Lifecycle**: Exists only during menu navigation, discarded on selection
**Not Persisted**: Lives in memory during UI interaction only

**Attributes**:
- `selected_index: int` - Currently highlighted menu option (0-based)
- `menu_items: List[str]` - Available menu options
- `title: str` - Menu title for display

**Rationale**: This is UI state, not domain data. No need to persist or expose outside UI layer.

### TaskListState (Internal)
**Purpose**: Track task list navigation state
**Lifecycle**: Exists only during task list viewing, discarded on menu exit
**Not Persisted**: Lives in memory during UI interaction only

**Attributes**:
- `tasks: List[Task]` - Tasks being displayed (from service layer)
- `selected_index: int` - Currently highlighted task
- `scroll_offset: int` - For long lists exceeding terminal height

**Rationale**: This is UI state composing domain entities (Task) for presentation. No modifications to Task entity needed.

### KeyInput (Internal)
**Purpose**: Represent captured keyboard input
**Lifecycle**: Instantaneous - created on key press, consumed immediately
**Not Persisted**: Ephemeral input event

**Attributes**:
- `key_name: str` - Key identifier (e.g., "KEY_UP", "KEY_DOWN", "KEY_ENTER")
- `is_printable: bool` - Whether key represents printable character
- `char: Optional[str]` - Character value for printable keys

**Rationale**: This is an input event wrapper over blessed's `inkey()` result. Provides abstraction for testability.

## Entity Relationships (Unchanged)

```text
[No changes to existing relationships]

TaskService → Task (creates, updates, queries)
Task → Priority (has-a relationship via enum)
Task → RecurrenceRule (has-a relationship via enum)
InMemoryTaskStore → Task (stores list of tasks)

[New UI layer relationships - no domain impact]

InteractiveMenu → MenuState (internal state)
InteractiveTaskList → Task (displays, no modifications)
InteractiveTaskList → TaskListState (internal state)
InputHandler → KeyInput (captures and translates)
```

## Data Flow (UI Layer Only)

```text
User Input:
  Terminal (arrow keys)
  → blessed.inkey()
  → InputHandler.get_key()
  → KeyInput
  → InteractiveMenu/InteractiveTaskList
  → Menu selection / Task selection

Display Output:
  Task (from TaskService)
  → ColorTheme.format_*()
  → ANSI color codes
  → blessed.Terminal
  → Terminal display
```

## Validation Rules (Unchanged)

All existing validation rules in the domain models remain unchanged. The interactive UI enforces the same validation as the original numeric menu system:

- Task title required (non-empty)
- Priority must be valid enum value
- Due date must be valid YYYY-MM-DD format
- Tags are comma-separated strings
- Recurrence rule must be valid enum value

## State Transitions (UI State Only)

### MenuState Transitions
```text
INITIAL → NAVIGATING (user presses arrow keys)
NAVIGATING → SELECTED (user presses Enter)
NAVIGATING → CANCELLED (user presses Esc)
```

### TaskListState Transitions
```text
VIEWING → NAVIGATING (user presses arrow keys)
NAVIGATING → CONTEXTUAL_MENU (user presses Enter on task)
CONTEXTUAL_MENU → ACTION_SELECTED (user selects action)
NAVIGATING → VIEWING (user presses Esc)
```

## No Persistence Changes

This feature maintains Phase I's in-memory storage constraint:
- ✅ All data remains in `InMemoryTaskStore`
- ✅ No database, file I/O, or external storage
- ✅ Data lifecycle unchanged (exists for process lifetime only)

## No API Changes

Since this is a CLI-only feature:
- ✅ No REST endpoints
- ✅ No GraphQL schemas
- ✅ No external API contracts
- ✅ All interaction through terminal I/O

## Summary

**Domain Model Impact**: ZERO
- No new domain entities
- No modifications to existing entities (Task, Priority, RecurrenceRule, SortOption)
- No changes to relationships, validation, or business logic

**UI State**: NEW (Internal Only)
- MenuState, TaskListState, KeyInput are ephemeral UI state types
- Not exposed outside UI layer
- Not persisted or part of domain model

**Rationale**: This is purely a UI presentation upgrade. The interactive experience is achieved through new UI components that compose and display existing domain entities with enhanced visual rendering. Clean separation between UI and domain layers is preserved.
