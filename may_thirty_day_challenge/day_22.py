"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

from collections import Counter


def sort_letters(text: str) -> str:

    if not text:
        return ""

    letter_counter = Counter(text)
    ordered_letters = [l * n for l, n in sorted(letter_counter.items(), reverse=True, key=lambda item: item[1])]
    return "".join(ordered_letters)


class Solution:
    def frequencySort(self, s: str) -> str:
        return sort_letters(s)
