#!/usr/bin/env python3
"""
Class Cache store and get
"""
import redis
import uuid
from typing import Any, Callable, Optional


class Cache:
    def __init__(self):
        # Initialize the Redis client and assign it to the private variable
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        
        # Flush the Redis database to clear any existing data
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        Store the input data in Redis with a random key.
        """
        # Generate a random UUID key
        key = str(uuid.uuid4())
        # Store the data in Redis using the random key
        self._redis.set(key, data)
        # Return the generated key
        return key
    
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
