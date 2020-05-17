"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be
larger than 20,100.

The order of output does not matter.
"""
from typing import List
from collections import Counter


def get_all_anagram_positions(text: str,
                              pattern: str) -> List[int]:

    positions = []

    if len(text) < len(pattern) or not pattern:
        return positions

    start = 0
    end = len(pattern) - 1

    pattern_counter = Counter(pattern)
    current_counter = Counter(text[start: end + 1])

    while True:
        if pattern_counter == current_counter:
            positions.append(start)

        current_counter[text[start]] -= 1
        if current_counter[text[start]] == 0:
            current_counter.pop(text[start])

        start += 1
        end += 1

        if end >= len(text):
            return positions
        elif text[end] in current_counter:
            current_counter[text[end]] += 1
        else:
            current_counter[text[end]] = 1


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return get_all_anagram_positions(s, p)
