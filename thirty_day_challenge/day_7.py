"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them separately.
"""
from typing import List


def get_element_count(arr: List[int]) -> int:

    count = 0
    valid = set(arr)

    for el in arr:
        if el + 1 in valid:
            count += 1

    return count


class Solution:
    def countElements(self, arr: List[int]) -> int:
        return get_element_count(arr)
