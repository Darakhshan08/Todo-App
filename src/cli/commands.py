"""
Command handlers for the CLI application.
Each command function prompts for user input and calls the appropriate service method.
"""

from src.services.task_service import TaskService
from src.cli.ui import (
    display_task,
    display_task_list,
    display_current_task_details,
    prompt_confirmation
)


def add_task_command(service: TaskService) -> None:
    """
    Handle Add Task operation.
    Prompts for title and optional description, creates task, displays confirmation.
    """
    print("\n=== Add New Task ===")

    # Prompt for title
    title = input("Enter task title: ").strip()

    # Prompt for description
    print("Enter task description (or press Enter to skip):")
    print("Tip: Use \\n for line breaks (e.g., 'Step 1\\nStep 2\\nStep 3')")
    description = input("> ").strip()

    # Call service to add task
    task, error = service.add_task(title, description)

    if error:
        print(f"\n{error}")
        return

    # Display success confirmation
    print(f"\nTask created successfully!")
    display_task(task)


def view_list_command(service: TaskService) -> None:
    """
    Handle View Task List operation.
    Retrieves all tasks and displays them with status symbols.
    """
    print("\n=== Task List ===")
    tasks = service.get_all_tasks()
    display_task_list(tasks)


def update_task_command(service: TaskService) -> None:
    """
    Handle Update Task operation.
    Prompts for task ID, shows current values, prompts for new values, updates task.
    """
    print("\n=== Update Task ===")

    # Prompt for task ID
    task_id = input("Enter task ID to update: ").strip()

    # Find and display current task
    task = service.get_task_by_id(task_id)
    if not task:
        print(f"\nError: Task with ID '{task_id}' not found.")
        return

    # Show current values
    display_current_task_details(task)

    # Prompt for new title
    print("Enter new title (or press Enter to keep current):")
    new_title = input("> ").strip()

    # Prompt for new description
    print("Enter new description (or press Enter to keep current):")
    print("Tip: Use \\n for line breaks (e.g., 'Step 1\\nStep 2\\nStep 3')")
    new_description = input("> ").strip()

    # Determine what to update
    title_to_update = new_title if new_title else None
    desc_to_update = new_description if new_description else None

    # Call service to update task
    updated_task, error = service.update_task(task_id, title_to_update, desc_to_update)

    if error:
        print(f"\n{error}")
        return

    # Display success confirmation
    print(f"\nTask updated successfully!")
    display_task(updated_task)


def delete_task_command(service: TaskService) -> None:
    """
    Handle Delete Task operation.
    Prompts for task ID, shows task, confirms deletion, removes task.
    """
    print("\n=== Delete Task ===")

    # Prompt for task ID
    task_id = input("Enter task ID to delete: ").strip()

    # Find task
    task = service.get_task_by_id(task_id)
    if not task:
        print(f"\nError: Task with ID '{task_id}' not found. No deletion performed.")
        return

    # Show task and confirm deletion
    print("\nTask to be deleted:")
    display_task(task)
    print()

    confirmed = prompt_confirmation(task_id, task.title)

    if not confirmed:
        return

    # Delete task
    success, error = service.delete_task(task_id)

    if error:
        print(f"\n{error}")
        return

    print(f"\nTask '{task_id}' has been deleted successfully.")


def toggle_status_command(service: TaskService) -> None:
    """
    Handle Toggle Task Status operation.
    Prompts for task ID, toggles status between complete/incomplete, displays new status.
    """
    print("\n=== Toggle Task Status ===")

    # Prompt for task ID
    task_id = input("Enter task ID to toggle status: ").strip()

    # Toggle status
    task, error = service.toggle_task_status(task_id)

    if error:
        print(f"\n{error}")
        return

    # Display confirmation with new status
    status_word = "complete" if task.status == "complete" else "incomplete"
    print(f"\nTask '{task_id}: {task.title}' is now {status_word}.")
    display_task(task, show_description=False)
