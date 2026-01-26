"""Input handler for keyboard capture and processing."""

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
        """
        Initialize input handler.

        Args:
            terminal: blessed Terminal instance
        """
        self.term = terminal

    def get_key(self, timeout: Optional[float] = None) -> KeyInput:
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
