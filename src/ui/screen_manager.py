"""Screen manager for terminal operations."""

from blessed import Terminal
from typing import Tuple


class ScreenManager:
    """Manages terminal screen operations and display."""

    def __init__(self):
        """Initialize screen manager with terminal instance."""
        self.term = Terminal()

    def clear(self):
        """Clear the screen."""
        print(self.term.clear)

    def refresh(self):
        """Refresh the screen (clear and reset cursor)."""
        print(self.term.home + self.term.clear)

    def get_dimensions(self) -> Tuple[int, int]:
        """
        Get terminal dimensions.

        Returns:
            Tuple of (width, height)
        """
        return self.term.width, self.term.height

    def supports_colors(self) -> bool:
        """
        Check if terminal supports colors.

        Returns:
            True if terminal supports 8+ colors
        """
        return self.term.number_of_colors >= 8

    def show_message(self, message: str, message_type: str = 'info'):
        """
        Display a message with appropriate styling.

        Args:
            message: Message text to display
            message_type: Type of message (info, success, error, warning)
        """
        use_colors = self.supports_colors()

        if message_type == 'error':
            symbol = "✗" if use_colors else "X"
            text = self.term.red(f"{symbol} {message}") if use_colors else f"{symbol} {message}"
        elif message_type == 'success':
            symbol = "✓" if use_colors else "*"
            text = self.term.green(f"{symbol} {message}") if use_colors else f"{symbol} {message}"
        elif message_type == 'warning':
            symbol = "⚠" if use_colors else "!"
            text = self.term.yellow(f"{symbol} {message}") if use_colors else f"{symbol} {message}"
        else:  # info
            symbol = "ℹ" if use_colors else "i"
            text = self.term.white(f"{symbol} {message}") if use_colors else f"{symbol} {message}"

        print(text)

    def pause(self, prompt: str = "Press any key to continue..."):
        """
        Pause execution and wait for key press.

        Args:
            prompt: Prompt text to display
        """
        try:
            display_prompt = self.term.dim(prompt) if self.supports_colors() else prompt
        except (TypeError, AttributeError):
            display_prompt = prompt
        print(display_prompt)
        with self.term.cbreak():
            self.term.inkey()

    def show_help_overlay(self):
        """Display keyboard shortcuts help overlay (Feature 008 - User Story 4)."""
        self.clear()
        use_colors = self.supports_colors()

        try:
            title = self.term.bold_cyan("Keyboard Shortcuts") if use_colors else "=== Keyboard Shortcuts ==="
        except (TypeError, AttributeError):
            title = "=== Keyboard Shortcuts ==="
        print(title)

        try:
            separator = self.term.dim("─" * 40) if use_colors else "─" * 40
        except (TypeError, AttributeError):
            separator = "─" * 40
        print(separator)
        print()

        shortcuts = [
            ("Navigation", [
                ("↑/↓", "Navigate menu items"),
                ("Enter", "Select item"),
                ("Esc", "Go back / Cancel"),
            ]),
            ("Quick Actions", [
                ("a", "Add new task"),
                ("f", "Filter tasks"),
                ("s", "Sort tasks"),
                ("/", "Search tasks"),
            ]),
            ("Help", [
                ("?", "Show this help"),
                ("q", "Quit (alternative to Esc)"),
            ]),
        ]

        for category, items in shortcuts:
            try:
                cat_text = self.term.bold(category) if use_colors else f"[{category}]"
            except (TypeError, AttributeError):
                cat_text = f"[{category}]"
            print(cat_text)

            for key, desc in items:
                try:
                    key_text = self.term.green(f"  {key:8}") if use_colors else f"  {key:8}"
                except (TypeError, AttributeError):
                    key_text = f"  {key:8}"
                print(f"{key_text} - {desc}")
            print()

        try:
            separator = self.term.dim("─" * 40) if use_colors else "─" * 40
        except (TypeError, AttributeError):
            separator = "─" * 40
        print(separator)
        self.pause()
