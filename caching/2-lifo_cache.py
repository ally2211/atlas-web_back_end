#!/usr/bin/python3
""" fifo_cache.py """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """FIFO (First-In, First-Out) caching."""
    def __init__(self):
        """Initialize the parent class"""
        super().__init__()
        # maintain the insertion order of the cache items
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add key-item pair to cache."""
        if key is None or item is None:
            return

        # Add the new item to the cache
        if key in self.cache_data:
            # If the key already exists, remove it
            del self.cache_data[key]

        # Store the item in the cache
        self.cache_data[key] = item

        # If the number of items exceeds MAX_ITEMS,
        if len(self.cache_data) > self.MAX_ITEMS:
            # Pop the first item (FIFO behavior)
            last_key, last_item = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")  # For testing or logging purposes

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is None:
            return None

        # Return the item if it exists in the cache
        return self.cache_data.get(key, None)
