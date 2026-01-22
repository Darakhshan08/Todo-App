# Phase I - Advanced Interactive In-Memory Todo CLI

A production-quality, menu-driven command-line todo application built with Python 3.13+. Features advanced task management including priorities, tags, due dates, and recurring tasks - all in-memory with zero persistence.

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
uv run main.py
```

The application will display a numbered menu with the following options:

1. **Add Task** - Create a new task with title, description, priority, tags, due date, and recurrence
2. **View All Tasks** - Display all tasks with their details
3. **View Task Details** - Show complete information for a specific task
4. **Update Task** - Modify task properties (title, description, priority, tags, due date, recurrence)
5. **Delete Task** - Remove a task (with confirmation)
6. **Mark Complete/Incomplete** - Toggle task completion status
7. **Search Tasks** - Find tasks by keyword in title or description
8. **Filter Tasks** - Display tasks matching specific criteria (priority, tags, completion status)
9. **Sort Tasks** - Reorder display by ID, priority, due date, or completion
10. **Clear Screen** - Clear the terminal display
11. **Exit** - Quit the application

## Navigation

- Enter the number corresponding to your choice
- Follow the prompts for each operation
- Type exact values as requested (case-sensitive for tags)
- Press Enter to skip optional fields
- Invalid input displays error messages with recovery options

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
- **Standard Library Only**: No external dependencies beyond Python 3.13+

## Architecture

The application follows clean architecture principles with four layers:

- **Presentation Layer** (`src/ui/`): Menu controller, formatters, input prompts
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
│   ├── ui/            # Presentation layer (MenuController, formatters, prompts)
│   └── utils/         # Utilities (date_utils)
├── tests/             # Test files (unit, integration, performance)
├── specs/             # Specification and planning documents
├── main.py            # Application entry point
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

### Running Tests
```bash
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

This application implements Phase I of the Evolution of Todo project. For complete specification details, see:

- **Specification**: `specs/007-phase1-todo-cli/spec.md`
- **Implementation Plan**: `specs/007-phase1-todo-cli/plan.md`
- **Task List**: `specs/007-phase1-todo-cli/tasks.md`

## License

[Specify license here]

## Contributing

[Specify contribution guidelines here]
