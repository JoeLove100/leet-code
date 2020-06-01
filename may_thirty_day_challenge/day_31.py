"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

-> Insert a character
-> Delete a character
-> Replace a character
"""


def min_changes(word_1: str,
                word_2: str) -> int:

    if not word_1 or not word_2:
        return max(len(word_1), len(word_2))

    dp = [[0 for _ in range(len(word_2) + 1)] for _ in range(len(word_1) + 1)]

    for i in range(len(word_1) + 1):
        for j in range(len(word_2) + 1):

            if i == 0 or j == 0:
                dp[i][j] = max(i, j)
            elif word_1[i - 1] == word_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[-1][-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return min_changes(word1, word2)
