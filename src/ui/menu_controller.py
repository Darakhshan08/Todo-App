"""
Menu controller for Phase I Todo CLI.
Enhanced with interactive arrow-key navigation (Feature 008).
"""
from datetime import datetime, date
from src.services.task_service import TaskService
from src.models.task import Priority, SortOption, RecurrenceRule, Task
from src.ui.formatters import (
    print_header,
    print_separator,
    print_error,
    print_success,
    print_info,
    display_task_list,
    display_task_details,
    format_task_detailed,
    clear_screen,
)
from src.ui.prompts import prompt_string, prompt_int, prompt_yes_no, prompt_multiline, press_enter_to_continue

# Interactive UI components (Feature 008)
from blessed import Terminal
from src.ui.interactive_menu import InteractiveMenu
from src.ui.interactive_task_list import InteractiveTaskList
from src.ui.input_handler import InputHandler
from src.ui.color_theme import ColorTheme
from src.ui.screen_manager import ScreenManager


class MenuController:
    """
    Controls the main menu loop and user interactions.

    Enhanced with interactive arrow-key navigation (Feature 008).
    Coordinates between user input and task service operations.
    """

    def __init__(self, task_service: TaskService, use_interactive: bool = True):
        """
        Initialize MenuController.

        Args:
            task_service: TaskService instance for business logic
            use_interactive: Enable interactive arrow-key UI (default: True)
        """
        self.task_service = task_service
        self.running = False
        # View state for filters
        self.active_filter = None  # Type of filter: 'search', 'status', 'priority', 'tag', or None
        self.filter_value = None   # Value for the active filter
        # View state for sorting
        self.active_sort = None  # SortOption or None for default

        # Interactive UI components (Feature 008)
        self.use_interactive = use_interactive
        if use_interactive:
            self.screen_manager = ScreenManager()
            self.term = self.screen_manager.term
            self.input_handler = InputHandler(self.term)
            self.theme = ColorTheme(self.term)
            self.menu = InteractiveMenu(self.term, self.input_handler, self.theme)
            self.task_list = InteractiveTaskList(self.term, self.input_handler, self.theme)

    def display_main_menu(self) -> None:
        """
        Display the main menu options.

        Example output:
            ============================================================
             Todo Application - Main Menu
            ============================================================
            1. Add Task
            2. View All Tasks
            3. View Task Details
            4. Update Task
            5. Delete Task
            6. Mark Complete/Incomplete
            7. Search Tasks
            8. Filter Tasks
            9. Sort Tasks
            10. Clear Screen
            0. Exit
            ============================================================
        """
        print_header("Todo Application - Main Menu")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Task Details")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Mark Complete/Incomplete")
        print("7. Search Tasks")
        print("8. Filter Tasks")
        print("9. Sort Tasks")
        print("10. Clear Screen")
        print("0. Exit")
        print_separator()

    def handle_add_task(self) -> None:
        """
        Handle task creation flow.

        Prompts user for:
        - Title (required)
        - Description (optional, supports multi-line with \\n)
        - Priority (1=High, 2=Medium, 3=Low, default=Medium)
        - Tags (comma-separated, optional)

        Creates task with specified values.
        """
        # Clear screen for better UX
        if self.use_interactive:
            self.screen_manager.clear()
        else:
            clear_screen()

        print_header("Add New Task")

        title = prompt_string("Enter task title", required=True)
        description = prompt_multiline("Enter description (optional)")

        # Priority selection - use interactive menu if available
        if self.use_interactive:
            priority_items = ['High priority', 'Medium priority (default)', 'Low priority']
            self.screen_manager.clear()
            print_header("Select Priority")
            priority_selected = self.menu.show("Task Priority", priority_items)

            if priority_selected is None:  # Cancelled
                priority = Priority.MEDIUM  # Default
            elif priority_selected == 0:
                priority = Priority.HIGH
            elif priority_selected == 2:
                priority = Priority.LOW
            else:
                priority = Priority.MEDIUM
        else:
            # Traditional mode
            print("\nSelect priority:")
            print("  1. High")
            print("  2. Medium (default)")
            print("  3. Low")
            priority_choice = prompt_int("Enter priority choice", min_value=1, max_value=3)

            if priority_choice == 1:
                priority = Priority.HIGH
            elif priority_choice == 3:
                priority = Priority.LOW
            else:
                priority = Priority.MEDIUM  # Default for None or 2

        # Prompt for tags (comma-separated, optional)
        tags_input = prompt_string("Enter tags (comma-separated, optional)", required=False)
        tags = []
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        # Prompt for due date (YYYY-MM-DD, optional)
        due_date_str = prompt_string("Enter due date (YYYY-MM-DD or YYYY-M-D, optional)", required=False)
        due_date = None
        if due_date_str:
            try:
                # Normalize the input: split by '-' and zero-pad parts
                parts = due_date_str.strip().split('-')
                if len(parts) == 3:
                    year, month, day = parts
                    # Zero-pad month and day to 2 digits
                    normalized_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                    due_date = datetime.strptime(normalized_date, "%Y-%m-%d").date()
                else:
                    raise ValueError("Invalid date format")
            except (ValueError, AttributeError):
                print_error("Invalid date format. Use YYYY-MM-DD or YYYY-M-D (e.g., 2026-02-05 or 2026-2-5). Task will be created without a due date.")
                due_date = None

        # Recurrence selection - use interactive menu if available
        recurrence_rule = RecurrenceRule.NONE
        if due_date:  # Only ask for recurrence if due date is set
            if self.use_interactive:
                recurrence_items = ['None (default)', 'Daily', 'Weekly', 'Monthly']
                self.screen_manager.clear()
                print_header("Select Recurrence")
                recurrence_selected = self.menu.show("Task Recurrence", recurrence_items)

                if recurrence_selected is None or recurrence_selected == 0:
                    recurrence_rule = RecurrenceRule.NONE
                elif recurrence_selected == 1:
                    recurrence_rule = RecurrenceRule.DAILY
                elif recurrence_selected == 2:
                    recurrence_rule = RecurrenceRule.WEEKLY
                elif recurrence_selected == 3:
                    recurrence_rule = RecurrenceRule.MONTHLY
            else:
                # Traditional mode
                print("\nSelect recurrence:")
                print("  1. None (default)")
                print("  2. Daily")
                print("  3. Weekly")
                print("  4. Monthly")
                recurrence_choice = prompt_int("Enter recurrence choice", min_value=1, max_value=4)

                if recurrence_choice == 2:
                    recurrence_rule = RecurrenceRule.DAILY
                elif recurrence_choice == 3:
                    recurrence_rule = RecurrenceRule.WEEKLY
                elif recurrence_choice == 4:
                    recurrence_rule = RecurrenceRule.MONTHLY

        task, error = self.task_service.create_task(
            title=title,
            description=description,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence_rule=recurrence_rule
        )

        if error:
            if self.use_interactive:
                self.screen_manager.show_message(error, 'error')
                self.screen_manager.pause()
            else:
                print_error(error)
                press_enter_to_continue()
        else:
            if self.use_interactive:
                self.screen_manager.show_message(f"Task '{task.title}' created successfully! (ID: {task.id})", 'success')
                self.screen_manager.pause()
            else:
                print_success(f"Task created successfully! (ID: {task.id})")
                press_enter_to_continue()

    def handle_view_tasks(self) -> None:
        """
        Handle viewing all tasks.

        Displays all tasks in brief format, respecting any active filters and sort order.
        """
        # Determine which tasks to display based on active filter
        if self.active_filter == 'search':
            print_header(f"Search Results: '{self.filter_value}'")
            tasks = self.task_service.search_tasks(self.filter_value)
        elif self.active_filter == 'status':
            status_label = "Completed" if self.filter_value else "Pending"
            print_header(f"Filtered Tasks: {status_label}")
            tasks = self.task_service.filter_by_status(self.filter_value)
        elif self.active_filter == 'priority':
            print_header(f"Filtered Tasks: Priority {self.filter_value.value}")
            tasks = self.task_service.filter_by_priority(self.filter_value)
        elif self.active_filter == 'tag':
            print_header(f"Filtered Tasks: #{self.filter_value}")
            tasks = self.task_service.filter_by_tag(self.filter_value)
        else:
            print_header("All Tasks")
            tasks = self.task_service.get_all_tasks()

        # Apply sorting if active
        if self.active_sort:
            tasks = self.task_service.sort_tasks(self.active_sort, tasks)

        if not tasks:
            if self.active_filter:
                print_info("No tasks match the current filter.")
            else:
                print_info("No tasks found. Create your first task!")
        else:
            display_task_list(tasks)

        press_enter_to_continue()

    def handle_complete_toggle(self) -> None:
        """
        Handle toggling task completion status.

        Prompts user for task ID and toggles completion.
        """
        print_header("Mark Complete/Incomplete")

        task_id = prompt_int("Enter task ID", min_value=1)

        if task_id is None:
            print_error("Invalid task ID")
            press_enter_to_continue()
            return

        # Get task before toggling to check recurrence
        task = self.task_service.get_task(task_id)
        if not task:
            print_error(f"Task with ID {task_id} not found")
            press_enter_to_continue()
            return

        # Toggle completion
        success, result = self.task_service.toggle_completion(task_id)

        if not success:
            print_error(result if isinstance(result, str) else "Failed to toggle task")
        else:
            task = self.task_service.get_task(task_id)
            status = "completed" if task.completed else "incomplete"
            print_success(f"Task {task_id} marked as {status}")

            # Check if a new recurring instance was created
            if task.completed and isinstance(result, Task):
                print_info(f"Recurring task created: New task ID {result.id} scheduled for {result.due_date}")

        press_enter_to_continue()

    def handle_view_task_details(self) -> None:
        """
        Handle viewing detailed task information.

        Prompts user for task ID and displays full details.
        """
        print_header("View Task Details")

        task_id = prompt_int("Enter task ID", min_value=1)

        if task_id is None:
            print_error("Invalid task ID")
            press_enter_to_continue()
            return

        task = self.task_service.get_task(task_id)

        if not task:
            print_error(f"Task with ID {task_id} not found")
        else:
            print()
            display_task_details(task)

        press_enter_to_continue()

    def handle_update_task(self) -> None:
        """
        Handle task update flow with sequential field updates.

        Goes through each field one by one, allowing user to update or skip.
        """
        if self.use_interactive:
            self._handle_update_task_interactive()
        else:
            self._handle_update_task_traditional()

    def _handle_update_task_interactive(self) -> None:
        """Interactive sequential update flow - updates fields one by one."""
        self.screen_manager.clear()

        # Get all tasks to select from
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            self.screen_manager.show_message("No tasks available to update", 'info')
            self.screen_manager.pause()
            return

        # Select task from interactive list
        selected = self.task_list.show(tasks, "Select Task to Update")

        if selected is None or selected == 'ADD_NEW':
            return

        task = selected
        task_id = task.id

        # Track what was updated
        updates_made = []

        # 1. Update Title
        self.screen_manager.clear()
        print_header("Update Title")
        print(f"\nCurrent title: {task.title}")
        print("\nPress Enter to keep current title, or type new title:")
        new_title = prompt_string("New title", required=False)

        # Ensure new_title is a string (safety check)
        if not isinstance(new_title, str):
            new_title = str(new_title) if new_title else ""

        if new_title and new_title.strip():
            result = self.task_service.update_task_title(task_id, new_title.strip())
            success = result[0] if isinstance(result, tuple) and len(result) > 0 else False
            error = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
            if error:
                self.screen_manager.show_message(f"Error updating title: {error}", 'error')
                self.screen_manager.pause()
            elif success:
                updates_made.append("title")
                task = self.task_service.get_task(task_id)  # Refresh task

        # 2. Update Description
        self.screen_manager.clear()
        print_header("Update Description")
        current_desc = task.description if task.description else "(none)"
        print(f"\nCurrent description: {current_desc}")
        print("\nPress Enter to keep current, type new description, or type 'clear' to remove:")
        new_description = prompt_multiline("New description")

        # Ensure new_description is a string (safety check)
        if not isinstance(new_description, str):
            new_description = str(new_description) if new_description else ""

        if new_description and new_description.strip():
            if new_description.strip().lower() == 'clear':
                new_description = ""
            result = self.task_service.update_task_description(task_id, new_description)
            success = result[0] if isinstance(result, tuple) and len(result) > 0 else False
            error = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
            if error:
                self.screen_manager.show_message(f"Error updating description: {error}", 'error')
                self.screen_manager.pause()
            elif success:
                updates_made.append("description")
                task = self.task_service.get_task(task_id)  # Refresh task

        # 3. Update Priority
        self.screen_manager.clear()
        print_header("Update Priority")
        print(f"\nCurrent priority: {task.priority.value}")
        print("\nSelect new priority or Esc to keep current:")

        priority_items = ['High priority', 'Medium priority', 'Low priority', 'Keep current']
        priority_selected = self.menu.show("Priority", priority_items)

        if priority_selected is not None and priority_selected < 3:
            if priority_selected == 0:
                new_priority = Priority.HIGH
            elif priority_selected == 1:
                new_priority = Priority.MEDIUM
            else:
                new_priority = Priority.LOW

            try:
                result = self.task_service.update_task_priority(task_id, new_priority)
                # Handle tuple unpacking safely
                if isinstance(result, tuple) and len(result) >= 2:
                    success = result[0]
                    error = result[1]
                else:
                    success = False
                    error = f"Unexpected return value: {result}"

                if error:
                    self.screen_manager.show_message(f"Error updating priority: {error}", 'error')
                    self.screen_manager.pause()
                elif success:
                    updates_made.append("priority")
                    task = self.task_service.get_task(task_id)  # Refresh task
            except Exception as e:
                self.screen_manager.show_message(f"Unexpected error updating priority: {str(e)}", 'error')
                self.screen_manager.pause()

        # 4. Update Tags
        self.screen_manager.clear()
        print_header("Update Tags")
        current_tags = ", ".join(task.tags) if task.tags else "(none)"
        print(f"\nCurrent tags: {current_tags}")
        print("\nPress Enter to keep current, type new tags (comma-separated), or type 'clear' to remove:")
        tags_input = prompt_string("New tags", required=False)

        # Ensure tags_input is a string (safety check)
        if not isinstance(tags_input, str):
            tags_input = str(tags_input) if tags_input else ""

        if tags_input and tags_input.strip():
            if tags_input.strip().lower() == 'clear':
                new_tags = []
            else:
                new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

            result = self.task_service.update_task_tags(task_id, new_tags)
            success = result[0] if isinstance(result, tuple) and len(result) > 0 else False
            error = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
            if error:
                self.screen_manager.show_message(f"Error updating tags: {error}", 'error')
                self.screen_manager.pause()
            elif success:
                updates_made.append("tags")
                task = self.task_service.get_task(task_id)  # Refresh task

        # 5. Update Due Date
        self.screen_manager.clear()
        print_header("Update Due Date")
        current_due = task.due_date.strftime("%Y-%m-%d") if task.due_date else "(none)"
        print(f"\nCurrent due date: {current_due}")
        print("\nPress Enter to keep current, type new date (YYYY-MM-DD), or type 'clear' to remove:")
        due_date_str = prompt_string("New due date", required=False)

        # Ensure due_date_str is a string (safety check)
        if not isinstance(due_date_str, str):
            due_date_str = str(due_date_str) if due_date_str else ""

        if due_date_str and due_date_str.strip():
            if due_date_str.strip().lower() == 'clear':
                new_due_date = None
                result = self.task_service.update_task_due_date(task_id, new_due_date)
                success = result[0] if isinstance(result, tuple) and len(result) > 0 else False
                error = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
                if not error and success:
                    updates_made.append("due date")
                    task = self.task_service.get_task(task_id)
            else:
                # Try multiple date formats to be flexible
                date_formats = [
                    "%Y-%m-%d",    # 2026-02-05 (strict format)
                    "%Y-%m-%d",    # Also handles 2026-2-5 (Python's strptime is flexible with single digits)
                ]
                new_due_date = None
                parse_error = None

                for fmt in date_formats:
                    try:
                        # Normalize the input: split by '-' and zero-pad parts
                        parts = due_date_str.strip().split('-')
                        if len(parts) == 3:
                            year, month, day = parts
                            # Zero-pad month and day to 2 digits
                            normalized_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                            new_due_date = datetime.strptime(normalized_date, fmt).date()
                            break
                    except ValueError as e:
                        parse_error = str(e)
                        continue

                if new_due_date:
                    result = self.task_service.update_task_due_date(task_id, new_due_date)
                    success = result[0] if isinstance(result, tuple) and len(result) > 0 else False
                    error = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
                    if error:
                        self.screen_manager.show_message(f"Error updating due date: {error}", 'error')
                        self.screen_manager.pause()
                    elif success:
                        updates_made.append("due date")
                        task = self.task_service.get_task(task_id)
                else:
                    self.screen_manager.show_message("Invalid date format. Use YYYY-MM-DD (e.g., 2026-02-05 or 2026-2-5)", 'error')
                    self.screen_manager.pause()

        # Refresh task to get latest due_date before checking recurrence
        task = self.task_service.get_task(task_id)

        # 6. Update Recurrence
        if task and task.due_date:  # Only if task has due date
            self.screen_manager.clear()
            print_header("Update Recurrence")
            print(f"\nCurrent recurrence: {task.recurrence_rule.value}")
            print("\nSelect new recurrence or Esc to keep current:")

            recurrence_items = ['None', 'Daily', 'Weekly', 'Monthly', 'Keep current']
            recurrence_selected = self.menu.show("Recurrence", recurrence_items)

            if recurrence_selected is not None and recurrence_selected < 4:
                if recurrence_selected == 0:
                    new_recurrence = RecurrenceRule.NONE
                elif recurrence_selected == 1:
                    new_recurrence = RecurrenceRule.DAILY
                elif recurrence_selected == 2:
                    new_recurrence = RecurrenceRule.WEEKLY
                else:
                    new_recurrence = RecurrenceRule.MONTHLY

                result = self.task_service.update_task_recurrence(task_id, new_recurrence)
                success = result[0] if isinstance(result, tuple) and len(result) > 0 else False
                error = result[1] if isinstance(result, tuple) and len(result) > 1 else ""
                if error:
                    self.screen_manager.show_message(f"Error updating recurrence: {error}", 'error')
                    self.screen_manager.pause()
                elif success:
                    updates_made.append("recurrence")

        # Show summary
        self.screen_manager.clear()
        if updates_made:
            updated_fields = ", ".join(updates_made)
            self.screen_manager.show_message(f"Task updated successfully! Updated: {updated_fields}", 'success')
        else:
            self.screen_manager.show_message("No changes made to task", 'info')
        self.screen_manager.pause()

    def _handle_update_task_traditional(self) -> None:
        """Traditional update flow - shows menu of fields to update."""
        print_header("Update Task")

        task_id = prompt_int("Enter task ID to update", min_value=1)

        if task_id is None:
            print_error("Invalid task ID")
            press_enter_to_continue()
            return

        task = self.task_service.get_task(task_id)

        if not task:
            print_error(f"Task with ID {task_id} not found")
            press_enter_to_continue()
            return

        # Display current task
        print("\nCurrent task:")
        display_task_details(task)
        print()

        # Show update menu
        print_separator()
        print("What would you like to update?")
        print("1. Title")
        print("2. Description")
        print("3. Priority")
        print("4. Tags")
        print("5. Due Date")
        print("6. Recurrence")
        print("0. Cancel")
        print_separator()

        choice = prompt_string("Enter your choice", required=True)

        if choice == "1":
            new_title = prompt_string("Enter new title", required=True)
            success, error = self.task_service.update_task_title(task_id, new_title)
            if error:
                print_error(error)
            else:
                print_success("Title updated successfully")

        elif choice == "2":
            new_description = prompt_string("Enter new description (leave empty to clear)", required=False)
            success, error = self.task_service.update_task_description(task_id, new_description)
            if error:
                print_error(error)
            else:
                print_success("Description updated successfully")

        elif choice == "3":
            print("\nSelect new priority:")
            print("  1. High")
            print("  2. Medium")
            print("  3. Low")
            priority_choice = prompt_int("Enter priority choice", min_value=1, max_value=3)

            if priority_choice == 1:
                new_priority = Priority.HIGH
            elif priority_choice == 3:
                new_priority = Priority.LOW
            elif priority_choice == 2:
                new_priority = Priority.MEDIUM
            else:
                print_error("Invalid priority choice")
                press_enter_to_continue()
                return

            success, error = self.task_service.update_task_priority(task_id, new_priority)
            if error:
                print_error(error)
            else:
                print_success("Priority updated successfully")

        elif choice == "4":
            tags_input = prompt_string("Enter new tags (comma-separated, leave empty to clear)", required=False)
            new_tags = []
            if tags_input:
                new_tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

            success, error = self.task_service.update_task_tags(task_id, new_tags)
            if error:
                print_error(error)
            else:
                print_success("Tags updated successfully")

        elif choice == "5":
            due_date_str = prompt_string("Enter new due date (YYYY-MM-DD, leave empty to clear)", required=False)
            new_due_date = None
            if due_date_str:
                try:
                    new_due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                except ValueError:
                    print_error("Invalid date format. Due date not updated.")
                    press_enter_to_continue()
                    return

            success, error = self.task_service.update_task_due_date(task_id, new_due_date)
            if error:
                print_error(error)
            else:
                print_success("Due date updated successfully")

        elif choice == "6":
            print("\nSelect new recurrence:")
            print("  1. None")
            print("  2. Daily")
            print("  3. Weekly")
            print("  4. Monthly")
            recurrence_choice = prompt_int("Enter recurrence choice", min_value=1, max_value=4)

            if recurrence_choice == 1:
                new_recurrence = RecurrenceRule.NONE
            elif recurrence_choice == 2:
                new_recurrence = RecurrenceRule.DAILY
            elif recurrence_choice == 3:
                new_recurrence = RecurrenceRule.WEEKLY
            elif recurrence_choice == 4:
                new_recurrence = RecurrenceRule.MONTHLY
            else:
                print_error("Invalid recurrence choice")
                press_enter_to_continue()
                return

            success, error = self.task_service.update_task_recurrence(task_id, new_recurrence)
            if error:
                print_error(error)
            else:
                print_success("Recurrence updated successfully")

        elif choice == "0":
            print_info("Update cancelled")

        else:
            print_error("Invalid choice")

        press_enter_to_continue()

    def handle_delete_task(self) -> None:
        """
        Handle task deletion flow with confirmation.

        Prompts user for task ID, displays task details, confirms deletion,
        and deletes if confirmed.
        """
        print_header("Delete Task")

        task_id = prompt_int("Enter task ID to delete", min_value=1)

        if task_id is None:
            print_error("Invalid task ID")
            press_enter_to_continue()
            return

        # Get task to display and verify it exists
        task = self.task_service.get_task(task_id)

        if not task:
            print_error(f"Task with ID {task_id} not found")
            press_enter_to_continue()
            return

        # Display task to be deleted
        print("\nTask to delete:")
        display_task_details(task)
        print()

        # Confirm deletion
        confirm = prompt_yes_no(f"Are you sure you want to delete task {task_id}?", default=False)

        if not confirm:
            print_info("Deletion cancelled")
            press_enter_to_continue()
            return

        # Delete task
        success, error = self.task_service.delete_task(task_id)

        if error:
            print_error(error)
        else:
            print_success(f"Task {task_id} deleted successfully")

        press_enter_to_continue()

    def run(self) -> None:
        """
        Main application loop.

        Uses interactive arrow-key UI if enabled, otherwise falls back to numeric menu.
        """
        if self.use_interactive:
            self._run_interactive()
        else:
            self._run_numeric()

    def _run_interactive(self) -> None:
        """Main loop with interactive arrow-key navigation (Feature 008)."""
        self.running = True

        # Welcome message
        self.screen_manager.clear()
        print(self.theme.title("Phase I - Advanced Interactive In-Memory Todo CLI"))
        print()
        print(self.theme.success("Welcome to the Interactive Todo CLI!"))
        print()
        print(self.theme.warning("WARNING: Data is stored in memory only."))
        print(self.theme.dim("         All tasks will be lost when you exit."))
        print()
        self.screen_manager.pause()

        while self.running:
            try:
                # Main menu items
                items = [
                    'Add task',
                    'View all tasks',
                    'Search tasks',
                    'Filter tasks',
                    'Sort tasks',
                    'Mark complete/incomplete',
                    'Update task',
                    'Delete task',
                    'View recurring tasks',
                    'Exit'
                ]

                selected = self.menu.show("Todo Application", items)

                # Handle shortcuts (negative values)
                if selected == -1:  # Help shortcut '?'
                    self.screen_manager.show_help_overlay()
                elif selected == -2:  # Add shortcut 'a'
                    self.handle_add_task()
                elif selected == -3:  # Filter shortcut 'f'
                    self.handle_filter_tasks()
                elif selected == -4:  # Sort shortcut 's'
                    self.handle_sort_tasks()
                elif selected == -5:  # Search shortcut '/'
                    self.handle_search_tasks()
                # Handle normal menu selections
                elif selected is None or selected == 9:  # Exit or cancelled
                    self.handle_exit()
                elif selected == 0:
                    self.handle_add_task()
                elif selected == 1:
                    self.handle_view_all_interactive()  # Use interactive task list
                elif selected == 2:
                    self.handle_search_tasks()
                elif selected == 3:
                    self.handle_filter_tasks()
                elif selected == 4:
                    self.handle_sort_tasks()
                elif selected == 5:
                    self.handle_complete_toggle()
                elif selected == 6:
                    self.handle_update_task()
                elif selected == 7:
                    self.handle_delete_task()
                elif selected == 8:
                    self.handle_view_recurring_tasks()

            except KeyboardInterrupt:
                self.handle_exit()
                break
            except Exception as e:
                self.screen_manager.show_message(f"Error: {str(e)}", 'error')
                self.screen_manager.pause()

    def _run_numeric(self) -> None:
        """Original numeric menu loop (backward compatibility)."""
        self.running = True
        print_header("Phase I - Advanced Interactive In-Memory Todo CLI")
        print()
        print("Welcome to the Todo CLI!")
        print()
        print("WARNING: Data is stored in memory only.")
        print("         All tasks will be lost when you exit.")
        print()
        press_enter_to_continue()

        while self.running:
            try:
                clear_screen()
                self.display_main_menu()

                choice = prompt_string("Enter your choice", required=True)

                if choice == "1":
                    self.handle_add_task()
                elif choice == "2":
                    self.handle_view_tasks()
                elif choice == "3":
                    self.handle_view_task_details()
                elif choice == "4":
                    self.handle_update_task()
                elif choice == "5":
                    self.handle_delete_task()
                elif choice == "6":
                    self.handle_complete_toggle()
                elif choice == "7":
                    self.handle_search_tasks()
                elif choice == "8":
                    self.handle_filter_tasks()
                elif choice == "9":
                    self.handle_sort_tasks()
                elif choice == "10":
                    clear_screen()
                    print_success("Screen cleared")
                    press_enter_to_continue()
                elif choice == "0":
                    self.handle_exit()
                else:
                    print_error("Invalid choice. Please enter a number from the menu.")
                    press_enter_to_continue()

            except KeyboardInterrupt:
                print()
                print_info("Interrupted. Returning to menu...")
                press_enter_to_continue()
            except Exception as e:
                print_error(f"An unexpected error occurred: {str(e)}")
                print_info("Returning to main menu...")
                press_enter_to_continue()

    def handle_search_tasks(self) -> None:
        """
        Handle task search flow.

        Prompts for keyword and searches in title and description.
        Sets active filter to show search results in View All Tasks.
        """
        # Clear screen
        if self.use_interactive:
            self.screen_manager.clear()
        else:
            clear_screen()

        print_header("Search Tasks")

        keyword = prompt_string("Enter search keyword", required=True)

        tasks = self.task_service.search_tasks(keyword)

        # Set active filter
        self.active_filter = 'search'
        self.filter_value = keyword

        if self.use_interactive:
            if tasks:
                self.screen_manager.clear()
                print(self.theme.title(f"Search Results: {len(tasks)} task(s) found"))
                print()
                display_task_list(tasks)
                print()
                print(self.theme.dim("Filter active. 'View All Tasks' will show these results."))
                print(self.theme.dim("Use 'Filter Tasks' menu to change or clear filters."))
                self.screen_manager.pause()
            else:
                self.screen_manager.show_message("No tasks found matching your search.", 'info')
                self.screen_manager.pause()
        else:
            print(f"\nFound {len(tasks)} task(s) matching '{keyword}':")
            print()

            if tasks:
                display_task_list(tasks)
                print()
                print_info(f"Filter active. 'View All Tasks' will show these results.")
                print_info("Use 'Filter Tasks' to change or clear filters.")
            else:
                print_info("No tasks found matching your search.")

            press_enter_to_continue()

    def handle_filter_tasks(self) -> None:
        """
        Handle task filter flow.

        Shows filter sub-menu with options:
        1 = Filter by Status (completed/pending)
        2 = Filter by Priority
        3 = Filter by Tag
        0 = Cancel
        """
        # Clear screen
        if self.use_interactive:
            self.screen_manager.clear()

            # Use interactive menu
            items = [
                'Filter by Status',
                'Filter by Priority',
                'Filter by Tag',
                'Clear All Filters',
                'Cancel'
            ]

            selected = self.menu.show("Filter Tasks", items)

            if selected is None or selected == 4:  # Cancel
                return

            choice = str(selected + 1)  # Convert to old numbering
        else:
            clear_screen()
            print_header("Filter Tasks")

            print_separator()
            print("Filter by:")
            print("1. Status (Completed/Pending)")
            print("2. Priority")
            print("3. Tag")
            print("4. Clear All Filters")
            print("0. Cancel")
            print_separator()

            choice = prompt_string("Enter your choice", required=True)

        if choice == "1":
            # Filter by status
            if self.use_interactive:
                status_items = ['Completed tasks', 'Pending tasks', 'Cancel']
                status_selected = self.menu.show("Filter by Status", status_items)

                if status_selected is None or status_selected == 2:  # Cancel
                    return

                status_choice = str(status_selected + 1)
            else:
                status_choice = prompt_string("Show (1) Completed or (2) Pending tasks?", required=True)

            if status_choice == "1":
                completed = True
                tasks = self.task_service.filter_by_status(True)
                self.active_filter = 'status'
                self.filter_value = True
                if self.use_interactive:
                    self.screen_manager.show_message(f"Filtered to {len(tasks)} completed task(s)", 'success')
                    self.screen_manager.pause()
                else:
                    print(f"\nFiltered to {len(tasks)} completed task(s)")
            elif status_choice == "2":
                completed = False
                tasks = self.task_service.filter_by_status(False)
                self.active_filter = 'status'
                self.filter_value = False
                if self.use_interactive:
                    self.screen_manager.show_message(f"Filtered to {len(tasks)} pending task(s)", 'success')
                    self.screen_manager.pause()
                else:
                    print(f"\nFiltered to {len(tasks)} pending task(s)")
            else:
                print_error("Invalid choice")
                press_enter_to_continue()
                return

        elif choice == "2":
            # Filter by priority
            if self.use_interactive:
                priority_items = ['High priority', 'Medium priority', 'Low priority', 'Cancel']
                priority_selected = self.menu.show("Filter by Priority", priority_items)

                if priority_selected is None or priority_selected == 3:  # Cancel
                    return

                priority_choice = priority_selected + 1
            else:
                print("\nSelect priority:")
                print("  1. High")
                print("  2. Medium")
                print("  3. Low")
                priority_choice = prompt_int("Enter priority choice", min_value=1, max_value=3)

            if priority_choice == 1:
                priority = Priority.HIGH
            elif priority_choice == 2:
                priority = Priority.MEDIUM
            elif priority_choice == 3:
                priority = Priority.LOW
            else:
                print_error("Invalid priority choice")
                press_enter_to_continue()
                return

            tasks = self.task_service.filter_by_priority(priority)
            self.active_filter = 'priority'
            self.filter_value = priority

            if self.use_interactive:
                self.screen_manager.show_message(f"Filtered to {len(tasks)} {priority.value} priority task(s)", 'success')
                self.screen_manager.pause()
            else:
                print(f"\nFiltered to {len(tasks)} task(s) with priority {priority.value}")

        elif choice == "3":
            tag = prompt_string("Enter tag to filter by", required=True)
            tasks = self.task_service.filter_by_tag(tag)
            self.active_filter = 'tag'
            self.filter_value = tag
            print(f"\nFiltered to {len(tasks)} task(s) with tag #{tag}")

        elif choice == "4":
            # Clear all filters
            self.handle_clear_filters()
            return

        elif choice == "0":
            print_info("Filter cancelled")
            press_enter_to_continue()
            return

        else:
            print_error("Invalid choice")
            press_enter_to_continue()
            return

        # Display filtered results
        if tasks:
            print()
            display_task_list(tasks)
            print()
            print_info(f"Filter active. 'View All Tasks' will show these results.")
            print_info("Return to 'Filter Tasks' (option 8) to change or clear.")
        else:
            print_info("No tasks match the selected filter.")

        press_enter_to_continue()

    def handle_clear_filters(self) -> None:
        """
        Handle clearing all active filters and sort order.

        Resets view to show all tasks in default order.
        """
        print_header("Clear Filters and Sort")

        has_filter = self.active_filter is not None
        has_sort = self.active_sort is not None

        if has_filter or has_sort:
            self.active_filter = None
            self.filter_value = None
            self.active_sort = None
            print_success("All filters and sort order cleared. 'View All Tasks' will now show all tasks in default order.")
        else:
            print_info("No active filters or sort order to clear.")

        press_enter_to_continue()

    def handle_sort_tasks(self) -> None:
        """
        Handle task sorting flow.

        Shows sort sub-menu with options:
        1 = Sort by Due Date
        2 = Sort by Priority
        3 = Sort by Alphabetical
        4 = Reset to Default Order
        0 = Cancel
        """
        # Clear screen
        if self.use_interactive:
            self.screen_manager.clear()

            # Use interactive menu
            items = [
                'Sort by Due Date',
                'Sort by Priority',
                'Sort by Alphabetical',
                'Reset to Default Order',
                'Cancel'
            ]

            selected = self.menu.show("Sort Tasks", items)

            if selected is None or selected == 4:  # Cancel
                return

            choice = str(selected + 1)  # Convert to old numbering
        else:
            clear_screen()
            print_header("Sort Tasks")

            print_separator()
            print("Sort by:")
            print("1. Due Date (overdue first, then chronological)")
            print("2. Priority (High → Medium → Low)")
            print("3. Alphabetical (A-Z by title)")
            print("4. Reset to Default Order (creation order)")
            print("0. Cancel")
            print_separator()

            choice = prompt_string("Enter your choice", required=True)

        if choice == "1":
            self.active_sort = SortOption.DUE_DATE
            if self.use_interactive:
                self.screen_manager.show_message("Sort order set to: Due Date", 'success')
                self.screen_manager.pause()
            else:
                print_success("Sort order set to: Due Date")
                print_info("'View All Tasks' will now show tasks sorted by due date.")

        elif choice == "2":
            self.active_sort = SortOption.PRIORITY
            if self.use_interactive:
                self.screen_manager.show_message("Sort order set to: Priority", 'success')
                self.screen_manager.pause()
            else:
                print_success("Sort order set to: Priority (High → Medium → Low)")
                print_info("'View All Tasks' will now show tasks sorted by priority.")

        elif choice == "3":
            self.active_sort = SortOption.ALPHABETICAL
            if self.use_interactive:
                self.screen_manager.show_message("Sort order set to: Alphabetical", 'success')
                self.screen_manager.pause()
            else:
                print_success("Sort order set to: Alphabetical (A-Z)")
                print_info("'View All Tasks' will now show tasks sorted alphabetically.")

        elif choice == "4":
            self.active_sort = None
            if self.use_interactive:
                self.screen_manager.show_message("Sort order reset to default", 'success')
                self.screen_manager.pause()
            else:
                print_success("Sort order reset to default (creation order)")
                print_info("'View All Tasks' will now show tasks in creation order.")

        elif choice == "0":
            if not self.use_interactive:
                print_info("Sort cancelled")

        else:
            print_error("Invalid choice")

        if not self.use_interactive:
            press_enter_to_continue()

    def handle_exit(self) -> None:
        """
        Handle application exit.

        Confirms exit and terminates application with farewell message.
        """
        print_header("Exit Application")
        confirm = prompt_yes_no("Are you sure you want to exit? All data will be lost.", default=False)

        if confirm:
            print_separator()
            print("All data has been discarded.")
            print("Thank you for using Todo CLI!")
            print_separator()
            self.running = False
        else:
            print_info("Exit cancelled. Returning to main menu.")
            press_enter_to_continue()

    # ========================================
    # Interactive UI Methods (Feature 008)
    # ========================================

    def handle_view_all_interactive(self) -> None:
        """Handle viewing all tasks with interactive navigation (Feature 008)."""
        tasks = self.task_service.get_all_tasks()

        # Apply sorting if active
        if self.active_sort:
            tasks = self.task_service.sort_tasks(self.active_sort, tasks)

        # Show interactive task list
        selected = self.task_list.show(tasks, "All Tasks")

        if selected == 'ADD_NEW':
            self.handle_add_task()
        elif selected:
            # Show contextual menu for selected task
            self._show_task_actions(selected)

    def _show_task_actions(self, task: Task) -> None:
        """
        Show contextual menu for a selected task (Feature 008).

        Args:
            task: Selected task to show actions for
        """
        while True:
            # Create contextual menu
            actions = [
                'View Details',
                'Edit Task',
                'Toggle Complete',
                'Delete Task',
                'Back'
            ]

            # Show task info in title
            status = "✓" if task.completed else "□"
            title = f"{status} {task.title}"

            selected_action = self.menu.show(title, actions)

            if selected_action is None or selected_action == 4:  # Back
                break
            elif selected_action == 0:  # View Details
                self._view_task_details_interactive(task)
            elif selected_action == 1:  # Edit
                self._edit_task_interactive(task)
            elif selected_action == 2:  # Toggle Complete
                self._toggle_task_interactive(task)
            elif selected_action == 3:  # Delete
                if self._delete_task_interactive(task):
                    break  # Return to task list after deletion

    def _view_task_details_interactive(self, task: Task) -> None:
        """View task details in interactive mode."""
        self.screen_manager.clear()
        print(self.theme.title(f"Task Details: {task.title}"))
        print()
        print(format_task_detailed(task))
        print()
        self.screen_manager.pause()

    def _edit_task_interactive(self, task: Task) -> None:
        """Edit task in interactive mode."""
        # For now, fall back to traditional prompts for editing
        # Full interactive editing would require more complex input handling
        self.screen_manager.clear()
        print(self.theme.title(f"Edit Task: {task.title}"))
        print()
        print(self.theme.dim("Note: Use traditional input for editing"))
        print()

        # Edit title
        new_title = prompt_string("Enter new title (leave empty to keep current)", required=False)
        if new_title:
            task.title = new_title

        # Edit description
        print()
        edit_desc = prompt_yes_no("Edit description?", default=False)
        if edit_desc:
            new_desc = prompt_multiline("Enter new description")
            if new_desc:
                task.description = new_desc

        self.screen_manager.show_message(f"Task '{task.title}' updated", 'success')
        self.screen_manager.pause()

    def _toggle_task_interactive(self, task: Task) -> None:
        """Toggle task completion status in interactive mode."""
        task.completed = not task.completed
        status_text = "completed" if task.completed else "incomplete"
        self.screen_manager.show_message(f"Task marked as {status_text}", 'success')
        self.screen_manager.pause()

    def _delete_task_interactive(self, task: Task) -> bool:
        """
        Delete task in interactive mode.

        Returns:
            True if deleted, False if cancelled
        """
        self.screen_manager.clear()
        print(self.theme.warning(f"Delete task: {task.title}?"))
        print()
        confirm = prompt_yes_no("Are you sure?", default=False)

        if confirm:
            self.task_service.delete_task(task.id)
            self.screen_manager.show_message(f"Task '{task.title}' deleted", 'success')
            self.screen_manager.pause()
            return True

        return False

    def handle_view_recurring_tasks(self) -> None:
        """
        Handle viewing recurring tasks (Feature 008 compatible).

        Shows all tasks that have a recurrence rule set.
        """
        # Clear screen
        if self.use_interactive:
            self.screen_manager.clear()

        # Get all tasks with recurrence
        from src.models.task import RecurrenceRule
        all_tasks = self.task_service.get_all_tasks()
        recurring_tasks = [t for t in all_tasks if t.recurrence_rule != RecurrenceRule.NONE]

        if self.use_interactive:
            if recurring_tasks:
                # Show interactive task list
                selected = self.task_list.show(recurring_tasks, "Recurring Tasks")

                if selected == 'ADD_NEW':
                    self.handle_add_task()
                elif selected:
                    # Show contextual menu for selected task
                    self._show_task_actions(selected)
            else:
                self.screen_manager.show_message("No recurring tasks found", 'info')
                self.screen_manager.pause()
        else:
            # Traditional mode
            clear_screen()
            print_header("Recurring Tasks")

            if recurring_tasks:
                display_task_list(recurring_tasks)
            else:
                print_info("No recurring tasks found")

            press_enter_to_continue()
