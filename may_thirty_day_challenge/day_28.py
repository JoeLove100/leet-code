"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
their binary representation and return them as an array.
"""
from typing import List


def get_ones(n: int) -> List[int]:

    ones = [0]

    while len(ones) < n + 1:
        ones.extend([i + 1 for i in ones])

    return ones[:n + 1]


class Solution:
    def countBits(self, num: int) -> List[int]:
        return get_ones(num)
