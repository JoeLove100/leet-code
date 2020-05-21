import unittest
from may_thirty_day_challenge.day_20 import get_kth_smallest_element, create_tree_from_list


class TestDay20(unittest.TestCase):

    def test_only_one_node(self):
        # act
        tree = create_tree_from_list([1])

        # act
        result = get_kth_smallest_element(tree, 1)

        # assert
        self.assertEqual(1, result)

    def test_left_nodes_only(self):
        # act
        tree = create_tree_from_list([20, 10, None, 2, None, 1, None])

        # act
        result = get_kth_smallest_element(tree, 3)

        # assert
        self.assertEqual(10, result)

    def test_right_nodes_only(self):
        # arrange
        tree = create_tree_from_list([2, None, 4, None, 9, None, 11])

        # act
        result = get_kth_smallest_element(tree, 2)

        # assert
        self.assertEqual(4, result)

    def test_get_smallest_element(self):
        # arrange
        tree = create_tree_from_list([3, 1, 4, None, 2])

        # act
        result = get_kth_smallest_element(tree, 1)

        # assert
        self.assertEqual(1, result)

    def test_unbalanced_tree(self):
        # arrange
        tree = create_tree_from_list([5, 3, 6, 2, 4, None, None, 1])

        # act
        result = get_kth_smallest_element(tree, 3)

        # assert
        self.assertEqual(3, result)
