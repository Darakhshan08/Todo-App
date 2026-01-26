# Phase 0 Research: Terminal Library Selection

**Feature**: Interactive Arrow-Key Driven CLI UI
**Date**: 2026-01-22
**Research Question**: Which Python terminal library best supports arrow-key navigation and ANSI colors with cross-platform compatibility?

## Research Summary

Evaluated three Python terminal libraries against requirements: arrow-key capture, ANSI color support, Windows compatibility, terminal detection, and API simplicity.

### Libraries Evaluated
1. **curses** (stdlib) - Traditional Unix terminal library
2. **prompt_toolkit** (third-party) - REPL-focused with high-level abstractions
3. **blessed** (third-party) - Modern, Pythonic terminal library

## Decision: Use **blessed** ⭐

### Rationale

**blessed** is the optimal choice for this project based on prioritized decision criteria:

1. **Windows Compatibility** ✅ (Critical requirement)
   - Native Windows Terminal and PowerShell support via `jinxed` package
   - Actively tested on Windows platforms
   - No additional setup required beyond package installation

2. **Arrow-Key Capture Ease** ✅
   - Simplest implementation with `term.inkey()` and readable `key.name` properties
   - Example: `if key.name == 'KEY_UP': # handle up arrow`
   - More intuitive than curses key codes or prompt_toolkit's KeyBindings

3. **Color Rendering Support** ✅
   - Full ANSI color support with automatic downconversion
   - Pythonic API: `term.red('text')`, `term.bold_green_on_black('text')`
   - Smart handling: automatically strips colors when output is redirected

4. **Minimal Dependencies** ✅
   - Only 1 dependency on Unix (`wcwidth`)
   - 2 dependencies on Windows (`wcwidth` + `jinxed`)
   - Comparable to prompt_toolkit's dependency count

5. **API Simplicity** ✅
   - Low learning curve with intuitive, Pythonic interface
   - Works naturally with f-strings and modern Python patterns
   - No forced full-screen mode (easier for simple menus)

### Additional Advantages
- **Recently updated**: Version 1.25 released January 20, 2026 (4 days ago)
- **Excellent documentation**: Comprehensive guides with practical examples
- **Better terminal detection**: `term.number_of_colors`, `term.does_styling`, automatic capability checks
- **Python 3.13+ support**: Confirmed compatibility with latest Python versions

## Alternatives Considered

### curses (stdlib)
**Rejected because**:
- ⚠️ Requires `windows-curses` extra package on Windows (not truly stdlib cross-platform)
- ⚠️ `windows-curses` has inactive maintenance and uncertain Python 3.13 support
- High learning curve with C-based API
- Forces full-screen mode by default

**Would use if**: Stdlib-only requirement on Unix systems (not our case - need Windows support)

### prompt_toolkit
**Rejected because**:
- Designed primarily for REPL/readline replacements (overcomplicated for simple menus)
- High API complexity for custom UIs
- Better suited for autocomplete/syntax highlighting use cases

**Would use if**: Building REPL-style interface with autocomplete or complex input validation

## Technical Implementation Details

### Installation
```bash
uv add blessed
```

### Basic Arrow-Key Menu Pattern
```python
from blessed import Terminal

term = Terminal()
menu_items = ['Add task', 'List tasks', 'Delete task', 'Exit']
selected = 0

with term.cbreak(), term.hidden_cursor():
    while True:
        # Clear and display menu
        print(term.home + term.clear)
        for i, item in enumerate(menu_items):
            if i == selected:
                print(term.black_on_white(f'» {item}'))
            else:
                print(f'  {item}')

        # Capture input
        key = term.inkey()

        # Handle navigation
        if key.name == 'KEY_UP':
            selected = (selected - 1) % len(menu_items)
        elif key.name == 'KEY_DOWN':
            selected = (selected + 1) % len(menu_items)
        elif key.name == 'KEY_ENTER':
            # Execute selected action
            break
        elif key.name == 'KEY_ESCAPE':
            # Cancel
            break
```

### Color Rendering with Terminal Detection
```python
from blessed import Terminal

term = Terminal()

# Detect capabilities
if term.number_of_colors < 8:
    # Fall back to ASCII-only
    priority_high = "[HIGH]"
else:
    # Use colors
    priority_high = term.red("[HIGH]")

# Semantic color helpers
def format_priority(priority):
    if priority == Priority.HIGH:
        return term.red("(HIGH)")
    elif priority == Priority.MEDIUM:
        return term.yellow("(MED)")
    else:
        return term.green("(LOW)")
```

### Terminal Capability Detection
```python
# Check if colors are supported
if term.number_of_colors >= 8:
    # Full color mode
    use_colors = True
elif term.does_styling:
    # Basic styling only
    use_colors = False
else:
    # ASCII fallback
    use_colors = False
```

## Key Implementation Modules (Based on Research)

### 1. `src/ui/input_handler.py`
- Wraps `term.inkey()` for arrow-key capture
- Maps key codes to actions (UP, DOWN, ENTER, ESC)
- Provides abstraction over blessed's key detection

### 2. `src/ui/color_theme.py`
- Defines semantic color helpers using blessed
- Implements terminal capability detection
- Provides ASCII fallback rendering functions

### 3. `src/ui/interactive_menu.py`
- Reusable arrow-key menu component
- Uses blessed for rendering and input
- Circular navigation support

### 4. `src/ui/interactive_task_list.py`
- Task-specific list navigation
- Integrates with existing Task model
- Contextual menu support

### 5. `src/ui/screen_manager.py`
- Terminal initialization with blessed
- Screen clearing and refresh management
- Handles context managers (`term.cbreak()`, `term.hidden_cursor()`)

## Performance Characteristics

- **Input latency**: blessed's `inkey()` is non-blocking with timeout support - easily meets < 100ms requirement
- **Screen transitions**: `term.clear` is fast, lightweight - well under 200ms target
- **Memory footprint**: Minimal - blessed adds ~500KB to application size

## Cross-Platform Validation Strategy

1. **Windows Terminal**: Primary development platform
2. **PowerShell 7+**: Test color rendering and key input
3. **Git Bash (Windows)**: Test Unix emulation layer
4. **WSL Ubuntu**: Test native Unix behavior
5. **Color detection tests**: Verify fallback to ASCII on limited terminals

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Windows Terminal incompatibility | Low | High | blessed has dedicated Windows support via jinxed |
| Key encoding issues | Low | Medium | blessed handles platform-specific encodings automatically |
| Color rendering failures | Low | Low | Built-in `term.does_styling` detection + ASCII fallback |
| Python 3.13 compatibility | Very Low | Medium | blessed released Jan 20, 2026 with Python 3.13 support |

## References

- [blessed Documentation](https://blessed.readthedocs.io/en/latest/intro.html)
- [blessed PyPI](https://pypi.org/project/blessed/) - Version 1.25 (Jan 20, 2026)
- [blessed GitHub Repository](https://github.com/jquast/blessed)
- [blessed Keyboard Input Guide](https://blessed.readthedocs.io/en/latest/keyboard.html)
- [blessed Colors Guide](https://blessed.readthedocs.io/en/latest/colors.html)
- [blessed Terminal Capabilities](https://blessed.readthedocs.io/en/latest/terminal.html)

## Conclusion

**blessed** resolves the "NEEDS CLARIFICATION" item from Technical Context. It provides the optimal balance of Windows compatibility, API simplicity, and terminal capabilities for building an interactive arrow-key driven CLI with color enhancement. The library is actively maintained (latest update 4 days ago), has Python 3.13 support, and aligns with all Phase I constraints (deterministic, no external services, clean architecture).

**Next Phase**: Proceed to Phase 1 design with blessed as the chosen terminal library.
