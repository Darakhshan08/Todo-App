"""
Quick test to verify Phase I basic functionality.
"""
from src.store.task_store import TaskStore
from src.services.task_service import TaskService
from src.models.task import Priority, RecurrenceRule


def test_basic_operations():
    """Test basic CRUD operations."""
    print("Testing Phase I - User Story 1 (Basic Task Management)...")
    print("=" * 60)

    # Initialize components
    task_store = TaskStore()
    task_service = TaskService(task_store)

    # Test 1: Create task
    print("\n1. Creating a task...")
    task1, error = task_service.create_task(
        title="Buy groceries",
        description="Milk, eggs, bread"
    )
    if error:
        print(f"   ERROR: {error}")
        return False
    print(f"   [OK] Task created: ID={task1.id}, Title='{task1.title}'")

    # Test 2: Create another task
    print("\n2. Creating another task...")
    task2, error = task_service.create_task(
        title="Write documentation",
        description="Complete Phase I docs",
        priority=Priority.HIGH
    )
    if error:
        print(f"   ERROR: {error}")
        return False
    print(f"   [OK] Task created: ID={task2.id}, Title='{task2.title}', Priority={task2.priority.value}")

    # Test 3: View all tasks
    print("\n3. Viewing all tasks...")
    all_tasks = task_service.get_all_tasks()
    print(f"   [OK] Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {task.id}. {status} [{task.priority.value}] {task.title}")

    # Test 4: Complete a task
    print(f"\n4. Completing task {task1.id}...")
    success, error = task_service.complete_task(task1.id)
    if error:
        print(f"   ERROR: {error}")
        return False
    print(f"   [OK] Task {task1.id} marked as completed")

    # Test 5: View tasks after completion
    print("\n5. Viewing all tasks after completion...")
    all_tasks = task_service.get_all_tasks()
    for task in all_tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"   {task.id}. {status} [{task.priority.value}] {task.title}")

    # Test 6: Toggle completion
    print(f"\n6. Toggling completion for task {task1.id}...")
    success, error = task_service.toggle_completion(task1.id)
    if error:
        print(f"   ERROR: {error}")
        return False
    task_check = task_service.get_task(task1.id)
    status = "completed" if task_check.completed else "incomplete"
    print(f"   [OK] Task {task1.id} is now: {status}")

    # Test 7: Validation test (empty title)
    print("\n7. Testing validation (empty title should fail)...")
    task_invalid, error = task_service.create_task(title="   ", description="Test")
    if error:
        print(f"   [OK] Validation worked: {error}")
    else:
        print(f"   ERROR: Empty title was accepted (should have failed)")
        return False

    print("\n" + "=" * 60)
    print("[OK] All tests passed! User Story 1 is functional.")
    print("=" * 60)
    return True


if __name__ == "__main__":
    success = test_basic_operations()
    if not success:
        print("\n[ERROR] Tests failed.")
        exit(1)
