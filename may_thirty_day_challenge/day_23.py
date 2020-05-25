"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.
"""
from typing import List
from collections import deque


def get_intervals(arr_1: List[List[int]],
                  arr_2: List[List[int]]) -> List[List[int]]:

    q_1 = deque(arr_1)
    q_2 = deque(arr_2)
    intersections = []

    while q_1 and q_2:

        interval_1 = q_1[0]
        interval_2 = q_2[0]

        if interval_1[0] <= interval_2[0]:
            if interval_1[1] < interval_2[0]:
                q_1.popleft()
            elif interval_2[0] <= interval_1[1] <= interval_2[1]:
                intersections.append([interval_2[0], interval_1[1]])
                q_1.popleft()
            else:
                intersections.append(interval_2)
                q_2.popleft()
        else:
            if interval_2[1] < interval_1[0]:
                q_2.popleft()
            elif interval_1[0] <= interval_2[1] <= interval_1[1]:
                intersections.append([interval_1[0], interval_2[1]])
                q_2.popleft()
            else:
                intersections.append(interval_1)
                q_1.popleft()

    return intersections


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return get_intervals(A, B)
