"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words,
one of the first string's permutations is the substring of the second string.
"""
from collections import Counter


def contains_permutation(s_1: str,
                         s_2: str) -> bool:

    if len(s_1) > len(s_2):
        return False

    start = 0
    end = len(s_1) - 1

    pattern = Counter(s_1)
    current_arr = Counter(s_2[start: end + 1])

    while True:

        if pattern == current_arr:
            return True

        # move window end by 1 and new letter
        end += 1
        if end >= len(s_2):
            # reached end of s_2 - stop
            break

        if s_2[end] in current_arr:
            current_arr[s_2[end]] += 1
        else:
            current_arr[s_2[end]] = 1

        # remove start letter and move start of window
        current_arr[s_2[start]] -= 1
        if current_arr[s_2[start]] == 0:
            current_arr.pop(s_2[start])

        start += 1

    return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return contains_permutation(s1, s2)
