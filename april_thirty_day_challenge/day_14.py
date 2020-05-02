"""
You are given a string s containing lowercase English letters, and a matrix
shift, where shift[i] = [direction, amount]:

-> direction can be 0 (for left shift) or 1 (for right shift).
-> amount is the amount by which string s is to be shifted.
-> A left shift by 1 means remove the first character of s and append it to the end.
-> Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.
"""

from typing import List
from collections import deque


def get_shifted_text(text: str,
                     all_shifts: List[List[int]]) -> str:

    text = deque(text)
    for shift in all_shifts:

        shift_direction = shift[0]
        shift_length = shift[1]
        if shift_direction == 0:
            text.rotate(len(text) - shift_length)
        else:
            text.rotate(shift_length)

    text = "".join(text)
    return text


def get_shifted_text_2(text: str,
                       all_shifts: List[List[int]]) -> str:

    total_shift = 0

    for shift in all_shifts:
        if shift[0] == 0:
            total_shift -= shift[1]
        else:
            total_shift += shift[1]

    text = deque(text)
    text.rotate(total_shift)
    return "".join(text)


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        return get_shifted_text_2(s, shift)
