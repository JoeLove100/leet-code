import unittest
from may_thirty_day_challenge.day_30 import get_k_closest_points


class TestDay30(unittest.TestCase):

    def test_less_than_k_points(self):
        # arrange
        points = [[-1, 1], [2, 3]]
        k = 3

        # act
        result = get_k_closest_points(points, k)

        # assert
        self.assertSequenceEqual([[-1, 1], [2, 3]], result)

    def test_all_positive(self):
        # arrange
        points = [[1, 1], [2, 2], [1, 2], [0, 10], [0, 1], [1, 0]]
        k = 2

        # act
        result = get_k_closest_points(points, k)

        # assert
        self.assertSequenceEqual([[0, 1], [1, 0]], result)

    def test_all_negative(self):
        # arrange
        points = [[-1, -1], [-1, -2], [-2, -3], [0, -1]]
        k = 2

        # act
        result = get_k_closest_points(points, k)

        # assert
        self.assertSequenceEqual([[-1, -1], [0, -1]], result)

    def test_both_positive_and_negative(self):
        # arrange
        points = [[0, 1], [2, 2], [-1, -2], [4, -1], [1, -1]]
        k = 2

        # act
        result = get_k_closest_points(points, k)

        # assert
        self.assertSequenceEqual([[1, -1], [0, 1]], result)
