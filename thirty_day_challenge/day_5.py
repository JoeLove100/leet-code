"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (i.e., buy one and sell one share of the stock multiple times).
"""

from typing import List


def get_max_profit(arr: List[int]):
    """
    get max profit from buying and selling
    the stock
    """

    max_from_first_sale = [0 for _ in range(len(arr) + 1)]
    max_profit = 0

    for i in reversed(range(len(arr) - 1)):

        if arr[i] >= arr[i + 1]:
            max_from_first_sale[i] = max_from_first_sale[i + 1]
            continue

        mx = 0
        for j in range(i, len(arr)):
            profit = max(0, arr[j] - arr[i])
            profit += max_from_first_sale[j + 1]
            mx = max(mx, profit)

        max_from_first_sale[i] = mx
        max_profit = max(max_profit, mx)

    return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return get_max_profit(prices)


if __name__ == "__main__":

    import cProfile

    arr = list(reversed(range(10001)))
    print(len(arr))
    cProfile.run(f"get_max_profit({arr})")
