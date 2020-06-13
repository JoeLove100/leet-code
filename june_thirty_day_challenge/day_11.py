"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""

from typing import List


def swap(i: int,
         j: int,
         arr: List[int]) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def get_sorted_array(arr: List[int]) -> List[int]:

    j = k = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            swap(i, k, arr)
            swap(k, j, arr)
            k += 1
            j += 1
        elif arr[i] == 1:
            swap(i, k, arr)
            k += 1

    return arr


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        get_sorted_array(nums)
