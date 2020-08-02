"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

-> All letters in this word are capitals, like "USA".
-> All letters in this word are not capitals, like "leetcode".
-> Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
"""

import string
from typing import Optional


def is_correct_caps(word: Optional) -> bool:

    if len(word) < 2:
        return True

    upper = set(string.ascii_uppercase)
    lower = set(string.ascii_lowercase)

    start = 1 if word[0] in upper else 0
    case_set = upper if word[start] in upper else lower

    for i in range(start, len(word)):
        if word[i] not in case_set:
            return False

    return True


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return is_correct_caps(word)
