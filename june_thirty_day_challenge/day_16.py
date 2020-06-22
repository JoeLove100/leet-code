"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
from typing import List, Tuple, Set


def get_neighbours(i: int,
                   j: int,
                   arr: List[List[str]]) -> List[Tuple[int, int]]:

    neighbours = []
    if i > 0 and arr[i - 1][j] == "O":
        neighbours.append((i - 1, j))
    if i < len(arr) - 1 and arr[i + 1][j] == "O":
        neighbours.append((i + 1, j))
    if j > 0 and arr[i][j - 1] == "O":
        neighbours.append((i, j - 1))
    if j < len(arr[0]) - 1 and arr[i][j + 1] == "O":
        neighbours.append((i, j + 1))

    return neighbours


def dfs(arr: List[List[str]],
        i: int,
        j: int,
        visited: Set) -> None:

    stack = [(i, j)]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            all_neighbours = get_neighbours(*current, arr)
            for neighbour in all_neighbours:
                stack.append(neighbour)


def set_board(arr: List[List[str]]) -> None:

    if not arr or not arr[0]:
        return None

    visited = set()

    for i in {0, max(len(arr) - 1, 0)}:
        for j in range(len(arr[0])):

            if arr[i][j] == "O" and (i, j) not in visited:
                dfs(arr, i, j, visited)

    for j in {0, max(len(arr[0]) - 1, 0)}:
        for i in range(1, len(arr) - 1):

            if arr[i][j] == "O" and (i, j) not in visited:
                dfs(arr, i, j, visited)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (i, j) in visited:
                arr[i][j] = "O"
            else:
                arr[i][j] = "X"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        return set_board(board)
