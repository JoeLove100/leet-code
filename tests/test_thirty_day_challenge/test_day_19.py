import unittest
from thirty_day_challenge.day_19 import shifted_binary_research


class TestDay19(unittest.TestCase):

    def test_shifted_binary_search_empty(self):
        # arrange
        arr = []
        key = 3

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(-1, result)

    def test_shifted_binary_search_no_shift(self):
        # arrange
        arr = [1, 2, 3, 4, 5, 6, 7]
        key = 2

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(1, result)

    def test_shifted_binary_search_pivot_left_key_left(self):
        # arrange
        arr = [5, 1, 2, 3, 4]
        key = 5

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(0, result)

    def test_shifted_binary_search_pivot_left_key_right(self):
        # arrange
        arr = [6, 7, 1, 2, 3, 4, 5]
        key = 4

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(5, result)

    def test_shifted_binary_search_pivot_right_key_left(self):
        # arrange
        arr = [3, 4, 5, 6, 7, 1, 2]
        key = 3

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(0, result)

    def test_shifted_binary_search_pivot_right_key_right(self):
        # arrange
        arr = [4, 5, 6, 7, 0, 1, 2]
        key = 0

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(4, result)

    def test_shifted_binary_search_key_not_found(self):
        # arrange
        arr = [3, 4, 5, 7, 8, 1, 2]
        key = 6

        # act
        result = shifted_binary_research(arr, key, 0, len(arr))

        # assert
        self.assertEqual(-1, result)

