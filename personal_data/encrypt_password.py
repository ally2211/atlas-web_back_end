#!/usr/bin/env python3
'''
encrypt a password
'''
import bcrypt


def hash_password (password: str) -> bytes:
    '''
    get a password as a string and return a salted hashed password
    which is a byte string
    '''
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Generate a salt
    salt = bcrypt.gensalt()
    
    # Hash the password using bcrypt.hashpw
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # Return the salted, hashed password (as a byte string)
    return hashed_password
