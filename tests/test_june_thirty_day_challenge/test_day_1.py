import unittest
from june_thirty_day_challenge.day_1 import create_tree_from_list, invert_binary_tree, dfs


class TestDay1(unittest.TestCase):

    def test_invert_one_node(self):
        # arrange
        tree = create_tree_from_list([1])

        # act
        result = invert_binary_tree(tree)
        result = dfs(result)

        # assert
        self.assertSequenceEqual([1], result)

    def test_invert_two_levels(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3])

        # act
        result = invert_binary_tree(tree)
        result = dfs(result)

        # assert
        self.assertSequenceEqual([1, 3, 2], result)

    def test_invert_three_layers_full(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])

        # act
        result = invert_binary_tree(tree)
        result = dfs(result)

        # assert
        self.assertSequenceEqual([1, 3, 2, 7, 6, 5, 4], result)

    def test_invert_three_layers_unbalanced(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3, 4, None, None, 5])

        # act
        result = invert_binary_tree(tree)
        result = dfs(result)

        # assert
        self.assertSequenceEqual([1, 3, 2, 5, None, None, 4], result)

    def test_linear(self):
        # arrange
        tree = create_tree_from_list([1, 2, None, 3, None, 4, None])

        # act
        result = invert_binary_tree(tree)
        result = dfs(result)

        # assert
        self.assertSequenceEqual([1, None, 2, None, 3, None, 4], result)

    def test_non_complete(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3, None, 4, None, 5])

        # act
        result = invert_binary_tree(tree)
        result = dfs(result)

        # assert
        self.assertSequenceEqual([1, 3, 2, 5, None, 4], result)
