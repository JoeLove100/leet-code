import unittest
from july_thirty_day_challenge.day_4 import get_nth_ugly_number


class TestDay4(unittest.TestCase):

    def test_get_first(self):
        # arrange
        n = 1

        # act
        result = get_nth_ugly_number(n)

        # assert
        self.assertEqual(1, result)

    def test_larger_than_one(self):
        # arrange
        n = 10

        # act
        result = get_nth_ugly_number(n)

        # assert
        self.assertEqual(12, result)