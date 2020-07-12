"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

from typing import List


def _power_set(nums: List[int],
               base: List[int],
               acc: List[List[int]]) -> None:

    acc.append(base)

    for i in range(len(nums)):
        _power_set(nums[i+1:], base + [nums[i]], acc)


def power_set(nums: List[int]) -> List[List[int]]:

    acc = []
    nums = sorted(nums)
    _power_set(nums, [], acc)

    return acc


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return power_set(nums)
