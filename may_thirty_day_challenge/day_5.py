"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""


def get_index_of_first_unique_letter(text: str) -> int:

    if not text:
        return -1

    unique_letters = dict()
    existing_letters = set()

    for i, letter in enumerate(text):

        if letter in unique_letters:
            unique_letters.pop(letter)

        if letter not in existing_letters:
            unique_letters.update({letter: i})
            existing_letters.add(letter)

    if not unique_letters:
        return -1
    else:
        return min(unique_letters.values())


class Solution:
    def firstUniqChar(self, s: str) -> int:
        return get_index_of_first_unique_letter(s)
