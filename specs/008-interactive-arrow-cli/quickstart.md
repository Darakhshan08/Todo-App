# Quickstart Guide: Interactive Arrow-Key Driven CLI UI

**Feature**: Interactive Arrow-Key Driven CLI UI
**Date**: 2026-01-22
**For**: Developers implementing this feature

## Overview

This guide provides implementation patterns for building the interactive arrow-key CLI upgrade. All code examples use **blessed** (chosen in Phase 0 research) and follow Phase I constraints.

## Prerequisites

```bash
# Install blessed terminal library
uv add blessed

# Verify Python version
python --version  # Should be 3.13+

# Verify existing Phase I implementation
uv run python main.py  # Should run existing numeric menu CLI
```

## Architecture Overview

```text
User Input Layer:
  InputHandler → KeyInput → InteractiveMenu/InteractiveTaskList

Presentation Layer:
  ColorTheme → Formatters (modified) → ScreenManager → Terminal

Business Logic Layer (unchanged):
  MenuController → TaskService → Task (domain model)

Data Layer (unchanged):
  InMemoryTaskStore
```

**Key Principle**: UI layer only. Zero changes to models, services, or store.

## Core Components

### 1. InputHandler (Key Capture)

**Purpose**: Abstract blessed's input handling for testability
**Location**: `src/ui/input_handler.py`

```python
from blessed import Terminal
from dataclasses import dataclass
from typing import Optional

@dataclass
class KeyInput:
    """Represents a captured keyboard input."""
    key_name: str
    is_printable: bool
    char: Optional[str] = None

class InputHandler:
    """Handles arrow-key and keyboard input capture."""

    def __init__(self, terminal: Terminal):
        self.term = terminal

    def get_key(self, timeout: float = None) -> KeyInput:
        """
        Capture a single key press.

        Args:
            timeout: Optional timeout in seconds (None = blocking)

        Returns:
            KeyInput with key information
        """
        key = self.term.inkey(timeout=timeout)

        if key.name:
            # Special key (arrow, Enter, Esc, etc.)
            return KeyInput(
                key_name=key.name,
                is_printable=False,
                char=None
            )
        else:
            # Printable character
            return KeyInput(
                key_name='',
                is_printable=True,
                char=str(key)
            )
```

**Usage Pattern**:
```python
handler = InputHandler(terminal)
key = handler.get_key()

if key.key_name == 'KEY_UP':
    # Handle up arrow
elif key.key_name == 'KEY_DOWN':
    # Handle down arrow
elif key.key_name == 'KEY_ENTER':
    # Handle selection
```

### 2. ColorTheme (Visual Rendering)

**Purpose**: Provide semantic color rendering with terminal detection
**Location**: `src/ui/color_theme.py`

```python
from blessed import Terminal
from src.models.task import Priority

class ColorTheme:
    """ANSI color theme with terminal capability detection."""

    def __init__(self, terminal: Terminal):
        self.term = terminal
        self.use_colors = terminal.number_of_colors >= 8

    def priority_color(self, priority: Priority, text: str) -> str:
        """Render text with priority-based color."""
        if not self.use_colors:
            return text  # ASCII fallback

        if priority == Priority.HIGH:
            return self.term.red(text)
        elif priority == Priority.MEDIUM:
            return self.term.yellow(text)
        else:
            return self.term.green(text)

    def status_color(self, completed: bool, text: str) -> str:
        """Render text with status-based color."""
        if not self.use_colors:
            return text

        return self.term.green(text) if completed else self.term.white(text)

    def highlight(self, text: str) -> str:
        """Render highlighted/selected text."""
        if not self.use_colors:
            return f"> {text}"  # ASCII fallback

        return self.term.black_on_white(f" {text} ")

    def warning(self, text: str) -> str:
        """Render warning text (overdue, errors)."""
        if not self.use_colors:
            return f"! {text}"

        return self.term.red(text)
```

**Usage Pattern**:
```python
theme = ColorTheme(terminal)

# Priority rendering
priority_text = theme.priority_color(Priority.HIGH, "(HIGH)")

# Selection highlighting
highlighted = theme.highlight("» Add task")
```

### 3. InteractiveMenu (Arrow Navigation)

**Purpose**: Reusable arrow-key navigable menu component
**Location**: `src/ui/interactive_menu.py`

```python
from blessed import Terminal
from typing import List, Optional, Tuple
from src.ui.input_handler import InputHandler, KeyInput
from src.ui.color_theme import ColorTheme

class InteractiveMenu:
    """Arrow-key navigable menu component."""

    def __init__(self, terminal: Terminal, input_handler: InputHandler, theme: ColorTheme):
        self.term = terminal
        self.input_handler = input_handler
        self.theme = theme

    def show(self, title: str, items: List[str]) -> Optional[int]:
        """
        Display menu and return selected index.

        Args:
            title: Menu title
            items: List of menu options

        Returns:
            Selected index (0-based) or None if cancelled
        """
        selected = 0

        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                # Clear and render menu
                print(self.term.home + self.term.clear)
                print(self.term.bold_cyan(title))
                print(self.term.dim('─' * len(title)))
                print()

                # Render items
                for i, item in enumerate(items):
                    if i == selected:
                        print(self.theme.highlight(f"» {item}"))
                    else:
                        print(f"  {item}")

                print()
                print(self.term.dim('↑↓: Navigate | Enter: Select | Esc: Back'))

                # Get input
                key = self.input_handler.get_key()

                # Handle navigation
                if key.key_name == 'KEY_UP':
                    selected = (selected - 1) % len(items)
                elif key.key_name == 'KEY_DOWN':
                    selected = (selected + 1) % len(items)
                elif key.key_name == 'KEY_ENTER':
                    return selected
                elif key.key_name == 'KEY_ESCAPE' or key.char == 'q':
                    return None
```

**Usage Pattern**:
```python
menu = InteractiveMenu(terminal, input_handler, theme)
items = ['Add task', 'List tasks', 'Delete task', 'Exit']

selected_index = menu.show("Main Menu", items)

if selected_index is not None:
    # User selected an option
    execute_action(items[selected_index])
else:
    # User cancelled
    return
```

### 4. InteractiveTaskList (Task Navigation)

**Purpose**: Arrow-key navigation through task lists
**Location**: `src/ui/interactive_task_list.py`

```python
from blessed import Terminal
from typing import List, Optional, Tuple
from src.models.task import Task
from src.ui.input_handler import InputHandler
from src.ui.color_theme import ColorTheme
from src.ui.formatters import format_task_brief

class InteractiveTaskList:
    """Interactive task list with arrow-key navigation."""

    def __init__(self, terminal: Terminal, input_handler: InputHandler, theme: ColorTheme):
        self.term = terminal
        self.input_handler = input_handler
        self.theme = theme

    def show(self, tasks: List[Task], title: str = "Tasks") -> Optional[Task]:
        """
        Display task list and return selected task.

        Args:
            tasks: List of tasks to display
            title: List title

        Returns:
            Selected Task or None if cancelled
        """
        if not tasks:
            print(self.term.clear)
            print(self.term.yellow("No tasks found"))
            print("Press 'a' to add a task or Esc to return")
            self.input_handler.get_key()
            return None

        selected = 0

        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                # Clear and render list
                print(self.term.home + self.term.clear)
                print(self.term.bold_cyan(title))
                print(self.term.dim('─' * len(title)))
                print()

                # Render tasks
                for i, task in enumerate(tasks):
                    task_line = format_task_brief(task)
                    if i == selected:
                        print(self.theme.highlight(task_line))
                    else:
                        print(f"  {task_line}")

                print()
                print(self.term.dim('↑↓: Navigate | Enter: Select | Esc: Back | a: Add'))

                # Get input
                key = self.input_handler.get_key()

                # Handle navigation
                if key.key_name == 'KEY_UP':
                    selected = (selected - 1) % len(tasks)
                elif key.key_name == 'KEY_DOWN':
                    selected = (selected + 1) % len(tasks)
                elif key.key_name == 'KEY_ENTER':
                    return tasks[selected]
                elif key.key_name == 'KEY_ESCAPE':
                    return None
                elif key.char == 'a':
                    # Shortcut: add task
                    return 'ADD_NEW'  # Signal to caller
```

**Usage Pattern**:
```python
task_list = InteractiveTaskList(terminal, input_handler, theme)
tasks = task_service.get_all_tasks()

selected_task = task_list.show(tasks, "All Tasks")

if selected_task:
    # Show contextual menu for selected task
    show_task_actions(selected_task)
```

### 5. ScreenManager (Terminal Management)

**Purpose**: Manage terminal initialization and screen operations
**Location**: `src/ui/screen_manager.py`

```python
from blessed import Terminal
from typing import Optional

class ScreenManager:
    """Manages terminal screen operations."""

    def __init__(self):
        self.term = Terminal()

    def clear(self):
        """Clear the screen."""
        print(self.term.clear)

    def refresh(self):
        """Refresh the screen (clear and reset cursor)."""
        print(self.term.home + self.term.clear)

    def get_dimensions(self) -> tuple[int, int]:
        """Get terminal dimensions (width, height)."""
        return self.term.width, self.term.height

    def supports_colors(self) -> bool:
        """Check if terminal supports colors."""
        return self.term.number_of_colors >= 8

    def show_message(self, message: str, message_type: str = 'info'):
        """Display a temporary message."""
        if message_type == 'error':
            print(self.term.red(f"✗ {message}"))
        elif message_type == 'success':
            print(self.term.green(f"✓ {message}"))
        elif message_type == 'warning':
            print(self.term.yellow(f"⚠ {message}"))
        else:
            print(self.term.white(f"ℹ {message}"))
```

## Integration with Existing Code

### Modify MenuController

**File**: `src/ui/menu_controller.py`

```python
from blessed import Terminal
from src.ui.interactive_menu import InteractiveMenu
from src.ui.interactive_task_list import InteractiveTaskList
from src.ui.input_handler import InputHandler
from src.ui.color_theme import ColorTheme
from src.ui.screen_manager import ScreenManager

class MenuController:
    """Main menu controller with interactive navigation."""

    def __init__(self, task_service):
        self.task_service = task_service
        self.screen_manager = ScreenManager()
        self.term = self.screen_manager.term
        self.input_handler = InputHandler(self.term)
        self.theme = ColorTheme(self.term)
        self.menu = InteractiveMenu(self.term, self.input_handler, self.theme)
        self.task_list = InteractiveTaskList(self.term, self.input_handler, self.theme)

    def run(self):
        """Main application loop."""
        while True:
            # Show main menu
            items = [
                'Add task',
                'View all tasks',
                'Search tasks',
                'Filter tasks',
                'Sort tasks',
                'Mark task complete',
                'Update task',
                'Delete task',
                'View recurring tasks',
                'Exit'
            ]

            selected = self.menu.show("Todo Application", items)

            if selected is None or selected == 9:  # Exit
                self.screen_manager.clear()
                print(self.term.green("Goodbye!"))
                break

            # Route to handlers
            self._handle_menu_choice(selected)

    def _handle_menu_choice(self, choice: int):
        """Route menu choice to appropriate handler."""
        handlers = {
            0: self.handle_add_task,
            1: self.handle_view_all,
            2: self.handle_search,
            # ... other handlers
        }
        handler = handlers.get(choice)
        if handler:
            handler()
```

### Modify Formatters

**File**: `src/ui/formatters.py`

Add color rendering to existing format functions:

```python
from blessed import Terminal

# Initialize terminal (module-level for color detection)
_term = Terminal()
_use_colors = _term.number_of_colors >= 8

def format_priority_label(priority: Priority) -> str:
    """Format priority with color."""
    if priority == Priority.HIGH:
        text = "(HIGH)"
        return _term.red(text) if _use_colors else text
    elif priority == Priority.MEDIUM:
        text = "(MED)"
        return _term.yellow(text) if _use_colors else text
    else:
        text = "(LOW)"
        return _term.green(text) if _use_colors else text

def format_status_indicator(completed: bool) -> str:
    """Format status with Unicode symbol and color."""
    if completed:
        symbol = "✓"
        return _term.green(symbol) if _use_colors else "X"
    else:
        symbol = "□"
        return _term.white(symbol) if _use_colors else " "
```

## Testing Patterns

### Unit Test Example

```python
import pytest
from blessed import Terminal
from src.ui.input_handler import InputHandler, KeyInput

def test_input_handler_arrow_keys():
    """Test arrow key capture."""
    term = Terminal()
    handler = InputHandler(term)

    # Mock key input (in real tests, use blessed's testing utilities)
    # Test that KEY_UP is recognized
    key = KeyInput(key_name='KEY_UP', is_printable=False)
    assert key.key_name == 'KEY_UP'
    assert not key.is_printable
```

### Integration Test Example

```python
def test_interactive_menu_navigation():
    """Test full menu navigation flow."""
    # Use blessed's testing facilities or mock terminal
    # Simulate arrow key sequence: DOWN, DOWN, ENTER
    # Verify correct item selected
    pass
```

## Development Workflow

1. **Create input_handler.py** with KeyInput and InputHandler
2. **Create color_theme.py** with ColorTheme and terminal detection
3. **Create screen_manager.py** with ScreenManager
4. **Create interactive_menu.py** with InteractiveMenu
5. **Create interactive_task_list.py** with InteractiveTaskList
6. **Modify formatters.py** to add color codes
7. **Modify menu_controller.py** to integrate interactive components
8. **Update main.py** to use new MenuController
9. **Test on Windows Terminal, PowerShell, and Git Bash**
10. **Verify ASCII fallback** on limited terminals

## Common Patterns

### Pattern 1: Keyboard Shortcuts

```python
# In any menu context
key = input_handler.get_key()

if key.char == 'a':  # Add shortcut
    handle_add_task()
elif key.char == 'f':  # Filter shortcut
    handle_filter()
elif key.char == '?':  # Help shortcut
    show_help_overlay()
```

### Pattern 2: Contextual Menus

```python
# After task selection
def show_task_actions(task: Task) -> Optional[str]:
    """Show contextual actions for a task."""
    actions = ['View Details', 'Edit', 'Delete', 'Toggle Complete', 'Back']
    selected = menu.show(f"Task: {task.title}", actions)

    if selected == 0:
        return 'VIEW'
    elif selected == 1:
        return 'EDIT'
    # ... etc
```

### Pattern 3: Graceful Degradation

```python
# Always provide ASCII fallback
if theme.use_colors:
    status = theme.status_color(task.completed, "✓")
else:
    status = "X" if task.completed else " "
```

## Troubleshooting

### Arrow Keys Not Working
- Verify terminal emulator supports ANSI escape sequences
- Check `term.inkey()` returns key.name correctly
- Test with simple print(key.name) debug output

### Colors Not Rendering
- Check `term.number_of_colors` value
- Verify terminal TERM environment variable (should be xterm-256color or similar)
- Test `theme.use_colors` flag

### Windows-Specific Issues
- Ensure jinxed package installed (blessed's Windows backend)
- Test on Windows Terminal (best compatibility)
- PowerShell ISE has limited support - use PowerShell 7+

## Next Steps

After implementing these components:
1. Run `/sp.tasks` to generate task breakdown
2. Implement tasks in order (input_handler → color_theme → screen_manager → interactive_menu → interactive_task_list → integration)
3. Test each component in isolation before integration
4. Validate cross-platform compatibility
5. Verify no regressions in existing Phase I features

## References

- [blessed Documentation](https://blessed.readthedocs.io/en/latest/intro.html)
- [blessed Keyboard Input](https://blessed.readthedocs.io/en/latest/keyboard.html)
- [blessed Colors](https://blessed.readthedocs.io/en/latest/colors.html)
- Phase I implementation: `specs/007-phase1-todo-cli/`
