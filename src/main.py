"""
Main entry point for the Todo CLI application.
Displays menu, handles user input routing, and manages the main application loop.
"""

import sys
from pathlib import Path

# Add project root to Python path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.services.task_service import TaskService
from src.cli.ui import display_menu
from src.cli.commands import (
    add_task_command,
    view_list_command,
    update_task_command,
    delete_task_command,
    toggle_status_command
)


def main() -> None:
    """
    Main application loop.
    Initializes service, displays menu, routes commands, loops until exit.
    """
    # Initialize task service
    service = TaskService()

    print("Welcome to Todo Application!")
    print("Manage your tasks efficiently from the command line.\n")

    while True:
        # Display menu
        display_menu()

        # Get user choice
        choice = input("Enter your choice (1-6): ").strip()

        # Route to appropriate command handler
        if choice == "1":
            add_task_command(service)
        elif choice == "2":
            view_list_command(service)
        elif choice == "3":
            update_task_command(service)
        elif choice == "4":
            delete_task_command(service)
        elif choice == "5":
            toggle_status_command(service)
        elif choice == "6":
            print("\nThank you for using Todo Application. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please enter a number between 1 and 6.")

        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
