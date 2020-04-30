import unittest
from thirty_day_challenge.day_30 import is_valid, create_tree_from_list


class TestDay30(unittest.TestCase):

    def test_is_valid_null_root(self):
        # arrange
        tree = None
        arr = [1, 0]

        # act
        result = is_valid(tree, arr)

        # assert
        self.assertFalse(result)

    def test_is_valid_empty_sequence(self):
        # arrange
        tree = create_tree_from_list([1])
        arr = []

        # act
        result = is_valid(tree, arr)

        # assert
        self.assertTrue(result)

    def test_is_valid_sequence_is_valid(self):
        # arrange
        tree = create_tree_from_list([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0, None, None])
        arr = [0, 1, 0, 1]

        # act
        result = is_valid(tree, arr)

        # assert
        self.assertTrue(result)

    def test_is_valid_sequence_is_not_valid(self):
        # arrange
        tree = create_tree_from_list([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
        arr = [0, 1, 1]

        # act
        result = is_valid(tree, arr)

        # assert
        self.assertFalse(result)

    def test_is_valid_shorter_sequence_than_tree(self):
        # arrange
        tree = create_tree_from_list([0, 1, None, 1, 1])
        arr = [0, 1]

        # act
        result = is_valid(tree, arr)

        # assert
        self.assertFalse(result)

    def test_is_valid_too_long(self):
        # arrange
        tree = create_tree_from_list([2, 9, 3, None, 1, None, 2, None, 8, None, None])
        arr = [2, 9, 1, 8, 0]

        # act
        result = is_valid(tree, arr)

        # assert
        self.assertFalse(result)
