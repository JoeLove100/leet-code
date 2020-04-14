"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given
target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""

from typing import List
import math


def binary_search(val: int,
                  arr: List[int],
                  start: int,
                  end: int,
                  get_lowest_index: bool) -> int:

    if start == end:
        return -1

    mid = math.floor((start + end) / 2)

    if arr[mid] == val:
        if get_lowest_index:
            lower_index = binary_search(val, arr, start, mid, get_lowest_index)
            if lower_index == -1:
                return mid
            else:
                return lower_index
        else:
            return max(mid, binary_search(val, arr, mid + 1, end, get_lowest_index))
    elif val < arr[mid]:
        return binary_search(val, arr, start, mid, get_lowest_index)
    else:
        return binary_search(val, arr, mid + 1, end, get_lowest_index)


def get_min_max(val: int,
                arr: List[int]) -> List[int]:

    min_idx = binary_search(val, arr, 0, len(arr), True)
    if min_idx == -1:
        return [-1, -1]

    max_idx = binary_search(val, arr, 0, len(arr), False)
    return [min_idx, max_idx]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return get_min_max(target, nums)


if __name__ == "__main__":

    arr = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6]
    print(get_min_max(1, arr))
