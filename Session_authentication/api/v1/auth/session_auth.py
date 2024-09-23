#!/usr/bin/env python3
import uuid
from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    # Inherit from Auth, without overloading any methods for now
    '''
    instance of method createsession
    '''
    def __init__(self):
        """
        Initialize the dictionary to store user_id by session_id.
        """
        self.user_id_by_session_id = {}  # Dictionary to store session IDs

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a given user_id.
        Returns None if user_id is None or not a string.
        Stores the session ID as a key and user_id as the value in user_id_by_session_id.
        """
        # Return None if user_id is None or not a string
        if user_id is None or not isinstance(user_id, str):
            return None
        
        # Generate a unique session ID
        session_id = str(uuid.uuid4())
        
        # Store the session ID as a key and user_id as the value
        self.user_id_by_session_id[session_id] = user_id
        
        return session_id

    
