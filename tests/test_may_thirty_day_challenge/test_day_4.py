import unittest
from may_thirty_day_challenge.day_4 import get_binary_complement


class TestDay4(unittest.TestCase):

    def test_get_binary_complement_zero(self):
        # arrange
        n = 1

        # act
        result = get_binary_complement(n)

        # assert
        self.assertEqual(0, result)

    def test_get_binary_complement(self):
        # arrange
        n = 5

        # act
        result = get_binary_complement(n)

        # assert
        self.assertEqual(2, result)
