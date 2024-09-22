#!/usr/bin/env python3
"""
Basic Authentication methods for users
"""
from api.v1.auth.auth import Auth


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
