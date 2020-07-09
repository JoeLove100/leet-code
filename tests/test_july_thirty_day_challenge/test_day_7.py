import unittest
from july_thirty_day_challenge.day_7 import get_perimeter


class TestDay7(unittest.TestCase):

    def test_no_grid(self):
        # arrange
        arr_1 = []
        arr_2 = [[]]

        # act
        result_1 = get_perimeter(arr_1)
        result_2 = get_perimeter(arr_2)

        # assert
        self.assertEqual(0, result_1)
        self.assertEqual(0, result_2)

    def test_no_island(self):
        # arrange
        arr = [[0, 0], [0, 0], [0, 0]]

        # act
        result = get_perimeter(arr)

        # assert
        self.assertEqual(0, result)

    def test_one_row(self):
        # arrange
        arr = [[0, 0, 1, 1, 1, 0]]

        # act
        result = get_perimeter(arr)

        # assert
        self.assertEqual(8, result)

    def test_one_column(self):
        # arrange
        arr = [[0], [1], [1]]

        # act
        result = get_perimeter(arr)

        # assert
        self.assertEqual(6, result)

    def test_no_water(self):
        # arrange
        arr = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

        # act
        result = get_perimeter(arr)

        # assert
        self.assertEqual(12, result)

    def test_island(self):
        # arrange
        arr = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0, ], [1, 1, 0, 0]]

        # act
        result = get_perimeter(arr)

        # assert
        self.assertEqual(16, result)