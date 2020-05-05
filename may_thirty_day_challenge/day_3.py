"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a
function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will
return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
"""

from collections import defaultdict


def can_construct(target: str,
                  available_letters: str) -> bool:

    if not target:
        return True

    if not available_letters:
        return False

    all_letters = defaultdict(lambda: 0)

    for letter in available_letters:
        all_letters[letter] += 1

    for letter in target:
        if letter not in all_letters or all_letters[letter] == 0:
            return False
        else:
            all_letters[letter] -= 1

    return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return can_construct(ransomNote, magazine)
