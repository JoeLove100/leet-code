"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear
exactly twice. Find the two elements that appear only once.
"""

from typing import List


def get_single_numbers(arr: List[int]) -> List[int]:

    potential = set()

    while arr:
        n = arr.pop()
        if n in potential:
            potential.remove(n)
        else:
            potential.add(n)

    return list(potential)


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return get_single_numbers(nums)
