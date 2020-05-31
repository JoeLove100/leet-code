import unittest
from may_thirty_day_challenge.day_27 import can_be_partitioned


class TestDat27(unittest.TestCase):

    def test_no_dislikes(self):
        # arrange
        n = 10
        dislikes = []

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertTrue(result)

    def test_all_dislike_each_other(self):
        # arrange
        n = 3
        dislikes = [[2, 3], [3, 1], [1, 2]]

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertFalse(result)

    def test_straight_line_dislikes(self):
        # arrange
        n = 5
        dislikes = [[1, 2], [2, 3], [3, 4], [4, 5]]

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertTrue(result)

    def test_even_loop(self):
        # arrange
        n = 4
        dislikes = [[1, 2], [2, 3], [3, 4], [4, 1]]

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertTrue(result)

    def test_odd_loop(self):
        # arrange
        n = 5
        dislikes = [[1, 2], [3, 4], [2, 3], [5, 1], [4, 5]]

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertFalse(result)

    def test_piecewise_bipartite(self):
        # arrange
        n = 7
        dislikes = [[1, 2], [3, 4], [5, 6], [5, 7]]

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertTrue(result)

    def test_piecewise_not_bipartite(self):
        # arrange
        n = 5
        dislikes = [[1, 2], [3, 4], [4, 5], [3, 5]]

        # act
        result = can_be_partitioned(n, dislikes)

        # assert
        self.assertFalse(result)
