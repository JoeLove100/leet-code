import unittest
from july_thirty_day_challenge.day_23 import get_single_numbers


class TestDay23(unittest.TestCase):

    def test_only_two_numbers(self):
        # arrange
        arr = [1, 2]

        # act
        result = get_single_numbers(arr)

        # assert
        self.assertSequenceEqual([1, 2], result)

    def test_number_at_end(self):
        # arrange
        arr = [1, 2, 3, 4, 3, 2, 1, 5]

        # act
        result = get_single_numbers(arr)

        # assert
        self.assertSequenceEqual([4, 5], result)

    def test_number_at_start(self):
        # arrange
        arr = [10, 2, 3, 3, 4, 5, 5, 4]

        # act
        result = get_single_numbers(arr)

        # assert
        self.assertSequenceEqual([2, 10], result)