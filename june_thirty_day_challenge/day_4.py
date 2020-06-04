"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.

You may assume all the characters consist of printable ascii characters.
"""
from typing import List


def reverse_string(text: List[str]) -> None:

    i = 0
    j = len(text) - 1

    while i < j:
        text[i], text[j] = text[j], text[i]
        i += 1
        j -= 1


class Solution:
    def reverseString(self, s: List[str]) -> None:
        reverse_string(s)
