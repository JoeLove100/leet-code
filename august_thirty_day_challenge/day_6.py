"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.
"""

from typing import List


def find_duplicated(arr: List[int]) -> List[int]:

    tmp = set()
    final = set()

    while arr:
        n = arr.pop()
        if n not in tmp:
            tmp.add(n)
        else:
            tmp.remove(n)
            final.add(n)

    return list(final)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return find_duplicated(nums)
