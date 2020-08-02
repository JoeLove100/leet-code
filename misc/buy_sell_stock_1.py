"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design
an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

from typing import List


def get_max_profit(arr: List[int]) -> int:

    if not arr:
        return 0

    buy = arr[0]
    sell = 0

    for price in arr:
        buy = min(buy, price)
        sell = max(sell, price - buy)

    return sell


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return get_max_profit(prices)
