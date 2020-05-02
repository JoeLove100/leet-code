import unittest
from april_thirty_day_challenge.day_20 import get_tree_in_order


class TestDay20(unittest.TestCase):

    def test_get_in_order_no_tree(self):
        # arrange
        arr = []

        # act
        result = get_tree_in_order(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_get_in_order_left_nodes_only(self):
        # arrange
        arr = [5, 4, 3, 2, 1]

        # act
        result = get_tree_in_order(arr)

        # assert
        self.assertSequenceEqual([5, 4, None, 3, None, 2, None, 1, None], result)

    def test_get_in_order_right_nodes_only(self):
        # arrange
        arr = [1, 2, 3, 4, 5]

        # act
        result = get_tree_in_order(arr)

        # assert
        self.assertSequenceEqual([1, None, 2, None, 3, None, 4, None, 5], result)

    def test_get_in_order_full_tree(self):
        # arrange
        arr = [5, 3, 2, 4, 7, 6, 12]

        # act
        result = get_tree_in_order(arr)

        # assert
        self.assertSequenceEqual([5, 3, 7, 2, 4, 6, 12], result)

    def test_get_in_order_not_full_tree(self):
        # arrange
        arr = [6, 4, 3, 1, 5, 12, 17, 13]

        # act
        result = get_tree_in_order(arr)

        # assert
        self.assertSequenceEqual([6, 4, 12, 3, 5, None, 17, 1, None, 13, None], result)
