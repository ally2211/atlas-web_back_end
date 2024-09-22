#!/usr/bin/env python3
"""
Authentication methods for users
"""
from flask import Request
from typing import List, TypeVar
# from api.v1.auth.auth import Auth
from models.user import User
import sys

# Define a generic type for User
User = TypeVar('User')


class Auth:
    '''
    Method that returns the current user based on the request object
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the requested path requires authentication.
        Returns False if the path is None or in excluded_paths.
        Returns True otherwise.
        """
        print(f"Checking if authentication is required for path: {path}")

        if path is None or excluded_paths is None:
            return True  # return True (require auth)

        # Normalize paths by stripping trailing slashes
        # to handle matching better
        normalized_path = path.rstrip('/')
        normalized_excluded_paths = [p.rstrip('/') for p in excluded_paths]

        # Return False if the path is in the excluded_paths
        if normalized_path in normalized_excluded_paths:
            return False
       
        return True  # Otherwise, return True (require auth)

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request object.
        Returns None if the header is not present.
        """
        print("Checking Authorization header...")
        if request is None or 'Authorization' not in request.headers:
            return None

        auth_header = request.headers.get('Authorization')
        print(f"Authorization Header found: {auth_header}")  # Debugging
        
        if auth_header is None or not auth_header.startswith('Basic '):
            return None

        return auth_header

    def current_user(self, request=None) -> User:
        """
        Return None by default, indicating no user is identified.
        This method would typically extract user information from the request
        and return a User instance.
        """
        print("Checking current user...")
        auth_header = self.authorization_header(request)
        print(f"Authorization Header: {auth_header}")  # Debugging
        if auth_header is None:
            return None

        # Extract Base64 part from the Authorization header
        base64_credentials = self.extract_base64_authorization_header(auth_header)
        print(f"Decoded Credentials: {decoded_credentials}")  # Debugging
        if base64_credentials is None:
            return None

        # Decode Base64 to get "email:password"
        decoded_credentials = self.decode_base64_authorization_header(base64_credentials)
        if decoded_credentials is None:
            return None

        # Extract email and password from the decoded string
        user_email, user_pwd = self.extract_user_credentials(decoded_credentials)
        print(f"User Email: {user_email}, Password: {user_pwd}")
        if user_email is None or user_pwd is None:
            return None

        # Find the user by email and verify password
        user = self.user_object_from_credentials(user_email, user_pwd)
        print(f"User: {user}")  # Debugging
        return user
