#!/usr/bin/python3
""" fifo_cache.py """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
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

        if key in self.cache_data:
            # If the key already exists, move it to the end
            del self.cache_data[key]
            
        # Add the new key-item pair to the cache
        self.cache_data[key] = item

        # If the number of items exceeds MAX_ITEMS,
        if len(self.cache_data) > self.MAX_ITEMS:
            # Pop the first item (least recently used)
            first_key, first_item = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Retrieve item from cache by key."""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        item = self.cache_data.pop(key) # remove the entry yet retrieve the item value
        self.cache_data[key] = item
        return item
