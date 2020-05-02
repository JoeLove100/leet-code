import unittest
from april_thirty_day_challenge.day_22 import get_number_of_subarrays


class TestDay22(unittest.TestCase):

    def test_get_number_of_subarrays_no_subarrays(self):
        # arrange
        arr = [1, 5, 2]
        n = 3

        # act
        result = get_number_of_subarrays(arr, n)

        # assert
        self.assertEqual(0, result)

    def test_get_number_of_subarrays_whole_array(self):
        # arrange
        arr = [1, 3, 9, 2]
        n = 15

        # act
        result = get_number_of_subarrays(arr, n)

        # assert
        self.assertEqual(1, result)

    def test_get_number_of_subarrays_multiple_arrays(self):
        # arrange
        arr = [1, 3, 2, 2, 1, 1]
        n = 4

        # act
        result = get_number_of_subarrays(arr, n)

        # assert
        self.assertEqual(3, result)

    def test_get_number_of_subarrays_negative_numbers(self):
        # arrange
        arr = [-1, 0, -2, 3, -2]
        n = -1

        # act
        result = get_number_of_subarrays(arr, n)

        # assert
        self.assertEqual(4, result)

    def test_get_number_of_subarrays(self):
        # arrange
        arr = [1, 2, -1, 1, 4]
        n = 4

        # act
        result = get_number_of_subarrays(arr, n)

        # assert
        self.assertEqual(2, result)
