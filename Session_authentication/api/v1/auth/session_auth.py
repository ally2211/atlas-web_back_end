#!/usr/bin/env python3
from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    # Inherit from Auth, without overloading any methods for now
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        '''
        instance of method createsession
        '''
        pass
        
