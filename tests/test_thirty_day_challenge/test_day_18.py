import unittest
from thirty_day_challenge.day_18 import get_min_path


class TestDay18(unittest.TestCase):

    def test_get_min_path_empty_grid(self):
        # arrange
        grid_1 = []
        grid_2 = [[]]

        # act
        result_1 = get_min_path(grid_1)
        result_2 = get_min_path(grid_2)

        # assert
        self.assertEqual(0, result_1)
        self.assertEqual(0, result_2)

    def test_get_min_path_one_number(self):
        # arrange
        grid = [[5]]

        # act
        result = get_min_path(grid)

        # assert
        self.assertEqual(5, result)

    def test_get_min_path_one_column(self):
        # arrange
        grid = [[1, 2, 3, 4]]

        # act
        result = get_min_path(grid)

        # assert
        self.assertEqual(10, result)

    def test_get_min_path_one_row(self):
        # arrange
        grid = [[1], [2], [3], [4]]

        # act
        result = get_min_path(grid)

        # assert
        self.assertEqual(10, result)

    def test_get_min_path_multiple_rows_and_columns(self):
        # arrange
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

        # act
        result = get_min_path(grid)

        # assert
        self.assertEqual(7, result)
