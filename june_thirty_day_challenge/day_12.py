"""
Design a data structure that supports all following operations in average O(1) time.

-> insert(val): Inserts an item val to the set if not already present.
-> remove(val): Removes an item val from the set if present.
-> getRandom: Returns a random element from current set of elements. Each element must have the same
probability of being returned.
"""
import random


class RandomizedSet:

    def __init__(self):

        self._items = []
        self._positions_by_items = dict()

    def insert(self,
               val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self._positions_by_items:
            return False
        else:
            self._items.append(val)
            self._positions_by_items.update({val: len(self._items) - 1})
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val not in self._positions_by_items:
            return False
        else:
            val_position = self._positions_by_items.pop(val)
            if val_position == len(self._items) - 1:
                self._items.pop()
            else:
                last_element = self._items[-1]
                self._items[val_position], self._items[-1] = self._items[-1], self._items[val_position]
                self._items.pop()
                self._positions_by_items.update({last_element: val_position})
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        rn = random.randint(0, len(self._items) - 1)
        return self._items[rn]
