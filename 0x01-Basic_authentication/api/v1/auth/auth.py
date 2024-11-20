#!/usr/bin/env python3

"""
This module provides an abstract Auth class that defines the core functionalities for authentication and authorization 
"""

from flask import request
from typing import List, TypeVar

class Auth:
    """
    An abstract class providing authentication and authorization functionalities.

    Subclasses of `Auth` should implement the abstract methods to provide specific
    authentication mechanisms like basic auth, token-based auth, or OAuth.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether authentication is required for a given path.

        Args:
            path: The current request path.
            excluded_paths: A list of paths that do not require authentication.

        Returns:
            True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request: The current Flask request object (optional).

        Returns:
            The authorization header value, or None if not found.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the currently authenticated user.

        Args:
            request: The current Flask request object (optional).

        Returns:
            The current user object, or None if no user is authenticated.
        """
        return None
