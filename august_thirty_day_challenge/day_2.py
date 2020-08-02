"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

-> add(value): Insert a value into the HashSet.
-> contains(value) : Return whether the value exists in the HashSet or not.
-> remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
"""


class MyHashSet:

    def __init__(self):

        self._map = [[] for _ in range(10000)]

    def add(self,
            key: int) -> None:

        if not self.contains(key):
            self._map[key % len(self._map)].append(key)

    def remove(self, key: int) -> None:

        if self.contains(key):
            self._map[key % len(self._map)].remove(key)

    def contains(self, key: int) -> bool:

        vals = self._map[key % len(self._map)]
        return key in vals
