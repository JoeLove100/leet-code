"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one
and sell one share of the stock multiple times) with the following restrictions:

-> You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
-> After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""

from typing import List


def get_max_profit(arr: List[int]) -> int:

    if len(arr) <= 1:
        return 0
    if len(arr) == 2:
        return max(arr[1] - arr[0], 0)

    have_stock = [-arr[0], max(-arr[1], -arr[0])]
    not_have_stock = [0, max(arr[1] - arr[0], 0)]

    for i in range(2, len(arr)):
        have_stock.append(max(have_stock[i - 1], not_have_stock[i - 2] - arr[i]))
        not_have_stock.append(max(not_have_stock[i - 1], have_stock[i - 1] + arr[i]))

    return not_have_stock[-1]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return get_max_profit(prices)