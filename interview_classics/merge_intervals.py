"""
Given a collection of intervals, merge all overlapping intervals.
"""
from typing import List


def get_merged_intervals(intervals: List[List[int]]) -> List[List[int]]:

    if not intervals:
        return []

    sorted_intervals = sorted(intervals)
    merged_intervals = []

    start, end = sorted_intervals[0]

    for interval in sorted_intervals:

        if end >= interval[0]:
            end = max(interval[1], end)
        else:
            merged_intervals.append([start, end])
            start, end = interval

    merged_intervals.append([start, end])
    return merged_intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return get_merged_intervals(intervals)

if __name__ == "__main__":

    print(get_merged_intervals([[1, 2], [2, 4], [1, 3], [5, 10]]))
