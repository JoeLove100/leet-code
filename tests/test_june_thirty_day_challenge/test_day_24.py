import unittest
from june_thirty_day_challenge.day_24 import get_number_of_trees


class TestDay24(unittest.TestCase):

    def test_n_is_one(self):
        # arrange
        n = 1

        # act
        result = get_number_of_trees(n)

        # assert
        self.assertEqual(1, result)

    def test_n_is_two(self):
        # arrange
        n = 2

        # act
        result = get_number_of_trees(n)

        # assert
        self.assertEqual(2, result)

    def test_n_is_three(self):
        # arrange
        n = 3

        # act
        result = get_number_of_trees(n)

        # assert
        self.assertEqual(5, result)

    def test_n_is_four(self):
        # arrange
        n = 4

        # act
        result = get_number_of_trees(n)

        # assert
        self.assertEqual(14, result)

    def test_n_is_five(self):
        # arrange
        n = 5

        # act
        result = get_number_of_trees(n)

        # assert
        self.assertEqual(42, result)
