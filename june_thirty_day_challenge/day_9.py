"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence
of "abcde" while "aec" is not).
"""


def is_subsequence(text: str,
                   pattern: str) -> bool:

    i = j = 0

    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            j += 1
        i += 1

    return j == len(pattern)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return is_subsequence(t, s)
