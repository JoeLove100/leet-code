import unittest
from may_thirty_day_challenge.day_28 import get_ones


class TestDay28(unittest.TestCase):

    def test_zero(self):
        # arrange
        n = 0

        # act
        result = get_ones(n)

        # assert
        self.assertSequenceEqual([0], result)

    def test_one(self):
        # arrange
        n = 1

        # act
        result = get_ones(n)

        # assert
        self.assertSequenceEqual([0, 1], result)

    def test_ten(self):
        # arrange
        n = 10

        # act
        result = get_ones(n)

        # assert
        self.assertSequenceEqual([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2], result)
