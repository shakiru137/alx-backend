#!/usr/bin/python3
"""Basic caching module."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.

    This is a basic caching system that does not have any limit on the number
    of items it can store.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is None
            or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
