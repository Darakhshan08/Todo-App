"""
Menu controller for Phase I Todo CLI.
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


class MenuController:
    """
    Controls the main menu loop and user interactions.

    Coordinates between user input and task service operations.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize MenuController.

        Args:
            task_service: TaskService instance for business logic
        """
        self.task_service = task_service
        self.running = False
        # View state for filters
        self.active_filter = None  # Type of filter: 'search', 'status', 'priority', 'tag', or None
        self.filter_value = None   # Value for the active filter
        # View state for sorting
        self.active_sort = None  # SortOption or None for default

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
        print_header("Add New Task")

        title = prompt_string("Enter task title", required=True)
        description = prompt_multiline("Enter description (optional)")

        # Prompt for priority (1=High, 2=Medium, 3=Low, default=2)
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
        due_date_str = prompt_string("Enter due date (YYYY-MM-DD, optional)", required=False)
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            except ValueError:
                print_error("Invalid date format. Task will be created without a due date.")
                due_date = None

        # Prompt for recurrence (1=None, 2=Daily, 3=Weekly, 4=Monthly, default=1)
        recurrence_rule = RecurrenceRule.NONE
        if due_date:  # Only ask for recurrence if due date is set
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
            print_error(error)
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
        Handle task update flow.

        Shows update sub-menu with options:
        1 = Update Title
        2 = Update Description
        3 = Update Priority
        4 = Update Tags
        0 = Cancel
        """
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

        Displays menu, processes user input, and executes commands until exit.
        """
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
        print_header("Search Tasks")

        keyword = prompt_string("Enter search keyword", required=True)

        tasks = self.task_service.search_tasks(keyword)

        # Set active filter
        self.active_filter = 'search'
        self.filter_value = keyword

        print(f"\nFound {len(tasks)} task(s) matching '{keyword}':")
        print()

        if tasks:
            display_task_list(tasks)
            print()
            print_info(f"Filter active. 'View All Tasks' will show these results.")
            print_info("Use 'Filter Tasks' (option 8) to change or clear filters.")
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
            status_choice = prompt_string("Show (1) Completed or (2) Pending tasks?", required=True)
            if status_choice == "1":
                completed = True
                tasks = self.task_service.filter_by_status(True)
                self.active_filter = 'status'
                self.filter_value = True
                print(f"\nFiltered to {len(tasks)} completed task(s)")
            elif status_choice == "2":
                completed = False
                tasks = self.task_service.filter_by_status(False)
                self.active_filter = 'status'
                self.filter_value = False
                print(f"\nFiltered to {len(tasks)} pending task(s)")
            else:
                print_error("Invalid choice")
                press_enter_to_continue()
                return

        elif choice == "2":
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
            print_success("Sort order set to: Due Date")
            print_info("'View All Tasks' will now show tasks sorted by due date.")

        elif choice == "2":
            self.active_sort = SortOption.PRIORITY
            print_success("Sort order set to: Priority (High → Medium → Low)")
            print_info("'View All Tasks' will now show tasks sorted by priority.")

        elif choice == "3":
            self.active_sort = SortOption.ALPHABETICAL
            print_success("Sort order set to: Alphabetical (A-Z)")
            print_info("'View All Tasks' will now show tasks sorted alphabetically.")

        elif choice == "4":
            self.active_sort = None
            print_success("Sort order reset to default (creation order)")
            print_info("'View All Tasks' will now show tasks in creation order.")

        elif choice == "0":
            print_info("Sort cancelled")

        else:
            print_error("Invalid choice")

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
