import unittest
from june_thirty_day_challenge.day_3 import get_min_cost


class TestDay3(unittest.TestCase):

    def test_two_people(self):
        # arrange
        arr = [[10, 5], [100, 6]]

        # act
        result = get_min_cost(arr)

        # assert
        self.assertEqual(16, result)

    def test_all_same_cost(self):
        # arrange
        arr = [[10, 10], [12, 12], [1, 1], [6, 6]]

        # act
        result = get_min_cost(arr)

        # assert
        self.assertEqual(29, result)

    def test_all_cheaper_for_b(self):
        # arrange
        arr = [[5, 1], [11, 10], [8, 2], [7, 2]]

        # act
        result = get_min_cost(arr)

        # assert
        self.assertEqual(20, result)

    def test_no_rebalance_required(self):
        # arrange
        arr = [[10, 20], [30, 200], [400, 50], [30, 20]]

        # act
        result = get_min_cost(arr)

        # assert
        self.assertEqual(110, result)

