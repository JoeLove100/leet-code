"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""
from typing import List


def count_squares(arr: List[List[int]]) -> int:

    if not arr or not arr[0]:
        return 0

    total = 0
    dp = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]

    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr[0]) -1, -1, -1):

            if i == len(arr) - 1 or j == len(arr[0]) - 1:
                dp[i][j] = arr[i][j]
            else:
                if arr[i][j] == 0:
                    dp[i][j] = 0
                else:
                    arr[i][j] = min(arr[i + 1][j + 1], arr[i + 1][j], arr[i][j + 1]) + 1

            total += arr[i][j]

    return total


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        return count_squares(matrix)
