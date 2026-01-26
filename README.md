# Phase I - Advanced Interactive In-Memory Todo CLI

A production-quality, **arrow-key driven** command-line todo application built with Python 3.13+. Features advanced task management including priorities, tags, due dates, and recurring tasks with a fully interactive, color-enhanced terminal UI - all in-memory with zero persistence.

## 🚀 Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd Todo-App

# Run the application
uv run python main.py
```

**Navigation**: Use ↑↓ arrow keys to navigate, Enter to select, Esc to go back, ? for help.

---

## ✨ Interactive UI (NEW!)

Navigate the entire application using **arrow keys** - no more typing numbers! The enhanced interface features:

- **Arrow-Key Navigation**: Use ↑↓ to navigate all menus and task lists, Enter to select
- **Color-Coded Display**: Priorities (🔴 HIGH, 🟡 MEDIUM, 🟢 LOW) and statuses visually highlighted
- **Visual Selection**: Clear highlighting shows your current selection
- **Keyboard Shortcuts**: Single-key commands (a=add, f=filter, s=sort, /=search, ?=help, q=quit)
- **Interactive Task Lists**: Select tasks with arrow keys to view contextual action menus
- **Smart Fallback**: Automatic ASCII mode for terminals without color support
- **Cross-Platform**: Works on Windows Terminal, PowerShell 7+, bash, and zsh

## Features

### Basic (P1 - MVP)
- **Task Management**: Add, view, update, delete, and complete tasks
- **Task Details**: Titles with optional descriptions
- **Safe Deletion**: Confirmation prompts to prevent accidental data loss
- **Graceful Lifecycle**: Clean startup and exit with clear feedback

### Intermediate (P2 - Organization)
- **Priority Management**: HIGH, MEDIUM, LOW priority levels
- **Tag Organization**: Multiple tags per task for categorization
- **Search & Filter**: Find tasks by title, description, priority, tags, completion status
- **Sort Tasks**: Order by ID, priority, due date, or completion status

### Advanced (P3 - Intelligence)
- **Due Date Management**: Set and track task deadlines
- **Recurring Tasks**: Automatic DAILY, WEEKLY, MONTHLY task generation

## Requirements

- Python 3.13 or higher
- UV package manager
- blessed 1.27.0+ (terminal UI library - installed automatically)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Todo-App
   ```

2. Ensure UV is installed:
   ```bash
   # Install UV if not already installed
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

## Usage

Launch the application using UV:

```bash
uv run python main.py
```

The application displays an **interactive arrow-key menu** with the following options:

- **Add Task** - Create a new task with interactive priority and recurrence selection
- **View All Tasks** - Navigate tasks with arrow keys, select for contextual actions
- **Search Tasks** - Find tasks by keyword in title or description
- **Filter Tasks** - Interactive filter menus for status, priority, and tags
- **Sort Tasks** - Interactive sort options (due date, priority, alphabetical)
- **Mark Complete/Incomplete** - Toggle task completion status
- **Update Task** - Modify task properties with interactive menus
- **Delete Task** - Remove a task (with confirmation)
- **View Recurring Tasks** - Display tasks with recurrence rules
- **Exit** - Quit the application (Esc or q)

## Navigation

### Arrow-Key Controls
- **↑ ↓ (Arrow Keys)**: Navigate through menus and task lists
- **Enter**: Select the highlighted option or task
- **Esc** or **q**: Go back to previous menu or exit application

### Keyboard Shortcuts (from main menu)
- **a**: Add a new task
- **f**: Open filter menu
- **s**: Open sort menu
- **/**: Search tasks
- **?**: Show help overlay with all shortcuts
- **q**: Quit application

### Text Input
- Follow the prompts for text fields (title, description, tags, dates)
- Type exact values as requested (case-sensitive for tags)
- Press Enter to skip optional fields
- Invalid input displays error messages with recovery options

### Interactive Selections
- All menus use arrow-key navigation (no number typing needed)
- Priority and recurrence selections use arrow-key menus
- Filter and sort options use arrow-key menus
- Task selection uses arrow-key navigation with contextual action menus

## Data Model

### Task Properties
- **ID**: Unique sequential identifier (auto-generated, immutable)
- **Title**: Required, 1-200 characters
- **Description**: Optional, up to 1000 characters
- **Completed**: Boolean status (true/false)
- **Priority**: HIGH, MEDIUM, or LOW (default: MEDIUM)
- **Tags**: List of strings (optional, comma-separated)
- **Due Date**: Optional date in YYYY-MM-DD format
- **Recurrence Rule**: NONE (default), DAILY, WEEKLY, or MONTHLY

### Task Lifecycle
1. **Creation**: Task assigned next sequential ID
2. **Active**: Task available for viewing, updating, completing
3. **Completed**: Task marked done, ID preserved
4. **Deleted**: Task removed from store, ID never reused
5. **Session End**: All data lost on exit (in-memory only)

## Important Notes

- **No Persistence**: All data is stored in memory and lost when the application exits
- **Deterministic Behavior**: No AI, no randomness - all operations are predictable
- **Single User**: Designed for single-user, single-session use
- **Interactive UI**: Requires terminal with arrow-key support (blessed library handles cross-platform compatibility)
- **ASCII Fallback**: Automatically degrades to ASCII mode on terminals without color support
- **Dependencies**: blessed 1.27.0+ for terminal UI (automatically installed with UV)

## Architecture

The application follows clean architecture principles with four layers:

- **Presentation Layer** (`src/ui/`): Interactive UI components, menu controller, formatters, input handlers
  - Interactive components: `interactive_menu.py`, `interactive_task_list.py`
  - UI foundation: `input_handler.py`, `color_theme.py`, `screen_manager.py`
  - Controllers: `menu_controller.py`, `formatters.py`
- **Service Layer** (`src/services/`): Business logic, validation
- **Domain Layer** (`src/models/`): Task entity, enums (Priority, RecurrenceRule)
- **Data Layer** (`src/store/`): In-memory task storage

## Development

### Project Structure
```
Todo-App/
├── src/
│   ├── models/        # Domain models (Task, enums)
│   ├── services/      # Business logic (TaskService, ValidationService)
│   ├── store/         # Data layer (TaskStore)
│   ├── ui/            # Presentation layer (interactive UI + controllers)
│   │   ├── interactive_menu.py       # Arrow-key menu navigation
│   │   ├── interactive_task_list.py  # Arrow-key task selection
│   │   ├── input_handler.py          # Keyboard input capture
│   │   ├── color_theme.py            # Color rendering & themes
│   │   ├── screen_manager.py         # Terminal operations
│   │   ├── menu_controller.py        # Main controller
│   │   └── formatters.py             # Display formatters
│   └── utils/         # Utilities (date_utils)
├── tests/             # Test files (unit, integration, performance)
├── specs/             # Specification and planning documents
│   ├── 007-phase1-todo-cli/          # Phase I base implementation
│   └── 008-interactive-arrow-cli/    # Interactive UI upgrade
├── main.py            # Application entry point
├── test_interactive.py  # Interactive component tests
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

### Running Tests
```bash
# Interactive component tests (quick validation)
uv run python test_interactive.py

# Unit tests
uv run pytest tests/unit/

# Integration tests
uv run pytest tests/integration/

# Performance tests
uv run pytest tests/performance/

# All tests with coverage
uv run pytest --cov=src --cov-report=term-missing
```

## Specification

This application implements **Phase I** of the Evolution of Todo project with an **Interactive Arrow-Key UI** upgrade.

### Phase I - Base Implementation ✅ COMPLETE
- **Feature 007**: Core todo CLI with full task management
- **Specification**: `specs/007-phase1-todo-cli/spec.md`
- **Implementation Plan**: `specs/007-phase1-todo-cli/plan.md`
- **Task List**: `specs/007-phase1-todo-cli/tasks.md`
- **Status**: 117/117 tasks complete

### Interactive UI Upgrade ✅ COMPLETE
- **Feature 008**: Arrow-key driven interactive interface
- **Specification**: `specs/008-interactive-arrow-cli/spec.md`
- **Implementation Plan**: `specs/008-interactive-arrow-cli/plan.md`
- **Task List**: `specs/008-interactive-arrow-cli/tasks.md`
- **Status**: 71/71 core tasks complete (100%)
- **Acceptance Tests**: 14/14 passed
- **User Stories**: All 4 complete (arrow navigation, color enhancement, task selection, shortcuts)

## License

[Specify license here]

## Contributing

[Specify contribution guidelines here]
