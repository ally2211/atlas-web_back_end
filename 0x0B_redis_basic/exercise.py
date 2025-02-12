#!/usr/bin/env python3
"""
Class Cache store and get
"""
import redis
import functools
from typing import Callable, Optional


# function to display the history of calls of a particular function.
def replay(method: Callable) -> None:
    """
    Display the history of inputs and outputs for a particular function.
    """
    # Access the Redis client from the class instance
    redis_client = method.__self__._redis

    # Generate keys for storing input and output history
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    # Retrieve the stored inputs and outputs from Redis
    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)

    # Decode the byte strings into regular strings for display
    inputs = [input_data.decode('utf-8') for input_data in inputs]
    outputs = [output_data.decode('utf-8') for output_data in outputs]

    # Display the history of calls
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for i, (input_args, output) in enumerate(zip(inputs, outputs)):
        print(f"{method.__qualname__}(*{input_args}) -> {output}")


# Decorator to count how many times a method is called
def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @functools.wraps(method)  # Preserve function metadata
    def wrapper(self, *args, **kwargs):
        # Use the method's qualified name as the key
        key = method.__qualname__
        # Increment the count in Redis
        self._redis.incr(key)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper


# Decorator to store function call history
def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    """
    @functools.wraps(method)  # Preserve function metadata
    def wrapper(self, *args, **kwargs):
        # Create input key
        input_key = f"{method.__qualname__}:inputs"
        # Create output key
        output_key = f"{method.__qualname__}:outputs"

        # Store function input in Redis
        self._redis.rpush(input_key, str(args))
        # Call the original function
        output = method(self, *args, **kwargs)
        # Store function output in Redis
        self._redis.rpush(output_key, str(output))

        # Return the function's output
        return output
    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize the Redis connection.
        """
        self._redis = redis.Redis()

    @count_calls  # Apply the decorator to count method calls
    @call_history  # Apply the decorator to track call history
    def store(self, data: str) -> str:
        """
        Store data in Redis and return the key.
        """
        # Generate a unique key using the hash of the data
        key = str(hash(data))
        # Store the data in Redis with the generated key
        self._redis.set(key, data)
        # Return the key
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Retrieve data from Redis by key
        and apply an optional conversion function.
        """
        # Retrieve the data from Redis
        data = self._redis.get(key)
        if data is None:
            # Return None if the key does not exist
            return None
        # Apply conversion function if provided
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and decode it as a string.
        """
        # Decode the data from bytes to string
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.
        """
        # Convert the data from bytes to integer
        return self.get(key, lambda d: int(d))
