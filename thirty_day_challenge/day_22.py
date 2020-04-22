"""
Given an array of integers and an integer k, you need to find the total number of continuous
subarrays whose sum equals to k.
"""

from typing import List
from collections import defaultdict


def get_number_of_subarrays(arr: List[int],
                            k: int) -> int:

    value_counts = defaultdict(lambda:0)
    value_counts.update({0: 1})
    subarray_count = 0
    running_total = 0

    for number in arr:
        running_total += number
        if running_total - k in value_counts:
            subarray_count += value_counts[running_total - k]

        value_counts[running_total] += 1

    return subarray_count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return get_number_of_subarrays(nums, k)


if __name__ == "__main__":

    import random
    import cProfile

    array = [random.randint(-1000, 1000) for _ in range(20000)]
    n = random.randint(-1000000, 1000000)

    cProfile.run(f"get_number_of_subarrays({array}, {n})")
