"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List, Tuple, Set


def _contains_word(arr: List[List[str]],
                   i: int,
                   j: int,
                   word: str,
                   visited: Set[Tuple[int, int]]) -> bool:

    # if all letters found, then true
    if not word:
        return True

    # check if we have already visited co-ordinates
    if (i, j) in visited:
        return False

    # check if co-ordinates are in bounds
    if i < 0 or i >= len(arr):
        return False
    if j < 0 or j >= len(arr[0]):
        return False

    # check if co-ordinates have correct letter
    if arr[i][j] == word[0]:
        for _i, _j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if _contains_word(arr, i + _i, j + _j, word[1:], visited | {(i, j)}):
                return True

    return False


def contains_word(arr: List[List[str]],
                  word: str) -> bool:

    if not word:
        return True

    if not arr or not arr[0]:
        return False

    length = len(arr)
    width = len(arr[0])

    for i in range(length):
        for j in range(width):
            if _contains_word(arr, i, j, word, set()):
                return True

    return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return contains_word(board, word)
