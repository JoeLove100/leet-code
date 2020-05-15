"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for
one element which appears exactly once. Find this single element that appears only once.
"""

from typing import List
import math


def _get_single_element(arr: List[int],
                        low: int,
                        high: int) -> int:

    mid = math.floor((high + low) / 2)

    if mid > 0 and arr[mid] == arr[mid - 1]:
        if mid % 2 == 0:
            return _get_single_element(arr, low, mid + 1)
        else:
            return _get_single_element(arr, mid + 1, high)
    if mid < len(arr) - 1 and arr[mid] == arr[mid + 1]:
        if mid % 2 == 0:
            return _get_single_element(arr, mid, high)
        else:
            return _get_single_element(arr, low, mid)
    else:
        return arr[mid]


def get_single_element(arr: List[int]) -> int:

    return _get_single_element(arr, 0, len(arr))


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return get_single_element(nums)
