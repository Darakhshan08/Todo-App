"""
Output formatting utilities for Phase I Todo CLI.
"""
from src.models.task import Task, Priority


def format_status_indicator(completed: bool) -> str:
    """
    Format completion status indicator.

    Args:
        completed: Completion status

    Returns:
        "X" if completed, " " (space) if incomplete

    Example:
        format_status_indicator(True) -> "X"
        format_status_indicator(False) -> " "
    """
    return "X" if completed else " "


def format_task_line(task: Task) -> str:
    """
    Format a single task for list view (alias for format_task_brief).

    Args:
        task: Task to format

    Returns:
        Formatted single-line string

    Example:
        "1. [X] [HIGH] Buy groceries"
    """
    return format_task_brief(task)


def display_task_list(tasks: list[Task]) -> None:
    """
    Display list of tasks to console.

    Args:
        tasks: List of tasks to display

    Example output:
        1. [X] [HIGH] Buy groceries
        2. [ ] [MEDIUM] Write documentation
        3. [ ] [LOW] Review code
    """
    formatted = format_task_list(tasks)
    print(formatted)


def display_task_details(task: Task) -> None:
    """
    Display detailed task information to console.

    Args:
        task: Task to display

    Example output:
        ID: 1
        Title: Buy groceries
        Description: Milk, eggs, bread
        Status: Completed
        Priority: HIGH
        Tags: shopping, urgent
        Due Date: 2025-12-31
        Recurrence: WEEKLY
    """
    formatted = format_task_detailed(task)
    print(formatted)


def format_task_brief(task: Task) -> str:
    """
    Format task in brief view (single line).

    Args:
        task: Task to format

    Returns:
        Formatted string showing ID, completion status, priority, title, tags, and due date

    Example:
        "1. [X] (HIGH) Buy groceries #shopping #urgent | Due: 2026-01-25"
        "2. [ ] (MED) Write documentation"
    """
    status_symbol = "X" if task.completed else " "
    priority_label = format_priority_label(task.priority)
    tags_str = format_tags(task.tags)
    due_str = format_due_date(task)
    recur_str = format_recurrence(task)

    # Build task line
    parts = [f"{task.id}. [{status_symbol}] {priority_label} {task.title}"]
    if recur_str:
        parts.append(recur_str)
    if tags_str:
        parts.append(tags_str)
    if due_str:
        parts.append(f"| {due_str}")

    return " ".join(parts)


def format_task_detailed(task: Task) -> str:
    """
    Format task in detailed view (multi-line).

    Args:
        task: Task to format

    Returns:
        Multi-line formatted string with all task details

    Example:
        ID: 1
        Title: Buy groceries
        Description: Milk, eggs, bread
        Status: Completed
        Priority: HIGH
        Tags: shopping, urgent
        Due Date: 2025-12-31
        Recurrence: WEEKLY
    """
    lines = [
        f"ID: {task.id}",
        f"Title: {task.title}",
        f"Description: {task.description if task.description else '(none)'}",
        f"Status: {'Completed' if task.completed else 'Incomplete'}",
        f"Priority: {task.priority.value}",
        f"Tags: {', '.join(task.tags) if task.tags else '(none)'}",
        f"Due Date: {task.due_date.strftime('%Y-%m-%d') if task.due_date else '(none)'}",
        f"Recurrence: {task.recurrence_rule.value}",
    ]

    # Add overdue indicator
    if task.is_overdue():
        lines.append("WARNING: OVERDUE")

    return "\n".join(lines)


def format_task_list(tasks: list[Task]) -> str:
    """
    Format multiple tasks as a numbered list.

    Args:
        tasks: List of tasks to format

    Returns:
        Multi-line string with all tasks in brief format

    Example:
        1. [X] [HIGH] Buy groceries
        2. [ ] [MEDIUM] Write documentation
        3. [ ] [LOW] Review code
    """
    if not tasks:
        return "(No tasks to display)"

    return "\n".join(format_task_brief(task) for task in tasks)


def format_priority_indicator(priority: Priority) -> str:
    """
    Format priority with visual indicator.

    Args:
        priority: Priority level

    Returns:
        Formatted string with priority name

    Example:
        "HIGH"
        "MEDIUM"
        "LOW"
    """
    return priority.value


def format_priority_label(priority: Priority) -> str:
    """
    Format priority as a compact label (alias for format_priority_indicator).

    Args:
        priority: Priority level

    Returns:
        Formatted string: "(HIGH)", "(MED)", or "(LOW)"

    Example:
        format_priority_label(Priority.HIGH) -> "(HIGH)"
        format_priority_label(Priority.MEDIUM) -> "(MED)"
        format_priority_label(Priority.LOW) -> "(LOW)"
    """
    priority_map = {
        Priority.HIGH: "(HIGH)",
        Priority.MEDIUM: "(MED)",
        Priority.LOW: "(LOW)"
    }
    return priority_map.get(priority, "(MED)")


def format_tags(tags: list[str]) -> str:
    """
    Format task tags for display.

    Args:
        tags: List of tag strings

    Returns:
        Formatted string with hashtag prefix for each tag, or empty string if no tags

    Example:
        format_tags(["work", "urgent"]) -> "#work #urgent"
        format_tags([]) -> ""
    """
    if not tags:
        return ""
    return " ".join(f"#{tag}" for tag in tags)


def format_due_date(task: Task) -> str:
    """
    Format task due date for display.

    Args:
        task: Task object

    Returns:
        Formatted string showing due date and overdue status

    Example:
        format_due_date(task) -> "Due: 2026-01-25"
        format_due_date(overdue_task) -> "WARNING: OVERDUE | Due: 2026-01-20"
        format_due_date(no_date_task) -> ""
    """
    if not task.due_date:
        return ""

    date_str = f"Due: {task.due_date.strftime('%Y-%m-%d')}"

    if task.is_overdue():
        return f"WARNING: OVERDUE | {date_str}"
    else:
        return date_str


def format_recurrence(task: Task) -> str:
    """
    Format task recurrence rule for display.

    Args:
        task: Task object

    Returns:
        Formatted string showing recurrence pattern

    Example:
        format_recurrence(daily_task) -> "(Daily)"
        format_recurrence(weekly_task) -> "(Weekly)"
        format_recurrence(no_recurrence_task) -> ""
    """
    from src.models.task import RecurrenceRule

    if task.recurrence_rule == RecurrenceRule.NONE:
        return ""
    elif task.recurrence_rule == RecurrenceRule.DAILY:
        return "(Daily)"
    elif task.recurrence_rule == RecurrenceRule.WEEKLY:
        return "(Weekly)"
    elif task.recurrence_rule == RecurrenceRule.MONTHLY:
        return "(Monthly)"
    else:
        return ""


def clear_screen() -> None:
    """
    Clear the terminal screen.

    Uses platform-independent method (print blank lines).
    """
    print("\n" * 50)


def print_separator() -> None:
    """Print a visual separator line."""
    print("=" * 60)


def print_header(title: str) -> None:
    """
    Print a formatted section header.

    Args:
        title: Header text to display

    Example:
        === Todo Application ===
    """
    print_separator()
    print(f" {title} ")
    print_separator()


def print_error(message: str) -> None:
    """
    Print an error message.

    Args:
        message: Error message to display

    Example:
        Error: Invalid task ID
    """
    print(f"\nError: {message}\n")


def print_success(message: str) -> None:
    """
    Print a success message.

    Args:
        message: Success message to display

    Example:
        Success: Task created successfully
    """
    print(f"\nSuccess: {message}\n")


def print_info(message: str) -> None:
    """
    Print an informational message.

    Args:
        message: Info message to display

    Example:
        Info: No tasks found
    """
    print(f"\nInfo: {message}\n")
