import unittest
from july_thirty_day_challenge.day_6 import get_plus_one


class TestDay6(unittest.TestCase):

    def test_does_not_end_in_nine(self):
        # arrange
        arr = [1, 2, 3, 4]

        # act
        result = get_plus_one(arr)

        # assert
        self.assertSequenceEqual([1, 2, 3, 5], result)

    def test_one_digit(self):
        # arrange
        arr = [6]

        # act
        result = get_plus_one(arr)

        # assert
        self.assertSequenceEqual([7], result)

    def test_ends_in_nine(self):
        # arrange
        arr = [1, 0, 9, 9]

        # act
        result = get_plus_one(arr)

        #
        self.assertSequenceEqual([1, 1, 0, 0], result)

    def test_all_nines(self):
        # arrange
        arr = [9, 9, 9]

        # act
        result = get_plus_one(arr)

        # assert
        self.assertSequenceEqual([1, 0, 0, 0], result)