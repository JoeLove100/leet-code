import unittest
from june_thirty_day_challenge.day_13 import get_max_divisible_subset


class TestDay13(unittest.TestCase):

    def test_empty_array(self):
        # arrange
        arr = []

        # act
        result = get_max_divisible_subset(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_mutually_prime(self):
        # arrange
        arr = [7, 4, 19]

        # act
        result = get_max_divisible_subset(arr)

        # assert
        self.assertSequenceEqual([19], result)

    def test_includes_1(self):
        # arrange
        arr = [1, 7, 9, 4]

        # act
        result = get_max_divisible_subset(arr)

        # assert
        self.assertSequenceEqual([1, 4], result)

    def test_all_multiples(self):
        # arrange
        arr = [4, 2, 16, 8, 1]

        # act
        result = get_max_divisible_subset(arr)

        # assert
        self.assertSequenceEqual([1, 2, 4, 8, 16], result)

    def test_multiple_subsets(self):
        # arrange
        arr = [1, 5, 9, 3, 15]

        # act
        result = get_max_divisible_subset(arr)

        # assert
        self.assertSequenceEqual([1, 3, 9], result)


