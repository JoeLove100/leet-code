"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the
array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

from typing import List


def get_plus_one(arr: List[int]) -> List[int]:

    i = len(arr) - 1
    while i >= 0:
        digit = arr[i] + 1
        if digit != 10:
            arr[i] = digit
            return arr
        else:
            arr[i] = 0
            i -= 1

    return [1] + arr


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return get_plus_one(digits)
