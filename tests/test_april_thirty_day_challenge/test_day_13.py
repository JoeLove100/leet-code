import unittest
from april_thirty_day_challenge.day_13 import get_max_sub_array_length


class TestDay13(unittest.TestCase):

    def test_max_length_all_zeroes(self):
        # arrange
        arr = [0, 0, 0, 0, 0, 0]

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(0, result)

    def test_max_length_no_zeroes(self):
        # arrange
        arr = [1, 1, 1, 1, 1]

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(0, result)

    def test_max_length_is_full_length(self):
        # arrange
        arr = [0, 1, 1, 1, 0, 0, 0, 1]

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(8, result)

    def test_max_length_not_full_length_even(self):
        # arrange
        arr = [0, 1, 1, 1, 1, 0]

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(result, 2)

    def test_max_length_not_full_odd(self):
        # arrange
        arr = [1, 0, 1, 0, 1]

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(4, result)

    def test_max_length_empty_arr(self):
        # arrange
        arr = []

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(0, result)

    def test_get_max_length(self):
        # arrange
        arr = [0, 1, 1, 0, 1, 1, 1, 0]

        # act
        result = get_max_sub_array_length(arr)

        # assert
        self.assertEqual(4, result)


