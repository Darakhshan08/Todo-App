"""Interactive task list with arrow-key navigation."""

from blessed import Terminal
from typing import List, Optional, Union
from src.models.task import Task
from src.ui.input_handler import InputHandler
from src.ui.color_theme import ColorTheme


class InteractiveTaskList:
    """Interactive task list with arrow-key navigation."""

    def __init__(self, terminal: Terminal, input_handler: InputHandler, theme: ColorTheme):
        """
        Initialize interactive task list.

        Args:
            terminal: blessed Terminal instance
            input_handler: InputHandler for key capture
            theme: ColorTheme for rendering
        """
        self.term = terminal
        self.input_handler = input_handler
        self.theme = theme

    def show(self, tasks: List[Task], title: str = "Tasks") -> Optional[Union[Task, str]]:
        """
        Display task list and return selected task.

        Args:
            tasks: List of tasks to display
            title: List title

        Returns:
            Selected Task, 'ADD_NEW' signal, or None if cancelled
        """
        if not tasks:
            print(self.term.clear)
            print(self.theme.warning("No tasks found"))
            print()
            print(self.theme.dim("Press 'a' to add a task or Esc to return"))
            key = self.input_handler.get_key()
            if key.char == 'a':
                return 'ADD_NEW'
            return None

        selected = 0

        with self.term.cbreak(), self.term.hidden_cursor():
            while True:
                # Clear and render list
                try:
                    print(self.term.home + self.term.clear)
                except (TypeError, AttributeError):
                    # Fallback if terminal methods fail
                    print('\n' * 50)

                print(self.theme.title(title))
                print(self.theme.dim('─' * len(title)))
                print()

                # Render tasks (simplified format for now)
                for i, task in enumerate(tasks):
                    # Format task line with status symbol
                    status_symbol = "✓" if task.completed else "□"
                    priority_text = f"[{task.priority.value}]" if task.priority else ""

                    task_line = f"{status_symbol} {task.title} {priority_text}".strip()

                    if i == selected:
                        print(self.theme.highlight(task_line))
                    else:
                        # Apply color based on status
                        if task.completed:
                            print(f"  {self.theme.status_color(True, task_line)}")
                        else:
                            print(f"  {task_line}")

                print()
                print(self.theme.dim('↑↓: Navigate | Enter: Select | Esc: Back | a: Add'))

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
                    return 'ADD_NEW'
