"""
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's
price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and
going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans
would be [1, 1, 1, 2, 1, 4, 6].
"""
from collections import namedtuple, deque

StockPrice = namedtuple("StockPrice", ["price", "score"])


class StockSpanner:

    def __init__(self):

        self._stack = deque()

    def next(self,
             price: int) -> int:

        score = 1
        while self._stack and self._stack[-1].price <= price:
            prev = self._stack.pop()
            score += prev.score

        self._stack.append(StockPrice(price, score))
        return score
