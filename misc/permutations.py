"""
Given a collection of distinct integers, return all possible permutations.
"""

from typing import List, Set


def _get_permutations(arr: List[int],
                      items: Set[int],
                      output: List[List[int]]) -> None:

    if not items:
        output.append(arr)

    for an_item in items:
        _get_permutations(arr + [an_item], items - {an_item}, output)


def get_permutations(arr: List[int]) -> List[List[int]]:

    if not arr:
        return []

    output = []
    _get_permutations([], set(arr), output)
    return output


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return get_permutations(nums)


if __name__ == "__main__":

    print(get_permutations([1, 2, 3]))
