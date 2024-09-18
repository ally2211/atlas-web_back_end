#!/usr/bin/env python3
'''
encrypt a password
'''
import bcrypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    check is a valid password
    '''
    # Convert the provided password to bytes
    password_bytes = password.encode('utf-8')
    # Use bcrypt's checkpw method to validate the password
    return bcrypt.checkpw(password_bytes, hashed_password)


def hash_password(password: str) -> bytes:
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
