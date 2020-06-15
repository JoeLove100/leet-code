import unittest
from june_thirty_day_challenge.day_14 import get_shortest_distance


class TestDay14(unittest.TestCase):

    def test_only_one_path(self):
        # arrange
        arr = [[1, 2, 100]]

        # act
        result = get_shortest_distance(arr, 1, 1, 2)

        # assert
        self.assertEqual(100, result)

    def test_no_path_exists_disjoint(self):
        # arrange
        arr = [[1, 2, 20], [2, 1, 20], [3, 4, 30], [4, 3, 32]]

        # act
        result = get_shortest_distance(arr, 2, 1, 3)

        # assert
        self.assertEqual(-1, result)

    def test_no_path_exists_too_far(self):
        # arrange
        arr = [[1, 2, 10], [2, 3, 50], [2, 4, 40], [3, 5, 15], [4, 5, 20], [5, 6, 15]]

        # act
        result = get_shortest_distance(arr, 2, 1, 6)

        # assert
        self.assertEqual(-1, result)

    def test_handles_back_edges(self):
        # arrange
        arr = [[1, 2, 20], [2, 1, 20]]

        # act
        result = get_shortest_distance(arr, 5, 1, 2)

        # assert
        self.assertEqual(20, result)

    def test_multiple_routes(self):
        # arrange
        arr = [[1, 2, 20], [1, 3, 50], [2, 3, 20]]

        # act
        result = get_shortest_distance(arr, 1, 1, 3)

        # assert
        self.assertEqual(40, result)
