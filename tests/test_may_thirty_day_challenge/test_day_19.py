import unittest
from may_thirty_day_challenge.day_19 import StockSpanner


class TestDay19(unittest.TestCase):

    def test_one_price_only(self):
        # act
        ss = StockSpanner()
        prices = [1]

        # act
        result = [ss.next(i) for i in prices]

        # assert
        self.assertSequenceEqual([1], result)

    def test_uniformly_increasing(self):
        # act
        ss = StockSpanner()
        prices = [10, 20, 30, 45, 50]

        # act
        result = [ss.next(i) for i in prices]

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 5], result)

    def test_uniformly_decreasing(self):
        # act
        ss = StockSpanner()
        prices = [10, 8, 4, 2, 1]

        # act
        result = [ss.next(i) for i in prices]

        # assert
        self.assertSequenceEqual([1, 1, 1, 1, 1], result)

    def test_all_same_value(self):
        # act
        ss = StockSpanner()
        prices = [2, 2, 2, 2]

        # act
        result = [ss.next(i) for i in prices]

        # assert
        self.assertSequenceEqual([1, 2, 3, 4], result)

    def test_handles_troughs_correctly(self):
        # act
        ss = StockSpanner()
        prices = [1, 5, 4, 3, 2, 6]

        # act
        result = [ss.next(i) for i in prices]

        # assert
        self.assertSequenceEqual([1, 2, 1, 1, 1, 6], result)

    def test_handles_peaks_correctly(self):
        # act
        ss = StockSpanner()
        prices = [1, 4, 10, 8, 11, 4, 5]

        # act
        result = [ss.next(i) for i in prices]

        # assert
        self.assertSequenceEqual([1, 2, 3, 1, 5, 1, 2], result)
