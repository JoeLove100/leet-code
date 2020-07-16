import unittest
from july_thirty_day_challenge.day_16 import my_pow


class TestDay16(unittest.TestCase):

    def test_zero_x(self):
        # arrange
        x = 0
        n = 50

        # act
        result = my_pow(x, n)

        # assert
        self.assertAlmostEqual(0, result)

    def test_zero_n(self):
        # arrange
        x = -0.5
        n = 0

        # act
        result = my_pow(x, n)

        # assert
        self.assertEqual(1, result)

    def test_not_integer(self):
        # arrange
        x = 2.5
        n = 3

        # act
        result = my_pow(x, n)

        # assert
        self.assertAlmostEqual(15.625, result)

    def test_negative_x(self):
        # arrange
        x = -3
        n = -3

        # act
        result = my_pow(x, n)

        # assert
        self.assertAlmostEqual(-1 / 27, result)

