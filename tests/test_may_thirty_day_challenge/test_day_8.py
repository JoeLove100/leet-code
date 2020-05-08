import math
import unittest
from may_thirty_day_challenge.day_8 import get_gradient, are_colinear


class TestDay8(unittest.TestCase):

    def test_get_gradient_horizontal(self):
        # arrange
        coord_1 = [3, 8]
        coord_2 = [1, 8]

        # act
        result = get_gradient(coord_1, coord_2)

        # assert
        self.assertEqual(0, result)

    def test_get_gradient_vertical(self):
        # arrange
        coord_1 = [1, 10]
        coord_2 = [1, -1]

        # act
        result = get_gradient(coord_1, coord_2)

        # assert
        self.assertEqual(math.inf, result)

    def test_get_gradient_in_order(self):
        # arrange
        coord_1 = [2, 4]
        coord_2 = [4, 8]

        # act
        result = get_gradient(coord_1, coord_2)

        # assert
        self.assertEqual(2, result)

    def test_get_gradient_reverse_order(self):
        # arrange
        coord_1 = [1, -1]
        coord_2 = [-1, 0]

        # act
        result = get_gradient(coord_2, coord_1)

        # assert
        self.assertEqual(-0.5, result)

    def test_are_colinear_two_points(self):
        # arrange
        coords = [[1, 4], [0, -10]]

        # act
        result = are_colinear(coords)

        # assert
        self.assertTrue(result)

    def test_are_colinear_vertical(self):
        # arrange
        coords = [[0, 2], [0, -3], [0, 100]]

        # act
        result = are_colinear(coords)

        # assert
        self.assertTrue(result)

    def test_are_colinear_not_colinear(self):
        # arrange
        coords = [[1, -1], [0, 0], [-1, -1]]

        # act
        result = are_colinear(coords)

        # assert
        self.assertFalse(result)

    def test_are_colinear_are_colinear(self):
        # arrange
        coords = [[4, 4], [3, 6], [6, 0], [0, 12]]

        # act
        result = are_colinear(coords)

        # assert
        self.assertTrue(result)
