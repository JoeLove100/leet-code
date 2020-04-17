"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the
array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
"""
from typing import List


def get_products(arr: List[int]) -> List[int]:

    if len(arr) == 1:
        return arr

    forwards = [arr[0]]
    for n in arr[1:]:
        forwards.append(forwards[-1] * n)

    backwards = [arr[-1]]
    for n in arr[-2::-1]:
        backwards.append(backwards[-1] * n)

    output = []
    i = -1
    j = len(arr) - 2

    for _ in range(len(arr)):

        if i < 0:
            output.append(backwards[j])
        elif j < 0:
            output.append(forwards[i])
        else:
            output.append(forwards[i] * backwards[j])

        i += 1
        j -= 1

    return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return get_products(nums)
