import unittest
from thirty_day_challenge.day_5 import get_max_profit, get_max_linear_time


class TestDay5(unittest.TestCase):

    def test_get_max_profit_one_price(self):
        # arrange
        arr = [10]

        # act
        result = get_max_linear_time(arr)

        # assert
        self.assertEqual(0, result)

    def test_get_max_profit_uniformly_increasing(self):
        # arrange
        arr = [1, 2, 3, 4, 5]

        # act
        result = get_max_linear_time(arr)

        # assert
        self.assertEqual(4, result)

    def test_get_max_profit_uniformly_decreasing(self):
        # arrange
        arr = [5, 4, 3, 2, 1]

        # act
        result = get_max_linear_time(arr)

        # assert
        self.assertEqual(0, result)

    def test_get_max_profit(self):
        # arrange
        arr = [7, 1, 5, 3, 6, 4]

        # act
        result = get_max_linear_time(arr)

        # assert
        self.assertEqual(7, result)

    def test_get_max_profit_with_zero(self):
        # arrange
        arr = [3, 2, 6, 5, 0, 3]

        # act
        result = get_max_linear_time(arr)

        # assert
        self.assertEqual(7, result)
