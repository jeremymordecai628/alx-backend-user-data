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

        # Check if any of the input parameters are None or if the excluded_paths list is empty
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize the path by removing any trailing slashes
        path = path.rstrip("/")

        # Iterate through the excluded paths and check for a match
        for exclude_path in excluded_paths:
            if path == exclude_path.rstrip("/"):
                return False

        # If no match is found, authentication is required
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request: The current Flask request object (optional).

        Returns:
            The authorization header value, or None if not found.
        """

        """Retrieve the Authorization header."""
        if request is None or 'Authorization' not in request.headers:
            return None
        
        return request.headers['Authorization']


    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the currently authenticated user.

        Args:
            request: The current Flask request object (optional).

        Returns:
            The current user object, or None if no user is authenticated.
        """
        return None
