"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""
from typing import List


def get_max_area(grid: List[List[str]]) -> int:

    if not grid or not grid[0]:
        return 0

    max_val = 0

    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):

            grid[i][j] = int(grid[i][j])

            if grid[i][j] == 0:
                continue

            if i != len(grid) - 1 and j != len(grid[0]) - 1:
                grid[i][j] = min(grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]) + 1

            max_val = max(max_val, grid[i][j])

    return max_val ** 2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return get_max_area(matrix)
