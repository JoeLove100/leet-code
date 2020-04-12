"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x
and y with x <= y.  The result of this smash is:

->   If x == y, both stones are totally destroyed;
->  If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""

import heapq
from typing import List


def get_remaining_weight(stones: List) -> int:

    stones = [-n for n in stones]  # negate for min heap
    heapq.heapify(stones)

    while len(stones) > 1:

        largest = -heapq.heappop(stones)
        next_largest = -heapq.heappop(stones)

        if next_largest < largest:
            heapq.heappush(stones, next_largest - largest)

    if not stones:
        return 0
    else:
        return -stones[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return get_remaining_weight(stones)