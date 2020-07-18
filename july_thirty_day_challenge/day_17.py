"""
Given a non-empty array of integers, return the k most frequent elements.
"""

import heapq
import functools
from typing import List


@functools.total_ordering
class HeapEntry:

    def __init__(self,
                 val: int,
                 priority: int,
                 valid: bool):

        self.val = val
        self.priority = priority
        self.valid = valid

    def __eq__(self,
               other: "HeapEntry") -> bool:
        return self.priority == other.priority

    def __lt__(self,
               other: "HeapEntry") -> bool:
        return self.priority < other.priority


def get_most_common(arr: List[int],
                    k: int) -> List[int]:

    number_heap = []
    heap_entries = dict()
    counters = dict()

    for n in arr:

        # update counts
        if n in counters:
            counters[n] += 1
        else:
            counters[n] = 1

        # clean out invalid entries in heap
        while number_heap and not number_heap[0].valid:
            heapq.heappop(number_heap)

        # update heap for n
        if len(heap_entries) < k or number_heap[0].priority < counters[n]:

            if n not in heap_entries and len(heap_entries) >= k:
                # number not currently in heap
                prev_entry = heapq.heappop(number_heap)
                heap_entries.pop(prev_entry.val)

            elif n in heap_entries:
                # already in heap so mark prev as invalid and add new entry
                heap_entries[n].valid = False

            # add new entry
            new_entry = HeapEntry(n, counters[n], True)
            heap_entries.update({n: new_entry})
            heapq.heappush(number_heap, new_entry)

    return [e.val for e in number_heap if e.valid]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return get_most_common(nums, k)
