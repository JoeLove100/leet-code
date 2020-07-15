"""
Given an input string, reverse the string word by word.
"""


def get_reversed_text(text: str) -> str:

    words = text.split()
    reversed_text = " ".join(words[::-1])
    return reversed_text


class Solution:
    def reverseWords(self, s: str) -> str:
        return get_reversed_text(s)
