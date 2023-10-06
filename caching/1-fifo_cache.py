'''
basic cache
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Basic cache class """
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Put an item """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed_key = self.queue.pop(0)
            del self.cache_data[removed_key]
            print(f"DISCARD: {removed_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
