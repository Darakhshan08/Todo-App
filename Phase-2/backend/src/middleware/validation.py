"""
Input validation middleware
"""
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
import re


class InputValidationMiddleware(BaseHTTPMiddleware):
    """
    Validate input for common security issues.
    Per spec.md L201: Input validation on all endpoints
    """

    # Patterns for suspicious input
    SQL_INJECTION_PATTERN = re.compile(r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER)\b)", re.IGNORECASE)
    XSS_PATTERN = re.compile(r"<script.*?>.*?</script>", re.IGNORECASE | re.DOTALL)

    async def dispatch(self, request: Request, call_next):
        # Validate query parameters
        if request.query_params:
            for key, value in request.query_params.items():
                if self.is_suspicious(value):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Suspicious input detected in query parameter: {key}",
                    )

        # Validate path parameters
        if request.path_params:
            for key, value in request.path_params.items():
                if isinstance(value, str) and self.is_suspicious(value):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Suspicious input detected in path parameter: {key}",
                    )

        response = await call_next(request)
        return response

    def is_suspicious(self, value: str) -> bool:
        """Check if input contains suspicious patterns"""
        if self.SQL_INJECTION_PATTERN.search(value):
            return True
        if self.XSS_PATTERN.search(value):
            return True
        return False
