import unittest
from thirty_day_challenge.day_12 import get_remaining_weight


class TestDay12(unittest.TestCase):

    def test_get_remaining_weight_no_stones(self):
        # arrange
        stones = []

        # act
        result = get_remaining_weight(stones)

        # assert
        self.assertEqual(0, result)

    def test_get_remaining_weight_no_last_stone(self):
        # arrange
        stones = [1, 1, 3, 3, 2, 2, 10, 10]

        # act
        result = get_remaining_weight(stones)

        # assert
        self.assertEqual(0, result)

    def test_get_remaining_weight_stone_remains(self):
        # arrange
        stones = [2, 7, 4, 1, 8, 1]

        # act
        result = get_remaining_weight(stones)

        # assert
        self.assertEqual(1, result)
