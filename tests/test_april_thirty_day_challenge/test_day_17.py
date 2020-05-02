import unittest
from april_thirty_day_challenge.day_17 import get_number_of_islands, get_number_of_islands_bfs


class TestDay17(unittest.TestCase):

    def test_number_of_islands_empty_arr(self):
        # arrange
        arr_1 = []
        arr_2 = [[]]

        # act
        result_1 = get_number_of_islands_bfs(arr_1)
        result_2 = get_number_of_islands_bfs(arr_2)

        # assert
        self.assertEqual(0, result_1)
        self.assertEqual(0, result_2)

    def test_number_of_islands_one_island(self):
        # arrange
        arr = [["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]

        # act
        result = get_number_of_islands_bfs(arr)

        # assert
        self.assertEqual(1, result)

    def test_number_of_islands_all_ones(self):
        # arrange
        arr = [["1", "1"], ["1", "1"]]

        # act
        result = get_number_of_islands_bfs(arr)

        # assert
        self.assertEqual(1, result)

    def test_number_of_islands_diagonals(self):
        # arrange
        arr = [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]]

        # act
        result = get_number_of_islands_bfs(arr)

        # assert
        self.assertEqual(4, result)

    def test_number_of_islands(self):
        # arrange
        arr = [["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]]

        # act
        result = get_number_of_islands_bfs(arr)

        # assert
        self.assertEqual(1, result)
