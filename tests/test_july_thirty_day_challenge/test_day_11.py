import unittest
from july_thirty_day_challenge.day_11 import power_set


class TestDay11(unittest.TestCase):

    def test_one_number(self):
        # arrange
        nums = [2]

        # act
        result = power_set(nums)

        # assert
        self.assertSequenceEqual([[], [2]], result)

    def test_not_in_order(self):
        # arrange
        nums = [3, 2, 1]

        # act
        result = power_set(nums)

        # assert
        expected_result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertSequenceEqual(expected_result, result)

    def test_no_numbers(self):
        # arrange
        nums = []

        # act
        result = power_set(nums)

        # assert
        self.assertSequenceEqual([[]], result)

