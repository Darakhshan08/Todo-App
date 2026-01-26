"""Color theme for terminal UI with capability detection."""

from blessed import Terminal
from src.models.task import Priority


class ColorTheme:
    """ANSI color theme with terminal capability detection and ASCII fallback."""

    def __init__(self, terminal: Terminal):
        """
        Initialize color theme.

        Args:
            terminal: blessed Terminal instance
        """
        self.term = terminal
        self.use_colors = terminal.number_of_colors >= 8

    def _safe_color(self, color_func, text: str, fallback: str = None) -> str:
        """
        Safely apply color function with fallback.

        Args:
            color_func: Terminal color function to apply
            text: Text to colorize
            fallback: Fallback text if color fails (defaults to plain text)

        Returns:
            Colored text or fallback
        """
        if not self.use_colors:
            return fallback if fallback is not None else text

        try:
            return color_func(text)
        except (TypeError, AttributeError):
            # Fallback if terminal doesn't support this color function
            return fallback if fallback is not None else text

    def priority_color(self, priority: Priority, text: str) -> str:
        """
        Render text with priority-based color.

        Args:
            priority: Priority enum (HIGH/MEDIUM/LOW)
            text: Text to colorize

        Returns:
            ANSI-colored string or plain text if colors disabled
        """
        if priority == Priority.HIGH:
            return self._safe_color(self.term.red, text)
        elif priority == Priority.MEDIUM:
            return self._safe_color(self.term.yellow, text)
        else:  # LOW
            return self._safe_color(self.term.green, text)

    def status_color(self, completed: bool, text: str) -> str:
        """
        Render text with status-based color.

        Args:
            completed: Whether task is completed
            text: Text to colorize

        Returns:
            Green for completed, white for incomplete, or plain text
        """
        if completed:
            return self._safe_color(self.term.green, text)
        else:
            return self._safe_color(self.term.white, text)

    def highlight(self, text: str) -> str:
        """
        Render highlighted/selected text.

        Args:
            text: Text to highlight

        Returns:
            Inverted colors or ASCII prefix
        """
        return self._safe_color(self.term.black_on_white, f" {text} ", f"> {text}")

    def warning(self, text: str) -> str:
        """
        Render warning text (overdue, errors).

        Args:
            text: Warning message

        Returns:
            Red text or prefixed text
        """
        return self._safe_color(self.term.red, text, f"! {text}")

    def dim(self, text: str) -> str:
        """
        Render dimmed/help text.

        Args:
            text: Text to dim

        Returns:
            Dimmed text or plain text
        """
        return self._safe_color(self.term.dim, text)

    def title(self, text: str) -> str:
        """
        Render title text.

        Args:
            text: Title text

        Returns:
            Cyan bold text or plain text
        """
        return self._safe_color(self.term.bold_cyan, text)

    def success(self, text: str) -> str:
        """
        Render success message.

        Args:
            text: Success message

        Returns:
            Green text or plain text
        """
        return self._safe_color(self.term.green, text)

    def error(self, text: str) -> str:
        """
        Render error message.

        Args:
            text: Error message

        Returns:
            Red text or plain text
        """
        return self._safe_color(self.term.red, text)
