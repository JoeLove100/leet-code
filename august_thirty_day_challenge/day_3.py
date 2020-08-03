"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


def is_valid_palindrome(text: str) -> bool:

    i = 0
    j = len(text) - 1

    while i < j:

        if not text[i].isalnum():
            i += 1
        elif not text[j].isalnum():
            j -= 1
        else:
            if text[i].lower() != text[j].lower():
                return False
            i += 1
            j -= 1

    return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return is_valid_palindrome(s)
