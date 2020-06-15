import unittest
from june_thirty_day_challenge.day_15 import create_tree_from_list, find_in_bst


class TestDay15(unittest.TestCase):

    def test_null_root(self):
        # arrange
        root = None

        # act
        result = find_in_bst(root, 10)

        # assert
        self.assertEqual(None, result)

    def test_not_in_tree(self):
        # arrange
        root = create_tree_from_list([5, 3, 8, 2, 4])

        # act
        result = find_in_bst(root, 1)

        # assert
        self.assertEqual(None, result)

