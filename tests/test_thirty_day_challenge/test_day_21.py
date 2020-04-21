import unittest
from thirty_day_challenge.day_21 import BinaryMatrix, get_left_most_one


class TestDay21(unittest.TestCase):

    def test_get_left_most_one_all_ones(self):
        # arrange
        mat = BinaryMatrix([[1], [1], [1]])

        # act
        result = get_left_most_one(mat)

        # assert
        self.assertEqual(0, result)

    def test_get_left_most_one_all_zeroes(self):
        # arrange
        mat = BinaryMatrix([[0, 0, 0], [0, 0, 0]])

        # act
        result = get_left_most_one(mat)

        # assert
        self.assertEqual(-1, result)

    def test_get_left_most_one_in_last_column(self):
        # arrange
        mat = BinaryMatrix([[0, 0, 0, 0], [0, 0, 1, 1, ], [1, 1, 1, 1], [0, 0, 1, 1]])

        # act
        result = get_left_most_one(mat)

        # assert
        self.assertEqual(0, result)

    def test_get_left_most_one_not_in_last_column(self):
        # arrange
        mat = BinaryMatrix([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])

        # act
        result = get_left_most_one(mat)

        # assert
        self.assertEqual(2, result)
