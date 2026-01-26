"""Interactive arrow-key navigable menu component."""

from blessed import Terminal
from typing import List, Optional
from src.ui.input_handler import InputHandler
from src.ui.color_theme import ColorTheme


class InteractiveMenu:
    """Arrow-key navigable menu component with circular navigation."""

    def __init__(self, terminal: Terminal, input_handler: InputHandler, theme: ColorTheme):
        """
        Initialize interactive menu.

        Args:
            terminal: blessed Terminal instance
            input_handler: InputHandler for key capture
            theme: ColorTheme for rendering
        """
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
        if not items:
            return None

        selected = 0

        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                # Clear and render menu
                try:
                    print(self.term.home + self.term.clear)
                except (TypeError, AttributeError):
                    # Fallback if terminal methods fail
                    print('\n' * 50)

                print(self.theme.title(title))
                print(self.theme.dim('─' * len(title)))
                print()

                # Render items
                for i, item in enumerate(items):
                    if i == selected:
                        print(self.theme.highlight(f"» {item}"))
                    else:
                        print(f"  {item}")

                print()
                print(self.theme.dim('↑↓: Navigate | Enter: Select | Esc: Back'))

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
                # Handle keyboard shortcuts if printable
                elif key.is_printable and key.char:
                    # Return special codes for shortcuts (negative numbers to distinguish from indices)
                    if key.char == '?':
                        return -1  # Help shortcut
                    elif key.char == 'a':
                        return -2  # Add shortcut
                    elif key.char == 'f':
                        return -3  # Filter shortcut
                    elif key.char == 's':
                        return -4  # Sort shortcut
                    elif key.char == '/':
                        return -5  # Search shortcut
                    # Otherwise ignore unhandled keys
                    pass
