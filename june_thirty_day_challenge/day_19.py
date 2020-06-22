"""
The set [1,2,3,...,n] contains a total of n! unique permutations. Given n and k, return the
kth permutation sequence.

Note:

-> Given n will be between 1 and 9 inclusive.
-> Given k will be between 1 and n! inclusive.
"""

import math
from typing import List


def _get_permutation(numbers: List[int],
                     k: int,
                     acc: List[int]) -> None:

    if not numbers:
        return

    fact = math.factorial(len(numbers) - 1)
    lo = k // fact
    acc.append(numbers[lo])

    new_k = k - fact * lo
    new_numbers = numbers[:lo] + numbers[lo + 1:]
    _get_permutation(new_numbers, new_k, acc)


def get_permutation(n: int,
                    k: int) -> List[int]:

    numbers = list(range(1, n + 1))
    acc = []
    _get_permutation(numbers, k - 1, acc)
    return acc


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perm = get_permutation(n, k)
        return ",".join([str(i) for i in perm])
