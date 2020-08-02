import unittest
from july_thirty_day_challenge.day_29 import get_max_profit


class TestDay29(unittest.TestCase):

    def test_one_day(self):
        # arrange
        arr = [10]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(0, result)

    def test_three_days(self):
        # arrange
        arr = [1, 4, 2]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(3, result)

    def test_monotone_increasing(self):
        # arrange
        arr = [3, 4, 5, 5, 6, 7, 8]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(5, result)

    def test_monotone_decreasing(self):
        # arrange
        arr = [10, 8, 6, 4, 2]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(0, result)

    def test_buy_at_peak(self):
        # arrange
        arr = [1, 2, 10, 0, 2]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(9, result)

    def test_buy_pre_peak(self):
        # arrange
        arr = [1, 2, 3, 0, 2]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(3, result)

    def test_double_peak(self):
        # arrange
        arr = [6, 1, 3, 2, 4, 7]

        # act
        result = get_max_profit(arr)

        # assert
        self.assertEqual(6, result)
