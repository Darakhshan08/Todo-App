"""
Date utility functions for Phase I Todo CLI.
Uses standard library only - no external dependencies.
"""
from datetime import date, timedelta


def add_days(start_date: date, days: int) -> date:
    """
    Add days to a date.

    Args:
        start_date: Starting date
        days: Number of days to add

    Returns:
        New date with days added
    """
    return start_date + timedelta(days=days)


def add_weeks(start_date: date, weeks: int) -> date:
    """
    Add weeks to a date.

    Args:
        start_date: Starting date
        weeks: Number of weeks to add

    Returns:
        New date with weeks added
    """
    return start_date + timedelta(weeks=weeks)


def add_months(start_date: date, months: int) -> date:
    """
    Add months to a date using standard library.

    Handles month-end edge cases:
    - Jan 31 + 1 month = Feb 28 (or 29 in leap year)
    - Oct 31 + 1 month = Nov 30

    Args:
        start_date: Starting date
        months: Number of months to add

    Returns:
        New date with months added
    """
    # Calculate target month and year
    month = start_date.month - 1 + months  # Convert to 0-indexed
    year = start_date.year + month // 12
    month = month % 12 + 1  # Convert back to 1-indexed

    # Handle day overflow (e.g., Jan 31 -> Feb 28)
    day = start_date.day
    # Get last day of target month
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    last_day_of_month = (next_month - timedelta(days=1)).day

    # Use the minimum of original day and last day of target month
    day = min(day, last_day_of_month)

    return date(year, month, day)


def format_date(date_obj: date) -> str:
    """
    Format date as YYYY-MM-DD string.

    Args:
        date_obj: Date to format

    Returns:
        Date string in YYYY-MM-DD format
    """
    return date_obj.strftime("%Y-%m-%d")


def parse_date(date_str: str) -> date | None:
    """
    Parse date from YYYY-MM-DD string.

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        Parsed date object, or None if invalid format
    """
    from datetime import datetime
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def calculate_next_occurrence(current_due_date: date, recurrence_rule) -> date:
    """
    Calculate the next occurrence date for a recurring task.

    Args:
        current_due_date: Current due date
        recurrence_rule: Recurrence pattern (DAILY, WEEKLY, MONTHLY)

    Returns:
        Next due date based on recurrence rule
    """
    from src.models.task import RecurrenceRule

    if recurrence_rule == RecurrenceRule.DAILY:
        return add_days(current_due_date, 1)
    elif recurrence_rule == RecurrenceRule.WEEKLY:
        return add_weeks(current_due_date, 1)
    elif recurrence_rule == RecurrenceRule.MONTHLY:
        return add_months(current_due_date, 1)
    else:
        # Default to no change for NONE or unknown
        return current_due_date
