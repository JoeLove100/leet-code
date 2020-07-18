import unittest
from july_thirty_day_challenge.day_17 import get_most_common


class TestDay17(unittest.TestCase):

    def test_zero_element(self):
        # arrange
        arr = []
        k = 0

        # act
        result = get_most_common(arr, k)

        # assert
        self.assertEqual([], result)

    def test_one_element(self):
        # arrange
        arr = [2]
        k = 1

        # act
        result = get_most_common(arr, k)

        # assert
        self.assertEqual([2], result)

    def test_multiple_elements(self):
        # arrange
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        k = 3

        # act
        result = get_most_common(arr, k)

        # assert
        self.assertEqual([2, 3, 4], result)

    def test_element_readded(self):
        # arrange
        arr = [1, 2, 3, 2, 3, 1, 1, 1, 3]
        k = 2

        # act
        result = get_most_common(arr, k)

        # assert
        self.assertEqual([1, 3], result)

    def test_reverse_order(self):
        # arrange
        arr = [4, 4, 4, 4, 3, 3, 3, 2, 2, 1]
        k = 3

        # act
        result = get_most_common(arr, k)

        # assert
        self.assertEqual([4, 3, 2], result)

    def test_added_first(self):
        # arrange
        arr = [4, 4, 4, 3]