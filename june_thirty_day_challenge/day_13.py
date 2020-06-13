"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in
this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
"""

from typing import List


def get_max_divisible_subset(arr: List[int]) -> List[int]:

    arr = sorted(arr)
    dp = [0 for _ in range(len(arr))]
    subsets = dict()
    max_subset = []

    for i in reversed(range(len(arr))):

        current_max = 0
        current_index_of_max = i

        for j in range(i + 1, len(arr)):

            if current_max < dp[j] and arr[j] % arr[i] == 0:
                current_max = dp[j]
                current_index_of_max = j

        dp[i] = current_max + 1

        if current_index_of_max == i:
            max_subset_for_i = [arr[i]]
        else:
            max_subset_for_i = [arr[i]] + subsets[arr[current_index_of_max]]

        if len(max_subset_for_i) > len(max_subset):
            max_subset = max_subset_for_i
        subsets.update({arr[i]: max_subset_for_i})

    return max_subset


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        return get_max_divisible_subset(nums)
