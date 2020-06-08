import unittest
from june_thirty_day_challenge.day_7 import get_combinations_2


class TestDay7(unittest.TestCase):

    def test_no_solutions(self):
        # arrange
        coins = [5, 10]
        n = 3

        # act
        result = get_combinations_2(n, coins)

        # assert
        self.assertEqual(0, result)

    def test_only_ones(self):
        # arrange
        coins = [1]
        n = 5

        # act
        result = get_combinations_2(n, coins)

        # assert
        self.assertEqual(1, result)

    def test_multiple_combos(self):
        # arrange
        coins = [1, 2, 5]
        n = 5

        # act
        result = get_combinations_2(n, coins)

        # assert
        self.assertEqual(4, result)

    def test_no_coins(self):
        # arrange
        coins = []
        n = 0

        # act
        result = get_combinations_2(n, coins)

        # assert
        self.assertEqual(1, result)
