import unittest
from july_thirty_day_challenge.day_27 import create_list_from_tree, recreate_tree


class TestDay27(unittest.TestCase):

    def test_no_input(self):
        # arrange
        in_order = []
        post_order = []

        # act
        result = recreate_tree(in_order, post_order)

        # assert
        self.assertIsNone(result)

    def test_straight_left(self):
        # arrange
        in_order = [3, 2, 1]
        post_order = [3, 2, 1]

        # act
        result = recreate_tree(in_order, post_order)
        result = create_list_from_tree(result)

        # assert
        self.assertSequenceEqual([1, 2, 3], result)

    def test_straight_right(self):
        # arrange
        in_order = [1, 2, 3]
        post_order = [3, 2, 1]

        # act
        result = recreate_tree(in_order, post_order)
        result = create_list_from_tree(result)

        # assert
        self.assertSequenceEqual([1, 2, 3], result)

    def test_full_tree(self):
        # arrange
        in_order = [2, 6, 1, 5, 13, 4, 12]
        post_order = [2, 1, 6, 13, 12, 4, 5]

        # act
        result = recreate_tree(in_order, post_order)
        result = create_list_from_tree(result)

        # assert
        self.assertSequenceEqual([5, 6, 2, 1, 4, 13, 12], result)

    def test(self):
        # arrange
        in_order = [1, 3, 2]
        post_order = [3, 2, 1]

        # act
        result = recreate_tree(in_order, post_order)
        result = create_list_from_tree(result)

        # assert
        self.assertSequenceEqual([1, 2, 3], result)
