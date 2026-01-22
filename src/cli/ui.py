"""
User interface components for the CLI.
Handles display formatting and user prompts.
"""

from typing import List
from src.models.task import Task


def display_task(task: Task, show_description: bool = True) -> None:
    """Display a single task with status symbol and optional description"""
    status_symbol = "✓" if task.status == "complete" else "✗"
    print(f"{task.id} {status_symbol} {task.title}")
    if show_description and task.description:
        # Handle multi-line descriptions
        for line in task.description.split("\n"):
            print(f"         {line}")


def display_task_list(tasks: List[Task]) -> None:
    """Display all tasks or empty list message"""
    if not tasks:
        print("No tasks found. Your task list is empty.")
        return

    for task in tasks:
        display_task(task)
        print()  # Blank line between tasks


def display_current_task_details(task: Task) -> None:
    """Display current task details before update"""
    print(f"\nTask ID: {task.id}")
    print(f"Current title: {task.title}")
    print(f"Current description: {task.description if task.description else 'No description'}\n")


def prompt_confirmation(task_id: str, title: str, max_attempts: int = 3) -> bool:
    """
    Prompt for deletion confirmation with retry limit.
    Returns True if confirmed, False if cancelled or max retries exceeded.
    """
    prompt = f"Are you sure you want to delete {task_id}: {title}? (yes/no): "
    attempts = 0

    while attempts < max_attempts:
        response = input(prompt).strip().lower()

        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            print(f"Deletion cancelled. Task '{task_id}' has not been deleted.")
            return False
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("Error: Maximum retry attempts exceeded. Returning to main menu.")
                return False

    return False


def display_menu() -> None:
    """Display main menu options"""
    print("\n=== Todo Application ===")
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Task Status")
    print("6. Exit")
    print()
