# API Contracts

**Feature**: Interactive Arrow-Key Driven CLI UI
**Date**: 2026-01-22
**Status**: No external contracts - CLI-only feature

## Overview

This feature does NOT expose external APIs. All interaction occurs through the CLI terminal interface. This directory is preserved for consistency with Spec-Kit Plus workflow but contains no contract files.

## Interaction Protocol

### Input Interface
**Protocol**: Terminal stdin via blessed keyboard capture
**Format**: Raw keyboard input (arrow keys, Enter, Esc, printable characters)

**Key Bindings Contract**:
```text
Arrow Keys:
  ↑ (KEY_UP)    → Navigate to previous menu item / task
  ↓ (KEY_DOWN)  → Navigate to next menu item / task
  ← (KEY_LEFT)  → [Reserved for future horizontal navigation]
  → (KEY_RIGHT) → [Reserved for future horizontal navigation]

Action Keys:
  Enter (KEY_ENTER) → Select highlighted item
  Esc (KEY_ESCAPE)  → Return to previous menu / Cancel

Keyboard Shortcuts:
  'a' → Add new task
  'f' → Open filter menu
  's' → Open sort menu
  '/' → Search tasks
  '?' → Show help overlay
  'q' → Quit (alternative to Esc)
```

### Output Interface
**Protocol**: Terminal stdout via blessed ANSI rendering
**Format**: ANSI escape codes + Unicode characters

**Color Semantics Contract**:
```text
Priority Colors:
  HIGH   → Red (#FF0000 or ANSI red)
  MEDIUM → Yellow (#FFFF00 or ANSI yellow)
  LOW    → Green (#00FF00 or ANSI green)

Status Colors:
  Completed   → Green (✓ symbol)
  Incomplete  → White (□ symbol)
  Overdue     → Red (⚠ symbol)

UI Elements:
  Selected item    → Black text on white background (inverted)
  Menu title       → Cyan + bold
  Help text        → Dim/gray
  Success message  → Green
  Error message    → Red
  Warning message  → Yellow
```

**ASCII Fallback Contract**:
```text
When terminal.number_of_colors < 8:
  Priority HIGH   → "[HIGH]"
  Priority MEDIUM → "[MED]"
  Priority LOW    → "[LOW]"

  Completed   → "X"
  Incomplete  → " "
  Overdue     → "!"

  Selected    → "> item"
  Unselected  → "  item"
```

## Internal Component Contracts

While not external APIs, these define contracts between UI components:

### InputHandler Contract

```python
class InputHandler:
    def get_key(timeout: Optional[float] = None) -> KeyInput:
        """
        Capture a single keyboard input.

        Args:
            timeout: Optional timeout in seconds (None = blocking)

        Returns:
            KeyInput with key_name, is_printable, char

        Behavior:
            - Blocks until key pressed (if timeout=None)
            - Returns immediately with timeout exception if timeout expires
            - Handles platform-specific key encoding automatically
        """
```

### InteractiveMenu Contract

```python
class InteractiveMenu:
    def show(title: str, items: List[str]) -> Optional[int]:
        """
        Display arrow-navigable menu and return selection.

        Args:
            title: Menu title to display
            items: List of menu option strings

        Returns:
            Selected index (0-based) or None if cancelled

        Behavior:
            - Circular navigation (wraps at top/bottom)
            - Highlights current selection
            - Returns None on Esc/q press
            - Clears screen before displaying
        """
```

### InteractiveTaskList Contract

```python
class InteractiveTaskList:
    def show(tasks: List[Task], title: str) -> Optional[Task]:
        """
        Display arrow-navigable task list and return selection.

        Args:
            tasks: List of Task objects to display
            title: List title to display

        Returns:
            Selected Task object or None if cancelled

        Behavior:
            - Shows "No tasks found" if empty list
            - Highlights current selection
            - Supports keyboard shortcuts (a=add)
            - Returns None on Esc press
        """
```

### ColorTheme Contract

```python
class ColorTheme:
    def priority_color(priority: Priority, text: str) -> str:
        """
        Apply priority-based color to text.

        Args:
            priority: Priority enum (HIGH/MEDIUM/LOW)
            text: Text to colorize

        Returns:
            ANSI-colored string or plain text (if colors disabled)

        Behavior:
            - Automatically detects terminal color support
            - Falls back to plain text if colors unavailable
            - Returns text unchanged if use_colors=False
        """

    def highlight(text: str) -> str:
        """
        Apply selection highlight to text.

        Args:
            text: Text to highlight

        Returns:
            Highlighted string (inverted colors or "> prefix")

        Behavior:
            - Uses inverted colors (black on white) if supported
            - Falls back to "> " prefix if colors unavailable
        """
```

## No External Dependencies

Phase I constraints maintained:
- ✅ No REST API endpoints
- ✅ No GraphQL schemas
- ✅ No network protocols
- ✅ No IPC mechanisms
- ✅ No file-based protocols

All interaction through terminal I/O only.

## Determinism Contract

All UI behavior is deterministic:
- ✅ Same key input → same navigation action
- ✅ Same task data → same display output
- ✅ Same terminal capabilities → same rendering
- ✅ No randomness in selection, colors, or layout
- ✅ No time-dependent behavior (except due date calculations from existing Phase I logic)

## Testing Contract

Components must support:
- Unit testing with mocked terminal/input
- Integration testing with simulated key sequences
- Cross-platform validation (Windows Terminal, PowerShell, bash, zsh)
- ASCII fallback verification on limited terminals

## Version Compatibility

This feature maintains:
- ✅ Backward compatibility with existing Phase I features
- ✅ All 117 Phase I tasks remain functional
- ✅ No breaking changes to models, services, or store layers
- ✅ Graceful degradation on terminals with limited capabilities
