#!/usr/bin/env python3
"""
Basic Authentication methods for users
"""
import base64
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
                                     str) -> (str, str):
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
