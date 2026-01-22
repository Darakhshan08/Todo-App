"""
Input validation service for Phase I Todo CLI.
"""
from datetime import date, datetime
from src.models.task import Priority, RecurrenceRule


class ValidationService:
    """
    Validates user input for task operations.

    Provides methods to validate all task fields according to specification requirements.
    """

    @staticmethod
    def validate_title(title: str) -> tuple[bool, str]:
        """
        Validate task title.

        Args:
            title: Title string to validate

        Returns:
            Tuple of (is_valid, error_message)
            - (True, "") if valid
            - (False, "error message") if invalid

        Rules:
            - Required (non-empty after trimming)
            - 1-200 characters after trimming
        """
        title = title.strip()
        if not title:
            return False, "Title is required and cannot be empty"
        if len(title) > 200:
            return False, "Title must be 200 characters or less"
        return True, ""

    @staticmethod
    def validate_description(description: str) -> tuple[bool, str]:
        """
        Validate task description.

        Args:
            description: Description string to validate

        Returns:
            Tuple of (is_valid, error_message)
            - (True, "") if valid
            - (False, "error message") if invalid

        Rules:
            - Optional (empty allowed)
            - 0-1000 characters after trimming
        """
        description = description.strip()
        if len(description) > 1000:
            return False, "Description must be 1000 characters or less"
        return True, ""

    @staticmethod
    def validate_priority(priority_str: str) -> tuple[bool, str, Priority | None]:
        """
        Validate and parse priority value.

        Args:
            priority_str: Priority string to validate (case-insensitive)

        Returns:
            Tuple of (is_valid, error_message, priority_enum)
            - (True, "", Priority.X) if valid
            - (False, "error message", None) if invalid

        Rules:
            - Must be one of: HIGH, MEDIUM, LOW (case-insensitive)
        """
        priority_str = priority_str.strip().upper()
        try:
            priority = Priority[priority_str]
            return True, "", priority
        except KeyError:
            valid_values = ", ".join([p.value for p in Priority])
            return False, f"Priority must be one of: {valid_values}", None

    @staticmethod
    def validate_tags(tags_str: str) -> tuple[bool, str, list[str]]:
        """
        Validate and normalize tags.

        Args:
            tags_str: Comma-separated tags string

        Returns:
            Tuple of (is_valid, error_message, normalized_tags)
            - (True, "", [tags]) if valid (tags normalized to lowercase, trimmed, deduplicated)
            - (False, "error message", []) if invalid

        Rules:
            - Comma-separated list
            - Each tag trimmed and normalized to lowercase
            - Duplicates removed
            - Empty tags ignored
        """
        if not tags_str.strip():
            return True, "", []

        tags = [tag.strip().lower() for tag in tags_str.split(",")]
        # Remove empty tags and duplicates while preserving order
        seen = set()
        normalized_tags = []
        for tag in tags:
            if tag and tag not in seen:
                seen.add(tag)
                normalized_tags.append(tag)

        return True, "", normalized_tags

    @staticmethod
    def validate_date(date_str: str) -> tuple[bool, str, date | None]:
        """
        Validate and parse date value.

        Args:
            date_str: Date string in YYYY-MM-DD format

        Returns:
            Tuple of (is_valid, error_message, date_object)
            - (True, "", date) if valid
            - (False, "error message", None) if invalid

        Rules:
            - Must be in YYYY-MM-DD format
            - Must be a valid calendar date
        """
        date_str = date_str.strip()
        if not date_str:
            return False, "Date cannot be empty"

        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return True, "", parsed_date
        except ValueError:
            return False, "Date must be in YYYY-MM-DD format (e.g., 2025-12-31)"

    @staticmethod
    def validate_recurrence(recurrence_str: str) -> tuple[bool, str, RecurrenceRule | None]:
        """
        Validate and parse recurrence rule value.

        Args:
            recurrence_str: Recurrence string to validate (case-insensitive)

        Returns:
            Tuple of (is_valid, error_message, recurrence_enum)
            - (True, "", RecurrenceRule.X) if valid
            - (False, "error message", None) if invalid

        Rules:
            - Must be one of: NONE, DAILY, WEEKLY, MONTHLY (case-insensitive)
        """
        recurrence_str = recurrence_str.strip().upper()
        try:
            recurrence = RecurrenceRule[recurrence_str]
            return True, "", recurrence
        except KeyError:
            valid_values = ", ".join([r.value for r in RecurrenceRule])
            return False, f"Recurrence must be one of: {valid_values}", None
