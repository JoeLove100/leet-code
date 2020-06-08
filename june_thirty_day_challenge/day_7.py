"""
You are given coins of different denominations and a total amount of money. Write a function to compute the
number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""
from typing import List


def get_combinations(n: int,
                     coins: List[int]) -> int:

    if not coins:
        return int(n == 0)

    coins = sorted(coins)

    dp = [[0 for _ in range(len(coins))] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(len(coins)):

            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                if i < coins[0]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - coins[0]][j]
            else:
                if i < coins[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - coins[j]][j]

    return dp[-1][-1]


def get_combinations_2(n: int,
                       coins: List[int]) -> int:

    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for c in coins:
        for i in range(c, n + 1):
            dp[i] += dp[i - c]

    return dp[-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return get_combinations(amount, coins)
