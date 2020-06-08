"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which
randomly picks an index in proportion to its weight.
"""
import bisect
import random
from typing import List


class Solution:

    def __init__(self,
                 w: List[int]):

        cumulative_sums = [w[0]]

        for number in w[1:]:
            cumulative_sums.append(number + cumulative_sums[-1])

        self._cumulative_sums = cumulative_sums

    def pickIndex(self) -> int:

        rand_int = random.randint(0, self._cumulative_sums[-1] - 1)
        return bisect.bisect(self._cumulative_sums, rand_int)


if __name__ == "__main__":

    random.seed(1234)
    arr = [3, 1]
    s = Solution(arr)

    zero_count = 0
    one_count = 0

    for _ in range(1000):

        if s.pickIndex() == 0:
            zero_count += 1
        else:
            one_count += 1

    print(zero_count)
    print(one_count)
