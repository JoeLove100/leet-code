"""
Given an array of size n, find the majority element. The majority element is the element that appears more
than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

import math
from typing import List
from collections import defaultdict


def get_modal_element(arr: List[int]) -> int:

    counter = defaultdict(lambda: 0)
    max_count = 0
    cutoff = math.floor(len(arr) / 2)

    for n in arr:
        counter[n] += 1
        max_count = max(max_count, counter[n])
        if max_count > cutoff:
            return n


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return get_modal_element(nums)


if __name__ == "__main__":

    print(get_modal_element([2, 2, 1, 1, 1, 2, 2]))
