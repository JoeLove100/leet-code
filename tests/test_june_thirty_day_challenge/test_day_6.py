import unittest
from june_thirty_day_challenge.day_6 import reconstruct_list


class TestDay6(unittest.TestCase):

    def test_no_list(self):
        # arrange
        arr = []

        # act
        result = reconstruct_list(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_one_person(self):
        # arrange
        arr = [[10, 0]]

        # act
        result = reconstruct_list(arr)

        # assert
        self.assertSequenceEqual([[10, 0]], result)

    def test_in_order(self):
        # arrange
        arr = [[2, 0], [1, 0], [5, 0], [4, 0], [3, 0]]

        # act
        result = reconstruct_list(arr)

        # assert
        expected_list = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
        self.assertSequenceEqual(expected_list, result)

    def test_in_reverse_order(self):
        # arrange
        arr = [[3, 0], [1, 2], [2, 1]]

        # act
        result = reconstruct_list(arr)

        # assert
        expected_list = [[3, 0], [2, 1], [1, 2]]
        self.assertSequenceEqual(expected_list, result)

    def test_out_of_order(self):
        # arrange
        arr = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

        # act
        result = reconstruct_list(arr)

        # assert
        expected_list = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        self.assertSequenceEqual(expected_list, result)
