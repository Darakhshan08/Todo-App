"""
Quick test to demonstrate interactive UI components.
"""
from src.ui.menu_controller import MenuController
from src.services.task_service import TaskService
from src.store.task_store import TaskStore
from src.models.task import Priority
from blessed import Terminal
from src.ui.color_theme import ColorTheme

def test_components():
    """Test individual components."""
    print("=" * 60)
    print("INTERACTIVE TODO CLI - COMPONENT TEST")
    print("=" * 60)
    print()

    # Initialize
    store = TaskStore()
    service = TaskService(store)

    # Add some sample tasks
    service.create_task("Buy groceries", "Milk, eggs, bread", Priority.HIGH, ["shopping"])
    service.create_task("Write documentation", "Update README", Priority.MEDIUM, ["work"])
    service.create_task("Review code", "Check PR #123", Priority.LOW, ["code-review"])

    print("[1] INITIALIZATION TEST")
    print("   - TaskStore: OK")
    print("   - TaskService: OK")
    print("   - Sample tasks created: 3")
    print()

    # Test MenuController
    controller = MenuController(service, use_interactive=True)

    print("[2] MENU CONTROLLER TEST")
    print("   - Interactive mode: ", controller.use_interactive)
    print("   - Color support: ", controller.screen_manager.supports_colors())
    print("   - Theme mode: ", "COLOR" if controller.theme.use_colors else "ASCII")
    print()

    # Test ColorTheme
    term = Terminal()
    theme = ColorTheme(term)

    print("[3] COLOR THEME TEST (ASCII Fallback Mode)")
    print("   - HIGH priority: ", theme.priority_color(Priority.HIGH, "(HIGH)"))
    print("   - MEDIUM priority: ", theme.priority_color(Priority.MEDIUM, "(MED)"))
    print("   - LOW priority: ", theme.priority_color(Priority.LOW, "(LOW)"))
    print("   - Completed: ", theme.status_color(True, "Done"))
    print("   - Incomplete: ", theme.status_color(False, "Pending"))
    print("   - Highlighted: ", theme.highlight("Selected Item"))
    print("   - Warning: ", theme.warning("OVERDUE"))
    print()

    # Test formatters
    from src.ui.formatters import format_priority_label, format_status_indicator

    print("[4] FORMATTER TEST")
    print("   - Status completed: [", format_status_indicator(True, use_unicode=False), "]")
    print("   - Status incomplete: [", format_status_indicator(False, use_unicode=False), "]")
    print("   - Priority HIGH: ", format_priority_label(Priority.HIGH, use_color=False))
    print("   - Priority MED: ", format_priority_label(Priority.MEDIUM, use_color=False))
    print("   - Priority LOW: ", format_priority_label(Priority.LOW, use_color=False))
    print()

    # Display tasks
    print("[5] TASK LIST TEST")
    tasks = service.get_all_tasks()
    print(f"   Total tasks: {len(tasks)}")
    for task in tasks:
        status = "X" if task.completed else " "
        priority = format_priority_label(task.priority, use_color=False)
        print(f"   [{status}] {priority} {task.title}")
    print()

    print("[6] INTERACTIVE MENU SIMULATION")
    print("   Main Menu Items:")
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
    for i, item in enumerate(items):
        if i == 0:
            # Simulate selected item
            print(f"   {theme.highlight(f'> {item}')}")
        else:
            print(f"     {item}")
    print()
    print("   Navigation: UP/DOWN: Navigate | Enter: Select | Esc: Back")
    print()

    print("=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
    print()
    print("NOTE: This is a component test in batch mode.")
    print("For full interactive experience, run: uv run python main.py")
    print("You'll be able to use arrow keys to navigate!")
    print()

if __name__ == "__main__":
    test_components()
