import unittest
from june_thirty_day_challenge.day_23 import get_node_count, create_tree_from_list


class TestDay23(unittest.TestCase):

    def test_null_root(self):
        # act
        root = None

        # arrange
        result = get_node_count(root)

        # assert
        self.assertEqual(0, result)

    def test_one_node(self):
        # act
        root = create_tree_from_list([2])

        # act
        result = get_node_count(root)

        # assert
        self.assertEqual(1, result)

    def test_full_tree(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])

        # act
        result = get_node_count(root)

        # assert
        self.assertEqual(7, result)

    def test_not_full_tree(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # act
        result = get_node_count(root)

        #
        self.assertEqual(10, result)
