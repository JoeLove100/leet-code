"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers
(h, k), where h is the height of the person and k is the number of people in front of this person who have a
height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
"""

from typing import List
from collections import defaultdict


def reconstruct_list(arr: List[List[int]]):

    orders_by_height = defaultdict(lambda: [])

    for person in arr:
        orders_by_height[person[0]] += [person[1]]

    queue = []
    for height in sorted(orders_by_height, reverse=True):

        orders = sorted(orders_by_height[height], reverse=False)

        for o in orders:
            queue.insert(o, [height, o])

    return queue


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        return reconstruct_list(people)
