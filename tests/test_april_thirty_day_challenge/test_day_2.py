import unittest
from april_thirty_day_challenge.day_2 import is_happy


class TestDay2(unittest.TestCase):

    def test_is_happy_should_be_false(self):
        # arrange
        n = 63

        # act
        result = is_happy(n)

        # assert
        self.assertFalse(result)

    def test_is_happy_should_be_true(self):
        # arrange
        n = 19

        # act
        result = is_happy(n)

        # assert
        self.assertTrue(result)
