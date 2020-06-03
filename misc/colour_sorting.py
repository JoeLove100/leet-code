"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
"""

from typing import List


def swap(arr: List[int],
         i: int,
         j: int) -> None:

    arr[i], arr[j] = arr[j], arr[i]


def sort_array(arr: List[int]) -> None:

    j = k = 0

    for i, n in enumerate(arr):
        if n == 0:
            swap(arr, i, j)
            swap(arr, j, k)
            j += 1
            k += 1
        elif n == 1:
            swap(arr, i, j)
            j += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        sort_array(nums)


if __name__ == "__main__":

    arr = [1, 2, 1, 1, 2]
    sort_array(arr)
    print(arr)
