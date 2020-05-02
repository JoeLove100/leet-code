"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
from typing import List


def get_min_path(grid: List[List[int]]):

    if not grid or not grid[0]:
        return 0

    min_path_sums = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if i == j == 0:
                min_path_sums[i][j] = grid[i][j]
            elif i == 0:
                min_path_sums[i][j] = grid[i][j] + min_path_sums[i][j - 1]
            elif j == 0:
                min_path_sums[i][j] = grid[i][j] + min_path_sums[i - 1][j]
            else:
                min_path_sums[i][j] = min(min_path_sums[i][j - 1], min_path_sums[i - 1][j])
                min_path_sums[i][j] += grid[i][j]

    return min_path_sums[-1][-1]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return get_min_path(grid)
