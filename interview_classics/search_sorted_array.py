"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

from typing import List
import math


def _binary_search(val: int,
                   arr: List[int],
                   start: int,
                   end: int) -> int:

    if end - start < 1:
        return -1

    mid = math.floor((start + end) / 2)

    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return _binary_search(val, arr, mid + 1, end)
    else:
        return _binary_search(val, arr, start, mid)


def _rotated_binary_search(val: int,
                           arr: List[int],
                           start: int,
                           end: int) -> int:

    if end - start < 1:
        return -1

    mid = math.floor((start + end) / 2)
    if arr[mid] == val:
        return mid

    left_of_pivot = arr[mid] > arr[start]

    if left_of_pivot:
        if arr[mid] > val >= arr[start]:
            return _binary_search(val, arr, start, mid)
        else:
            return _rotated_binary_search(val, arr, mid + 1, end)
    else:
        if arr[mid] < val <= arr[end - 1]:
            return _binary_search(val, arr, mid + 1, end)
        else:
            return _rotated_binary_search(val, arr, start, mid)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return _rotated_binary_search(target, nums, 0, len(nums))

if __name__ == "__main__":

    arr = [6, 8, 1, 2, 3, 4, 5]
    print(_rotated_binary_search(1, arr, 0, len(arr)))

