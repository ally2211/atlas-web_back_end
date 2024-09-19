#!/usr/bin/env python3
""" Authentication
"""
from flask import Request
from typing import List, TypeVar
# from api.v1.auth.auth import Auth
from models.user import User

# Define a generic type for User
User = TypeVar('User')


class Auth:
    '''
    class Auth authenticates users
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Return False if path is None
        or in excluded_paths, otherwise True.
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
        Return the Authorization header
        from the Flask request object,
        or None if missing.
        """
        if request is None or 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """Return None by default, indicating no user
        is identified.
        """
        return None
