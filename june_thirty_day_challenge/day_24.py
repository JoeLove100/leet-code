"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

# catalan numbers


def get_number_of_trees(n: int) -> int:

    dp = [1]

    for i in range(n):
        number_trees = 0
        for j in range(i + 1):
            number_trees += dp[j] * dp[len(dp) - 1 - j]

        dp.append(number_trees)

    return dp[-1]


class Solution:
    def numTrees(self, n: int) -> int:
        return get_number_of_trees(n)
