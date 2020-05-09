import unittest
from may_thirty_day_challenge.day_9 import is_perfect_square


class TestDay9(unittest.TestCase):

    def test_is_perfect_square_one(self):
        # arrange
        n = 1

        # act
        result = is_perfect_square(n)

        # assert
        self.assertTrue(result)

    def test_is_perfect_square_square_number(self):
        # arrange
        n = 144

        # act
        result = is_perfect_square(n)

        # assert
        self.assertTrue(result)

    def test_is_perfect_square_number_not_square(self):
        # arrange
        n = 95

        # act
        result = is_perfect_square(n)

        # assert
        self.assertFalse(result)

    def test_is_perfect_square_almost_square(self):
        # arrange
        n = 82

        # act
        result = is_perfect_square(n)

        # assert
        self.assertFalse(result)