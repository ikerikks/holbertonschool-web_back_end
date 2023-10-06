#!/usr/bin/env python3
""" cache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ mru cache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put a key/value pair into the cache """
        if key is None or item is None:
            return

        # Check if the cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find and remove the most recently used item
            mru_key = max(self.accessed.keys(), key=lambda k: self.accessed[k])
            del self.cache_data[mru_key]
            del self.accessed[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the new item to the cache
        self.cache_data[key] = item
        self.accessed[key] = self.current_time

        self.current_time += 1

    def get(self, key):
        """ Get the item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.accessed[key] = self.current_time
        self.current_time += 1

        return self.cache_data[key]
