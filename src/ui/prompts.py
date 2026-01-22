"""
Input prompt utilities for Phase I Todo CLI.
"""


def prompt_string(message: str, required: bool = False, default: str = "") -> str:
    """
    Prompt user for string input.

    Args:
        message: Prompt message to display
        required: If True, re-prompt until non-empty input received
        default: Default value if user presses Enter (displayed in prompt)

    Returns:
        User input string (stripped)

    Example:
        >>> prompt_string("Enter title: ", required=True)
        Enter title: Buy groceries
        'Buy groceries'
    """
    if default:
        full_message = f"{message} [{default}]: "
    else:
        full_message = f"{message}: "

    while True:
        value = input(full_message).strip()
        if not value and default:
            return default
        if required and not value:
            print("  This field is required. Please enter a value.")
            continue
        return value


def prompt_int(message: str, min_value: int | None = None, max_value: int | None = None) -> int | None:
    """
    Prompt user for integer input.

    Args:
        message: Prompt message to display
        min_value: Minimum allowed value (inclusive)
        max_value: Maximum allowed value (inclusive)

    Returns:
        Integer value, or None if input is empty or invalid

    Example:
        >>> prompt_int("Enter task ID: ", min_value=1)
        Enter task ID: 5
        5
    """
    value = input(f"{message}: ").strip()
    if not value:
        return None

    try:
        int_value = int(value)
        if min_value is not None and int_value < min_value:
            print(f"  Value must be at least {min_value}")
            return None
        if max_value is not None and int_value > max_value:
            print(f"  Value must be at most {max_value}")
            return None
        return int_value
    except ValueError:
        print("  Invalid number format")
        return None


def prompt_yes_no(message: str, default: bool | None = None) -> bool:
    """
    Prompt user for yes/no confirmation.

    Args:
        message: Prompt message to display
        default: Default value if user presses Enter (True for yes, False for no, None for no default)

    Returns:
        True for yes, False for no

    Example:
        >>> prompt_yes_no("Delete task?", default=False)
        Delete task? [y/N]: y
        True
    """
    if default is True:
        suffix = " [Y/n]: "
    elif default is False:
        suffix = " [y/N]: "
    else:
        suffix = " [y/n]: "

    while True:
        response = input(message + suffix).strip().lower()
        if not response and default is not None:
            return default
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("  Please enter 'y' for yes or 'n' for no")


def prompt_choice(message: str, choices: list[str], default: str | None = None) -> str | None:
    """
    Prompt user to select from a list of choices.

    Args:
        message: Prompt message to display
        choices: List of valid choices (case-insensitive)
        default: Default choice if user presses Enter

    Returns:
        Selected choice (in original case from choices list), or None if empty and no default

    Example:
        >>> prompt_choice("Select priority: ", ["HIGH", "MEDIUM", "LOW"], default="MEDIUM")
        Select priority (HIGH, MEDIUM, LOW) [MEDIUM]: high
        'HIGH'
    """
    choices_str = ", ".join(choices)
    if default:
        full_message = f"{message} ({choices_str}) [{default}]: "
    else:
        full_message = f"{message} ({choices_str}): "

    while True:
        value = input(full_message).strip()
        if not value:
            return default if default else None

        # Case-insensitive match
        value_lower = value.lower()
        for choice in choices:
            if choice.lower() == value_lower:
                return choice

        print(f"  Invalid choice. Please select from: {choices_str}")


def prompt_multiline(message: str) -> str:
    """
    Prompt user for multi-line input.

    Args:
        message: Prompt message to display

    Returns:
        User input (may contain newlines from \\n escape sequences)

    Note:
        Users should type literal \\n for line breaks (e.g., "Line 1\\nLine 2")
        This is processed and converted to actual newlines.

    Example:
        >>> prompt_multiline("Enter description")
        Enter description: First line\\nSecond line
        'First line\nSecond line'
    """
    value = input(f"{message} (use \\n for line breaks): ").strip()
    # Replace literal \n with actual newlines
    return value.replace("\\n", "\n")


def press_enter_to_continue() -> None:
    """
    Wait for user to press Enter before continuing.

    Example:
        Press Enter to continue...
    """
    input("\nPress Enter to continue...")
