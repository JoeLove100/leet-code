"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""

from typing import List


def is_possible(arr: List[int]) -> bool:

    if len(arr) <= 1:
        return True

    possible = [True for _ in range(len(arr))]

    for i in range(len(arr) - 2, -1, -1):

        max_jump = arr[i]
        possible[i] = any(possible[i + 1: min(len(arr), i + 1 + max_jump)])

    return possible[0]


def is_possible_linear(arr: List[int]) -> bool:

    if len(arr) <= 1:
        return True

    i = 0
    j = 0

    while i <= j:

        j = max(arr[i] + i, j)
        if j >= len(arr) - 1:
            return True

        i += 1

    return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return is_possible(nums)



