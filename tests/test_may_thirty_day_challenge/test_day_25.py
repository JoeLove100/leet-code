import unittest
from may_thirty_day_challenge.day_25 import get_connecting_lines


class TestDay25(unittest.TestCase):

    def test_no_array(self):
        # act
        result_1 = get_connecting_lines([], [1, 2])
        result_2 = get_connecting_lines([2, 5, 3], [])

        # assert
        self.assertEqual(0, result_1)
        self.assertEqual(0, result_2)

    def test_no_connecting_lines(self):
        # arrange
        arr_1 = [1, 5, 3, 5]
        arr_2 = [2, 4, 6]

        # act
        result = get_connecting_lines(arr_1, arr_2)

        # assert
        self.assertEqual(0, result)

    def test_all_same_number(self):
        # arrange
        arr_1 = [5, 5, 5, 5]
        arr_2 = [5, 5]

        # act
        result = get_connecting_lines(arr_1, arr_2)

        # assert
        self.assertEqual(2, result)

    def test_max_two_connections(self):
        # arrange
        arr_1 = [3, 10, 8]
        arr_2 = [10, 3, 8, 9, 9, 1]

        # act
        result = get_connecting_lines(arr_1, arr_2)

        # assert
        self.assertEqual(2, result)

    def test_multiple_occurrences(self):
        # arrange
        arr_1 = [2, 5, 1, 2, 5]
        arr_2 = [10, 5, 2, 1, 5, 2]

        # act
        result = get_connecting_lines(arr_1, arr_2)

        # assert
        self.assertEqual(3, result)

    def test_different_lengths(self):
        # arrange
        arr_1 = [3, 3, 1, 3]
        arr_2 = [1, 3, 2, 3, 3, 1]

        # act
        result = get_connecting_lines(arr_1, arr_2)

        # assert
        self.assertEqual(3, result)
