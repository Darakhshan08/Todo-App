---
name: cli-app-pattern
description: Defines a reusable architectural pattern for deterministic, user-friendly CLI applications
category: architecture
input: CLI feature or behavior requirements
output: Recommended CLI structure, commands, and interaction patterns
context: Used exclusively in Phase I for CLI-based Todo system design and execution
constraints:
  - No application code
  - No agent definitions
  - Architecture and patterns only
---

## Overview

`cli_app_pattern` is a reusable architectural pattern skill for building deterministic, user-friendly command-line applications in Hackathon II – Evolution of Todo. It defines **structure, commands, interaction models, output formats, and best practices** for CLI applications.

**When to use**: Design Phase I console/CLI application architecture, define command structure, specify user interaction patterns, and establish deterministic behavior standards.

**Key responsibility**: Provide a blueprint for building CLI apps that are **predictable, testable, and user-friendly**.

---

## CLI Design Philosophy

### Core Principles

**1. Determinism**: Same input → Same output, always

- No random behavior in output formatting
- Consistent ordering (alphabetical, by ID, by date)
- Predictable error messages
- Reproducible state handling

**2. User-Friendliness**: Clear, helpful interaction

- Obvious command names and syntax
- Helpful error messages (not cryptic)
- Progress feedback (what's happening)
- Status indicators (success/failure, counts)

**3. Scriptability**: Usable in automation

- Machine-readable output formats (JSON option)
- Proper exit codes (success, failure, validation)
- No interactive prompts unless explicitly requested
- Piping support (stdin/stdout chains)

**4. Predictability**: Behavior is obvious

- Consistent argument ordering
- Predictable command structure (verbs, nouns)
- Clear documentation (--help, README)
- No hidden side effects

**5. Simplicity**: Keep it focused

- One tool does one thing well
- Clear scope boundaries
- Minimal dependencies
- Easy to understand and extend

---

## CLI Application Architecture

### Three-Tier Structure

```
┌─────────────────────────────────────┐
│      User/Command Layer             │  (CLI entry point, command parsing)
│    (main.py, __main__.py, click)    │
├─────────────────────────────────────┤
│      Application Logic Layer        │  (Services, business logic)
│  (services/, models/, repositories) │
├─────────────────────────────────────┤
│      Data/State Layer               │  (In-memory storage, persistence)
│  (data_store.py, serialization)     │
└─────────────────────────────────────┘
```

### Recommended Project Structure

```
todo-app/
├── src/
│   ├── __main__.py              # Entry point (python -m todo_app)
│   ├── main.py                  # CLI command dispatcher
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── add.py               # add task command
│   │   ├── delete.py            # delete task command
│   │   ├── update.py            # update task command
│   │   ├── list.py              # list tasks command
│   │   └── complete.py          # mark complete command
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py              # Task data model
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py      # Business logic
│   ├── storage/
│   │   ├── __init__.py
│   │   └── task_store.py        # Data persistence/retrieval
│   └── utils/
│       ├── __init__.py
│       ├── formatter.py         # Output formatting
│       ├── validators.py        # Input validation
│       └── errors.py            # Custom exceptions
├── tests/
│   ├── test_commands/
│   ├── test_services/
│   ├── test_models/
│   └── test_integration/
├── pyproject.toml               # Project metadata and dependencies
├── README.md                    # User documentation
├── CLAUDE.md                    # Claude Code instructions
└── requirements.txt             # Python dependencies (if not using uv)
```

---

## Command Structure & Naming

### Verb-Based Command Pattern

CLI commands follow a **verb-noun** pattern:

```
todo <verb> <noun> [options] [arguments]

Examples:
  todo add "Buy groceries" "Milk, eggs, bread"
  todo list
  todo list --status pending
  todo update 1 --title "Buy groceries and fruits"
  todo delete 3
  todo complete 2
```

### Standard Commands for Todo App

**Basic CRUD Operations**:

| Command | Syntax | Purpose |
|---------|--------|---------|
| **add** | `todo add TITLE [DESCRIPTION]` | Create new task |
| **list** | `todo list [--status pending\|completed\|all]` | View all tasks |
| **update** | `todo update ID --title TITLE [--description DESC]` | Modify task |
| **delete** | `todo delete ID` | Remove task |
| **complete** | `todo complete ID` | Toggle completion status |

**Utility Commands**:

| Command | Syntax | Purpose |
|---------|--------|---------|
| **help** | `todo help [COMMAND]` | Show help (automatic via --help) |
| **version** | `todo --version` | Display app version |
| **status** | `todo status` | Show app state summary |

### Command Design Best Practices

**1. Consistency**: All commands follow same pattern

```
✅ CONSISTENT:
   todo add <title> <description>
   todo update <id> <title> <description>
   todo delete <id>

❌ INCONSISTENT:
   todo add-task <title>
   todo modify <id> <title>
   todo remove <id>
```

**2. Abbreviations**: Short flags for common options

```
✅ GOOD:
   todo list --status pending      # Long form
   todo list -s pending            # Short form (both work)
   todo update --title "New"        # Long form
   todo update -t "New"             # Short form

❌ BAD:
   Only one form (too restrictive or too cryptic)
```

**3. Optional Arguments**: Clear when required vs optional

```
✅ CLEAR:
   todo add "Title" "Optional description"
              ^required   ^optional

   todo list [--status TYPE]
             ^optional

❌ UNCLEAR:
   todo add "Title" "Description"  (Which is required?)
   todo list STATUS                (Always required?)
```

---

## Input Handling & Validation

### Argument Parsing Strategy

**Use argument parser** (argparse, Click, Typer):

```python
# Pattern: Parse args → Validate → Execute → Format output

def main():
    parser = create_parser()          # Define commands and options
    args = parser.parse_args()         # Parse user input

    try:
        validate_args(args)            # Check for errors
        result = execute_command(args) # Run the command
        format_output(result)          # Display results
    except ValidationError as e:
        print_error(e.message)         # User-friendly error
        exit(1)
    except Exception as e:
        print_error("Unexpected error") # Generic error
        exit(2)

    exit(0)  # Success
```

### Input Validation Rules

**Always validate**:
- ✅ Required fields present
- ✅ Field types correct (ID is integer, title is string)
- ✅ Field lengths within bounds (title not empty, description reasonable)
- ✅ IDs exist before update/delete
- ✅ No duplicate data where needed

**Example Task Model Validation**:

```python
class Task:
    def __init__(self, title: str, description: str = ""):
        if not title or len(title) < 1:
            raise ValueError("Title cannot be empty")
        if len(title) > 200:
            raise ValueError("Title too long (max 200 chars)")
        if len(description) > 1000:
            raise ValueError("Description too long (max 1000 chars)")

        self.title = title
        self.description = description
```

### Error Handling Strategy

**Three-tier error response**:

| Error Type | User Message | Exit Code | Example |
|---|---|---|---|
| **Validation** | Clear, specific problem | 1 | "Task title cannot be empty" |
| **Not Found** | Clear what's missing | 1 | "Task with ID 5 not found" |
| **Unexpected** | Generic, helpful | 2 | "Unexpected error. Contact support." |

**Example**:
```
$ todo delete 999
Error: Task with ID 999 not found
(exit code: 1)

$ todo add ""
Error: Task title cannot be empty
(exit code: 1)

$ todo add "Buy milk" 2>&1 | cat > /tmp/output
(Depending on what happens, exit with 0 or 1/2)
```

---

## Output Formatting

### Three Output Modes

**1. Human-Readable (Default)**

```
$ todo list

Tasks (3 total):
  1. Buy groceries [pending]
  2. Call mom [pending]
  3. Finish report [completed]

Status: 2 pending, 1 completed
```

**2. JSON (--json flag)**

```
$ todo list --json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2026-01-17T10:30:00Z"
  },
  ...
]
```

**3. Compact/Raw (--raw flag)**

```
$ todo list --raw
1 Buy groceries pending
2 Call mom pending
3 Finish report completed
```

### Output Design Principles

**1. Determinism**: Always same order, format

```
✅ DETERMINISTIC:
   - Tasks sorted by ID (ascending)
   - Dates in ISO format (2026-01-17T10:30:00Z)
   - Boolean as true/false (not Yes/No)
   - Counts consistent

❌ NON-DETERMINISTIC:
   - Random order
   - Dates in local timezone
   - Boolean as X/
   - Inconsistent formatting
```

**2. Clarity**: Easy to read and parse

```
✅ CLEAR:
   ID  Title              Status
   1   Buy groceries      pending
   2   Call mom           pending

❌ UNCLEAR:
   Title              pending/completed
   Buy groceries      0
   Call mom           1
```

**3. Scannability**: Users quickly find info

```
✅ SCANNABLE:
   - Status indicators aligned
   - Empty lines between sections
   - Counts at top or bottom
   - ID always first column

❌ HARD TO SCAN:
   - Everything in paragraph form
   - No visual separation
   - Information scattered
```

### Specific Output Patterns

**List Output**:

```
Tasks (N total, X pending, Y completed):
  ID  Title                      Status      Created
  1   Buy groceries              pending     2026-01-17
  2   Call mom                   pending     2026-01-15
  3   Finish project report      completed   2026-01-10
```

**Single Item Output**:

```
Task #1
-------
Title:       Buy groceries
Description: Milk, eggs, bread
Status:      pending
Created:     2026-01-17 10:30 AM
Updated:     2026-01-17 10:30 AM
```

**Success Messages**:

```
✓ Task added (ID: 4)
✓ Task updated
✓ Task deleted
✓ Task marked complete
```

**Error Messages**:

```
✗ Task title cannot be empty
✗ Task with ID 5 not found
✗ Description exceeds maximum length (max 1000 chars)
```

---

## State Management & Persistence

### In-Memory State Pattern (Phase I)

```python
class TaskStore:
    def __init__(self):
        self.tasks: dict[int, Task] = {}  # ID → Task
        self.next_id: int = 1

    def add(self, task: Task) -> int:
        """Add task, return ID"""
        task_id = self.next_id
        self.tasks[task_id] = task
        self.next_id += 1
        return task_id

    def get(self, task_id: int) -> Task:
        """Get task by ID"""
        if task_id not in self.tasks:
            raise NotFoundError(f"Task {task_id} not found")
        return self.tasks[task_id]

    def list(self) -> list[Task]:
        """List all tasks in ID order"""
        return [self.tasks[task_id]
                for task_id in sorted(self.tasks.keys())]

    def update(self, task_id: int, **kwargs) -> Task:
        """Update task fields"""
        task = self.get(task_id)
        for key, value in kwargs.items():
            setattr(task, key, value)
        return task

    def delete(self, task_id: int) -> None:
        """Delete task"""
        if task_id not in self.tasks:
            raise NotFoundError(f"Task {task_id} not found")
        del self.tasks[task_id]
```

### Singleton Pattern for Global State

```python
# Global task store (Phase I specific pattern)
_store = None

def get_store() -> TaskStore:
    """Get global task store"""
    global _store
    if _store is None:
        _store = TaskStore()
    return _store

# Usage in commands
def add_command(title: str, description: str = ""):
    store = get_store()
    task = Task(title, description)
    task_id = store.add(task)
    return {"task_id": task_id, "title": title}
```

### Data Persistence Hooks (for Future Phases)

Structure allows easy upgrade to database:

```python
class TaskStore:
    def __init__(self, persist_handler=None):
        self.tasks = {}
        self.persist_handler = persist_handler

    def add(self, task: Task) -> int:
        task_id = self._get_next_id()
        self.tasks[task_id] = task

        if self.persist_handler:
            self.persist_handler.save(task_id, task)  # Optional: save to DB

        return task_id
```

---

## Interaction Models

### Model 1: Non-Interactive (Recommended for Phase I)

**Pattern**: Command-line arguments → Execute → Exit

```bash
$ todo add "Buy milk"
✓ Task added (ID: 1)

$ todo list
Tasks (1 total):
  1. Buy milk [pending]
```

**Advantages**:
- ✅ Scriptable (can chain commands)
- ✅ Testable (deterministic input/output)
- ✅ Simple (no state during execution)

**Disadvantages**:
- ❌ More commands for multi-step workflows

### Model 2: Interactive REPL (Avoid for Phase I)

**Pattern**: Start shell → Prompt loop → Execute → Prompt again

```bash
$ todo
> add Buy milk
✓ Task added (ID: 1)
> list
  1. Buy milk
> quit
```

**Advantages**:
- ✅ Fewer keystrokes for power users
- ✅ Can maintain state between commands

**Disadvantages**:
- ❌ Hard to script/automate
- ❌ Non-deterministic (session state)
- ❌ Complex error handling

### Recommendation for Phase I

**Use Non-Interactive Model**:
- Phase I requirements emphasize simplicity
- Each command is atomic and independent
- Output is deterministic
- Easier to test and verify
- Natural progression to web UI in Phase II

---

## Testing CLI Applications

### Three Testing Levels

**1. Unit Tests (Commands)**

Test individual command handlers:

```python
def test_add_command():
    result = add_command("Buy milk", "2% milk")
    assert result["task_id"] == 1
    assert result["title"] == "Buy milk"

def test_add_empty_title():
    with pytest.raises(ValueError):
        add_command("", "description")

def test_list_command():
    add_command("Task 1")
    add_command("Task 2")
    result = list_command()
    assert len(result) == 2
```

**2. Integration Tests (Command + Storage)**

Test full command execution:

```python
def test_add_and_list():
    # Setup
    store = TaskStore()

    # Execute
    add_command("Buy milk", store=store)
    add_command("Call mom", store=store)
    tasks = list_command(store=store)

    # Assert
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Buy milk"
    assert tasks[1]["title"] == "Call mom"

def test_delete_removes_task():
    store = TaskStore()
    task_id = add_command("Task", store=store)
    delete_command(task_id, store=store)
    assert len(list_command(store=store)) == 0
```

**3. End-to-End Tests (CLI Arguments)**

Test actual CLI invocation:

```python
def test_cli_add():
    result = subprocess.run(
        ["python", "-m", "todo_app", "add", "Buy milk"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Task added (ID: 1)" in result.stdout

def test_cli_list():
    subprocess.run(["python", "-m", "todo_app", "add", "Task 1"])
    result = subprocess.run(
        ["python", "-m", "todo_app", "list"],
        capture_output=True,
        text=True
    )
    assert "Task 1" in result.stdout
```

### Testing Strategy for Determinism

**Always verify**:
- Output is identical for same input
- Exit codes are consistent
- Error messages are predictable
- JSON output is valid

---

## CLI Frameworks & Tools

### Framework Comparison for Phase I

| Framework | Complexity | Features | Best For |
|---|---|---|---|
| **argparse** | Low | Basic parsing | Simple CLIs (Phase I) |
| **Click** | Medium | Groups, decorators | Moderate CLIs |
| **Typer** | Medium | Type hints, auto-docs | Modern Python |
| **Hydra** | High | Config management | Complex configs |

### Recommended for Phase I: argparse

**Why**:
- ✅ Built-in (no extra dependencies)
- ✅ Simple for CRUD operations
- ✅ Clean help generation
- ✅ Familiar pattern

**Basic Structure**:

```python
import argparse
import sys

def create_parser():
    parser = argparse.ArgumentParser(
        description="Simple todo list manager"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("description", nargs="?", default="",
                           help="Task description")

    # list command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--status", choices=["all", "pending", "completed"],
                            default="all", help="Filter by status")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # ... more commands

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        if args.command == "add":
            result = add_command(args.title, args.description)
        elif args.command == "list":
            result = list_command(args.status)
        elif args.command == "delete":
            result = delete_command(args.id)

        print(format_output(result))
        sys.exit(0)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print("Unexpected error", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
```

---

## Error Handling Patterns

### Exit Code Convention

```
0 = Success (task completed)
1 = Validation error (invalid input)
2 = Runtime error (unexpected issue)
3 = Not found (task ID doesn't exist)
```

### Error Message Pattern

```
Error: <specific problem>

Example:
  Error: Task title cannot be empty
  Error: Task with ID 5 not found
  Error: Description exceeds maximum length (max 1000 chars)
```

### Exception Hierarchy

```python
class TodoError(Exception):
    """Base exception for todo app"""
    pass

class ValidationError(TodoError):
    """Invalid input from user"""
    exit_code = 1

class NotFoundError(TodoError):
    """Task ID doesn't exist"""
    exit_code = 3

class RuntimeError(TodoError):
    """Unexpected internal error"""
    exit_code = 2
```

---

## User Experience Patterns

### Feedback Loop

Every command should provide:

1. **Action**: What was requested
2. **Status**: Did it work?
3. **Result**: What changed?

**Example**:
```
$ todo add "Buy groceries" "Milk and eggs"
✓ Task added
   ID: 1
   Title: Buy groceries
   Status: pending
```

### Help Text

Provide clear, discoverable help:

```
$ todo --help
usage: todo [-h] {add,list,update,delete,complete} ...

Simple todo list manager

positional arguments:
  {add,list,update,delete,complete}
    add      Add a new task
    list     List all tasks
    update   Update a task
    delete   Delete a task
    complete Mark a task complete

optional arguments:
  -h, --help   Show this help message and exit

Examples:
  todo add "Buy groceries"
  todo list --status pending
  todo update 1 --title "Buy groceries and milk"
  todo delete 1
  todo complete 1
```

### Status Indicators

Use visual markers for clarity:

```
✓ Success (checkmark)
✗ Error (X)
→ Arrow for commands
• Bullet for items
```

### Confirmation & Progress

For destructive operations, confirm:

```
$ todo delete 1
This will delete "Buy groceries". Continue? [y/N]: y
✓ Task deleted
```

---

## Phase I Specific Patterns

### Recommended Architecture for Todo Phase I

```
Entry Point
    └─→ main.py (argparse setup)
        └─→ Command Router
            ├─→ add_command()
            ├─→ list_command()
            ├─→ update_command()
            ├─→ delete_command()
            └─→ complete_command()
                └─→ Task Service
                    ├─→ Validate input
                    ├─→ Call store
                    └─→ Return result
                        └─→ Output Formatter
                            ├─→ Human-readable
                            └─→ JSON (optional)
                                └─→ Task Store (Global)
                                    └─→ In-memory dict
```

### Task Model for Phase I

```python
@dataclass
class Task:
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def mark_complete(self) -> None:
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self) -> None:
        self.completed = False
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
```

### Basic Commands for Phase I

**Command 1: Add Task**
```
$ todo add "Buy groceries" "Milk, eggs, bread"
✓ Task added (ID: 1)
```

**Command 2: List Tasks**
```
$ todo list
Tasks (1 total, 1 pending, 0 completed):
  1. Buy groceries [pending]
```

**Command 3: Update Task**
```
$ todo update 1 --title "Buy groceries and fruits"
✓ Task updated
```

**Command 4: Delete Task**
```
$ todo delete 1
✓ Task deleted
```

**Command 5: Mark Complete**
```
$ todo complete 1
✓ Task marked complete
```

---

## CLI Best Practices Checklist

### Design Checklist

- [ ] Commands follow verb-noun pattern
- [ ] Command names are short, memorable
- [ ] Arguments clearly required vs optional
- [ ] Help text is clear and complete
- [ ] Output is deterministic (same input = same output)

### Implementation Checklist

- [ ] Argument parsing is robust (handles edge cases)
- [ ] Input validation happens before execution
- [ ] Error messages are specific and helpful
- [ ] Exit codes follow convention (0, 1, 2, 3)
- [ ] Output formatting is consistent

### Testing Checklist

- [ ] Unit tests for each command
- [ ] Integration tests for command + storage
- [ ] End-to-end tests for CLI invocation
- [ ] Error cases are tested
- [ ] Output format is verified

### User Experience Checklist

- [ ] Help text is discoverable (--help works)
- [ ] Command examples are provided (README)
- [ ] Status feedback is clear (success/error messages)
- [ ] Output is scannable and easy to read
- [ ] Common workflows are simple

---

## Evolution Path to Phase II

This CLI architecture is designed to transition smoothly to Phase II (web app):

```
Phase I: CLI              Phase II: Web App
─────────────             ──────────────
main.py                   →  routes/
  ├─ add_command()        →    POST /tasks
  ├─ list_command()       →    GET /tasks
  ├─ update_command()     →    PUT /tasks/{id}
  ├─ delete_command()     →    DELETE /tasks/{id}
  └─ complete_command()   →    PATCH /tasks/{id}/complete
        ↓                        ↓
  task_service.py         →  services/task_service.py
        ↓                        ↓
  task_store.py           →  database models (SQLModel)
        ↓                        ↓
  Task (in-memory)        →  Task (persistent)
```

**Key points**:
- Services remain mostly unchanged
- Storage layer is abstracted (can swap in-memory for DB)
- Command logic becomes endpoint logic
- Output formatting becomes JSON responses

---

## Summary: CLI App Pattern's Job

This skill helps you:

| Responsibility | What It Provides |
|---|---|
| **Structure** | Clear project layout and architecture |
| **Commands** | Verb-noun pattern, command design |
| **Input** | Argument parsing, validation strategies |
| **Output** | Formatting, determinism, multiple modes |
| **State** | In-memory storage, singleton pattern |
| **Testing** | Unit, integration, E2E test patterns |
| **Frameworks** | Tool recommendations and examples |
| **Errors** | Exception hierarchy, exit codes |
| **UX** | Help text, feedback loops, status |
| **Evolution** | Path to Phase II architecture |

**Output**: A blueprint for building deterministic, user-friendly CLI applications that can evolve into web apps.

---

**Last Updated**: 2026-01-17
**Project**: Hackathon II – Evolution of Todo
**Phase**: Phase I (CLI Application)
**Scope**: CLI architecture and patterns (exclusive to Phase I)

