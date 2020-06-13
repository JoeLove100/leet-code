"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index
where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
from typing import List


def _binary_search(arr: List[int],
                   low: int,
                   high: int,
                   target: int) -> int:
    if high == low:
        return low

    mid = (high + low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return _binary_search(arr, low, mid, target)
    else:
        return _binary_search(arr, mid + 1, high, target)


def binary_search(arr: List[int],
                  target: int) -> int:
    return _binary_search(arr, 0, len(arr), target)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)
