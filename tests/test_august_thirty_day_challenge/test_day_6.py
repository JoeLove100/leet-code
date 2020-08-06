import unittest
from august_thirty_day_challenge.day_6 import find_duplicated


class TestDay6(unittest.TestCase):

    def test_no_array(self):
        # arrange
        arr = []

        # act
        result = find_duplicated(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_no_duplicates(self):
        # arrange
        arr = [1, 2, 6, 4, 10, 8, 99]

        # act
        result = find_duplicated(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_finds_dupes(self):
        # arrange
        arr = [1, 2, 56, 7, 1, 3, 2, 3]

        # act
        result = find_duplicated(arr)

        # assert
        self.assertSequenceEqual([1, 2, 3], result)