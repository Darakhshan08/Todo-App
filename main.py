"""
Phase I - Advanced Interactive In-Memory Todo CLI
Entry point for the application.
"""
from src.store.task_store import TaskStore
from src.services.validation_service import ValidationService
from src.services.task_service import TaskService
from src.ui.menu_controller import MenuController


def main():
    """Main entry point for the Todo CLI application."""
    # Initialize components
    task_store = TaskStore()
    task_service = TaskService(task_store)
    menu_controller = MenuController(task_service)

    # Run application
    menu_controller.run()


if __name__ == "__main__":
    main()
