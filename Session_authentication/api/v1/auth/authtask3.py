#!/usr/bin/env python3
""" 
Authentication methods for users
"""
from flask import Request
from typing import List, TypeVar
# from api.v1.auth.auth import Auth
from models.user import User

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
        if request is None or 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """
        Return None by default, indicating no user is identified.
        This method would typically extract user information from the request
        and return a User instance.
        """
        return None
