#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required."""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieve Authorization header."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve current user."""
        return None
