"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""
from typing import List


def get_single_element(arr: List[int]) -> int:
    """
    get the single repeated element in arr
    """

    visited_numbers = set()

    while arr:
        if arr[-1] in visited_numbers:
            visited_numbers.remove(arr.pop())
        else:
            visited_numbers.add(arr.pop())

    return list(visited_numbers)[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return get_single_element(nums)
