"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its
capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a POSITIVE capacity.
"""

import heapq


class LRUCache:

    def __init__(self, capacity: int):

        self._capacity = capacity
        self._heap = []
        heapq.heapify([])
        self._cache = dict()
        self._count = 0
        self._entry_register = dict()

    def get(self, key: int) -> int:

        if key not in self._cache:
            return -1
        else:
            if key in self._entry_register:
                prev_entry = self._entry_register[key]
                prev_entry[2] = False

            new_entry = [self._count, key, True]
            self._entry_register.update({key: new_entry})
            heapq.heappush(self._heap, new_entry)
            self._count += 1
            return self._cache[key]

    def put(self, key: int, value: int) -> None:

        if key in self._cache:
            prev_entry = self._entry_register[key]
            prev_entry[2] = False
        else:
            if len(self._cache) == self._capacity:
                while True:
                    to_remove = heapq.heappop(self._heap)
                    if to_remove[2]:
                        self._cache.pop(to_remove[1])
                        break

        new_entry = [self._count, key, True]
        heapq.heappush(self._heap, new_entry)
        self._cache[key] = value
        self._entry_register[key] = new_entry
        self._count += 1


if __name__ == "__main__":

    lru_cache = LRUCache(2)
    print(lru_cache.get(2))
    lru_cache.put(2, 6)
    print(lru_cache.get(1))
    lru_cache.put(1, 5)
    lru_cache.put(1, 2)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
