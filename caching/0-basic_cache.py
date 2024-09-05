#!/usr/bin/python3
""" basic_cache.py """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class inherits and overrides put and get to dictionary
    key value pairs."""
    def __init__(self):
        """Initialize the parent class"""
        super().__init__()
        self.cache_data = {}  # Initialize an empty dictionary for caching

    def put(self, key, item):
        """Add key-item pair to cache."""
        if key is None or item is None:
            return

        # Store the item in the cache
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is None:
            return None

        # Return the item if it exists in the cache
        return self.cache_data.get(key, None)
