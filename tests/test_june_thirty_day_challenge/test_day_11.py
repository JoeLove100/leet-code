import unittest
from june_thirty_day_challenge.day_11 import get_sorted_array


class TestDay11(unittest.TestCase):

    def test_empty_array(self):
        # arrange
        arr = []

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_already_sorted(self):
        # arrange
        arr = [0, 0, 1, 2, 2]

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([0, 0, 1, 2, 2], result)

    def test_reverse_order(self):
        # arrange
        arr = [2, 2, 1, 0, 0]

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([0, 0, 1, 2, 2], result)

    def test_0_1_only(self):
        # arrange
        arr = [0, 1, 1, 0, 1]

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([0, 0, 1, 1, 1], result)

    def test_1_2_only(self):
        # arrange
        arr = [2, 2, 1, 2]

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([1, 2, 2, 2], result)

    def test_0_2_only(self):
        # arrange
        arr = [0, 2, 0, 2, 2]

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([0, 0, 2, 2, 2], result)

    def test_unsorted(self):
        # arrange
        arr = [2, 0, 2, 1, 1, 0]

        # act
        result = get_sorted_array(arr)

        # assert
        self.assertSequenceEqual([0, 0, 1, 1, 2, 2], result)

