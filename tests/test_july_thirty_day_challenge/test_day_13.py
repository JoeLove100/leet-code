import unittest
from july_thirty_day_challenge.day_13 import create_tree_from_list, are_same, TreeNode


class TestDay13(unittest.TestCase):

    def test_both_null(self):
        # arrange
        tree_1 = tree_2 = None

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertTrue(result)

    def test_first_null(self):
        # arrange
        tree_1 = None
        tree_2 = TreeNode(2)

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertFalse(result)

    def test_second_null(self):
        # arrange
        tree_1 = TreeNode(2)
        tree_2 = None

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertFalse(result)

    def test_not_equal_different_lengths(self):
        # arrange
        tree_1 = create_tree_from_list([1, 2, 3, 4])
        tree_2 = create_tree_from_list([1, 2, 3])

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertFalse(result)

    def test_not_equal_different_values(self):
        # arrange
        tree_1 = create_tree_from_list([1, 2, 3, 4, 5, 6, 8])
        tree_2 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertFalse(result)

    def test_not_equal_different_positions(self):
        # arrange
        tree_1 = create_tree_from_list([1, 2])
        tree_2 = create_tree_from_list([1, None, 2])

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertFalse(result)

    def test_not_equal_different_row_lengths(self):
        # arrange
        tree_1 = create_tree_from_list([1, 2, 3, 4, 5])
        tree_2 = create_tree_from_list([1, 2, 3, 4, 5, None, 6])

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertFalse(result)

    def test_are_equal(self):
        # arrange
        tree_1 = create_tree_from_list([1, None, 2, 3, 10])
        tree_2 = create_tree_from_list([1, None, 2, 3, 10])

        # act
        result = are_same(tree_1, tree_2)

        # assert
        self.assertTrue(result)