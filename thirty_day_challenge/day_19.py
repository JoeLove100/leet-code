"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""
import math
from typing import List


def shifted_binary_research(arr: List[int],
                            key: int,
                            start: int,
                            end: int):

    if end - start <= 0:
        return -1

    mid = math.floor((start + end) / 2)

    if arr[mid] == key:
        return mid

    if arr[mid] > arr[start]:
        if arr[start] <= key < arr[mid]:
            return shifted_binary_research(arr, key, start, mid)
        else:
            return shifted_binary_research(arr, key, mid + 1, end)
    else:
        if key < arr[mid] or key >= arr[start]:
            return shifted_binary_research(arr, key, start, mid)
        else:
            return shifted_binary_research(arr, key, mid + 1, end)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return shifted_binary_research(nums, target, 0, len(nums))
