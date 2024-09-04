#!/usr/bin/env python3
"""FIFO Caching System
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class that inherits from BaseCaching.
    Implements a caching system using the FIFO method.
    """

    def __init__(self):
        """Initialize the cache and call the parent constructor.
        """
        super().__init__()
        self.order = []  # To keep track of the insertion order

    def put(self, key, item):
        """Add an item to the cache using FIFO strategy.

        Args:
            key: The key for the item.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the old key to maintain the order correctly
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first item inserted (FIFO)
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key, None)
