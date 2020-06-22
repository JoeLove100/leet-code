"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at
least h citations each, and the other N − h papers have no more than h citations each."
"""
from typing import List


def get_h_index(arr: List[int]):

    j = len(arr)
    i = j - 1
    counter = 0

    while counter != j:

        if arr[i] >= j:
            counter += 1
            i -= 1
        else:
            j -= 1

    return counter


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return get_h_index(citations)
