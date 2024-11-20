#!/usr/bin/env python3
"""
The class will handle operations for basic authetication
"""
from api.v1.auth.auth import Auth
import base64

class BasicAuth(Auth):
    """Basic authentication class."""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract Base64 part from the Authorization header."""
        if not authorization_header or not isinstance(authorization_header, str) :
            return None
        
        if not authorization_header.startswith('Basic'):
            return None
        
        return authorization_header.split(' ', 1)[1]
        
