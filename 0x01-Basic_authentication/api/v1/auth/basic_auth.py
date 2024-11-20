#!/usr/bin/env python3
"""
The class will handle operations for basic authetication
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple , TypeVar
from models.user import User


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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user email and password from the decoded Base64 header.
        """
        if not decoded_base64_authorization_header or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
    
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Retrieves a User instance based on email and password.
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user