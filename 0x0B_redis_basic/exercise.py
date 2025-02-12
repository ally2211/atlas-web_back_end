import redis
import functools
from typing import Callable, Optional

# Decorator to count how many times a method is called
def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @functools.wraps(method)  # Preserve function metadata
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__  # Use the method's qualified name as the key
        self._redis.incr(key)  # Increment the count in Redis
        return method(self, *args, **kwargs)  # Call the original method
    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize the Redis connection.
        """
        self._redis = redis.Redis()

    @count_calls  # Apply the decorator to count method calls
    def store(self, data: str) -> str:
        """
        Store data in Redis and return the key.
        """
        key = str(hash(data))  # Generate a unique key using the hash of the data
        self._redis.set(key, data)  # Store the data in Redis with the generated key
        return key  # Return the key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Retrieve data from Redis by key and apply an optional conversion function.
        """
        data = self._redis.get(key)  # Retrieve the data from Redis
        if data is None:
            return None  # Return None if the key does not exist
        return fn(data) if fn else data  # Apply conversion function if provided

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and decode it as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))  # Decode the data from bytes to string

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.
        """
        return self.get(key, lambda d: int(d))  # Convert the data from bytes to integer
