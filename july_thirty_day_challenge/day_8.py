"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
triplets in the array which gives the sum of zero.
"""
from typing import List
from collections import  Counter


def get_triples(arr: List[int]) -> List[List[int]]:

    if len(arr) < 3:
        return []

    counter = Counter(arr)
    all_triples = set()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            total = -(arr[i] + arr[j])
            if total in counter:
                triple = tuple(sorted([arr[i], arr[j], total]))
                if total != arr[i] and total != arr[j]:
                    all_triples.add(triple)
                if total == arr[i] and total == arr[j]:
                    if counter[total] > 2:
                        all_triples.add(triple)
                else:
                    if counter[total] > 1:
                        all_triples.add(triple)

    all_triples = [list(t) for t in all_triples]
    return all_triples


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return get_triples(nums)