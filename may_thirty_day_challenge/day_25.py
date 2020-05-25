"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

-> A[i] == B[j];
-> The line we draw does not intersect any other connecting (non-horizontal) line.
-> Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to
   one connecting line.

Return the maximum number of connecting lines we can draw in this way.
"""
from typing import List


def get_connecting_lines(arr_1: List[int],
                         arr_2: List[int]) -> int:

    if not arr_1 or not arr_2:
        return 0

    dp = [[0 for _ in range(len(arr_2))] for _ in range(len(arr_1))]
    last_positions_1 = {}

    for i in range(len(arr_1)):
        last_positions_2 = {}
        for j in range(len(arr_2)):

            if i == 0 and j == 0:
                dp[i][j] = int(arr_1[i] == arr_2[j])
            elif i == 0:
                dp[i][j] = max(dp[i][j - 1], int(arr_1[i] == arr_2[j]))
            elif j == 0:
                dp[i][j] = max(dp[i - 1][j], int(arr_1[i] == arr_2[j]))
            else:
                if arr_1[i] == arr_2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    if arr_1[i] in last_positions_2:
                        last_pos = last_positions_2[arr_1[i]]
                        if last_pos > 0:
                            dp[i][j] = dp[i - 1][last_pos - 1] + 1
                        else:
                            dp[i][j] = 1
                    if arr_2[j] in last_positions_1:
                        last_pos = last_positions_1[arr_2[j]]
                        if last_pos > 0:
                            dp[i][j] = max(dp[i][j], dp[last_pos - 1][j - 1] + 1)
                        else:
                            dp[i][j] = max(dp[i][j], 1)
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

            last_positions_1.update({arr_1[i]: i})
            last_positions_2.update({arr_2[j]: j})

    return dp[-1][-1]


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        return get_connecting_lines(A, B)

