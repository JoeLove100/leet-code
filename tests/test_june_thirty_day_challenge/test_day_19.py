import unittest
from june_thirty_day_challenge.day_19 import get_permutation


class TestDay19(unittest.TestCase):

    def test_one_number(self):
        # arrange
        n = 1
        k = 1

        # act
        result = get_permutation(n, k)

        # assert
        self.assertEqual([1], result)

    def test_two_numbers(self):
        # arrange
        n = 2
        k = 2

        # act
        result = get_permutation(n, k)

        # assert
        self.assertEqual([2, 1], result)

    def test_three_numbers(self):
        # arrange
        n = 3
        k = 4

        # act
        result = get_permutation(n, k)

        # assert
        self.assertEqual([2, 3, 1], result)

    def test_four_numbers(self):
        # arrange
        n = 4
        k = 16

        # act
        result = get_permutation(n, k)

        # assert
        self.assertEqual([3, 2, 4, 1], result)
