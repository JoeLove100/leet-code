import unittest
from may_thirty_day_challenge.day_11 import _get_neighbours, _fill


class TestDay11(unittest.TestCase):

    def test_get_neighbours_center(self):
        # arrange
        coord = (1, 1)
        length = 3
        width = 3

        # act
        result = _get_neighbours(coord, length, width)

        # assert
        self.assertSequenceEqual([(2, 1), (0, 1), (1, 2), (1, 0)], result)

    def test_get_neighbours_corner(self):
        # arrange
        coord = (0, 0)
        length = 4
        width = 2

        # act
        result = _get_neighbours(coord, length, width)

        # assert
        self.assertSequenceEqual([(1, 0), (0, 1)], result)

    def test_fill_no_matching_neighbours(self):
        # arrange
        arr = [[0, 1, 0], [2, 2, 2], [1, 1, 0]]
        coord = (0, 1)
        nc = 2

        # act
        _fill(arr, coord, nc, set())

        # assert
        expected_arr = [[0, 2, 0], [2, 2, 2], [1, 1, 0]]
        self.assertSequenceEqual(expected_arr, arr)

    def test_fill_matching_neighbours(self):
        # arrange
        arr = [[1, 1, 1, 2], [3, 0, 1, 1], [2, 0, 1, 2], [5, 1, 1, 0]]
        coord = (2, 2)
        nc = 5

        # act
        _fill(arr, coord, nc, set())

        # assert
        expected_arr = [[5, 5, 5, 2], [3, 0, 5, 5], [2, 0, 5, 2], [5, 5, 5, 0]]
        self.assertSequenceEqual(expected_arr, arr)

    def test_flood_fill(self):
        # arrange
        arr = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        coord = (1, 1)
        new_colour = 2

        # act
        _fill(arr, coord, new_colour, set())

        # asset
        expected_arr = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertSequenceEqual(expected_arr, arr)
