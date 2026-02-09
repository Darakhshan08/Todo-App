"""
Constitution compliance checker utilities
Ensures adherence to project constitution principles
"""
from typing import List, Dict


class ConstitutionChecker:
    """
    Verify implementation follows project constitution.
    Based on .specify/memory/constitution.md
    """

    @staticmethod
    def check_user_isolation(user_id: str, resource_owner: str) -> bool:
        """
        Verify user can only access their own data.
        Constitution Principle: User data isolation
        """
        return user_id == resource_owner

    @staticmethod
    def check_jwt_authentication(headers: Dict[str, str]) -> bool:
        """
        Verify JWT token present in headers.
        Constitution Principle: JWT-based authentication
        """
        return "Authorization" in headers and headers["Authorization"].startswith("Bearer ")

    @staticmethod
    def validate_input_constraints(data: Dict, constraints: Dict) -> List[str]:
        """
        Validate input against constitution constraints.
        Constitution Principle: Input validation

        Args:
            data: Input data to validate
            constraints: Validation constraints

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        for field, constraint in constraints.items():
            if field not in data:
                if constraint.get("required"):
                    errors.append(f"{field} is required")
                continue

            value = data[field]

            # Length validation
            if "max_length" in constraint and len(str(value)) > constraint["max_length"]:
                errors.append(f"{field} exceeds maximum length of {constraint['max_length']}")

            if "min_length" in constraint and len(str(value)) < constraint["min_length"]:
                errors.append(f"{field} below minimum length of {constraint['min_length']}")

        return errors
