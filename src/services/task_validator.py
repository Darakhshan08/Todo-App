"""
Input validation functions for the Todo application.
Validates task titles, descriptions, and IDs according to specification constraints.
"""

import re
from typing import Tuple


def validate_title(title: str) -> Tuple[bool, str]:
    """
    Validate a task title according to specification rules.

    Rules:
    - Must not be empty after trimming whitespace
    - Must not exceed 200 characters after trimming

    Args:
        title: The title string to validate

    Returns:
        Tuple of (is_valid: bool, error_message: str)
        If valid, error_message is empty string

    Examples:
        >>> validate_title("Buy groceries")
        (True, '')
        >>> validate_title("   ")
        (False, 'Error: Task title cannot be empty. Please provide a title.')
        >>> validate_title("a" * 201)
        (False, 'Error: Title exceeds maximum length of 200 characters. Please shorten your title.')
    """
    trimmed = title.strip()

    if not trimmed:
        return False, "Error: Task title cannot be empty. Please provide a title."

    if len(trimmed) > 200:
        return False, "Error: Title exceeds maximum length of 200 characters. Please shorten your title."

    return True, ""


def validate_description(description: str) -> Tuple[bool, str]:
    """
    Validate a task description according to specification rules.

    Rules:
    - Can be empty (optional field)
    - Must not exceed 1000 characters after trimming

    Args:
        description: The description string to validate

    Returns:
        Tuple of (is_valid: bool, error_message: str)
        If valid, error_message is empty string

    Examples:
        >>> validate_description("Buy milk and eggs")
        (True, '')
        >>> validate_description("")
        (True, '')
        >>> validate_description("a" * 1001)
        (False, 'Error: Description exceeds maximum length of 1000 characters. Please shorten your description.')
    """
    trimmed = description.strip()

    if len(trimmed) > 1000:
        return False, "Error: Description exceeds maximum length of 1000 characters. Please shorten your description."

    return True, ""


def validate_task_id(task_id: str) -> Tuple[bool, str]:
    """
    Validate a task ID format according to specification rules.

    Rules:
    - Must match format "task-NNN" where NNN is 3 digits (e.g., task-001, task-042)

    Args:
        task_id: The task ID string to validate

    Returns:
        Tuple of (is_valid: bool, error_message: str)
        If valid, error_message is empty string

    Examples:
        >>> validate_task_id("task-001")
        (True, '')
        >>> validate_task_id("5")
        (False, "Error: Invalid task ID format. Please use format 'task-NNN' (e.g., task-001).")
        >>> validate_task_id("task-42")
        (False, "Error: Invalid task ID format. Please use format 'task-NNN' (e.g., task-001).")
    """
    pattern = r"^task-\d{3}$"

    if not re.match(pattern, task_id):
        return False, "Error: Invalid task ID format. Please use format 'task-NNN' (e.g., task-001)."

    return True, ""


def parse_multiline_input(user_input: str) -> str:
    """
    Parse user input containing literal \\n escape sequences into actual newlines.

    According to the refined spec (006-refine-cli-specs), users enter literal
    backslash-n sequences in console input to represent line breaks.

    Args:
        user_input: Raw user input string that may contain \\n sequences

    Returns:
        Processed string with \\n converted to actual newline characters

    Examples:
        >>> parse_multiline_input("Step 1\\nStep 2\\nStep 3")
        'Step 1\\nStep 2\\nStep 3'
        >>> parse_multiline_input("Single line")
        'Single line'
    """
    # Replace literal \n escape sequences with actual newlines
    return user_input.replace("\\n", "\n")


def trim_input(text: str) -> str:
    """
    Trim leading and trailing whitespace from input text.

    Args:
        text: Input text to trim

    Returns:
        Trimmed text

    Examples:
        >>> trim_input("  hello world  ")
        'hello world'
        >>> trim_input("no spaces")
        'no spaces'
    """
    return text.strip()
