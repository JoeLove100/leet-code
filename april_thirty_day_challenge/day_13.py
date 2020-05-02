"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""


from typing import List


def get_max_sub_array_length_quadratic(arr: List[int]) -> int:

    if not arr:
        return 0

    max_length = min(sum(arr), len(arr) - sum(arr)) * 2

    while max_length >= 0:

        i = 0
        j = i + max_length
        target_sum = max_length / 2

        while j <= len(arr):
            if sum(arr[i: j]) == target_sum:
                return max_length

            i += 1
            j += 1

        max_length -= 2

    return 0


def get_max_sub_array_length(arr: List[int]) -> int:

    max_length = 0
    first_occurrences = dict({0: 0})
    counter = 0

    for i, n in enumerate(arr):

        if n == 0:
            counter -= 1
        else:
            counter += 1

        if counter in first_occurrences:
            max_length = max(max_length, i + 1 - first_occurrences[counter])
        else:
            first_occurrences.update({counter: i + 1})

    return max_length


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        return get_max_sub_array_length_quadratic(nums)
