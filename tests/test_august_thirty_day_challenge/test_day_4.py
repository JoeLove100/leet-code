import unittest
from august_thirty_day_challenge.day_4 import is_power_of_4


class TestDay4(unittest.TestCase):

    def test_one(self):
        # arrange
        num = 1

        # act
        result = is_power_of_4(num)

        # assert
        self.assertTrue(result)

    def test_power_of_four(self):
        # arrange
        num = 64

        # act
        result = is_power_of_4(num)

        # assert
        self.assertTrue(result)

    def test_power_of_two_no_four(self):
        # arrange
        num = 128

        # act
        result = is_power_of_4(num)

        # assert
        self.assertFalse(result)

    def test_not_power_of_two(self):
        # arrange
        num = 100

        # act
        result = is_power_of_4(num)

        # assert
        self.assertFalse(result)