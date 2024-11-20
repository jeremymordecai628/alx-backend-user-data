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
    

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 authorization header.
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        
        try :
            decoded = base64.b64decode(base64_authorization_header).decode('utf-8')
            return decoded
        except Exception:
            return None
