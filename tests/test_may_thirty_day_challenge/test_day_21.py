import unittest
from may_thirty_day_challenge.day_21 import count_squares


class TestDay21(unittest.TestCase):

    def test_no_array(self):
        # arrange
        arr_1 = []
        arr_2 = [[]]

        # act
        result_1 = count_squares(arr_1)
        result_2 = count_squares(arr_2)

        # assert
        self.assertEqual(0, result_1)
        self.assertEqual(0, result_2)

    def test_column_array(self):
        # arrange
        arr = [[1], [1], [0], [1]]

        # act
        result = count_squares(arr)

        # assert
        self.assertEqual(3, result)

    def test_row_array(self):
        # arrange
        arr = [[1, 0, 1, 0]]

        # act
        result = count_squares(arr)

        # assert
        self.assertEqual(2, result)

    def test_squares_of_multiple_sizes(self):
        # arrange
        arr = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]

        # act
        result = count_squares(arr)

        # assert
        self.assertEqual(15, result)
