"""
Given a non-empty array of integers, every element appears three times except for one, which appears
exactly once. Find that single one.
"""

from typing import List


def get_single_element(arr: List[int]) -> int:

    numbers = {}

    for n in arr:
        if n not in numbers:
            numbers[n] = 0
        elif numbers[n] == 0:
            numbers[n] += 1
        else:
            numbers.pop(n)

    return list(numbers)[0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return get_single_element(nums)
