"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

-> FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
-> int showFirstUnique() returns the value of the first unique integer of the queue, and
   returns -1 if there is no such integer.
-> void add(int value) insert value to the queue.
"""
from typing import List
from collections import OrderedDict


class FirstUnique:

    def __init__(self,
                 nums: List[int]) -> None:

        self._unique_numbers = OrderedDict()
        self._non_unique_numbers = set()

        for n in nums:
            if n in self._unique_numbers:
                self._unique_numbers.pop(n)
                self._non_unique_numbers.add(n)
            elif n not in self._unique_numbers and n not in self._non_unique_numbers:
                self._unique_numbers.update({n: None})

    def add(self,
            value: int) -> None:

        if value in self._non_unique_numbers:
            return
        elif value in self._unique_numbers:
            self._unique_numbers.pop(value)
            self._non_unique_numbers.add(value)
        else:
            self._unique_numbers.update({value: None})

    def showFirstUnique(self):

        return next(iter(self._unique_numbers), -1)
