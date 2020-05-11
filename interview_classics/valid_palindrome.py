"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""


def _can_be_palindrome(text: str,
                       start: int,
                       end: int,
                       mismatches: int) -> bool:
    if start >= end:
        return True

    if text[start] == text[end]:
        return _can_be_palindrome(text, start + 1, end - 1, mismatches)
    else:
        if mismatches == 1:
            return False
        else:
            return _can_be_palindrome(text, start, end - 1, mismatches + 1) \
                   or _can_be_palindrome(text, start + 1, end, mismatches + 1)


def can_be_palindrome(text) -> bool:
    return _can_be_palindrome(text, 0, len(text) - 1, 0)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        return can_be_palindrome(s)


if __name__ == "__main__":

    print(can_be_palindrome("abcddfcba"))
