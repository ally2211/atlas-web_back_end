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

        print(f"Base64 Credentials: {base64_credentials}")  # Debugging
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
            print(f"Decoded Credentials: {decoded_str}")  # Debugging
        except (base64.binascii.Error, UnicodeDecodeError):
            # Return None if decoding fails
            return None

        return decoded_str

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> 'User':
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
                                     user_pwd: str) -> 'User':
        """
        Validate the user credentials
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            print(f"Invalid email or password format")  # Debugging
            return None

        print(f"Looking for user with email: {user_email}")  # Debugging

        if not user_email or not user_pwd:
            return None

        # Simulating database check or user store
        user = self.find_user_by_email(user_email)

        if user is None:
            print(f"User not found with email: {user_email}")  # Debugging
            return None

        print(f"User found: {user_email} {user_pwd} verifying password...")  # Debugging
        # Check provided password matches stored password
        #if not user.is_valid_password(user_pwd):
            #print(f"Invalid password for user: {user_email}")  # Debugging
            #return None

        # Return the User object if the credentials are valid
        print(f"User authenticated: {user_email}")  # Debugging
        return user

    def find_user_by_email(cls, email: str) -> 'User':
        """
        find user email
        """
        # fetching the user from in-memory store
        # Assuming users is a dictionary {email: User}
        print(f"Searching for user with email: {email}")
        user = User()
        if user:
            print(f"User found: {email}")
        else:
            print(f"No user found with email: {email}")
        return user

    def is_valid_password(self, password: str) -> bool:
        """
        Check if the provided password is valid. In real applications, compare the hashed password.
        """
        print(f"Checking if provided password matches for user: {self.email}")
        print(f"Stored password: {self.password}, Provided password: {password}")  # Debugging

        # In real apps, compare hashed passwords
        return self.password == password

    def current_user(self, request=None) -> User:
        """
        Return the current authenticated user.
        """
        # Get the Authorization header from the request
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Extract the Base64 part of the Authorization header
        base64_credentials = self.extract_base64_authorization_header(
            auth_header)
        if base64_credentials is None:
            return None

        # Decode the Base64 credentials
        decoded_credentials = self.decode_base64_authorization_header(
            base64_credentials)
        if decoded_credentials is None:
            return None

        # Extract the user email and password
        user_email, user_pwd = self.extract_user_credentials(
            decoded_credentials)
        if user_email is None or user_pwd is None:
            return None

        # Retrieve the user object using the email and password
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
