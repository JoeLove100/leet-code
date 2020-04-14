"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its
capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a POSITIVE capacity.
"""

from collections import deque


class LRUCache:

    def __init__(self, capacity: int):

        self._capacity = capacity
        self._queue = deque([])
        self._cache = dict()

    def get(self, key: int) -> int:

        return self._cache.get(key, -1)

    def put(self, key: int, value: int) -> None:

        if len(self._queue) == self._capacity:
            to_remove = self._queue.popleft()
            self._cache.pop(to_remove)

        self._queue.append(key)
        self._cache[key] = value


if __name__ == "__main__":

    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))
    lru_cache.put(3, 3)
    print(lru_cache.get(2))
    lru_cache.put(4, 4)
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
