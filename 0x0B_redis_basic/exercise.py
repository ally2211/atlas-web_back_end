#!/usr/bin/env python3
"""
Class Cache store and get
"""
from functools import wraps
import redis
import uuid
from typing import Union, Any, Callable, Optional

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Generate the Redis key using the method's qualified name
        key = method.__qualname__
        # Increment the count for this method in Redis
        self._redis.incr(key)
        # Call the original method and get its return value
        result = method(self, *args, **kwargs)
        # Return the result of the original method
        return result
    return wrapper

class Cache:
    def __init__(self):
        # Initialize the Redis client and assign it to the private variable
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        # Flush the Redis database to clear any existing data
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key.
        """
        # Generate a random UUID key
        key = str(uuid.uuid4())
        # Store the data in Redis using the random key
        self._redis.set(key, data)
        # Return the generated key
        return key
    
    @count_calls
    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieve data from Redis
        and optionally apply a transformation function.
        """
        # Retrieve data from Redis
        data = self._redis.get(key)
        # If the data is None, return None
        if data is None:
            return None
        # If a transformation function is provided, apply it to the data
        if fn is not None:
            return fn(data)
        # Return the raw byte string if no transformation function is provided
        return data
