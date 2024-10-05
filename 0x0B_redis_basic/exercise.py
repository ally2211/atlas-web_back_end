#!/usr/bin/env python3
"""
Class Cache store and get
"""
from functools import wraps
import redis
import uuid
from typing import Union, Any, Callable, Optional, TypeVar
import json
T = TypeVar('T')


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


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method in Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Generate keys for storing input and output history
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Store the input arguments as a JSON string
        self._redis.rpush(input_key, str(args))
        # Call the original method and store the output
        result = method(self, *args)
        # Store the output result as a JSON string
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


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
        '''
        Initialize the Redis client and assign it to the private variable
        '''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        # Flush the Redis database to clear any existing data
        self._redis.flushdb()

    @call_history
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

    @call_history
    def get(self, key: str, fn: Callable[[bytes], T] = None
            ) -> Union[bytes, T, None]:
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

    @call_history
    def get_str(self, key: str) -> str:
        '''
        retrieve data from Redis and convert to string
        '''
        return self.get(key, lambda data: data.decode('utf-8'))

    @call_history
    def get_int(self, key: str) -> int:
        '''
        retrieve data from Redis and convert to int
        '''
        return self.get(key, lambda data: int(data))


# Example usage in terminal
if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
