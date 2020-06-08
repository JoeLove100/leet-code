import unittest
from june_thirty_day_challenge.day_8 import is_power_of_2


class TestDay8(unittest.TestCase):

    def test_one(self):
        # arrange
        n = 1

        # act
        result = is_power_of_2(n)

        # assert
        self.assertTrue(result)

    def test_power_of_two(self):
        # arrange
        n = 1024

        # act
        result = is_power_of_2(n)

        # assert
        self.assertTrue(result)

    def test_not_power_of_two_odd(self):
        # arrange
        n = 101

        # act
        result = is_power_of_2(n)

        # arrange
        self.assertFalse(result)

    def test_not_power_of_two_event(self):
        # arrange
        n = 96

        # act
        result = is_power_of_2(n)

        # assert
        self.assertFalse(result)
