#!/usr/bin/env python3
"""
Basic Authentication methods for users
"""
import base64
from typing_extensions import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    Implements basic authentication logic.
    """
    def current_user(self, request=None):
        """
        Override the current_user method to implement basic authentication.
        """
        print("BasicAuth: Checking current user...")
        return super().current_user(request)

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header
        """
        # Return None if authorization_header is not a string
        if not isinstance(authorization_header, str):
            return None

        # Check if the header starts with "Basic " (case-sensitive)
        if not authorization_header.startswith("Basic "):
            return None

        # Extract the part after "Basic " and return it
        base64_credentials = authorization_header[len("Basic "):]

        # Ensure the Base64 credentials exist
        if not base64_credentials:
            return None

        return base64_credentials

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """
        Decode the Base64-encoded part
        """
        # Return None if base64_authorization_header is not a string
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convert bytes to string
            decoded_str = decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            # Return None if decoding fails
            return None

        return decoded_str

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> TypeVar('User'):
        """
        Extract the username and password
        from the decoded Base64 string.
        """
        # Return None if the input is not a string
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if the decoded string contains a colon
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string by the first colon only
        username, password = decoded_base64_authorization_header.split(':', 1)

        # Return None for missing username or password
        if not username or not password:
            return None, None

        return username, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Validate the user credentials
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        if not user_email or not user_pwd:
            return None

        # Simulating database check or user store
        user = self.find_user_by_email(user_email)

        if user is None:
            return None

        # Check provided password matches stored password
        if not user.is_valid_password(user_pwd):
            return None

        # Return the User object if the credentials are valid
        return user

    def find_user_by_email(self, email: str) -> User:
        """
        find user email
        """
        # fetching the user from in-memory store
        # Assuming users is a dictionary {email: User}
        users = {
            "user@example.com": User("user@example.com", "password123")
        }

        return users.get(email, None)

    def check_password(self, user: User, password: str) -> bool:
        """
        Simulate password checking.
        """
        # password is stored in plain text
        return user.password == password
